# Elements UI 機構の全体像

吉里吉里Z の [Dialog](../../reference/Dialog.md) ( Elements ベースの UI ) は、**4 つの層**が
積み重なってできています。どの層に何があるか、どの層を直せばよいか、どの文書を読めば
よいかをここにまとめます。個々の使い方は [ダイアログ ( ガイド )](../../guide/Dialog.md)、
API は [Dialog クラスリファレンス](../../reference/Dialog.md) を参照してください。

## 層構造

```
┌─────────────────────────────────────────────────────────────┐
│ ④ ゲーム / TJS 側の UI コード                                  │
│    画面の出し入れ、ゲーム状態との接続、画面遷移の方針           │
│    ※ 共有の枠組みは無く、プロジェクトごとに書かれている         │
├─────────────────────────────────────────────────────────────┤
│ ③ krkrz 本体 ( src/core/common/visual/elements/ )             │
│    TJS Dialog クラス / DrawDevice への描画接続 / 入力ルーティング │
│    複数インスタンスと z-order / モーダルの nested ループ         │
│    ホスト資源との接続 ( Storages・フォント・ソフトキーボード )    │
├─────────────────────────────────────────────────────────────┤
│ ② elements_modal ( external/elements/external/elements_modal ) │
│    画面 JSON の仕様と構築、変数 store、named action、画面遷移     │
│    overlay_session ( 描画先バッファと入力を受け取るだけの口 )     │
│    ※ 吉里吉里に依存しない。単体アプリからも同じ JSON が動く      │
├─────────────────────────────────────────────────────────────┤
│ ① elements ( cycfi/elements の派生 )                          │
│    ウィジェットの土台、レイアウト計算、フォーカス、ThorVG 描画    │
└─────────────────────────────────────────────────────────────┘
```

**①②は吉里吉里Zと無関係に動きます**。画面 JSON は単体のホストアプリでも同じように
表示・操作でき、③はそれをゲーム画面の上へ載せてゲームの入力と資源に繋ぐ役です。

## どの層を直すのか ( 早見表 )

| やりたいこと | 直す層 | 具体的な場所 |
|---|---|---|
| 画面の見た目・配置・文言を変える | 画面 JSON | プロジェクトの画面 JSON |
| ウィジェットを増やす / 既存ウィジェットに属性を足す | ② | `json_layout.cpp` + elements_modal README |
| 変数連動・入力バインド・画面遷移の仕様を変える | ② | 同上 |
| ウィジェットの描画そのもの・レイアウト計算・フォーカス移動 | ① | elements 本体 (`lib/`) |
| TJS の API を増やす ( `Dialog.*` ) | ③ | `DialogIntf.cpp` + `doc/manual/Dialog.manual.tjs` |
| 表示先 ( DrawDevice ) や入力経路、複数インスタンスの扱い | ③ | `ElementsDialogManager.cpp` |
| 画面をどう出し入れするか、ゲーム状態とどう繋ぐか | ④ | ゲーム側スクリプト |

判断に迷ったときの目安は「**吉里吉里Zが無くても意味がある機能か**」です。意味があるなら
②か①、ゲーム側の事情が絡むなら③か④になります。

## データの流れ

**描画**: ゲームのフレーム末尾で `DrawDevice::Show()` から `PaintOverlay` が呼ばれ、
② がピクセルバッファへ描き、③ がそれを DrawDevice ごとのテクスチャ ( SDL / OpenGL /
D3D11 ) へ転送してゲーム画面の上に出します。再描画が不要なフレームは前回のテクスチャを
そのまま提示し、変化した矩形だけを描き直します。

**入力**: ウィンドウのマウス / キー / パッド入力を③が横取りし、表示中のダイアログへ
渡します。②が処理しなかった入力だけがゲーム ( レイヤ ) へ流れます ( 非モーダル時 )。

**値**: 画面 JSON の中の変数は 1 本のストアにぶら下がります。TJS からは
[setVar](../../reference/Dialog.md#setvar) で書き、[getVar](../../reference/Dialog.md#getvar) で
読み、[onVar](../../reference/Dialog.md#onvar) で変化を受け取れます。ボタン押下や値変更は
[onAction](../../reference/Dialog.md#onaction) で届きます。**この 4 つが③と④の間の
インターフェースの全て**です。

## ドキュメント地図

| 文書 | 層 | 内容 |
|---|---|---|
| [ダイアログ ( ガイド )](../../guide/Dialog.md) | ③④ | 表示モード、フロー、一覧、変数、入力バインドの使い方 |
| [Dialog クラスリファレンス](../../reference/Dialog.md) | ③ | TJS API の全メンバー |
| [ElementsDialog.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/ElementsDialog.md) | ③ | **本体側の実装 SSOT**。DrawDevice 接続、入力ルーティング、複数インスタンス、部分再描画、計測 |
| [elements_modal README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md) | ② | **画面 JSON 仕様の SSOT**。ウィジェット一覧、変数連動、テーマ、アトラス、遷移、演出 |
| [elements リポジトリ](https://github.com/wamsoft/elements) | ① | ライブラリ本体 ( 派生元は cycfi/elements ) |
| [ゲームパッド入力](gamepad.md) | ③ | パッドのキー変換 ( ダイアログのパッド操作もこの上に乗る ) |

## 用語

- **overlay** … ゲーム画面の上に重ねて表示する形。非モーダルもモーダルもこの形が既定
- **独立ウィンドウ modal** … OS のウィンドウを別に開いてブロッキング表示する形
- **フロー ( navigator )** … 複数の画面 JSON を遷移させる仕組み。遷移先は画面 JSON 側の
  宣言で決まり、ホストは遷移を書かない
- **画面 JSON** … 1 画面ぶんのレイアウト定義。TJS の Dictionary でも書ける
- **変数ストア** … 画面の中で共有される名前付きの値。文字列で持つ
- **named action** … キー / パッド / マウスへ割り当てる名前付き操作。組込名は
  ダイアログ内で処理され、それ以外はホストへ通知される
