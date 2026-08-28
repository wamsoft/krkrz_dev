---
name: elements
description: 吉里吉里Z 上の Elements ベース汎用ダイアログ/画面 UI (cycfi/elements + elements_modal) の作り方リファレンス。TJS で JSON / Dictionary 定義のダイアログを作る・出す・イベントを受ける・複数画面フロー(navigator)や常駐メニューを組む・入力/フォーカス/モーダルを制御する・Agent で動作検証する、といった場面で使う。基本的なダイアログ画面の作り方(最小例・レイアウト JSON スキーマ・ウィジェット一覧)から、モーダル/非モーダル/独立ウィンドウ/常駐フロー、複数インスタンス/z-order、DrawDevice 登録タイミング等のハマりどころまで網羅。Win32 ネイティブの WIN32Dialog(win32dialog プラグイン)とは別物。TJS2 言語仕様は skill `tjs2`、本体クラス API は `krkrz`、REPL/Agent 駆動は `krkrz-repl` を参照。
---

# Elements ベース ダイアログ / 画面 UI (krkrz)

吉里吉里Z に埋め込んだ [Elements](https://github.com/wamsoft/elements) (ThorVG/cycfi ベースの C++ GUI) で、**JSON / TJS Dictionary 定義のダイアログや画面**を出す仕組み。`Dialog` クラス経由で使う。全デスクトップ変種 (SDL3 / WINVER / OGL) で動作する。

> **Win32 の `WIN32Dialog`(win32dialog プラグイン)とは別物**。あちらは Win32 ネイティブダイアログ。こちらは全 PF 共通の Elements UI。

## パスの読み方
本文のエンジンパスは engine ルート相対 (`common/...`, `data/...`, `doc/...`, `external/...`)。
本スキルが置かれている **umbrella (`krkrz_dev`) では `src/core/` を前置**して読む
(例: `src/core/doc/ElementsDialog.md`、`src/core/data/ui/`、`src/core/external/elements/`)。
engine 単独チェックアウトならそのまま。

## ゲーム (KAG/kag) へ組み込むときは
**[`references/krkr_integration.md`](references/krkr_integration.md) を読む** — 案件へ載せるときの統合知識: 層構成 (基盤 TJS + 画面ドライバ) / 表示経路の選択と engine 側の制約 (overlay のサイズ上限・`showFile` が autopath に乗らない・サブクラスの `super.Dialog()`) / KAG の openDialog 枠へ乗せるホストレイヤ方式と z オーダー / ドライバの型とライフサイクルの落とし穴 (常駐画面の再表示・タブ切替) / 値と動的画像の注入 / 資材探索とフォント一括登録 / 遷移エフェクト / Agent 検証の癖 / 未解決の engine TODO。

## 最初に読むべき一次資料 (SSOT)
- **`doc/ElementsDialog.md`** — 機構全体・API 経路・入力ルーティング・複数インスタンス・フェーズ状態。**まずこれ**。
- **`external/elements/external/elements_modal/README.md`** — **JSON レイアウトの全ウィジェット/属性カタログ**(下の一覧は要約)。
- 実例: `data/ui/about.json` / `data/ui/menu/*.json` + `data/ui/menu/app.jsonc`(navigator フロー) / `data/elements_gallery/` / `data/transition_demo/` / `data/startup.tjs`(`FlowMenuDialog` 常駐メニュー)。

---

## 1. 基本的なダイアログの作り方 (最小例)

`Dialog` を継承し、`onAction` でボタン等に反応、`showJson`(または `showDict`)で表示、`close()` で閉じる。**非モーダル (オーバーレイ) が基本形**。

```tjs
class MyDialog extends Dialog {
    function onAction(id, payload) {
        // state widget の値変化 / button click で発火 (payload: 値、button は void)
        switch (id) {
        case "ok":     System.inform("OK が押されました"); close(); break;
        case "cancel": close(); break;
        }
    }
}
var dlg = new MyDialog();
dlg.showJson('{
    "size": [360, 200],
    "background": [30, 30, 60, 245],
    "input": { "arrow_focus_nav": true },
    "content": { "type": "margin", "padding": 20, "child": {
        "type": "vtile", "children": [
            { "type": "align_center",
              "child": { "type": "label", "text": "こんにちは", "size_scale": 1.3 } },
            { "type": "vspacer", "height": 20 },
            { "type": "htile", "children": [
                { "type": "button", "id": "ok",     "text": "OK",     "initial_focus": true },
                { "type": "hspacer", "width": 12 },
                { "type": "button", "id": "cancel", "text": "キャンセル" }
            ] }
        ]
    } }
}');
```

### Dictionary で書く (`showDict`) — JSON 文字列を書かなくて済む
`common/visual/elements/VariantJsonUtil.cpp` が Dictionary→JSON へ変換してから同じ経路に流す。JSON をエスケープせずに書けて可読性が高い。

```tjs
dlg.showDict(%[
    size: [360, 200], background: [30, 30, 60, 245],
    input: %[ arrow_focus_nav: true ],
    content: %[ type: "margin", padding: 20, child: %[
        type: "vtile", children: [
            %[ type: "label", text: "こんにちは", size_scale: 1.3 ],
            %[ type: "vsize", height: 40,
               child: %[ type: "button", id: "ok", text: "OK", close_on_click: true ] ],
        ] ] ]
]);
```
- **`Dialog.dictToJson(value)`** で変換結果 JSON を取得できる (デバッグ / 資材書き出し)。
- **TJS Dictionary の制約 2 点**(重要):
  1. **bool が無い**: `true`=整数1。`close_on_click: true` は JSON の `1` になる (elements 側は 0/非0 を真偽として受ける)。
  2. **空文字キー不可**: navigator の既定遷移 `"": "<exit>"` は Dict で書けない → 未定義 action フォールバック(entry=exit / 子画面=pop)で足りるか、その画面だけ JSON 文字列にする。

---

## 2. レイアウト JSON スキーマ

### トップレベル
| キー | 型 | 説明 |
|---|---|---|
| `size` | `[w,h]` | **希望論理サイズ(上限)**。実サイズは content の自然サイズにフィット縮小(上余白対策) |
| `background` | `[r,g,b,a]` | content 描画前の塗り(省略=透明・縁なし) |
| `align` | `"center"`(既定)/`top`/`bottom`/`left`/`right`/`top_left`/`bottom_right` 等 | overlay 上の配置。入力座標補正も同じなのでクリックずれ無し。全 overlay 経路で有効 |
| `margin` | int | 非中央側のサーフェス端からの余白 px(既定 0)。例: 左上メニュー = `"align":"top_left","margin":24` |
| `locale` | `"ja-JP"` 等 | label の locale 未指定時の既定(CJK 同形字の出し分け) |
| `content` | element | ルート要素 |
| `input` | object | キー/パッドナビ設定(§6) |
| `vars` | `{name:string}` | 変数 store 初期値(`label.text_var` / `vars_on_focus` が参照) |
| `transitions` | `{action:target}` | navigator の遷移定義(§5)。object 形式で画面切替エフェクト(`effect`/`duration`/`rule`/`vague`)も宣言可 |
| `pad_theme` | `xbox`/`ps`/`switch`/`keyboard`/`none` | pad_icon の名前解決 |
| `atlases` | `{name:spec}` | テクスチャアトラス事前ロード(`atlas_*` が参照) |
| `font_scale` | number | 明示 size を持たない button/toggle/check_box/label の既定フォント倍率(既定 1.0) |
| `style` | object | **レイアウト密度の一括指定**: `%[font_scale, tile_gap(gap未指定タイルの既定), row_height(button系/input_box/selection_menu の既定最小高), padding(content外側余白)]`。全て省略=従来一致。既定の「詰まった」見た目を spacer なしで解消できる |

### ウィジェット (`"type"`) 要約 (全リストは elements_modal/README.md)
**レイアウト**: `vtile`/`htile`(`children`,`gap`=子間隙間px・省略時 style.tile_gap→0) / `margin`(`padding`,`child`) / `hsize`/`vsize`(`width`|`height`,`child`) / `hspacer`/`vspacer`(`width`|`height`) / `spacer`(`size`) / `align_center`/`align_left`/`align_right`/`align_top`/`align_middle`/`align_bottom`/`align_center_middle`(`child`) / `box`(`color`) / `band`(`color`+任意`child`) / `layer`(`children`,先頭=最前) / `group`(`title`,`child`) / `scroller`(`child`) / `filler` / `floating`(`at:[x,y,w,h]`,`child`) / `canvas`(`children` に `at` 付き、PSD 絶対配置向け。`choice_nav:true` で子 choice 群を 1 フォーカスの左右トグル化、子の `at_var` で配置を変数駆動)。
**注意**: `hsize`/`vsize` の指定値は **child の limits に clamp される** (cycfi fixed_size 仕様)。label 等の固定 max を持つ child を直接包んでも希望サイズまで広がらない → 全体サイズを確定したい画面は各パーツ幅を明示して自然サイズ=希望値にするのが確実。
**長文テキスト**: `text_box` — 複数行・自動折返しの静的テキスト (`text`,`size`|`size_scale`,`color`,`mono`=等幅,`text_var`=setVar で本文丸ごと差替え)。幅は親 (`hsize`) が決め、高さは折返しに追従。長文は親に `scroller`。行 label 大量生成より軽い。実例=`data/ui/license_dialog.tjs` (showLicenseDialog: 左=一覧/右=text_box の 2 ペイン全画面モーダル、モーダル中も onAction→setVar が同期で効く)。
**矩形テキスト/字幕**: `text_area` — 矩形へ流し込む静的テキスト (`text`/`text_id`/`text_var`/`text_list_id`+`index_var` は label と同規約, `size`|`size_scale`, `color`, `font`=comma区切りfamilies, `align`=left/center/right, `line_spacing`=行間追加px, `base`=auto/ltr/rtl, **`count_var`=文字送り** (-1=全部))。**折返し・行頭行末禁則・count が本体 `Layer.drawShapedTextArea` と同一ロジック**なので同じ本文・同じ幅なら**改行位置が一致**する (glyphware `layoutBlock`)。折返しは全文で確定してから count を適用=送ってもリフローしない。数える単位はクラスタ (`Layer.shapedTextCount` と同じ)。`text_box` は従来互換 (素朴な折返し・禁則なし) で据置なので**既存画面の改行は変わらない**。⚠`floating` の絶対座標で置くなら top-level `"size":[w,h]` を必ず書く (省略するとダイアログが内容最小サイズまで縮み**何も見えない**)。仕様=elements `docs/block-text.md`。
**入力/state**: `label`(`text`,`size`=px絶対 or `size_scale`=倍率,`color`,`text_var`,`text_id`=i18n,`text_list`+`index_var`=指定番号表示) / `button`(`text`,`id`) / `checkbox`|`check_box`(`text`,`id`,`value`) / `toggle_button` / `input_box`(`placeholder`,`id`,`size`) / `selection_menu`(`id`,`options`,`selected`) / `invert_button` / `ring_button` / `labeled_row`(`label`,`label_width`,`child`) / `tab_view`(`tabs`,`initial`) / picker 系 `cycle_picker`/`framed_cycle_picker`/`segmented_picker`(`options`|`options_id`=i18n,`initial`,`font_size`,`index_var`=選択indexを変数へ)。
**装飾/画像**: `pad_icon`(コントローラアイコン) / `sprite_button` / `atlas_image`(`rect` or `rect_list`+`index_var`=変数で矩形切替)/`atlas_button`/`atlas_toggle`/`atlas_choice`(排他)/`atlas_slider`(thumb 形式 or `fill`+`fill_at` ゲージ形式、`value_var`)/`atlas_progress`/`atlas_cycle_picker`(画像矢印ピッカー、フォーカス=矢印hilite)/`animated_sprite` / `gizmo_image`(9patch)。
- 色は `[r,g,b,a]` 配列(0–255)。フォントサイズは **`size`=px絶対 / `size_scale`=倍率**(テーマ既定≒14px 比)。JSON/JSONC(コメント+末尾カンマ)可。
- **i18n**: top-level `strings`(`{id:{lang:str}}`) + `lang`。`text_id`/`options_id`/`text_list_id` が現在言語で解決される。**TJS からの実行中切替は `Dialog.language = "en"`**(表示中の全ダイアログへ即時反映・開き直し不要、picker は選択 index 維持。以後開く画面の既定にもなる)。
- **変数連動**: picker `index_var`(**双方向**: 選択変更で書き + setVar で quiet 追従) ↔ `text_list`/`rect_list` の `index_var`(読み) を同名にすると選択連動(機種選択→SPEC/スクショ等)。`value_var`=10進小数、`at_var`=`"x,y[,w,h]"`。picker `enabled_var`=選択肢の有効/無効 mask(`'0'/'1'`文字列、step/click が無効 index をスキップ。未開放機種の出し分け)。choice (`atlas_choice`/`radio_button`) の `selected_var`+`selected_value`=ラジオグループ変数(グループ全員同じ var + 異なる value、var==value の1個が選択、双方向)。TJS からは `dlg.setVar(name, value)` で駆動。
- **モーダルへの初期 vars 注入**: `dlg.showModalFile(path, %[name=>value,...])`(showModalJson/Dict も同様、第2引数 Dictionary)。build 直後・pump 前に変数 store へ流し込む(モーダル中は TJS がブロックされ setVar 不可のため)。モーダル中も onAction は同期で届く。
- **pad_icon/フォント setup (static)**: `Dialog.setPadIconBase(dir)`(Kenney SVG のベース storage パス。未設定だと灰色プレースホルダ)/`Dialog.setPadTheme("xbox"|"ps"|"switch"|"keyboard"|"auto")`(`"auto"`=接続パッドの系統〔`System.padStyle`〕から自動選択、画面を開くたび決め直し)/`Dialog.registerFontDir(dir)`/`Dialog.defaultFontFamily = "Open Sans, Roboto, Noto Sans JP, ..."`(明示設定は自動 theme 並びに上書きされない。Emoji 系は必ず末尾に)。
- **要素の有効/無効を変数連動**: button 系(`button`/`atlas_button`/`invert_button`/`ring_button`)の `enabled_var`。値 `"0"` で無効、それ以外(既定)で有効。無効中はクリック/キー決定が効かず、描画は `disabled` frame があればそれ、無ければ半透明。進行で開放されるメニュー項目(未クリアなら「おまけ」を灰色)等に。

### static 設定一覧 (クラス全体に効く。`Dialog.xxx`)

⚠ **`Dialog` を継承したクラスのメソッド内から触るときは `global.Dialog.xxx`**。素の `Dialog` は親クラス参照になり、static プロパティへの代入が「メンバが見つかりません」になる。

| プロパティ | 既定 | 用途 |
|---|---|---|
| `language` | `""` | i18n 表示言語。代入で表示中の全画面へ即時反映(上記 i18n 参照) |
| `focusRing` | `true` | フォーカス中要素に描かれる汎用の枠(青い角丸)。**状態別の絵を持つ画像 UI では `false`** にする(枠が素材に重なるため)。button/slider/dial/thumbwheel が対象。フォーカス自体は生きるのでキー/パッド操作と `hilite` 切替は不変 |
| `renderCache` | `true` | 変化の無いフレームの再ラスタ+再アップロードを省略。アイドルがゼロコストになる。`false` は負荷比較用 |
| `partialRedraw` | `true` | 変化した矩形だけ描き直す(ダーティ矩形)。`false` は全面 |
| `renderScale` | `0` | ラスタライズ密度。0=auto(present サイズで直接)/`>0`=authored×倍率で描いて拡縮 |
| `renderStats` / `renderStatsReset()` | — | 描画パイプラインの区間計測(frames/rasters/partials/updateUs/rasterUs/uploadUs/presentUs 等)。累積値なので2回読んで差分を取る。計測画面=`data/elements_bench`(`-benchauto` で無操作スイープ) |
| `renderCount` | — | 累計ラスタライズ回数。アイドルで増えなければ renderCache が効いている |

### interactive 属性 (focusable widget 共通)
- **`"id"`** — `onAction` / `result.values` / shortcut / setVar の参照キー。
- **`"initial_focus": true`** — 起動時フォーカス候補(複数なら build 順で先勝ち)。
- **`"close_on_click": true`** — **既定 false**。true の button だけが click で「閉じて確定」する(`result.action=id`)。false は `onAction` を発火するだけで閉じない → OK/Cancel 等の「閉じるボタン」にだけ付ける。

---

## 3. 表示経路の使い分け (`Dialog` メソッド)

| メソッド | モード | 用途 |
|---|---|---|
| `showJson(json[, grabFocus=true[, modal=grabFocus]])` / `showFile(path, ...)` | overlay・非ブロッキング | 通常のダイアログ。`onAction` 逐次、`close()` で終了。**`showJson(json, true, false)`=非モーダル+フォーカスあり(操作パネル推奨形)** |
| `showDict(dict, ...)` | 同上の Dictionary 版 | JSON を書かずに |
| `showModalJson(json)` / `showModalDict(dict)` | overlay モーダル・**ブロッキング** | ゲーム画面上に nested ループ。戻り値 `%[action, values]` |
| `showModalJson(json, title, w, h)` | **独立 OS ウィンドウ**モーダル・ブロッキング | 別ウィンドウ。SDL=run_modal / WINVER=専用 Win32 窓 |
| `showFlow(manifest)` / `showFlowScreens(dict, entry)` | overlay・ブロッキング・複数画面 | navigator フロー(§5) |
| `startFlow(manifest)` / `startFlowScreens(dict, entry)` | overlay・**非ブロッキング・常駐** | 出しっぱなしメニュー。背景動作と併存(§5) |

- **ブロッキング(showModal*/showFlow)** は `result` を返す: `result.action`=閉じた button id(Esc/× は `""`)、`result.values`=state widget 最終値マップ。
- `showFile`/`showFlow` のパスは **Storages 解決**(autopath)。画面ファイルの相対資材はその画面ファイルのディレクトリ起点。

---

## 4. イベント (Dialog をサブクラスして override)
```tjs
class D extends Dialog {
    function onAction(id, payload)      { /* 値変化 / click。payload=値(buttonはvoid) */ }
    function onClose(action)            { /* teardown 完了。action=閉じた button id(外部要因は空) */ }
    function onScreen(name)             { /* フロー: 画面 enter */ }
    function onScreenLeave(name, act)   { /* フロー: 画面 leave */ }
    function onDrag(e)                  { /* ドラッグ。e=%[id,phase,x,y,dx,dy,startX,startY,modifiers] */ }
}
```
- `onAction` は **全 button click と state widget 値変化**で発火(TVPPostEvent 経由)。
- **`onDrag`** は画面 JSON で `"drag_events": true` を書いた widget の 押下→移動→離す で発火。
  `e.phase` は `"begin"` / `"move"` / `"end"`(TJS Dictionary に bool が無いので文字列)。
  座標は画面 JSON の座標系。溜まった `move` は最新 1 件へ畳まれる(`begin`/`end` は畳まない)。
  ⚠ **掴んだ絵をついてこさせるだけなら `onDrag` は要らない**: widget に
  `"drag_at_var": "名前"` を書くと位置が `"x,y"` で変数へ書かれ、canvas 子の `"at_var"` に
  同じ変数を挿すだけで追従する(C++ 内で完結しフレーム同期)。`"drag_bounds": [x,y,w,h]` で
  可動域も制限できる。`onDrag` は「どこで離したか」等の**判断**用。
- **サブクラスは必ず `super.Dialog()` を呼ぶ**(コンストラクタ)。呼ばないと native インスタンスが未初期化になる。
- ホスト→UI の値反映: **`dlg.setVar(name, value)`**(`vars`/`text_var` を subscribe した label が次フレームで更新)。ソフトキーボードの入力表示等。

---

## 5. 複数画面フロー (navigator) と 常駐メニュー
1 つの overlay 上で複数画面 (JSON) を遷移。各画面の top-level `"transitions"` が「閉じトリガ action id → 次手」を定義:
- target 語彙: `"name"`(push・山括弧不要)/ `"<back>"`(pop)/ `"<replace:name>"` / `"<stay>"` / `"<exit>"`(または空)。未定義 action は entry=exit / 子=pop にフォールバック。
- 画面遷移する button は **`close_on_click:true` + `transitions`**。その場で動く(閉じない) button は `close_on_click` 無し(`onAction` のみ)。
- **画面切替エフェクト** (krkrz overlay 配線済・CPU 合成で全 DrawDevice 同一動作): entry を object 形式にして `%[target:"s2", effect:"fade", duration:300]` / `%[target:"<back>", effect:"universal", rule:"rule.png", vague:64, duration:500]`。`rule` はグレースケール画像(値が小さい画素から先に次画面へ)、解決順=宣言した画面の相対→Storages→autopath。未対応 effect / rule 不在は警告+即切替(rule 不在は fade フォールバック)。デモ: `src/core/data/elements_flow/`。
- **退場(exit)演出**: 要素の `"animate"` に `"on":"exit"` を付けると、閉じ/遷移時に演出を再生してから finish する(session 内自動協調)。TJS `Dialog.close()` でも発火(演出完了後に閉じ、transitions は解決せずフロー終了)。`"animate"` は move/scale/rotate/fade を `from`/`to`/`frames`/`easing` で指定するパーツ演出(トリガ `on`: enter(既定)/focus/select/exit/hover/change)。

```tjs
// ブロッキング複数画面: マニフェスト or インライン辞書
var r = dlg.showFlow("ui/app.jsonc");
var r = dlg.showFlowScreens(%[ "menu": '{...}', "settings": '{...}' ], "menu");

// 常駐(非ブロッキング)メニュー: 出しっぱなしで背景動作と併存
dlg.startFlow("ui/menu/app.jsonc");   // 即 return(戻り値=起動成否)
// dlg.active … この dlg が今アクティブか(getter)   dlg.close() … 閉じる
```
実例: `data/startup.tjs` の `FlowMenuDialog` + `data/ui/menu/*.json`。

---

## 6. 入力・フォーカス・モーダル・複数インスタンス
- **配送優先順位 (2026-08-11 整理)**: `モーダル(全消費) > ホストホットキー(バイパス) > フォーカスパネル(handled素通し) > ゲーム`。
- **複数インスタンス同時表示 OK**(z-order。先頭=最背面/末尾=最前面)。各インスタンスは `modal` フラグを持つ。
  - `modal=true`(showJson 既定/showModal*/showFlow): 全入力を独占(下・ゲームに通さない)。
  - `modal=false`(startFlow/startFlowScreens、showJson 系は第3引数で指定可): ヒットしない入力は下/ゲームへ**素通し**。
- **用途 3 態**: モーダル `showJson(json)` / **操作パネル `showJson(json, true, false)`**(キー/パッドがパネルへ届き、未処理分はホストへ素通し。パッド十字=フォーカスナビ/A=決定) / 表示専用 HUD `showJson(json, false)`(キーを一切受けない)。
- **キーボードフォーカス**: modal または `wants_focus` の最前面が保持。後から開いた focus-grab が自然に前面、閉じると直前へ戻る。テキスト入力ウィジェット focus 中は grabFocus=false でもキー/テキストが届く(focus_consumes_text フォールバック)。
- **ホストホットキー `Dialog.registerHotKey(key, shift=0, duringTextInput=false)`** / `unregisterHotKey` / `clearHotKeys`: 登録キー(VK_PAD*・VK_RBUTTON 等マウスも同じ空間)はパネルへ渡らず `Window.onKeyDown/onMouseDown` へ直行(バイパス方式・専用イベント無し)。テキスト入力中は既定抑止(`duringTextInput=true` で有効)。モーダル中は無効。ESC/PgUp/PgDn 等「シェルが必ず受けたいキー」の確保に使う(実例=demolib DemoShell)。
- `input`(top-level)で矢印/パッドナビ(`arrow_focus_nav` / `dpad_mode` / `shortcuts`〔key/pad→id〕/ `pad_bindings`)を設定。既定 bind: A=Enter / B=Esc / X=Shift+Tab / Y=Tab / D-Pad=矢印。`"bindings": [{key|pad|mouse|wheel, action}]` で named-action を差替(`"none"`=消費して無効化、`"passthrough"`=消費せずホストへ素通し=常駐オーバレイが「この入力は下のゲームのもの」と宣言する用)。pad のフェイスボタンは刻印(`"a"`/`"b"`/`"x"`/`"y"`)と位置(`"face_south"`/`"face_east"`/`"face_west"`/`"face_north"`)の 2 系統で、1 押下で両方届く。表示側 `pad_icon` の name も同 2 系統を持つので割り当てと表示は同じ基準で組にする(任天堂系は X/Y の位置が Xbox と逆)。
- **フォーカス無しから方向キーで入る位置**: `input.arrow_focus_enter` = `"first"`(既定・収集順の先頭)/ `"directional"`(押した方向の端。右キーなら一番右)。`initial_focus` を置かない確認ダイアログ向け。
- 複数 Dialog の ownership: `close()` は**自分のインスタンスだけ**閉じる(`IsHandlerActive(this)` ゲート)。ブロッキング pump も自分の handler で終了判定。

---

## 7. ハマりどころ (memory 由来・重要)
- **DrawDevice 登録タイミング**: 起動直後(初回フレーム前)は overlay renderer 未登録で **`showJson` が false を返す**ことがある。初回表示は `Window.onContinuousHandler` 等へ遅延し、**成功するまでリトライ**する(`data/demolib` 参照)。[[reference_elements_dialog_drawdevice_timing]]
- **GL DrawDevice 上で出ない**: 提示中デバイスへ host 解決が追従していないと GL 画面上でパネルが出ない/操作不可。エンジン修正済だが、デモ側の「パネル再試行が自壊(shellClosePanel が pending を消す)」に注意。[[reference_elements_on_gl_drawdevice]]
- **サイズ**: `size` は**上限**でfit-to-content。全画面化はできない(BeginScreen 実装のきめうち有り)。size の peek が widget "size" 属性に誤爆する既知点あり。[[reference_elements_overlay_dialog_sizing]]
- **フォーカス奪取 / 共通ホットキー**: ✅解決済(2026-08-11)。操作パネルは `showJson(json, true, false)`+ホスト必須キーを `Dialog.registerHotKey` で確保(§6)。旧回避策の grabFocus=false は表示専用 HUD 用。[[project_elements_global_shortcut]]
- **サブクラスは `super.Dialog()` 必須**。`showFile` は autopath 未対応な場面あり(相対解決に注意)。
- **サブクラス内から static を触るときは `global.Dialog.xxx`**。素の `Dialog` は親クラス参照になり `Dialog.focusRing = false` 等が「メンバが見つかりません」で落ちる。
- **描画が重いと感じたら**まず `Dialog.renderStats` の差分を見る(`renderCount` がアイドルで増えていないかも)。`data/elements_bench` に更新パターン別の計測画面がある。overlay 描画の支配項はテキストのラスタライズで、同内容のテキストは自動でビットマップキャッシュされる(毎フレーム内容が変わる HUD カウンタは意図的に載らない)。
- **case-name 規約**: 共有/公開リポ(krkrz_dev/elements)に**案件固有名を書かない**。elements リポのコメント等はホストを「SDL を使うホストアプリ」等の汎用表現で。[[feedback_elements_repo_project_agnostic]] [[feedback_no_case_names_in_shared_repo]]

---

## 8. 動作検証 (Agent / REPL)
GUI は `krkrz-repl` skill のファイルチャネル + Agent API で駆動・目視できる:
- `Agent.dialogs()` — アクティブダイアログ配列(index/modal/active/screen/rect)。
- `Agent.dialogClick(i, id)` — **id 指定でボタン起動**(座標不要・確実)。`Agent.click(x,y)` は座標。
- `Agent.text(str)` — アクティブダイアログへテキスト入力(input_box)。
- `Agent.captureScreen(path)` — overlay 込み実画面 PNG(次フレーム)。→ Read で目視。
- ドットコマンド: `.dlg` / `.dlgclose` / `.click X Y` / `.cap`。
- 検証時の注意: REPL eval は式評価。永続変数は `global.x = ...`。多重 primary layer は不可(2枚目以降は `new Layer(win, primary)`)。詳細は skill `krkrz-repl`。

---

## 9. 実装場所 (深掘り時)
- TJS `Dialog` バインド: `common/visual/elements/DialogIntf.cpp`(showJson/showDict/showFlow/startFlow/close/onAction/onClose/setVar/registerFont/`active`/`defaultFontFamily`/`language`/`focusRing`/`renderCache`/`partialRedraw`/`renderScale`/`renderStats` 等)。
- マネージャ: `common/visual/elements/`(`tTVPElementsDialogManager` = z-order インスタンスリスト)。
- レンダラ提供口: `iTVPDialogRenderer`/`iTVPDialogRendererHost`(tp_stub 公開)。SDL=`SDLDialogRenderer` / OGL=`OGLDialogRenderer` / WINVER=`D3D11DialogRenderer` / 独立窓=`WinElementsModalRunner`。
- JSON→UI: elements_modal(`json_layout.cpp` / `navigator` / `overlay_session`)。プラグイン向け C ABI: `tp_dialog_service.h`。
- 関連 doc: `doc/Gamepad.md`(pad↔key)、`doc/D3D11Migration.md`(DestRect)、`external/elements/external/elements_modal/README.md`。

## 関連 skill
- `tjs2`(TJS 言語)/ `krkrz`(本体クラス API)/ `krkrz-repl`(REPL・Agent 駆動・captureScreen)。
