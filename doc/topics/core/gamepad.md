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

### `VK_PAD1`〜`VK_PAD4` はボタンの**刻印**で決まります ( SDL3 / 汎用ビルド )

`VK_PAD1` = 刻印 **A** ( PlayStation では **✕** )、`VK_PAD2` = **B** ( **○** )、
`VK_PAD3` = **X** ( **□** )、`VK_PAD4` = **Y** ( **△** ) に割り当てられます。

任天堂系のコントローラは A/B・X/Y の**位置**が Xbox 系と入れ替わっているため、
位置で割り当てると「画面に『A で決定』と出ているのに刻印 B のボタンで決定される」
というずれが起きます。刻印基準にすることで、どのメーカーのコントローラでも
表示と実際に押すボタンが一致します。

| | Xbox 系 | PlayStation 系 | 任天堂系 |
|---|---|---|---|
| `VK_PAD1` | A ( 下 ) | ✕ ( 下 ) | **A ( 右 )** |
| `VK_PAD2` | B ( 右 ) | ○ ( 右 ) | **B ( 下 )** |
| `VK_PAD3` | X ( 左 ) | □ ( 左 ) | **X ( 上 )** |
| `VK_PAD4` | Y ( 上 ) | △ ( 上 ) | **Y ( 左 )** |

Windows ネイティブ ( WINVER ) ビルドのパッド入力は XInput ベースで、ボタンの刻印が
Xbox 系に固定されているため位置と刻印が食い違いません ( 下記の設定も WINVER には
ありません )。

従来の位置基準に戻したい場合は
[System.padButtonMapping](../../reference/System.md#padbuttonmapping) `= "position"`
または起動オプション `-padbuttons=position` を指定します。刻印が判定できない
コントローラでは自動的に位置基準へフォールバックします。

この割り当ては「SDL のボタン → `VK_PAD*`」の唯一の分岐点で行われるため、
ゲーム側の `padKeyMap` と Elements ダイアログのパネル操作の**両方に同時に効きます**。
解決結果はパッドごとに 1 回ログへ出るので、実機での確認に使えます。

### 位置で指したいボタンは `VK_PAD_FACE_*`

フェイスボタン 4 つには、刻印基準の `VK_PAD1`〜`VK_PAD4` とは別に、**位置**で指す
仮想キーがあります。

| キーコード | 位置 | Xbox 系の刻印 | 任天堂系の刻印 |
|---|---|---|---|
| `VK_PAD_FACE_SOUTH` (0x1D4) | 下 | A | B |
| `VK_PAD_FACE_EAST` (0x1D5) | 右 | B | A |
| `VK_PAD_FACE_WEST` (0x1D6) | 左 | X | Y |
| `VK_PAD_FACE_NORTH` (0x1D7) | 上 | Y | X |

同じ物理ボタンの 1 回の押下で**刻印側と位置側の両方のキーイベントが届く**ので、
割り当てる側がボタンごとに「刻印で揃える」「位置で揃える」を選べます
(例: 決定は刻印の A = `VK_PAD1`、「上のボタンで開くメニュー」は
`VK_PAD_FACE_NORTH`)。`padButtonMapping` の設定にかかわらず、位置側は常に
物理的な配置を指します。

ボタンガイドの表示側も同じ 2 系統を持っています (Elements の `pad_icon` は
`face_north` と `y` の両方の名前を受けます)。割り当てと表示は同じ基準どうしで
組にしてください。

### `System.padStyle` — ボタン絵をどの系統にするか

接続しているパッドのボタン表記の系統は
[System.padStyle](../../reference/System.md#padstyle) (読み取り専用) で取得
できます。`"xbox"` / `"ps"` / `"switch"` のいずれか、判定できないときは
空文字列です。操作ガイドに表示するボタン絵の選択に使えます。Elements の
[ElementsDialog.setPadTheme](../../reference/ElementsDialog.md#setpadtheme) に `"auto"` を
指定すると、この判定に基づいてボタン絵テーマが自動選択されます (画面を開く
たびに決め直されるため、コントローラの差し替えにも追従します)。

### Elements ダイアログとの関係

[Dialog](../../reference/ElementsDialog.md) のパネルがキーボードフォーカスを持っていると、
`VK_PAD*` はパネルのウィジェット操作 (十字 = フォーカスナビ / A = 決定 / B =
cancel) に消費されます。「このパッドボタンだけは必ずゲーム側で受けたい」場合は
[ElementsDialog.registerHotKey](../../reference/ElementsDialog.md#registerhotkey) で登録すると、
ダイアログをバイパスして `Window.onKeyDown` へ直行します (入力の配送優先順位は
[Dialog ガイド](../../guide/ElementsDialog.md) を参照)。逆に画面 JSON 側から
「この入力はゲームのもの」と宣言するには、`"bindings"` で
`"action": "passthrough"` を指定します (パネルが消費せず素通しになります。
`"none"` は消費した上で何もしない点が違います)。

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
- `System.padStyle` … 最後に操作したパッドのボタン表記の系統 (`"xbox"` / `"ps"` /
  `"switch"`、不明なら空文字列)。ボタン絵の選択に使う (前節)
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

- **SDL3 / その他**: `SDL_Gamepad` ベース。多機種対応。同梱の
  `gamecontrollerdb.txt` があればパッドを開く前に読み込み、SDL 標準のマッピングに
  無いコントローラも認識できます。
- **WINVER (Windows ネイティブ)**: **XInput** ベース (最大 4 台・振動対応)。Xbox 系
  コントローラが対象で、汎用 DirectInput パッドは対象外です。

デバッグ表示 (ボタンマトリクス + 軸値のオーバレイ) は
[PadOverlay](pad_overlay.md) を参照してください。エンジン内部の設計詳細は
`src/core/doc/Gamepad.md` (SSOT) にあります。
