# Elements 要修正事項 (ホスト案件からのフィードバック)

Elements (`src/core/external/elements` = wamsoft/elements、その中の
`external/elements_modal`) に対して、ホスト側案件で実際に踏んだ不具合・改善要望を
溜めておくファイル。Elements 側の作業時間が取れたときにまとめて対応し、対応後は
`src/core` の submodule bump → 各案件へ展開する。

対応したら項目に ✅ と対応コミットを書き、消さずに残す (再発防止の記録)。

---

## 1. 複数行テキストがレイアウトで壊れる (優先度: 高) — ✅ 対応済み

> **2026-08-15 対応** (elements `develop`): 1-a は `default_label_styler` の
> `limits` / `draw` を改行対応にして解決。 1-b は `block_text_box::limits` の実装
> (elements `fb473a83`) で既に解決済みだったことを実機で確認。 1-c は仕様どおりで
> README に記載済み。 1-d は 1-a の解決により lint 不要。 詳細は各項の末尾を参照。

報告元: rpgsys (吉里吉里Z + threepp の RPG テンプレート) のメインメニュー。
2026-08-14 に実機調査。詳細メモ = `D:\work\kirikiri\krkrz_rpgsys\docs\elements-feedback-multiline.md`。

環境: krkrz SDL3 ビルド (2026-08-13 ビルド、glyphware 統合後) + `ElementsDialog.showDict`。
**glyphware は無関係** (1 行/矩形テキストの整形・描画のみを担い、ウィジェットの
高さ = limits には関与しない)。原因はレイアウト層。

### 1-a. `label` に改行入りテキストを渡すと後続ウィジェットが重なる

```jsonc
{ "content": { "type": "vtile", "children": [
    { "type": "label", "text": "一行目\n二行目\n三行目" },
    { "type": "button", "id": "b1", "text": "ボタン1" } ] } }
```

- **描画は 3 行ぶん出るのに、レイアウトが確保する高さは 1 行分**。
  次の子 (ボタン) が 2〜3 行目に重なる
- vtile の子が増えるほど崩れが累積し、実アプリでは「タイトルもボタン文字も見えない、
  枠だけの謎の画面」になる (原因特定に時間がかかった。他案件では複数行 label を
  使った例がなく、これまで踏まれていないと思われる)
- cycfi の `label` は元々 1 行ものなので仕様どおりとも言えるが、**無警告で壊れる**のが問題

対応候補 (`src/json_layout.cpp` `LayoutBuilder::build_label` 付近, 現行 L1470):
1. `text` に `\n` が含まれていたら、行ごとの label を縦に積んだ要素へ自動展開する
   (後方互換。既存 JSON がそのまま直る) — **推奨**
2. 最低限 `em_logf` で「複数行 label は text_area/text_box を使うこと」と警告
3. README のスキーマ表に「label は 1 行専用」と明記

**✅ 採った対応 (2026-08-15)**: 上記いずれでもなく、**`default_label_styler` 自体を
改行対応にした** (`lib/src/element/label.cpp`)。 描画側はもともと 3 行出ていて
`limits` だけが 1 行分を返していたのが原因だったため、

- `limits`: 改行で分割して「幅 = 最長行 / 高さ = 行高 x 行数」を返す
- `draw`: 行ごとに `fill_text` し、 縦アラインはブロック全体に適用

とした。 JSON 側の自動展開ではないので **`text_var` / `text_id` の動的テキストでも
そのまま効く** (ただし行数が変わる差し替えは、 次に親がレイアウトし直すまで高さが
追従しない旨を README に明記)。 実機確認: 3 行 label + button 2 個の vtile で
重なりが解消。

### 1-b. `text_area` / `text_box` が縦の内容高さを返さない (複数行の受け皿がない)

1-a の正しい代替であるはずの `text_area` が、`vtile` の子に置くと**何も表示されない**。

```jsonc
{ "type": "vtile", "children": [
    { "type": "text_area", "text": "一行目\n二行目\n三行目" },
    { "type": "button", "id": "b1", "text": "ボタン1" } ] }
// → ダイアログ実サイズ 132x180、text_area の領域は 0 で不可視
```

`hsize`(幅 300) + `vsize`(高さ 96) で囲んでも同じ (実サイズ 360x26、text_area は不可視)。

- 「与えられた矩形へ流し込む」用途 (字幕・セリフ窓) の設計なのは理解できるが、
  **`vsize` 指定すら効かない**のは想定外に見える
- 結果として fit-to-content なダイアログに複数行テキストを置く正攻法が現状ない

対応候補 (`build_text_area` L1946 / `build_text_box` L1890、根本は cycfi 側の
static_text_box の limits):
1. 与えられた幅での折返し結果の高さを縦 limits に返す
2. 少なくとも `vsize` で囲んだときは確実にその高さで描画されるようにする
3. 幅 0 のまま構築されたら警告ログ (静かに消えるのが一番つらい)

**✅ 解決済み (報告時点より新しい elements で修正済)**: `block_text_box::limits`
(elements `fb473a83` 「矩形テキスト widget text_area を追加」) が
「幅 = 直近レイアウト幅での折返し結果 (最小 200px) / 高さ = 折返し結果の高さ」を
返すようになっており、 2026-08-15 に実機で再確認したところ **vtile の子に直接置いた
`text_area` は 3 行ぶんの高さを確保し、 後続の button と重ならない**。
報告は 2026-08-13 ビルドでのものだったため、 その後の修正で解消していた。

### 1-c. (確認事項) dialog の `size` は「固定」ではなく「上限」?

`"size": [320, 220]` でも内容が小さいと実サイズは内容ぶん (例 104x42) に縮み、
内容が大きいときは指定値まで伸びる。仕様ならスキーマ表に明記してほしい。

**✅ 仕様どおり・記載済み**: `elements_modal/README.md` の「トップレベル」表に
`size` = 「推奨論理サイズ (run_modal は上限としてのみ使用、 fit-to-content で実サイズが
決まる)」と明記されている。 固定サイズにしたい場合は content 側を `hsize` / `vsize` で
括る。

### 1-d. elements_console (EUI DSL / uitool) 側

同じ落とし穴を DSL でも踏むので、lint (label の text に改行 → 警告して text_area を
勧める) と README 注記があると良い。

**✅ lint は不要になった (2026-08-15)**: 1-a の対応で `label` が改行をそのまま正しく
扱えるようになったため、警告して `text_area` へ誘導する必要がなくなった。README には
「label は明示した改行でのみ改行し、自動折返しはしない (折返しが要るなら `text_area` /
`text_box`)」を追記済み。

### ホスト側の現状回避策 (対応後に外せる)

rpgsys は**複数行テキストを行ごとの label に分解して vtile へ積む**回避策を入れた
(`data/rpglib/menu.tjs` の `addLines` / `setLineVars` / `lineVars`)。
reactive 更新のため `text_var` も行ごと (`status0`, `status1`, ...)。

**2026-08-15 時点**: Elements 側 (1-a) は解決したので、この回避策は外せる状態。
**rpgsys 側の削除と動作調整は rpgsys リポで別途対応する** (本リポの作業範囲外)。
外す際の注意として、`label` は明示した改行文字でしか改行しない (自動折返しはしない)
ので、幅で折り返したい箇所は `text_area` を使うこと。 また `text_var` で**行数が
変わる**差し替えをすると、次に親がレイアウトし直すまで高さが追従しない。

---

## 2. input_box のキャレット (カーソル) 位置がずれる (優先度: 中) — ✅ 対応済み

