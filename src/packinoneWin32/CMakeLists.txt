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

# systemEx: レジストリ / DPI / OS バージョン / 既知フォルダ / メッセージポンプ /
#           DLL 検索パス。 移植できる分は本体へ移してある (IfMissing 登録)
packinone_absorb(systemEx SIMPLEBIND SOURCES main.cpp)

# process: メッセージ専用ウィンドウを作って子プロセスと遣り取りする
packinone_absorb(process NCBIND SOURCES main.cpp)

# dpiicon: DPI に合わせた大きさのウィンドウアイコン (DpiIcon クラス)
packinone_absorb(dpiicon SIMPLEBIND SOURCES Main.cpp)

# windowEx: Win32 のウィンドウ拡張 (メニューバー / NC マウス / メッセージフック / システムメニュー等)
#   と MenuItem 拡張 (bmpItem / rightJustify / popupEx)。 従来型メニュー (menu.dll) 用。
#   WINDOWEX_BUNDLE=1 で Debug.console / Pad / Scripts の拡張を外し、本体が持つメンバは
#   IF_MISSING で登録する (本体を上書きしない)。 MenuItem が無ければ空のダミーに取り付ける
packinone_absorb(windowEx NCBIND SOURCES main.cpp DEFINITIONS WINDOWEX_BUNDLE=1)

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
