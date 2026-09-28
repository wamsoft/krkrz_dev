//---------------------------------------------------------------------------
// proxyfs - 別名を参照するストレージメディア  "proxy://./<名前>"
//
//   global.ProxyStorageMap の辞書に
//     "./<名前(小文字)>" => 実際のファイル名 / octet / 辞書
//   を入れておくと、"proxy://./<名前>" でそれが読める。
//
//   旧 proxyfs (krkrtemplate/plugins_utf8/proxyfs) を **Win32 の IStream を
//   使わない形で作り直した**もの。 中身は全部 iTJSBinaryStream で書いてあるので
//   generic (SDL / CS) でも動く。
//
//   値の型で振る舞いが変わる:
//     文字列 … そのファイルを開く (別名参照)
//     octet  … その中身をファイルとして読む (読み取り専用)
//     辞書   … %[ file:, offset:, size: ] で「ファイルの一部」を読む
//     MemStreamHolder … メモリ上のファイル (読み書き可)
//     未登録 … 書き込みで開くと MemStreamHolder が作られて登録される
//---------------------------------------------------------------------------
#include "tp_stub.h"
#include "simplebinder.hpp"

#include <vector>
#include <memory>
#include <mutex>
#include <string.h>

#define BASENAME TJS_W("proxy")
#define PROXYMAP TJS_W("ProxyStorageMap")
#define MEMSTRHLD_CLASSID (0x4D6D5348) // 'MmSH'

//---------------------------------------------------------------------------
// 共有メモリバッファ
//   MemStreamHolder が持ち、そこから作ったストリームが共有する
//   (IStream の CreateStreamOnHGlobal + Clone と同じ関係)。
//---------------------------------------------------------------------------
typedef std::vector<tjs_uint8>   ProxyBuffer;
typedef std::shared_ptr<ProxyBuffer> ProxyBufferPtr;

//---------------------------------------------------------------------------
// iTJSBinaryStream の共通土台 (位置の管理と既定の振る舞い)
//---------------------------------------------------------------------------
class tProxyStreamBase : public iTJSBinaryStream
{
protected:
	tjs_uint64 Pos;
	tProxyStreamBase() : Pos(0) {}

public:
	virtual tjs_uint64 TJS_INTF_METHOD GetSize() = 0;

	tjs_uint64 TJS_INTF_METHOD Seek(tjs_int64 offset, tjs_int whence)
	{
		tjs_int64 np;
		switch(whence)
		{
		case TJS_BS_SEEK_SET: np = offset;                      break;
		case TJS_BS_SEEK_CUR: np = (tjs_int64)Pos + offset;     break;
		case TJS_BS_SEEK_END: np = (tjs_int64)GetSize() + offset; break;
		default:              return Pos;
		}
		const tjs_int64 size = (tjs_int64)GetSize();
		if(np < 0)    np = 0;
		if(np > size) np = size;
		Pos = (tjs_uint64)np;
		return Pos;
	}

	tjs_uint TJS_INTF_METHOD Write(const void * /*buffer*/, tjs_uint /*size*/) { return 0; }
	void     TJS_INTF_METHOD SetEndOfStorage() { TVPThrowExceptionMessage(TJS_W("proxyfs: read only stream")); }
};

//---------------------------------------------------------------------------
// メモリ上のファイル。 バッファは MemStreamHolder と共有する
//---------------------------------------------------------------------------
class tProxyMemStream : public tProxyStreamBase
{
	ProxyBufferPtr Buffer;
	bool CanWrite;

public:
	tProxyMemStream(const ProxyBufferPtr &buffer, tjs_uint32 flags)
		: Buffer(buffer), CanWrite(false)
	{
		const tjs_uint32 access = flags & TJS_BS_ACCESS_MASK;
		CanWrite = (access != TJS_BS_READ);
		if(access == TJS_BS_WRITE) Buffer->clear();          // 書き込みは切り詰めてから
		if(access == TJS_BS_APPEND) Pos = Buffer->size();
	}

	tjs_uint64 TJS_INTF_METHOD GetSize() { return Buffer->size(); }

	tjs_uint TJS_INTF_METHOD Read(void *buffer, tjs_uint size)
	{
		const tjs_uint64 rest = Buffer->size() - Pos;
		if((tjs_uint64)size > rest) size = (tjs_uint)rest;
		if(size) memcpy(buffer, &(*Buffer)[(size_t)Pos], size);
		Pos += size;
		return size;
	}