> **2026-08-24 対応** (elements: font.cpp/hpp + glyph_layout_gw.cpp): §4 修正後も
> 「日本語の文字幅が計測に反映されない」ずれが残存し、原因を特定。**描画**
> (canvas fill_text) はホストのフォントエンジンが families 列 (Roboto → Noto Sans
> JP → …) でグリフ単位フォールバックするのに対し、**計測** (glyph_layout_gw) は
> 先頭 family の単一 face で shapeRun していたため、日本語がラテン face の
> .notdef advance で測られていた。修正 = font に families 残りの解決ファイル
> (fallback_files) を保持し、計測時に glyphIndex でコードポイントごとに face を
> フォールバック選択 → face 単位のランに分割して shapeRun し位置を連結。検証 =
> ebox に「漢字あいABC」注入でキャレットが末尾に正着 + 「字|あ」間クリック後の
> 挿入が「漢字XあいABC」になることを確認 (クリック位置→挿入位置がピクセル対応)。

報告: 2026-08-24、softkey_ime デモの Elements 入力欄 (input_box) で、テキスト入力時の
キャレット表示位置が実際の挿入位置とずれて見える。**以前からの既知バグ** (今回の
onTextInput 移行とは無関係、それ以前から発生)。

環境: krkrz SDL3 / WINVER 両ビルドの overlay ダイアログ (`ElementsDialog.showDict` 系 +
`input_box`)。glyphware 統合後のビルドで確認。

原因候補 (未調査): cycfi elements の `basic_input_box` はキャレット x 座標を自前の
テキスト計測で求めるが、実描画は krkrz 側 backend (glyphware) が行うため、
**計測と描画で字幅の計算系が異なる**とずれる (プロポーショナル/日本語で顕著になる
はず)。elements_modal のテキスト計測 seam と描画 backend の字幅を一致させる必要が
ありそう。

再現: softkey_ime デモ → パネルの「Elements 入力欄」に日本語/ASCII 混在テキストを
入力してキャレット位置を目視。

> **2026-08-24 注記**: §4 (マウス反応位置ずれ) の修正により「クリック位置 → キャレット
> 挿入位置」の対応も是正された。§2 として見えていたずれが §4 と同一原因だった可能性が
> 高い。なお計測系は 2026-08-10 の glyphware 一本化 (bc46358c) で描画と統一済みで、
> 当時「入力欄キャレット表示正常」を実機確認している。§4 修正後も文字とキャレットの
> 描画位置そのものがずれるなら本項を再オープンする (要再検証)。

---

## 3. input_box にプログラム的フォーカスが効かない (優先度: 中) — ✅ 対応済み (2026-09-02)

**原因**: `view::focus(element_ptr)` の `descend_set_focus` はターゲット**まで**の
composite に focus index を張るが、ターゲット**の内側**は張らない。input_box は
`layer(margin(scroller(hold(basic_input_box))))` の包みなので、layer composite の
`_focus` / `_saved_focus` が両方 -1 のまま `begin_focus(restore_previous)` が
そこで return し、編集フォーカスに届かなかった (クリックすると `_saved_focus` が
入るので以後は効く = 「一度クリックすれば入る」の正体)。

**対応**: `descend_set_focus` がターゲットに到達したら、その内側も
`wants_focus()` の先頭の葉まで focus index を張る (`descend_focus_first`)。
`initial_focus` / `focus_by_id` / `Agent.dialogFocus` すべて同根で解決。
あわせて **`ElementsDialog.focus(id)`** (instance 版の focus_by_id) を追加 —
画面の組み替え (at_var の park/unpark) の後に入力先を移せる。
既定値入りの input_box は **build 時に全選択**にした (initial_focus で
そのまま打つと置き換え。OS の入力ダイアログと同じ挙動)。
ホスト案件の名前入力画面で実機確認 (開いた直後に打てる / 2 段目切替も
クリック不要)。

報告: 2026-08-24。overlay モーダルの `"input_box"` に `"initial_focus": true` を
指定しても、開いた直後の打鍵が入力欄に入らない (クリックすれば入る)。同根で
`focus_by_id` / `Agent.dialogFocus(i, id)` も input_box には効かない
(`Agent.dialogs()` の focused が "" のまま)。

確認手順: showModalJson で input_box (initial_focus:true) を開き、クリックせずに
Agent.text → 入力欄に入らない。クリック後の Agent.text は入る。

実装状況: json_layout の `note_initial_focus` は `ce::input_box()` の外側
composite を登録し、overlay_session::start が `view->focus(element_ptr)`
(asio::post デファード) を呼んでいる。ボタンにはフォーカスリングが乗るケースが
あるので view->focus 自体は動いているが、**input_box の編集フォーカス (キャレット
+ text 受理) に変換されていない**。cycfi の composite focus 連鎖と input_box
proxy 階層の対応付けを調査する必要あり。

影響: System.inputString overlay (SDL) は開いた直後にそのまま打鍵できず、
一度クリックが必要。Steam Deck では focus 駆動 OSK が「開いただけでは出ない」
ことにもつながる (クリック/タップで focus すれば出る)。

**2026-08-28 追記 (優先度を上げたい)**: ホスト案件の「名前入力」画面
(全画面の絵 + 入力欄 1 個) で実際に踏んだ。 `"initial_focus": true` を書いても
**開いた直後に打てず、入力欄をクリックしてもらう必要がある**。 画面には入力欄が
1 個しか無いので、 «クリックしないと打てない» のが素の作りとして出てしまう。
`Agent.text` での実機検証も、 クリックを挟まないと入らない (現象の確認に使える)。

---

## 4. overlay ダイアログのマウス反応位置が表示とずれる (優先度: 中) — ✅ 対応済み

> **2026-08-24 対応** (ElementsDialogManager.cpp): 原因は overlay_session の配置契約の
> 取り違え。session は「呼出側が out_rect の位置にテクスチャを貼る」契約でコンテンツを
> buffer (canvas) 原点に描き、アンカー配置済みの last_rect を返す。on_mouse は
> last_rect を引いて view 座標へ戻す。一方 manager は out_rect を無視して buffer 全体を
> 自前配置していたため、**「描画 = canvas 原点 / ヒット判定 = アンカー位置」の不一致**が
> 生じ、authored "size" > 内容実寸 かつ 非中央 "align" の画面 (デモパネル等) でアンカー
> オフセットぶんマウス反応がずれていた (自動フィット中央の画面は offset 0 で露見せず)。
> 修正 = ①render_to_buffer へ渡す surface を 0,0 にして session 内部アンカーを無効化
> (last_rect = (0,0,実寸) → 入力と描画が一致)、②manager の placement をコンテンツ実寸
> 基準に変更 (bottom/right 寄せが本当に端へ付くようになる = 従来は内容が authored より
> 小さいぶん手前に浮いていた)。onAction カウンタ方式のヒットプローブで、視覚位置と
> 反応領域のピクセル一致を確認済み。

報告: 2026-08-24。overlay ダイアログ (softkey_ime デモのパネル等) で、ウィジェットの
見た目の位置とマウス/タッチの反応位置がずれる。**PC (SDL Windows) と Steam Deck の
両方で再現** = プラットフォーム非依存。報告者の見立て: present fit (拡縮・配置) の
調整とマウス座標変換の不整合。

関連コード: ElementsDialogManager.cpp の「マウス座標 → session へ渡す座標」変換
(TranslateWindowToDrawArea で DestRect 原点を引いた描画領域基準 → 原点足し戻し →
present fit の倍率・配置オフセットの逆変換)。描画側の present 変換
(present_scale/off) と入力側の逆変換のどちらかが片方だけ更新されている、または
基準 (window client / DestRect / surface) の取り違えを疑う。

