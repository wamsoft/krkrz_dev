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
krkr_richtext
extrans
extNagano
AlphaMovie
expat
#krkrlua
)

# 非同期通知(worker スレッド + ウィンドウメッセージ通知)イディオムを全バリアント
# 対応化したもの。`_beginthread`→std::thread、`::PostMessage`→TVPPostWindowMessage、
# Win32 型(WM_APP/WPARAM/DWORD 等)を移植して WIN/SDL/LIB 共通でビルドできる。
#   layerExSave : レイヤ画像の非同期セーブ (PNG/TLG5)
#   sigcheck    : 実行ファイル/ファイル署名の非同期検証 (libtomcrypt)
list(APPEND TVP_PLUGINS
layerExSave
sigcheck
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

# OpenGL ES 描画系プラグイン。GLES(ANGLE/glad)で描画し、描画先の GL コンテキストは
# 吉里吉里本体の OGLDrawDevice もしくは krkrgles の GLESAdaptor が供給する。
#   krkreffekseer : Effekseer エフェクト再生 (ホスト供給の GL コンテキストへ描画)。
#                   Win32 GUI 非依存で全プラットフォーム対象。
list(APPEND TVP_PLUGINS
krkreffekseer
)

# krkrgles は EGL/ANGLE を Window.HWND から生成する作りで Windows 専用
# (macOS / Linux には HWND が無い)。非 Windows では krkreffekseer / krkrlive2d の
# GL コンテキスト供給は本体 OGLDrawDevice を使うため krkrgles は不要。
# ※このブロックは project() より前なので CMAKE_HOST_WIN32 で判定する。
#   krkrgles      : GLES 描画アダプタ (レイヤ⇔FBO、ポストエフェクト)
if(CMAKE_HOST_WIN32)
list(APPEND TVP_PLUGINS
krkrgles
)
endif()

# krkrlive2d は上記に加えて Live2D Cubism Core を必要とする。SDK パスは環境変数
# CUBISM_SDK (ドライバ側 CMake が $ENV{CUBISM_SDK}/Core を参照) で与えられ、未設定では
# ビルドできないため、設定されているときだけビルド対象に含める。
if(DEFINED ENV{CUBISM_SDK})
list(APPEND TVP_PLUGINS
krkrlive2d
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

# ----------------------------------------------------
# 共通外部依存 (ICU / HarfBuzz)
#
# layerExVector / krkr_richtext / elements が各自抱えていた重複ビルドを
# umbrella 1 箇所に集約する。各サブの CMakeLists.txt が
# if(NOT TARGET <name>) ガードで自分のビルドをスキップする前提。
# 詳細は cmake/CommonExternals.cmake のヘッダコメント参照。
# ----------------------------------------------------
include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/CommonExternals.cmake)

# KRKRZ 本体
option(KRKRZ_BUILD_TESTS "build SIMD parity tests" OFF)
add_subdirectory(src/core ${CMAKE_CURRENT_BINARY_DIR}/core)
