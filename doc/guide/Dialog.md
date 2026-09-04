# ダイアログ

## ダイアログについて

吉里吉里Z は、JSON / Dictionary で記述したレイアウトからボタン・チェックボックス・テキスト入力などを含むダイアログを表示する機構を内蔵しています。TJS からは [ElementsDialog](../reference/ElementsDialog.md) クラスで利用します ( 旧名 `Dialog`。ゲーム側スクリプトのクラス名と衝突しやすい汎用名だったため改名されました )。

このダイアログは、[Elements](https://github.com/wamsoft/elements) ( ThorVG ベースの C++ GUI ライブラリ ) を組み込んで実現されています。プラットフォーム依存のネイティブダイアログ ( Win32 の WIN32Dialog など ) とは異なり、SDL3 ビルドと Windows ネイティブ ( D3D11 ) ビルドの両方で同じ JSON 定義から同じ見た目のダイアログを表示できるのが特徴です。JSON / JSONC ( コメント付き JSON ) で記述したレイアウトを渡すだけで、レイアウト計算・描画・入力処理はエンジン側が行います。

Windows 標準の GUI に依存しないクロスプラットフォーム UI を目的とした機構のため、SDL3 ビルドでの利用を主眼に設計されていますが、WINVER ( Windows ネイティブ ) ビルドでも同じように動作します。

## 表示モード

ダイアログには、1 画面だけを表示する「単発ダイアログ」と、複数画面の遷移を含む「フロー」があります。それぞれにモーダル ( 閉じるまで TJS の処理をブロックする ) と非モーダル ( ゲーム画面に重ねて表示しメインループを止めない ) の別があります。

### 単発ダイアログ

| 表示モード | TJS API | 挙動 |
|---|---|---|
| 非モーダル ( オーバーレイ ) | [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) | 既存ゲーム画面の上にダイアログを描き、メインループを止めません。値の変化・ボタンのクリックは [onAction](../reference/ElementsDialog.md#onaction) で逐次通知されます。[close](../reference/ElementsDialog.md#close) で終了します。 |
| ブロッキングモーダル ( 独立ウィンドウ ) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) ( title / w / h を渡す ) | 新しいネイティブウィンドウを開き、閉じるまでブロッキングします。閉じると `%[ action, values ]` 形式の Dictionary を返します。 |
| ブロッキングモーダル ( オーバーレイ ) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) ( JSON 1 引数のみ ) | 独立ウィンドウを作らずに既存ゲーム画面に重ねて表示し、閉じるまでブロッキングします。戻り値は独立ウィンドウ版と同じです。 |
| ホストレイヤ描画 ( パネル ) | [ElementsPanel](../reference/ElementsPanel.md) ( `new ElementsPanel(layer)` + [showFile](../reference/ElementsPanel.md#showfile) 等 ) | オーバーレイではなく**指定した Layer のビットマップへ描画**します。z 順・トランジション・スクリーンショットへの写り込み・入力の帰属がレイヤの仕組みに従うので、HUD やゲーム画面の一部としての UI に使います。イベント / 変数 API は ElementsDialog と同形です。 |

`showModalJson` / `showModalFile` の戻り値は次の形式です。

```tjs
%[
    action: <閉じた button の id (Esc / × は "")>,
    values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]
```

モーダル中も [onAction](../reference/ElementsDialog.md#onaction) は発火しますが、ダイアログを閉じるのは JSON 側で `"close_on_click": true` を指定したボタン ( および Esc / × による中断 ) だけです。

### 複数画面フロー

複数の画面を順に切り替えていく「フロー」も定義できます。マニフェスト ( または Dictionary ) で複数画面と画面間の遷移を宣言します。

| 表示モード | TJS API | 挙動 |
|---|---|---|
| ブロッキング ( オーバーレイ ) | [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) | 複数画面の遷移をオーバーレイで実行します。フロー終了まで TJS をブロックし、最後に閉じた画面の `%[ action, values ]` を返します。 |
| 非モーダル ( 常駐 ) | [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) | 同じフロー定義を非ブロッキングで開始します ( ゲーム画面に常駐 )。`close` で閉じ、teardown ( 後始末 ) の完了は [active](../reference/ElementsDialog.md#active) で判別します。 |

画面が切り替わるタイミングで [onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave)、widget の操作で [onAction](../reference/ElementsDialog.md#onaction) が発火します。

#### 画面切替エフェクト ( fade / universal )

画面 JSON の `transitions` エントリを object 形式にすると、画面切替時の遷移エフェクトを宣言できます。CPU 合成のため、SDL / WINVER / GL のすべての DrawDevice で同一に動作します。

```jsonc
"transitions": {
    "next": { "target": "s2", "effect": "fade", "duration": 300 },
    "back": { "target": "<back>", "effect": "universal",
              "rule": "rule.png", "vague": 64, "duration": 500 }
}
```

| キー | 意味 |
|---|---|
| `effect` | `"fade"` = クロスフェード / `"universal"` = rule 画像によるユニバーサルトランジション。未対応名は警告ログ + 即切替 |
| `duration` | 所要時間 ms。省略 / 0 で 200ms |
| `rule` | universal の rule 画像 ( グレースケール。値が小さい画素ほど早く次画面へ切り替わる )。解決順 = 遷移を宣言した画面からの相対 → Storages パス → autopath 検索 |
| `vague` | 境界ぼかし幅 ( rule 値スケール 0〜255、既定 64 ) |

#### 退場 ( exit ) 演出との協調

要素の `"animate"` に `"on": "exit"` を付けると、画面が閉じる / 遷移するときに退場演出を再生してから遷移します。close_on_click / Esc などの画面内トリガに加えて、TJS からの [close](../reference/ElementsDialog.md#close) でも発火します ( 演出完了後に閉じ、フロー実行中は transitions を解決せずフローごと終了します )。

GPU ( OpenGL 描画 ) 側で同等のトランジションを行いたい場合は、[3D グラフィックシステム](Graphic3DSystem.md) の Canvas トランジション描画を参照してください。

## レイアウト密度の指定 ( gap / style )

既定は fit-to-content ( 内容に合わせたサイズ ) + 密着積みのため、明示指定を省略すると詰まった見た目になります。spacer を並べる代わりに、以下で密度をまとめて指定できます。

```jsonc
{
    "style": { "font_scale": 1.25, "row_height": 44, "tile_gap": 8, "padding": 24 },
    "content": { "type": "vtile", "gap": 12, "children": [ ... ] }
}
```

- `vtile` / `htile` の `"gap"` — 子要素間の隙間 px ( spacer 自動挿入と等価 )
- top-level `"style"` — `font_scale` ( 既定フォント倍率 ) / `tile_gap` ( gap 未指定タイルの既定 ) / `row_height` ( button 系 / input_box の既定最小高 ) / `padding` ( content 全体の外側余白 ) を、未指定値の既定として適用します

いずれも省略すれば従来と完全に一致します。

## 矩形テキスト ( text_area )

字幕やセリフ窓のように「決まった矩形に本文を流し込み、文字送りする」用途には `text_area` を使います。

```jsonc
{ "type": "text_area",
  "text": "…本文…",
  "size": 36,                    // px
  "font": "Noto Sans JP",        // 省略時はテーマ既定
  "align": "left",               // left / center / right
  "line_spacing": 12,            // 行間追加 px
  "count_var": "sub_count" }     // 文字送り ( -1 = 全部 )
```

- 折り返し・行頭行末禁則・文字送りの単位が [Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea) と**同じロジック**です。同じ本文・同じ幅・同じフォント / サイズなら**改行位置が一致**します ( レイヤ描画と Elements で字幕を出し分けても行組みがずれません )。
- `"count_var"` に変数名を与えると、ホストが [setVar](../reference/ElementsDialog.md#setvar) で数値を書くだけで文字送りが進みます。**折り返しは全文で確定してから count を適用する**ので、送っている途中でリフローしません。数える単位は [Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) と同じクラスタ ( 合字・結合文字・絵文字 ZWJ シーケンスで 1 ) です。
- 本文の差し替えは `"text_var"` / `"text_id"`、リストからの指定番号表示は `"text_list_id"` + `"index_var"` で、いずれも `label` と同じ規約です。
- 行ごとに固定の `"index"` と、行で共有する `"index_offset_var"` ( 先頭位置 ) を組み合わせると「N 行の窓」になります。ホストは [setVar](../reference/ElementsDialog.md#setvar) で**先頭位置の変数 1 個を動かすだけで一覧が送れる**ので、行ごとに変数を用意する必要がありません ( 一覧データ自体の差し替えは `"text_list_var"` )。
- 従来からある `text_box` は互換のためそのまま残っています ( 素朴なワード折り返し・禁則なし )。既存画面の改行位置は変わりません。

⚠ 絶対座標で置く ( `floating` の `"at"` を使う ) 場合は、top-level に `"size": [w, h]` を明示してください。省略するとダイアログが内容の最小サイズまで縮み、絶対座標がその外に出て何も表示されません。

## ドラッグ操作 ( drag_at_var / onDrag )

widget に `"drag_at_var"` を書くと、ドラッグ中の位置が `"x,y"` 形式でその変数へ書き込まれます。canvas の子の `"at_var"` に同じ変数を挿せば、TJS を介さずに**絵がドラッグへ追従**します ( エンジン内で完結するのでイベント配送の遅延を受けません )。可動域は `"drag_bounds": [x, y, w, h]` で制限できます。

「どこで離したか」のような判断を TJS 側で行いたい場合は、その widget に `"drag_events": true` を指定して [onDrag](../reference/ElementsDialog.md#ondrag) を実装します。

```tjs
class DragDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function DragDialog() { super.ElementsDialog(); }
    function onDrag(e) {
        // e.id / e.phase ( "begin" | "move" | "end" ) / e.x / e.y
        // e.dx / e.dy ( 前回からの差分 ) / e.startX / e.startY / e.modifiers
        if (e.phase == "end") {
            // 離した位置で当たり判定を取る、といった判断はここで
        }
    }
}
```

座標は画面 JSON に書いた座標系です。溜まった `"move"` は最新の 1 件へ畳まれます ( `"begin"` / `"end"` は畳まれません )。**見た目を追従させるだけなら onDrag は不要**で、`drag_at_var` + `at_var` の組み合わせで済みます。

## 一覧とスクロールバー ( list / atlas_scrollbar )

行が並ぶ画面は `"type": "list"` で組みます。**1 行分のテンプレートを行数ぶん複製**する仕組みで、行の位置・当たり判定・hover・選択・「データが足りない行の後始末」までウィジェット側が持ちます。TJS 側はデータを流し込むだけです。

```tjs
var layout = %[
  "content" => %[
    "type" => "list", "id" => "files",
    "rows" => 6, "row_size" => [676, 36], "pitch" => [0, 40],
    "index_offset_var" => "top", "count_var" => "n",
    "select_var" => "sel", "row_hover_var" => "rhov#index",
    "row" => %[ "type" => "label", "id" => "row#index",
                "text_list_var" => "items" ]
  ]
];
dlg.showDict(layout);
dlg.setVar("items", "file 0\nfile 1\nfile 2");   // 一覧データ
dlg.setVar("n", "3");                             // 総件数
```

- 文字列の中の `#index` が行番号へ置換されます ( `"id": "row#index"` → `row0` / `row1` … )。`text_list_var` を持つ要素には行番号と先頭位置が自動で挿さるので、テンプレートに 1 行書くだけで一覧になります
- 行をクリックすると [onAction](../reference/ElementsDialog.md#onaction) が **`payload` = データ index** で発火します ( 行の中にボタンがあればそちらが優先 )
- `count_var` を渡すと、データが無い行は描画も当たり判定も消えます
- hover / 選択の色は、行ごとのフラグ変数 ( `row_hover_var` / `row_select_var` を `"visible_var"` で受ける ) か、[onVar](../reference/ElementsDialog.md#onvar) で `hover_var` / `select_var` を拾ってホスト側のレイヤを差し替える形のどちらでも組めます

スクロールバーは `"type": "atlas_scrollbar"` に**同じ `index_offset_var`** を挿すだけです。つまみの長さは「見えている行数 ÷ 総件数」に比例し、つまみのドラッグ・溝クリックでのページ送り・ホイールまで内蔵しています ( 本文が `scroller` に載っている画面なら `scroller` の `pos_var` で足ります )。

## 変数の読み書きと変化通知 ( setVar / getVar / onVar )

画面 JSON の変数は 1 本の store にぶら下がっていて、[setVar](../reference/ElementsDialog.md#setvar) で書けるだけでなく [getVar](../reference/ElementsDialog.md#getvar) で読み出せます。読めるのは自分が書いた値だけではありません — `"vars_on_hover"` / `"vars_on_focus"`、slider の `"value_var"`、`"drag_at_var"`、一覧の `"index_offset_var"` のように**画面側が書いた値も同じ store**なので、そのまま読めます。

変化した時点で知りたい場合は [onVar](../reference/ElementsDialog.md#onvar) を実装します。

```tjs
class ListDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function ListDialog() { super.ElementsDialog(); }
    function onVar(name, value) {
        if (name == "row_hover") {
            // カーソルが乗っている行が変わった → ホスト側のレイヤを差し替える
            highlightRow(+value);
        }
    }
}
```

これで「**絵はホスト側のレイヤ、当たり判定だけダイアログ**」という構成が組めます。1 枚絵が大きすぎて atlas に積めない一覧画面などで、ダイアログには透明なボタンだけを並べて hover を受け取り、表示はゲーム側のレイヤで行う、という分担です。

- 通知は 1 フレーム遅延し、同じ変数の連続変化は最新の 1 件へ畳まれます。「いまの値」が要るときは [getVar](../reference/ElementsDialog.md#getvar) を読みます
- **onVar を実装したダイアログだけが観測対象**になります ( 実装していなければコストはかかりません )。受け取る変数を絞りたいときは [watchVars](../reference/ElementsDialog.md#watchvars) に名前を並べます — hover 連動変数やドラッグ位置は毎フレーム書き換わるためです
- 画面にどんな変数があるかは [listVars](../reference/ElementsDialog.md#listvars) で一覧できます ( 変数名・現在値・参照している widget の id と種類 )。デバッグパネルや画面 JSON の検証に使えます

## 非モーダルの複数同時表示とフォーカス

非モーダル ( オーバーレイ ) パネルの配置は画面 JSON の top-level `"align"` / `"margin"` で指定し、配置と拡縮の基準領域は top-level `"base"` で選べます — `"window"` ( 既定、ウィンドウ全面基準 ) / `"content"` ( ゲーム画像の表示領域基準。字幕窓のようにゲーム画像へ追従させたい場合 )。拡縮はゲームの基準面に対するウィンドウ ( または表示領域 ) の比率に追従するため、フルスクリーン等ではゲームと同率で拡大されます。ゲーム画面と別解像度で UI を author しているタイトル ( ゲーム画面 640x400 / UI 1920x1080 等 ) では、[ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) に author 基準面のサイズを設定すると拡縮の分母がそちらになり、ゲーム側の基準面サイズの変更にも巻き込まれません。

非モーダルダイアログ ( [showJson](../reference/ElementsDialog.md#showjson) / [startFlow](../reference/ElementsDialog.md#startflow) 系 ) は z-order 付きのインスタンスリストとして管理され、複数同時に表示できます。マウスは最前面からヒットテストし、キーボード / ゲームパッドはフォーカスを保持しているインスタンス ( z-order 末尾優先 ) に届きます。モーダルダイアログを重ねた場合、下のインスタンスは描画は維持されたまま入力だけがブロックされます。

非モーダル開始系 ( [startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) ) には `grabFocus` 引数があり、偽を指定すると「フォーカスを取らない常駐 HUD」として動きます。常駐 UI がゲームのホットキーまで食ってしまうのを防ぎたい場合に利用します。

非モーダルでは、Elements 側で実際に処理されたキーだけを消費し、未処理キーはゲームへ通過させる ( handled pass-through ) ため、メニューを開いたままゲーム本体のホットキーで別のダイアログを開く、といった共存も可能です。

### 入力の配送優先順位とホストホットキー

入力は次の優先順位で配送されます。

1. **最上位ホットキー** ( [System.registerHotKey](../reference/System.md#registerhotkey) ) — イベントポンプの入口。**モーダル表示中でも効く**唯一の層です ( フックは SDL3 系ビルドのみ配線されており、WINVER ビルドでは発火しません )
2. **モーダルダイアログ** — 全入力を独占 ( 下にもゲームにも通しません )
3. **ホストホットキー** ( [registerHotKey](../reference/ElementsDialog.md#registerhotkey) ) — 登録キーはダイアログへ渡らず [Window.onKeyDown](../reference/Window.md#onkeydown) 等へ直行
4. **フォーカスを持つ非モーダルパネル** — キー / パッドを受け、未処理分のみ素通し
5. **ゲーム / レイヤ** — 未消費の落ち先

単発表示系 ( [showJson](../reference/ElementsDialog.md#showjson) / showFile / showDict ) は第 3 引数 `modal` で「非モーダル + フォーカスあり」( `showJson(json, true, false)` ) を指定できます。slider や picker を含む操作パネルはこの形で出すと、パッドの十字 / A ボタンやキーボードでウィジェットを操作しつつ、パネルが使わないキーはゲームへ流れます。その上で ESC ( シーン復帰 ) や PageUp/Down ( 画面切替 ) のような「必ずホストが受けたいキー」を registerHotKey で確保するのが定石です ( 実例: `data/demolib/demo_common.tjs` の DemoShell )。

- ホットキーはテキスト入力ウィジェットにキャレットがある間は既定で抑止されます ( `duringTextInput = true` で入力中も有効化 )
- モーダル表示中はホットキーも無効です ( 確認ダイアログの ESC = cancel を奪いません )
- マウスボタン ( VK_RBUTTON 等 ) も登録でき、全画面透過 HUD が右クリックを拾って閉じてしまう問題の回避にも使えます
- 最上位ホットキー側のコールバックで「モーダルが出ている間は何もしない」と分岐したい場合は [ElementsDialog.modalActive](../reference/ElementsDialog.md#modalactive) を見ます ( モーダルインスタンスの有無。フォーカスを取らない常駐オーバレイは含みません )

### 入力バインドと named action

`"input"` ブロックの `"bindings"` で、キー / パッド / マウス / ホイールに**名前付きアクション** ( named action ) を割り当てられます。`"accept"` / `"cancel"` / `"nav_up"` … のような**組込名はダイアログ内で処理される**ため TJS へは届きません。組込以外の任意の名前を書いた場合だけ、その入力がホストへ通知されます。

```jsonc
"input": { "bindings": [
    { "wheel": "up",   "action": "prev_page" },   // 任意名 = ホストへ通知
    { "key": "escape", "action": "cancel" } ] }   // 組込名 = ダイアログ内で処理
```

通知は [onAction](../reference/ElementsDialog.md#onaction) で受けますが、**`id` は `"<action>"` 固定で、付けた名前は `payload` に入ります**。

```tjs
function onAction(id, payload) {
    if (id == "<action>") {
        switch (payload) {
        case "prev_page": /* ホイール上で前ページ */ break;
        }
    }
}
```

`id` に自分で付けた名前が来るものと思って書くと、**その入力だけが黙って無反応**になり原因に気づきにくいので注意してください。

## ミニマルな利用例

[Dialog](../reference/ElementsDialog.md) を継承したクラスで [onAction](../reference/ElementsDialog.md#onaction) を実装し、JSON レイアウトを渡して表示します。

```tjs
class TestDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function TestDialog() { super.ElementsDialog(); }
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

ボタン・入力欄などの widget を JSON でどう記述するかの一覧は、[Dialog](../reference/ElementsDialog.md) クラスリファレンスを参照してください。

## フォントの登録

ダイアログ描画に使うフォントは krkrz の Storages ( XP3 含む ) を経由して読み込まれます。スクリプトから明示的に登録するには [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [ElementsDialog.registerFontDir](../reference/ElementsDialog.md#registerfontdir) を、既定フォントファミリの確認・上書きには [ElementsDialog.defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) プロパティを使います。

エンジン側でも、起動時にリソースパス下の `.ttf` / `.otf` を自動スキャンして登録しています ( ファイル名から family / weight / slant / stretch を推定 )。

チェックボックスの ✓ や selection_menu の ▼ などのアイコングリフは、本文フォントではなくアイコンフォント `elements_basic.ttf` ( `resource/` に同梱 ) で描画されます。エンジンが自動登録するため通常は意識不要ですが、リソースを差し替える構成でこのフォントを外すと「枠は出るが ✓ が出ない」状態になります。

### 可変フォント ( ウェイト指定つき登録 )

`registerFont` のパスに `"#tag=val"` サフィックスを付けると、可変フォントの軸インスタンスを別名として登録できます。画面 JSON 側は `"font": "MyFont-Medium"` のような名前だけで、実体は 1 つの可変フォントに集約できます。widget の `"font"` に直接 `"MyFont#wght=700"` と書く指定も同じ表記です。

```tjs
ElementsDialog.registerFont("MyFont", "fonts/MyFont-VF.ttf");                   // 素の VF ( 無指定 = wght=400 )
ElementsDialog.registerFont("MyFont-Medium", "fonts/MyFont-VF.ttf#wght=500");   // 別名 = 軸インスタンス
```

### 言語連動フォント置換 ( 多言語 UI )

日本語 / 繁体字 / 簡体字のように文字体系ごとの別フォントを持つ UI では、[ElementsDialog.fontLanguages](../reference/ElementsDialog.md#fontlanguages) に言語→ファミリの置換表を設定しておくと、[ElementsDialog.language](../reference/ElementsDialog.md#language) の切替に連動してフォント解決時にファミリが差し替わります ( 共有コードポイントの漢字を表示言語に合った地域字形で描画できます )。表は画面 JSON の top-level `"font_languages"` でも宣言でき、特定 widget だけ言語を固定したい場合は widget の `"locale"` を指定します。

## ビルド構成

ダイアログ機能は `KRKRZ_USE_ELEMENTS=ON` ( デフォルト ) でビルドされたエンジンで利用できます。SDL3 ビルドと WINVER ( Windows ネイティブ / D3D11 ) ビルドの両方に対応します。`KRKRZ_USE_ELEMENTS=OFF` でビルドした場合は [ElementsDialog](../reference/ElementsDialog.md) / [ElementsPanel](../reference/ElementsPanel.md) クラスは登録されず、ダイアログ関連のコードはリンクから除外されて実行ファイルサイズが削減されます。

## 関連 API

- [ElementsDialog](../reference/ElementsDialog.md) — TJS バインディングクラス
- [ElementsPanel](../reference/ElementsPanel.md) — ホストのレイヤへ描くパネル ( イベント / 変数 API は同形 )
- [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) — 非モーダル
- [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) — モーダル
- [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) — ブロッキングフロー
- [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) — 非モーダル ( 常駐 ) フロー
- [ElementsDialog.onAction](../reference/ElementsDialog.md#onaction) / [onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave) / [onDrag](../reference/ElementsDialog.md#ondrag) — イベント
- [ElementsDialog.active](../reference/ElementsDialog.md#active) — 非モーダルの teardown 完了判定 / [modalActive](../reference/ElementsDialog.md#modalactive) — モーダル表示中かどうか
- [ElementsDialog.registerHotKey](../reference/ElementsDialog.md#registerhotkey) — ホストホットキー ( ダイアログをバイパス ) / [System.registerHotKey](../reference/System.md#registerhotkey) — 最上位ホットキー ( モーダル中でも効く )
- [ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) — UI の author 基準面サイズ / [renderScale](../reference/ElementsDialog.md#renderscale) — 描画密度
- [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [registerFontDir](../reference/ElementsDialog.md#registerfontdir) / [defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) — フォント登録
- [ElementsDialog.language](../reference/ElementsDialog.md#language) / [fontLanguages](../reference/ElementsDialog.md#fontlanguages) — i18n ( 表示言語と言語連動フォント置換 )
