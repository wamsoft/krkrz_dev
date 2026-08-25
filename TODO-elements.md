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

環境: krkrz SDL3 ビルド (2026-08-13 ビルド、glyphware 統合後) + `Dialog.showDict`。
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

環境: krkrz SDL3 / WINVER 両ビルドの overlay ダイアログ (`Dialog.showDict` 系 +
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

## 3. input_box にプログラム的フォーカスが効かない (優先度: 中)

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