	tjs_uint TJS_INTF_METHOD Write(const void *buffer, tjs_uint size)
	{
		if(!CanWrite || size == 0) return 0;
		if(Pos + size > Buffer->size()) Buffer->resize((size_t)(Pos + size));
		memcpy(&(*Buffer)[(size_t)Pos], buffer, size);
		Pos += size;
		return size;
	}

	void TJS_INTF_METHOD SetEndOfStorage()
	{
		if(!CanWrite) TVPThrowExceptionMessage(TJS_W("proxyfs: read only stream"));
		Buffer->resize((size_t)Pos);
	}
};

//---------------------------------------------------------------------------
// octet をそのままファイルとして読む (読み取り専用)
//---------------------------------------------------------------------------
class tProxyOctetStream : public tProxyStreamBase
{
	tTJSVariantOctet *Octet;
	const tjs_uint8  *Data;
	tjs_uint          Size;

public:
	tProxyOctetStream(const tTJSVariant &v) : Octet(NULL), Data(NULL), Size(0)
	{
		Octet = v.AsOctet();                                  // AddRef される
		if(Octet)
		{
			Data = Octet->GetData();
			Size = Octet->GetLength();
		}
	}
	~tProxyOctetStream() { if(Octet) Octet->Release(); }

	bool IsValid() const { return Octet != NULL; }

	tjs_uint64 TJS_INTF_METHOD GetSize() { return Size; }

	tjs_uint TJS_INTF_METHOD Read(void *buffer, tjs_uint size)
	{
		const tjs_uint64 rest = Size - Pos;
		if((tjs_uint64)size > rest) size = (tjs_uint)rest;
		if(size) memcpy(buffer, Data + Pos, size);
		Pos += size;
		return size;
	}
};

//---------------------------------------------------------------------------
// ファイルの一部だけを見せる (読み取り専用)
//   %[ file: "...", offset: n, size: n ]
//   offset が負なら末尾から、size が負なら「末尾から -size-1 バイト手前まで」
//---------------------------------------------------------------------------
class tProxyRangeStream : public tProxyStreamBase
{
	iTJSBinaryStream *Stream;
	tjs_uint64 Offset, Length;

	static bool GetElement(tTJSVariantClosure &closure, const tjs_char *name, tTJSVariant &result)
	{
		return TJS_SUCCEEDED(closure.PropGet(0, name, NULL, &result, 0));
	}
	static ttstr GetString(tTJSVariantClosure &closure, const tjs_char *name)
	{
		tTJSVariant v;
		return (GetElement(closure, name, v) && v.Type() == tvtString) ? ttstr(v) : ttstr();
	}
	static tjs_int64 GetInteger(tTJSVariantClosure &closure, const tjs_char *name)
	{
		tTJSVariant v;
		if(GetElement(closure, name, v))
		{
			switch(v.Type())
			{
			case tvtInteger: case tvtReal: case tvtString: return v.AsInteger();
			default: break;
			}
		}
		return 0;
	}

public:
	tProxyRangeStream(const tTJSVariant &param) : Stream(NULL), Offset(0), Length(0)
	{
		if(param.Type() != tvtObject) return;
		tTJSVariantClosure closure(param.AsObjectClosureNoAddRef());
		ttstr name(GetString(closure, TJS_W("file")));
		if(name.IsEmpty()) return;

		Stream = TVPCreateStream(name, TJS_BS_READ);
		if(!Stream) return;

		const tjs_int64  size = (tjs_int64)Stream->GetSize();
		tjs_int64 ofs = GetInteger(closure, TJS_W("offset"));
		tjs_int64 siz = GetInteger(closure, TJS_W("size"));
		if(ofs < 0) ofs += size;

		tjs_int64 end = (siz < 0) ? (size + siz + 1) : (ofs + siz);
		// [0, size] へ収める
		if(ofs < 0)    ofs = 0;
		if(ofs > size) ofs = size;
		if(end < ofs)  end = ofs;
		if(end > size) end = size;

		Offset = (tjs_uint64)ofs;
		Length = (tjs_uint64)(end - ofs);
	}
	~tProxyRangeStream() { if(Stream) Stream->Destruct(); }

	bool IsValid() const { return Stream != NULL; }

	tjs_uint64 TJS_INTF_METHOD GetSize() { return Length; }

	tjs_uint TJS_INTF_METHOD Read(void *buffer, tjs_uint size)
	{
		if(!Stream) return 0;
		const tjs_uint64 rest = Length - Pos;
		if((tjs_uint64)size > rest) size = (tjs_uint)rest;
		if(!size) return 0;
		Stream->Seek((tjs_int64)(Offset + Pos), TJS_BS_SEEK_SET);
		const tjs_uint read = Stream->Read(buffer, size);
		Pos += read;
		return read;
	}
};

