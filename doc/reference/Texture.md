# Texture

テクスチャクラス。
ハードウェア上のテクスチャとほぼ対応しています。

invalidateすることでテクスチャは無効化されるため、必要なくなったら明示的にinvalidate呼び出すことを推奨します。

## メンバー一覧

### コンストラクタ

- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)

### プロパティ

- [width](#width)
- [height](#height)
- [memoryWidth](#memorywidth)
- [memoryHeight](#memoryheight)
- [isGray](#isgray)
- [isPowerOfTwo](#ispoweroftwo)
- [nativeHandle](#nativehandle)
- [stretchType](#stretchtype)
- [wrapModeHorizontal](#wrapmodehorizontal)
- [wrapModeVertical](#wrapmodevertical)
- [margin9Patch](#margin9patch)

### メソッド

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [setDrawSize](#setdrawsize)

### 定数

- [stNearest](#stnearest)
- [stLinear](#stlinear)
- [wmRepeat](#wmrepeat)
- [wmClampToEdge](#wmclamptoedge)
- [wmMirror](#wmmirror)

---

### Texture

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `filename` | `string` | `&nbsp;` | 画像ファイル名 |
| `format` | `int` | `tcfRGBA` | カラーフォーマット(tcfRGBA or tcfAlpha), tcfAlpha選択時に色情報はグレイスケール化されます |
| `is9patch` | `bool` | `false` | 9patch情報を読み込み、9patch描画用として使用するかどうか |

**解説**

ファイル読み込み版コンストラクタ

---

### Texture

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `bitmap` | `Bitmap` | `&nbsp;` | テクスチャの元となるBitmapクラスのインスタンス |
| `format` | `int` | `tcfRGBA` | カラーフォーマット(tcfRGBA or tcfAlpha), tcfAlpha選択時に色情報はグレイスケール化されます |
| `is9patch` | `bool` | `false` | 9patch情報を読み込み、9patch描画用として使用するかどうか |

**解説**

Bitmapコピー版コンストラクタ

---

### Texture

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | テクスチャ幅 |
| `height` | `int` | `&nbsp;` | テクスチャ高さ |
| `format` | `int` | `tcfRGBA` | カラーフォーマット(tcfRGBA or tcfAlpha) |

**解説**

サイズ指定版コンストラクタ

テクスチャの内容は未初期化なのでごみが入っています。

---

### Texture

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `sizelist` | `Array` | `&nbsp;` | ミップマップを生成するサイズを配列で幅、高さの組み合わせで指定します。 |
| `filename` | `string` | `&nbsp;` | 画像ファイル名 |
| `type` | `&nbsp;` | `stFastAreaAvg` | 縮小アルゴリズムを指定します。ImageFunction.operateStretch の type か Layer.operateStretch の type 引数と同じです。 |
| `typeopt` | `real` | `-1.0` | ３次元補間時のシャープネスです。他の補間方法では現在のところ意味を持ちません。 |

**解説**

ミップマップ生成版コンストラクタ

---

### width

プロパティ \ アクセス: `r/w`

**解説**

幅(有効範囲)

pot指定されていなければ、memoryWidthと同一です。

---

### height

プロパティ \ アクセス: `r/w`

**解説**

高さ(有効範囲)

pot指定されていなければ、memoryHeightと同一です。

---

### memoryWidth

プロパティ \ アクセス: `r/w`

**解説**

実際(ハードウェア上)の幅

---

### memoryHeight

プロパティ \ アクセス: `r/w`

**解説**

実際(ハードウェア上)の高さ

---

### isGray

プロパティ \ アクセス: `r/w`

**解説**

8bitカラーかどうか(内部ではアルファテクスチャ)

---

### isPowerOfTwo

プロパティ \ アクセス: `r/w`

**解説**

テクスチャサイズが2の累乗値かどうか

---

### nativeHandle

プロパティ \ アクセス: `r/w`

**解説**

ネイティブハンドル(環境依存)

OpenGL ES2/3 環境下ではテクスチャID

---

### stretchType

プロパティ \ アクセス: `r/w`

**解説**

拡大縮小時の補間方法

---

### wrapModeHorizontal

プロパティ \ アクセス: `r/w`

**解説**

水平方向ラップモード

---

### wrapModeVertical

プロパティ \ アクセス: `r/w`

**解説**

垂直方向ラップモード

---

### margin9Patch

プロパティ \ アクセス: `r/w`

**解説**

9patchマージン

is9patchを指定して読み込んだ場合Rectクラスのオブジェクトが読み取り専用でアクセスできます。
指定されていなかったり、読み取りできなかった場合はvoidです。

---

### copyRect

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | コピー先左端 |
| `dtop` | `int` | `&nbsp;` | コピー先上端 |
| `src` | `Bitmap` | `&nbsp;` | Bitmapクラスのオブジェクト |
| `srcRect` | `Rect` | `&nbsp;` | srcのコピー元矩形 |

**解説**

矩形コピー(位置指定Rect版)

---

### copyRect

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | コピー先左端 |
| `dtop` | `int` | `&nbsp;` | コピー先上端 |
| `src` | `Bitmap` | `&nbsp;` | Bitmapクラスのオブジェクト |
| `sleft` | `int` | `&nbsp;` | コピー元左端位置 |
| `stop` | `int` | `&nbsp;` | コピー元上端位置 |
| `swidth` | `int` | `&nbsp;` | コピー元幅 |
| `sheight` | `int` | `&nbsp;` | コピー元高さ |

**解説**

矩形コピー(位置指定)

---

### copyRect

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `src` | `Bitmap` | `&nbsp;` | Bitmapクラスのオブジェクト |

**解説**

矩形コピー(全コピー)

bitmap全体をコピーします。はみ出す場合はクリッピングされます。

---

### setDrawSize

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 表示基準幅 |
| `height` | `int` | `&nbsp;` | 表示基準高さ |

**解説**

描画基準サイズの設定

Canvas.drawTextureで等倍描画した時、何も指定しないとテクスチャのサイズで描画されますが、このメソッドで幅と高さを設定すると、このテクスチャインスタンスを使って描画した時設定したサイズで描画されるようになります。
拡大縮小などもこのサイズが基準となり描画されます。
内部画像データのサイズと普段描画するサイズが異なる場合に設定しておくと、拡大率を表示したいサイズ基準で指定できるようになります。

---

### stNearest

定数

**解説**

最近傍点法。stretchTypeプロパティに設定します。

---

### stLinear

定数

**解説**

線形補間。stretchTypeプロパティに設定します。

---

### wmRepeat

定数

**解説**

繰り返し。wrapModeHorizontal/wrapModeVerticalプロパティに設定します。

---

### wmClampToEdge

定数

**解説**

端色引き延ばし。wrapModeHorizontal/wrapModeVerticalプロパティに設定します。2の累乗サイズでない場合はこの定数でなければなりません(default)。

---

### wmMirror

定数

**解説**

ミラー繰り返し。wrapModeHorizontal/wrapModeVerticalプロパティに設定します。

---
