# ゲームパッド状態の観察 (PadOverlay)

SDL3 ビルドのエンジンには、画面左上にゲームパッドの状態 ( 16 ボタンの
ON/OFF と 6 軸のアナログ値 ) をリアルタイム表示するデバッグ用オーバレイ
が組み込まれています。実機 ( 例えば Switch ) でコントローラ周りの動作
確認をするときに使えます。

詳細な表示仕様と内部構造は src/core 側のガイドを参照:

- [doc/PadOverlay.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/PadOverlay.md)
- [doc/Gamepad.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Gamepad.md)

---

## 表示例

```
+--------------------------------+
| Pad: Xbox Series X Controller  |
| [A ][B ][X ][Y ]               |
| [L1][R1][L2][R2]               |
| [BK][ST][LS][RS]               |
| [Lf][Up][Rt][Dn]               |
| LX +0.45 LY -0.32              |
| RX +0.00 RY +0.00              |
| LT +0.00 RT +0.80              |
+--------------------------------+
```

- ヘッダ: SDL ゲームパッド名 ( 未接続時は `(none)` )
- セル: 押下中は緑、未押下は暗灰
- 軸: スティック軸は `-1.00 〜 +1.00`、トリガ軸は `0.00 〜 +1.00`

WINVER ビルドではパッド抽象 API を持たないため、OGLDrawDevice 経路で出した
場合は全 OFF・全軸 +0.00 の表示になります。

---

## オーバレイの有効化

- 起動時から: [`-padoverlay=1`](../../guide/CommandLine.md)
- 実行中の切替: [System.setPadOverlay](../../reference/System.md#setpadoverlay)
- [REPL](repl.md) から: `.padoverlay [on|off]`

[`-memoverlay=1`](../../guide/CommandLine.md) ( 画面右上 ) と独立に動作し、
両方同時に表示できます。

---

## TJS2 から軸を直接取得する

オーバレイは観察用ですが、スクリプトから軸のアナログ値を取得するには
[System.getPadAxis](../../reference/System.md#getpadaxis) を使います。

```tjs
var v = System.getPadAxis(0, System.padAxisLeftX);
// v は -1.0 〜 +1.0 の実数 (未接続/無効値で 0.0)
```

軸 ID 定数は [System.padAxisLeftX](../../reference/System.md#padaxisleftx)
など 6 種類が用意されています。

振動制御は [System.rumblePad](../../reference/System.md#rumblepad) /
[System.stopRumblePad](../../reference/System.md#stoprumblepad) で行えます。
ゲームパッドの接続数・存在確認は
[System.getJoypadCount](../../reference/System.md#getjoypadcount) /
[System.hasJoypad](../../reference/System.md#hasjoypad) を使います。
