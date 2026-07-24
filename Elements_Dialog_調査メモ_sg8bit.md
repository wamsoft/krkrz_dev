# Elements Dialog 調査メモ (pcx_5pb_sg8bit ランチャー実装中に判明)

STEINS;GATE 8BIT (pcx_5pb_sg8bit) のコンソール版ランチャー(機種選択)を
`Dialog` (Elements) で実装する過程で分かった挙動・ハマりどころ・要調査点の
メモ。engine 側 (`krkrz_dev/src/core/common/visual/elements/`) で後日確認する。

環境: `krkrz_nx_sg8bit` build/x64-windows/Release、SDL3 + OGL DrawDevice、
`KRKRZ_USE_ELEMENTS=ON`、layerExVector 組み込み済み。REPL (`-replfile`) 駆動。

---

## 1. TJS サブクラスは `super.Dialog()` 明示コンストラクタが無いとイベントが一切届かない ★要調査

`class Foo extends Dialog { function onAction(){} function onClose(){} }` を
**明示コンストラクタ無し**で `new Foo()` すると、`showJson`/`showDict` で表示は
できる (ダイアログは出る・ナビも効く) が、**`onAction` / `onClose` / `onScreen`
等のイベントが TJS 側メソッドに一切届かない**。

原因は `tTJSNI_Dialog::On*` が `if (!Owner) return;` で、`Owner` (TJS オブジェクト
への逆参照) が未設定のため `TVPPostEvent(Owner, ...)` が飛ばないこと
(`DialogIntf.cpp` の `OnAction`/`OnClosed`/`OnScreenEnter` 参照)。

**回避策**: サブクラスに明示コンストラクタを書き、`super.Dialog()` を呼ぶと
`Owner` が設定されイベントが届くようになる。

```tjs
class Foo extends Dialog {
    function Foo() { super.Dialog(); }   // ← これが無いと onClose 等が来ない
    function onClose(action) { ... }
}
```

要調査点:
- サブクラスで明示 super 呼び出しが無い場合に `Owner` が設定されないのは
  仕様か、それとも設定漏れ (ネイティブクラス継承時の Owner 紐付けが
  コンストラクタ経由でしか行われない) か。
- **本件は特に「Dialog クラス名が別名で参照されている」状況で踏んだ**
  (下記 3 参照)。素の `Dialog` で継承した場合に自動 super が効くかは未確認。
  ドキュメント (`doc/topics/core/elements_dialog.md`) の例は明示コンストラクタ
  無しで書かれているので、素の場合は効いている可能性がある。
- 望ましくは「明示 super が無くても Owner が設定される」ようにするか、
  ドキュメントに「サブクラスは super.Dialog() 必須」を明記する。

## 2. `close_on_click` ボタンは `onClose(action)` で通知される (`onAction` ではない)

`{"type":"button","id":"X","close_on_click":true}` を押す/Enter すると、
セッションが finish し **`onClose(action)` が `action = "X"` で呼ばれる**。
`onAction` は (少なくともこの経路では) 呼ばれない。

- Esc / × で閉じた場合は `onClose(action="")` (空文字)。
- これは仕様と思われる (modal は「中で情報完結」= onClose/戻り値で受ける)。
  `DialogIntf.cpp` に「showModalJson 経路では onAction は発火しない
  (内部 collector handler が全イベントを吸収)」の注記あり。
- 実装側の教訓: 選択系メニューは `close_on_click` + `onClose(action)` で組む。
  非 close の値変化を拾いたいときだけ `onAction`。

## 3. ゲーム側が `global.Dialog` を上書きしていて Elements の Dialog が隠れる (ゲーム固有)

pcx_5pb_sg8bit は `data/sysscn/system.tjs` で
`var Dialog = new DialogModeManager();` と **global.Dialog を独自インスタンスで
上書き**しており、ネイティブ Elements `Dialog` クラスが参照できなくなる。

**回避策 (ゲーム側)**: `Initialize.tjs` (system.tjs より先に走る) で
`global.ElementsDialog = global.Dialog;` とネイティブクラスを別名退避し、
以降 `class X extends ElementsDialog` で使う。

engine 的にはゲーム固有の名前衝突なので engine 修正は不要だが、
「Dialog という一般的な名前は衝突しやすい」ことの一例。
(将来 Elements 側クラス名を別名にする案も出たが波及大のため保留)

