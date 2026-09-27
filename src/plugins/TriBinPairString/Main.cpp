//---------------------------------------------------------------------------
// TriBinPairString - バイナリ/数値/文字列を「見た目が壊れない」全角文字列へ
//                    可逆エンコードする
//
//   Scripts.encodeTBPS(値 [, 厳密]) / Scripts.decodeTBPS(文字列)
//
//   旧 PackinOne の TriBinPairString.cpp を個別プラグインとして起こし直したもの。
//   中身は純粋な計算だけで Win32 依存は無い (旧実装の <windows.h> は不要)。
//---------------------------------------------------------------------------
#include "tp_stub.h"
#include "simplebinder.hpp"

#include <vector>
typedef std::vector<tjs_char>  WchrVec;
typedef std::vector<tjs_uint8> ByteVec;

////////////////////////////////////////////////////////////////
/**
 * 使用するコードページ
	U+4E00～U+4FFF :  2page - 文字列terminate用
	U+5000～U+5FFF : 16page * 文字列 偶数
	U+6000～U+6FFF : 16page * 文字列 奇数

	U+2F00 : void
	U+2F01 : null
	U+2F02 : ""
	U+2F03 : <% %>
	U+2F04 : 64bit integer
	U+2F05 : 64bit double
	
	U+3400～U+3DFF : 10page - 数値 即値／場合分け用
							 { 34:正8bit即値, 35:負8bit即値, 36:正32bit, 37:負32bit, 38:正56bit, 39:負56bit, 3A:int64, 3B:float, 3C:double, 3D:reserved }
	U+3E00～U+3FFF :  2page - 数値 terminate用
	U+7000～U+7FFF : 16page * 数値 偶数
	U+8000～U+8FFF : 16page * 数値 奇数

	U+AE00～U+AFFF :  2page - octet terminate用
	U+B000～U+BFFF : 16page * octet 偶数
	U+C000～U+CFFF : 16page * octet 奇数

	U+F900～U+F9FF :  1page : 型決定用

	[FEATURE] Object向け
	U+9000～U+9DFF : 14page : 長さクイック指定
	U+9Dxx         :  1page : 長さ32bit
	U+9F00                  : 長さ64bit


 * その他コードページメモ：
	U+4000～U+4CFF : 13page

kor:
	U+AC00～U+ADFF :  2page
	U+D000～U+D6FF :  7page

 */

// マーカー／定数など
enum {
	ENCTYPE_VOID   = 0x2F00,
	ENCTYPE_NULL   = 0x2F01,
	ENCTYPE_EMPSTR = 0x2F02,
	ENCTYPE_EMPOCT = 0x2F03,
	ENCTYPE_INT64  = 0x2F04,
	ENCTYPE_DOUBLE = 0x2F05,

	NUMBER_BASE   = 0x3400, // ~ +5
	NUMBER_INT64  = 0x3A00,
	NUMBER_FLOAT  = 0x3B00,
	NUMBER_DOUBLE = 0x3C00,
	NUMBER_MASK   = 0x3F00,

	MARK_ENCTYPE = 0x2000,
	MARK_NUMBER  = 0x3000,
	MARK_STRING  = 0x5000,
	MARK_STRTERM = 0x4000,
	MARK_OCTET   = 0xB000,
	MARK_OCTTERM = 0xA000,
};
static const tjs_char StringMarks[4] = { 0x5000, 0x6000, 0x4E00, 0x4F00 };
static const tjs_char NumberMarks[4] = { 0x7000, 0x8000, 0x3E00, 0x3F00 };
static const tjs_char  OctetMarks[4] = { 0xB000, 0xC000, 0xAE00, 0xAF00 };
static const tjs_char DoubleMark []  = { ENCTYPE_DOUBLE, 0 };
static const tjs_char  Int64Mark []  = { ENCTYPE_INT64,  0 };
static const tjs_char EmpStrMark []  = { ENCTYPE_EMPSTR, 0 };
static const tjs_char EmpOctMark []  = { ENCTYPE_EMPOCT, 0 };
static const tjs_char   VoidMark []  = { ENCTYPE_VOID,   0 };

////////////////////////////////////////////////////////////////
/**
 *
 * バイナリ列を wchar_t 文字列に詰め込む
 *
 * Aa Bb Cc の 3byte単位で U+?BAa U+?bCc の 2wordに詰め込む(?の部分はmarks[0]/marks[1]が利用される）
 * 末尾の3byte未満の余り部分は "U+4EAa U+4FBb" "U+4FAa" のようにmarks[2]/marks[3]ページが利用される
 * 
 */