§2 (input_box のキャレット位置ずれ) と原因が同じ可能性あり (両方とも「計測系と
表示系の座標変換の不一致」)。§2/§4 はまとめて調査するのが良い。

再現: softkey_ime デモのパネルで、ボタンやピッカーの端をクリックして反応位置と
見た目の対応を観察。

---

## 5. 画面資材そのまま移植で出た拡張要望 — ✅ 対応済み (5-7 のみ見送り)

> **2026-08-29 対応**: 5-1 は krkrz 本体 (`src/core` fcae740b)、 5-2 / 5-3 / 5-4 /
> 5-5 は elements (`365bc122` / `a2a36319` / `06c39b99` / `bd7b607d`)、 5-6 は
> ドキュメントのみ。 5-7 は elements 側の課題ではないため見送り (engine の
> フォントサービス側へ集約)。 各項の末尾に採った対応を書いた。
> SDL3 x64 で実機確認済み、 WINVER (x64-windows-win) もビルド確認済み。

報告: 2026-08-28。 PSD 資材を絶対配置 + atlas でそのまま移植するホスト案件から。
題材は「8 行の窓 + スクロールバーの一覧を PSD 資材そのままで組む」画面
(フォント選択のプルダウン)。

**1 巡目 (同日に対応済み)**: `label` の `color_var` / `vars_on_hover` /
`atlas_image` の `native` / `scroller` の `pos_var` 双方向 / `font_families()` /
`drag_at_var` + `drag_events` (`ElementsDialog.onDrag`) / 一覧の «窓»
(`index` + `index_offset_var` / `text_list_var`)。 **これで逃げの実装は全部畳めた**。
以下は **その口を実際に使って組んでみて出たもの** = «片側だけだったもの» と
«使って初めて分かった不足»。

### 5-1. 変数をホストから読めない / 変わったことを知れない (優先度: 高) — ✅ 対応済み

`vars_on_hover` / `vars_on_focus` の書き込み先は elements の変数で、 ホストからは
**書けるだけ** (`ElementsDialog.setVar`)。 読み出しも変化通知も無い。

そのため «**絵はホスト側のレイヤ、 当たり判定だけ elements**» という構成
(大きすぎて atlas に積めない一枚絵を並べる一覧など) では **hover を活かせない**。
画面 JSON の中で閉じる用途 (色替え・出し分け) は足りているが、 ホスト側の処理へ
繋がらない。 実例: 進展度で絵が丸ごと変わる一覧画面で、 カーソルを乗せたときの
ハイライト差し替えが今も繋げないまま (ハイライト素材は用意済み)。

**elements 側にはもう口がある** — `overlay_session::get_var()` と
`set_var_watcher()` (`include/elements_modal/modal.h`)。 **ホスト側のバインドを
生やすだけ**で済むはず:

- `tTJSNI_Dialog` に `SetVar` しか無い (`common/visual/elements/DialogIntf.cpp`)。
  `getVar(name)` を足す
- 変化通知は `set_var_watcher` を `ElementsDialog.onVar(name, value)` へ流すか、
  画面 JSON の `"watch_vars": [...]` で対象を絞って通知する

**✅ 採った対応 (2026-08-29、 `src/core` fcae740b)**: ホスト側バインドを 4 つ追加。

- `ElementsDialog.getVar(name)` … 1 件読出 (未知 / 非アクティブは void)
- `ElementsDialog.listVars()` … 変数一覧 (`name` / `value` / `usedBy` = `%[id, kind]`)
- `ElementsDialog.onVar(name, value)` … 変化通知
- `ElementsDialog.watchVars` … 通知対象を絞る (`"*"` / 名前配列 / `[]` / void)

観測は **opt-in**: `BeginScreen` が `WantsVarNotify()` を問い合わせ、
「`watchVars` が明示されていればそれに従う / 未指定なら **TJS 側に `onVar` が
あるときだけ全変数**」で決める (`onVar` に native の no-op 既定を置かないのは
この判定のため)。 通知は elements のレンダリング中に発火するので即時配送せず
既存の `pending_actions` キューへ積み、 同名は最新 1 件へ畳む (1 フレーム遅延。
«いまの値» は `getVar`)。 対象は「絞らなければ全変数」なので、
`vars_on_hover` / スライダ / ドラッグ座標 / 一覧の先頭位置も全部拾える。

#### 使ってみて分かったこと (2026-09-01。 ホスト案件で「絵はホスト / 当たりは elements」を通した)

**通った**。 進展度で絵が丸ごと変わる一覧画面 (上に書いた実例) のハイライトが
繋がった: 当たり判定に `vars_on_hover` で `<id>_hv` を書かせ、 `onVar` で
拾ってホスト側のレイヤの絵を差し替える。 実測で絵の差分 196,156px、
カーソルを離すと差分 0px (元の絵へ完全復帰)。

実測できた仕様 (ドキュメントに書いておくと助かる):

- **`vars_on_hover` はカーソルが離れると元の値へ戻す**。 「離脱時に戻す」ための
  背景当たり判定などをホスト側で作る必要は無い

残っている使い勝手の問題 (**優先度: 低**):

- **`watchVars` の既定値の意味**がドキュメントから読み取れない
  (`"*"` / 名前配列 / `[]` は書いてあるが `void` = 既定が何をするか)。
  実装は「`watchVars` が明示されていればそれに従う / 未指定なら **TJS 側に
  `onVar` があるときだけ全変数**」なので、 **そう書いてあると迷わない**。
  ここは engine 側ではなくドキュメントの話
- **中継は KAG (KAGEX) 側の話**として整理したほうが良い。 `ElementsDialog` を
  ラップしているダイアログ実装のクラスに `onVar` を書くと
  `WantsVarNotify()` が全画面で true になってしまうので、 そのままでは
  置けない。 **`onVar` の中継と同時に `watchVars` の既定を `[]` (止める)
  にしておけば**、 «要る画面だけ opt-in» を保ったまま
  「ドライバに `onVar` を書くだけ」にできる。 いまホスト側は
  **インスタンスへ直に生やして**回避している (TJS はクラスへメソッドを
  足しても既にあるインスタンスには届かない):

  ```tjs
  dlg.sysScreenOwner = this;
  dlg.onVar = function(name, value) { ... } incontextof dlg;
  dlg.watchVars = varWatchList;   // 既定は [] にしてある
  ```

  elements / krkrz core の変更は要らない。 **KAG 側のラッパを整えるときの
  メモ**として残す

### 5-2. `drag_at_var` は「1 変数 = 1 矩形」なので複数枚の部品に使えない — ✅ 対応済み

つまみを 上キャップ + 伸びる胴 + 下キャップ の 3 枚で描くと、 1 本の変数では
どれか 1 枚しか動かない。 結局 `drag_events` + ホスト側の計算になった
(それ自体は問題なく動く)。 案は 2 つ:

- `at_var` を挿す側に **差分**を書けるようにする (`at_var_offset: [dx,dy,dw,dh]`)。
  1 変数で 9-slice が組める
- `atlas_slider` の `thumb` に 9-slice を許す。 今の `thumb` は単一矩形なので
  (`json_layout.cpp` の `build_atlas_slider`)、 キャップ付きのつまみ資材が
  そのままでは載らない

**✅ 採った対応 (2026-08-29、 elements `365bc122`)**: **両方**入れた。

- canvas の子に `"at_var_offset": [dx, dy, dw, dh]` — 同じ `at_var` を複数枚に
  挿し、 それぞれ違う差分を書けば 1 変数で 9-slice が組める (dw/dh はサイズ加算)