//---------------------------------------------------------------------------
// MemStreamHolder : メモリ上のファイルを表す TJS オブジェクト
//   ProxyStorageMap["./名前"] に入って、バイト列として添字アクセスできる。
//   関数として呼ぶと octet が返る。
//---------------------------------------------------------------------------
class MemStreamHolder : public tTJSDispatch
{
	ProxyBufferPtr Buffer;

public:
	MemStreamHolder() : tTJSDispatch(), Buffer(new ProxyBuffer()) {}

	bool Open(const tjs_uint8 *data = NULL, tjs_uint size = 0)
	{
		Buffer->assign(data, data + (data ? size : 0));
		return true;
	}

	iTJSBinaryStream *CreateStream(tjs_uint32 flags)
	{
		return new tProxyMemStream(Buffer, flags);
	}

	static MemStreamHolder *GetInstance(iTJSDispatch2 *obj)
	{
		if(!obj) return NULL;
		iTJSNativeInstance *ni = NULL;
		if(TJS_FAILED(obj->NativeInstanceSupport(TJS_NIS_GETINSTANCE, MEMSTRHLD_CLASSID, &ni)))
			return NULL;
		return reinterpret_cast<MemStreamHolder *>(ni);
	}

private:
	tjs_error ToOctet(tTJSVariant *result)
	{
		if(result)
		{
			if(Buffer->empty()) *result = tTJSVariant((const tjs_uint8 *)"", 0);
			else                *result = tTJSVariant(&(*Buffer)[0], (tjs_int)Buffer->size());
		}
		return TJS_S_OK;
	}
	tjs_error SetOctet(const tTJSVariant *param)
	{
		if(param->Type() != tvtOctet) return TJS_E_INVALIDPARAM;
		tTJSVariantOctet *oct = param->AsOctetNoAddRef();
		if(oct)
		{
			const tjs_uint len = oct->GetLength();
			Buffer->assign(oct->GetData(), oct->GetData() + len);
		}
		return TJS_S_OK;
	}
	// 数値だけの文字列なら添字として扱う (辞書風アクセス)
	static bool AsIndex(const tjs_char *name, tjs_int &index)
	{
		if(!name || !*name) return false;
		tjs_int v = 0;
		for(const tjs_char *p = name; *p; p++)
		{
			if(*p < TJS_W('0') || *p > TJS_W('9')) return false;
			v = v * 10 + (tjs_int)(*p - TJS_W('0'));
		}
		index = v;
		return true;
	}

public:
	// --- iTJSDispatch2 (必要なところだけ) ---
	tjs_error TJS_INTF_METHOD FuncCall(tjs_uint32 /*flag*/, const tjs_char *membername,
		tjs_uint32 * /*hint*/, tTJSVariant *result, tjs_int /*numparams*/,
		tTJSVariant ** /*param*/, iTJSDispatch2 * /*objthis*/)
	{
		if(membername) return TJS_E_MEMBERNOTFOUND;
		return ToOctet(result);                              // 関数呼び出しで octet
	}

	tjs_error TJS_INTF_METHOD PropGet(tjs_uint32 /*flag*/, const tjs_char *membername,
		tjs_uint32 * /*hint*/, tTJSVariant *result, iTJSDispatch2 * /*objthis*/)
	{
		if(!membername) return ToOctet(result);
		if(!TJS_strcmp(membername, TJS_W("count")) || !TJS_strcmp(membername, TJS_W("length")))
		{
			if(result) *result = (tjs_int)Buffer->size();
			return TJS_S_OK;
		}
		tjs_int index;
		if(AsIndex(membername, index)) return PropGetByNum(0, index, result, NULL);
		return TJS_E_MEMBERNOTFOUND;
	}

	tjs_error TJS_INTF_METHOD PropGetByNum(tjs_uint32 /*flag*/, tjs_int num,
		tTJSVariant *result, iTJSDispatch2 * /*objthis*/)
	{
		if(num < 0 || (size_t)num >= Buffer->size()) return TJS_E_MEMBERNOTFOUND;
		if(result) *result = (tjs_int)(*Buffer)[(size_t)num];
		return TJS_S_OK;
	}

