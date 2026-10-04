# アクセシビリティ (スクリーンリーダー) 対応 設計 — 吉里吉里Z 接続

状態: **Phase A / B 実装済み (2026-10-04)**。Windows (SDL3 / WINVER)・macOS・Linux の実機で確認した。下の「使い方」が実際の口。以降の節は設計時の記録で、細部は実装と違うところがある (違いは「使い方」の下に列挙)。Elements 側の設計は `external/elements/docs/accessibility.md` にある (この文書では「本体設計」と呼ぶ)。この文書では、krkrz 側の接続と REPL / Agent の拡張だけを扱う。パスは `src/core/` 起点。

## 使い方 (実装済み)

| 口 | 内容 |
|---|---|
| ビルド | `KRKRZ_USE_A11Y` (デスクトップ = Windows / macOS / Linux の通常ビルドは既定 ON)。Elements の `elements_a11y_accesskit` をリンクし、`KRKRZ_HAS_A11Y` を立てる。OFF でもツリーの取得 / 操作 / 読み上げログは使える (OS へ出ないだけ) |
| ウィンドウ | 最初の `PaintOverlay` (メインウィンドウのデバイス) でメインウィンドウに付く。SDL3 版は `accesskit_host::attach_sdl`、WINVER は HWND に `attach` (どちらも `SetWindowSubclass` / 表示後の後付け)。スクリーンリーダーが繋がるまでは何もしない |
| ゲーム本体の slot | OS への口を開いた時点で置く (常設)。ダイアログより下で、モーダルなダイアログの表示中は隠れる。空の live region (status) を最初から置いておき、`announce` で中身を変える (文字の入った live region が後から現れると、スクリーンリーダーは読まないことがある) |
| ダイアログ | `ElementsDialogManager` の各インスタンスが slot になる。重なり順・モーダル・位置 (`present_scale` / `present_off_x/y`) は `PaintOverlay` の末尾で同期する。画面 JSON の `"a11y"` (本体設計 §4) がそのまま効く |
| `ElementsDialog.announce(text[, assertive])` | 読み上げさせる (最前面ダイアログの live region。ダイアログが無ければゲーム本体の slot の live region)。assertive=true は割り込みの指定 (読み上げ側がどう扱うかはスクリーンリーダー次第)。同じ文を続けて渡しても読む。スクリーンリーダーが繋がっていなくても受け付ける (繋がったら最新の状態が渡る) |
| `ElementsDialog.setGameA11y(nodes[, focus])` | ゲーム本体 (Layer に描いた選択肢 / メニュー / 設定画面) を読み上げツリーに載せる。下の「ゲーム本体のノード」を参照 |
| `ElementsDialog.clearGameA11y()` | ゲーム本体のノードを全て外す (slot と live region は残る) |
| `ElementsDialog.onGameA11yAction(id, action, arg)` | ゲーム本体のノードへの AT の操作を受けるイベント (スクリプトで関数を代入する) |
| `ElementsDialog.a11yLayers` | メインウィンドウの Layer を読み上げツリーに自動で載せる (既定 false)。下の「Layer の自動」を参照 |
| `ElementsDialog.a11yActive` | OS のスクリーンリーダー等が接続中か (読み取り専用)。スクリーンリーダーが初めてツリーを問い合わせた時点で真になる (Windows はウィンドウが前面 / フォーカスになったとき。起動直後はまだ偽) |
| `ElementsDialog.onA11yActiveChanged(active)` | `a11yActive` が変わったときに呼ばれる (スクリプトで関数を代入する。描画の外、WINVER の静止画面でも即時)。「繋がっていたら本文を読ませる」判定はキャッシュせず、これか読む直前の `a11yActive` で行う |
| `ElementsDialog.a11yMode` | `"auto"` (既定) / `"off"` (OS へ出さない) |
| `ElementsDialog.a11yLabel` | 読み上げツリーの根 (ウィンドウ) の名前。空なら最前面画面の名前 |
| `Agent.a11yTree()` | 読み上げツリー (JSON 文字列)。`{"dialogs":[{"index","screen","modal","tree"}],"game":{"hidden","tree"}}`。`game` はゲーム本体の slot (無ければ `null`、`hidden` はモーダルなダイアログの下で隠れているか) |
| `Agent.a11yLog([since])` | 読み上げログ `%[lines, next]`。REPL が動いているときだけ溜まる。announce もここに残る |
| `Agent.a11yAction(node, action[, arg])` | スクリーンリーダーと同じ経路で操作する (click / focus / increment / decrement / set_value)。最前面のダイアログから探し、モーダルなダイアログが無ければゲーム本体のノードも探す |
| REPL | `.a11y` / `.a11ylog [N]` / `.a11ydo <node> <action> [arg]` / `.say <text>` (file / web / socket / console 共通) |

