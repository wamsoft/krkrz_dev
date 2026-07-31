# Elements ベースの汎用ダイアログ (Dialog クラス)

吉里吉里Z は内部に [Elements](https://github.com/wamsoft/elements)
( ThorVG ベースの C++ GUI ライブラリ ) を組み込んでいて、JSON / JSONC で
記述したレイアウトからボタン・チェックボックス・テキスト入力等を含む
ダイアログを動かせます。TJS からは [Dialog](../../reference/Dialog.md)
クラスで利用します。

設計の経緯や DrawDevice との接続、`tTVPElementsDialogManager` 等の
内部構造は src/core 側のドキュメントを参照してください。

- [doc/ElementsDialog.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/ElementsDialog.md)
- elements_modal ライブラリ: [external/elements_modal/README.md](https://github.com/wamsoft/krkrz_develop/blob/master/external/elements_modal/README.md)
- JSON で表現できる widget / 属性 / キー操作: [elements_modal の README](https://github.com/wamsoft/elements/blob/develop/docs/keyboard-navigation.md)

`KRKRZ_USE_ELEMENTS=ON` ( デフォルト ) でビルドされたエンジンで利用できます。
SDL3 ビルドと **WINVER ( Windows ネイティブ / D3D11 ) ビルドの両方**に対応します
( WINVER では独立 OS ウィンドウ版モーダルは overlay モーダルで代替 )。
`KRKRZ_USE_ELEMENTS=OFF` ビルドでは [Dialog](../../reference/Dialog.md)
クラスは登録されません。

---

## 表示モード

1 画面の単発ダイアログには 3 モード、複数画面の遷移を含む「フロー」
には 2 モードがあります。

### 単発ダイアログ

| 表示モード | TJS API | 挙動 |
|---|---|---|
| 非モーダル (オーバーレイ) | [Dialog.showJson](../../reference/Dialog.md#showjson) / [showFile](../../reference/Dialog.md#showfile) | 既存ゲーム画面の上にダイアログを描き、メインループを止めない。値変化・button click は [onAction](../../reference/Dialog.md#onaction) で逐次通知。[close](../../reference/Dialog.md#close) で終了。 |
| ブロッキングモーダル (独立ウィンドウ) | [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) ( title / w / h を渡す ) | 新しいネイティブウィンドウを開き、閉じるまでブロッキング。閉じると `%[ action, values ]` 形式の Dictionary を返す。 |
| ブロッキングモーダル (オーバーレイ) | [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) ( JSON 1 引数のみ ) | 独立ウィンドウを作らずに既存ゲーム画面に重ねて表示し、閉じるまでブロッキング。戻り値は独立ウィンドウ版と同じ。 |

### 複数画面フロー

| 表示モード | TJS API | 挙動 |
|---|---|---|
| ブロッキング ( オーバーレイ ) | [Dialog.showFlow](../../reference/Dialog.md#showflow) / [showFlowScreens](../../reference/Dialog.md#showflowscreens) | マニフェスト ( または Dictionary ) で定義された複数画面の遷移をオーバーレイで実行。フロー終了まで TJS をブロックし、最後に閉じた画面の `%[ action, values ]` を返す。 |
| 非モーダル ( 常駐 ) | [Dialog.startFlow](../../reference/Dialog.md#startflow) / [startFlowScreens](../../reference/Dialog.md#startflowscreens) | 同じフロー定義を非ブロッキングで開始 ( ゲーム画面に常駐 )。`close` で閉じ、teardown 完了は [active](../../reference/Dialog.md#active) で判別。 |

画面が切り替わるタイミングで [onScreen](../../reference/Dialog.md#onscreen) /
[onScreenLeave](../../reference/Dialog.md#onscreenleave)、widget の
操作で [onAction](../../reference/Dialog.md#onaction) が発火します。

`showModalJson` / `showModalFile` の戻り値:

```tjs
%[
    action: <閉じた button の id (Esc / × は "")>,
    values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]
```

モーダル中も [onAction](../../reference/Dialog.md#onaction) は発火しますが、
ダイアログを閉じるのは JSON 側で `"close_on_click": true` を指定した button
( および Esc / × による中断 ) だけです。

---

## 非モーダルの複数同時表示とフォーカス

非モーダルダイアログ ( [showJson](../../reference/Dialog.md#showjson) /
[startFlow](../../reference/Dialog.md#startflow) 系 ) は z-order 付きの
インスタンスリストとして管理され、複数同時に表示できます。マウスは
最前面からヒットテストし、キーボード / ゲームパッドはフォーカスを
保持しているインスタンス ( z-order 末尾優先 ) に届きます。モーダル
ダイアログを重ねた場合、下のインスタンスは描画維持・入力だけブロック
されます。

非モーダル開始系 ( [startFlow](../../reference/Dialog.md#startflow) /
[startFlowScreens](../../reference/Dialog.md#startflowscreens) ) には
`grabFocus` 引数があり、偽を指定すると「フォーカスを取らない常駐 HUD」
として動きます。常駐 UI がゲームのホットキーまで食ってしまうのを
防ぎたい場合に利用します。

非モーダルでは、Elements 側で実際に処理されたキーだけを消費して未処理
キーはゲームへ通過させる ( handled pass-through ) ため、メニューを開いた
ままゲーム本体のホットキーで別ダイアログを開く、といった共存も可能です。

---

## ミニマルな利用例

```tjs
class TestDialog extends Dialog {
    function onAction(id, payload) {
        switch (id) {
        case "ok":     System.inform("OK!");  close(); break;
        case "cancel": close(); break;
        }
    }
}

var json = @"
{
    // hspacer で 560 幅を確保 (JSONC コメント可)
    'size': [ 560, 200 ],
    'content': {
        'type': 'vtile',
        'children': [
            { 'type': 'hspacer', 'size': 560 },
            { 'type': 'label', 'text': 'Hello, Elements!' },
            { 'type': 'htile', 'children': [
                { 'type': 'button', 'id': 'ok',     'text': 'OK',     'close_on_click': true },
                { 'type': 'button', 'id': 'cancel', 'text': 'Cancel', 'close_on_click': true }
            ]}
        ]
    }
}";

var dlg = new TestDialog();
dlg.showJson(json);             // 非モーダル
// var r = dlg.showModalJson(json, "Title", 560, 200);   // 独立ウィンドウ
// var r = dlg.showModalJson(json);                       // ゲーム画面オーバーレイ
```

ボタン / 入力欄を JSON でどう書くかの詳細は [elements_modal の README](https://github.com/wamsoft/krkrz_develop/blob/master/external/elements_modal/README.md)
を参照してください。

---

## フォントの登録

Elements 自身は krkrz Storages ( XP3 含む ) を経由してフォントを読みます。
スクリプトから明示的に登録するには [Dialog.registerFont](../../reference/Dialog.md#registerfont) /
[Dialog.registerFontDir](../../reference/Dialog.md#registerfontdir) を、
既定フォントファミリの確認・上書きには [Dialog.defaultFontFamily](../../reference/Dialog.md#defaultfontfamily)
プロパティを使います。

エンジン側でも、起動時に `Application->ResourcePath()` 下の `.ttf` / `.otf`
を自動スキャンして登録しています ( ファイル名から family / weight /
slant / stretch を推定 )。

---

## ビルド構成

`CMakeLists.txt` の `KRKRZ_USE_ELEMENTS` で Elements / UserConfig を一括で
無効化できます ( SDL3 / WINVER 共通、デフォルト ON )。OFF にすると以下が
コンパイル / リンクから除外されます。

- `external/elements` ( cycfi::elements + thorvg ) と `external/elements_modal`
- `common/visual/elements/*` / `sdl3/visual/SDL{Dialog,Elements*}` /
  `common/visual/opengl/OGLDialogRenderer.{cpp,h}` /
  `win32/visual/D3D11DialogRenderer.{cpp,h}` ( WINVER )
- TJS [Dialog](../../reference/Dialog.md) クラスの登録

x64-windows 計測で krkrz64.exe が 15.6 MB → 13.8 MB ( OFF ) と約 1.8 MB
削減されます。

---

## 関連 API

- [Dialog](../../reference/Dialog.md) — TJS バインディングクラス
- [Dialog.showJson](../../reference/Dialog.md#showjson) / [showFile](../../reference/Dialog.md#showfile) — 非モーダル
- [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) — モーダル
- [Dialog.showFlow](../../reference/Dialog.md#showflow) / [showFlowScreens](../../reference/Dialog.md#showflowscreens) — ブロッキングフロー
- [Dialog.startFlow](../../reference/Dialog.md#startflow) / [startFlowScreens](../../reference/Dialog.md#startflowscreens) — 非モーダル ( 常駐 ) フロー
- [Dialog.onAction](../../reference/Dialog.md#onaction) / [onScreen](../../reference/Dialog.md#onscreen) / [onScreenLeave](../../reference/Dialog.md#onscreenleave) — イベント
- [Dialog.active](../../reference/Dialog.md#active) — 非モーダルの teardown 完了判定
- [Dialog.registerFont](../../reference/Dialog.md#registerfont) / [registerFontDir](../../reference/Dialog.md#registerfontdir) / [defaultFontFamily](../../reference/Dialog.md#defaultfontfamily)