## 4. オーバレイ Dialog が画面 (1280x720) いっぱいに広がらない ★要調査 (最重要)

`showDict`/`showJson` のオーバレイダイアログが **content サイズに縮んで中央
表示**され、ゲームウィンドウ全面 (1280x720) に広げられない。

試したが効かなかった指定 (いずれも content ルートに置いた):
- `hmin_size`(width) + `vmin_size`(height) … サンプル (image_demo/sysmenu) が
  fullscreen 用に使っている形。standalone の elements_console では全画面だが、
  **ゲーム内オーバレイだと小さいまま**。
- `hsize`(width) + `vsize`(height) 固定サイズ
- top-level `"size": [1280,720]`

`Agent.dialogs()` の rect は ~400x220 のまま (この測定値自体が content bounds
なのか overlay bounds なのかも要確認)。

### 根本原因 (engine コード確定): `ElementsDialogManager::Impl::BeginScreen`

`ElementsDialogManager.cpp` の overlay サイズ決定ロジック (BeginScreen,
行 416-455 付近) を読んで確定した:

```
inst.dialog_w = 400;  inst.dialog_h = 220;          // ★ハードコードのデフォルト上限
// JSON top-level "size":[w,h] があればそれを上限に採用 (コメント「上限サイズ」)
if (size 指定あり) { inst.dialog_w = w; inst.dialog_h = h; }
sess->start(json, inst.dialog_w, inst.dialog_h, ...);
// content の自然サイズへ「縮める」フィット (上側空欄対策):
if (sess->measure_content(mw, mh)) {
    int fit_w = (mw > 0 && mw < inst.dialog_w) ? mw : inst.dialog_w;  // 縮小のみ
    int fit_h = (mh > 0 && mh < inst.dialog_h) ? mh : inst.dialog_h;
    inst.dialog_w = fit_w; inst.dialog_h = fit_h;
}
// PresentOverlay(layer, rect.x, rect.y, dialog_w, dialog_h)  // ここで描画・クリップ
```

つまりオーバレイの最終サイズ = **`min(measure_content, top-level "size" or デフォルト 400x220)`**。

- **"size" 未指定 → 上限 400x220 きめうち**。content がそれより大きいと
  **クリップされる** (実測: 機種ボタンが右で見切れ、中央 400x220 だけ描画)。
- **"size":[1280,720] 指定 → 上限は 1280x720 に上がる**が、`measure_content`
  が返す自然サイズが小さいと **そこまで縮む** (実測: hspacer 1280 + margin
  構成だと measure が 96x72=margin 相当を返し、96x72 に縮んだ)。
- `hmin_size`/`hsize`/`hspacer` 等の「最小/固定幅」指定は **measure_content の
  値には効かない模様** (measure が想定より小さい値を返す)。
- 補足: `measure_content` が **false を返すか mw/mh が 0** の場合は fit ブロックが
  skip され、dialog は "size"(=1280x720)のまま full 表示になるはず
  (この経路を使えば全面化できる可能性)。

### 「実装概念が漏れている」箇所 (ユーザ指摘・要 engine 対応)

- `showModalJson`/`showModalFile` は width/height を取り、独立 SDL_Window を
  その寸法で開く。一方 **overlay 経路 (`showJson`/`showFile`/`showDict`) には
  サイズ引数が無く**、上記のとおり default 400x220 に頭打ち。
  → **overlay にも「表示サイズ」または「surface 全面フィル」の概念が必要**。
- 候補となる engine 修正:
  1. overlay のデフォルト上限を **surface サイズ (innerWidth/Height)** にする
     (400x220 きめうちをやめる)。
  2. top-level に `"fill": true` / `"size": "surface"` を追加して full 化。
  3. `measure_content` が `hmin_size`/`hsize`/`hspacer` の幅を尊重するよう修正
     (今は縮小方向にしか効かない/効いていない)。
  4. overlay の show 系にも width/height 引数を追加 (showModal と対称に)。
- ゲームの外枠 UI (ランチャー/タイトルメニュー/コンフィグ) は全画面前提なので、
  この修正は SGOCT-5/8/9 全体に効く。**優先度高**。

### さらに: top-level "size" の peek が壊れている ★要調査

BeginScreen の "size" 抽出は **JSON 文字列を素朴に検索** している:

```cpp
auto pos = json_utf8.find("\"size\"");   // 最初の "size" を拾う
auto lb  = json_utf8.find('[', pos);     // その後の最初の '[' を拾う
```

