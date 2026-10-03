set(TPSTUB_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../tp_stub CACHE PATH "Path to tp_stub directory")
include(${TPSTUB_DIR}/krkrz.cmake)

krkrz_plugin(proxyfs
    SIMPLEBIND
    SOURCES
        Main.cpp
)

target_compile_features(proxyfs PRIVATE cxx_std_17)
# システム終了時 (スクリプトエンジン破棄後) の解放でストレージメディアの登録を外す ONV2DETACH を使う
target_compile_definitions(proxyfs PRIVATE V2LINK_USE_V2DETACH)
