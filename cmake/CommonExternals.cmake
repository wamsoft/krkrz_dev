# ==============================================================================
# CommonExternals.cmake
#
# krkrz_dev umbrella 用の共通外部依存設定。サブモジュール (layerExVector /
# krkr_richtext/richtext / src/core/external/elements) が各自抱えていた
# ICU / HarfBuzz の重複ビルドを umbrella 1 箇所に集約する。
#
# - ICU は krkr_richtext (= minikin が <hb-icu.h> を必要とする) を使う構成のみで
#   FetchContent する。
# - HarfBuzz は常に FetchContent。ICU が居れば HB_HAVE_ICU=ON。
# - ThorVG は集約対象に含めない (3 つの submodule を同じ SHA に揃えてある上、
#   ThorVG 3e00b8c9 自体が if(NOT TARGET harfbuzz) ガードで親プロジェクトの HB
#   を再利用する仕組みを持つので、最初に呼ばれるサブの add_subdirectory で
#   生成される thorvg target をそのまま使う)。
#
# 各サブ側は umbrella で先に target が生成されることを期待して、
# add_subdirectory(thorvg) / add_subdirectory(ext/icu) / add_subdirectory(ext/harfbuzz)
# を if(NOT TARGET ...) で囲んでスキップする責務を持つ。
# ==============================================================================

include(FetchContent)

# ------------------------------------------------------------------------------
# krkrz_setup_icu()
#   minikin の richtext/ext/minikin/ext/icu/CMakeLists.txt の処理を移植。
#   icucommon STATIC + ICU::common / ICU::uc ALIAS を作る。
# ------------------------------------------------------------------------------
function(krkrz_setup_icu)
    if(TARGET icucommon)
        return()
    endif()

    set(ICU_VERSION "77.1" CACHE STRING "ICU version (e.g. 77.1)")
    set(ICU_VERSION_TAG "77-1" CACHE STRING "ICU version tag (e.g. 77-1)")
    string(REGEX MATCH "^[0-9]+" ICU_VER "${ICU_VERSION}")

    set(ICU_URL "https://github.com/unicode-org/icu/archive/refs/tags/release-${ICU_VERSION_TAG}.tar.gz")

    FetchContent_Declare(
        icu_source
        URL ${ICU_URL}
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
    )

    message(STATUS "Downloading ICU ${ICU_VERSION} from ${ICU_URL}...")
    FetchContent_MakeAvailable(icu_source)

    set(ICU_SOURCE_DIR "${icu_source_SOURCE_DIR}/icu4c/source")

    file(GLOB ICU_COMMON_SOURCES "${ICU_SOURCE_DIR}/common/*.cpp")
    file(GLOB ICU_COMMON_C_SOURCES "${ICU_SOURCE_DIR}/common/*.c")
    file(GLOB ICU_I18N_SOURCES "${ICU_SOURCE_DIR}/i18n/*.cpp")
    file(GLOB ICU_I18N_C_SOURCES "${ICU_SOURCE_DIR}/i18n/*.c")

    add_library(icucommon STATIC
        ${ICU_COMMON_SOURCES}
        ${ICU_COMMON_C_SOURCES}
        ${ICU_I18N_SOURCES}
        ${ICU_I18N_C_SOURCES}
    )

    target_include_directories(icucommon PUBLIC
        ${ICU_SOURCE_DIR}/common
        ${ICU_SOURCE_DIR}/i18n
        ${ICU_SOURCE_DIR}/stubdata
    )

    target_compile_definitions(icucommon PUBLIC
        U_STATIC_IMPLEMENTATION=1
        PIC
        U_COMMON_IMPLEMENTATION
        U_I18N_IMPLEMENTATION
    )

    if(MSVC)
        target_compile_options(icucommon PRIVATE
            /Zc:__cplusplus
            /utf-8
            /wd4267
            /wd4244
            /wd4996
            /std:c++17
        )
    endif()

    add_library(ICU::common ALIAS icucommon)
    add_library(ICU::uc     ALIAS icucommon)

    set(ICU_FOUND TRUE CACHE BOOL "ICU found" FORCE)
    set(ICU_uc_FOUND TRUE CACHE BOOL "ICU uc component found" FORCE)
    set(ICU_INCLUDE_DIRS "${ICU_SOURCE_DIR}/common" CACHE PATH "ICU include directories" FORCE)
endfunction()

