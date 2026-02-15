cmake_minimum_required(VERSION 3.20)

set(PROJECT_NAME krkrz_all)
set(PROJECT_VERSION 1.0)

project(${PROJECT_NAME} VERSION ${PROJECT_VERSION})

# プラグイン対象フォルダ
list(APPEND TVP_PLUGIN_FOLDERS ${CMAKE_CURRENT_SOURCE_DIR}/src/plugins)

# プラグイン一覧
list(APPEND TVP_PLUGINS
KAGParserEx
binaryStream
csvParser
fpslimit
getSample
json
layerExAreaAverage
layerExBTOA
layerExDraw
layerExImage
layerExLongExposure
layerExRaster
layerExSave
lineParser
#minizip
#psbfile
saveStruct
scriptsEx
shrinkCopy
#sigcheck
systemEx
tftSave
#krkrlua
)


if (WIN32)
list(APPEND TVP_PLUGINS
# WIN32固有機能をつかっていて現時点でWIN専用。要改修
addFont
memfile
#psdfile
varfile
fstat
gamepad
menu
msgreceiver
stdio
#resourceRW
win32dialog
windowEx
httprequest
shellExecute
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
add_subdirectory(src/core ${CMAKE_CURRENT_BINARY_DIR}/core)
