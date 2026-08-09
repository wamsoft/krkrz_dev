# ファイルフォーマット

吉里吉里Zがサポートするファイルフォーマットについて記載しています。

### 目次

[ファイルフォーマット](#fileformat)

## ファイルフォーマット { #fileformat }

| 種類 | 形式 | 拡張子 | 説明 |
| --- | --- | --- | --- |
| 静止画像 | Windows ビットマップ (Bitmap) | .bmp | 無圧縮形式のみサポート。 |
| 静止画像 | JPEG | .jpg | 読み込み時精度を指定可能。<br>設定可能な値は 'high' (高い), 'normal' (標準), 'low' (低い) のいずれか。<br>デフォルトは'normal'。<br>low はIDCTに固定小数点(整数)ANN、色差拡大補間なし。<br>normal はIDCTに固定小数点(整数)ANN、色差拡大補間あり。<br>high はIDCTに浮動小数点AAN、色差拡大補間あり。<br>指定方法については[起動オプション -jpegdec (JPEG画像デコード精度)](../guide/CommandLine.md)を参照のこと。<br>※ IDCTに固定小数点(整数)LLM、色差拡大補間ありがデフォルトの方がいいと思われる。 |
| 静止画像 | Portable Network Graphic (PNG) | .png | αチャンネルや透明色指定に対応。 |
| 静止画像 | Entis Rasterized Image format (ERI) | .eri | L.Entis 氏の提唱する可逆圧縮フォーマット<br>アルファチャネル付きのものも読み込むことができる。<br>詳細は[ERI Developer's site](http://www.entis.jp/eridev/frame.html)を参照のこと。 |
| 静止画像 | TLG5 | .tlg | 吉里吉里独自形式。<br>展開速度が高速(PNGの4倍速程度)なのが特徴。<br>[画像フォーマットコンバータ](../guide/TPC.md)で変換可能。 |
| 静止画像 | TLG6 | .tlg | 吉里吉里独自形式。<br>PNGやTLG5よりも圧縮率は高いが、TLG5の倍ほど展開に時間がかかります。<br>ただ、それでもPNGの2倍速程度なので高速です。<br>[画像フォーマットコンバータ](../guide/TPC.md)で変換可能。 |
| 静止画像 | その他 | .* | Susie-plugin による拡張が可能。 |
| 音声 | WAVE | .wav | 無圧縮WAVE形式をサポート。 |
| 音声 | Ogg Vorbis | .ogg | 本体統合済 (追加 DLL 不要)。 |
| 音声 | Opus | .opus | 本体統合済 (追加 DLL 不要)。 |
| 音声 | その他 | .* | プラグインにより拡張可能。 |
| 動画 | WebM | .webm | VP8 / VP9。アルファ (透過) 付き動画に対応。動画再生機構は本体統合済 (追加 DLL 不要)。 |
| 動画 | MPEG-1 | .mpg<br>.mpeg<br>.mpv<br>.m1v<br>.dat | MPEG-1 のみサポート (MPEG-2 以降は非サポート)。本体統合の pl_mpeg でデコード。 |
| 動画 | MP4 | .mp4<br>.m4v<br>.mov | H.264 / HEVC。Media Foundation でデコード (既定でハードウェアデコード)。 |
| 動画 | Windows Media Video (WMV) | .wmv<br>.asf | Media Foundation でデコード。再生機に Windows Media コンポーネントが必要。 |
| 動画 | AVI | .avi | 非公式サポート。内部コーデックが Media Foundation で扱える場合のみ再生可 (公式サポートは行わない)。 |
| アニメーション | ASD ファイル | .asd | 吉里吉里独自のアニメーション定義形式。<br>AnimationLayer.tjs のコメントを参照のこと。 |
| アーカイブ | XP3 | .xp3 | 吉里吉里独自形式。<br>[Releaser](../guide/Releaser.md)にて作成する。 |
| アーカイブ | PEXP3 | .exe | 吉里吉里独自形式。<br>吉里吉里実行ファイル（krkr.eXe）とXP3形式を組み合わせたもの。<br>非推奨形式。<br>[Releaser](../guide/Releaser.md)にて作成する。 |
| アーカイブ | その他 | .* | プラグインにより拡張可能。 |
| フォント | レンダリング済みフォント | .tft | 吉里吉里独自形式。<br>[レンダリング済みフォントデータ作成ツール](../guide/FontMaker.md)にて生成する |
| フォント | TrueType/OpenType フォント | .ttf<br>.otf | 非公式サポート。<br>システムにフォントをインストールすることなく使える。<br>要 [addFont.dll](https://github.com/wamsoft/addFont)。Windows のみ対応。 |
