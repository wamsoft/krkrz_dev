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
	PACKINONE_TJSDATAPACK(f)

#include "bundle_impl.h"