- `atlas_slider` の `"thumb"` をオブジェクトでも受ける
  (`{ "rect": …, "insets": [l,t,r,b], "size": [w,h] }`) — `atlas_nine` を
  `fixed_size` で固定して «キャップを潰さず胴だけ伸ばす» つまみになる

あわせて、 位置が変わる要素の部分再描画ダーティを精密化した
(`set_child_rect_notifier` で «移動前 / 移動後» の 2 矩形を渡す。 従来は範囲を
出せず全面再描画へフォールバックしていた)。

### 5-3. スクロールバーは結局「毎回組む」ことになる — ✅ 対応済み

`pos_var` の双方向化は **本文が `scroller` に載っている**ときの解。 行を自前で
並べる一覧 (5-4 の «窓») では 溝・つまみ・ページ送り・ホイール を毎回手で組む。
資材が «溝 + キャップ付きつまみ × 4 状態» で来るのはよくある形なので、
**`atlas_scrollbar`** 相当があると手組みが丸ごと消える:

`vertical` / 溝の矩形 / つまみ 9-slice / `value_var` か `index_offset_var` へ直結 /
溝クリックでページ送り / ホイール / つまみのドラッグ。

**✅ 採った対応 (2026-08-29、 elements `a2a36319`)**: 挙げられた要件のまま
`atlas_scrollbar` を新設した。 `index_offset_var` (+ `count_var` / `visible`) に
直結すると **つまみの長さが «見えている行数 ÷ 総件数» に比例**し、
`value_var` なら 0..1 (scroller の `pos_var` と同じ変数で連動)。
`page` (既定 = visible) / `wheel_step` / `thumb_min` を持ち、 つまみは
atlas_slider と同じ 2 形式 (単一矩形 / 9-slice)。

### 5-4. 一覧の «窓» は «文字» までで、 行の当たり・hover・色は自前 — ✅ 対応済み

実際に組むと 行あたり **label 1 + 当たり判定ボタン 1**、 変数は
**文字・色・当たりの位置** の 3 本になり、 «件数が足りない行は当たりごと画面外へ
逃がす» 後始末も要る。 «行が label 1 個で済まない一覧を組んでから検討» という
判断だったので、 要件だけ置いておく:

**行数 / 先頭 index / 行の矩形 (ピッチ) / 行クリックで «行 index» が payload で
返る / hover と選択の色 / 件数不足の行は当たりごと消える**。
ここまで持ってくれると、 一覧は «データを流し込むだけ» になる。

**✅ 採った対応 (2026-08-29、 elements `06c39b99`)**: 挙げられた要件をそのまま
満たす `list` (別名 `row_list`) を新設。 **行テンプレートを行数ぶん複製**する方式
(専用 list widget ではなく、 行の中身は任意のウィジェット木) にしたので、
既存の «窓» と地続きで資材の自由度も落ちない。

- 文字列値の `#index` を行番号へ展開 (`"id": "row#index"` /
  `"visible_var": "rhov#index"`)
- `text_list_var` 等を持つ要素には `"index"` と `"index_offset_var"` を自動で挿す
  (= テンプレートに 1 行書くだけで «窓» になる)
- 行の中の widget が先にクリックを受け、 誰も受けなければ**行クリック**として
  `onAction(id, データ index)`。 モーダルなら `result.values[id]` にも載る
- `count` / `count_var` で **データが無い行は描画も当たりも消える**
- hover / 選択は行ごとフラグ (`row_hover_var` / `row_select_var` →
  `visible_var` で受ける) と、 ホスト向けの `hover_var` / `select_var`
  (5-1 の `onVar` で拾って «絵はホスト側のレイヤ» を差し替える) の両方

### 5-5. ドラッグ中に «掴んだ widget» の矩形を動かしたときの挙動が未定義 — ✅ 対応済み (仕様として明記)

つまみを追従させるにはドラッグ中に矩形を書き換えたくなるが、 掴み位置がどう
なるか分からないので **掴んでいる間は動かさない**実装で回避した。 仕様として
一行あると安心 (「ドラッグ中の `at_var` 変更は掴み位置を維持する」等)。

**✅ 採った対応 (2026-08-29、 elements `bd7b607d`、 ドキュメントのみ)**: 実装を
読んだところ **既に «掴み位置は維持される»**。 tracker は掴んだ瞬間の `at_var`
値を起点として控え、 以後は移動量を足した値を毎フレーム書き直すので、
ドラッグ中のホスト書込は次の move (と離したときの end) で上書きされる。
ホスト書込が位置として効くのは «掴んでいない間» で、 次に掴んだときの起点として
読み直される。 この挙動を elements_modal README の「掴んで動かす」節へ明記した。

### 5-6. `bindings` の named action の通知形がドキュメントに無い — ✅ 対応済み

組込以外の action は `onAction` の **id が `"<action>"` で、 名前は payload** に入る
(`overlay_session` の `dispatch_action` → `external_cb("<action>", …)`)。
配布スキルの `references/ElementsDialog.md` にはあるが、
**`.claude/skills/elements/SKILL.md` と `doc/guide/ElementsDialog.md` には無い**。

id に自分で付けた名前が来ると思って書くと **その入力だけ黙って無反応**になり、
原因に気づきにくい (ホイールを `{"wheel":"up","action":"..."}` で付け替えたときに
踏んだ)。 ドキュメント追記だけで足りる。

**✅ 採った対応 (2026-08-29)**: `.claude/skills/elements/SKILL.md` に 1 項目、
`doc/guide/ElementsDialog.md` に「入力バインドと named action」節を追加した
(組込名は届かないこと / `id` は `"<action>"` 固定で名前は payload に入ること /
自分の名前が id に来ると思って書くと黙って無反応になること)。

### 5-8. `input_box` に最大長が無い (優先度: 中) — ✅ 対応済み (2026-09-02)

`basic_input_box` に `max_length` (Unicode codepoint 単位、 0 = 無制限) を
足し、 JSON は **`"max_chars"`** (別名 `"maxlength"`) で指定できるようにした。
満杯での打鍵は消費して無視 (選択があれば置き換えなので通す)、 paste は
codepoint 境界で収まる分だけ入る。 初期値 (`"text"`) はプログラム的投入
なので制限しない。 ホスト案件の名前入力 (全角 4 文字仕様) で実機確認。
クラスタ単位ではなく codepoint 単位 (結合文字は個別に数える) — 日本語の
名前入力用途では実質同じ。

ついでの「**プログラムから入力欄の中身を差し替える口も無い**」は**未対応のまま**:
初期値はビルド時の `"text"` だけなので、 «同じ画面で 2 つの既定を出し分ける»
には入力欄を 2 個置いて片方を画面外へ逃がすことになる。 `text_var` が
`input_box` にも効くと素直。 (ホストは 2 個 + park で回避済み、 急ぎでない)

### 5-7. OS にインストール済みのフォントは family 名から引けない — 見送り (engine 側の課題へ集約)

`font_families()` で **登録済み (同梱ぶん)** は取れるようになった。 残りは OS 側で、
`registerFont` がファイル経由 (`font::file()` が鍵) なので
«一覧の各行をそのフォントの書体で描く» はまだできない。

ホスト案件では «行はテーマの書体で名前だけ出す» と決めて回避した (OS のフォントを
行に出すたびに実ファイルを解決して登録するのは重い) ので **急ぎではない**。
やるならホスト側で family → ファイルを解決して `registerFont` する形が素直で、
elements 側は今のままでよい。

