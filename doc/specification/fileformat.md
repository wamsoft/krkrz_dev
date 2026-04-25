# ファイルフォーマット

吉里吉里2/KAG3がサポートするファイルフォーマットついて記載。

### 目次

[ファイルフォーマット](#fileformat)

## ファイルフォーマット { #fileformat }

| 種類 | 形式 | 拡張子 | 説明 |
| --- | --- | --- | --- |
| 静止画像 | Windows ビットマップ (Bitmap) | .bmp | 無圧縮形式のみサポート。 |
| 静止画像 | JPEG | .jpg | 読み込み時精度を指定可能。<br>設定可能な値は 'high' (高い), 'normal' (標準), 'low' (低い) のいずれか。<br>デフォルトは'normal'。<br>low はIDCTに固定小数点(整数)ANN、色差拡大補間なし。<br>normal はIDCTに固定小数点(整数)ANN、色差拡大補間あり。<br>high はIDCTに浮動小数点AAN、色差拡大補間あり。<br>指定方法については[起動オプション -jpegdec (JPEG画像デコード精度)](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/CommandLine.html#id47)を参照のこと。<br>※ IDCTに固定小数点(整数)LLM、色差拡大補間ありがデフォルトの方がいいと思われる。 |
| 静止画像 | Portable Network Graphic (PNG) | .png | αチャンネルや透明色指定に対応。 |
| 静止画像 | Entis Rasterized Image format (ERI) | .eri | L.Entis 氏の提唱する可逆圧縮フォーマット<br>アルファチャネル付きのものも読み込むことができる。<br>詳細は[ERI Developer's site](http://www.entis.jp/eridev/frame.html)を参照のこと。 |
| 静止画像 | TLG5 | .tlg | 吉里吉里独自形式。<br>展開速度が高速(PNGの4倍速程度)なのが特徴。<br>[画像フォーマットコンバータ](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/TPC.html)で変換可能。 |
| 静止画像 | TLG6 | .tlg | 吉里吉里独自形式。<br>PNGやTLG5よりも圧縮率は高いが、TLG5の倍ほど展開に時間がかかります。<br>ただ、それでもPNGの2倍速程度なので高速です。<br>[画像フォーマットコンバータ](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/TPC.html)で変換可能。 |
| 静止画像 | その他 | .* | Susie-plugin による拡張が可能。 |
| 音声 | WAVE | .wav | 無圧縮WAVE形式をサポート。 |
| 音声 | Ogg Vorbis | .ogg | 要wuvorbis.dllプラグイン |
| 音声 | MIDI | .smf<br>.mid | &nbsp; |
| 音声 | CD-DA | .cda | CD-XA形式のCDに対応。 |
| 音声 | その他 | .* | プラグインにより拡張可能。 |
| 動画 | MPEG I | .mpg<br>.mpeg<br>.mpv<br>.m1v<br>.dat | MPEG Iのみサポート。<br>MPEG2などそれ以降は非サポート。<br>要 krmovie.dll。<br>再生機にWindows Media Player 6.4以降、<br>またはDirectX 7以降がインストールされていること。 |
| 動画 | Adobe Flash | .swf | 要 krflash.dll。<br>再生機にFlash Playerがインストールされていること。 |
| 動画 | Windows Media Video (WMV) | .wmv | 要 krmovie.dll。<br>再生機にWindows Media Player 9以降がインストールされていること。 |
| 動画 | AVI | .avi | 非公式サポート。<br>要 krmovie.dll。<br>Codecなどの問題により再生出来ないことなどがあり、公式サポートは行わない。 |
| アニメーション | ASD ファイル | .asd | 吉里吉里独自形式。<br>KAG3 でサポートされる。<br>AnimationLayer.tjsのコメント、もしくは[吉里吉里2/KAG3のアニメーション](http://homepage1.nifty.com/gutchie/KAG3Animation.html)を参照のこと |
| アーカイブ | XP3 | .xp3 | 吉里吉里独自形式。<br>[Releaser](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/Releaser.html)にて作成する。 |
| アーカイブ | PEXP3 | .exe | 吉里吉里独自形式。<br>吉里吉里実行ファイル（krkr.eXe）とXP3形式を組み合わせたもの。<br>非推奨形式。<br>[Releaser](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/Releaser.html)にて作成する。 |
| アーカイブ | その他 | .* | プラグインにより拡張可能。 |
| フォント | レンダリング済みフォント | .tft | 吉里吉里独自形式。<br>[レンダリング済みフォントデータ作成ツール](http://devdoc.kikyou.info/tvp/docs/kr2doc/contents/FontMaker.html)にて生成する |
| フォント | TrueType/OpenType フォント | .ttf<br>.otf | 非公式サポート。<br>システムにフォントをインストールすることなく使える。<br>要[addFont.dll](../../src/plugins/win32/addFont/)。Windows2000/XP/Vista のみ対応。 |
