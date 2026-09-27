//---------------------------------------------------------------------------
// pemachinetype - PE ヘッダの Machine 種別を読む
//
//   Plugins.fetchMachineType(ファイル名) -> IMAGE_FILE_MACHINE_* の値
//                                           (PE でなければ -1)
//
//   旧 PackinOne の pemachinetype_main.cpp を個別プラグインとして起こし直したもの。
//   ⚠ 旧実装は Win32 の IStream (TVPCreateIStream) を使っていて generic で動かず、
//     さらにストリームを Release していなかった。 ここでは本体のストレージ
//     ストリーム (TVPCreateStream / iTJSBinaryStream) に置き換えてある。
//---------------------------------------------------------------------------
#include "tp_stub.h"
#include "simplebinder.hpp"

#include <memory>
#include <string.h>

//---------------------------------------------------------------------------
// ストリームの後始末 (iTJSBinaryStream は delete ではなく Destruct)
//---------------------------------------------------------------------------
struct StreamDeleter
{
	void operator()(iTJSBinaryStream *s) const { if(s) s->Destruct(); }
};
typedef std::unique_ptr<iTJSBinaryStream, StreamDeleter> StreamPtr;

//---------------------------------------------------------------------------
// リトルエンディアンで読む (PE ヘッダの並びは常にリトルエンディアン)
//---------------------------------------------------------------------------
static inline tjs_uint32 ReadLE32(const tjs_uint8 *p)
{
	return  (tjs_uint32)p[0]        | ((tjs_uint32)p[1] <<  8) |
	       ((tjs_uint32)p[2] << 16) | ((tjs_uint32)p[3] << 24);
}
static inline tjs_uint16 ReadLE16(const tjs_uint8 *p)
{
	return (tjs_uint16)((tjs_uint32)p[0] | ((tjs_uint32)p[1] << 8));
}

//---------------------------------------------------------------------------
static bool ReadExact(iTJSBinaryStream *s, void *buf, tjs_uint size)
{
	return s->Read(buf, size) == size;
}

//---------------------------------------------------------------------------
static tjs_error FetchMachineType(tTJSVariant *result, tTJSVariant *file)
{
	if(result) *result = (tjs_int)-1;
	if(!file || file->Type() != tvtString) return TJS_S_OK;

	StreamPtr stream(TVPCreateStream(ttstr(*file), TJS_BS_READ));
	if(!stream) return TJS_S_OK;

	// IMAGE_DOS_HEADER::e_lfanew (0x3c) が PE シグネチャの位置を指す
	tjs_uint8 buf[6] = {0};
	if(stream->Seek(0x3c, TJS_BS_SEEK_SET) != 0x3c) return TJS_S_OK;
	if(!ReadExact(stream.get(), buf, 4)) return TJS_S_OK;

	const tjs_uint64 peoffset = ReadLE32(buf);
	if(stream->Seek((tjs_int64)peoffset, TJS_BS_SEEK_SET) != peoffset) return TJS_S_OK;
	if(!ReadExact(stream.get(), buf, 6)) return TJS_S_OK;

	// "PE\0\0" + IMAGE_FILE_HEADER::Machine
	static const tjs_uint8 pe[4] = { 'P', 'E', 0, 0 };
	if(memcmp(pe, buf, sizeof(pe)) != 0) return TJS_S_OK;

	if(result) *result = (tjs_int)ReadLE16(buf + 4);
	return TJS_S_OK;
}

//---------------------------------------------------------------------------
bool PEMachineTypeEntry(bool link)
{
	return SimpleBinder::BindUtil(TJS_W("Plugins"), link)
		.Function(TJS_W("fetchMachineType"), &FetchMachineType)
		.IsValid();
}

bool ONV2LINK()   { return PEMachineTypeEntry(true);  }
bool ONV2UNLINK() { return PEMachineTypeEntry(false); }
//---------------------------------------------------------------------------
