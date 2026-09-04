# krkr 案件へ Elements UI を組み込む — 統合リファレンス

`elements` skill 本体は **Elements 単体の使い方** (Dialog API / レイアウト JSON /
navigator)。こちらは**吉里吉里Z のゲーム (KAG/kag 機構) に実際に載せるとき**の
統合知識 — engine 側の事実と制約、TJS 配線の型、ライフサイクルの落とし穴、
資材の探索、検証手段、未解決事項をまとめる。

**案件固有の値 (画面名・kag プロパティ対応表・ドライバ一覧) は各案件の資料を見ること**。
ここに書くのは全案件で共通する部分だけ。

## 0. 層構成

```
 KAG シナリオ / kag / SystemAction        ← ゲーム進行・設定値の実体
        │ syshook / kag.process() / kag.*
 画面ドライバ (案件ごと。例 uielements.tjs)   ← 「押したら何をするか」を書く層
        │ extends / show() / setVar()
 基盤 TJS (例 ElementsUI.tjs)               ← 触る頻度は低い。基底クラスと初期化
        │ showFile / onAction / onClose
 native ElementsDialog クラス (elements_modal)      ← engine
        │ 読む
 画面資材 <name>.jsonc + atlas PNG          ← uitool で生成
```

基盤と画面ドライバを分けるのが要点。基盤 = Elements 非対応 exe でも壊れないための
ガードと共通基底、ドライバ = 案件のふるまい。

## 1. 起動と存在判定

- **クラス名は `ElementsDialog`** (2026-09-04 に旧名 `Dialog` から改名。ゲーム側
  TJS のクラス名と実際に衝突したため。互換エイリアスなし)。旧 exe (クラス名
  `Dialog`) と混在する期間は、初期化時に
  `if (typeof global.ElementsDialog != "Object" && typeof global.Dialog == "Object") global.ElementsDialog = global.Dialog;`
  で新名へ寄せてから、以後 `ElementsDialog` だけを使うと両対応になる。
- ロードは条件付きにして非対応 exe を守る:
  `KAGLoadScript("...") if (typeof global.ElementsDialog == "Object");`
- **フォント登録 (`setupFont()` 相当) は show の前に一度**。krkr は複数フォルダの
  フォントリストを作れないので、**一か所で一括登録**する方針
  (engine 側は `fonts.json` 宣言 + 初回使用で遅延ロード、glyphware で統一済み)。

## 2. 表示経路の選択 (最初に決める設計判断)

- **非モーダル (`showFile` / `showJson` / `showDict`) + コールバック**が原則。
  `showModal*` はネストポンプに入るため **REPL やイベントが止まる**。
- `{"type":"button","close_on_click":true}` の決定は **`onClose(action=ボタンid)`**
  で来る (`onAction` ではない)。Esc/× は `action=""`。選択系メニューはこの形が定石。
- **TJS サブクラスは明示 `super.ElementsDialog()` (旧 exe は `super.Dialog()`) が
  必要**。明示コンストラクタ無しで `new` すると表示とナビは効くのに
  `onAction`/`onClose`/`onScreen` が一切来ない
  (engine 側で `Owner` がコンストラクタ経由でしか設定されないため)。
- **`showFile` は Storages の autopath 探索に乗っていない** — ファイル名だけでは
  失敗する。パス付き (`"system/foo.jsonc"`) で渡す。★engine 側 要調査
- **overlay の表示サイズ** — overlay 経路にはサイズ引数が無く、画面 JSON の
  top-level `"size"` が上限になる。**`"size"` を書かなければ surface (ゲーム画面)
  全面が上限**なので、全画面級の画面も普通に組める (旧: 既定 400x220 きめうちで
  クリップされていた)。実サイズは fit-to-content で決まる (`size` は上限指定)。
  top-level `"size"` の抽出は **深さ 1 のキーだけ**を見る (2026-08-29 修正、
  src/core `7352157f`)。以前は入れ子の配列 `"size"` — `spacer` の `[w,h]` や
  9-slice thumb の `[w,h]` — を先に拾ってダイアログがその大きさに縮んだ。

## 3. KAG のダイアログ / パネル枠に乗せる (ホストレイヤ方式)

既存の `openDialog` / `showPanel` 機構をほぼ無改造で使うために、**Elements の
セッションを透明な DialogLayer / PanelLayer 派生 (ホスト) でラップ**する。

- ホストは全面透明 (`hitType=htMask`, `hitThreshold=0`) なので、ウィジェット外に
  素通りした入力を吸収し、下の UI への漏れを防ぐ。KAG 側キー系も遮蔽される。
