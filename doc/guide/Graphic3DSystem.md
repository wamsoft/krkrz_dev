# 3D グラフィックシステム

## 概要

吉里吉里Z は、[グラフィックシステム](GraphicSystem.md) で説明した通常のレイヤ描画 ( BasicDrawDevice / SDLDrawDevice ) に加えて、OpenGL ES ベースの GPU 描画パスを持っています。このパスは [OGLDrawDevice](../reference/OGLDrawDevice.md) を中心に、[Canvas](../reference/Canvas.md) / [Texture](../reference/Texture.md) / [ShaderProgram](../reference/ShaderProgram.md) / [Offscreen](../reference/Offscreen.md) などのクラス群で構成され、テクスチャ描画・シェーダによる加工・トランジションなどを GPU 上で直接扱えます。

これらの GL 系クラスは、[OGLDrawDevice](../reference/OGLDrawDevice.md) がアクティブな ( ウィンドウにセットされている ) 間のみ機能します。OGLDrawDevice が管理する OpenGL コンテキストに紐付いているためで、通常のレイヤ描画デバイス ( BasicDrawDevice / SDLDrawDevice ) が使われている状態では利用できません。

## OGLDrawDevice への切り替え

GPU 描画を使うには、[Window.drawDevice](../reference/Window.md#drawdevice) プロパティに [OGLDrawDevice](../reference/OGLDrawDevice.md) をセットして描画デバイスを切り替えます。

```tjs
var dev = new OGLDrawDevice();
window.drawDevice = dev;
```

OGLDrawDevice を構築した直後はまだ OpenGL コンテキストは生成されません。`Window.drawDevice` にセットしたタイミングで内部の OpenGL ES コンテキストが遅延生成・初期化されます。この初期化やその後の描画サイクルは、次のイベントで扱います。

| イベント | 発火タイミング | 用途 |
|---|---|---|
| [onInit](../reference/OGLDrawDevice.md#oninit) | GL コンテキストの生成・初期化が完了した直後 | シェーダ・テクスチャなど初期リソースの確保 |
| [onDraw](../reference/OGLDrawDevice.md#ondraw) | 描画サイクルごと | フレーム描画コマンドの発行 |
| [onDone](../reference/OGLDrawDevice.md#ondone) | デバイスの切り離し / コンテキスト破棄の直前 | onInit で確保したリソースの解放 |

## onDraw での描画処理概要

毎フレームの描画は [onDraw](../reference/OGLDrawDevice.md#ondraw) イベント内で行います。OGLDrawDevice が [Canvas](../reference/Canvas.md) を管理している場合、onDraw は内部で Canvas の BeginDrawing 〜 EndDrawing で挟まれた状態で呼ばれます。そのためハンドラ内では、デバイスの [canvas](../reference/OGLDrawDevice.md#canvas) プロパティ経由で drawTexture などの描画コマンドをそのまま発行できます ( BeginDrawing / EndDrawing を自分で呼ぶ必要はありません )。

```tjs
class MyGLDevice extends OGLDrawDevice {
    var tex;
    function onInit() {
        tex = new Texture("image.png");   // 初期リソース確保
    }
    function onDraw() {
        canvas.drawTexture(tex);          // BeginDrawing〜EndDrawing の内側
    }
    function onDone() {
        if (tex !== void) invalidate tex; // リソース解放
        tex = void;
    }
}
```

配置や変形は Canvas の `matrix` ( [Matrix32](../reference/Canvas.md) 系 ) 、合成方法は `blendMode` で制御します。

## ポストエフェクト / クリッピング

[Canvas](../reference/Canvas.md) の描画には、GPU 内で完結するポストエフェクト ( 色調加工・ぼかしなど ) と画像クリッピングを適用できます。CPU への読み戻しなしに GPU 上で処理が完結するのが特徴で、[OGLDrawDevice](../reference/OGLDrawDevice.md) がアクティブな間のみ動作します。

### ポストエフェクト

```tjs
canvas.beginEffect();
    canvas.drawTexture(tex);        // 捕捉対象 (何を描いてもよい)
canvas.endEffect([
    %[ cmd:"grayscale" ],
    %[ cmd:"gamma", value:1.3 ],
]);
```

`beginEffect()` 〜 `endEffect(commands)` で囲んだ描画を中間バッファ ( 透明クリア済み ) に捕捉し、`commands` ( 加工コマンド配列 ) を順に適用してから、現在の `blendMode` で直前の描画先へ合成します。ネスト可能です。`commands` を省略すると素通し合成になります。

加工コマンドは大きく、点処理 ( 各画素を独立に加工。連続するものは内部で 1 パスに融合 ) と、近傍処理 ( 周囲の画素を参照するぼかし ) に分かれます。

```
点処理 (連続すると 1 パスに融合):
  %[ cmd:"grayscale" ]
      グレースケール化  Y = (19*B + 183*G + 54*R) >> 8

  %[ cmd:"gamma", value:γ ]                         // 全チャンネル一括
  %[ cmd:"gamma", rgamma:.., rfloor:.., rceil:..,
                  ggamma:.., gfloor:.., gceil:..,
                  bgamma:.., bfloor:.., bceil:.. ]   // チャンネル別
      ガンマ補正  out = pow(in/255, 1/γ)*(ceil-floor)+floor
      (本体 Layer.adjustGamma 準拠。floor 既定 0 / ceil 既定 255)

  %[ cmd:"light", brightness:b, contrast:c ]
      明度 b(-255〜255) / コントラスト c(-100〜100)

  %[ cmd:"lut", table:[ ...256要素... ] ]
      全チャンネル共通の 256 段ルックアップテーブル

  %[ cmd:"colorize", hue:h, sat:s, blend:b ]
      色相 h(0〜255) / 彩度 s(0〜255) / 合成率 b(0〜1)

  %[ cmd:"modulate", hue:h, saturation:s, luminance:l ]
      色相 h(-180〜180) / 彩度 s(-100〜100) / 輝度 l(-100〜100)

  %[ cmd:"noise", level:n ]
      ノイズ付加 n(0〜255)

  %[ cmd:"generateWhiteNoise" ]
      グレースケールのホワイトノイズ生成 (α は保持)

  %[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ]
      指定色での全体塗りつぶし合成 (吉里吉里 fillOperateRect 準拠)。
      合成αは color 上位8bit(AA) × opacity(0〜255, 既定255)。
      type は吉里吉里の合成モード値 (tTVPBlendOperationMode)。

近傍処理 (中間バッファを介して H/V 2 パス):
  %[ cmd:"boxBlur", area:r, iter:n ]
      半径 r の一様ぼかしを n 回 (iter 既定 1)

  %[ cmd:"gaussianBlur", radius:r ]
      半径 r のガウスぼかし
```

各演算は吉里吉里本体 ( `TVPDoGrayScale` / `TVPAdjustGamma` ) や layerExImage プラグインの結果に合わせていますが、以下は原理的に完全一致せず、視覚的な同等を狙っています。

- `noise` / `generateWhiteNoise` — CPU の `rand()` 列は再現不能なため座標ハッシュで代替
- `boxBlur` / `gaussianBlur` の最外周 — CPU は端で重み再正規化、GPU は `CLAMP_TO_EDGE`
- `colorize` — CPU は整数 HSL 丸め、GPU は同アルゴリズムの浮動小数版

### クリッピング

矩形クリップは既存の `canvas.clipRect` ( Rect ) + `canvas.enableClipRect` をそのまま使います。scissor はエフェクト / マスクの合成時にも適用されます。

画像 ( 任意形状 ) によるクリップには 2 方式があります。

```tjs
// mask 方式 (どんな描画にも安全)
canvas.beginMaskClip();
    canvas.drawTexture(src);
canvas.endMaskClip(maskTex, 100, 100);   // mask の α を乗算、矩形外は α=0
                                          // mask に void で素通し合成

// stencil 方式 (単純テクスチャ描画専用)
canvas.beginStencilClip(maskTex, 100, 100, 1);  // α 閾値 1〜255
    canvas.drawTexture(src);
canvas.endStencilClip();
```

- `endMaskClip(mask, x, y)` — mask は [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md)。CPU 版 `Layer.clipAlphaRect` の第 8 引数 0 相当 ( マスク矩形の外側は完全クリップ ) です。
- `beginStencilClip` はマスク α をステンシルへ書き込んで切り抜きます。自前でステンシルを使う描画とは競合するので、その場合は mask 方式を使ってください。

### 注意事項

- シェーダは GLSL ES 3.00 です。GLES2 フォールバック環境 ( EGL 2.0 コンテキスト ) ではエフェクトはコンパイルに失敗して素通しになります ( ログに出ます )。マスク / ステンシルクリップは ES2 シェーダなので動作します。
- `beginEffect` / `beginMaskClip` の閉じ忘れは EndDrawing ( フレーム終端 ) で破棄され、警告ログが出ます。
- Canvas の既定シェーダの `a_opacity` uniform は既定値 1.0 ( Canvas 生成時に設定 ) です。半透明にしたい場合のみ `canvas.defaultShader.a_opacity` を変更します。自作シェーダで `a_opacity` を宣言した場合は従来どおり自分で設定が必要です ( 未設定の uniform は GL 初期値 0 = 完全透明 )。

## トランジション描画 ( drawTransition )

表 ( front ) と裏 ( back ) の 2 テクスチャを進行度 `phase` で合成して描画する Canvas の内蔵機能です。クロスフェードと、rule 画像によるユニバーサルトランジションをシェーダ内蔵で提供します。従来 TJS 層で [ShaderProgram](../reference/ShaderProgram.md) を自前生成して実装していたトランジションを、1 メソッドで置き換えられます。

```tjs
// クロスフェード
canvas.drawTransition(front, back, phase);

// ユニバーサルトランジション (rule 画像)
canvas.drawTransition(front, back, phase, ruleTex);        // vague 既定 64
canvas.drawTransition(front, back, phase, ruleTex, 128);   // vague 指定
```

| 引数 | 意味 |
|---|---|
| `front` / `back` | [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md)。phase=0 で front のみ、1 で back のみ |
| `phase` | 進行度 0.0〜1.0 ( 範囲外はクランプ ) |
| `rule` | rule 画像テクスチャ。**`tcfAlpha` で作成する** ( `new Texture("rule.png", tcfAlpha)` )。値が小さい画素ほど早く back へ切り替わる。省略 / null でクロスフェード |
| `vague` | 境界ぼかし幅 ( rule 値スケール 0〜255、既定 64 ) |

- 配置・変形・ブレンドは `drawTexture` と同じ規約 ( `canvas.matrix` / `blendMode` / クリップに従う ) です。
- ユニバーサルの閾値は `phase * (1 + vague/255)` をスイープします ( phase=1 で必ず全画素 back )。[ダイアログ](ElementsDialog.md) のフロー画面切替エフェクト ( JSON `transitions` の `effect` / `rule` / `vague` ) と同じ意味論で、同じ rule 資材が使えます。
- 内蔵シェーダは初回使用時に遅延生成されてキャッシュされます。`a_opacity` uniform ( 既定 1.0 ) で全体不透明度を掛けられます。

### 使用例 ( 画面遷移 )

```tjs
// onDraw 内: old / cur は Offscreen (旧画面と新画面をそれぞれ描いたもの)
var t = (System.getTickCount() - startTick) / duration;
if (t < 1.0) {
    canvas.drawTransition(oldScreen, curScreen, t, ruleTex, 64);
} else {
    canvas.drawTexture(curScreen);
}
```

## 参考

- [ShaderProgram / シェーダの詳しい解説 ( multi_platform_design )](https://krkrz.github.io/multi_platform_design/shader_program.html) — シェーダプログラムの記述方法や設計の詳細
- [OGLDrawDevice](../reference/OGLDrawDevice.md) — OpenGL ES 描画デバイス
- [Canvas](../reference/Canvas.md) — 描画コマンドの発行口
- [ShaderProgram](../reference/ShaderProgram.md) — シェーダプログラム
- [Texture](../reference/Texture.md) — GPU テクスチャ
- [Offscreen](../reference/Offscreen.md) — オフスクリーン描画ターゲット
