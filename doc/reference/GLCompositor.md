# GLCompositor

OGLDrawDevice を使わない状況 (画面の描画デバイスが D3D11 や
SDL_Renderer 等) でも、裏で OpenGL ES によるオフスクリーン合成を行い、その結果を
Layer へ書き戻すためのクラスです。

旧 krkrgles プラグインの GLESAdaptor 相当の機能を、本体内蔵かつ Canvas / Offscreen の
既存 GL 描画コードを共有する形で提供します。描画デバイスに依存せず、ウィンドウから
GL コンテキストを取得して自前でカレント化します (画面への present は行わず、
オフスクリーン FBO への描画のみ)。OGL 描画デバイスが動作中の場合はそのコンテキストを
共有します。

capture() のコールバックは「incontextof このコンポジタ」で実行され、
コールバック内の this はこの GLCompositor になります。そのため this.canvas
(内部 Canvas) の フル API (drawTexture / beginEffect / endEffect / クリップ等) や
this.drawLayer / this.copyLayer をそのまま利用できます (GLESAdaptor 互換)。

## メンバー一覧

### コンストラクタ

- [GLCompositor](#glcompositor)

### プロパティ

- [canvas](#canvas)
- [blendMode](#blendmode)
- [unpremultiply](#unpremultiply)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [GLGetProcAddress](#glgetprocaddress)

### メソッド

- [capture](#capture)
- [drawLayer](#drawlayer)
- [copyLayer](#copylayer)
- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)

---

### GLCompositor

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `window` | `Window` | `&nbsp;` | 対象の Window オブジェクト |

**解説**

GLCompositor を生成。

指定ウィンドウの GL コンテキストで初期化します。

---

### canvas

プロパティ \ アクセス: `r`

**解説**

内部 Canvas。

drawTexture / beginEffect / endEffect / クリップ等、Canvas の
フル API を利用できます。

---

### blendMode

プロパティ \ アクセス: `r/w`

**解説**

描画の合成モード指定。

内部 Canvas の blendMode に対応します。

---

### unpremultiply

プロパティ \ アクセス: `r/w`

**解説**

capture の読み戻しで un-premultiply するか (既定 false)。

true にすると capture() の読み戻し時に premultiplied-alpha を
straight-alpha へ戻して (RGB = RGB×255÷A) Layer へ書き込みます。MSAA を効かせた
3D (VRM 立ち絵等) の半透明縁が premultiplied のまま読み戻ると、通常アルファ合成
(ltAlpha) で縁に白フリンジが出るのを防ぎます。旧 GLESAdaptor.unpremultiply 相当。

---

### screenWidth

プロパティ \ アクセス: `r/w`

**解説**

オフスクリーン合成の既定幅。

---

### screenHeight

プロパティ \ アクセス: `r/w`

**解説**

オフスクリーン合成の既定高さ。

---

### GLGetProcAddress

プロパティ \ アクセス: `r`

**解説**

GL エントリポイント解決関数へのポインタ (整数)。

GLES 系プラグイン (EffekseerDevice 等) の oglbase として利用します。
例: new EffekseerDevice(compositor)。

---

### capture

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 描画結果の書き戻し先 Layer |
| `callback` | `&nbsp;` | `&nbsp;` | 描画コールバック function(w:int, h:int, param) (this=GLCompositor) |
| `param` | `&nbsp;` | `&nbsp;` | callback へ渡す任意の値 |
| `color` | `int` | `&nbsp;` | クリア色 (ARGB) |

**解説**

オフスクリーン合成を実行し、結果を layer へ書き戻す。

layer のサイズのオフスクリーン FBO を color でクリアしたのち、
callback(w, h, param) を「incontextof このコンポジタ」で呼び出して描画させ、
その結果を layer のメインイメージへ読み戻します。callback 内では this が
この GLCompositor になるので、this.canvas を使って drawTexture / beginEffect /
クリップ等の描画が行え、this.drawLayer / this.copyLayer も直接利用できます
(GLESAdaptor 互換。canvas は引数ではなく this.canvas で参照します)。

---

### drawLayer

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 描画元 Layer |
| `a` | `real` | `&nbsp;` | 変換行列 m11 |
| `b` | `real` | `&nbsp;` | 変換行列 m12 |
| `c` | `real` | `&nbsp;` | 変換行列 m21 |
| `d` | `real` | `&nbsp;` | 変換行列 m22 |
| `tx` | `real` | `&nbsp;` | 平行移動 x |
| `ty` | `real` | `&nbsp;` | 平行移動 y |
| `opacity` | `int` | `255` | = 255 不透明度 (0〜255) |

**解説**

layer をアフィン変換 + 不透明度で現在の描画先へ描く。

capture() のコールバック内から呼び出します。変換行列は
2x2 部 (a,b,c,d) + 平行移動 (tx,ty) で指定します。

---

### copyLayer

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 描画元 Layer |
| `left` | `int` | `&nbsp;` | 配置 x |
| `top` | `int` | `&nbsp;` | 配置 y |

**解説**

layer を (left, top) にそのまま描く。

drawLayer の単純平行移動版です。capture() のコールバック内から
呼び出します。

---

### setScreenSize

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 幅 |
| `height` | `int` | `&nbsp;` | 高さ |

**解説**

オフスクリーン合成の既定サイズを設定。

---

### makeCurrent

メソッド

**解説**

この GLCompositor の GL コンテキストをカレントにする。

---
