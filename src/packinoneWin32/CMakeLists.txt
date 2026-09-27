# packinoneWin32 - WINVER 専用の機能を 1 つの DLL に詰め合わせる
#
# 取り込みの仕組みは ../packinone/absorb.cmake / bundle_impl.h。
# 全機種で動くものは ../packinone 側。

if(NOT KRKRZ_VARIANT STREQUAL "WIN")
    message(STATUS "packinoneWin32: KRKRZ_VARIANT=${KRKRZ_VARIANT} なので作らない (WINVER 専用)")
    return()
endif()

include(${CMAKE_CURRENT_SOURCE_DIR}/../packinone/absorb.cmake)

set(PACKINONE_SOURCES "")

# fstat: ローカルファイルシステム操作。本体に無い分だけ補完する (IF_MISSING 登録)
packinone_absorb(fstat NCBIND SOURCES Main.cpp)

krkrz_plugin(packinoneWin32
    INCLUDES
        ${PACKINONE_DIR}
        ${PACKINONE_PLUGINS_DIR}
        ${PACKINONE_PLUGINS_DIR}/ncbind
    SOURCES
        packinoneWin32.cpp
        ${PACKINONE_SOURCES}
)

target_compile_features(packinoneWin32 PRIVATE cxx_std_17)

set_target_properties(packinoneWin32 PROPERTIES OUTPUT_NAME PackinOneWin32)
