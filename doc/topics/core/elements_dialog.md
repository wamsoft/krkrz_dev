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

SDL3 ビルド + `KRKRZ_USE_ELEMENTS=ON` ( デフォルト ) でビルドされた
エンジンで利用できます。WINVER ビルド・`KRKRZ_USE_ELEMENTS=OFF`
ビルドでは [Dialog](../../reference/Dialog.md) クラスは登録されません。

---

## 3 つの表示モード

| 表示モード | TJS API | 挙動 |
|---|---|---|
| 非モーダル (オーバーレイ) | [Dialog.showJson](../../reference/Dialog.md#showjson) / [showFile](../../reference/Dialog.md#showfile) | 既存ゲーム画面の上にダイアログを描き、メインループを止めない。値変化・button click は [onAction](../../reference/Dialog.md#onaction) で逐次通知。[close](../../reference/Dialog.md#close) で終了。 |
| ブロッキングモーダル (独立ウィンドウ) | [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) ( title / w / h を渡す ) | 新しいネイティブウィンドウを開き、閉じるまでブロッキング。閉じると `%[ action, values ]` 形式の Dictionary を返す。 |
| ブロッキングモーダル (オーバーレイ) | [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) ( JSON 1 引数のみ ) | 独立ウィンドウを作らずに既存ゲーム画面に重ねて表示し、閉じるまでブロッキング。戻り値は独立ウィンドウ版と同じ。 |

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
無効化できます ( SDL3 ビルド専用、デフォルト ON )。OFF にすると以下が
コンパイル / リンクから除外されます。

- `external/elements` ( cycfi::elements + thorvg ) と `external/elements_modal`
- `common/visual/elements/*` / `sdl3/visual/SDL{Dialog,Elements*}` /
  `common/visual/opengl/OGLDialogRenderer.{cpp,h}`
- TJS [Dialog](../../reference/Dialog.md) クラスの登録

x64-windows 計測で krkrz64.exe が 15.6 MB → 13.8 MB ( OFF ) と約 1.8 MB
削減されます。

---

## 関連 API

- [Dialog](../../reference/Dialog.md) — TJS バインディングクラス
- [Dialog.showJson](../../reference/Dialog.md#showjson) / [showFile](../../reference/Dialog.md#showfile) — 非モーダル
- [Dialog.showModalJson](../../reference/Dialog.md#showmodaljson) / [showModalFile](../../reference/Dialog.md#showmodalfile) — モーダル
- [Dialog.onAction](../../reference/Dialog.md#onaction) — 操作通知
- [Dialog.registerFont](../../reference/Dialog.md#registerfont) / [registerFontDir](../../reference/Dialog.md#registerfontdir) / [defaultFontFamily](../../reference/Dialog.md#defaultfontfamily)