// 必要な word 数計算用
#define BIN2WIDE_LENGTH(sz) ((sz) - ((sz)/3) + 1)
#define WIDE2BIN_LENGTH(len) (((len+1)/2)*3) // 最大値なので注意

/**
 * @param hash   ソースデータ
 * @param length hashの長さ
 * @param result \0で終わる結果出力先（サイズはHASH2WIDE_LENGTHマクロかNULLを渡して計算する） 
 * @return 出力したワード数，もしくは(result=NULLの場合)必要なワード数
 */
template <typename SRC, typename DST>
static inline size_t BinaryToWideString(const SRC *hash, size_t length, DST *result, const DST *marks) {
	if (!result) return BIN2WIDE_LENGTH(length);
	DST page = 0;
	DST *w = result;
	int pos = 0;
	for (const int max = length-3; pos <= max; pos+=3) {
		DST a = (DST)hash[pos];
		DST b = (DST)hash[pos+1];
		DST c = (DST)hash[pos+2];
		*w++ = a | ((b << 4) & 0x0F00) | marks[0];
		*w++ = c | ((b << 8) & 0x0F00) | marks[1];
	}
	switch (length % 3)
	{
	case 2: {
		DST a = (DST)hash[pos];
		DST b = (DST)hash[pos+1];
		*w++ = a | marks[2];
		*w++ = b | marks[3];
	} break;
	case 1: {
		DST a = (DST)hash[pos];
		*w++ = a | marks[3];
	} break;
	case 0: break;
	}
	*w++ = 0;
	return (size_t)(w - result);
}

/**
 * @param result 結果出力先
 * @param wstr   文字列
 * @param length 文字列長さ（計算用／通常時は不要）
 * @return 出力したバイト数，もしくは必要なバイト数
 */
template <typename DST, typename SRC>
static inline size_t BinaryFromWideString(DST *result, const SRC *marks, const SRC *wstr, size_t length = 0) {
	if (!result && (!wstr || length > 0)) return WIDE2BIN_LENGTH(length);
	const SRC ordr = 0xF000;
	const SRC high = 0x0F00;
	const SRC mask = 0xFF00;
	const SRC byte = 0x00FF;
	size_t r = 0;
	for (SRC page = 0x5000; true; wstr+=2) {
		const SRC ch1 = wstr[0];
		if (!ch1) return r;
		const SRC ch2 = wstr[1];
		const SRC hb = ch1 & mask;
		if (hb == marks[2]) {
			++r;
			if (result) *result++ = (DST)(ch1 & byte);
			if ((ch2 & mask) == marks[3]) {
				++r;
				if (result) *result++ = (DST)(ch2 & byte);
			}
			return r;
		} else if (hb == marks[3]) {
			++r;
			if (result) *result++ = (DST)(ch1 & byte);
			return r;
		} else if (((ch1 & ordr) != marks[0]) || ((ch2 & ordr) != marks[1])) return r;
		r += 3;
		if (result) {
			*result++ = (DST)(ch1 & byte);
			*result++ = (DST)(((ch1 & high) >> 4) | (ch2 & high) >> 8);
			*result++ = (DST)(ch2 & byte);
		}
		page = ((page-0x4000) & 0x3000) + 0x5000; // 0x5000 ～ 0x8000
	}
}

////////////////////////////////////////////////////////////////
// 文字コード変換用utils
static bool ConvWStrToUTF8(const tjs_char *src, ByteVec &vec) {
	const tjs_int len = TVPWideCharToUtf8String(src, nullptr);
	if (len <= 0) return false;
	vec.resize(len);
	return TVPWideCharToUtf8String(src, (char*)&vec.front()) > 0;
}
static bool ConvUTF8ToWStr(const char *src, ttstr &dst) {
	const tjs_int len = TVPUtf8ToWideCharString(src, nullptr);
	if (len < 0) return false;
	else if (!len) {
		dst.Clear();
		return true;
	}
	TVPUtf8ToWideCharString(src, dst.AllocBuffer(len));
	dst.FixLen();
	return true;
}

////////////////////////////////////////////////////////////////
// エンコード

