# Canvas ポストエフェクト / クリッピング

[Canvas](../../reference/Canvas.md) クラスの描画に、GPU 内で完結する
ポストエフェクト (色調加工・ぼかし等) と画像クリッピングを適用する機構です。

もともと gles プラグイン (`GLESAdaptor`) で拡張されていた機構を本体へ
取り込んだもので、コマンド仕様はプラグインと互換です。OGLDrawDevice
(OpenGL 描画) でのみ動作します。

## ポストエフェクト

```tjs
canvas.beginEffect();
    canvas.drawTexture(tex);        // 捕捉対象 (何を描いてもよい)
canvas.endEffect([
    %[ cmd:"grayscale" ],
    %[ cmd:"gamma", value:1.3 ],
]);
```

`beginEffect()` 〜 `endEffect(commands)` で囲んだ描画を中間バッファ
(透明クリア済み) に捕捉し、`commands` (加工コマンド配列) を順に適用して
から、現在の `blendMode` で直前の描画先へ合成します。ネスト可。
`commands` を省略すると素通し合成。加工は CPU 読み戻しなしに GPU 内で
完結します。

### 処理の分類 (内部構造)

| 種別 | コマンド | パス構成 |
|---|---|---|
| LUT 系 | `gamma` / `adjustGamma`, `light`, `lut` | per-channel 256 段 LUT に帰着。連続するものは CPU 側で 1 枚に合成し 1 パス |
| 混合系 | `grayscale`, `colorize`, `modulate`, `noise`, `generateWhiteNoise`, `overcolor` | オペコードループ 1 パスに融合 |
| 近傍系 | `boxBlur`, `gaussianBlur` | 重み付き分離畳み込み (H/V 2 パス、中間 FBO で ping-pong) |

チェーンコンパイラはカテゴリ境界で融合を区切ります。

### コマンド一覧

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
      type は吉里吉里の合成モード値 (tTVPBlendOperationMode):
        1=Opaque 2=Alpha(既定) 3=Additive 4=Subtractive 5=Multiplicative
        8=Dodge 9=Darken 10=Lighten 11=Screen 12=AddAlpha
        13=PsNormal 14=PsAdditive 15=PsSubtractive 16=PsMultiplicative
        17=PsScreen 18=PsOverlay 19=PsHardLight 20=PsSoftLight
        21=PsColorDodge 22=PsColorDodge5 23=PsColorBurn
        24=PsLighten 25=PsDarken 26=PsDifference 27=PsDifference5
        28=PsExclusion

近傍処理 (中間バッファを介して H/V 2 パス):
  %[ cmd:"boxBlur", area:r, iter:n ]
      半径 r の一様ぼかしを n 回 (iter 既定 1)

  %[ cmd:"gaussianBlur", radius:r ]
      半径 r のガウスぼかし
```

各演算は吉里吉里本体 (`TVPDoGrayScale` / `TVPAdjustGamma`) と layerExImage
プラグイン、および吉里吉里 GPU 描画の blendmode GLSL に合わせています。
ただし以下は原理的に完全一致せず、視覚的同等を狙っています:

- `noise` / `generateWhiteNoise` — CPU の `rand()` 列は再現不能なため座標ハッシュで代替
- `boxBlur` / `gaussianBlur` の最外周 — CPU は端で重み再正規化、GPU は `CLAMP_TO_EDGE`
- `colorize` — CPU は整数 HSL 丸め、GPU は同アルゴリズムの浮動小数版

## クリッピング

矩形クリップは既存の `canvas.clipRect` (Rect) + `canvas.enableClipRect` を
そのまま使います。scissor はエフェクト / マスクの**合成時にも適用**されます。

画像クリップは二方式:

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

- `endMaskClip(mask, x, y)` — mask は `Texture` / `Offscreen`。
  CPU 版 `Layer.clipAlphaRect` の第8引数 0 相当 (マスク矩形の外側は完全クリップ)。
- `beginStencilClip` はマスク α をステンシルへ書き込んで切り抜きます。自前で
  ステンシルを使う描画とは競合するので、その場合は mask 方式を使ってください。
  Offscreen (renderTarget) の FBO は D24S8 付きなのでオフスクリーンでも機能します。

## 注意事項

- シェーダは GLSL ES 3.00。GLES2 フォールバック環境 (EGL 2.0 コンテキスト)
  ではエフェクトはコンパイルに失敗して素通しになります (ログに出ます)。
  マスク / ステンシルクリップは ES2 シェーダなので動作します。
- `beginEffect` / `beginMaskClip` の閉じ忘れは `EndDrawing` (フレーム終端) で
  破棄され、警告ログが出ます。
- Canvas の既定シェーダの `a_opacity` uniform は**既定値 1.0** (Canvas 生成時に
  設定されます)。半透明にしたい場合のみ `canvas.defaultShader.a_opacity` を
  変更します。自作シェーダで `a_opacity` を宣言した場合は従来どおり自分で
  設定が必要です (未設定の uniform は GL 初期値 0 = 完全透明)。
- gles プラグインとの対応: `GLESAdaptor.drawLayer` → `Canvas.drawTexture`
  (+Matrix32)、`GLESTexture` → `Texture`、`capture` → `renderTarget`
  (Offscreen) + `Canvas.capture`。`setClipRect/clearClipRect` →
  `clipRect`/`enableClipRect`。`beginEffect/endEffect/beginMaskClip/endMaskClip/
  beginStencilClip/endStencilClip` は同名で互換。
