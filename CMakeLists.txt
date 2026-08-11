cmake_minimum_required(VERSION 3.20)

set(PROJECT_NAME krkrz_all)
set(PROJECT_VERSION 1.0)

# 共通プラグインフォルダ
set(PLUGINS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/plugins)

# ワムソフト開発作業用プラグインフォルダ (krkrtemplate 側、UTF-8 版)
# ../krkrtemplate/plugins_utf8 に src/plugins に無いプラグインのソースがある
set(WAMSOFT_PLUGINS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../krkrtemplate/plugins_utf8)

# ワムソフト SVN 作業ツリー (psbfile / psbwriter 等のソース)
set(WAMSOFT_WORK_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../wamsoft_work)

# プラグイン対象フォルダ
list(APPEND TVP_PLUGIN_FOLDERS
    ${PLUGINS_DIR}
    ${WAMSOFT_PLUGINS_DIR}
    ${WAMSOFT_WORK_DIR}
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
psbfile          # wamsoft_work 由来 (PSBファイル読取 + Storages.mountPSB)
psbwriter        # wamsoft_work 由来 (PSBファイル生成。psbwriter.dll 復元版)
#krkrlua
)

# ワムソフト追加分 (plugins_utf8 由来) のうち Win32 非依存を確認できたもの。
# 全バリアント (WIN/SDL/LIB) 共通でビルドする。
#   textrender : フォント実測は TJS コールバック委譲。windows.h 無し・.rc 不参照。
#   wfstkeff   : 音声エフェクト(STK)。windows.h は #ifdef _WIN32 ガード済、
#                license.cpp は非Windows no-op、license.rc/V2LINK_NEED_HMODULE は WIN 限定。
#   wfdspfilter: 音声フィルタ(DSPFilters 純C++)。同上。
#   ※ wf* の非Windows 実ビルドは未検証 (特に wfstkeff の STK OS 設定)。要ビルド確認。
#   layerExAreaSplit : Layer の画像バッファプロパティ経由のみ。windows.h 除去 +
#                      simplebinder の V2Link scaffold 化済。
list(APPEND TVP_PLUGINS
textrender      # textrender.dll
wfstkeff        # wfBasicEffect.dll
wfdspfilter     # wfTypicalDSP.dll
layerExAreaSplit # layerExAreaSplit.dll (色領域別 province 塗り)
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

# ----------------------------------------------------
# wamsoft_work 由来のうちソースが WINVER 前提のもの (wchar_t=tjs_char 仮定の
# L"..." リテラル、TVPCreateIStream、SetDllDirectory/HWND 等)。generic 変種への
# 移植 (TJS_W 化ほか「旧Win32プラグイン近代化」パターン) が済むまで WIN 専用。
# フォルダ名とターゲット名は一致しない (krkrz_plugin() 登録名で解決される):
#   motion → krkrmotion + krkremote / live2d → krkrlive2d / gles → krkrgles
#   libpsd → psd (libpsd 同梱。ファイル I/O は TVPCreateStream 化済だが実機未検証のため WIN 限定)
# live2d は環境変数 CUBISM_SDK (CubismNativeSamples のパス) が必要。
# ----------------------------------------------------
list(APPEND TVP_PLUGINS
motion           # M2Motion/Emote
)

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

# ----------------------------------------------------
# ワムソフト開発作業用プラグイン (krkrtemplate/plugins_utf8 由来)
#
# makeworld_tools_utf8/plugin64* に配置されている DLL のうち、src/plugins に
# ソースが無く plugins_utf8 側にソースがあるもので、Win32 依存が残るもの。
# (Win32非依存化できた textrender/wfstkeff/wfdspfilter は上の base リストへ移動済)
# ----------------------------------------------------
list(APPEND TVP_PLUGINS
getLangName     # getLangName.dll   (CMakeLists 既存)
lzfs            # lzfs.dll
msdfrender      # msdfrender.dll    (GDIフォント使用: Plugin.cpp/kzbackport)
xlsxWriter      # xlsxWriter.dll    (Excel 読み書き。libxlsxwriter/openxlsx/zlib 同梱, CMake化+x64対応 2026-07-27)
# wfstkeff / wfdspfilter は Win32 非依存化して base(全バリアント)へ移動済
# k2compat は除外 (原則今後は使わない方針。吉里吉里2互換のGUI/WM_TOUCH依存。
#   CMakeLists.txt は残置)
# wvdecoder は除外 (解析ツール用。ogg/opus は wu*.dll(TSS COMモジュール)の動的
#   ロードが前提だが、本体機能とは別物で本構成には無い。将来は python 等の
#   別ツールでの解析対応が無難という方針。CMakeLists.txt は残置)
)
endif()

# OpenGL ES 描画系プラグイン。GLES(ANGLE/glad)で描画し、描画先の GL コンテキストは
# 吉里吉里本体の OGLDrawDevice もしくは krkrgles の GLESAdaptor が供給する。
#   krkreffekseer : Effekseer エフェクト再生 (ホスト供給の GL コンテキストへ描画)。
#                   Win32 GUI 非依存で全プラットフォーム対象。
list(APPEND TVP_PLUGINS
krkreffekseer
)

# krkrthreepp : threepp (three.js 互換 C++ 3D エンジン) による 3D シーン描画 + VRM ロード。
#               ホスト供給の GL コンテキストへ描画 (krkreffekseer 同様 Win32 GUI 非依存で全PF対象)。
#               nested submodule (threepp / external/VRM) を要再帰初期化。
list(APPEND TVP_PLUGINS
krkrthreepp
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