// 汎用処理
static tjs_int encode(WchrVec &vec, const tjs_uint8 *data, tjs_int length, const tjs_char *table) {
	size_t size = length > 0 ? BinaryToWideString((const tjs_uint8*)nullptr, (size_t)length, (tjs_char*)nullptr, table) : 0;
	vec.resize(size);
	if (size > 0) BinaryToWideString(data, length, &vec.front(), table);
	return (tjs_int)size;
}
// number エンコード
static void encode_number(ttstr &dst, const tjs_char *head, const tjs_uint8 *data, tjs_int length) {
	WchrVec vec;
	if (encode(vec, data, length, NumberMarks)) {
		dst = ttstr(head);
		dst += &vec.front();
	} else dst.Clear();
}
// int64/double/float特殊
static void encode_number(ttstr &dst, const tjs_uint8 *data, tjs_int length, tjs_char mark) {
	WchrVec vec;
	if (encode(vec, data, length, NumberMarks)) {
		vec[0] &= 0x00FF;
		vec[0] |= mark;
		dst = &vec.front();
	} else dst.Clear();
}
// int可変長エンコード
static void encode_number_ex(ttstr &dst, tTVInteger n) {
	const tTVInteger mask = 0xFF00000000000000uLL;
	const tTVInteger expr = (n >= 0) ? (n & mask) : ((-n)&mask);
	if (!expr) {
		// 56bit未満
		tjs_char quick[2] = { NUMBER_BASE, 0 };
		if (n < 0) {
			// 負数フラグ
			n = -n;
			quick[0] |= 0x0100;
		}
		quick[0] |= (n & 255);
		if (n < 256) {
			// 1文字 (-256～+255)
			dst = ttstr(quick);
			return;
		}
		if ((n >> 32) == 0) {
			// 3文字(32bit)
			quick[0] += 0x0200;
			tjs_uint8 tmp[3] = { (n>>8)&255, (n>>16)&255, (n>>24)&255 };
			encode_number(dst, quick, tmp, sizeof(tmp));
			return;
		}
		if ((n >> 56) == 0) {
			// 5文字(56bit)
			quick[0] += 0x0400;
			tjs_uint8 tmp[6] = { (n>>8)&255, (n>>16)&255, (n>>24)&255, (n>>32)&255, (n>>40)&255, (n>>48)&255 };
			encode_number(dst, quick, tmp, sizeof(tmp));
			return;
		}
	}
	// 64bit
	tjs_uint8 tmp[9] = {n&0xFF, 0, (n>>8)&0xFF, (n>>16)&0xFF, (n>>24)&0xFF, (n>>32)&0xFF, (n>>40)&0xFF, (n>>48)&0xFF, (n>>56)&0xFF };
	encode_number(dst, tmp, sizeof(tmp), NUMBER_INT64);
}
// realエンコード
static void encode_double(ttstr &dst, tTVReal real) {
	tTVInteger n = *reinterpret_cast<tTVInteger*>(&real);
	tjs_uint8 tmp[9] = {n&0xFF, 0, (n>>8)&0xFF, (n>>16)&0xFF, (n>>24)&0xFF, (n>>32)&0xFF, (n>>40)&0xFF, (n>>48)&0xFF, (n>>56)&0xFF };
	encode_number(dst, tmp, sizeof(tmp), NUMBER_DOUBLE);
}
// 文字列エンコード
static void encode_string(ttstr &dst, const ttstr &src, bool strict) {
	dst.Clear();
	if (src.IsEmpty()) {
		if (strict) dst = ttstr(EmpStrMark);
		return;
	}
	const tjs_int len = TVPWideCharToUtf8String(src.c_str(), nullptr);
	if (len > 0) {
		ByteVec tmp;
		tmp.resize(len);
		TVPWideCharToUtf8String(src.c_str(), (char*)&tmp.front());
		WchrVec vec;
		const tjs_int size = encode(vec, &tmp.front(), len, StringMarks);
		if (size > 1) dst = ttstr(&vec.front(), (int)size-1);
	}
}
// octetエンコード
static void encode_octet(ttstr &dst, const tTJSVariantOctet * oct, bool strict) {
	dst.Clear();
	const tjs_uint len = oct->GetLength();
	if (len == 0) dst = ttstr(EmpOctMark);
	else {
		WchrVec vec;
		tjs_int size = encode(vec, oct->GetData(), (tjs_int)len, OctetMarks);
		if (size > 1) dst = ttstr(&vec.front(), (int)size-1);
	}
}

