# 画像処理機能

吉里吉里Z がサポートする画像処理機能について記載します。

## 概要

吉里吉里Z の画像処理は、CPU 側の 32bpp BGRA ビットマップ (`tTVPBaseBitmap`) を合成面として行われます。ブレンド (合成演算) やリサンプル (拡大縮小・回転) などのピクセル処理は SIMD 実装 (SSE2 / AVX2 / NEON) で高速化されており、SIMD が使えない環境向けに C リファレンス実装 (`tvpgl.c`) も備えています。

このほか、OpenGL ES の Canvas / Texture を用いた GPU 描画パスもあり、テクスチャ合成やシェーダによる描画を GPU 上で行えます。

### 目次

[諸元](#spec)

[読み書き可能な画像形式](#imageformat)

[合成演算](#blend_mode)

## 諸元 { #spec }

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- | --- |
| 合成<br>演算 | 不透明 | 乗算合成 | Photoshop互換<br>覆い焼き(リニア)合成(加算合成) | Photoshop互換<br>ハードライト合成 | Photoshop互換<br>比較(明)合成 |
| 合成<br>演算 | アルファ合成 | 覆い焼き合成 | Photoshop互換<br>焼き込み(リニア)合成(減算合成) | Photoshop互換<br>ソフトライト合成 | Photoshop互換<br>比較(暗)合成 |
| 合成<br>演算 | 加算アルファ合成 | 比較(明)合成 | Photoshop互換<br>乗算合成 | Photoshop互換<br>覆い焼きカラー合成 | Photoshop互換<br>差の絶対値合成 |
| 合成<br>演算 | 加算合成 | 比較(暗)合成 | Photoshop互換<br>スクリーン合成 | Photoshop V.5.x以下互換<br>覆い焼きカラー合成 | Photoshop V.5.x以下互換<br>差の絶対値合成 |
| 合成<br>演算 | 減算合成 | スクリーン乗算合成 | Photoshop互換<br>オーバーレイ合成 | Photoshop互換<br>焼き込みカラー合成 | Photoshop互換<br>除外合成 |

## 読み書き可能な画像形式 { #imageformat }

標準状態で読み込み・書き出しの双方に対応する画像形式は以下の通りです。

| 形式 | 拡張子 | 備考 |
| --- | --- | --- |
| BMP | .bmp | Windows 標準のビットマップ形式。32bpp の BMP はアルファチャネル付きと見なされます。 |
| JPEG | .jpg / .jpeg | libjpeg-turbo によるデコード/エンコード。 |
| PNG | .png | libpng によるデコード/エンコード。アルファチャネル付きに対応します。 |
| TLG5 / TLG6 | .tlg | 吉里吉里独自の可逆圧縮フォーマット。TLG5 は高速展開、TLG6 は高圧縮率が特徴です。 |

また、色情報の画像(メイン)とアルファチャネル(マスク)を分離した **メイン/マスク分離形式** に対応します。マスク画像はメイン画像のファイル名に `_m` を付加したもの (たとえば `abc.jpg` に対して `abc_m.jpg`) となります。メインとマスクの形式が異なっていてもかまいません。

対応する画像形式はプラグインによって拡張することができます。

## 合成演算 { #blend_mode }

以下に、レイヤの合成演算 (レイヤタイプ) の一覧を示します。式中の *result* は結果、*dest* は重ね合わせ先の輝度、*src* は重ね合わせる画像の輝度、*α* はピクセルごとのアルファ値で、いずれも値の範囲は 0.0 ～ 1.0 とします。`blend(a, b, r)` は `a × (1.0 - r) + b × r` を表します。

| No. | 種類 | 式 | 説明 |
| --- | --- | --- | --- |
| 1 | 不透明 | result = src | アルファチャンネルを参照せずに合成を行います |
| 2 | アルファ合成 | result = blend(dest, src, α) | アルファ合成を行います。<br>透過を行う際のもっとも基本的なタイプです。 |
| 3 | 加算アルファ合成 | result = min(1.0, dest × ( 1.0 - α ) + src) | 加算アルファ合成を行います。 |
| 4 | 加算合成 | result = min(1.0, dest × ( 1.0 - α ) + src) | 加算合成を行います。光彩の表現に適しています。<br>11.Photoshopにおける「覆い焼き(リニア)」に相当しますが、本合成ではアルファは無視されます。<br>中性色 (重ね合わせても変化のない色) は黒です。 |
| 5 | 減算合成 | result = max(0.0, dest + src - 1.0)<br>※ result = dest - src と違うのは src が反転しないかするかの違いだけです。 | 減算合成を行います。αは無視されます。<br>中性色は白です。 |
| 6 | 乗算合成 | result = dest × src | 乗算合成を行います。<br>αは無視されます。<br>中性色は白です。 |
| 7 | 覆い焼き合成 | result = min(1.0, dest ÷ ( 1.0 - src ) ) | 覆い焼き合成を行います。<br>光に照らされたものの表現に適しています。<br>αは無視されます。<br>中性色は黒です。 |
| 8 | 比較(明)合成 | result = max(dest, src) | 「比較(明)」合成を行います。<br>αは無視されます。<br>中性色は黒です。 |
| 9 | 比較(暗)合成 | result = min(dest, src) | 「比較(暗)」合成を行います。<br>αは無視されます。<br>中性色は白です。 |
| 10 | スクリーン乗算合成 | result = 1.0 - ( 1.0 - dest ) × ( 1.0 - src ) | 「スクリーン乗算」合成を行います。<br>αは無視されます。<br>中性色は黒です。 |
| 11 | Photoshop互換<br>覆い焼き(リニア)合成<br>(加算合成) | result = blend(dest, min(1.0, dest + src), α) | Photoshop互換の「覆い焼き(リニア)」合成(加算合成)を行います。<br>4.加算合成と違い、αは無視されません。<br>中性色は黒です。 |
| 12 | Photoshop互換<br>焼き込み(リニア)合成<br>(減算合成) | result = blend(dest, max(0.0, dest + src - 1.0), α) | Photoshop互換の「焼き込み(リニア)」合成(減算合成)を行います。<br>5.減算合成と違い、αは無視されません。<br>中性色は白です。 |
| 13 | Photoshop互換<br>乗算合成 | result = blend(dest, dest × src, α) | Photoshop互換の「乗算」合成を行います。<br>6.乗算合成と違い、αは無視されません。<br>中性色は白です。 |
| 14 | Photoshop互換<br>スクリーン合成 | result = blend(dest, 1.0 - (1.0 - dest) × (1.0 - src), α) | Photoshop互換の「スクリーン」合成を行います。<br>10.スクリーン乗算合成と違い、αは無視されません。<br>中性色は黒です。 |
| 15 | Photoshop互換<br>オーバーレイ合成 | result = blend(dest, overlay(dest, src), α)<br>ここで overlay(a, b) =<br>a × b × 2.0 ( a < 0.5 のとき)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (それ以外のとき) | Photoshop互換の「オーバーレイ」合成を行います。<br>中性色は50%灰色です。 |
| 16 | Photoshop互換<br>ハードライト合成 | result = blend(dest, hardlight(dest, src), α)<br>ここで hardlight(a, b) =<br>a × b × 2.0 (b < 0.5 のとき)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (それ以外のとき) | Photoshop互換の「ハードライト」合成を行います。<br>中性色は50%灰色です。 |
| 17 | Photoshop互換<br>ソフトライト合成 | result = blend(dest, softlight(dest, src), α)<br>ここで softlight(a, b) =<br>後でLatexで書いた式を貼り付ける | Photoshop互換の「ソフトライト」合成を行います。<br>中性色は50%灰色です。 |
| 18 | Photoshop互換<br>覆い焼きカラー合成 | result = blend(dest, min(1.0, dest ÷ ( 1.0 - src ) ), α) | Photoshop互換の「覆い焼きカラー」合成を行います。<br>ltDodge と違い、αは無視されません。<br>中性色は黒です。 |
| 19 | Photoshop Ver.5.x以下互換<br>覆い焼きカラー合成 | result = min(1.0, dest ÷ ( 1.0 - src × α) ) | Photoshopのバージョン 5.x 以下と互換の「覆い焼きカラー」合成を行います。<br>18.Photoshop互換覆い焼きカラー合成とは式が若干異なります。<br>中性色は黒です。 |
| 20 | Photoshop互換<br>焼き込みカラー合成 | result = blend(dest, max(0.0, 1.0 - (1.0 - dest) ÷ src), α) | Photoshop互換の「焼き込みカラー」合成を行います。<br>中性色は白です。 |
| 21 | Photoshop互換<br>比較(明)合成 | result = blend(dest, max(dest, src), α) | Photoshop互換の「比較(明)」合成を行います。<br>8.比較(明)合成と違い、αは無視されません。<br>中性色は黒です。 |
| 22 | Photoshop互換<br>比較(暗)合成 | result = blend(dest, min(dest, src), α) | Photoshop互換の「比較(暗)」合成を行います。<br>9.比較(暗)合成と違い、αは無視されません。<br>中性色は白です。 |
| 23 | Photoshop互換<br>差の絶対値合成 | result = blend(dest, abs(dest - src), α) | Photoshop互換の「差の絶対値」合成を行います。<br>中性色は黒です。 |
| 24 | Photoshop Ver.5.x以下互換<br>差の絶対値合成 | result = abs(dest - src × α) | Photoshopのバージョン 5.x 以下と互換の「差の絶対値」合成を行います。<br>23.Photoshop互換差の絶対値合成とは式が若干異なります。<br>中性色は黒です。 |
| 25 | Photoshop互換<br>除外合成 | result = blend(dest, dest + src - 2.0 × src × dest, α) | Photoshop互換の「除外」合成を行います。<br>中性色は黒です。 |
