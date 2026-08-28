# ダイアログ

## ダイアログについて

吉里吉里Z は、JSON / Dictionary で記述したレイアウトからボタン・チェックボックス・テキスト入力などを含むダイアログを表示する機構を内蔵しています。TJS からは [Dialog](../reference/Dialog.md) クラスで利用します。

このダイアログは、[Elements](https://github.com/wamsoft/elements) ( ThorVG ベースの C++ GUI ライブラリ ) を組み込んで実現されています。プラットフォーム依存のネイティブダイアログ ( Win32 の WIN32Dialog など ) とは異なり、SDL3 ビルドと Windows ネイティブ ( D3D11 ) ビルドの両方で同じ JSON 定義から同じ見た目のダイアログを表示できるのが特徴です。JSON / JSONC ( コメント付き JSON ) で記述したレイアウトを渡すだけで、レイアウト計算・描画・入力処理はエンジン側が行います。

Windows 標準の GUI に依存しないクロスプラットフォーム UI を目的とした機構のため、SDL3 ビルドでの利用を主眼に設計されていますが、WINVER ( Windows ネイティブ ) ビルドでも同じように動作します。

## 表示モード

ダイアログには、1 画面だけを表示する「単発ダイアログ」と、複数画面の遷移を含む「フロー」があります。それぞれにモーダル ( 閉じるまで TJS の処理をブロックする ) と非モーダル ( ゲーム画面に重ねて表示しメインループを止めない ) の別があります。

### 単発ダイアログ

| 表示モード | TJS API | 挙動 |
|---|---|---|
| 非モーダル ( オーバーレイ ) | [Dialog.showJson](../reference/Dialog.md#showjson) / [showFile](../reference/Dialog.md#showfile) | 既存ゲーム画面の上にダイアログを描き、メインループを止めません。値の変化・ボタンのクリックは [onAction](../reference/Dialog.md#onaction) で逐次通知されます。[close](../reference/Dialog.md#close) で終了します。 |
| ブロッキングモーダル ( 独立ウィンドウ ) | [Dialog.showModalJson](../reference/Dialog.md#showmodaljson) / [showModalFile](../reference/Dialog.md#showmodalfile) ( title / w / h を渡す ) | 新しいネイティブウィンドウを開き、閉じるまでブロッキングします。閉じると `%[ action, values ]` 形式の Dictionary を返します。 |
| ブロッキングモーダル ( オーバーレイ ) | [Dialog.showModalJson](../reference/Dialog.md#showmodaljson) / [showModalFile](../reference/Dialog.md#showmodalfile) ( JSON 1 引数のみ ) | 独立ウィンドウを作らずに既存ゲーム画面に重ねて表示し、閉じるまでブロッキングします。戻り値は独立ウィンドウ版と同じです。 |

`showModalJson` / `showModalFile` の戻り値は次の形式です。

```tjs
%[
    action: <閉じた button の id (Esc / × は "")>,
    values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]
```

モーダル中も [onAction](../reference/Dialog.md#onaction) は発火しますが、ダイアログを閉じるのは JSON 側で `"close_on_click": true` を指定したボタン ( および Esc / × による中断 ) だけです。

### 複数画面フロー

複数の画面を順に切り替えていく「フロー」も定義できます。マニフェスト ( または Dictionary ) で複数画面と画面間の遷移を宣言します。

| 表示モード | TJS API | 挙動 |
|---|---|---|
| ブロッキング ( オーバーレイ ) | [Dialog.showFlow](../reference/Dialog.md#showflow) / [showFlowScreens](../reference/Dialog.md#showflowscreens) | 複数画面の遷移をオーバーレイで実行します。フロー終了まで TJS をブロックし、最後に閉じた画面の `%[ action, values ]` を返します。 |
| 非モーダル ( 常駐 ) | [Dialog.startFlow](../reference/Dialog.md#startflow) / [startFlowScreens](../reference/Dialog.md#startflowscreens) | 同じフロー定義を非ブロッキングで開始します ( ゲーム画面に常駐 )。`close` で閉じ、teardown ( 後始末 ) の完了は [active](../reference/Dialog.md#active) で判別します。 |

画面が切り替わるタイミングで [onScreen](../reference/Dialog.md#onscreen) / [onScreenLeave](../reference/Dialog.md#onscreenleave)、widget の操作で [onAction](../reference/Dialog.md#onaction) が発火します。

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

要素の `"animate"` に `"on": "exit"` を付けると、画面が閉じる / 遷移するときに退場演出を再生してから遷移します。close_on_click / Esc などの画面内トリガに加えて、TJS からの [close](../reference/Dialog.md#close) でも発火します ( 演出完了後に閉じ、フロー実行中は transitions を解決せずフローごと終了します )。

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
- `"count_var"` に変数名を与えると、ホストが [setVar](../reference/Dialog.md#setvar) で数値を書くだけで文字送りが進みます。**折り返しは全文で確定してから count を適用する**ので、送っている途中でリフローしません。数える単位は [Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) と同じクラスタ ( 合字・結合文字・絵文字 ZWJ シーケンスで 1 ) です。
- 本文の差し替えは `"text_var"` / `"text_id"`、リストからの指定番号表示は `"text_list_id"` + `"index_var"` で、いずれも `label` と同じ規約です。
- 行ごとに固定の `"index"` と、行で共有する `"index_offset_var"` ( 先頭位置 ) を組み合わせると「N 行の窓」になります。ホストは [setVar](../reference/Dialog.md#setvar) で**先頭位置の変数 1 個を動かすだけで一覧が送れる**ので、行ごとに変数を用意する必要がありません ( 一覧データ自体の差し替えは `"text_list_var"` )。
- 従来からある `text_box` は互換のためそのまま残っています ( 素朴なワード折り返し・禁則なし )。既存画面の改行位置は変わりません。

⚠ 絶対座標で置く ( `floating` の `"at"` を使う ) 場合は、top-level に `"size": [w, h]` を明示してください。省略するとダイアログが内容の最小サイズまで縮み、絶対座標がその外に出て何も表示されません。

## ドラッグ操作 ( drag_at_var / onDrag )

widget に `"drag_at_var"` を書くと、ドラッグ中の位置が `"x,y"` 形式でその変数へ書き込まれます。canvas の子の `"at_var"` に同じ変数を挿せば、TJS を介さずに**絵がドラッグへ追従**します ( エンジン内で完結するのでイベント配送の遅延を受けません )。可動域は `"drag_bounds": [x, y, w, h]` で制限できます。

「どこで離したか」のような判断を TJS 側で行いたい場合は、その widget に `"drag_events": true` を指定して [onDrag](../reference/Dialog.md#ondrag) を実装します。

```tjs
class DragDialog extends Dialog {
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

## 非モーダルの複数同時表示とフォーカス

非モーダル ( オーバーレイ ) パネルの配置は画面 JSON の top-level `"align"` / `"margin"` で指定し、配置と拡縮の基準領域は top-level `"base"` で選べます — `"window"` ( 既定、ウィンドウ全面基準 ) / `"content"` ( ゲーム画像の表示領域基準。字幕窓のようにゲーム画像へ追従させたい場合 )。拡縮はゲームの基準面に対するウィンドウ ( または表示領域 ) の比率に追従するため、フルスクリーン等ではゲームと同率で拡大されます。ゲーム画面と別解像度で UI を author しているタイトル ( ゲーム画面 640x400 / UI 1920x1080 等 ) では、[Dialog.baseSize](../reference/Dialog.md#basesize) に author 基準面のサイズを設定すると拡縮の分母がそちらになり、ゲーム側の基準面サイズの変更にも巻き込まれません。

非モーダルダイアログ ( [showJson](../reference/Dialog.md#showjson) / [startFlow](../reference/Dialog.md#startflow) 系 ) は z-order 付きのインスタンスリストとして管理され、複数同時に表示できます。マウスは最前面からヒットテストし、キーボード / ゲームパッドはフォーカスを保持しているインスタンス ( z-order 末尾優先 ) に届きます。モーダルダイアログを重ねた場合、下のインスタンスは描画は維持されたまま入力だけがブロックされます。

非モーダル開始系 ( [startFlow](../reference/Dialog.md#startflow) / [startFlowScreens](../reference/Dialog.md#startflowscreens) ) には `grabFocus` 引数があり、偽を指定すると「フォーカスを取らない常駐 HUD」として動きます。常駐 UI がゲームのホットキーまで食ってしまうのを防ぎたい場合に利用します。

非モーダルでは、Elements 側で実際に処理されたキーだけを消費し、未処理キーはゲームへ通過させる ( handled pass-through ) ため、メニューを開いたままゲーム本体のホットキーで別のダイアログを開く、といった共存も可能です。

### 入力の配送優先順位とホストホットキー

入力は次の優先順位で配送されます。

1. **最上位ホットキー** ( [System.registerHotKey](../reference/System.md#registerhotkey) ) — イベントポンプの入口。**モーダル表示中でも効く**唯一の層です ( フックは SDL3 系ビルドのみ配線されており、WINVER ビルドでは発火しません )
2. **モーダルダイアログ** — 全入力を独占 ( 下にもゲームにも通しません )
3. **ホストホットキー** ( [registerHotKey](../reference/Dialog.md#registerhotkey) ) — 登録キーはダイアログへ渡らず [Window.onKeyDown](../reference/Window.md#onkeydown) 等へ直行
4. **フォーカスを持つ非モーダルパネル** — キー / パッドを受け、未処理分のみ素通し
5. **ゲーム / レイヤ** — 未消費の落ち先

単発表示系 ( [showJson](../reference/Dialog.md#showjson) / showFile / showDict ) は第 3 引数 `modal` で「非モーダル + フォーカスあり」( `showJson(json, true, false)` ) を指定できます。slider や picker を含む操作パネルはこの形で出すと、パッドの十字 / A ボタンやキーボードでウィジェットを操作しつつ、パネルが使わないキーはゲームへ流れます。その上で ESC ( シーン復帰 ) や PageUp/Down ( 画面切替 ) のような「必ずホストが受けたいキー」を registerHotKey で確保するのが定石です ( 実例: `data/demolib/demo_common.tjs` の DemoShell )。

- ホットキーはテキスト入力ウィジェットにキャレットがある間は既定で抑止されます ( `duringTextInput = true` で入力中も有効化 )
- モーダル表示中はホットキーも無効です ( 確認ダイアログの ESC = cancel を奪いません )
- マウスボタン ( VK_RBUTTON 等 ) も登録でき、全画面透過 HUD が右クリックを拾って閉じてしまう問題の回避にも使えます
- 最上位ホットキー側のコールバックで「モーダルが出ている間は何もしない」と分岐したい場合は [Dialog.modalActive](../reference/Dialog.md#modalactive) を見ます ( モーダルインスタンスの有無。フォーカスを取らない常駐オーバレイは含みません )

## ミニマルな利用例

[Dialog](../reference/Dialog.md) を継承したクラスで [onAction](../reference/Dialog.md#onaction) を実装し、JSON レイアウトを渡して表示します。

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

ボタン・入力欄などの widget を JSON でどう記述するかの一覧は、[Dialog](../reference/Dialog.md) クラスリファレンスを参照してください。

## フォントの登録

ダイアログ描画に使うフォントは krkrz の Storages ( XP3 含む ) を経由して読み込まれます。スクリプトから明示的に登録するには [Dialog.registerFont](../reference/Dialog.md#registerfont) / [Dialog.registerFontDir](../reference/Dialog.md#registerfontdir) を、既定フォントファミリの確認・上書きには [Dialog.defaultFontFamily](../reference/Dialog.md#defaultfontfamily) プロパティを使います。

エンジン側でも、起動時にリソースパス下の `.ttf` / `.otf` を自動スキャンして登録しています ( ファイル名から family / weight / slant / stretch を推定 )。

チェックボックスの ✓ や selection_menu の ▼ などのアイコングリフは、本文フォントではなくアイコンフォント `elements_basic.ttf` ( `resource/` に同梱 ) で描画されます。エンジンが自動登録するため通常は意識不要ですが、リソースを差し替える構成でこのフォントを外すと「枠は出るが ✓ が出ない」状態になります。

### 可変フォント ( ウェイト指定つき登録 )

`registerFont` のパスに `"#tag=val"` サフィックスを付けると、可変フォントの軸インスタンスを別名として登録できます。画面 JSON 側は `"font": "MyFont-Medium"` のような名前だけで、実体は 1 つの可変フォントに集約できます。widget の `"font"` に直接 `"MyFont#wght=700"` と書く指定も同じ表記です。

```tjs
Dialog.registerFont("MyFont", "fonts/MyFont-VF.ttf");                   // 素の VF ( 無指定 = wght=400 )
Dialog.registerFont("MyFont-Medium", "fonts/MyFont-VF.ttf#wght=500");   // 別名 = 軸インスタンス
```

### 言語連動フォント置換 ( 多言語 UI )

日本語 / 繁体字 / 簡体字のように文字体系ごとの別フォントを持つ UI では、[Dialog.fontLanguages](../reference/Dialog.md#fontlanguages) に言語→ファミリの置換表を設定しておくと、[Dialog.language](../reference/Dialog.md#language) の切替に連動してフォント解決時にファミリが差し替わります ( 共有コードポイントの漢字を表示言語に合った地域字形で描画できます )。表は画面 JSON の top-level `"font_languages"` でも宣言でき、特定 widget だけ言語を固定したい場合は widget の `"locale"` を指定します。

## ビルド構成

ダイアログ機能は `KRKRZ_USE_ELEMENTS=ON` ( デフォルト ) でビルドされたエンジンで利用できます。SDL3 ビルドと WINVER ( Windows ネイティブ / D3D11 ) ビルドの両方に対応します。`KRKRZ_USE_ELEMENTS=OFF` でビルドした場合は [Dialog](../reference/Dialog.md) クラスは登録されず、ダイアログ関連のコードはリンクから除外されて実行ファイルサイズが削減されます。

## 関連 API

- [Dialog](../reference/Dialog.md) — TJS バインディングクラス
- [Dialog.showJson](../reference/Dialog.md#showjson) / [showFile](../reference/Dialog.md#showfile) — 非モーダル
- [Dialog.showModalJson](../reference/Dialog.md#showmodaljson) / [showModalFile](../reference/Dialog.md#showmodalfile) — モーダル
- [Dialog.showFlow](../reference/Dialog.md#showflow) / [showFlowScreens](../reference/Dialog.md#showflowscreens) — ブロッキングフロー
- [Dialog.startFlow](../reference/Dialog.md#startflow) / [startFlowScreens](../reference/Dialog.md#startflowscreens) — 非モーダル ( 常駐 ) フロー
- [Dialog.onAction](../reference/Dialog.md#onaction) / [onScreen](../reference/Dialog.md#onscreen) / [onScreenLeave](../reference/Dialog.md#onscreenleave) / [onDrag](../reference/Dialog.md#ondrag) — イベント
- [Dialog.active](../reference/Dialog.md#active) — 非モーダルの teardown 完了判定 / [modalActive](../reference/Dialog.md#modalactive) — モーダル表示中かどうか
- [Dialog.registerHotKey](../reference/Dialog.md#registerhotkey) — ホストホットキー ( ダイアログをバイパス ) / [System.registerHotKey](../reference/System.md#registerhotkey) — 最上位ホットキー ( モーダル中でも効く )
- [Dialog.baseSize](../reference/Dialog.md#basesize) — UI の author 基準面サイズ / [renderScale](../reference/Dialog.md#renderscale) — 描画密度
- [Dialog.registerFont](../reference/Dialog.md#registerfont) / [registerFontDir](../reference/Dialog.md#registerfontdir) / [defaultFontFamily](../reference/Dialog.md#defaultfontfamily) — フォント登録
- [Dialog.language](../reference/Dialog.md#language) / [fontLanguages](../reference/Dialog.md#fontlanguages) — i18n ( 表示言語と言語連動フォント置換 )