// 型判定エンコード
static bool encode_select(ttstr &dst, const tTJSVariant &src, bool strict) {
	switch (src.Type()) {
	default: return false;
	case tvtVoid:
		if (strict) dst = VoidMark;
		else return false;
		break;
//	case tvtObject:  encode_object   (dst, src.AsObjectClosureNoAddRef(), strict); break; // todo object
	case tvtString:  encode_string   (dst, ttstr(src), strict);            break;
	case tvtOctet:   encode_octet    (dst, src.AsOctetNoAddRef(), strict); break;
	case tvtInteger: encode_number_ex(dst, src.AsInteger());               break;
	case tvtReal:    encode_double   (dst, src.AsReal());                  break;
	}
	return true;
}

//--------------------------------------------------------------
// TJSエンコードインターフェース
static tjs_error encodeTriBinPairString(tTJSVariant *result, tTJSVariant *src, tjs_int optnum, tTJSVariant **optargs) {
	if (result) {
		ttstr dst;
		const bool strict = optnum > 0 && optargs[0]->operator bool();
		if (encode_select(dst, *src, strict)) *result = dst;
		else result->Clear();
	}
	return TJS_S_OK;
}

////////////////////////////////////////////////////////////////
// デコード

// 汎用
static tjs_int decode(ByteVec &vec, const tjs_char *src, const tjs_int len, const tjs_char *table) {
	size_t size = len > 0 ? BinaryFromWideString((tjs_uint8*)nullptr, table, (const tjs_char*)nullptr, (size_t)len) : 0;
	vec.resize(size);
	if (size > 0) {
		size = BinaryFromWideString(&vec.front(), table, src);
		vec.resize(size);
		// [MEMO]使用word数を返す必要があるのでToWideStr
		return (tjs_int)BinaryToWideString((const tjs_uint8*)nullptr, size, (tjs_char*)nullptr, table) - 1;
	}
	return 0;
}
// 文字列
static tjs_int decode_string(tTJSVariant &result, const tjs_char *str, const tjs_int len) {
	ByteVec vec;
	const tjs_int n = decode(vec, str, len, StringMarks);
	vec.push_back(0);
	ttstr dst;
	if (ConvUTF8ToWStr((const char*)&vec.front(), dst)) result = dst;
	else result.Clear();
	return n;
}
// octet
static tjs_int decode_octet(tTJSVariant &result, const tjs_char *str, const tjs_int len) {
	ByteVec vec;
	const tjs_int n = decode(vec, str, len, OctetMarks);
	if (n >= 0) {
		tTJSVariantOctet *oct = TJSAllocVariantOctet(&vec.front(), vec.size());
		if (oct) {
			result = oct;
			oct->Release();
		}
	}
	return n;
}

// 数値デコードutil
static size_t decode_number(ByteVec &vec, const tjs_char *src, const tjs_int len) {
	return decode(vec, src, len, NumberMarks);
}
// 強制キャスト版
template <typename T>
static size_t decode_number(tTJSVariant &result, const tjs_char *src, const tjs_int len, T*) {
	ByteVec vec;
	size_t r = decode_number(vec, src, len);
	if (r > 0) {
		if (vec.size() < sizeof(T)) vec.resize(sizeof(T));
		result = *(reinterpret_cast<T*>(&vec.front()));
	} else result.Clear();
	return r;
}
// 強制キャスト版(int64のみ)
static size_t decode_number(tTVInteger &num, const tjs_char *src, const tjs_int len) {
	ByteVec vec;
	size_t r = decode_number(vec, src, len);
	if (r > 0) {
		if (vec.size() < sizeof(tTVInteger)) vec.resize(sizeof(tTVInteger));
		num = *(reinterpret_cast<tTVInteger*>(&vec.front()));
	}
	return r;
}

