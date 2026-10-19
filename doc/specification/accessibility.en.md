---
source_hash: 483d0edc0871
---

# Accessibility (Screen Reader) Support Design: Kirikiri Z Integration

Status: **Phases A and B implemented (2026-10-04)**. Character-, word- and line-level reading of input fields (Elements Phase 5) is also in. Verified on real hardware on Windows (SDL3 / WINVER), macOS and Linux. The "Usage" section below describes the actual interface. The sections after it are design-time records, and some details differ from the implementation (the differences are listed under "Usage"). The Elements-side design is in `external/elements/docs/accessibility.md` (referred to in this document as the "core design"). This document covers only the krkrz-side integration and the REPL / Agent extensions. Paths are relative to `src/core/`.

Usage guide: [Screen reader](../guide/Accessibility.md). A working example is the core demo `data/a11y`.

API reference: [ElementsDialog](../reference/ElementsDialog.md) (`announce` / `setGameA11y` / `a11yLayers` and more), [Agent](../reference/Agent.md) (`a11yTree` / `a11yLog` / `a11yAction`), [Layer](../reference/Layer.md) (members you add to a Layer).

## Usage (implemented)

| Interface | Description |
|---|---|
| Build | `KRKRZ_USE_A11Y` (ON by default for regular desktop builds: Windows / macOS / Linux). Links Elements' `elements_a11y_accesskit` and defines `KRKRZ_HAS_A11Y`. Even when OFF, getting the tree, performing actions and the speech log still work (nothing is exposed to the OS) |
| Window | Attached to the main window on the first `PaintOverlay` (for the main window's device). The SDL3 build uses `accesskit_host::attach_sdl`; WINVER calls `attach` on the HWND (both via `SetWindowSubclass`, attached after the window is shown). Does nothing until a screen reader connects |
| Game slot | Placed when the OS interface is opened (permanent). It sits below dialogs and is hidden while a modal dialog is shown. An empty live region (status) is placed from the start, and `announce` changes its content (screen readers may not read a live region that appears later already containing text) |
| Dialogs | Each `ElementsDialogManager` instance becomes a slot. Stacking order, modality and position (`present_scale` / `present_off_x/y`) are synchronized at the end of `PaintOverlay`. The screen JSON's `"a11y"` (core design §4) takes effect as is |
| `ElementsDialog.announce(text[, assertive])` | Makes the screen reader speak (via the live region of the frontmost dialog, or the game slot's live region if there is no dialog). assertive=true requests an interruption (how it is handled depends on the screen reader). Passing the same text repeatedly still reads it. Accepted even when no screen reader is connected (the latest state is delivered once one connects) |
| `ElementsDialog.setGameA11y(nodes[, focus])` | Puts the game's own UI (choices / menus / settings screens drawn on Layers) into the accessibility tree. See "Game nodes" below |
| `ElementsDialog.clearGameA11y()` | Removes all game nodes (the slot and live region remain) |
| `ElementsDialog.onGameA11yAction(id, action, arg)` | Event that receives AT actions on game nodes (assign a function from script) |
| `ElementsDialog.a11yLayers` | Automatically puts the main window's Layers into the accessibility tree (default false). See "Automatic Layers" below |
| `ElementsDialog.a11yActive` | Whether an OS screen reader or similar is connected (read-only). Becomes true when a screen reader first queries the tree (on Windows, when the window comes to the front / gains focus; still false right after startup) |
| `ElementsDialog.onA11yActiveChanged(active)` | Called when `a11yActive` changes (assign a function from script; called outside rendering, and immediately even on a static WINVER screen). Do not cache the "read the text if connected" decision; use this event or check `a11yActive` right before speaking |
| `ElementsDialog.a11yMode` | `"auto"` (default) / `"off"` (not exposed to the OS) |
| `ElementsDialog.a11yLabel` | Name of the accessibility tree root (the window). If empty, the name of the frontmost screen |
| `Agent.a11yTree()` | The accessibility tree (JSON string). `{"dialogs":[{"index","screen","modal","tree"}],"game":{"hidden","tree"}}`. `game` is the game slot (`null` if none; `hidden` indicates whether it is hidden under a modal dialog) |
| `Agent.a11yLog([since])` | The speech log `%[lines, next]`. Accumulated only while the REPL is running. announce calls are recorded here too |
| `Agent.a11yAction(node, action[, arg])` | Performs an action through the same path as a screen reader (click / focus / increment / decrement / set_value). Searches from the frontmost dialog, and also searches game nodes if there is no modal dialog |
| REPL | `.a11y` / `.a11ylog [N]` / `.a11ydo <node> <action> [arg]` / `.say <text>` (common to file / web / socket / console) |

### Input fields

Dialog input fields (`input_box` / `text_box`) can be read by character, word and line by a screen reader, and caret movement can be followed (UIA TextPattern / AT-SPI Text and EditableText / macOS AXSelectedTextRange and AXStringForRange). The screen reader can also move the caret and selection. Nothing is required from script.

- When only the caret moves without the value changing, the speech log shows `[caret] x` (`(line end)` at the end of a line, `(end)` at the end of the text); when text is selected, it shows `[selected] <text>`.
- IME composition strings (not yet committed) are not handled. The OS IME itself conveys the composing text and candidates to the screen reader, so exposing them from the application as well would make them read twice. Input fields hold only committed text (core design §6.5).
- The game's `EditLayer` (`a11yLayers`) and `text_input` in `setGameA11y` only expose the value; there is no character-level reading.

### Game nodes (`setGameA11y`)

UI drawn on Layers is outside Elements, so the script passes a table of nodes. Each call replaces the whole set, and the engine computes the differences.

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

| Key | Description |
|---|---|
| `id` | Required. A unique string. `Agent.a11yAction` / `.a11ydo` also refer to nodes by this id |
| `role` | `button` / `toggle_button` / `check_box` / `radio_button` / `tab` / `menu_item` / `list` / `list_item` / `slider` / `spin_button` / `text_input` / `label` / `heading` / `image` / `status` / `group` (group if omitted) |
| `name` / `value` / `description` | Name / value / supplementary description to be read |
| `states` | An array or `"focusable,checked"`. `focusable` / `disabled` / `checked` / `selected` / `expanded` / `read_only`. `focused` is determined by the second argument |
| `rect` | `[x, y, w, h]` in primary layer coordinates. Optional (a node without it gets the rectangle enclosing its children). The engine converts for window scaling and letterboxing |
| `parent` | The parent's `id`. Top level if omitted |
| `num_value` / `num_min` / `num_max` / `num_step` | Numeric values for slider / spin_button |

- Available actions are determined by the role. Pressable roles (button / check_box / list_item ...) get click; slider / spin_button get increment / decrement / set_value; text_input gets set_value. All accept focus, and a `disabled` node accepts only focus.
- AT actions arrive at `onGameA11yAction` outside rendering (called on the main thread regardless of which thread they come from). The engine does not move the focus or change values on its own. The script changes the game state and calls `setGameA11y` again.
- Stacking order: the game slot is below dialogs. However, when no dialog is receiving keys and the focus is on the game side, it is raised to the front (because the screen reader takes the focus from the topmost slot). It is hidden while a modal dialog is shown.
- Main window only.

### Automatic Layers (`a11yLayers`)

Setting `ElementsDialog.a11yLayers = true` traverses the main window's primary layer and its descendants and adds nodes to the game slot. The default is false (behavior is unchanged unless you opt in). If the default is ever changed to true, users who build their trees with `setGameA11y` without using this feature must be notified in advance.

Included:

- Layers in the focus chain (`focusable` and `joinFocusChain`). The name is `hint`; the role is button (`CheckBoxLayer` is check_box, `EditLayer` is text_input)
- Layers that have `a11yName` or `a11yRole` (they need not be focusable; useful for headings and descriptive text)
- Layers that draw an ElementsPanel. The widgets in the panel are placed beneath it, and actions are delivered to the panel

Excluded: Layers whose `visible` is false and their children. Layers whose `a11yHidden` is true and their children (set it on layers you expose yourself via `setGameA11y`).

Members you add to a Layer (all optional):

| Member | Description |
|---|---|
| `a11yName` / `a11yRole` / `a11yValue` / `a11yDescription` | Name / role (same names as in `setGameA11y`) / value / supplementary description |
| `a11yStates` | An array or `"checked,selected"`. `disabled` is also derived from `enabled` |
| `a11yHidden` | If true, the whole subtree is excluded |
| `onA11yAction(action, arg)` | Receives AT actions. Returning false also runs the default handling |

- Default handling: focus calls `layer.focus()`; click focuses the layer and then sends the Enter key (keyboard-operable widgets can be pressed this way). Value changes (increment / set_value, etc.) are received only through `onA11yAction`.
- Focus: `window.focusedLayer`. However, when a focus is passed to `setGameA11y`, that takes precedence.
- Order: `setGameA11y` nodes come first, followed by the automatic Layers (in Layer stacking order). The id is `layer:<Layer.name>` (duplicate names get `#2`, `#3` ...).
- Read frequency: at most once every 150 ms (immediately when the focused Layer changes). Reading happens only while an AT is connected or while the REPL speech log is being collected, and is done outside rendering (in the continuous event). If you implement `a11y*` as property getters, keep them lightweight. `Agent.a11yTree` / `Agent.a11yAction` re-read on the spot.
- On WINVER, while an AT is connected, the continuous event keeps running for this re-reading (it also wakes up when idle).

Changes since the design:

- The TJS interface is not a new `Accessibility` class but static members of the existing `ElementsDialog` (in the same form as `language` and others).
- WINVER also leaves `TTVPWindowForm::Proc` untouched and subclasses the HWND afterward (Elements' `accesskit_host::attach`).
- Coordinates: coordinates on the drawing surface (the renderer's surface) are converted to OS units by the ratio between the surface and the window's actual size. On macOS this is points × `backingScaleFactor` (2 on Retina even if the SDL window is not high-DPI; Elements' `accesskit_host::native_scale`); on Linux, window coordinates.
- The Phase B game source was split into two: `setGameA11y`, where the script passes a node table, and `a11yLayers`, which reads the Layer focus chain automatically (including ElementsPanel). Phase C has not been started. The KAG3 extension ("KAG integration" below) will not be done (because KAG3 itself is not going to be extended further; KAG-based titles support accessibility by calling `setGameA11y` / `announce` from their own scripts).

Verified (automatic Layers): on Windows (SDL3 / WINVER) / macOS / Linux, we verified focus-chain Layers, overriding with `a11yName` / `a11yRole`, exclusion via `a11yHidden` and invisibility, ElementsPanel contents, combined use with `setGameA11y` (ordering and focus precedence), and click (Enter) and `onA11yAction` from the AT / `Agent.a11yAction`.

Verified: on both the SDL3 and WINVER builds, we opened `data/elements_gallery` and checked the tree (names, roles, values, states) with an external UI Automation client, as well as the REPL's `.a11ydo` / `.say` / `.a11ylog`. For game nodes, we likewise verified the tree and coordinates (including letterbox), UIA Invoke / SelectionItem.Select / RangeValue.SetValue → `onGameA11yAction`, hiding while a modal is shown, announce when there is no dialog, and operation on a WINVER screen whose rendering has stopped.

## 1. Current state (investigation results)

- There is no accessibility, UIA or TTS code. No WndProc handles `WM_GETOBJECT`; it falls through to DefWindowProc.
- **All Elements UI is drawn offscreen.**
  - For `ElementsDialog`, `tTVPElementsDialogManager` manages `overlay_session`s in z-order, and `PaintOverlay` (`common/visual/elements/ElementsDialogManager.cpp`) composites them onto the game frame.
  - `ElementsPanel` draws into a Layer's bitmap.
  - The only exception is `showModalJson(json,title,w,h)`, which creates a dedicated OS window (SDL: `SDLElementsModalRunner.cpp`; WINVER: `ModalWndProc` in `WinElementsModalRunner.cpp`).
- Hooks into the native window:
  - WINVER: `TTVPWindowForm::Proc` (`win32/environ/WindowFormUnit.cpp`) calls `DeliverMessageToReceiver` first. `WM_GETOBJECT` can be caught here.
  - SDL3: the window is created in `sdl3/environ/form.cpp`. The HWND can be obtained via `SDL_PROP_WINDOW_WIN32_HWND_POINTER` (there is a precedent in the same file). The properties for macOS / Linux are unused.
- The existing introspection of internal structures is insufficient as a substitute for a tree.
  - `Agent.dialogs()` / `Agent.dialogTree(i)` use `overlay_session::list_widgets()`. They return only a flat `(id,type,value)` for widgets that have an `id`, with no names, rectangles or hierarchy.
  - To be replaced by the core design's `a11y_snapshot()`.
- Layers have a complete focus chain consisting of `focusable` / `joinFocusChain` / `focused` / `hint` / `onFocus`. KAG's `ButtonLayer` / `MessageLayer` links / `CheckBoxLayer` / `EditLayer` use it. This is in scope for Phase B.
- The REPL is `tTVPReplThread::ProcessLine` in `common/utils/REPL.cpp`, shared by the file / web / socket / console channels. `.dlg` / `.click` are implemented by rewriting the input into `Agent.*` calls.

## 2. Architecture

```
             ┌──────────── tTVPAccessibility (新規, common/visual/accessibility/) ─────────────┐
 OS AT  ⇄  accesskit_host (Elements L3)                                                   │
             │  slot 0     : ゲーム本体 source (tTVPGameA11ySource: 場面名・Layer フォーカス連鎖) │
             │  slot 1..N  : ElementsDialogManager の各 overlay_session (z 順, modal 連動)      │
             └──────────────────────────────────────────────────────────────────────────────┘
 TJS:  Accessibility クラス (announce / mode / active / onActive)
 REPL: Agent.a11yTree / a11yLog / a11yAction, .a11y / .a11ylog / .say
```

(In the diagram: slot 0 is the game source (`tTVPGameA11ySource`: scene name and Layer focus chain); slots 1..N are each `overlay_session` of `ElementsDialogManager` (in z-order, tied to modality).)

- `KRKRZ_USE_A11Y` (default: same as `KRKRZ_USE_ELEMENTS`) is linked to Elements' `ELEMENTS_A11Y_ACCESSKIT`. OFF for the LIB variant, NX and similar.
- Even when OFF, `Agent.a11yTree()` alone works with Elements L0–L2 (so it can be tested without AccessKit).

## 3. Attaching to the window

| Build | Attachment |
|---|---|
| SDL3 (Win / mac / Linux) | `accesskit_host::attach_sdl(window)` right after the window is created in `form.cpp`. For Linux, focus and bounds are notified via window events in `SDL_AppEvent` |
| WINVER | When `TTVPWindowForm::Proc` receives `WM_GETOBJECT`, call `on_wm_getobject()`; on `WM_ACTIVATE`, call `on_window_focus()`. Handled directly in the core, not through a plugin message receiver |
| Dedicated window of `showModalJson` | Phase C. Attach a separate `accesskit_host` to the dedicated window as well (the `run_modal` side uses the same processing as the engine's Win32 / SDL host) |

- There can be multiple main windows (multiple `Window`s can be created). Therefore an `accesskit_host` is held per Window, and each Elements instance registers with the host of "the Window it is drawn on".
- The root node's name is `Window.caption`.

## 4. Making ElementsDialog a source (`ElementsDialogManager`)

- Call `add_source` / `remove_source` when an instance is created / destroyed. When the z-order, `modal` or `active` changes, synchronize `set_modal` and z.
- Coordinates: right after `PaintOverlay` finalizes `last_rect` in surface logical coordinates, call `set_transform` with the surface → client pixel transform. This transform is shared with the IME transform in `GetTextInputArea`.
- Connect `overlay_session::set_a11y_dirty_callback` to `invalidate()`.
- `ElementsPanel` (drawn on a Layer) is handled in Phase B. It is attached as a child of the game source, following the Layer's coordinates and visibility.

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

- An `"a11y"` key written in ElementsDialog JSON / Dictionary (core design §4.1) takes effect as is, with no extra work.
- When `active` is false, `announce` only records to the speech log and returns immediately.

### KAG integration (opt-in script): not done

> This was a design-time proposal. Since KAG3 is no longer going to be extended, it will not be added to `script/KAG3`. KAG-based titles pass the text to `ElementsDialog.announce` and expose choices and the like via `setGameA11y` from their own scripts (some titles actually do this).

KAG's own .tjs files are not modified. An extension `system/A11yKAG.tjs` is provided and enabled with `kag.a11y.messages = true`.

- When `MessageLayer` finishes displaying a line or a page, the accumulated text is passed to `Accessibility.announce(name + "「" + text + "」")`. It uses the same text that is pushed to `HistoryLayer`, so ruby and tags are already removed.
- When the focus moves to a choice (link), its `hint` is read. Once the Layer chain becomes a source in Phase B it will be read automatically, so this is a stopgap until then.
- Lines with voice can be skipped depending on a setting: `kag.a11y.skipVoiced`

## 6. REPL / Agent

The existing `dialogTree` is kept as is.

| Addition | Implementation |
|---|---|
| `Agent.a11yTree([window])` | Returns the combined tree (all slots) held by the Window's host as a Dictionary in the format of core design §5. Specifying `index` returns only that dialog's source |
| `Agent.a11yLog([since])` | An array of speech log entries (an approximate one-line form for focus, value changes, live regions and announce) |
| `Agent.a11yAction(nodeId, action[, arg])` | Performs the action through the same path as an action from an AT (`accesskit_host` → `source::perform`) |
| `.a11y` / `.a11ylog` / `.say <text>` | Added to the rewrite block in `ProcessLine`, and added to the help lines. Usable on all channels: file / web / socket / console |
| web `/a11y`, SSE `/sub/a11y` | Native routes of `ReplWebServer`. The panel-style UI shares the tree view and speech log view with the A11y tab of elements_console |

Unlike `Agent.dialogClick`, `Agent.a11yAction` executes without going through synthesized keys. This makes it possible to test the AT action path itself.

## 7. Phases

| Phase | Content |
|---|---|
| A (done) | Attaching to the SDL3 / WINVER main window, making ElementsDialog a source, the TJS interface (static members of `ElementsDialog`), REPL additions |
| B (done) | The game source (`setGameA11y`, and `a11yLayers`, which reads the Layer focus chain / `hint` / `focusedLayer` / `ElementsPanel`). The KAG extension script will not be done |
| C | The dedicated window of `showModalJson`, multiple Windows (verification on real macOS / Linux hardware was completed together with A / B) |

Character-, word- and line-level reading of input fields is done on the Elements side (core design §6.5). IME composition strings are intentionally not handled (see "Input fields" above). What remains is Phase C. The index is the umbrella's `TODO.md`.