	tjs_error TJS_INTF_METHOD PropSet(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 * /*hint*/, const tTJSVariant *param, iTJSDispatch2 * /*objthis*/)
	{
		if(!membername) return SetOctet(param);
		tjs_int index;
		if(AsIndex(membername, index)) return PropSetByNum(flag, index, param, NULL);
		return TJS_E_MEMBERNOTFOUND;
	}

	tjs_error TJS_INTF_METHOD PropSetByNum(tjs_uint32 flag, tjs_int num,
		const tTJSVariant *param, iTJSDispatch2 * /*objthis*/)
	{
		if(num < 0) return TJS_E_MEMBERNOTFOUND;
		if((size_t)num >= Buffer->size())
		{
			if(!(flag & TJS_MEMBERENSURE)) return TJS_E_MEMBERNOTFOUND;
			Buffer->resize((size_t)num + 1);
		}
		(*Buffer)[(size_t)num] = (tjs_uint8)(tjs_int)*param;
		return TJS_S_OK;
	}

	tjs_error TJS_INTF_METHOD GetCount(tjs_int *result, const tjs_char *membername,
		tjs_uint32 * /*hint*/, iTJSDispatch2 * /*objthis*/)
	{
		if(membername) return TJS_E_MEMBERNOTFOUND;
		if(result) *result = (tjs_int)Buffer->size();
		return TJS_S_OK;
	}

	tjs_error TJS_INTF_METHOD IsInstanceOf(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, const tjs_char *classname, iTJSDispatch2 *objthis)
	{
		if(!membername && classname && !TJS_strcmp(classname, TJS_W("MemStreamHolder")))
			return TJS_S_TRUE;
		return tTJSDispatch::IsInstanceOf(flag, membername, hint, classname, objthis);
	}

	tjs_error TJS_INTF_METHOD NativeInstanceSupport(tjs_uint32 flag, tjs_int32 classid,
		iTJSNativeInstance **pointer)
	{
		if(classid != MEMSTRHLD_CLASSID) return TJS_E_NATIVECLASSCRASH;
		if(flag == TJS_NIS_GETINSTANCE)
		{
			if(pointer) *pointer = reinterpret_cast<iTJSNativeInstance *>(this);
			return TJS_S_OK;
		}
		return TJS_E_NOTIMPL;
	}
};

//---------------------------------------------------------------------------
// ロック付きの辞書
//   ProxyStorageMap はスクリプト側から書かれ、メディア側 (読み込みスレッドを
//   含む) から読まれるので、両側を同じ錠で囲う。
//   ⚠ 旧実装は CRITICAL_SECTION を直接使っていた。 ここは std::recursive_mutex。
//---------------------------------------------------------------------------
class tProxyGuardDict : public tTJSDispatch
{
	iTJSDispatch2 *Dict;
	std::recursive_mutex Mutex;

	void BeforeDestruction()
	{
		if(Dict) Dict->Release();
		Dict = NULL;
	}

public:
	tProxyGuardDict() : tTJSDispatch(), Dict(TJSCreateDictionaryObject()) {}

	// --- 錠をかけて中の辞書へ流す ---
	tjs_error TJS_INTF_METHOD PropGet(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, tTJSVariant *result, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->PropGet(flag, membername, hint, result, Dict);
	}
	tjs_error TJS_INTF_METHOD PropGetByNum(tjs_uint32 flag, tjs_int num,
		tTJSVariant *result, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->PropGetByNum(flag, num, result, Dict);
	}
	tjs_error TJS_INTF_METHOD PropSet(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, const tTJSVariant *param, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->PropSet(flag, membername, hint, param, Dict);
	}
	tjs_error TJS_INTF_METHOD PropSetByNum(tjs_uint32 flag, tjs_int num,
		const tTJSVariant *param, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->PropSetByNum(flag, num, param, Dict);
	}
	tjs_error TJS_INTF_METHOD PropSetByVS(tjs_uint32 flag, tTJSVariantString *membername,
		const tTJSVariant *param, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->PropSetByVS(flag, membername, param, Dict);
	}
	tjs_error TJS_INTF_METHOD DeleteMember(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->DeleteMember(flag, membername, hint, Dict);
	}
	tjs_error TJS_INTF_METHOD DeleteMemberByNum(tjs_uint32 flag, tjs_int num,
		iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->DeleteMemberByNum(flag, num, Dict);
	}
	tjs_error TJS_INTF_METHOD EnumMembers(tjs_uint32 flag,
		tTJSVariantClosure *callback, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->EnumMembers(flag, callback, Dict);
	}

