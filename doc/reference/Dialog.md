# Dialog

Dialog クラスは、Elements ベースの汎用ダイアログを TJS から駆動するための

クラスです ( SDL3 ビルド限定 )。

JSON / JSONC ( コメントと末尾カンマを許容 ) 形式のレイアウト定義を渡して、
ボタン・チェックボックス・トグル・テキスト入力等を含むダイアログを表示
できます。動作モードは 3 種類あります。

- **非モーダル (オーバーレイ表示)**
[showJson](#showjson) / [showFile](#showfile) で表示します。表示中もメイン
ループは止まらず、ボタン押下や値変更があるたびに [onAction](#onaction)
が逐次発火します。明示的に [close](#close) を呼ぶか、ダイアログ側で
閉じるイベントが起きるまで残ります。
- **ブロッキングモーダル (独立ウィンドウ)**
[showModalJson](#showmodaljson) / [showModalFile](#showmodalfile) に
タイトル ( および幅・高さ ) を渡して呼ぶと、新しいネイティブウィンドウ
が開き、閉じるまで TJS の実行を止めて結果を Dictionary で返します。
- **ブロッキングモーダル (ゲーム画面へのオーバーレイ)**
[showModalJson](#showmodaljson) / [showModalFile](#showmodalfile) を
JSON 1 引数だけで呼ぶと、独立ウィンドウを開かずに既存のゲーム画面に
重ねて表示し、閉じるまでブロッキングします。

JSON 仕様の要素タイプ ( label / button / input_box / checkbox / toggle /
vtile / htile / vspacer / hspacer 等 ) や属性、`"input"` ノードによる
キーボード / ゲームパッド操作の設定詳細は [elements_modal の README](https://github.com/wamsoft/elements/blob/develop/docs/keyboard-navigation.md)
を参照してください。

`KRKRZ_USE_ELEMENTS=OFF` でビルドした exe や WINVER ビルドでは Dialog
クラスは利用できません。

## メンバー一覧

### コンストラクタ

- [Dialog](#dialog)

### プロパティ

- [defaultFontFamily](#defaultfontfamily)

### メソッド

- [showJson](#showjson)
- [showFile](#showfile)
- [showModalJson](#showmodaljson)
- [showModalFile](#showmodalfile)
- [close](#close)
- [registerFont](#registerfont)
- [registerFontDir](#registerfontdir)

### イベント

- [onAction](#onaction)

---

### Dialog

コンストラクタ

**解説**

Dialog オブジェクトの構築

Dialog クラスのオブジェクトを構築します。

---

### defaultFontFamily

プロパティ \ アクセス: `r/w`

**型**: `string`

**解説**

デフォルトフォントファミリ

Elements の theme に適用される label / button 等の既定フォントファミリ
名 ( カンマ区切り ) を取得 / 設定します。値の getter / setter とも
Elements ランタイムが初期化されたあと ( 最初のダイアログ表示後 ) に
意味を持ちます。

---

### showJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `json` | `&nbsp;` | JSON / JSONC 形式のレイアウト定義文字列を指定します。 |

**戻り値**

表示開始に成功したら真を返します。

**解説**

JSON 文字列で非モーダルダイアログを表示する

指定された JSON / JSONC 形式のレイアウト定義からダイアログを構築し、
既存のゲーム画面にオーバーレイ表示します。表示中もメインループは
止まらず、ユーザ操作のたびに [onAction](#onaction) が発火します。
表示を終わらせるには [close](#close) を呼んでください。

**関連:** [Dialog.showFile](Dialog.md#showfile) / [Dialog.onAction](Dialog.md#onaction) / [Dialog.close](Dialog.md#close)

---

### showFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | JSON / JSONC ファイルのパスを指定します。 |

**戻り値**

表示開始に成功したら真を返します。

**解説**

ファイルから非モーダルダイアログを表示する

指定パスから JSON / JSONC レイアウト定義を読み込み、[showJson](#showjson)
と同じ動作で表示します。パスは Storages 経由のパス指定が使えます。

**関連:** [Dialog.showJson](Dialog.md#showjson)

---

### showModalJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `json` | `&nbsp;` | JSON / JSONC 形式のレイアウト定義文字列を指定します。 |
| `title` | `""` | 独立ウィンドウのタイトルを指定します ( 省略するとオーバーレイモードに切替わります )。 |
| `width` | `800` | 独立ウィンドウの幅をピクセル単位で指定します ( 既定値 800 )。 |
| `height` | `600` | 独立ウィンドウの高さをピクセル単位で指定します ( 既定値 600 )。 |

**戻り値**

action と values を保持する Dictionary が返ります。

**解説**

JSON 文字列でモーダルダイアログを表示する

指定された JSON / JSONC 定義からダイアログを構築し、閉じるまで
TJS の実行を止めてブロッキング表示します。

- 引数を JSON 1 個だけで呼ぶと、既存のゲーム画面にオーバーレイ表示
( in-game modal ) します。
- title 以降を渡すと独立した新しいネイティブウィンドウを開いて表示
します。

戻り値は次の構造の Dictionary です。

%[
action: <閉じた button の id ( Esc / × は "" )>,
values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]

モーダル表示中も [onAction](#onaction) は発火しますが、ダイアログを
閉じるのは `"close_on_click": true` 指定の button が押されたとき
( および Esc / × による中断 ) だけです。

**関連:** [Dialog.showModalFile](Dialog.md#showmodalfile) / [Dialog.onAction](Dialog.md#onaction)

---

### showModalFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | JSON / JSONC ファイルのパスを指定します。 |
| `title` | `""` | 独立ウィンドウのタイトルを指定します ( 省略するとオーバーレイモードに切替わります )。 |
| `width` | `800` | 独立ウィンドウの幅をピクセル単位で指定します ( 既定値 800 )。 |
| `height` | `600` | 独立ウィンドウの高さをピクセル単位で指定します ( 既定値 600 )。 |

**戻り値**

action と values を保持する Dictionary が返ります。

**解説**

ファイルからモーダルダイアログを表示する

指定パスから JSON / JSONC レイアウト定義を読み込んで [showModalJson](#showmodaljson)
と同じ動作で表示します。パスは Storages 経由のパス指定が使えます。

**関連:** [Dialog.showModalJson](Dialog.md#showmodaljson)

---

### close

メソッド

**解説**

ダイアログを閉じる

このインスタンスで開いた非モーダル / モーダルダイアログを閉じます。
他のインスタンスが開いたダイアログは閉じません。

---

### registerFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `family` | `&nbsp;` | 登録時に使うファミリ名を指定します。 |
| `path` | `&nbsp;` | フォントファイル ( .ttf / .otf ) の Storages パスを指定します。 |
| `weight` | `40` | weight 値を指定します ( 既定値 40 = normal )。 |
| `slant` | `0` | slant 値を指定します ( 既定値 0 = normal )。 |
| `stretch` | `50` | stretch 値を指定します ( 既定値 50 = normal )。 |

**戻り値**

実際に登録された family 名 ( ThorVG embedded 優先 )。

**解説**

Elements 用フォントの登録

Elements ダイアログで使用するフォントを krkrz Storages 経由で登録
します。ThorVG がファイルから読み取った embedded family 名 ( 取れな
かった場合は空文字 ) を戻り値として返します。スクリプトはこの戻り値
を見て theme への組込みやログ表示に利用できます。

weight / slant / stretch は font_constants の整数値です ( 詳細は
`StoragesResourceLoader.h` を参照 )。

**関連:** [Dialog.registerFontDir](Dialog.md#registerfontdir)

---

### registerFontDir

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 登録対象ディレクトリの Storages パスを指定します。 |

**戻り値**

真が返ります ( ディレクトリが空でも例外にはなりません )。

**解説**

Elements 用フォントの一括登録

指定ディレクトリ配下の .ttf / .otf を全て列挙して登録します ( ファイル
名から family / weight / slant / stretch を推定 )。dir は Storages 経由の
パス指定が使え、XP3 内のディレクトリでも構いません。

**関連:** [Dialog.registerFont](Dialog.md#registerfont)

---

### onAction

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 発生元 widget の id 文字列。 |
| `payload` | `&nbsp;` | widget が伴って渡す値 ( 上記参照 )。 |

**解説**

ダイアログ上の操作通知

ダイアログ上で発生したアクション ( button click や state widget の値
変化 ) を受け取るイベントです。TJS 側で override してください。

非モーダル ( [showJson](#showjson) / [showFile](#showfile) ) では
表示中ずっと発火します。モーダル ( [showModalJson](#showmodaljson) /
[showModalFile](#showmodalfile) ) でも、`"close_on_click": true` で
閉じる前に発生したアクションは順次このイベントに通知されます。

payload の内容は widget の種類によって変わります。

- button click ... void
- checkbox / toggle ... bool ( 変更後の値 )
- input_box ... string ( 編集後のテキスト )
- slider 等 ... 各 widget が渡す値

---
