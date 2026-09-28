# packinone - 全機種で動く個別プラグインのソースを 1 つの DLL に詰め合わせる
#
# 取り込みの仕組みは absorb.cmake / bundle_impl.h、方針は README.md。
# Win32 専用の機能は ../packinoneWin32 側。

include(${CMAKE_CURRENT_SOURCE_DIR}/absorb.cmake)

set(PACKINONE_SOURCES "")

packinone_absorb(csvParser     SOURCES main.cpp)
packinone_absorb(saveStruct    NCBIND SOURCES Main.cpp)
packinone_absorb(scriptsEx     NCBIND SOURCES Main.cpp)
packinone_absorb(shrinkCopy    NCBIND SOURCES main.cpp)
packinone_absorb(layerExBTOA   NCBIND SOURCES Main.cpp)
packinone_absorb(layerExRaster NCBIND SOURCES main.cpp)
packinone_absorb(layerExImage  NCBIND SOURCES LayerExImage.cpp Main.cpp LicensesGen.cpp)

# 旧 PackinOne にしか無かったものを個別プラグインとして起こし直した分
packinone_absorb(pemachinetype    SIMPLEBIND SOURCES Main.cpp)
packinone_absorb(TriBinPairString SIMPLEBIND SOURCES Main.cpp)
packinone_absorb(proxyfs          SIMPLEBIND SOURCES Main.cpp)

# tjsDataPack だけは現行ツリーの外 (krkrtemplate/plugins_utf8) にある
set(PACKINONE_TJSDATAPACK_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../krkrtemplate/plugins_utf8/tjsDataPack"
    CACHE PATH "Path to tjsDataPack sources")
if(EXISTS "${PACKINONE_TJSDATAPACK_DIR}/Main.cpp")
    packinone_absorb(tjsDataPack SIMPLEBIND
        DIR      ${PACKINONE_TJSDATAPACK_DIR}
        INCLUDES lz4 xxHash
        SOURCES
            Main.cpp
            VariantArchive.cpp
            LayerImage.cpp
            ImageChunk.cpp
            lz4/lz4.c
            lz4_license_bin.c
            xxHash/xxhash.c
            xxhash_license_bin.c)
    set(PACKINONE_HAS_TJSDATAPACK TRUE)
else()
    message(WARNING "packinone: tjsDataPack sources not found at ${PACKINONE_TJSDATAPACK_DIR} - skipped")
endif()

# tlgSliceLoader も現行ツリーの外。 lz4 は tjsDataPack のものを共用する
# (同じ DLL 内なので lz4.c は tjsDataPack 側の 1 本で足りる)。
set(PACKINONE_TLGSLICE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../krkrtemplate/plugins_utf8/tlgSliceLoader"
    CACHE PATH "Path to tlgSliceLoader sources")
if(PACKINONE_HAS_TJSDATAPACK AND EXISTS "${PACKINONE_TLGSLICE_DIR}/Main.cpp")
    packinone_absorb(tlgSliceLoader SIMPLEBIND
        DIR      ${PACKINONE_TLGSLICE_DIR}
        INCLUDES ${PACKINONE_TJSDATAPACK_DIR}/lz4
        SOURCES
            Main.cpp
            LoadTLG.cpp
            LoadQOI.cpp
            FetchSize.cpp
            MyException.cpp
            SliceLayer_bin.c
            lz4wrap.cpp)
    set(PACKINONE_HAS_TLGSLICE TRUE)
else()
    message(WARNING "packinone: tlgSliceLoader sources not found at ${PACKINONE_TLGSLICE_DIR} - skipped")
endif()

krkrz_plugin(packinone
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${PACKINONE_PLUGINS_DIR}
        ${PACKINONE_PLUGINS_DIR}/ncbind
    SOURCES
        packinone.cpp
        ${PACKINONE_SOURCES}
)

target_compile_features(packinone PRIVATE cxx_std_17)

if(PACKINONE_HAS_TJSDATAPACK)
    target_compile_definitions(packinone PRIVATE PACKINONE_HAS_TJSDATAPACK)
endif()
if(PACKINONE_HAS_TLGSLICE)
    target_compile_definitions(packinone PRIVATE PACKINONE_HAS_TLGSLICE)
endif()

# 歴史的な名前 (スクリプトは "PackinOne.dll" を link する)
set_target_properties(packinone PROPERTIES OUTPUT_NAME PackinOne)
