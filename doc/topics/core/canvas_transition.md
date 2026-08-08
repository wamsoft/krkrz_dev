# Canvas トランジション描画 ( drawTransition )

表 ( front ) と裏 ( back ) の 2 テクスチャを進行度 `phase` で合成して描画する
Canvas の内蔵機能です。クロスフェードと、rule 画像によるユニバーサル
トランジションをシェーダー内蔵で提供します。従来 TJS 層で
[ShaderProgram](../../reference/ShaderProgram.md) を自前生成して実装していた
トランジションを 1 メソッドで置き換えられます。

## API

```tjs
// クロスフェード
canvas.drawTransition(front, back, phase);

// ユニバーサルトランジション (rule 画像)
canvas.drawTransition(front, back, phase, ruleTex);        // vague 既定 64
canvas.drawTransition(front, back, phase, ruleTex, 128);   // vague 指定
```

| 引数 | 意味 |
|---|---|
| `front` / `back` | [Texture](../../reference/Texture.md) / [Offscreen](../../reference/Offscreen.md)。phase=0 で front のみ、1 で back のみ |
| `phase` | 進行度 0.0〜1.0 ( 範囲外はクランプ ) |
| `rule` | rule 画像テクスチャ。**`tcfAlpha` で作成する** ( `new Texture("rule.png", tcfAlpha)` )。値が小さい画素ほど早く back へ切り替わる。省略 / null でクロスフェード |
| `vague` | 境界ぼかし幅 ( rule 値スケール 0〜255、既定 64 ) |

- 配置・変形・ブレンドは `drawTexture` と同じ規約 ( `canvas.matrix` /
  `blendMode` / クリップに従う )。
- ユニバーサルの閾値は `phase * (1 + vague/255)` をスイープします ( phase=1 で
  必ず全画素 back )。[Elements ダイアログの画面切替エフェクト](elements_dialog.md)
  ( JSON `transitions` の `effect` / `rule` / `vague` ) と同じ意味論・同じ
  rule 資材が使えます。
- 内蔵シェーダーは初回使用時に遅延生成されてキャッシュされます。
  `a_opacity` uniform ( 既定 1.0 ) で全体不透明度を掛けられます。

## 使用例 ( 画面遷移 )

```tjs
// onDraw 内: old / cur は Offscreen (旧画面と新画面をそれぞれ描いたもの)
var t = (System.getTickCount() - startTick) / duration;
if (t < 1.0) {
    canvas.drawTransition(oldScreen, curScreen, t, ruleTex, 64);
} else {
    canvas.drawTexture(curScreen);
}
```

## 関連

- [Canvas リファレンス](../../reference/Canvas.md)
- [Canvas ポストエフェクト / クリッピング](canvas_effect.md)
- [Elements ベースの汎用ダイアログ](elements_dialog.md) — フロー画面切替の
  CPU 版 ( 全 DrawDevice 対応 ) が同じ語彙で使えます
