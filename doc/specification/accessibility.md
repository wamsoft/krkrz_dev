# アクセシビリティ (スクリーンリーダー) 対応 設計 — 吉里吉里Z 接続

状態: **Phase A 実装済み (2026-10-04)**。下の「使い方」が実際の口。以降の節は設計時の記録で、細部は実装と違うところがある (違いは「使い方」の下に列挙)。Elements 側の設計は `external/elements/docs/accessibility.md` にある (この文書では「本体設計」と呼ぶ)。この文書では、krkrz 側の接続と REPL / Agent の拡張だけを扱う。パスは `src/core/` 起点。

## 使い方 (Phase A、実装済み)

| 口 | 内容 |
|---|---|
| ビルド | `KRKRZ_USE_A11Y` (デスクトップ = Windows / macOS / Linux の通常ビルドは既定 ON)。Elements の `elements_a11y_accesskit` をリンクし、`KRKRZ_HAS_A11Y` を立てる。OFF でもツリーの取得 / 操作 / 読み上げログは使える (OS へ出ないだけ) |
| ウィンドウ | 最初の `PaintOverlay` (メインウィンドウのデバイス) でメインウィンドウに付く。SDL3 版は `accesskit_host::attach_sdl`、WINVER は HWND に `attach` (どちらも `SetWindowSubclass` / 表示後の後付け)。スクリーンリーダーが繋がるまでは何もしない |
| ダイアログ | `ElementsDialogManager` の各インスタンスが slot になる。重なり順・モーダル・位置 (`present_scale` / `present_off_x/y`) は `PaintOverlay` の末尾で同期する。画面 JSON の `"a11y"` (本体設計 §4) がそのまま効く |
| `ElementsDialog.announce(text[, assertive])` | 読み上げさせる (最前面ダイアログの live region)。assertive=true は割り込みの指定 (読み上げ側がどう扱うかはスクリーンリーダー次第) |
| `ElementsDialog.a11yActive` | OS のスクリーンリーダー等が接続中か (読み取り専用) |
| `ElementsDialog.a11yMode` | `"auto"` (既定) / `"off"` (OS へ出さない) |
| `ElementsDialog.a11yLabel` | 読み上げツリーの根 (ウィンドウ) の名前。空なら最前面画面の名前 |
| `Agent.a11yTree()` | 表示中ダイアログの読み上げツリー (JSON 文字列)。`{"dialogs":[{"index","screen","modal","tree"}]}` |
| `Agent.a11yLog([since])` | 読み上げログ `%[lines, next]`。REPL が動いているときだけ溜まる。announce もここに残る |
| `Agent.a11yAction(node, action[, arg])` | スクリーンリーダーと同じ経路で操作する (click / focus / increment / decrement / set_value) |
| REPL | `.a11y` / `.a11ylog [N]` / `.a11ydo <node> <action> [arg]` / `.say <text>` (file / web / socket / console 共通) |

設計時からの変更:

- TJS の口は新しい `Accessibility` クラスではなく、既存の `ElementsDialog` の静的メンバにした (`language` などと同じ形)。
- WINVER も `TTVPWindowForm::Proc` を触らず、HWND を後からサブクラス化する (Elements 側の `accesskit_host::attach`)。
- Phase B (Layer のフォーカス連鎖 / ゲーム本体の source / `ElementsPanel`) と Phase C は未着手。

確認: SDL3 版 / WINVER 版とも、`data/elements_gallery` を開いて UI Automation の外部クライアントでツリー (名前・ロール・値・状態)、REPL の `.a11ydo` / `.say` / `.a11ylog` を確認した。

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

### KAG 連携 (opt-in スクリプト)

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
| A | SDL3 / WINVER のメインウィンドウへの接続、ElementsDialog の source 化、TJS の `Accessibility`、REPL の追加。全 `data/elements_*` のサンプルを NVDA で確認 |
| B | ゲーム本体の source (Layer フォーカス連鎖、`hint` を名前に、`focused` を focus に、`ElementsPanel`)、KAG 拡張スクリプト |
| C | `showModalJson` の専用ウィンドウ、複数 Window、macOS / Linux 実機での確認 |