### ゲーム本体のノード (`setGameA11y`)

Layer に描いた UI は Elements の外なので、スクリプトがノードの表を渡す。呼ぶたびに丸ごと差し替え、差分は本体が取る。

```
ElementsDialog.onGameA11yAction = function(id, action, arg) {
    // action: "click" / "focus" / "increment" / "decrement" / "set_value" (arg が値)
    // focus を受けたら、 ゲーム側のフォーカスを動かして setGameA11y を呼び直す
};
ElementsDialog.setGameA11y([
    %[ id:"choices", role:"list", name:"選択肢" ],
    %[ id:"c1", role:"list_item", name:"北へ行く", parent:"choices", rect:[100,400,600,48] ],
    %[ id:"c2", role:"list_item", name:"南へ行く", parent:"choices", rect:[100,460,600,48] ],
    %[ id:"vol", role:"slider", name:"音量", value:"50%", num_value:50, num_min:0, num_max:100 ],
], "c1");
```

| キー | 内容 |
|---|---|
| `id` | 必須。一意な文字列。`Agent.a11yAction` / `.a11ydo` もこの id で指す |
| `role` | `button` / `toggle_button` / `check_box` / `radio_button` / `tab` / `menu_item` / `list` / `list_item` / `slider` / `spin_button` / `text_input` / `label` / `heading` / `image` / `status` / `group` (省略で group) |
| `name` / `value` / `description` | 読み上げる名前 / 値 / 補足説明 |
| `states` | 配列か `"focusable,checked"`。`focusable` / `disabled` / `checked` / `selected` / `expanded` / `read_only`。`focused` は第 2 引数で決める |
| `rect` | primary layer の座標 `[x, y, w, h]`。省略可 (省略したノードは子を囲む矩形になる)。ウィンドウの拡縮とレターボックスは本体が換算する |
| `parent` | 親の `id`。省略すると最上位 |
| `num_value` / `num_min` / `num_max` / `num_step` | slider / spin_button の数値 |

- 操作はロールから決まる。押せるもの (button / check_box / list_item …) は click、slider / spin_button は increment / decrement / set_value、text_input は set_value。どれも focus を受け、`disabled` なら focus だけ。
- AT の操作は描画の外で `onGameA11yAction` に届く (どのスレッドから来ても、メインスレッドで呼ぶ)。本体はフォーカスや値を自分では動かさない。スクリプトがゲームの状態を変えて `setGameA11y` を呼び直す。
- 重なり順: ゲーム本体の slot はダイアログより下。ただし、キーを受けているダイアログが無く、ゲーム側にフォーカスがあるときは最前面に上げる (スクリーンリーダーのフォーカスはいちばん上の slot のものが採られるため)。モーダルなダイアログの表示中は隠れる。
- メインウィンドウのみ。

### Layer の自動 (`a11yLayers`)

`ElementsDialog.a11yLayers = true` にすると、メインウィンドウの primary layer 以下を辿って、ゲーム本体の slot にノードを足す。既定は false (何もしなければ動作は変わらない)。既定を true に変える場合は、この機能を使わずに `setGameA11y` で組んでいる利用側へ事前に知らせる。

載るもの:

- フォーカス連鎖に入っている Layer (`focusable` かつ `joinFocusChain`)。名前は `hint`、ロールは button (`CheckBoxLayer` は check_box、`EditLayer` は text_input)
- `a11yName` か `a11yRole` を持つ Layer (フォーカスできなくてもよい。見出しや説明文に)
- ElementsPanel を描いている Layer。パネルの中の部品がその下に並び、操作もパネルへ届く

