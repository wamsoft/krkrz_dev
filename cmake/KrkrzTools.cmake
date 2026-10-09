#---------------------------------------------------------------------------
# 標準ツール (src/tools/krkrz_tools) のビルドと install
#
# krkrz_tools はツールごとに exe 1 本で配るため、MSVC ランタイムも vcpkg の
# ライブラリも静的リンク (triplet *-windows-static) で作る。本体とは triplet も
# ランタイムも違うので add_subdirectory では取り込まず、ExternalProject で
# 別のビルドとして作る (ビルド先は <build>/krkrz_tools、常に Release)。
#
#   make / cmake --build   … 本体と一緒にツールもビルドする
#   make install           … <prefix>/tools/ にツールの exe とライセンスを置く
#
# KRKRZ_BUILD_TOOLS=OFF でビルドしない。既定は Windows のみ ON
# (krkrz_tools の Linux / macOS ビルドは未確認のため)。
# 初回は krkrz_tools 用の vcpkg ライブラリ (静的版) のビルドで時間がかかる。
#---------------------------------------------------------------------------
set(_KRKRZ_TOOLS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src/tools/krkrz_tools")

if(WIN32)
    set(_krkrz_tools_default ON)
else()
    set(_krkrz_tools_default OFF)
endif()
option(KRKRZ_BUILD_TOOLS "標準ツール (src/tools/krkrz_tools) をビルドし、install で tools/ に置く" ${_krkrz_tools_default})

if(NOT KRKRZ_BUILD_TOOLS)
    return()
endif()
if(NOT EXISTS "${_KRKRZ_TOOLS_DIR}/CMakeLists.txt")
    message(WARNING "KRKRZ_BUILD_TOOLS: ${_KRKRZ_TOOLS_DIR} がありません (git submodule update --init --recursive)。ツールはビルドしません")
    return()
endif()

# 本体の triplet (x64-windows など) から、同じアーキテクチャの静的版を決める
set(_krkrz_tools_triplet "")
if(VCPKG_TARGET_TRIPLET MATCHES "^([a-z0-9]+)-windows")
    set(_krkrz_tools_triplet "${CMAKE_MATCH_1}-windows-static")
elseif(VCPKG_TARGET_TRIPLET)
    set(_krkrz_tools_triplet "${VCPKG_TARGET_TRIPLET}")
endif()

set(_krkrz_tools_stage "${CMAKE_BINARY_DIR}/krkrz_tools-install")
set(_krkrz_tools_args
    "-DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE}"
    "-DVCPKG_TARGET_TRIPLET=${_krkrz_tools_triplet}"
    # 本体は VCPKG_MANIFEST_DIR を build 側のマージ済みマニフェストへ向けているので、
    # ツール側は自分の vcpkg.json を使うよう明示する
    "-DVCPKG_MANIFEST_DIR=${_KRKRZ_TOOLS_DIR}"
    "-DCMAKE_INSTALL_PREFIX=${_krkrz_tools_stage}"
    "-DKRT_INSTALL_BINDIR=."
)
if(CMAKE_C_COMPILER)
    list(APPEND _krkrz_tools_args "-DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}")
endif()
if(CMAKE_CXX_COMPILER)
    list(APPEND _krkrz_tools_args "-DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}")
endif()
if(GIT_EXECUTABLE)
    list(APPEND _krkrz_tools_args "-DGIT_EXECUTABLE=${GIT_EXECUTABLE}")
endif()

include(ExternalProject)
ExternalProject_Add(krkrz_tools
    SOURCE_DIR      "${_KRKRZ_TOOLS_DIR}"
    BINARY_DIR      "${CMAKE_BINARY_DIR}/krkrz_tools"
    INSTALL_DIR     "${_krkrz_tools_stage}"
    CMAKE_ARGS      ${_krkrz_tools_args}
    BUILD_COMMAND   ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release
    INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
    # ツールのソースの変更を拾うため毎回ビルドを呼ぶ (変更が無ければすぐ終わる)
    BUILD_ALWAYS    ON
    USES_TERMINAL_CONFIGURE ON
    USES_TERMINAL_BUILD ON
)

install(DIRECTORY "${_krkrz_tools_stage}/" DESTINATION tools USE_SOURCE_PERMISSIONS)
message(STATUS "krkrz_tools: ${_KRKRZ_TOOLS_DIR} (triplet ${_krkrz_tools_triplet}) → install で tools/")
