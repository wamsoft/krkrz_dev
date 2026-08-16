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
- [drawTransition](#drawtransition)
- [drawTransition](#drawtransition)
- [drawTextureAtlas](#drawtextureatlas)
- [drawTextureAtlas](#drawtextureatlas)
- [draw9Patch](#draw9patch)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)
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

既定シェーダーの a_opacity uniform は Canvas 生成時に 1.0 が設定される。
半透明で描画したい場合のみ `canvas.defaultShader.a_opacity` を変更する。
自作シェーダーで a_opacity を宣言した場合は呼び出し側での設定が必要
(未設定の uniform は GL 初期値 0 = 完全透明になる点に注意)。

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

### drawTransition

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | 表側 ( phase=0.0 で表示される ) テクスチャ |
| `back` | `Texture` | `&nbsp;` | 裏側 ( phase=1.0 で表示される ) テクスチャ |
| `phase` | `real` | `&nbsp;` | 進行度 0.0〜1.0 ( 範囲外はクランプされます ) |

**解説**

表裏 2 枚のテクスチャをクロスフェード描画

front → back を進行度 phase で混色して描画します。
シェーダーは内蔵されているため ShaderProgram を用意する必要はありません。
位置や拡大縮小、回転は matrix で指定します ( drawTexture と同じ規約で、
blendMode / クリップにも従います )。
テクスチャは Texture クラスだけでなく Offscreen クラスも指定できます。

---

### drawTransition

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | 表側テクスチャ |
| `back` | `Texture` | `&nbsp;` | 裏側テクスチャ |
| `phase` | `real` | `&nbsp;` | 進行度 0.0〜1.0 |
| `rule` | `Texture` | `&nbsp;` | rule 画像テクスチャ ( tcfAlpha )。null でクロスフェード |
| `vague` | `int` | `64` | 境界ぼかし幅 ( rule 値スケール 0〜255 ) |

**解説**

表裏 2 枚のテクスチャをユニバーサルトランジション描画

rule 画像 ( グレースケール ) の値が小さい画素ほど早く back 側へ
切り替わります。切替の閾値は phase * (1 + vague/255) をスイープするため、
phase=1.0 で必ず全画素が back になります。境界は vague の幅でぼかされます。

rule テクスチャは tcfAlpha 形式で作成してください
( 例: `new Texture("rule.png", tcfAlpha)` )。rule に null を渡すと
クロスフェードとして動作します。

Elements ダイアログのフロー画面切替エフェクト ( JSON `transitions` の
`effect` / `rule` / `vague` ) と同じ意味論・同じ rule 資材が使えます。

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

### beginEffect

メソッド

**解説**

ポストエフェクトの捕捉を開始する

ここから [endEffect](#endeffect) までの描画を中間バッファ
(透明クリア済み) に捕捉する。ネスト可。閉じ忘れはフレーム終端で破棄され
警告ログが出る。
コマンド仕様や内部構造の詳細は
[3D グラフィックシステム](../guide/Graphic3DSystem.md) を参照。

**関連:** [Canvas.endEffect](Canvas.md#endeffect)

---

### endEffect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `commands` | `null` | 加工コマンド ( Dictionary ) の配列。省略すると素通し合成。 |

**解説**

捕捉した描画に加工コマンド列を適用して合成する

[beginEffect](#begineffect) からの描画に commands を順に
適用し、現在の blendMode で直前の描画先へ合成する。加工は CPU 読み戻し
なしに GPU 内で完結する。

コマンドは `%[ cmd:"名前", ... ]` の Dictionary 配列で指定する:
LUT 系 ( gamma / adjustGamma / light / lut )、
混合系 ( grayscale / colorize / modulate / noise / generateWhiteNoise /
overcolor )、近傍系 ( boxBlur / gaussianBlur )。
各コマンドのパラメータと融合規則は
[3D グラフィックシステム](../guide/Graphic3DSystem.md) を参照。

**関連:** [Canvas.beginEffect](Canvas.md#begineffect)

---

### beginMaskClip

メソッド

**解説**

マスククリップの捕捉を開始する

ここから [endMaskClip](#endmaskclip) までの描画を捕捉する。
どんな描画にも安全に使える画像クリップ方式。

**関連:** [Canvas.endMaskClip](Canvas.md#endmaskclip)

---

### endMaskClip

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | マスクに使う Texture / Offscreen。void で素通し合成。 |
| `x` | `int` | `&nbsp;` | マスクを置く X 位置 |
| `y` | `int` | `&nbsp;` | マスクを置く Y 位置 |

**解説**

捕捉した描画にマスクの α を乗算して合成する

mask の α を乗算して直前の描画先へ合成する。マスク矩形の
外側は α=0 (完全クリップ)。CPU 版 Layer.clipAlphaRect 相当。

**関連:** [Canvas.beginMaskClip](Canvas.md#beginmaskclip)

---

### beginStencilClip

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | マスクに使う Texture / Offscreen |
| `x` | `int` | `&nbsp;` | マスクを置く X 位置 |
| `y` | `int` | `&nbsp;` | マスクを置く Y 位置 |
| `threshold` | `int` | `1` | α 閾値 ( 1〜255 ) |

**解説**

ステンシルクリップを開始する

マスクの α をステンシルバッファへ書き込み、
[endStencilClip](#endstencilclip) までの描画を切り抜く。単純なテクスチャ
描画向けの軽量方式 (自前でステンシルを使う描画とは競合するので、その
場合はマスククリップを使う)。

**関連:** [Canvas.endStencilClip](Canvas.md#endstencilclip)

---

### endStencilClip

メソッド

**解説**

ステンシルクリップを終了する

**関連:** [Canvas.beginStencilClip](Canvas.md#beginstencilclip)

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