# ------------------------------------------------------------------------------
# krkrz_setup_harfbuzz()
#   HarfBuzz 13.1.1 を FetchContent。ICU::uc が居れば HB_HAVE_ICU=ON。
# ------------------------------------------------------------------------------
function(krkrz_setup_harfbuzz)
    if(TARGET harfbuzz)
        return()
    endif()

    if(TARGET ICU::uc)
        set(_hb_have_icu ON)
    else()
        set(_hb_have_icu OFF)
    endif()

    set(HB_HAVE_FREETYPE ON CACHE BOOL "Enable freetype interop helpers" FORCE)
    set(HB_HAVE_ICU      ${_hb_have_icu} CACHE BOOL "Enable icu unicode functions" FORCE)
    set(HB_BUILD_SUBSET  OFF CACHE BOOL "Build harfbuzz-subset" FORCE)
    set(HB_BUILD_UTILS   OFF CACHE BOOL "Build harfbuzz utils" FORCE)

    set(SKIP_INSTALL_ALL       ON CACHE BOOL "Skip all install targets" FORCE)
    set(SKIP_INSTALL_LIBRARIES ON CACHE BOOL "Skip library install" FORCE)
    set(SKIP_INSTALL_HEADERS   ON CACHE BOOL "Skip header install" FORCE)

    # HarfBuzz の find_package(ICU) を ICU::uc ターゲットに流す shim を
    # CMAKE_MODULE_PATH 先頭に追加。
    if(_hb_have_icu)
        list(INSERT CMAKE_MODULE_PATH 0 "${CMAKE_CURRENT_LIST_DIR}")
        set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH}" PARENT_SCOPE)
    endif()

    set(HB_VERSION "13.1.1")
    FetchContent_Declare(
        harfbuzz_source
        GIT_REPOSITORY https://github.com/harfbuzz/harfbuzz.git
        GIT_TAG ${HB_VERSION}
        GIT_SHALLOW TRUE
    )

    message(STATUS "Downloading HarfBuzz ${HB_VERSION} (HB_HAVE_ICU=${_hb_have_icu})...")
    FetchContent_MakeAvailable(harfbuzz_source)

    # Emscripten (emsdk の clang) では、HarfBuzz 自身が hb.hh で
    #   #pragma GCC diagnostic error "-Wunused"
    # と書いているため、このコンパイラが出す -Wunused-template (グループ -Wunused に
    # 含まれる) がエラーへ格上げされてビルドが止まる。HarfBuzz が用意している
    # エスケープハッチで「error への格上げ」だけ無効化する (警告は残る)。
    # ※ コマンドラインの -Wno-... では後続の pragma に上書きされるので効かない。
    if(EMSCRIPTEN)
        # ターゲット名は HarfBuzz のバージョンで増減する (harfbuzz / -raster /
        # -vector / -subset ...) ので、取得した BUILDSYSTEM_TARGETS 全部へ入れる。
        get_property(_hb_targets DIRECTORY "${harfbuzz_source_SOURCE_DIR}"
                     PROPERTY BUILDSYSTEM_TARGETS)
        foreach(_hb_target IN LISTS _hb_targets)
            get_target_property(_hb_type ${_hb_target} TYPE)
            if(NOT _hb_type STREQUAL "INTERFACE_LIBRARY" AND
               NOT _hb_type STREQUAL "UTILITY")
                target_compile_definitions(${_hb_target}
                    PRIVATE HB_NO_PRAGMA_GCC_DIAGNOSTIC_ERROR)
            endif()
        endforeach()
    endif()

    # ThorVG / elements / その他は harfbuzz::harfbuzz / HarfBuzz::HarfBuzz
    # 双方の名前で参照することがあるので両方エイリアスを張る。
    if(NOT TARGET harfbuzz::harfbuzz)
        add_library(harfbuzz::harfbuzz ALIAS harfbuzz)
    endif()
    if(NOT TARGET HarfBuzz::HarfBuzz)
        add_library(HarfBuzz::HarfBuzz ALIAS harfbuzz)
    endif()
endfunction()

# ==============================================================================
# ThorVG 共通設定 (umbrella 全体に適用)
#
# ThorVG 自体の add_subdirectory はサブ側 (layerExVector / elements / 等)
# が if(NOT TARGET thorvg) ガード越しに行うので、ここでは「最初に呼ばれる
# サブが見るべき cache 値」だけを先に確定させる。
# ==============================================================================

# install(EXPORT thorvgTargets) は harfbuzz 等 PRIVATE 依存を含む export set を
# 構築しようとして configure 失敗する。add_subdirectory 統合用途では不要なので
# 全構成で OFF。
set(TVG_INSTALL OFF CACHE BOOL "Generate install/export rules" FORCE)

# src/core (Elements 統合経路) と同じ意図で、PNG/JPG/WebP は ThorVG 内蔵
# デコーダで賄う (vcpkg の libpng/libjpeg-turbo に依存しない)。
set(TVG_STATIC_MODULES ON CACHE BOOL "Use static modules in ThorVG" FORCE)

# ==============================================================================
# 実行
# ==============================================================================

# krkr_richtext (minikin) が含まれる構成だけ ICU を持ち込む。
# ICU は数百 TU の重量級なので、不要な構成では FetchContent ごとスキップ。
if("krkr_richtext" IN_LIST TVP_PLUGINS)
    krkrz_setup_icu()
endif()

krkrz_setup_harfbuzz()
