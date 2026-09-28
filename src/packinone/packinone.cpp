//---------------------------------------------------------------------------
// packinone - 全機種で動く個別プラグインを 1 つの DLL に詰め合わせる
//
//   Win32 専用の機能は packinoneWin32 側にある。
//   仕組みは bundle_impl.h を参照。
//---------------------------------------------------------------------------
#ifdef PACKINONE_HAS_TJSDATAPACK
# define PACKINONE_TJSDATAPACK(f) f(tjsDataPack)
#else
# define PACKINONE_TJSDATAPACK(f)
#endif

#ifdef PACKINONE_HAS_TLGSLICE
# define PACKINONE_TLGSLICE(f) f(tlgSliceLoader)
#else
# define PACKINONE_TLGSLICE(f)
#endif

#define PACKINONE_PLUGINS(f) \
	f(csvParser)             \
	f(saveStruct)            \
	f(scriptsEx)             \
	f(shrinkCopy)            \
	f(layerExBTOA)           \
	f(layerExRaster)         \
	f(layerExImage)          \
	f(pemachinetype)         \
	f(TriBinPairString)      \
	f(proxyfs)               \
	PACKINONE_TJSDATAPACK(f) \
	PACKINONE_TLGSLICE(f)

#define PACKINONE_SELF_NAME TJS_W("PackinOne.dll")

#include "bundle_impl.h"
