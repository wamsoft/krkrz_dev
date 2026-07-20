# Dialog

Dialog クラスは、Elements ベースの汎用ダイアログを TJS から駆動するための

クラスです ( SDL3 ビルド限定 )。

JSON / JSONC ( コメントと末尾カンマを許容 ) 形式のレイアウト定義を渡して、
ボタン・チェックボックス・トグル・テキスト入力等を含むダイアログを表示
できます。動作モードは 3 種類あります。

レイアウト定義は JSON / JSONC 文字列のほか、TJS の Dictionary / Array を
そのまま渡せる Dict 系メソッド ( [showDict](#showdict) /
[showModalDict](#showmodaldict) ) も利用できます。

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

複数画面を遷移する「フロー」の駆動にも対応しています。ブロッキング
実行は [showFlow](#showflow) / [showFlowScreens](#showflowscreens)、
非モーダル ( 常駐 ) 実行は [startFlow](#startflow) /
[startFlowScreens](#startflowscreens) を使用します。画面遷移の
タイミングで [onScreen](#onscreen) / [onScreenLeave](#onscreenleave)
が発火し、widget 操作は引き続き [onAction](#onaction) に通知されます。

非モーダルダイアログは複数同時に表示できます ( z-order 付きで重ね
描画され、マウスはヒットテスト、キーボードは最前面の handler 優先で
フォーカスが移ります )。`grabFocus` 引数を偽にすると、フォーカスを
取らない常駐 HUD として表示できます。

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
- [active](#active)

### メソッド

- [showJson](#showjson)
- [showFile](#showfile)
- [showDict](#showdict)
- [showModalJson](#showmodaljson)
- [showModalFile](#showmodalfile)
- [showModalDict](#showmodaldict)
- [dictToJson](#dicttojson)
- [showFlow](#showflow)
- [showFlowScreens](#showflowscreens)
- [startFlow](#startflow)
- [startFlowScreens](#startflowscreens)
- [close](#close)
- [registerFont](#registerfont)
- [registerFontDir](#registerfontdir)

### イベント

- [onScreen](#onscreen)
- [onScreenLeave](#onscreenleave)
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

### active

プロパティ \ アクセス: `r`

**型**: `bool`

**解説**

この Dialog インスタンスがアクティブかどうか ( 読み取り専用 )

この Dialog で開いた非モーダルダイアログ / フローが現在アクティブな
ときに真になります。[close](#close) を呼んだ直後はまだ teardown が
終わっていないため真のままで、teardown 完了後に偽に切り替わります。

非モーダル UI を閉じてから次のモーダルダイアログを起動したい、
といったタイミング制御に使います。

---

### showJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `json` | `&nbsp;` | JSON / JSONC 形式のレイアウト定義文字列を指定します。 |
| `grabFocus` | `true` | キーボードフォーカスを取得するかどうか ( 既定 true )。<br>true のときはパネルがキーボードフォーカスを取得し、input_box 等への文字<br>入力やウィジェットのキー操作ができます ( ただしパネルが処理するキーは<br>ホスト側 [Window.onKeyDown](Window.md#onkeydown) には届きません )。<br>false のときはフォーカスを取らず、キー入力はホスト ( Window ) へ通ります。<br>ゲーム側のホットキーを活かしたい常駐 HUD 的なパネルや、独自のキー操作<br>( 画面切替等 ) と併用する場合に指定します。この場合パネル内の input_box 等<br>への文字入力はできません。マウス操作は grabFocus に関わらず有効です。 |

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
| `grabFocus` | `true` | キーボードフォーカスを取得するかどうか ( 既定 true )。詳細は [showJson](#showjson) を参照。 |

**戻り値**

表示開始に成功したら真を返します。

**解説**

ファイルから非モーダルダイアログを表示する

指定パスから JSON / JSONC レイアウト定義を読み込み、[showJson](#showjson)
と同じ動作で表示します。パスは Storages 経由のパス指定が使えます。

**関連:** [Dialog.showJson](Dialog.md#showjson)

---

### showDict

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | レイアウト定義の Dictionary を指定します。 |
| `grabFocus` | `true` | キーボードフォーカスを取得するかどうか ( 既定 true )。詳細は [showJson](#showjson) を参照。 |

**戻り値**

表示開始に成功したら真を返します。

**解説**

Dictionary で非モーダルダイアログを表示する

[showJson](#showjson) のレイアウトを JSON 文字列ではなく TJS の
Dictionary / Array で直接指定する版です。内部で JSON へ変換して
同じ経路で表示します ( 変換仕様は [dictToJson](#dicttojson) と同じ )。

**関連:** [Dialog.showJson](Dialog.md#showjson) / [Dialog.dictToJson](Dialog.md#dicttojson)

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

### showModalDict

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | レイアウト定義の Dictionary を指定します。 |
| `title` | `""` | 独立ウィンドウのタイトルを指定します ( 省略するとオーバーレイモードに切替わります )。 |
| `width` | `800` | 独立ウィンドウの幅をピクセル単位で指定します ( 既定値 800 )。 |
| `height` | `600` | 独立ウィンドウの高さをピクセル単位で指定します ( 既定値 600 )。 |

**戻り値**

action と values を保持する Dictionary が返ります。

**解説**

Dictionary でモーダルダイアログを表示する

[showModalJson](#showmodaljson) のレイアウトを TJS の Dictionary /
Array で直接指定する版です。引数 1 個で呼ぶとオーバーレイ、title
以降を渡すと独立ウィンドウで表示する点、および戻り値の形式は
[showModalJson](#showmodaljson) と同じです。

**関連:** [Dialog.showModalJson](Dialog.md#showmodaljson) / [Dialog.showDict](Dialog.md#showdict)

---

### dictToJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` | 変換する値 ( Dictionary / Array / 基本型 ) を指定します。 |

**戻り値**

JSON 文字列が返ります。

**解説**

Dictionary / Array を JSON 文字列へ変換する

[showDict](#showdict) / [showModalDict](#showmodaldict) が内部で行う
変換をそのまま呼び出すユーティリティです。Dictionary で組み立てた
レイアウトを JSON 資材として保存する、変換結果を確認する、といった
用途に使えます。インスタンスを作らず `Dialog.dictToJson(...)` として
呼べます。

対応する値の型は void / Integer / Real / String / Dictionary / Array
です。それ以外 ( Octet や一般のオブジェクト、循環参照、非有限の実数 )
は例外になります。

**関連:** [Dialog.showDict](Dialog.md#showdict)

---

### showFlow

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | app.jsonc マニフェストの Storages パスを指定します。 |

**戻り値**

action と values を保持する Dictionary が返ります。

**解説**

マニフェストから複数画面フローをブロッキング表示する

`app.jsonc` 形式のマニフェスト ( Storages 経由のパス指定 ) を読み込んで、
複数画面の遷移を含むフローを既存のゲーム画面にオーバーレイで実行します。
フロー終了まで TJS の実行を止め、最後に閉じた画面の Dictionary
`%[ action, values ]` を返します。

画面が切り替わるたびに [onScreen](#onscreen) / [onScreenLeave](#onscreenleave)、
各 widget の操作で [onAction](#onaction) が発火します。

**関連:** [Dialog.showFlowScreens](Dialog.md#showflowscreens) / [Dialog.startFlow](Dialog.md#startflow)

---

### showFlowScreens

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | 画面名 ( 文字列 ) をレイアウト定義 ( JSON 文字列、または Dictionary / Array ) にマップする Dictionary。両形式の混在も可能です。 |
| `entry` | `&nbsp;` | 起点画面名 ( screensDict のキー ) を指定します。 |

**戻り値**

action と values を保持する Dictionary が返ります。

**解説**

インライン定義から複数画面フローをブロッキング表示する

ファイル I/O を介さず、Dictionary で画面名 → レイアウト定義を渡して
フローを実行する [showFlow](#showflow) のインライン版です。
動作と戻り値は [showFlow](#showflow) と同じです。

**関連:** [Dialog.showFlow](Dialog.md#showflow) / [Dialog.startFlowScreens](Dialog.md#startflowscreens)

---

### startFlow

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | app.jsonc マニフェストの Storages パスを指定します。 |
| `grabFocus` | `true` | 真でキーボード / ゲームパッドフォーカスを取ります ( 既定値 真 )。偽を指定するとフォーカスを取らない常駐 HUD として表示されます。 |

**戻り値**

開始に成功したら真を返します。

**解説**

非モーダル ( 常駐 ) 複数画面フローを開始する

[showFlow](#showflow) と同じマニフェストを非モーダル ( 非ブロッキング ) で
開始し、即座に戻ります。ゲーム画面に出しっぱなしで進行させられるため、
メインメニューや HUD のような常駐 UI に適しています。

画面遷移は JSON 側 `transitions` 定義で行います。ボタン押下等を起点に
TJS 側で処理する場合は、`"close_on_click"` を指定しない button の
[onAction](#onaction) で振り分けてください。明示的に終了させるには
[close](#close) を呼び、teardown が完了したかどうかは
[active](#active) で判別できます。

**関連:** [Dialog.startFlowScreens](Dialog.md#startflowscreens) / [Dialog.showFlow](Dialog.md#showflow) / [Dialog.active](Dialog.md#active)

---

### startFlowScreens

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | 画面名 ( 文字列 ) を JSON 文字列にマップする Dictionary。 |
| `entry` | `&nbsp;` | 起点画面名 ( screensDict のキー ) を指定します。 |
| `grabFocus` | `true` | 真でキーボード / ゲームパッドフォーカスを取ります ( 既定値 真 )。偽を指定するとフォーカスを取らない常駐 HUD として表示されます。 |

**戻り値**

開始に成功したら真を返します。

**解説**

インライン定義から非モーダル ( 常駐 ) 複数画面フローを開始する

[showFlowScreens](#showflowscreens) と同じ Dictionary 形式の画面定義を
非モーダル ( 非ブロッキング ) で開始する [startFlow](#startflow) の
インライン版です。

**関連:** [Dialog.startFlow](Dialog.md#startflow) / [Dialog.showFlowScreens](Dialog.md#showflowscreens)

---

### close

メソッド

**解説**

ダイアログを閉じる

このインスタンスで開いた非モーダル / モーダルダイアログ ( フロー含む )
を閉じます。他のインスタンスが開いたダイアログは閉じません。

内部の teardown は次フレームで行われるため、close を呼んだ直後でも
しばらく [active](#active) は真のままです。次のモーダルを安全に
起動したい場合は [active](#active) が偽になるのを待ってください。

**関連:** [Dialog.active](Dialog.md#active)

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

### onScreen

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 入った画面の名前 ( マニフェストの画面キー ) 。 |

**解説**

フロー画面遷移通知 ( 画面に入った )

[showFlow](#showflow) / [startFlow](#startflow) 系で実行している
フローの画面に入ったタイミングで発火します。TJS 側で override して
ください。

**関連:** [Dialog.onScreenLeave](Dialog.md#onscreenleave)

---

### onScreenLeave

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 出た画面の名前 ( マニフェストの画面キー ) 。 |
| `action` | `&nbsp;` | 画面を離れる契機となった button の id ( Esc / × は空文字列 ) 。 |

**解説**

フロー画面遷移通知 ( 画面から出た )

[showFlow](#showflow) / [startFlow](#startflow) 系で実行している
フローの画面から離れるタイミングで発火します。TJS 側で override
してください。

**関連:** [Dialog.onScreen](Dialog.md#onscreen)

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