- **`finalize()` で native の close を必ず実行**する。`closeDialog` 一括・
  強制破棄・直接 invalidate のどの経路でも Elements 側が取り残されない。
- **二重クローズを冪等に**: Esc は Elements 側 (`onClose`) と KAG 側
  (`onKeyDown`/`onRightClicked`) のどちらが先に食うか exe 差があり得る。
  `_done` フラグ + `isvalid` で守る。
- conductor は `openDialog` が interrupt するので、「開く=停止 / 閉じる=再開」が自動。
- **z オーダーの構造的制約**: overlay (ElementsDialog) は native overlay なので
  **常に KAG レイヤ群より上**に出る。Elements パネル表示中に旧 DialogLayer を
  開くと論理 z と見た目が食い違う。
  → **本命は `ElementsPanel`** (2026-09 以降の exe): 同じ画面 JSON を KAG レイヤの
  ビットマップへ描くので z 順・`[trans]`・piledCopy がレイヤの仕組みに従い、
  この制約自体が消える (skill 本文 §3 参照)。イベント / 変数 API は同形なので
  ドライバはほぼ流用できる (入力はホストレイヤの onMouse* から `panel.mouse*` へ
  流す)。旧 exe では従来どおり「旧ダイアログ表示中だけ Elements 側を一時 hide
  するフック」か同時使用回避で運用する。

## 4. 画面ドライバの型

1 画面 = 1 jsonc を非モーダル表示し、アクション/クローズを派生クラスへ中継する
基底クラスを 1 つ持つ。最低限のインタフェース:

| メンバ | 役割 |
|---|---|
| `show(vars)` | 表示 + 直後に流し込む変数辞書 |
| `closeScreen()` | **明示クローズ**。`onClosed` は発火しない |
| `setVar(name, value)` | 表示中の変数 store を更新 (`text_var` / `value_var` 連動) |
| `onOpen()` / `onAction(id, payload)` / `onClosed(action)` | override 用フック |

**落とし穴**:

- **明示クローズと自動クローズを区別する**。自分で閉じた (`closeScreen`) ときは
  `onClosed` が来ない。Esc/×/engine 都合で閉じたときだけ来る。
- **常駐画面の「閉じたら再表示」は状態フラグで守る**。`onClosed` で無条件に
  `show()` すると、**ゲーム本編に入った後でも復活して入力を奪う**
  (別の Elements ダイアログの出入りで `onClosed` が誘発される)。
  「今この画面を出しておくべきか」を `wantVisible` 等で持ち、syshook で切り替える。
- **タブ切替の巻き添えを復帰処理にしない**。「今の画面を閉じて次を開く」方式では、
  切替で閉じた旧画面の `onClosed` はレジストリ側で吸収し、`current` と一致しない
  ものは無視する。

## 5. 値の出し入れ

- 表示時は `show(vars)` で一括注入、表示中は `setVar()`。
- **状態は変数で読み書きする** — `atlas_toggle` / `atlas_slider` は `value_var`
  (`"v_" + id` の命名規約が扱いやすい)。`atlas_toggle` の `value_var` 対応は
  **2026-08-10 以降の exe** が必要。
- **スライダの数値表示は `display_var`** + 書式 (`min`/`max`/`step`/`digits`/`suffix`)。
  engine が整形済み文字列を変数へ書くのでホスト実装は不要。**表示は四捨五入**なので、
  ドライバ側の `payload` → 実値の換算も四捨五入に揃える (切り捨てにすると
  「表示 65% なのに保存値 64」のズレが出る)。書式のレンジは実値の換算式と一致させる。
- **動的画像 (セーブサムネ・CG) は PNG 化して注入**する:
  ```tjs
  lay.saveLayerImage(tmp, "png");            // ★engine のデコーダは krkr の BMP を読めない
  ElementsDialog.registerImage("id", tmp);   // "mem://id" で参照
  ```
  差し替えは **再 register するだけで表示中の画面にも即時反映**される
  (2026-09 以降の exe。engine が `refresh_mem_image` で構築済み widget を
  再デコードする)。旧 exe では build 時に一度だけ読むため、再 register 後に
  画面を開き直す。いずれも**登録前に build した widget は空表示**なので、
  初回は画面を開く前に register する。

## 6. 資材の探索とファイル I/O