**判断 (2026-08-29): 見送り**。 elements 側の課題ではなく、 engine のフォント
サービス側で「システムフォント全列挙 (`allowSystem`) の検索統合」が要る話で、
これは既に `src/core/doc/FontEngine.md` の将来項目として登録済み。 急ぎでない
ことも報告どおりなので、 本ファイルではクローズし engine 側へ集約する。

---

## 6. ホストの描画中に elements のテキストだけ出ない — ✅ 対応済み

> **2026-09-01 対応** (`src/core` 3310a2d0 = `StoragesResourceLoader.cpp`)。
> 「ホストの描画中」は症状の条件ではなかった。 真の条件は
> **実行中にテーマの書体の並びを入れ直すこと**で、 ホスト案件が
> 「タイトルの初期化」と「言語ごとの適用」の 2 か所で
> `defaultFontFamily` を入れていたため、 タイトルで 1 回目・ゲームに
> 入る前後で 2 回目が走り、 結果として「タイトルからは出るのに
> 再生中は出ない」という見え方になっていた。

**原因**: theme の `font_descr` は families を **`string_view` で
「所有せずに」持つ**仕様なのに、 engine 側がその実体を **static な
`std::string` 1 本**で使い回していた。 入れ直すたびに旧バッファが解放され、
それを見ている `font_descr` のコピー (widget が持っている分など) が宙を指し、
フォントが引けず文字が描かれなくなる。 **`font` を明示している widget は
無事**なので気付きにくい。

`std::string::clear()` はバッファを解放しないので、 **入れ直した並びが
前より長くなって再確保が起きた回でだけ露見する** = 未定義動作。 ビルドや
呼び出し順で出方が変わり、 「特定の状況でだけ出る不可解な症状」に見えていた
(2026-08-28 の報告時に「ホストの描画中」と条件付けしてしまったのはこのため。
同じホストの別ビルドでは無条件に出た)。

**対応**: 一度テーマへ渡した文字列は解放せずに貯める (`ThemeFamiliesPool`)。
増えるのは入れ直した回数ぶんの数十バイトだけ。

**確認** (2026-09-01、 ホスト案件の実機で `-replfile` + `captureScreen`):

| 確かめたもの | 結果 |
|---|---|
| 書体の並びを 長 → 短 → 長 と 3 回入れ直してから画面を開く | 項目名・ボタン・`label` の `text_var`・`input_box` の既定値 全部出る |
| `list` + `label` の一覧 (9 行) | 全行出る |
| **ホストのシーン再生中**に開く (もとの報告の条件) | 出る |
| 一覧・回想・音楽・立ち絵の 5 画面 | 文字・絵とも出る。 例外 0 |

**教訓**: 「絵は出るのに文字だけ出ない」は **書体が引けていない**サイン。
`font` を明示した widget だけ無事なら、 theme の書体の並びを疑う。

---

## 7. 画面データ側で UI を完結させるための不足 (優先度: 高。 未着手)

報告: 2026-08-29。 複数のホスト案件がそれぞれ独自の UI フレームワークを書き始めて
いる状況を受けての方針転換。

**方針**: **UI の処理は画面データ側 (elements_modal + 画面 JSON) で完結させ、確認も
ホスト非依存のツール上で行う。ホスト (吉里吉里 / KAG) 側は「呼ぶ / 値を供給する /
アクションを実行する」だけにする**。 ホストを跨いだ展開と案件間の使い回しを考えると
この形が収まりが良い、という判断。

切り分けの原則は「**ゲームの状態に触るか**」。 画面遷移・タブ・一覧のスクロールと
選択・値の整形と出し分け・フォーカス・演出は画面データ側。 設定値やセーブデータの
実体、セーブ / ロードの実行、SE の実再生、ホストのダイアログ機構との調停はホスト側。

現状を実測したところ、**画面データ側に足りないものは多くない**。 一覧まわりは §5 の
`list` / `atlas_scrollbar` で埋まったので、残りは次の 4 点。

### 7-1. 画面をまたぐ変数が無い (優先度: 高)

言語と (同じ画面へ戻ったときの) フォーカス位置は遷移をまたいで保たれるが、
**変数は画面ごと**で、引き継ぎたい値はホストが持つ仕様 (elements_modal README
「画面をまたいで保たれるもの」)。 このためタブ切替や設定画面の一時値のたびに
ホストへ戻る必要があり、「画面データ側で完結」が崩れる。

→ **マニフェスト / セッション単位の共有変数スコープ**を足す。 画面ごとの変数と
共存させ、どちらに置くかを宣言できる形が要る。

### 7-2. 動的画像を実行時に差し替えられない (優先度: 高)

`image` + `mem://<name>` でホスト注入画像を出せるが、 **pixmap は build 時に一度
読む**ため、差し替えは画面を開き直す前提になっている (README の `image` の項)。
セーブ一覧をページ送りするとサムネイルが変わる、という**最も普通の画面が組めない**。

→ 変数で画像を差す口 (`image_var` 相当) と、 注入画像の差し替えが次フレームで
反映される経路。 `refresh_mem_image` + `invalidate` は既にあるので、 build 時に
焼いている pixmap 解決を遅延させるのが本体。

**2026-09-01 実測による訂正 (ホスト案件)**: 「差し替えは画面を開き直す前提」は
**言い過ぎ**だった。 実際は

- **一度 widget ができてしまえば、 `registerImage` し直すだけでその場で
  差し替わる**。 一覧のページ送りはこれで組めている (サムネイル 9 枚 x 2 画面)
- 本当の制約は **`show()` の前に登録が無いと widget ごと作られない**こと。
  ホストは「空きスロット用に透明な 1 枚を用意して必ず全数を埋める」回避を
  している

なので §7-2 の実害は「**無ければ空で作る**」が無いことに縮む (ダミー画像の
用意が要る)。 `image_var` があれば素直になるのは変わらないが、 **優先度は
高 → 中**に落として良い。

**ついでに**: elements の画像デコーダは **BMP を読めない** (PNG / JPEG /
WEBP は読める)。 ホストが BMP しか持っていない場面 (セーブサムネイル等) では
ホスト側で読み直して PNG へ焼く必要がある。 対応するかは要相談だが、
README に「読める形式」を明記しておくと踏まない。

### 7-3. 画面契約 (要求する変数 / 出るアクション) を束ねる形が無い (優先度: 中)

`ElementsDialog.listVars()` (§5-1 で追加) で「画面が読む変数」は機械的に取れるようになった。
出る側は widget id + named action で決まる。 これを**契約として束ねて外へ出す**と、

- ホスト非依存の確認ツールが、契約からスタブ値を流し込んで操作確認できる
- ホスト接続時に「画面が要求する変数を供給しているか」を照合できる
  (いまは繋ぎ忘れが黙って空表示になり、原因に気づきにくい)
- 画面ごとの「必要な変数 / 出るアクション」表を資料として生成できる

### 7-4. 標準ロールの語彙が決まっていない (優先度: 中)

config / save / load / backlog / title / yes-no は、どの案件でも**やることは同じ**なのに
変数名とアクション名が案件ごとにバラバラで、ホスト側の実装が毎回書き直しになっている。
既存案件の実装から抽出して語彙を決めれば、ホスト側は対応表だけになる。

> 各案件の現状比較と移行の段取りは、ホスト側 (KAG 側) の設計メモに置く。
> ここに書くのは**画面データ側に足りないもの**だけ。

---

## 8. overlay の出力先をホストのレイヤへ向けられるようにする — ✅ 対応済み