ところが widget の **フォントサイズも `"size": 32` というキー**なので、
top-level の `"size":[1280,720]` より先に button の `"size":32` がヒットし、
その後の `[` (別の配列) を拾って誤解釈する。結果 top-level "size" が効かず
**default 400x220 のまま**になる (実測: "size":[1280,720] + hsize/vsize でも
400x220 のまま)。

→ peek ではなく **パース済み JSON の top-level から "size" を取る**べき。
   (そもそも overlay サイズを content 依存にせず surface 既定にするのが
    本筋なので、上記「概念漏れ」の修正で一緒に解消するのが望ましい)

### 当面の回避 (未確立)

engine 修正なしで全面化する確実な方法は見つかっていない。
`measure_content` を回避 (false/0 を返させる) か "size" を正しく効かせる必要が
あるが、いずれも上記バグに阻まれる。**engine 側対応が本筋。**

## 5. Agent.dialogClick がオーバレイのボタンを activate しないことがある ★要調査 (Agent ツール)

`Agent.dialogClick(index, id)` (= focus 適用 → Enter 送出) が、
**単純な 2 ボタンのダイアログでは効く**が、ランチャー (8 個の close_on_click
ボタン + vars_on_focus + 全画面レイアウト) では **activate しない**
(onClose が飛ばず閉じない)。

一方、**実キー入力 (Agent.keyDown/keyUp で VK_RETURN=13) は正しく activate**
し、focus 中の機種で `onClose(action=機種id)` が飛ぶ。マウス/パッドの実入力も
問題ない。

要調査点:
- `ActivateWidgetById` (`ElementsDialogManager.cpp`) の
  「focus を即時適用してから Enter を送る」経路が、多ボタン/特定レイアウトで
  取りこぼす条件。Agent 検証ツールの信頼性に関わる。
- ※ 実運用 (実キー/パッド/マウス) には影響しないので優先度は低いが、
  自動テストで dialogClick を使うと誤って「動かない」と誤診する
  (実際、本実装のデバッグ中に長時間ハマった)。

## 6. `Dialog.showFile` が Storages の autopath 自動探索に乗っていない ★要調査

`data/system/_sysmenu.jsonc` を置いて `showFile("_sysmenu.jsonc")` (ファイル名
のみ) すると **「ストレージ _sysmenu.jsonc を開くことができません」** で失敗。
`showFile("system/_sysmenu.jsonc")` (サブディレクトリ付き) にすると開ける。

一方、同じファイルを `Scripts.execStorage("system/...")` は普通に読めるし、
ゲームの他資材はファイル名だけで autopath 解決される。つまり **Dialog の
ファイル解決 (`ShowFromJsonFile` → `StoragesResourceLoader`) が krkrz の
autopath 自動探索を通っていない** 疑いがある。

要調査点:
- `ShowFromJsonFile` / `StoragesResourceLoader` のパス解決が
  `Storages.getPlacedPath` 相当 (autopath 探索) を通しているか。
- 通していないなら、ファイル名のみでの参照ができず、呼出側が常にフルパス/
  サブディレクトリ付きを書く必要があり不便。autopath 探索に乗せるべき。
- jsonc 内の相対資材参照 (atlas の `resources/xxx.png` 等) の解決基準
  (jsonc の場所基準か、固定 resource root か) も併せて要確認。

---

## 参考: 動いた実装パターン (ランチャー)

```tjs
class Sg8bitLauncher extends ElementsDialog {   // ElementsDialog = 退避した native Dialog
    function Sg8bitLauncher() { super.Dialog(); }   // ★必須
    function open(current, decided) {
        // ... showDict(%[ ...machine buttons with close_on_click + vars_on_focus... ])
    }
    function onClose(action) {                       // ★close_on_click はここに来る
        if (action != "" && SG8bitMachineConfig[action] !== void) {
            kag.scflags.MachineType = action;        // 機種確定はこれだけ
            onDecided(action) if (onDecided !== void);
        }
    }
}
```

- ナビ (arrow/pad) → focus 移動、`vars_on_focus` で SPEC ラベル (`text_var`) を
  宣言的に更新 (TJS からの setVar 不要) → 動作 OK。
- Enter/クリック/パッド決定 → `onClose(action=機種id)` → 機種確定 → 動作 OK。
- 残: 全画面化 (上記 4)。