- 画面資材 (`json/` + `atlas/`) は uitool のランタイム規定構造。案件では
  **`uitool_project.json` の `runtime` をゲームの資材フォルダへ直接向ける**と
  export がそのまま資材になる (uitool 側 `docs/case_project_guide.md`)。
- **リソース解決は krkr 低層に任せてよい** — 「パスつき検索 → パスなし
  (ユニークファイル名) 検索」を行うので、**検索パス登録 + ファイル名をユニークに
  保つ**だけで足りる。elements 側にファイル名検索を足す対応は不要 (2026-08-08 結論)。
  ただし `showFile` 自体は autopath に乗らない (§2) ので呼び出しはパス付きで。
- engine のファイル I/O は監査済みで健全: `ELEMENTS_FILE_IO_SUPPORT=OFF` +
  `TVG_FILE_IO=OFF` 強制 + `StoragesResourceLoader` 経由 (画像/フォント/JSON すべて)。
  独自の I/O インタフェースを足す必要はない。

## 7. 画面遷移とエフェクト

- 複数画面フロー (navigator / `showFlow`) の切替に **fade / universal** の遷移を
  指定できる (`rule` 画像 + `vague`)。CPU 合成なので全 DrawDevice で同じに出る。
- **旧画面は last_frame 方式** (finish 後の session は再描画できないため、直近フレームの
  複製を遷移元に使う)。遷移中に旧画面が動くことは期待しない。
- **退場 (exit) 演出は `ElementsDialog.close()` と協調**する (`close_after_exit`)。
  即時 teardown が要るときは ForceClose 系。
- GPU 側で自前に混ぜたいときは `Canvas.drawTransition(front, back, phase, rule, vague)`。

## 8. 実機検証 (REPL / Agent)

```
<exe> -replfile=<チャネルdir>        # skill dev-toolkit:appctl の作法で起動・停止する
```

- `Agent.dialogs()` … 表示中ダイアログ一覧 (index / modal / screen / focused / rect)
- `Agent.dialogClick(index, "<id>")` … id 指定でボタン起動 (座標不要)
- `Agent.captureScreen("path.png")` … overlay 込みの実画面 PNG → Read で目視確認
- **`Agent.dialogClick` の取りこぼし**: choice_nav グループ内の `atlas_choice` や、
  多ボタン + vars_on_focus + 全画面レイアウトでは activate しないことがある。
  実マウスクリック (`Agent.click(x, y)`) / 実キー入力なら正常。**自動テストの誤診に注意**。
- **REPL 中のモーダル** (`inputString` / `confirm` 等) は応答チャネル待ちになる
  (既定 30 秒でタイムアウト例外)。

## 9. 実務 (文字コード・配置)

- 案件のドライバ TJS が **Shift-JIS** のことがある。**SJIS ファイルに Edit/Write を
  直接使わない** (ASCII だけの挿入でもファイル全体が UTF-8 化して壊れる)。
  UTF-8 原本を別に持ち `iconv -f UTF-8 -t CP932` で配置する。
  **全角ダッシュは U+2015 (―)** を使う (U+2014 は CP932 に変換できない)。
- レイアウト `.jsonc` は UTF-8 のまま直接編集してよい (コメント・末尾カンマ可)。
- **リリースパックでは devmode と参照先が違う**ことがある (開発ツリーの
  `sysscn/` を見るか、パック内の `data/sysscn/` を見るか)。基盤 TJS の同期漏れに注意。
- TJS の文法は skill `tjs2`。よく踏むのは**後置 `if` が式限定**
  (`return X if (cond);` は文法エラー)。

## 10. 未解決 / engine 側 TODO (★は要対応・要調査)

| 項目 | 状態 |
|---|---|
| overlay が surface 全面に広がらない (既定上限 400x220) | ✅ 解消済み。`"size"` 未指定なら surface 全面が上限 |
| top-level `"size"` の peek が widget の `"size"` を誤読 | ✅ 解消済み (2026-08-29 src/core `7352157f`)。深さ 1 のキーだけを見る |
| `showFile` が autopath 探索に乗らない | ★要調査。当面はパス付きで回避 |
| サブクラスで明示 `super.ElementsDialog()` が無いとイベントが来ない | ★要調査。当面は必ず書く (2026-09-04 のクラス改名でコンストラクタ名も ElementsDialog に) |
| `Agent.dialogClick` が activate しない条件がある | ★要調査 (Agent ツール側)。実運用に影響なし |
| DrawDevice overlay 描画口の汎用開放 | 【予定】未着手 |
| 遷移の GPU present 拡張 (Phase C) | 将来 optional (CPU で足りている) |
