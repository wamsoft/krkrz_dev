# ゲームパッド

吉里吉里Z のゲームパッド (ジョイスティック) 入力の使い方をまとめます。個々の
API の詳細は [System クラスリファレンス](../../reference/System.md) を参照してください。

## パッド番号 (論理インデックス)

すべてのパッド API はパッド番号 `no` を取ります。番号の意味は共通です。

- **`0`** … 「**最後に操作したパッド**」を指す特別番号。実際に触ったパッドへ
  自動的に追従します。
- **`1` 以上** … 接続順の実パッド (`1` = 1 台目, `2` = 2 台目, …)。接続台数は
  `System.getJoypadCount()` で取得できます。

**ボタン押下のキーイベント (後述) は常に `0` 番 = 最後に操作したパッドを発生源**と
します。1 台だけ接続している場合は `0` と `1` が同じパッドを指します。

「最後に操作したパッド」の切り替わりは、ボタン / 十字キーの押下で判定します
(アナログスティックの微小なドリフトでは切り替わりません)。

## ボタン入力 (キーイベント)

ボタンはキーイベントとして届きます。`Window.onKeyDown` / `onKeyUp` で
`VK_PAD1`〜`VK_PAD12` / `VK_PADLEFT`〜`VK_PADDOWN` / `VK_PAD_L_*` / `VK_PAD_R_*`
を受け取ります (キーコード一覧は [キーコード表](../../guide/KeyCodes.md) を参照)。
現在の押下状態は `System.getKeyState(VK_PADn)` でも取得できます。

```tjs
// Window を継承したクラスで
function onKeyDown(key, shift) {
    if (key == VK_PAD1) {  /* A ボタン */ }
    if (key == VK_PADLEFT) { /* 十字左 */ }
}
```

十字キー・左右スティック方向は 8 方向に量子化され、上記の方向キーとして届きます
(生のスティック値が必要なときは次節)。

### Elements ダイアログとの関係

[Dialog](../../reference/Dialog.md) のパネルがキーボードフォーカスを持っていると、
`VK_PAD*` はパネルのウィジェット操作 (十字 = フォーカスナビ / A = 決定 / B =
cancel) に消費されます。「このパッドボタンだけは必ずゲーム側で受けたい」場合は
[Dialog.registerHotKey](../../reference/Dialog.md#registerhotkey) で登録すると、
ダイアログをバイパスして `Window.onKeyDown` へ直行します (入力の配送優先順位は
[Dialog ガイド](../../guide/Dialog.md) を参照)。

コアデモ `pad_advanced` にはこの確保を ON/OFF するチェックがあり、同じボタンが
「ゲームに届く」「パネルに吸われる」と切り替わる様子をその場で比較できます。

## アナログ軸

スティックの傾き・トリガの押し込み量は `System.getPadAxis(no, axisId)` で取得します。

```tjs
var x = System.getPadAxis(0, System.padAxisLeftX);       // -1.0 〜 +1.0
var y = System.getPadAxis(0, System.padAxisLeftY);       // -1.0 〜 +1.0 (下が正)
var t = System.getPadAxis(0, System.padAxisLeftTrigger); //  0.0 〜 +1.0
```

軸 ID は `System.padAxisLeftX` / `padAxisLeftY` / `padAxisRightX` / `padAxisRightY`
/ `padAxisLeftTrigger` / `padAxisRightTrigger` の 6 種。TJS グローバル定数
`paLeftX` … `paRightTrigger` でも同じ値を指定できます。デッドゾーンは適用されない
ので、必要に応じて呼び出し側で処理してください。

!!! tip "無操作でも 0 にはならない"
    デッドゾーン未適用のため、スティックに触れていなくても実測で ±0.05 程度の
    値が返ります。「触っていないのにキャラが動く」を避けるには、呼び出し側で
    小さい値を切り捨てる処理を入れてください。挙動はコアデモ `pad_advanced`
    (スティック升目 + 生値表示) で確認できます。

## 接続の検知 / 振動

- `System.getJoypadCount()` … 接続中の実パッド台数
- `System.hasJoypad(no)` … 指定番号が有効か
- `System.getJoypadType(no)` … 機種名の文字列 (環境依存。SDL 版は認識名、WINVER 版は
  `"XInput Controller"`)
- `System.onJoypadChange(no, name)` … 最後に操作したパッドの識別名が変化したときに
  呼ばれるコールバック (パッドが無くなったときは `name` が空文字列)
- `System.rumblePad(no, low, high, durationMs)` / `System.stopRumblePad(no)` …
  振動 (low/high は 0〜255)

## パッド機能の無効化 (サポート用)

他のデバイスが誤ってゲームパッドとして認識され誤動作する、といったケースの対処
として、パッド機能を丸ごと無効化できます。無効時は状態取得もキーイベント生成も
行われません。

- 実行時: `System.padEnabled = false;` (再有効化は `= true;`)
- 起動時: コマンドラインオプション `-joypad=no` ([コマンドライン](../../guide/CommandLine.md))

`System.padEnabled` で明示指定した場合はコマンドラインより優先されます。

## プラットフォームと実装

パッド入力は全ビルド共通の論理管理層 (`tTVPPadManager`) の上に、プラットフォーム別の
バックエンドを持ちます。

- **SDL3 / その他**: `SDL_Gamepad` ベース。多機種対応。
- **WINVER (Windows ネイティブ)**: **XInput** ベース (最大 4 台・振動対応)。Xbox 系
  コントローラが対象で、汎用 DirectInput パッドは対象外です。

デバッグ表示 (ボタンマトリクス + 軸値のオーバレイ) は
[PadOverlay](pad_overlay.md) を参照してください。エンジン内部の設計詳細は
`src/core/doc/Gamepad.md` (SSOT) にあります。
