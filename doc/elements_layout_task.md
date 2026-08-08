# Elements JSON レイアウト改善 作業指示 (2026-08-08)

> **状況 (2026-08-08 実装完了)**
>
> - **1. `gap` 属性 / 2. `style` ブロック**: 実装済 (elements_modal
>   json_layout.cpp)。`gap` は vtile/htile の子間へ spacer 自動挿入相当、
>   `style` は `font_scale` / `tile_gap` / `row_height` (button 系 +
>   input_box + selection_menu の vmin_size 相当) / `padding` (content
>   外側余白) を未指定値の既定として適用。既定 0 で従来と完全一致を
>   実機キャプチャで確認 (elements_flow / 密着ダイアログ無変化)。
> - **3. Dict 経由 bool 属性**: **現行 HEAD では再現せず**。number 0/非0 の
>   真偽受容は elements df9fcffd (2026-07-20) で対応済みで、showDict +
>   `close_on_click => true` (int 1) → クリックで閉じることを実機確認した。
>   json_layout 全域 + 他ソースを横断監査し、厳格 `is<bool>()` 判定の残りは
>   無し。**再現した「別案件」は elements の pin が df9fcffd より古いはず**
>   なので、submodule/checkout の bump で解消する。
> - **uitool 追従**: uitool のエクスポートは canvas 絶対配置 (atlas_* + at)
>   主体で vtile/gap を出力しないため追従不要と判断。手書き画面の importer
>   は spacer を自前モデルに畳んでおり gap 対応は必要になった時点で検討。
> - ドキュメント: elements_modal README (style ブロック節 + gap)、
>   src/core/doc/ElementsDialog.md、doc/topics/core/elements_dialog.md 反映済。

Elements ベーストランジション作業と同領域のため本リポジトリ側で検討・実装する。
発端: JSON/Dict 定義 UI が既定で「詰まった」見た目になる問題 (複数プロジェクトで再現)。

## 背景 (現状の挙動)

1. `vtile`/`htile` に自動の隙間 (gap) がなく、子は密着で積まれる (spacer 手挿入が必須)
2. ダイアログは fit-to-content で中身の自然サイズまで縮む → 余白なしの塊になる
3. テーマ既定がツール UI 密度 (フォント≒14px、ボタン自然高もコンパクト)
→ 明示指定を省略すると常に「みちみち」になり、UI 記述が spacer だらけになる

## 提案 (2段階)

### 1. コンテナ `gap` 属性 (小改修・即効)

```jsonc
{ "type": "vtile", "gap": 8, "children": [...] }   // htile も同様
```
- json_layout の構築時に子の間へ spacer を自動挿入するだけ。既定 0 で後方互換
- cycfi コアの改造は不要 (elements_modal 内で完結)

### 2. トップレベル `style` ブロック (テーマ機構の入口)

```jsonc
"style": { "font_scale": 1.25, "row_height": 44, "tile_gap": 8, "padding": 24 }
```
- widget 側で未指定の値の既定として構築時に適用
- 将来の 9patch/atlas スキン指定 (テーマ一括差し替え、known_issues 記載の将来課題) の
  受け皿としてここを拡張していく想定

実装場所: `external/elements/external/elements_modal/src/json_layout.cpp` (構築部)。
elements_modal README のスキーマ表、EUI/uitool 側 (sibling リポジトリ) の追従も併せて。
消費者は elements_console (即検証可) と krkrz (submodule bump + リビルド) の2系統。

## 併せて調査: Dict 経由の bool 属性が効かない件

- **症状**: `Dialog.showDict` で `close_on_click => true` と書くと TJS の制約で int 1 に
  なるが、**このとき close_on_click が機能しない** (クリックで onAction は発火するが
  セッションが閉じない)。JSON 文字列で `"close_on_click": true` と書けば機能する
- elements_modal README は「0/非0 を真偽として受ける」としており、ドキュメントと実装が
  乖離している可能性。json_layout の該当属性が `is_bool()` 等の厳格判定になっていないか確認
- close_on_click 以外の bool 属性 (initial_focus / arrow_focus_nav / edgeConnect 系など) も
  同様の判定漏れがないか横断確認したい
- 再現環境: SDL3 ビルド + showDict のオーバーレイダイアログ (2026-08-08 実測)。
  回避策として現状は onAction 側で明示 close() している

## 検証の観点

- gap/style 追加後、既存レイアウト (data/ui/*.json, elements_gallery) が無変化であること
- showDict (Dictionary→JSON 変換経路) でも gap/style/bool 属性が期待通り効くこと