// 可変長数値
static size_t decode_number_ex(tTJSVariant &result, const tjs_char *src, const tjs_int len) {
	// マーカーチェック
	const tjs_char ch = *src;
	if (ch >= NUMBER_BASE && ch < NUMBER_INT64) {
		const bool neg = (ch & 0x0100) != 0;
		if (((ch - NUMBER_BASE) & 0xFE00) == 0) {
			// 1文字 (-256～+255)
			const tTVInteger num = ch & 0xFF;
			result = neg ? -num : num;
			return 1;
		}
		// 3文字/5文字(32bit/56bit)
		tTVInteger num = 0;
		const size_t r = decode_number(num, src+1, len-1);
		if (r > 0) {
			num <<= 8;
			num |= ch & 0xFF;
			result = neg ? -num : num;
			return r + 1;
		}
	} else {
		const tjs_char mode = (ch & NUMBER_MASK);
		ByteVec vec;
		if (len >= 6 && (mode == NUMBER_INT64 || mode == NUMBER_DOUBLE)) {
			// 6文字(64bit/double)
			tjs_char tmp[] = { (src[0]&0xFF)|NumberMarks[0],src[1], src[2],src[3], src[4],src[5] };
			if (decode_number(vec, tmp, 6) == 6) {
				vec.erase(vec.begin()+1);
				if (mode == NUMBER_INT64) result = *(reinterpret_cast<const tTVInteger*>(&vec.front()));
				else                      result = *(reinterpret_cast<const tTVReal   *>(&vec.front()));
				return 6;
			}
		} else if (len >= 4 && (mode == NUMBER_FLOAT)) {
			// 4文字(float)
			tjs_char tmp[] = { (src[0]&0xFF)|NumberMarks[0],src[1], src[2],src[3] };
			if (decode_number(vec, tmp, 4) == 4) {
				vec.erase(vec.begin()+1);
				result = (tTVReal)(*(reinterpret_cast<const float*>(&vec.front())));
				return 4;
			}
		}
	}
	result.Clear();
	return 0;
}
// enctypeからのint64
static size_t decode_int64(tTJSVariant &result, const tjs_char *src, const tjs_int len) {
	return decode_number(result, src, len, (tTVInteger*)nullptr);
}
// enctypeからのdouble
static size_t decode_double(tTJSVariant &result, const tjs_char *src, const tjs_int len) {
	return decode_number(result, src, len, (tTVReal*)nullptr);
}
static size_t decode_enctype(tTJSVariant &result, const tjs_char *src, const tjs_int len) {
	switch (*src) {
	default: result.Clear(); return 0;
	case ENCTYPE_VOID:   result.Clear(); break;
	case ENCTYPE_NULL:   result = tTJSVariant(nullptr, nullptr); break;
	case ENCTYPE_EMPSTR: result = TJS_W(""); break;
	case ENCTYPE_INT64:  return decode_int64 (result, src+1, len-1) + 1;
	case ENCTYPE_DOUBLE: return decode_double(result, src+1, len-1) + 1;
	case ENCTYPE_EMPOCT:
		tTJSVariantOctet *oct = TJSAllocVariantOctet((const tjs_uint8*)nullptr, (tjs_uint)0);
		if (oct) {
			result = oct;
			oct->Release();
		}
		break;
	}
	return 1;
}

static const tjs_char* decode_select(tTJSVariant &result, const tjs_char *src, size_t &len) {
	const tjs_char ch = *src;
	if (!ch) return nullptr;
	size_t fw = 0;
	switch (ch & 0xF000) {
	case MARK_ENCTYPE: fw = decode_enctype(result, src, len); break;
	case MARK_NUMBER:  fw = decode_number_ex(result, src, len); break;
	case MARK_STRTERM:
	case MARK_STRING:  fw = decode_string (result, src, len); break;
	case MARK_OCTTERM:
	case MARK_OCTET:   fw = decode_octet  (result, src, len); break;
	default: return nullptr;
	}
	len -= fw;
	return src + fw;
}

//--------------------------------------------------------------
// TJSデコードインターフェース
static tjs_error decodeTriBinPairString(tTJSVariant *result, tTJSVariant *src) {
	if (!result) return TJS_S_OK;
	if (src->Type() == tvtString) {
		ttstr str(*src);
		tjs_int len = str.length();
		if (len <= 0) *result = TJS_W("");
		else {
			size_t slen = (size_t)len;
			decode_select(*result, str.c_str(), slen);
		}
	} else *result = *src;
	return TJS_S_OK;
}



////////////////////////////////////////////////////////////////
bool TriBinPairStringEntry(bool link) {
	return (SimpleBinder::BindUtil(TJS_W("Scripts"), link)
			.Function(TJS_W("encodeTBPS"), &encodeTriBinPairString)
			.Function(TJS_W("decodeTBPS"), &decodeTriBinPairString)
			.IsValid());
}

bool ONV2LINK()   { return TriBinPairStringEntry(true);  }
bool ONV2UNLINK() { return TriBinPairStringEntry(false); }
