# AlphaMovie

擬似コードによるマニュアル

吉里吉里Z AlphaMovie プラグイン。

アルファチャンネル付き動画コンテナ .amv (Alpha Movie) を再生し、各フレームを
対象 Layer のメイン画像バッファへ直接（アルファ込みで）上書き描画します。

使用例:
var mov = new AlphaMovie();
mov.open("video/explosion.amv");
mov.setPosition(100, 80);
mov.loop = true;
// 毎フレーム:
var no = mov.showNextImage(layer);

showNextImage は呼ぶ度に 1 フレーム進め、描画したフレーム番号を返します。
末尾で loop=true なら先頭へ巻き戻します。loop=false かつ末尾なら末尾番号を
返し続けます（setNextMovieFile 予約があれば次映像へ自動遷移）。
各フレームはフレーム固有の矩形（left,top,width,height）だけを上書きするため、
描かれない領域は前フレームの内容が Layer 上に保持されます。

## メンバー一覧

### コンストラクタ

- [AlphaMovie](#alphamovie)

### プロパティ

- [numOfFrame](#numofframe)
- [frame](#frame)
- [loop](#loop)
- [nextLoop](#nextloop)
- [preloadSamples](#preloadsamples)
- [left](#left)
- [top](#top)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [FPSScale](#fpsscale)
- [FPSRate](#fpsrate)

### メソッド

- [open](#open)
- [clear](#clear)
- [showNextImage](#shownextimage)
- [isPlaying](#isplaying)
- [play](#play)
- [stop](#stop)
- [setPosition](#setposition)
- [setNextMovieFile](#setnextmoviefile)

---

### AlphaMovie

コンストラクタ

**解説**

コンストラクタ（引数なし）

---

### numOfFrame

プロパティ \ アクセス: `r`

**解説**

全フレーム数（読み取り専用）

---

### frame

プロパティ \ アクセス: `r/w`

**解説**

現在のフレーム番号。設定するとその位置へシークする

---

### loop

プロパティ \ アクセス: `r/w`

**解説**

ループ再生するか

---

### nextLoop

プロパティ \ アクセス: `r/w`

**解説**

次映像（setNextMovieFile）のループ設定

---

### preloadSamples

プロパティ \ アクセス: `r/w`

**解説**

先読みバッファ数（本実装は値の保持のみ、既定 5）

---

### left

プロパティ \ アクセス: `r/w`

**解説**

表示位置左（= setPosition の X）

---

### top

プロパティ \ アクセス: `r/w`

**解説**

表示位置上（= setPosition の Y）

---

### screenWidth

プロパティ \ アクセス: `r`

**解説**

映像の幅（読み取り専用）

---

### screenHeight

プロパティ \ アクセス: `r`

**解説**

映像の高さ（読み取り専用）

---

### FPSScale

プロパティ \ アクセス: `r`

**解説**

FPS の分子。FPS = FPSScale / FPSRate（読み取り専用）

---

### FPSRate

プロパティ \ アクセス: `r`

**解説**

FPS の分母。FPS = FPSScale / FPSRate（読み取り専用）

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ストレージ（.amv） |

**解説**

amv を開く

---

### clear

メソッド

**解説**

デコード済みキューをクリアする（本実装は同期デコードのため no-op）

---

### showNextImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 描画先 Layer（hasImage であること） |

**戻り値**

描画したフレーム番号（整数）

**解説**

次フレームを対象 Layer へ描画する

---

### isPlaying

メソッド

**戻り値**

true=再生中 / false=停止中

**解説**

再生中かどうかを返す

---

### play

メソッド

**解説**

再生を開始する（先頭フレームへ巻き戻し、再生状態にする）

---

### stop

メソッド

**解説**

再生を停止する

---

### setPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 表示位置 X |
| `y` | `&nbsp;` | 表示位置 Y |

**解説**

表示位置（左上）を設定する

---

### setNextMovieFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 次に再生する amv ストレージ |

**解説**

次に再生する amv を予約する（現映像の終了で自動遷移）

---