	// --- 錠なしで流すだけ (辞書の持つメソッドや個数取得) ---
	tjs_error TJS_INTF_METHOD FuncCall(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, tTJSVariant *result, tjs_int numparams,
		tTJSVariant **param, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->FuncCall(flag, membername, hint, result, numparams, param, Dict);
	}
	tjs_error TJS_INTF_METHOD GetCount(tjs_int *result, const tjs_char *membername,
		tjs_uint32 *hint, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->GetCount(result, membername, hint, Dict);
	}
	tjs_error TJS_INTF_METHOD IsValid(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->IsValid(flag, membername, hint, Dict);
	}
	tjs_error TJS_INTF_METHOD Operation(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, tTJSVariant *result, const tTJSVariant *param,
		iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->Operation(flag, membername, hint, result, param, Dict);
	}
	tjs_error TJS_INTF_METHOD IsInstanceOf(tjs_uint32 flag, const tjs_char *membername,
		tjs_uint32 *hint, const tjs_char *classname, iTJSDispatch2 * /*objthis*/)
	{
		std::lock_guard<std::recursive_mutex> lock(Mutex);
		return Dict->IsInstanceOf(flag, membername, hint, classname, Dict);
	}
};

//---------------------------------------------------------------------------
// GetListAt 用: 辞書のキーを列挙して、指定フォルダ直下のものだけ拾う
//---------------------------------------------------------------------------
class tProxyLister : public tTJSDispatch
{
	ttstr Search;
	iTVPStorageLister *Lister;

public:
	// ローカル変数としてしか使わないので参照カウントは潰しておく
	tjs_uint TJS_INTF_METHOD AddRef(void)  { return 1; }
	tjs_uint TJS_INTF_METHOD Release(void) { return 0; }

	tProxyLister(const ttstr &name, iTVPStorageLister *lister)
		: Search(name), Lister(lister) { Search.ToLowerCase(); }

	tjs_error TJS_INTF_METHOD FuncCall(tjs_uint32 /*flag*/, const tjs_char * /*membername*/,
		tjs_uint32 * /*hint*/, tTJSVariant *result, tjs_int numparams,
		tTJSVariant **param, iTJSDispatch2 * /*objthis*/)
	{
		if(numparams > 1)
		{
			const tTVInteger flag = param[1]->AsInteger();
			if(!(flag & TJS_HIDDENMEMBER))
			{
				ttstr name(*param[0]);
				if(TVPExtractStoragePath(name) == Search)
					Lister->Add(TVPExtractStorageName(name));
			}
		}
		if(result) *result = true;
		return TJS_S_OK;
	}
};

//---------------------------------------------------------------------------
// ProxyStorage : ストレージメディア本体
//---------------------------------------------------------------------------
class ProxyStorage : public iTVPStorageMedia
{
	tTJSVariant Map;
	tjs_uint    RefCount;
	static ProxyStorage *Instance;

	ProxyStorage() : RefCount(1)
	{
		iTJSDispatch2 *dic = new tProxyGuardDict();
		Map = tTJSVariant(dic, dic);
		TVPRegisterGlobalObject(PROXYMAP, dic);
		dic->Release();
	}
	~ProxyStorage() { TVPRemoveGlobalObject(PROXYMAP); }

	bool GetProxy(ttstr name, tTJSVariant *result = NULL)
	{
		iTJSDispatch2 *obj = Map.AsObjectNoAddRef();
		if(!obj) return false;
		tTJSVariant conv;
		name.ToLowerCase();
		if(TJS_FAILED(obj->PropGet(0, name.c_str(), name.GetHint(), &conv, obj))) return false;
		if(result) *result = conv;
		switch(conv.Type())
		{
		case tvtString: case tvtObject: case tvtOctet: return true;
		default: return false;
		}
	}
	bool SetProxy(ttstr name, const tTJSVariant &set)
	{
		iTJSDispatch2 *obj = Map.AsObjectNoAddRef();
		if(!obj) return false;
		name.ToLowerCase();
		// ⚠ 新しい名前を作るので TJS_MEMBERENSURE が要る (0 だと未登録名で失敗する)
		return TJS_SUCCEEDED(obj->PropSet(TJS_MEMBERENSURE, name.c_str(), name.GetHint(), &set, obj));
	}