載らないもの: `visible` が false の Layer とその子。`a11yHidden` が真の Layer とその子 (自前で `setGameA11y` に載せるレイヤに立てる)。

Layer に生やして使うメンバ (どれも任意):

| メンバ | 内容 |
|---|---|
| `a11yName` / `a11yRole` / `a11yValue` / `a11yDescription` | 名前 / ロール (`setGameA11y` と同じ名前) / 値 / 補足説明 |
| `a11yStates` | 配列か `"checked,selected"`。`disabled` は `enabled` からも付く |
| `a11yHidden` | 真なら部分木ごと外す |
| `onA11yAction(action, arg)` | AT の操作を受ける。false を返すと既定の処理も行う |

- 既定の処理: focus は `layer.focus()`、click はフォーカスしてから Enter キーを送る (キー操作できる部品はこれで押せる)。値の変更 (increment / set_value など) は `onA11yAction` でしか受けない。
- フォーカス: `window.focusedLayer`。ただし `setGameA11y` に focus を渡しているときはそちらが優先する。
- 並び順: `setGameA11y` のノードが先、自動の Layer が後 (Layer の重なり順)。id は `layer:<Layer.name>` (同名は `#2`, `#3` …)。
- 読む頻度: 150ms に 1 回まで (フォーカス中の Layer が変わったら即時)。読むのは AT が繋がっている間か、REPL の読み上げログを取っている間だけで、描画の外 (continuous イベント) で読む。`a11y*` を property の getter にしているなら軽く保つこと。`Agent.a11yTree` / `Agent.a11yAction` はその場で読み直す。
- WINVER で AT が繋がっている間は、この読み直しのために continuous イベントが回り続ける (アイドル時も起きる)。

設計時からの変更:

- TJS の口は新しい `Accessibility` クラスではなく、既存の `ElementsDialog` の静的メンバにした (`language` などと同じ形)。
- WINVER も `TTVPWindowForm::Proc` を触らず、HWND を後からサブクラス化する (Elements 側の `accesskit_host::attach`)。
- 座標: 描画面 (renderer の surface) の座標を、描画面とウィンドウの実寸の比で OS の単位へ換算する。macOS はポイント × `backingScaleFactor` (SDL のウィンドウが高解像度でなくても Retina なら 2。Elements の `accesskit_host::native_scale`)、Linux はウィンドウ座標。
- Phase B のゲーム本体の source は 2 段にした。スクリプトがノードの表を渡す `setGameA11y` と、Layer のフォーカス連鎖を自動で読む `a11yLayers` (ElementsPanel を含む)。Phase C は未着手。KAG3 の拡張 (下の「KAG 連携」) は行わない (KAG3 自体を今後拡張しない方針のため。KAG 系の作品は、作品側のスクリプトから `setGameA11y` / `announce` を呼んで対応する)。

確認 (Layer の自動): Windows (SDL3 / WINVER) / macOS / Linux で、フォーカス連鎖の Layer、`a11yName` / `a11yRole` の上書き、`a11yHidden` と非表示の除外、ElementsPanel の中身、`setGameA11y` との併用 (並び順・focus の優先)、AT / `Agent.a11yAction` からの click (Enter) と `onA11yAction` を確認した。

確認: SDL3 版 / WINVER 版とも、`data/elements_gallery` を開いて UI Automation の外部クライアントでツリー (名前・ロール・値・状態)、REPL の `.a11ydo` / `.say` / `.a11ylog` を確認した。ゲーム本体のノードも同じく、ツリーと座標 (letterbox 込み)、UIA の Invoke / SelectionItem.Select / RangeValue.SetValue → `onGameA11yAction`、モーダル表示中に隠れること、ダイアログが無いときの announce、WINVER の描画が止まった画面での操作を確認した。

## 1. 現状 (調査結果)

