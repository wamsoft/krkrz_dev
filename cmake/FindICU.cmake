# ==============================================================================
# カスタム FindICU.cmake (umbrella 用 shim)
# ==============================================================================
# ICU::uc は krkrz_setup_icu() (cmake/CommonExternals.cmake) または minikin の
# ext/icu/CMakeLists.txt で事前にビルド済み。
# HarfBuzz が `find_package(ICU)` を呼んだときに既存ターゲットへ流す。

if(TARGET ICU::uc)
    set(ICU_FOUND TRUE)
    set(ICU_uc_FOUND TRUE)
    set(ICU_VERSION "${ICU_VERSION}" CACHE STRING "ICU version")

    get_target_property(ICU_INCLUDE_DIRS ICU::uc INTERFACE_INCLUDE_DIRECTORIES)

    message(STATUS "FindICU: Using pre-built ICU::uc target (version ${ICU_VERSION})")
else()
    message(FATAL_ERROR "FindICU: ICU::uc target not found. Ensure krkrz_setup_icu() was called before harfbuzz setup.")
endif()