	// 未登録の名前を書き込みで開いたとき: メモリ上のファイルを作って登録する
	iTJSBinaryStream *CreateMemFile(const ttstr &name, tjs_uint32 flags,
		const tjs_uint8 *data = NULL, tjs_uint size = 0)
	{
		MemStreamHolder *msh = new MemStreamHolder();
		msh->Open(data, size);
		if(!SetProxy(name, tTJSVariant(msh, msh))) { msh->Release(); return NULL; }
		iTJSBinaryStream *ret = msh->CreateStream(flags);
		msh->Release();
		return ret;
	}

public:
	// --- iTVPStorageMedia ---
	void TJS_INTF_METHOD AddRef()  { RefCount++; }
	void TJS_INTF_METHOD Release() { if(RefCount == 1) delete this; else RefCount--; }

	void TJS_INTF_METHOD GetName(ttstr &name) { name = BASENAME; }
	void TJS_INTF_METHOD NormalizeDomainName(ttstr & /*name*/) {}
	void TJS_INTF_METHOD NormalizePathName  (ttstr & /*name*/) {}

	bool TJS_INTF_METHOD CheckExistentStorage(const ttstr &name) { return GetProxy(name); }

	iTJSBinaryStream * TJS_INTF_METHOD Open(const ttstr &name, tjs_uint32 flags)
	{
		const tjs_char *errmes = TJS_W("cannot open proxyfile:%1");
		const tjs_uint32 access = flags & TJS_BS_ACCESS_MASK;
		iTJSBinaryStream *stream = NULL;
		tTJSVariant conv;

		if(GetProxy(name, &conv))
		{
			switch(conv.Type())
			{
			case tvtString:
				// 別名参照: そのまま本体のストレージへ投げる
				stream = TVPCreateStream(ttstr(conv), flags);
				break;

			case tvtObject: {
				iTJSDispatch2 *obj = conv.AsObjectNoAddRef();
				MemStreamHolder *msh = MemStreamHolder::GetInstance(obj);
				if(msh)
				{
					stream = msh->CreateStream(flags);
				}
				else if(obj)
				{
					if(access == TJS_BS_READ)
					{
						tProxyRangeStream *rs = new tProxyRangeStream(conv);
						if(rs->IsValid()) stream = rs;
						else              delete rs;
					}
					else errmes = TJS_W("write mode not supported:%1");
				}
				else stream = CreateMemFile(name, flags);
			}	break;

			case tvtOctet:
				if(access == TJS_BS_READ)
				{
					tProxyOctetStream *os = new tProxyOctetStream(conv);
					if(os->IsValid()) stream = os;
					else              delete os;
				}
				else
				{
					tTJSVariantOctet *oct = conv.AsOctetNoAddRef();
					if(oct) stream = CreateMemFile(name, flags, oct->GetData(), oct->GetLength());
				}
				break;

			default: break;
			}
		}
		else if(access == TJS_BS_WRITE || access == TJS_BS_APPEND)
		{
			// 初回。 メモリ上のファイルを作る
			if(conv.Type() == tvtVoid) stream = CreateMemFile(name, flags);
		}

		if(stream) return stream;

		conv.Clear();
		TVPThrowExceptionMessage(errmes, name);
		return NULL;
	}

	void TJS_INTF_METHOD GetListAt(const ttstr &name, iTVPStorageLister *lister)
	{
		iTJSDispatch2 *obj = Map.AsObjectNoAddRef();
		if(!obj) return;
		tProxyLister caller(name, lister);
		tTJSVariantClosure closure(&caller);
		obj->EnumMembers(TJS_IGNOREPROP | TJS_ENUM_NO_VALUE, &closure, obj);
	}

	void TJS_INTF_METHOD GetLocallyAccessibleName(ttstr &name)
	{
		tTJSVariant conv;
		if(GetProxy(name, &conv) && conv.Type() == tvtString)
			// ⚠ 正規化してから渡すこと。 素の "foo.bin" のままだと
			//   「対応していないメディアタイプ」で落ちる
			name = TVPGetLocallyAccessibleName(TVPNormalizeStorageName(ttstr(conv)));
		else
			name = ttstr();
	}

	// --- 登録 / 解除 ---
	static bool Install()
	{
		if(Instance) return false;
		Instance = new ProxyStorage();
		TVPRegisterStorageMedia(Instance);
		return true;
	}
	static void Uninstall()
	{
		if(!Instance) return;
		TVPUnregisterStorageMedia(Instance);
		Instance->Release();
		Instance = NULL;
	}
};
ProxyStorage *ProxyStorage::Instance = NULL;

//---------------------------------------------------------------------------
bool ONV2LINK()   { return ProxyStorage::Install(); }
bool ONV2UNLINK() { ProxyStorage::Uninstall(); return true; }
//---------------------------------------------------------------------------
