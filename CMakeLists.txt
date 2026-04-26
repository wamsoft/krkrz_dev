cmake_minimum_required(VERSION 3.20)

set(PROJECT_NAME krkrz_all)
set(PROJECT_VERSION 1.0)

# 共通プラグインフォルダ
set(PLUGINS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/plugins)

# プラグイン対象フォルダ
list(APPEND TVP_PLUGIN_FOLDERS
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
layerExVector
lineParser
minizip
psdfile
saveStruct
scriptsEx
shrinkCopy
sigcheck
#krkrlua
)


if (KRKRZ_VARIANT STREQUAL "WIN")
list(APPEND TVP_PLUGINS
# WIN32固有機能をつかっていて現時点でWIN専用。要改修
addFont
binaryStream
fpslimit
memfile
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

# ----------------------------------------------------
# vcpkg マニフェスト統合
#
# src/core/vcpkg.json を BASE として、src/core/external/movie-player と
# TVP_PLUGIN_FOLDERS / TVP_PLUGINS から解決した各プラグインフォルダ直下の
# vcpkg.json をマージし、${CMAKE_BINARY_DIR}/vcpkg.json に書き出す。
# VCPKG_MANIFEST_DIR を build dir に向けることで、umbrella 直下に
# vcpkg.json を置かなくても vcpkg manifest install がマージ済み
# マニフェストを参照する。
#
# 本処理は project() より前に実行する必要がある (vcpkg toolchain は最初の
# project() 呼び出しで manifest install を起動するため)。src/core 側にも
# 同じマージ処理があるが、umbrella 経由のときは既にここで生成済みのため、
# サブ側で再実行されても出力内容は同一で no-op となる
# (krkrz_merge_vcpkg_manifest は内容差分が無ければ書き換えない)。
# ----------------------------------------------------
include(${CMAKE_CURRENT_SOURCE_DIR}/src/core/cmake/MergeVcpkgManifest.cmake)

set(_KRKRZ_VCPKG_SUBDIRS
    "${CMAKE_CURRENT_SOURCE_DIR}/src/core/external/movie-player"
)

# TVP_PLUGINS × TVP_PLUGIN_FOLDERS を解決して、各プラグイン直下の
# vcpkg.json を統合対象に含める。本体側 foreach(PLUGIN ${TVP_PLUGINS})
# と同じ検索順 (フォルダリストの先頭で一致したものを採用)。
foreach(_plugin IN LISTS TVP_PLUGINS)
    foreach(_folder IN LISTS TVP_PLUGIN_FOLDERS)
        if(EXISTS "${_folder}/${_plugin}")
            list(APPEND _KRKRZ_VCPKG_SUBDIRS "${_folder}/${_plugin}")
            break()
        endif()
    endforeach()
endforeach()

krkrz_merge_vcpkg_manifest(
    BASE    "${CMAKE_CURRENT_SOURCE_DIR}/src/core/vcpkg.json"
    OUTPUT  "${CMAKE_BINARY_DIR}/vcpkg.json"
    SUBDIRS ${_KRKRZ_VCPKG_SUBDIRS}
    # movie-player の glew/glfw3 はサンプル用で krkrz のビルドには不要
    EXCLUDE
        "movie-player:glew"
        "movie-player:glfw3"
)
set(VCPKG_MANIFEST_DIR "${CMAKE_BINARY_DIR}" CACHE PATH
    "vcpkg manifest directory (merged manifest written by krkrz_merge_vcpkg_manifest)" FORCE)

project(${PROJECT_NAME} VERSION ${PROJECT_VERSION})

# KRKRZ 本体
option(KRKRZ_BUILD_TESTS "build SIMD parity tests" OFF)
add_subdirectory(src/core ${CMAKE_CURRENT_BINARY_DIR}/core)
