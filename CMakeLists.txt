cmake_minimum_required(VERSION 3.20)

set(PROJECT_NAME krkrz_all)
set(PROJECT_VERSION 1.0)

project(${PROJECT_NAME} VERSION ${PROJECT_VERSION})

# 共通プラグインフォルダ
set(PLUGINS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/plugins)

# プラグイン対象フォルダ
LIST(APPEND TVP_PLUGIN_FOLDERS
    ${PLUGINS_DIR}
)

set(TPSTUB_DIR ${PLUGINS_DIR}/tp_stub)
set(NCBIND_DIR ${PLUGINS_DIR}/ncbind)
set(SIMPLEBIND_DIR ${PLUGINS_DIR}/simplebinder)

# プラグイン一覧
list(APPEND TVP_PLUGINS
KAGParserEx
csvParser
getSample
json
layerExAreaAverage
layerExBTOA
layerExImage
layerExLongExposure
layerExRaster
lineParser
#minizip
saveStruct
scriptsEx
shrinkCopy
#sigcheck
#krkrlua
)


if (BUILD_WINVER)
list(APPEND TVP_PLUGINS
# WIN32固有機能をつかっていて現時点でWIN専用。要改修
addFont
binaryStream
fpslimit
memfile
#psdfile
varfile
fstat
gamepad
layerExDraw
layerExSave
menu
msgreceiver
stdio
#resourceRW
win32dialog
windowEx
httprequest
shellExecute
systemEx
tftSave
#httpserv
process
messenger
windowExProgress
win32ole
)
endif()

# 特殊プラグイン
# STEAMプラグインはSDKパスが環境変数で提供された場合のみビルド
if(DEFINED ENV{STEAMWORKS_SDK})
list(APPEND PLUGINS 
#	steam
)
endif()

# KRKRZ 本体
option(KRKRZ_BUILD_TESTS "build SIMD parity tests" OFF)
add_subdirectory(src/core ${CMAKE_CURRENT_BINARY_DIR}/core)
