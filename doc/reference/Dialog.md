# Dialog

Dialog クラスは、Elements ベースの汎用ダイアログを TJS から駆動するための

クラスです ( SDL3 / WINVER 両ビルド対応 )。

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
取らない常駐 HUD として表示できます。`showJson(json, true, false)`
( フォーカスあり非モーダル ) にするとキー / パッドでパネルを操作しつつ
未処理キーをホストへ素通しでき、ホストが必ず受けたいキーは
[registerHotKey](#registerhotkey) で確保できます。

JSON 仕様の要素タイプ ( label / button / input_box / checkbox / toggle /
text_box / text_area / vtile / htile / vspacer / hspacer 等 ) や属性、
レイアウト密度指定 ( `"gap"` / top-level `"style"` ブロック ) の詳細は
[elements_modal の README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md)、
`"input"` ノードによるキーボード / ゲームパッド操作の設定詳細は
[キーボードナビゲーション仕様](https://github.com/wamsoft/elements/blob/develop/docs/keyboard-navigation.md)
を参照してください。

矩形へ本文を流し込むなら `text_area` を使います。折り返し・行頭行末禁則・
文字送りが [Layer.drawShapedTextArea](Layer.md#drawshapedtextarea) と同じ
ロジックなので、**同じ本文・同じ幅なら改行位置が一致します**。
`"count_var"` に変数名を与えると [setVar](#setvar) で文字送りが進み、
折り返しは全文で確定済みなので送ってもリフローしません
( 字幕やセリフ窓向け。従来からある `text_box` は互換のためそのまま )。

`KRKRZ_USE_ELEMENTS=OFF` でビルドした exe では Dialog クラスは利用できません。
WINVER (Windows ネイティブ / D3D11) ビルドでも Dialog は利用できます
(非モーダル / overlay モーダル / 独立ウィンドウモーダル / フロー /
テキスト入力すべてに対応)。

## メンバー一覧

### コンストラクタ

- [Dialog](#dialog)

### プロパティ

- [defaultFontFamily](#defaultfontfamily)
- [active](#active)
- [modalActive](#modalactive)
- [language](#language)
- [fontLanguages](#fontlanguages)
- [virtualKeyboard](#virtualkeyboard)
- [hasPhysicalKeyboard](#hasphysicalkeyboard)
- [focusRing](#focusring)
- [baseSize](#basesize)
- [renderScale](#renderscale)
- [renderCache](#rendercache)
- [partialRedraw](#partialredraw)
- [renderCount](#rendercount)
- [renderStats](#renderstats)

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
- [registerHotKey](#registerhotkey)
- [unregisterHotKey](#unregisterhotkey)
- [clearHotKeys](#clearhotkeys)
- [registerImage](#registerimage)
- [unregisterImage](#unregisterimage)
- [clearImages](#clearimages)
- [setVar](#setvar)
- [setPadIconBase](#setpadiconbase)
- [setPadTheme](#setpadtheme)
- [renderStatsReset](#renderstatsreset)

### イベント

- [onScreen](#onscreen)
- [onScreenLeave](#onscreenleave)
- [onAction](#onaction)
- [onDrag](#ondrag)
- [onClose](#onclose)

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

### modalActive

プロパティ \ アクセス: `r`

**型**: `bool`

**解説**

モーダルなダイアログが表示中かどうか ( 読み取り専用 )

[showModalJson](#showmodaljson) 系やモーダルフローで開いたインスタンスが
1 つでもアクティブなら真になります ( どのインスタンスから読んでもプロセス
全体の状態を返します )。フォーカスを取らない常駐オーバレイ ( 字幕・HUD 等 )
は含みません。

最上位ホットキー ( [System.registerHotKey](System.md#registerhotkey) ) の
コールバックで「モーダル表示中は何もせず素通しする」判定に使います。

**関連:** [Dialog.active](Dialog.md#active)

---

### language

プロパティ \ アクセス: `r/w`

**型**: `String`

**解説**

i18n の表示言語

画面 JSON の top-level `strings` ( textID → 言語別文字列 ) を引くときのキーです
( クラス全体に効く static 相当 )。`"ja"` / `"en"` / `"tc"` / `"sc"` など、
`strings` 側で使っているキーをそのまま指定します。

```tjs
global.Dialog.language = "en";     // 表示中の画面もその場で切り替わる
```

代入すると**表示中の全ダイアログへ即時適用**されます ( `text_id` / `text_list_id` /
`options_id` を持つ widget が再解決され、画面を開き直さずに表示が変わります )。
以後に開く画面の既定にもなります。picker 系は選択 index を維持したまま
表示文字列だけ差し替わります。

読み出すと設定済みの言語を返します。未設定なら空文字 ( = 各画面 JSON の
`lang` 指定に従う ) です。`strings` を持たない画面では何も起きません。

---

### fontLanguages

プロパティ \ アクセス: `r/w`

**型**: `Object`

**解説**

言語連動フォント置換表

文字体系ごとの別フォント ( Noto Sans JP / TC / SC など ) を持つ多言語 UI で、
表示言語に応じてフォント解決時にファミリを差し替えるための表です
( クラス全体に効く static 相当 )。日中で共有しているコードポイントの漢字を、
表示言語に合った地域字形で描画できます。

言語コードをキーに、`map` ( ファミリ名または [registerFont](#registerfont) の
別名 → 置換先ファミリ ) と `fallback` ( 任意。その言語のときの theme 既定
ファミリチェーンの並び ) を持つ辞書 ( または同形の JSON 文字列 ) を代入します。

```tjs
global.Dialog.fontLanguages = %[
"tc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans TC" ] ],
"sc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans SC" ] ] ];
global.Dialog.language = "sc";   // 以後 "Noto Sans JP" 指定は SC フォントで描画
```

`map` は widget の `"font"` 指定と theme 既定チェーンの各ファミリトークンに
適用され、`"#tag=val"` の可変軸サフィックスは温存されます ( JP/TC/SC が同じ
軸を持つ可変フォントならウェイト指定がそのまま引き継がれます )。適用される
言語は widget の明示 `"locale"` があればそれ、無ければ [language](#language)
です。表にエントリの無い言語では置換されません。

画面 JSON / app.jsonc の top-level `"font_languages"` と同じ表で、言語単位に
マージ登録されます ( 後から設定した方が言語ごとに上書き )。読み出すと最後に
代入した表を JSON 文字列で返します ( 未設定なら空文字。画面 JSON 側の宣言は
含みません )。

`text_area` はビルド時にフォントが確定するため、表示中の言語切替には追従
しません ( 画面を開き直すと反映されます )。

---

### virtualKeyboard

プロパティ \ アクセス: `r/w`

**型**: `String`

**解説**

内蔵仮想キーボードの動作モード

テキスト欄 ( `input_box` 等 ) に focus が入ったとき、OS のソフトウェア
キーボードの代わりに Elements 内蔵の英数キーボードを出すかどうかを
指定します。設定できる値は次の通りです。

| 値 | 意味 |
|---|---|
| `"auto"` | 既定。物理キーボードが接続されていないときだけ出す |
| `"always"` | 物理キーボードがあっても常に出す ( テスト用。デスクトップでも出る ) |
| `"never"` | 出さない ( OS 側に任せる )。表示中なら閉じる |

初期値は環境変数 `KRKRZ_FORCE_VIRTUAL_KEYBOARD=1` があれば `"always"`、
無ければ `"auto"` です。

出るのは **Elements のテキスト欄に focus が入ったとき**で、ゲーム側が
自前で描いている入力欄では出ません。押鍵は貯めずにその場で入力先へ
流し込まれるため、入力欄がリアルタイムに更新されます。
現バージョンでは大文字英数字のみ対応です。

動作を確認できるコアデモは `softkey_ime` です。

**関連:** [Dialog.hasPhysicalKeyboard](Dialog.md#hasphysicalkeyboard)

---

### hasPhysicalKeyboard

プロパティ \ アクセス: `r`

**型**: `Boolean`

**解説**

物理キーボードの有無

物理 ( ハードウェア ) キーボードが接続されているかを返します。読み出し専用。
デスクトップでは常に真、コンソール機等では USB キーボードの接続状態に
なります。ゲーム側が独自のソフトウェアキーボードを出すかどうかの判断に
使用します。

**関連:** [Dialog.virtualKeyboard](Dialog.md#virtualkeyboard)

---

### focusRing

プロパティ \ アクセス: `r/w`

**型**: `Boolean`

**解説**

フォーカス枠の表示

フォーカス中の要素に Elements が描く汎用の枠 ( 青い角丸 ) の表示です
( クラス全体に効く static 相当 )。既定は true。

```tjs
global.Dialog.focusRing = false;    // アプリ全体で消す
```

button / slider / dial / thumbwheel の枠がまとめて消えます。状態別の絵
( 通常 / オーバー / 押し下げ / 無効 ) を素材として持つ画像 UI では、汎用の枠が
絵に重なって邪魔になるので切ります。**フォーカス自体は生きている**ので、
キー/パッドのナビゲーションと hilite フレームへの切替は従来どおり動きます。

画面単位ではなくアプリ全体の設定です ( グローバルテーマのフラグ )。

クラス内から触るときは `global.Dialog.focusRing` と書きます。Dialog を継承した
クラスのメソッド内で素の `Dialog` と書くと親クラス参照になり、static プロパティへの
代入が「メンバが見つかりません」になります。

---

### baseSize

プロパティ \ アクセス: `r/w`

**型**: `Array`

**解説**

UI の author 基準面サイズ

オーバレイ表示の拡縮率 ( fit ) の分母になる基準面のサイズを `[w, h]` の
配列で指定します。void ( または要素の無い配列 ) を設定すると既定 =
ゲームの基準面 ( primaryLayer のサイズ ) に戻ります。設定していないときの
getter は void です。

ゲーム画面と別解像度で UI を author しているタイトル ( ゲーム画面
640x400 / UI 1920x1080 等 ) で設定すると、部分パネルの拡縮が author 基準
どおりになり、ゲーム側の primaryLayer サイズ変更 ( 低解像度機種の
エミュレーション等 ) にも巻き込まれません。表示中の画面にも次のフレーム
から反映されます。

**関連:** [Dialog.renderScale](Dialog.md#renderscale)

---

### renderScale

プロパティ \ アクセス: `r/w`

**解説**

オーバーレイの描画密度モード

overlay の描画密度モードです ( クラス全体に効く static 相当 )。

- 0 ( 既定 ) = auto: 最終 present サイズで直接ラスタライズ。
- >0 = authored 論理サイズ × この倍率で描き、present 時に拡縮 ( 1.0 = 原寸レンダ→拡縮表示、
2.0 = supersampling 相当 )。

表示中の画面にも次フレームから反映されます ( 描画品質/負荷の比較用 )。

---

### renderCache

プロパティ \ アクセス: `r/w`

**解説**

オーバーレイの再ラスタライズ抑止

true ( 既定 ) の間、変化の無いフレームはダイアログの再ラスタライズ ( CPU ) と
テクスチャ再アップロードを省略し、前回の描画結果をそのまま提示します
( クラス全体に効く static 相当 )。アイドル中の CPU 負荷が大きく下がります。

入力イベント・フォーカス/ホバー変化・パーツ演出再生中・setVar の実変化・
テキスト欄キャレットの点滅・画面遷移エフェクト中などは自動的に再描画されます。
false にすると従来どおり毎フレーム再描画します ( 負荷比較・問題切り分け用 )。

---

### partialRedraw

プロパティ \ アクセス: `r/w`

**解説**

オーバーレイの部分再描画

true ( 既定 ) の間、変化した範囲が矩形で特定できる場合は**その矩形だけ**を
再ラスタライズしてテクスチャへ部分転送します ( クラス全体に効く static 相当 )。
矩形が特定できるのはテキスト欄のキャレット点滅などに限られ、入力・フォーカス
変化・パーツ演出・setVar などは従来どおり全面再描画になります。

[Dialog.renderCache](Dialog.md#rendercache) が有効なときのみ機能します
( 前回の描画結果が残っていることが前提 )。false にすると変化フレームは
常に全面再描画します ( 負荷比較・問題切り分け用 )。実際に部分再描画できた
回数は [Dialog.renderStats](Dialog.md#renderstats) の "partials" で確認できます。

---

### renderCount

プロパティ \ アクセス: `r/w`

**解説**

ラスタライズ累計回数 ( 読み取り専用 )

実際にラスタライズ ( 再描画 ) を行った累計回数です ( クラス全体で共通 )。
アイドル時に増えていなければ renderCache が効いています ( 検証・負荷比較用 )。

---

### renderStats

プロパティ \ アクセス: `r/w`

**解説**

描画パイプラインの区間計測 ( 読み取り専用 )

オーバーレイ描画の負荷内訳を Dictionary で返します ( クラス全体で共通の累積値 )。
時間はすべてマイクロ秒です:
%[ "frames" => 提示フレーム数, "updates" => 状態更新回数,
"rasters" => ラスタライズ回数, "partials" => うち部分再描画だった回数,
"cachedPresents" => ラスタ省略提示回数,
"presents" => 提示回数, "totalUs" => 描画処理全体, "updateUs" => 状態更新,
"rasterUs" => CPU ラスタライズ, "acquireUs" => バッファ確保,
"uploadUs" => テクスチャ転送, "presentUs" => 提示 ]

累積値なので 2 回読んで差分を取り、経過実時間との比で
「Elements が消費した時間・割合」を計算します
( [Dialog.renderStatsReset](Dialog.md#renderstatsreset) で 0 クリア )。
計測用のベンチ画面がコアデモ `elements_bench` にあります
( シナリオ切替 + renderCache A/B + 500ms ごとの内訳表示 )。

---

### showJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `json` | `&nbsp;` | JSON / JSONC 形式のレイアウト定義文字列を指定します。 |
| `grabFocus` | `true` | キーボードフォーカスを取得するかどうか ( 既定 true )。<br>true のときはパネルがキーボードフォーカスを取得し、input_box 等への文字<br>入力やウィジェットのキー / パッド操作ができます。<br>false のときはフォーカスを取らず、キー入力はホスト ( Window ) へ通ります。<br>表示専用の常駐 HUD 的なパネルに指定します。この場合パネル内の input_box 等<br>への文字入力はできません。マウス操作は grabFocus に関わらず有効です。 |
| `modal` | `grabFocus` | モーダル ( 入力独占 ) にするかどうか。省略時は後方互換で<br>grabFocus と同じ値になります。<br>`showJson(json, true, false)` = 「非モーダル + フォーカスあり」の中間状態で、<br>キー / パッドはパネルへ届いてウィジェットを操作でき ( パッドの十字 = フォーカス<br>ナビ / A = 決定 )、パネルが処理しなかったキーだけがホスト<br>( [Window.onKeyDown](Window.md#onkeydown) ) へ素通しされます。操作パネル用途は<br>この指定を推奨します。ホストが必ず受けたいキーは<br>[registerHotKey](#registerhotkey) で確保してください。<br>用途 3 態: モーダルダイアログ `showJson(json)` / 操作パネル<br>`showJson(json, true, false)` / 表示専用 HUD `showJson(json, false)`。 |

**戻り値**

表示開始に成功したら真を返します。

**解説**

JSON 文字列で非モーダルダイアログを表示する

指定された JSON / JSONC 形式のレイアウト定義からダイアログを構築し、
既存のゲーム画面にオーバーレイ表示します。表示中もメインループは
止まらず、ユーザ操作のたびに [onAction](#onaction) が発火します。
表示を終わらせるには [close](#close) を呼んでください。

**関連:** [Dialog.showFile](Dialog.md#showfile) / [Dialog.registerHotKey](Dialog.md#registerhotkey) / [Dialog.onAction](Dialog.md#onaction) / [Dialog.close](Dialog.md#close)

---

### showFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | JSON / JSONC ファイルのパスを指定します。 |
| `grabFocus` | `true` | キーボードフォーカスを取得するかどうか ( 既定 true )。詳細は [showJson](#showjson) を参照。 |
| `modal` | `grabFocus` | モーダルにするかどうか ( 省略時は grabFocus に追従 )。詳細は [showJson](#showjson) を参照。 |

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
| `modal` | `grabFocus` | モーダルにするかどうか ( 省略時は grabFocus に追従 )。詳細は [showJson](#showjson) を参照。 |

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

画面 JSON の `transitions` エントリを object 形式にすると、画面切替時の
遷移エフェクトを宣言できます ( `effect: "fade"` = クロスフェード /
`effect: "universal"` = rule 画像によるユニバーサルトランジション。
`duration` = 所要 ms ( 省略時 200 )、universal では追加で `rule` =
rule 画像パス ( 宣言した画面からの相対 / Storages パス / autopath 検索 )、
`vague` = 境界ぼかし幅 0〜255 ( 省略時 64 ) を指定します )。

```json
"transitions": {
"next": { "target": "s2", "effect": "fade", "duration": 300 },
"back": { "target": "<back>", "effect": "universal",
"rule": "rule.png", "vague": 64, "duration": 500 }
}
```

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

画面内の要素に `"animate"` の `"on": "exit"` 指定 ( 退場演出 ) がある
場合、close でも退場演出を再生し、完了してから閉じます ( その間も
[active](#active) は真のままです )。フロー実行中の close は画面遷移
( transitions ) を解決せず、フローごと終了します。

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

### registerHotKey

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 仮想キーコード ( VK_ESCAPE 等 )。キーのほか、パッドボタン<br>( VK_PAD1 〜 VK_PAD12 等 ) とマウスボタン ( VK_LBUTTON / VK_RBUTTON /<br>VK_MBUTTON / VK_XBUTTON1 / VK_XBUTTON2 ) も同じ空間で指定できます。<br>印字キーの登録は非推奨です ( onKeyPress の文字イベントまでは抑止<br>されません )。 |
| `shift` | `0` | 修飾キーの組合せ ( ssShift \| ssAlt \| ssCtrl、既定 0 )。<br>キー down は完全一致で判定し、up はキーのみの一致で対にバイパスします。 |
| `duringTextInput` | `false` | 真にすると、ダイアログ内のテキスト入力ウィジェット<br>( input_box 等 ) にキャレットがある間も有効になります。既定の偽では<br>テキスト入力中は抑止され、ESC / BackSpace 等を入力欄から奪いません。 |

**戻り値**

戻り値はありません。同じ ( key, shift ) の再登録は
duringTextInput の上書きになります。

**解説**

ホストホットキーの登録

「ダイアログにフォーカスを渡しつつ、特定のキーだけは必ずホスト側で
受けたい」ためのバイパス機構です。登録したキーはダイアログへ渡らず、
そのまま通常のゲーム入力経路
( [Window.onKeyDown](Window.md#onkeydown) /
[Window.onMouseDown](Window.md#onmousedown) 等 ) へ届きます
( 専用イベントはありません )。

入力の配送優先順位は次の一列です。

1. モーダルダイアログ ( 全入力を独占。ホットキーより優先 )
2. ホストホットキー ( ダイアログをバイパスしてホストへ )
3. フォーカスを持つ非モーダルパネル ( 未処理キーのみ素通し )
4. ゲーム / レイヤ

ESC でのシーン復帰や PageUp/Down での画面切替を、slider 等を含む
操作パネル ( `showJson(json, true, false)` ) の表示中でも確実に効かせる
用途を想定しています。

**関連:** [Dialog.unregisterHotKey](Dialog.md#unregisterhotkey) / [Dialog.clearHotKeys](Dialog.md#clearhotkeys) / [Dialog.showJson](Dialog.md#showjson)

---

### unregisterHotKey

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 仮想キーコードを指定します。 |
| `shift` | `0` | 修飾キーの組合せ ( 既定 0 )。 |

**解説**

ホストホットキーの解除

[registerHotKey](#registerhotkey) で登録したホットキーを解除します
( key と shift の両方が一致するエントリを削除 )。

**関連:** [Dialog.registerHotKey](Dialog.md#registerhotkey)

---

### clearHotKeys

メソッド

**解説**

ホストホットキーの全解除

[registerHotKey](#registerhotkey) で登録したホットキーを全て解除します。

**関連:** [Dialog.registerHotKey](Dialog.md#registerhotkey)

---

### registerImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ストア上の名前 ( `mem://<name>` で参照 )。 |
| `path` | `&nbsp;` | 登録する画像の統一ストレージパス。 |

**戻り値**

読込・登録に成功したかどうか。

**解説**

実行時画像を登録する

統一ストレージパス path のファイルを name で実行時画像ストアへ登録します。jsonc の
image ウィジェット等からは `"mem://<name>"` で参照します。セーブサムネイル等、実行時に
変わる画像を Elements へ渡すための仕組みです。pixmap は画面 build 時に読み直されるので、
再登録 → 画面再オープンで表示が更新されます。

---

### unregisterImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 削除する画像の名前。 |

**解説**

実行時画像を削除する

[registerImage](#registerimage) で登録した name を実行時画像ストアから削除します。

---

### clearImages

メソッド

**解説**

実行時画像をすべて消去する

実行時画像ストアを全消去します。

---

### setVar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 変数名。 |
| `value` | `&nbsp;` | 設定する値 ( 文字列 )。 |

**戻り値**

書き込めたかどうか。

**解説**

表示中ダイアログの変数を書き換える

表示中ダイアログの変数 store へ値を書き込みます。JSON で `"text_var": name` を指定した
label 等が次フレームで更新されます。自分のインスタンスが非アクティブなら false を返します。

---

### setPadIconBase

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | pad_icon 素材のベースディレクトリ ( 統一ストレージパス )。 |

**解説**

pad_icon のベースディレクトリを設定する

pad_icon ( Kenney input prompts ) のベースディレクトリを設定します。dir は統一ストレージ
パス ( XP3 内でも可 )。配下に xbox/ps/switch/keyboard の各ディレクトリ + vector/*.svg がある
構成を想定します。未設定のままだと pad_icon は灰色プレースホルダになります。

---

### setPadTheme

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | テーマ名。 |

**戻り値**

名前を解釈できたかどうか。

**解説**

pad_icon の全体テーマを設定する

pad_icon の全体テーマ ( `"xbox"` / `"ps"` / `"switch"` / `"keyboard"` / `"none"` ) を
設定します。`"auto"` を指定すると、接続しているパッドの系統
( [System.padStyle](System.md#padstyle) ) からテーマを自動選択します。
パッドが無い場合は動作プラットフォームから決まり、画面を開くたびに決め直される
ため、途中でコントローラを差し替えても次に開く画面から追従します。
画面 JSON の top-level `"pad_theme"` が指定されていればそちらが優先されます。

---

### renderStatsReset

メソッド

**解説**

描画計測カウンタのリセット

[Dialog.renderStats](Dialog.md#renderstats) の累積カウンタを 0 クリアします。
計測区間の開始時に呼びます。

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

### onDrag

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `payload` | `&nbsp;` | ドラッグ状態を表す Dictionary ( 上記参照 )。 |

**解説**

ドラッグ通知

画面 JSON で `"drag_events": true` を指定した widget の 押下 → 移動 →
離す が届くイベントです。TJS 側で override してください。

payload は Dictionary で、`id` ( 発生元 widget の id )、`phase`
( `"begin"` / `"move"` / `"end"` )、`x` / `y` ( 現在位置 )、`dx` / `dy`
( 前回からの差分 )、`startX` / `startY` ( 押下位置 )、`modifiers`
( シフト状態 ) を持ちます。座標は画面 JSON に書いた座標系です。

溜まった `"move"` は最新の 1 件へ畳まれます ( `"begin"` / `"end"` は
畳まれません )。

**絵をドラッグに追従させるだけならこのイベントは不要です**。widget に
`"drag_at_var"` を書いてドラッグ位置を変数へ出し、canvas 子の `"at_var"`
へ同じ変数を挿すとエンジン内で完結します ( `"drag_bounds"` で可動域も
制限できます )。このイベントは「どこで離したか」のような判断を TJS 側で
行う用途に使います。

---

### onClose

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `action` | `&nbsp;` | 閉じる契機となった button の id ( `close_on_click` / Esc で閉じた場合。<br>[close](#close) 等で明示的に閉じた場合は空文字列 )。 |

**解説**

ダイアログ teardown 完了通知

このインスタンスのダイアログが閉じ切った ( teardown 完了 ) タイミングで発火する
非ブロッキング経路のイベントです。TJS 側で override してください。

---
