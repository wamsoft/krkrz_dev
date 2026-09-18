set(TPSTUB_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../tp_stub CACHE PATH "Path to tp_stub directory")
include(${TPSTUB_DIR}/krkrz.cmake)

# 音声のスペクトラム表示 (drawFFTGraph)。
#
# 吉里吉里2 の標準プラグイン (src/plugins/win32/fftgraph) を移植したもの。
# SoundBuffer の getVisBuffer で取った PCM を FFT にかけ、帯域ごとの棒と
# ピークをレイヤへ直接描く。
#
# 移植 (2026-09-19):
#   - Shift_JIS / LF → UTF-8 / CRLF
#   - Borland の `_stdcall _export` と fftgraph.def → 他プラグインと同じ
#     `__declspec(dllexport)` + アーキ分岐の /EXPORT pragma
#   - `#pragma argsused` は削除
#
# FFT は大浦拓哉氏の General Purpose FFT Package (fftsg.c) を同梱している。
# 表記は readme.txt を参照。

krkrz_plugin(fftgraph
    SOURCES
        Main.cpp
        fftsg.c
)