> **2026-09-01 対応** (`src/core` e2f05dbc / 06085168 / fbd51004 / 029c9413)。
> **`ElementsPanel`** を追加した (overlay とは別枠)。 TJS からは
> `new ElementsPanel(layer)` + `openFile` / `openJson` で、 イベント名と引数は
> `Dialog` と同じ。 詳細 = `src/core/doc/ElementsDialog.md`
> 「ホストのレイヤへ描く」。
>
> 実機で確認: 画面が出る / クリックで `onAction` が届く (**座標変換なし**) /
> hover で `onVar` が届く / **`piledCopy` に写る** / 手前のレイヤが覆う
> (z 順が効く) / 通常アルファと加算アルファの合成結果が一致 (差分 0px) /
> ホスト案件のタイトル画面の JSON をそのまま開ける / 例外 0。
>
> 副産物: 同じバッファをレイヤへ直接置いて比べたことで、 **overlay の提示が
> straight alpha でアルファを二重に掛けていた**のが判明し直した
> (fbd51004)。 半透明の画素だけが薄く出ていた (不透明な画素は影響を受けない
> ので気付きにくい)。 D3D11 / GL / SDL の 3 経路とも premultiplied 合成へ。
> **既存の画面の見た目が変わる** (半透明部分が濃くなる方向) ので、
> 袋文字の縁のように「暗く出ていたのを前提に調整した資材」は見え方が変わる。
>
> 初回に入れていないもの (要ると分かってから足す): キー / パッドの
> フォーカス調停 / navigator フローと遷移エフェクト / `close_on_click` の
> 自動 finish とモーダル結果 / 仮想キーボードと IME。


報告: 2026-09-01。 ホスト案件で「**uipsd で組んでいる画面 (メッセージ窓 /
バックログ) を elements に寄せて統一できないか**」を検討した結果、
**ここが分水嶺**になった。 単独では小粒に見える不具合が、 原因で束ねると
ほぼこの 1 点に集まる。

### 8-1. overlay はレイヤツリーの外にいて常に最前面

overlay は DrawDevice の `Show()` 終端で `PresentOverlay` されるので、
**ゲームのレイヤツリーのどこにも属さず、 常に最前面**。 帰結:

- **本文の上に窓の絵が被る**ので、 テキストを出す画面は elements で組めない
  (ホスト案件はメッセージ窓とバックログを uipsd = 吉里吉里のレイヤに残している)
- `piledCopy` に写らない。 **ホストのスクリーンショット機能に overlay が入らない**
  (実測: `kag.primaryLayer` を写すと overlay のパネルだけ抜ける)
- 表 / 裏のどちらでもないので **`[trans]` に乗らない**。 裏用を用意する手も無い
  ため、 画面遷移は elements 自身の `transitions` で別系統に組むことになる

### 8-2. overlay が下のレイヤの入力を食べる

overlay が出ている間、 その下の吉里吉里レイヤのボタンが押せない。 ホスト案件は
**「絵はホストのレイヤ / 当たり判定だけ elements の透明ボタン」**という構成で
逃げているが (`at_var` で追随させる)、 これは §5-1 の `onVar` が入って
ようやく成立した回避で、 素の作りとしては重い。

派生して踏んだもの:

- 当たり判定の無い `label` に `vars_on_hover` を付けると、 hover 用の proxy が
  下のボタンを塞ぐ (→ ホスト側は `vars_on_hover` をボタンに付ける規約にした)

### 案: `render_to_buffer` の書き込み先をホストのレイヤにする

**ほぼ配線だけで通せる見込みがある**。 いまの経路は

```
overlay_session::render_to_buffer(buf, w, h, ...)      ← ARGB8888 (LE=BGRA) を書くだけ
  ↑ buf は iTVPDialogRenderer::AcquireBuffer(layer, w, h) が返す CPU 連続バッファ
ReleaseBuffer(layer)        → テクスチャへアップロード
PresentOverlay(layer, ...)  → DrawDevice::Show() 終端で貼る (= 常に最前面)
```

で、 **`render_to_buffer` の書き込み先はもともと ARGB8888 の素の CPU バッファ**。
これは **吉里吉里の Layer のビットマップとまったく同じ画素形式**なので、
`AcquireBuffer` の代わりに **Layer 自身のバッファを渡す**だけで「elements の
画面が Layer の中身になる」。 貼り付け (`PresentOverlay`) は要らなくなり、
代わりに `Layer.update(dirty)` を呼ぶ。

得られるもの:

- **z 順がホストの自由**になる (本文の下・絵の上・任意の `absolute`)
- **表 / 裏の両方に置ける**ので `[trans]` にそのまま乗る。
  「表裏両属」は 2 枚作るだけになり、 特別扱いが要らない
- `piledCopy` / スクリーンショット / レイヤのトーンや不透明度が**そのまま効く**
- 入力は「**Layer 側で受けて座標変換して session へ投げる**」に変わるので、
  **8-2 が構造的に消える** (どのレイヤが入力を受けるかは吉里吉里の当たり判定が
  決める。 透明ボタンを敷く回避が不要になる)
- 常駐パネル (Layer) とモーダル (今の overlay) を**同じ画面 JSON で出し分け**られる

詰めるところ:

- **アルファの扱いは合っている見込み**。 elements は tvg canvas を
  `tvg::ColorSpace::ARGB8888` (= **premultiplied**。 straight は `ARGB8888S`)
  で target しているので (`lib/src/support/canvas.cpp`)、 吉里吉里側は
  **`type` を `ltAddAlpha` (additive alpha = premultiplied) にした Layer**
  にそのまま置ける。 変換は不要。 `ltAlpha` (straight) の Layer に置きたい
  場合だけ un-premultiply が要る (どちらを既定にするかは決めどころ)
- **駆動**。 毎フレーム tick して、 present の代わりに `Layer.update` を呼ぶ
  (部分再描画は `render_to_buffer_partial` の `out_updated_px` を
  そのまま更新矩形に使える)
- **サイズ**。 Layer のサイズ = buffer サイズ = 画面の logical サイズにして、
  拡縮は Layer 側 (`stretchCopy` / `Layer.setPos`) に任せるのが素直
- **入力の受け口**。 Layer の `onMouseDown` / `onMouseMove` / `onKeyDown` を
  session の `on_mouse_*` / `on_key` へ流す。 フォーカスやドラッグの状態は
  session が持っているので、 座標をそのまま渡すだけで足りる
- **TJS の口**。 今の overlay とは**別のクラス**にする (既定の overlay の
  挙動には一切触らない)

> 以下は 2026-09-01 に決めた。 上の段落は「案」として残す。

**この案件だけの話ではない**: 「elements で組んだパネルをゲームのレイヤ構成の
中に置きたい」は、 KAG のメッセージ窓 / ステータス表示 / マップ画面など、
どのホスト案件でも出る形。 §7 (画面データ側で UI を完結させる) とも噛み合う
(画面 JSON はそのままで、 **どこに出るか**だけホストが決められる)。

### 決まったこと (2026-09-01)

1. **座標変換は要らない**。 Layer のマウスハンドラへ来る座標は
   **Layer 左上原点に補正済み**。 `render_to_buffer` へ渡す `surface_w/h` を
   0 にすれば `out_rect = (0,0,コンテンツ実寸)` になり (manager が既に使って
   いる手)、 **Layer local 座標 = view local 座標**でそのまま
   `on_mouse_*` へ投げられる
2. **ダイアログ系とは独立に、 別枠で自前に処理する**。 下の「なぜ独立させるか」
3. **今の overlay を残したまま足す**。 出力先の抽象を先に切る形は取らない

### なぜ「ダイアログ系とは独立」が妥当か (内部構造の調査結果)

`tTVPElementsDialogManager::Impl::Instance` が持っているものを数えると、
**大半が「overlay として画面へ提示する」ための状態**で、 Layer に描く
パネルには意味が無い:

| Instance の状態 | Layer パネルでは |
|---|---|
| `modal` / `wants_focus` / `armed_vks` | **不要**。 入力の帰属は krkrz の当たり判定が決める |
| `present_scale` / `present_off_*` / `dest_offset_*` | **不要**。 拡縮は Layer 側 (`setPos` / `stretchCopy`) |
| `cache_*` (前回の present 引数一式 11 個) | **不要**。 提示は `Layer.update` |
| `last_rect` / `has_rect` / `cursor_inside` | **不要**。 ヒットテストは Layer |
| `nav` / `screen_jsons` / `trans_*` / `last_frame` | **要らない** (画面遷移は `[trans]` に任せる) |
| `session` / `handler` | **これだけ共通** |

さらに manager 側のプロセス全体の状態 — `IsModalActive()` (DrawDevice の
入力インターセプトのゲート) / `HasModalInstance()` (ウィンドウクローズ抑止) /
ホストホットキー表 / 仮想キーボード / `TakeLastModalResult` /
`DescribeInstances` (= `Agent.dialogs()`) — は **すべて「overlay が入力を
独占する」前提**の仕組み。 ここに Layer パネルを混ぜると

- パネルを出しただけでゲームの入力インターセプトが有効になる
- パネルがあるとウィンドウを閉じられなくなる
- `Agent.closeAllDialogs()` が常駐パネルまで畳む
- `Agent.dialogs()` の index がずれて既存の検証コードが壊れる

という「変な影響」が出る。 **`Impl::instances` には入れない**。

一方で **プロセス全体で共有すべきもの**はある: ThorVG / フォントの初期化
(`EnsureRuntimeInitialized`)、 テーマ (`defaultFontFamily` / `focusRing` /
pad テーマ)、 表示言語 (`SetLanguage`)、 `registerImage` の mem:// store。
これらは既に `StoragesResourceLoader` 側でプロセス全体なので、
**パネルは同じものを使い、 言語変更と `InvalidateOverlays` の fan-out 先に
パネルの registry を足すだけ**で足りる。

### 実装スケッチ (どういうクラスがどう生えるか)

**A. 共有部の切り出し** (既存 .cpp の匿名 namespace から出すだけ。 挙動不変)

| 新規 | 中身 | 出どころ |
|---|---|---|
| `ElementsInputMap.h` | `MouseButtonToElements` / `FlagsToElementsMods` / `RouteVk` / `MouseButtonToVk` | `ElementsDialogManager.cpp` 匿名 namespace |
| `ElementsSessionBuild.h/.cpp` | `BuildSession(json, w, h, resource_base, handler, lang)` → `unique_ptr<overlay_session>`。 bridge callback / drag callback / `set_language` / var watch の配線 | `Impl::BeginScreen` の後半 (前半の「surface 全面を既定サイズにする」は overlay 固有なので manager に残す) |
| `ElementsActionQueue.h/.cpp` | `pending_actions` + `OnContinuousCallback` での drain (paint 中に発火した通知を window update の外へ逃がす) | `Impl::pending_actions` + `Impl::ActionDrainHook` |

> `ElementsActionQueue` は **1 本を manager とパネルで共用**する
> (ダイアログとパネルの通知順序が入れ替わらないように)。 いまの drain は
> 「`FindByHandler` で生きているインスタンスがあるか」で捨て判定をしている
> ので、 **owner ごとに「この handler はまだ生きているか」の述語を登録する**
> 形へ一般化する。

**B. パネル本体** (`common/visual/elements/ElementsLayerPanel.h/.cpp`)

```
class tTVPElementsLayerPanel : public tTVPContinuousEventCallbackIntf
    unique_ptr<overlay_session>  session
    tTJSNI_BaseLayer*            layer        // 弱参照。 描画先
    iTVPDialogEventHandler*      handler
    vector<tjs_uint32>           staging      // w*h。 連続 pitch (部分再描画の前提)
    int w, h                                  // = Layer のサイズ

    bool Open(json_utf8, resource_base)       // BuildSession → staging 確保 →
                                              //   TVPAddContinuousEventHook(this)
    void Close()                              // Hook 解除 → session 破棄 → OnClosed

    void OnContinuousCallback(tick) override   // ★ 自前で毎フレーム回す
        session->update(dt)
        dirty なら render_to_buffer_partial(staging, w, h, 0, 0, rect, updated)
        updated の矩形だけ staging → layer の bitmap へ行コピー
          (layer が ltAlpha なら行ごとに TVPConvertAdditiveAlphaToAlpha)
        layer->Update(updated 矩形)

    // 入力。 座標は Layer local のまま渡す (変換なし)
    void MouseDown/Up/Move/Wheel(x, y, btn, flags)
    void KeyDown/KeyUp/Char/Text(...)         // 呼ばれたときだけ = 既定では鍵を取らない

    // 状態
    bool SetVar/GetVar/DescribeVars/RefreshVarWatch/SetLanguage/Invalidate
    bool FocusById/ActivateById
```

要点:

- **`PaintOverlay` を一切通らない**。 駆動は継続イベントフック
  (manager の `ActionDrainHook` と同じ仕組み) で、 krkrz のアニメーション
  レイヤと同じ「毎フレーム描いて `Update`」の作り
- **画素形式**: elements は premultiplied な `0xAARRGGBB` を書く
  (tvg `ColorSpace::ARGB8888` = alpha-premultiplied, A,R,G,B の順)。
  krkrz の Layer が
  - `ltAddAlpha` … **そのまま行コピー**でよい (変換ゼロ)
  - `ltAlpha` (既定) … 行ごとに既存の `TVPConvertAdditiveAlphaToAlpha`
    (SIMD 実装あり) を通す。 ダーティ矩形だけなので負荷は小さい
- **pitch**: Layer の bitmap は `GetMainImagePixelBufferPitch()` が `w*4` と
  一致しない (アラインされる) ことがあるので staging を挟んで行コピーする。
  staging を持つのは `render_to_buffer_partial` の「前回描画が残っている」
  前提を満たすためにも要る

**C. パネルの registry** (`tTVPElementsPanelRegistry`。 小さい)

開いているパネルの一覧だけ持つ。 用途は **プロセス全体の fan-out に限る**:
`SetLanguage` / `InvalidateOverlays` (`registerImage` の差替反映) /
テーマの再適用 / 将来の `Agent.panels()`。 **z 順も入力の調停も持たない**
(そこは krkrz のレイヤツリーの仕事)。

**D. TJS の口** (`common/visual/elements/PanelIntf.h/.cpp`。 `DialogIntf` の写し)

```
tTJSNC_ElementsPanel / tTJSNI_ElementsPanel : iTVPDialogEventHandler
    new ElementsPanel(layer)      // tTJSNC_Layer::ClassID で tTJSNI_BaseLayer* を取る
    openFile(path) / openJson(str) / close()
    setVar / getVar / listVars / registerImage / unregisterImage / invalidate
    mouseDown(x,y,btn,shift) / mouseUp / mouseMove / mouseWheel(delta,x,y)
    keyDown(key,shift) / keyUp / text(str)        // 呼ばなければ鍵を取らない
    focusById(id) / activateById(id)
    property active / watchVars
    イベント: onAction(id, payload) / onDrag(e) / onVar(name, value) / onClosed(action)
```

**イベント名と引数は `ElementsDialog` と同じ**にする。 既存のドライバ (ホスト案件の
画面ドライバ群) がほぼそのまま載る。 `iTVPDialogEventHandler` をそのまま
実装するので、 `BuildSession` と通知キューは無改造で使える。