- アクセシビリティ、UIA、TTS 関連のコードはない。どの WndProc も `WM_GETOBJECT` を処理せず、DefWindowProc に流している。
- **Elements の UI はすべてオフスクリーン**で描かれる。
  - `ElementsDialog` は `tTVPElementsDialogManager` が `overlay_session` を z 順に管理し、`PaintOverlay` (`common/visual/elements/ElementsDialogManager.cpp`) でゲームのフレームに合成する。
  - `ElementsPanel` は Layer のビットマップに描く。
  - 例外は `showModalJson(json,title,w,h)` だけで、これは専用の OS ウィンドウを作る (SDL: `SDLElementsModalRunner.cpp`、WINVER: `WinElementsModalRunner.cpp` の `ModalWndProc`)。
- ネイティブウィンドウへの接続口:
  - WINVER: `TTVPWindowForm::Proc` (`win32/environ/WindowFormUnit.cpp`) が最初に `DeliverMessageToReceiver` を呼ぶ。ここで `WM_GETOBJECT` を捕まえられる。
  - SDL3: `sdl3/environ/form.cpp` でウィンドウを作っている。HWND は `SDL_PROP_WINDOW_WIN32_HWND_POINTER` で取得できる (同じファイルに前例あり)。macOS / Linux 用のプロパティは未使用。
- 既存の内部構造の観察 (introspection) は、ツリーの代わりとしては不足している。
  - `Agent.dialogs()` / `Agent.dialogTree(i)` は `overlay_session::list_widgets()` を使う。返るのは `id` を持つウィジェットの平坦な `(id,type,value)` だけで、名前・矩形・階層がない。
  - 本体設計の `a11y_snapshot()` で置き換える。
- Layer には `focusable` / `joinFocusChain` / `focused` / `hint` / `onFocus` からなる完全なフォーカス連鎖がある。KAG の `ButtonLayer` / `MessageLayer` のリンク / `CheckBoxLayer` / `EditLayer` が使っている。ここは Phase B の対象にする。
- REPL は `common/utils/REPL.cpp` の `tTVPReplThread::ProcessLine` で、file / web / socket / console の各チャネルに共通。`.dlg` / `.click` は `Agent.*` への文字列書き換えで実装されている。

## 2. 構成

```
             ┌──────────── tTVPAccessibility (新規, common/visual/accessibility/) ─────────────┐
 OS AT  ⇄  accesskit_host (Elements L3)                                                   │
             │  slot 0     : ゲーム本体 source (tTVPGameA11ySource: 場面名・Layer フォーカス連鎖) │
             │  slot 1..N  : ElementsDialogManager の各 overlay_session (z 順, modal 連動)      │
             └──────────────────────────────────────────────────────────────────────────────┘
 TJS:  Accessibility クラス (announce / mode / active / onActive)
 REPL: Agent.a11yTree / a11yLog / a11yAction, .a11y / .a11ylog / .say
```

- `KRKRZ_USE_A11Y` (既定は `KRKRZ_USE_ELEMENTS` と同じ) と Elements の `ELEMENTS_A11Y_ACCESSKIT` を連動させる。LIB 変種と NX などでは OFF。
- OFF の場合でも、`Agent.a11yTree()` だけは Elements の L0〜L2 で動く (AccessKit なしで検証できる)。

## 3. ウィンドウへの接続

| ビルド | 接続 |
|---|---|
| SDL3 (Win / mac / Linux) | `form.cpp` でウィンドウを作った直後に `accesskit_host::attach_sdl(window)`。Linux 向けには `SDL_AppEvent` のウィンドウイベントで focus と bounds を通知する |
| WINVER | `TTVPWindowForm::Proc` で `WM_GETOBJECT` を受けたら `on_wm_getobject()`。`WM_ACTIVATE` で `on_window_focus()`。プラグインの message receiver ではなく、コア内で直接処理する |
| `showModalJson` の専用ウィンドウ | Phase C。専用ウィンドウにも別の `accesskit_host` を付ける (`run_modal` 側で本体の Win32 / SDL ホストと同じ処理を使う) |

- メインウィンドウは複数ありうる (`Window` を複数生成できる)。そこで `accesskit_host` は Window ごとに持ち、Elements の各インスタンスは「そのインスタンスが描かれる Window」の host に登録する。
- root ノードの名前は `Window.caption` を使う。

## 4. ElementsDialog の source 化 (`ElementsDialogManager`)

