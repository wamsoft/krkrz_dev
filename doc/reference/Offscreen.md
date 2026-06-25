# Offscreen

オフスクリーン。
いわゆるレンダーターゲット。テクスチャとしても利用可能です。
内部的に FBO, Renderbuffer, Texture が生成されます。
レンダーターゲットとして設定しないのであれば、わざわざこのクラスを使用する必要性はありません。
Textureクラスを使用した方がメモリ効率が良いです。

## メンバー一覧

### コンストラクタ

- [Offscreen](#offscreen)

### プロパティ

- [width](#width)
- [height](#height)
- [nativeHandle](#nativehandle)

### メソッド

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [exchangeTexture](#exchangetexture)

---

### Offscreen

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | オフスクリーン幅 |
| `height` | `int` | `&nbsp;` | オフスクリーン高さ |

**解説**

オフスクリーンを生成。

破棄はinvalidate時に行われるので、不要になったら明示的なinvalidate推奨します。

---

### width

プロパティ \ アクセス: `r/w`

**解説**

幅、生成時に指定されたもの[r]

---

### height

プロパティ \ アクセス: `r/w`

**解説**

高さ、生成時に指定されたもの[r]

---

### nativeHandle

プロパティ \ アクセス: `r/w`

**解説**

環境依存のハンドル[r]

OpenGL ES下ではtexture idとなる。

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

矩形コピー

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

矩形コピー

---

### copyTo

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 格納先ビットマップ |
| `dleft` | `int` | `&nbsp;` | コピー先左端 |
| `dtop` | `int` | `&nbsp;` | コピー先上端 |
| `sleft` | `int` | `&nbsp;` | コピー元左端 |
| `stop` | `int` | `&nbsp;` | コピー元上端 |
| `width` | `int` | `&nbsp;` | サイズ横幅 |
| `height` | `int` | `&nbsp;` | サイズ縦幅 |

**解説**

Bitmapにコピー

---

### copyTo

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 格納先ビットマップ |

**解説**

Bitmapにコピー

BitmapはOffscreenのサイズに合わせて拡大縮小されます。

---

### copyTo

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 格納先ビットマップ |
| `dleft` | `int` | `&nbsp;` | コピー先左端 |
| `dtop` | `int` | `&nbsp;` | コピー先上端 |
| `srcRect` | `Rect` | `&nbsp;` | コピー元矩形 |

**解説**

Bitmapにコピー

---

### exchangeTexture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 交換するTextureクラスのインスタンス。 |

**解説**

フレームバッファに設定されているテクスチャとTextureクラスが指すテクスチャを入れ替える。

交換するテクスチャのサイズは合わせておかないと例外となる。
カラーフォーマットもRGBAとする必要がある。
レンダリング途中での入れ替えも行わない方がいいかもしれない(要確認)。
クロスフェードなどで両方に描画する必要がない場合、以前の画像をTextureとして取り出し、新しいTextureに差し替えることでオーバーヘッドを減らせる。

---
