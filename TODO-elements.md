# Elements 要修正事項 (ホスト案件からのフィードバック)

Elements (`src/core/external/elements` = wamsoft/elements、その中の
`external/elements_modal`) に対して、ホスト側案件で実際に踏んだ不具合・改善要望を
溜めておくファイル。Elements 側の作業時間が取れたときにまとめて対応し、対応後は
`src/core` の submodule bump → 各案件へ展開する。

対応したら項目に ✅ と対応コミットを書き、消さずに残す (再発防止の記録)。

---

## 1. 複数行テキストがレイアウトで壊れる (優先度: 高)

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

### 1-c. (確認事項) dialog の `size` は「固定」ではなく「上限」?

`"size": [320, 220]` でも内容が小さいと実サイズは内容ぶん (例 104x42) に縮み、
内容が大きいときは指定値まで伸びる。仕様ならスキーマ表に明記してほしい。

### 1-d. elements_console (EUI DSL / uitool) 側

同じ落とし穴を DSL でも踏むので、lint (label の text に改行 → 警告して text_area を
勧める) と README 注記があると良い。

### ホスト側の現状回避策 (対応後に外せる)

rpgsys は**複数行テキストを行ごとの label に分解して vtile へ積む**回避策を入れた
(`data/rpglib/menu.tjs` の `addLines` / `setLineVars` / `lineVars`)。
reactive 更新のため `text_var` も行ごと (`status0`, `status1`, ...)。
Elements 側が直ったらこの回避策は削除する。
