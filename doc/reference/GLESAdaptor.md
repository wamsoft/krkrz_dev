# GLESAdaptor

OpenGL ES の描画コンテキストを保持できるアダプター (EGLベース)

描画に使うオブジェクトは egl を使ってコンテキスト処理する前提になります

## メンバー一覧

### コンストラクタ

- [GLESAdaptor](#glesadaptor)

### プロパティ

- [screenWidth](#screenwidth)
- [screenHeihgt](#screenheihgt)
- [blendMode](#blendmode)

### メソッド

- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)
- [capture](#capture)
- [copyLayer](#copylayer)
- [drawLayer](#drawlayer)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [setClipRect](#setcliprect)
- [clearClipRect](#clearcliprect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)

---

### GLESAdaptor

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 対象ウインドウ |

**解説**

コンストラクタ

---

### screenWidth

プロパティ \ アクセス: `r/w`

**解説**

スクリーン横幅

---

### screenHeihgt

プロパティ \ アクセス: `r/w`

**解説**

スクリーン縦幅

---

### blendMode

プロパティ \ アクセス: `r/w`

**解説**

ブレンドモード (tTVPBlendMode 相当: 0=Disable,1=Opaque,2=Alpha,3=Add,...)

---

### setScreenSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

スクリーンサイズの設定

---

### makeCurrent

メソッド

**解説**

OpenGL コンテキスト設定

---

### capture

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 結果格納先レイヤ |
| `callback` | `&nbsp;` | 処理関数  function(width, height, param)  このオブジェクトのコンテキストで実行されます |
| `param` | `&nbsp;` | 追加パラメータ |
| `color` | `&nbsp;` | 塗りつぶし色 |

**解説**

OpenGL描画処理実行

---

### copyLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | レイヤ または GLESTexture |
| `left` | `&nbsp;` | 左位置 |
| `top` | `&nbsp;` | 上位置 |

**解説**

レイヤのコピー

---

### drawLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | レイヤ または GLESTexture |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |
| `d` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |
| `opacity` | `&nbsp;` | 不透明度 0～255 (省略時 255) |

**解説**

レイヤの描画

---

### beginEffect

メソッド

**解説**

エフェクト捕捉の開始

以降の描画は中間フレームバッファ(透明クリア済み)へ行われる。
対応する endEffect() を必ず呼ぶこと。

---

### endEffect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `commands` | `&nbsp;` | 加工コマンドの配列。各要素は辞書で cmd メンバに種別、<br>残りのメンバにパラメータを持つ。下記「コマンド一覧」参照。 |
| `opacity` | `255` | 合成時の不透明度(0～255、省略時 255)。α に乗算される。<br>Live2D のように自前描画で opacity を解釈しない<br>モジュールのレイヤ不透明度を反映するのに使う。<br>加工不要なら commands に空配列を渡せば<br>「捕捉して opacity 付きで合成するだけ」になる。<br>例) [ %[ cmd:"grayscale" ], %[ cmd:"gamma", value:1.2 ] ] |

**解説**

エフェクト適用と合成

直前の beginEffect() 以降に描画された内容へ commands を順に適用し、
現在の blendMode で直前の描画先へ合成する。

---

### setClipRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

矩形クリップの設定

以降の drawLayer / endEffect / endMaskClip の合成が矩形内に制限される。
描画モジュールが scissor 状態を尊重する場合は直接描画にも効くが、
確実にクリップしたい場合は beginMaskClip/endMaskClip で囲むこと。

---

### clearClipRect

メソッド

**解説**

矩形クリップの解除

---

### beginMaskClip

メソッド

**解説**

マスククリップ捕捉の開始

以降の描画は中間フレームバッファ(透明クリア済み)へ行われる。
対応する endMaskClip() を必ず呼ぶこと。beginEffect() とネスト可。

---

### endMaskClip

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mask` | `&nbsp;` | マスク画像 (GLESTexture または Layer)。void なら素通し合成<br>(矩形クリップだけを合成時に確実に適用したい場合に使う) |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

マスク適用合成

直前の beginMaskClip() 以降に描画された内容へマスク画像の α を
乗算し、現在の blendMode で直前の描画先へ合成する。
マスク矩形の外側は α=0 (完全クリップ)。

---

### beginStencilClip

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mask` | `&nbsp;` | マスク画像 (GLESTexture または Layer) |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `threshold` | `&nbsp;` | クリップを有効とする α 閾値 (1～255、省略不可) |

**解説**

ステンシルクリップの開始

マスク画像の α が閾値以上の領域をステンシルへ書き込み、
以降の drawLayer をその領域内に切り抜く。

---

### endStencilClip

メソッド

**解説**

ステンシルクリップの終了

---