- インスタンスの生成・破棄で `add_source` / `remove_source` を呼ぶ。z 順の入れ替え、`modal`、`active` が変わったら `set_modal` と z を同期する。
- 座標: `PaintOverlay` がサーフェス論理座標の `last_rect` を確定させた直後に、サーフェス → クライアントピクセルの変換で `set_transform` を呼ぶ。この変換は `GetTextInputArea` の IME 用変換と同じものを共有する。
- `overlay_session::set_a11y_dirty_callback` を `invalidate()` につなぐ。
- `ElementsPanel` (Layer に描く) は Phase B で扱う。Layer の座標と可視性に従って、ゲーム本体の source の子として接ぐ。

## 5. TJS API

```
class Accessibility  // static
{
  property mode;        // "auto"(既定: AT 接続時のみ) / "on" / "off"
  property active;      // read-only: OS の AT が接続中か
  property gameLabel;   // ゲーム本体ノードの名前 (場面名など)
  function announce(text, assertive=false, window=void);
  // event
  onActiveChanged(active);   // System.addEventListener 相当で受ける (TVPPostEvent)
}
```

- ElementsDialog の JSON / Dictionary に書いた `"a11y"` キー (本体設計 §4.1) は、何もしなくてもそのまま効く。
- `active` が false のときは、`announce` は読み上げログへの記録だけ行い、すぐ戻る。

### KAG 連携 (opt-in スクリプト) — 行わない

> 設計時の案。KAG3 は今後拡張しない方針になったので、`script/KAG3` には入れない。KAG 系の作品は、作品側のスクリプトで本文を `ElementsDialog.announce` に渡し、選択肢などを `setGameA11y` で載せる (実際にそうしている作品がある)。

KAG 本体の .tjs は変更しない。拡張 `system/A11yKAG.tjs` を用意し、`kag.a11y.messages = true` で有効にする。

- `MessageLayer` で 1 行または 1 ページの表示が終わったら、蓄積した文字列を `Accessibility.announce(name + "「" + text + "」")` に渡す。`HistoryLayer` に積む文字列と同じものを使うので、ルビとタグは除いた状態になる。
- 選択肢 (リンク) にフォーカスが移ったら、その `hint` を読ませる。Phase B で Layer の連鎖を source にすれば自動で読むようになるので、それまでの暫定措置。
- ボイスがある行は、設定によって読まない。`kag.a11y.skipVoiced`

## 6. REPL / Agent

既存の `dialogTree` はそのまま残す。

| 追加 | 実装 |
|---|---|
| `Agent.a11yTree([window])` | Window の host が持つ合成ツリー (全 slot) を本体設計 §5 の形式の Dictionary で返す。`index` を指定するとその dialog の source だけを返す |
| `Agent.a11yLog([since])` | 読み上げログ (focus、value の変化、live、announce の近似 1 行) の配列 |
| `Agent.a11yAction(nodeId, action[, arg])` | AT からのアクションと同じ経路 (`accesskit_host` → `source::perform`) で実行する |
| `.a11y` / `.a11ylog` / `.say <text>` | `ProcessLine` の書き換えブロックに追加し、ヘルプ行にも足す。file / web / socket / console の全チャネルで使える |
| web `/a11y`、SSE `/sub/a11y` | `ReplWebServer` のネイティブ route。panel 系の UI はツリー表示と読み上げログ表示を elements_console の A11y タブと共有する |

`Agent.a11yAction` は `Agent.dialogClick` と違ってキー合成を介さずに実行する。そのため、AT の操作経路そのものを検証できる。

## 7. 段階

| Phase | 内容 |
|---|---|
| A (済) | SDL3 / WINVER のメインウィンドウへの接続、ElementsDialog の source 化、TJS の口 (`ElementsDialog` の静的メンバ)、REPL の追加 |
| B (済) | ゲーム本体の source (`setGameA11y` と、Layer フォーカス連鎖 / `hint` / `focusedLayer` / `ElementsPanel` を読む `a11yLayers`)。KAG 拡張スクリプトは行わない |
| C | `showModalJson` の専用ウィンドウ、複数 Window (macOS / Linux 実機での確認は A / B と一緒に済んだ) |
