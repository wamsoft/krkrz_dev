# サウンドシステム

## サウンドシステムについて

吉里吉里のサウンドシステムは Wave (PCM) を再生できます。

Wave 再生は複数を同時再生でき、ストリーミング再生 (長いサウンドを少しずつ読み込みながら再生) をすることができるほか、サウンドループ情報ファイル (.sli ファイル) を用いて、つぎめを感じさせないシームレスなループ再生を実現できます (サウンドループ情報ファイルはループチューナで作成します)。

## WaveSoundBuffer で再生可能な形式

[WaveSoundBuffer](WaveSoundBuffer.md) では、標準で無圧縮の RIFF Wave 形式 ( 拡張は .wav で、Windows 標準形式 ) を再生することができます。受け付けられる形式は以下の通りです。

- WAVE_FORMAT_PCM 形式で、8bit 以上 32bit 以下の整数 PCM、かつチャンネル数が 1(モノラル)、2(ステレオ), 4(quadraphonic)、6(5.1ch) のもの
- WAVE_FORMAT_IEEE_FLOAT 形式で、32bit の浮動小数点数 PCM、かつチャンネル数が 1(モノラル)、2(ステレオ), 4(quadraphonic)、6(5.1ch) のもの
- WAVE_FORMAT_EXTENSIBLE 形式で、サブタイプが KSDATAFORMAT_SUBTYPE_PCM 形式で8bit 以上 32bit 以下の整数 PCM
- WAVE_FORMAT_EXTENSIBLE 形式で、サブタイプが KSDATAFORMAT_SUBTYPE_IEEE_FLOAT 形式の 32bit 浮動小数点数 PCM

WaveSoundBuffer で再生可能な形式は、プラグインによって拡張することができます。

## WaveSoundBuffer での 4ch および 6ch の扱い

WAVE_FORMAT_EXTENSIBLE は、データ内に「どのチャンネルがどのスピーカーに割り当てられているか」の情報を持っていますが、WAVE_FORMAT_PCM や WAVE_FORMAT_IEEE_FLOAT の場合はその情報を持っていません。吉里吉里が WAVE_FORMAT_PCM や WAVE_FORMAT_IEEE_FLOAT で 4ch や 6ch のデータを扱うときは次のように解釈します。

- **4chのとき**  
  チャンネルの先頭から、それぞれ、前左、前右、後左、後右のスピーカー用データであると見なされます
- **6chのとき**  
  チャンネルの先頭から、それぞれ、前左、前中央、前右、後左、後右、低周波のスピーカー用データであると見なされます

また、OggVorbis で 4ch や 6ch のサウンドを再生するときにもこれと同じルールが適用されます。
