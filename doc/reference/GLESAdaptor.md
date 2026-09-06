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

===================================================================== ポストエフェクト (描画後処理) beginEffect() ～ endEffect() で囲んだ描画を中間バッファに捕捉し、 画像加工コマンド列を GPU 上で適用してから直前の描画先へ合成する。 capture() のコールバック内で、モジュール(Live2D / drawLayer 等) の描画ごとに個別のエフェクトを掛けられる。ネスト可。 =====================================================================

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
--------------------------------------------------------------------- コマンド一覧 (endEffect の commands 配列に並べる) ● 点処理 (連続すると 1 パスに融合される) %[ cmd:"grayscale" ] グレースケール化  Y=(19*B+183*G+54*R)>>8 %[ cmd:"gamma", value:r ]                     // 全チャンネル一括 %[ cmd:"gamma", rgamma:.., rfloor:.., rceil:.., ggamma:.., gfloor:.., gceil:.., bgamma:.., bfloor:.., bceil:.. ] // チャンネル別 ガンマ補正  out = pow(in/255, 1/gamma)*(ceil-floor)+floor (本体 Layer.adjustGamma と同じ。floor 既定 0 / ceil 既定 255) %[ cmd:"light", brightness:b, contrast:c ] 明度 b(-255～255) / コントラスト c(-100～100) %[ cmd:"lut", table:[ ...256要素... ] ] 全チャンネル共通の 256 段ルックアップテーブル %[ cmd:"colorize", hue:h, sat:s, blend:b ] 色相 h(0～255) / 彩度 s(0～255) / 合成率 b(0～1) %[ cmd:"modulate", hue:h, saturation:s, luminance:l ] 色相 h(-180～180) / 彩度 s(-100～100) / 輝度 l(-100～100) %[ cmd:"noise", level:n ] ノイズ付加 n(0～255) %[ cmd:"generateWhiteNoise" ] グレースケールのホワイトノイズ生成 (α は保持) %[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ] 指定色での全体塗りつぶし合成 (吉里吉里 fillOperateRect 準拠)。 color の上位8bit(AA) と opacity(0～255,既定255) が合成αになる。 type は吉里吉里の合成モード値 (tTVPBlendOperationMode): 1=Opaque 2=Alpha(既定) 3=Additive 4=Subtractive 5=Multiplicative 8=Dodge 9=Darken 10=Lighten 11=Screen 12=AddAlpha 13=PsNormal 14=PsAdditive 15=PsSubtractive 16=PsMultiplicative 17=PsScreen 18=PsOverlay 19=PsHardLight 20=PsSoftLight 21=PsColorDodge 22=PsColorDodge5 23=PsColorBurn 24=PsLighten 25=PsDarken 26=PsDifference 27=PsDifference5 28=PsExclusion ● 近傍処理 (中間バッファを介して H/V 2 パス) %[ cmd:"boxBlur", area:r, iter:n ] 半径 r の一様ぼかしを n 回 (iter 既定 1) %[ cmd:"gaussianBlur", radius:r ] 半径 r のガウスぼかし ※ noise / blur の最外周 / colorize は CPU 版と完全一致ではなく視覚的同等。 --------------------------------------------------------------------- ===================================================================== クリッピング (AffineLayer の clip / clipImage 相当) 矩形クリップ   : setClipRect / clearClipRect。scissor で実現。 画像クリップ   : 二方式 mask 方式    : beginMaskClip() ～ endMaskClip() で囲んだ描画を 中間バッファに捕捉し、マスク画像の α を乗算しながら 直前の描画先へ合成する。マスク矩形の外側は α=0。 (CPU 版 Layer.clipAlphaRect の第8引数 0 相当) 描画モジュール (Live2D 等) にも安全に使える。 stencil 方式 : beginStencilClip() ～ endStencilClip()。 マスク α をステンシルに書き込み描画を切り抜く。 α は閾値で2値化される。描画モジュールが自前で ステンシルを使う場合は競合するため drawLayer による単純テクスチャ描画専用。 =====================================================================

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
