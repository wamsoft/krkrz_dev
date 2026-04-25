# Canvas

Canvasは描画機能を提供するクラスです。
Windowを生成すると、プロパティcanvasが自動的に作られます。
使用する時は、このWindowのcanvasプロパティを使用します。

## メンバー一覧

### プロパティ

- [clearColor](#clearcolor)
- [renderTarget](#rendertarget)
- [blendMode](#blendmode)
- [matrix](#matrix)
- [defaultShader](#defaultshader)
- [defaultFillShader](#defaultfillshader)
- [width](#width)
- [height](#height)
- [clipRect](#cliprect)
- [enableClipRect](#enablecliprect)
- [enableCulling](#enableculling)

### メソッド

- [clear](#clear)
- [capture](#capture)
- [save](#save)
- [restore](#restore)
- [fill](#fill)
- [drawMesh](#drawmesh)
- [drawMesh](#drawmesh)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTextureAtlas](#drawtextureatlas)
- [drawTextureAtlas](#drawtextureatlas)
- [draw9Patch](#draw9patch)
- [flush](#flush)
- [drawText](#drawtext)

---

### clearColor

プロパティ \ アクセス: `r/w`

**解説**

クリア色指定・描画処理前の画面クリア色

---

### renderTarget

プロパティ \ アクセス: `r/w`

**解説**

描画ターゲット指定

Offscreenクラスを指定可能。
null/void指定で直接描画に。

---

### blendMode

プロパティ \ アクセス: `r/w`

**解説**

描画の合成モード指定

bmDisable, bmOpaque, bmAlpha, bmAdd, bmAddWithAlpha が指定可能。
ここにないブレンド方法が必要であればシェーダーを記述する。

---

### matrix

プロパティ \ アクセス: `r/w`

**解説**

描画マトリックス指定

(Matrix32 クラス)

---

### defaultShader

プロパティ \ アクセス: `r/w`

**解説**

テクスチャの描画に使用されるデフォルトのシェーダー(drawTextureでtexture1枚のみ渡した時のシェーダー)

設定もできるが、基本的に変更する必要はない。
voidを入れると組み込みの初期デフォルトシェーダーに戻る。

---

### defaultFillShader

プロパティ \ アクセス: `r/w`

**解説**

fill時に使用されるデフォルトのシェーダー

設定もできるが、基本的に変更する必要はない
voidを入れると組み込みの初期デフォルトシェーダーに戻る。

---

### width

プロパティ \ アクセス: `r/w`

**解説**

描画領域の幅

基本的にはクライアント領域と一致、Windowリサイズから再描画まで一時的にずれる期間(1フレーム)があります。

---

### height

プロパティ \ アクセス: `r/w`

**解説**

描画領域の高さ

基本的にはクライアント領域と一致、Windowリサイズから再描画まで一時的にずれる期間(1フレーム)があります。

---

### clipRect

プロパティ \ アクセス: `r/w`

**解説**

クリッピング用矩形のRectクラス

canvas.clipRect.set( l, t, r, b ); 等で呼び出せます。
enableClipRect で有効/無効設定可

---

### enableClipRect

プロパティ \ アクセス: `r/w`

**解説**

矩形でクリッピングするかどうかの設定

true の時、clipRectプロパティによってクリッピングされる

---

### enableCulling

プロパティ \ アクセス: `r/w`

**解説**

表裏カリングを行うかどうかの設定

true の時は行う、false の時は行わない、デフォルトはfalse。

---

### clear

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `argb` | `int` | `&nbsp;` | クリア色(未指定時はclearColorプロパティでクリアされる) |

**解説**

描画領域全体をクリア

---

### capture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `dest` | `&nbsp;` | `&nbsp;` | キャプチャ先Bitmap/Texture/Offscreen |
| `front` | `bool` | `true` | front bufferからのキャプチャかback bufferからのキャプチャかの指定。trueでfront、falseでback |

**解説**

現在の描画内容全体をBitmap/Texture/Offscreenにキャプチャ

ビットマップのサイズはスクリーンサイズに補正
Texture/Offscreenの場合は変更されない

---

### save

メソッド

**解説**

matrix と clip の状態を保存する(スタック)

---

### restore

メソッド

**解説**

matrix と clip の状態を復元する(スタック)

---

### fill

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 塗りつぶし範囲幅 |
| `height` | `int` | `&nbsp;` | 塗りつぶし範囲高さ |
| `colors` | `&nbsp;` | `0xffffffff` | 4頂点の頂点カラーARGB。単独数値なら単色、配列なら4頂点個別指定 |
| `shader` | `&nbsp;` | `null` | 塗りつぶしシェーダー。nullの時defaultFillShaderで塗りつぶされる |

**解説**

色での塗りつぶし

XY座標はmatrixで指定する。

---

### drawMesh

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | テクスチャや頂点情報まで関連付けられたシェーダーを指定する |
| `count` | `int` | `&nbsp;` | 描画する頂点数 |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | トライアングルなどの指定 |
| `offset` | `int` | `0` | 頂点配列の中で描画開始するオフセット |

**解説**

メッシュ描画

メッシュ(VertexBinder:頂点情報)は、呼び出し前にshaderに関連付け(プロパティで設定)しておく必要があります。
テクスチャ情報も同様に関連付けしておく必要があります。
呼出し後shaderに関連付けた情報は解除(=void)してください。

---

### drawMesh

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | テクスチャや頂点情報まで関連付けられたシェーダーを指定する |
| `index` | `VertexBinder` | `&nbsp;` | インデックスバッファを指定する |
| `count` | `int` | `&nbsp;` | 描画するインデックス数 |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | トライアングルなどの指定 |

**解説**

メッシュ描画のインデックスバッファ使用版

メッシュ(VertexBinder:頂点情報)は、呼び出し前にshaderに関連付け(プロパティで設定)しておく必要があります。
テクスチャ情報も同様に関連付けしておく必要があります。
呼出し後shaderに関連付けた情報は解除(=void)してください。

---

### drawTexture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 描画に使用するテクスチャを指定します |

**解説**

1枚のテクスチャを描画

defaultShaderで描画されます。
位置や拡大縮小、回転は matrix で指定します。
テクスチャはTextureクラスだけでなく、Offscreenクラスを指定しても問題ありません。
Offscreenクラスを指定する場合は、renderTargetからそのOffscreenクラスは外されていることが前提(循環しないように)です。

---

### drawTexture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 描画に使用するテクスチャを指定します |
| `shader` | `ShaderProgram` | `&nbsp;` | 描画に使用するシェーダーを指定します |

**解説**

1枚のテクスチャをシェーダー指定して描画

位置や拡大縮小、回転は matrix で指定します。
テクスチャはTextureクラスだけでなく、Offscreenクラスを指定しても問題ありません。
Offscreenクラスを指定する場合は、renderTargetからそのOffscreenクラスは外されていることが前提(循環しないように)です。

---

### drawTexture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 描画に使用するテクスチャを指定します |
| `texture2` | `Texture` | `&nbsp;` | 描画に使用する2枚目のテクスチャを指定します |
| `shader` | `ShaderProgram` | `&nbsp;` | 描画に使用するシェーダーを指定します |

**解説**

2枚のテクスチャをシェーダー指定して描画

位置や拡大縮小、回転は matrix で指定します。
テクスチャはTextureクラスだけでなく、Offscreenクラスを指定しても問題ありません。
Offscreenクラスを指定する場合は、renderTargetからそのOffscreenクラスは外されていることが前提(循環しないように)です。

---

### drawTexture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 描画に使用するテクスチャを指定します |
| `texture2` | `Texture` | `&nbsp;` | 描画に使用する2枚目のテクスチャを指定します |
| `texture3` | `Texture` | `&nbsp;` | 描画に使用する3枚目のテクスチャを指定します |
| `shader` | `ShaderProgram` | `&nbsp;` | 描画に使用するシェーダーを指定します |

**解説**

3枚のテクスチャをシェーダー指定して描画

位置や拡大縮小、回転は matrix で指定します。
テクスチャはTextureクラスだけでなく、Offscreenクラスを指定しても問題ありません。
Offscreenクラスを指定する場合は、renderTargetからそのOffscreenクラスは外されていることが前提(循環しないように)です。
OpenGL ES 2.0の場合はテクスチャ最大8枚、3.0は頂点側最大16枚，フラグメント側最大16枚なので、まだ追加できますが、とりあえずは3枚まで定義しています。
将来的にはテクスチャを配列で渡すバージョンを作り、4枚以上はそちらで対応も検討します。

---

### drawTextureAtlas

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | テクスチャ内で描画する矩形領域 |
| `texture` | `Texture` | `&nbsp;` | 描画するテクスチャ |

**解説**

テクスチャの一部分を描画

defaultShaderで描画されます。

---

### drawTextureAtlas

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | テクスチャ内で描画する矩形領域 |
| `texture` | `Texture` | `&nbsp;` | 描画するテクスチャ |
| `shader` | `ShaderProgram` | `&nbsp;` | 描画に使用するシェーダー |

**解説**

テクスチャの一部分を描画(シェーダー指定あり)

---

### draw9Patch

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `txture` | `Texture` | `&nbsp;` |  |
| `width` | `int` | `&nbsp;` | 描画する幅 |
| `height` | `int` | `&nbsp;` | 描画する高さ |
| `shader` | `ShaderProgram` | `null` | 描画に使用するシェーダー。省略可能。 |

**戻り値**

マージン情報を返します。

**解説**

9patchを利用して描画

描画に使用するTextureは9patch情報が読み込まれている必要があります。
指定できるのはTextureクラスのみです。

---

### flush

メソッド

**解説**

描画をフラッシュする

描画を反映したいrenderTargetを入れ替える場合などに使われます。
onDraw中にrenderTargetを入れ替えると、内部的にflushは呼ばれるので、明示的な呼び出しは不要です。

---

### drawText

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `font` | `Font` | `&nbsp;` | フォント |
| `x` | `int` | `&nbsp;` | X位置 |
| `y` | `int` | `&nbsp;` | Y位置 |
| `text` | `string` | `&nbsp;` | テキスト |
| `color` | `int` | `&nbsp;` | 色指定 |

**解説**

テキスト描画(未実装)

---