**E. 使う側の便利クラス** (スクリプト。 KAG3 か sample ライブラリ)

```tjs
class ElementsPanelLayer extends Layer {
    var panel;
    function ElementsPanelLayer(win, par) {
        super.Layer(win, par);
        type = ltAlpha;  hitThreshold = 0;      // 全部のマウスメッセージを受ける
        panel = new ElementsPanel(this);
    }
    function open(path) { return panel.openFile(path); }
    function onMouseDown(x, y, b, f) { panel.mouseDown(x, y, b, f); }
    function onMouseUp  (x, y, b, f) { panel.mouseUp  (x, y, b, f); }
    function onMouseMove(x, y, f)    { panel.mouseMove(x, y, f); }
    function onMouseWheel(sh, d, x, y) { panel.mouseWheel(d, x, y); }
    function onAction(id, payload) {}           // 使う側が override
}
```

ネイティブ側でクラス継承 (`ElementsLayer extends Layer` を C++ で作る) は
**やらない**。 krkrz にネイティブクラスがネイティブクラスを継承する前例が
無く、 スクリプトのクラスで足りる (使う側が自由に派生できる利点もある)。

**初回に入れないもの** (別枠で足す前提を守るため。 要ると分かってから足す)

- **キー / パッドのフォーカス調停**。 鍵はスクリプトが明示的に流したときだけ。
  「複数のパネルのうちどれがキーを取るか」は krkrz 側に既存の枠が無いので、
  先に入れると必ず「変な影響」になる
- **navigator フロー / `transitions`**。 1 パネル = 1 画面。 画面の切替は
  `openJson` を呼び直す。 クロスフェードは Layer を 2 枚にして krkrz の
  `[trans]` に任せる (それができるのがこの案の狙いなので)
- **`close_on_click` の自動 finish / モーダル結果**。 `onAction` だけ
- **仮想キーボード / IME**。 `input_box` を置くパネルは後回し

**F. 既存コードへの触り方**

| ファイル | 変更 |
|---|---|
| `ElementsDialogManager.cpp` | 匿名 namespace の入力変換を `ElementsInputMap.h` へ移動。 `Impl::BeginScreen` の後半を `BuildSession` 呼出へ。 `pending_actions` を共有キューへ。 **挙動は変えない** |
| `ElementsDialogManager.cpp` (`SetLanguage` / `InvalidateOverlays`) | パネル registry へも fan-out |
| `LayerIntf.h` | 変更なし (`GetMainImagePixelBufferForWrite` / `GetMainImagePixelBufferPitch` / `Update(rect)` は既に公開) |
| CMake | 新規 3 + 2 ファイルを `KRKRZ_USE_ELEMENTS` の枠に追加 |

**残る確認点**

- `overlay_session::update()` に渡す dt を継続イベントの tick 差分で作るが、
  **継続イベントの間隔はフレームと一致しない**。 演出のなめらかさに影響する
  なら `Update` を打つ頻度を別に絞る余地がある
- Layer のサイズが変わったとき (`setSize`) は staging 再確保 +
  `notify_view_resize`。 スクリプトから呼ばせるか、
  `ElementsPanelLayer.onResize` を用意するか
---

## 9. 同じチャンネルの `animate` が連ならない — ✅ 対応済み

> **2026-09-01 対応** (elements `8f5f0145` / `src/core` 58cc0a81)。
> `animator` に「チャンネルごとに、 いま支配している束縛 1 本」を決める
> `governing_index()` を入れ、 tick / start / fire / focus・hover の各所で
> その 1 本だけを反映するようにした。 支配は「**delay を過ぎて再生を始めた
> 束縛のうち最後のもの**」で、 まだどれも始まっていなければ先頭。
> これで `"delay"` の昇順に並べるだけで折れ線になる。
> 1 本しか無いチャンネルと別チャンネルの同時掛けは挙動不変 (後方互換)。
> `tween` に `waiting()` を足したのはこの判定のため。 README に例つきで追記。
>
> 検証: ヘッドレスで 2 本 / 3 本の折れ線・単体 delay・別チャンネルの
> 同時掛けを数値比較 (修正前は先行の動きが消え、 修正後は繋がる)。
> 実機でも既存画面 (enter move + exit move / enter move + hover move) の
> 見た目が変わらず、 hover の往復も差分 0px で完全復帰することを確認。


報告: 2026-09-01。 1 つの要素に `delay` 違いの `move` を 2 本並べても
**折れ線にならず、 そもそも動き出さなかった**。 README は `"delay"` を
「スタッガー/シーケンスに使う」と書いているので、 意図とずれている。

**原因はコードから明らか**: `anim_binding::apply()` は毎フレーム
**無条件に**チャンネルへ書き込み、 `delay` 中は進捗 0 = `from` の値を書く
(`include/elements_modal/animator.h`)。 同じ `xform_state` を共有しているので、

- 「移動 + 拡縮 + 回転」の同時掛けは**別フィールドを書くので合成される** (README どおり)
- しかし **同じチャンネルを 2 本**にすると合成にならず、 毎フレーム
  **後ろのエントリが前のエントリの結果を上書きする**。 後ろが `delay` 中は
  その `from` に固定されるので、 先行するエントリの動きが一切見えない

**対応案**: チャンネルごとに「**いま支配している binding**」を 1 本決めて、
それだけ `apply()` する。

- そのチャンネルで **`delay` を過ぎて再生を始めた binding のうち最後のもの**が支配
- まだどれも始まっていなければ **先頭の binding** が支配
  (単体の「遅れて出てくるスライドイン」が `delay` 中に `from` で待つ今の挙動を保つ)

これで **`delay` の昇順に並べるだけで折れ線になる**。 1 本しか無いチャンネルの
挙動は変わらないので後方互換。

**ホスト側の現状回避**: 多段の演出は TJS のタイマ駆動へ逃がしている。
直れば駆動コードが減り、 演出が画面 JSON に収まる。

---

## 10. 報告したが「既存機能で組み方を直せば済む」だったもの (記録)

再発防止と、 同じ相談が来たときの回答用に残す。 **elements 側の変更は不要**。

### 10-1. `atlas_choice` の選択表示が、 別のグループを押すと消える

**症状**: `selected_var` の違うラジオグループを 2 組置くと、 片方を押した
ときにもう片方の**選択表示だけ**消える。 変数は正しいまま。 `setVar` で
入れ直しても戻らない。

**答え**: 仕様どおり。 排他スコープは **「自分の直近の親 composite」** なので、
1 枚の `canvas` に独立したグループを直接並べると相互排他になる。
README の「**排他グループの分離**」のとおり、 **各グループを別々の composite
(ネストした `canvas` 等) に入れる**。 ホスト案件はこれで直った
(生成ツール側でグループごとに入れ子 canvas へ畳むようにした)。

> `setVar` で戻らないのは、 兄弟スキャンが widget を直接 `select(false)` する
> のに対し、 そのグループの変数は変わっていないので購読が発火しないため。
> **組み方を直せば起きない**ので追わない。

### 10-2. `atlas_image` の `rect_list` が bounds へ引き伸ばす

**症状**: `rect_list` + `index_var` で N 枚から 1 枚を選ぶとき、 大きさの
違う絵を並べられない。

**答え**: **`"native": true`** (または `"native_frames"`) で「引き伸ばさず実寸の
まま bounds 中央へ」描ける。 README の `atlas_image` に記載済み。
ホスト案件は知らずに「同じ場所に N 個置いて使わない方を `at_var` で画面外へ
park する」回避をしていた (動いてはいるので急がないが、 新規の画面は `native`
を使う)。
