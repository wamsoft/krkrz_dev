---
source_hash: f21ded550dcf
---

# Dialogs

## About dialogs

Kirikiri Z has a built-in mechanism for showing dialogs, containing buttons, check boxes, text input, and so on, from a layout written in JSON / Dictionary. From TJS it is used through the [ElementsDialog](../reference/ElementsDialog.md) class (formerly `Dialog`; it was renamed because that generic name tended to clash with class names in game scripts).

These dialogs are implemented by embedding [Elements](https://github.com/wamsoft/elements) (a ThorVG-based C++ GUI library). Unlike platform-specific native dialogs (such as WIN32Dialog on Win32), the same JSON definition produces the same-looking dialog in both the SDL3 build and the native Windows (D3D11) build. You just pass a layout written in JSON / JSONC (JSON with comments), and the engine handles layout calculation, drawing, and input processing.

Because the mechanism aims at a cross-platform UI that does not depend on the standard Windows GUI, it was designed primarily for the SDL3 build, but it works the same way in the WINVER (native Windows) build.

## Display modes

There are "single dialogs", which show one screen, and "flows", which include transitions between multiple screens. Each comes in modal (blocks TJS processing until closed) and non-modal (shown over the game screen without stopping the main loop) variants.

### Single dialogs

| Display mode | TJS API | Behavior |
|---|---|---|
| Non-modal (overlay) | [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) | Draws the dialog over the existing game screen without stopping the main loop. Value changes and button clicks are reported one by one through [onAction](../reference/ElementsDialog.md#onaction). Ends with [close](../reference/ElementsDialog.md#close). |
| Blocking modal (separate window) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) (with title / w / h) | Opens a new native window and blocks until it is closed. On close it returns a Dictionary of the form `%[ action, values ]`. |
| Blocking modal (overlay) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) (JSON argument only) | Shows the dialog over the existing game screen without creating a separate window, and blocks until it is closed. The return value is the same as the separate-window version. |
| Drawing to a host layer (panel) | [ElementsPanel](../reference/ElementsPanel.md) (`new ElementsPanel(layer)` + [showFile](../reference/ElementsPanel.md#showfile), etc.) | **Draws into the bitmap of a specified Layer** instead of an overlay. Z-order, transitions, appearance in screenshots, and input ownership follow the layer mechanism, so use it for HUDs and UI that is part of the game screen. The event / variable APIs have the same shape as ElementsDialog. |

The return value of `showModalJson` / `showModalFile` has this form:

```tjs
%[
    action: <閉じた button の id (Esc / × は "")>,
    values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]
```

[onAction](../reference/ElementsDialog.md#onaction) also fires while modal, but the dialog is closed only by buttons with `"close_on_click": true` in the JSON (and by cancelling with Esc / ×).

### Multi-screen flows

You can also define a "flow" that switches between several screens in sequence. A manifest (or Dictionary) declares the screens and the transitions between them.

| Display mode | TJS API | Behavior |
|---|---|---|
| Blocking (overlay) | [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) | Runs the multi-screen transitions as an overlay. Blocks TJS until the flow ends, then returns `%[ action, values ]` of the last screen closed. |
| Non-modal (resident) | [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) | Starts the same flow definition without blocking (resident on the game screen). Close it with `close`, and check [active](../reference/ElementsDialog.md#active) to tell when teardown (cleanup) has finished. |

[onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave) fire when screens switch, and [onAction](../reference/ElementsDialog.md#onaction) fires when a widget is operated.

#### Screen-switch effects (fade / universal)

Writing a `transitions` entry in the screen JSON in object form declares a transition effect for screen switches. Compositing is done on the CPU, so it behaves identically on every DrawDevice: SDL / WINVER / GL.

```jsonc
"transitions": {
    "next": { "target": "s2", "effect": "fade", "duration": 300 },
    "back": { "target": "<back>", "effect": "universal",
              "rule": "rule.png", "vague": 64, "duration": 500 }
}
```

| Key | Meaning |
|---|---|
| `effect` | `"fade"` = crossfade / `"universal"` = universal transition with a rule image. Unsupported names log a warning and switch immediately |
| `duration` | Duration in ms. Omitted / 0 means 200 ms |
| `rule` | The rule image for universal (grayscale; pixels with smaller values switch to the next screen earlier). Resolution order = relative to the screen that declares the transition → Storages path → autopath search |
| `vague` | Width of the blurred boundary (on the rule value scale 0 to 255, default 64) |

#### Coordinating with exit animations

Adding `"on": "exit"` to an element's `"animate"` plays an exit animation before the screen closes / transitions. Besides in-screen triggers such as close_on_click / Esc, it is also triggered by [close](../reference/ElementsDialog.md#close) from TJS (the dialog closes after the animation finishes; while a flow is running, transitions are not resolved and the whole flow ends).

For equivalent transitions on the GPU (OpenGL drawing) side, see Canvas transition drawing in [3D Graphic System](Graphic3DSystem.md).

## Specifying layout density (gap / style)

By default, elements are fit-to-content (sized to their content) and stacked tightly, so omitting explicit settings gives a cramped look. Instead of lining up spacers, you can set the density in one place:

```jsonc
{
    "style": { "font_scale": 1.25, "row_height": 44, "tile_gap": 8, "padding": 24 },
    "content": { "type": "vtile", "gap": 12, "children": [ ... ] }
}
```

- `"gap"` on `vtile` / `htile` — the gap between child elements in px (equivalent to inserting spacers automatically)
- Top-level `"style"` — applies `font_scale` (default font scale) / `tile_gap` (default for tiles without gap) / `row_height` (default minimum height of button-type elements / input_box) / `padding` (outer margin around the whole content) as defaults for unspecified values

If you omit all of these, the result is exactly the same as before.

## Rectangular text (text_area)

For pouring text into a fixed rectangle and revealing it character by character, as in subtitles or dialogue windows, use `text_area`.

```jsonc
{ "type": "text_area",
  "text": "…本文…",
  "size": 36,                    // px
  "font": "Noto Sans JP",        // 省略時はテーマ既定
  "align": "left",               // left / center / right
  "line_spacing": 12,            // 行間追加 px
  "count_var": "sub_count" }     // 文字送り ( -1 = 全部 )
```

- Line wrapping, line-start/line-end prohibition rules (kinsoku, the Japanese rules that keep certain characters off line edges), and the unit of character reveal use **the same logic** as [Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea). With the same text, width, and font / size, **line breaks match** (subtitles do not reflow differently whether drawn on a layer or in Elements).
- When you give a variable name in `"count_var"`, the host advances the reveal just by writing a number with [setVar](../reference/ElementsDialog.md#setvar). **Wrapping is fixed for the whole text before count is applied**, so the text does not reflow mid-reveal. The counting unit is the same cluster as [Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) (a ligature, combining sequence, or emoji ZWJ sequence counts as 1).
- To replace the text, use `"text_var"` / `"text_id"`; to show an entry from a list by index, use `"text_list_id"` + `"index_var"`. Both follow the same conventions as `label`.
- Combining a fixed per-row `"index"` with a shared `"index_offset_var"` (the start position) gives an "N-row window". The host **scrolls the list by moving just the one start-position variable** with [setVar](../reference/ElementsDialog.md#setvar), so you do not need a variable per row (replace the list data itself with `"text_list_var"`).
- The existing `text_box` is kept as is for compatibility (simple word wrapping, no kinsoku). Line breaks on existing screens do not change.

⚠ When placing elements at absolute coordinates (using `"at"` in `floating`), specify `"size": [w, h]` explicitly at the top level. If omitted, the dialog shrinks to the minimum size of its content, the absolute coordinates fall outside it, and nothing is shown.

## Dragging (drag_at_var / onDrag)

Writing `"drag_at_var"` on a widget writes the position during a drag into that variable in the form `"x,y"`. If you put the same variable in `"at_var"` of a canvas child, **the picture follows the drag** without going through TJS (it is handled entirely inside the engine, so it is not delayed by event delivery). The movable range can be limited with `"drag_bounds": [x, y, w, h]`.

If you want TJS to make decisions such as "where was it dropped", specify `"drag_events": true` on that widget and implement [onDrag](../reference/ElementsDialog.md#ondrag).

```tjs
class DragDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function DragDialog() { super.ElementsDialog(); }
    function onDrag(e) {
        // e.id / e.phase ( "begin" | "move" | "end" ) / e.x / e.y
        // e.dx / e.dy ( 前回からの差分 ) / e.startX / e.startY / e.modifiers
        if (e.phase == "end") {
            // 離した位置で当たり判定を取る、といった判断はここで
        }
    }
}
```

Coordinates are in the coordinate system written in the screen JSON. Queued `"move"` events are collapsed into the latest one (`"begin"` / `"end"` are not collapsed). **If you only need the visuals to follow, onDrag is unnecessary**; the `drag_at_var` + `at_var` combination is enough.

## Lists and scroll bars (list / atlas_scrollbar)

Screens with rows are built with `"type": "list"`. It works by **duplicating a one-row template for the number of rows**, and the widget takes care of row positions, hit testing, hover, selection, and even "cleaning up rows with no data". The TJS side just feeds in the data.

```tjs
var layout = %[
  "content" => %[
    "type" => "list", "id" => "files",
    "rows" => 6, "row_size" => [676, 36], "pitch" => [0, 40],
    "index_offset_var" => "top", "count_var" => "n",
    "select_var" => "sel", "row_hover_var" => "rhov#index",
    "row" => %[ "type" => "label", "id" => "row#index",
                "text_list_var" => "items" ]
  ]
];
dlg.showDict(layout);
dlg.setVar("items", "file 0\nfile 1\nfile 2");   // 一覧データ
dlg.setVar("n", "3");                             // 総件数
```

- `#index` in strings is replaced with the row number (`"id": "row#index"` → `row0` / `row1` ...). Elements with `text_list_var` get the row number and start position inserted automatically, so writing one row in the template is enough to make a list
- Clicking a row fires [onAction](../reference/ElementsDialog.md#onaction) with **`payload` = data index** (a button inside the row takes precedence)
- When you pass `count_var`, rows without data lose both drawing and hit testing
- Hover / selection colors can be built either with per-row flag variables (receive `row_hover_var` / `row_select_var` with `"visible_var"`) or by picking up `hover_var` / `select_var` in [onVar](../reference/ElementsDialog.md#onvar) and swapping host-side layers

For a scroll bar, just put **the same `index_offset_var`** on `"type": "atlas_scrollbar"`. The thumb length is proportional to "visible rows ÷ total count", and thumb dragging, paging by clicking the track, and the mouse wheel are all built in (if the content is in a `scroller`, the `scroller`'s `pos_var` is enough).

## Smooth-scrolling lists (virtual_scroller)

`list` and «windows» scroll one row at a time. To **scroll smoothly pixel by pixel**, like lists on a smartphone, use `"type": "virtual_scroller"`. Wheel and key scrolling are animated, and with `"drag_scroll": true` the content follows your finger while dragging and keeps moving with inertia at the release speed.

If you place cells for the number of rows that fit in the window plus one in a child `canvas`, the widget shifts the whole set of cells according to the position and reports the **top row** each time a row boundary is crossed. The number of cells stays the same even with thousands of items.

```tjs
var cells = [];
for (var i = 0; i < 5; i++)   // 表示 4 行 + 予備 1 行
    cells.add(%[ "type" => "label", "at" => [0, i * 100, 676, 96],
                 "index" => i, "index_offset_var" => "top", "text_list_var" => "items" ]);
var layout = %[
  "content" => %[ "type" => "canvas", "children" => [
    %[ "type" => "virtual_scroller", "id" => "list", "at" => [148, 192, 676, 400],
       "row_height" => 100, "rows_visible" => 4,
       "row_count_var" => "rows", "top_row_var" => "top", "pos_var" => "pos",
       "child" => %[ "type" => "canvas", "children" => cells ] ]
  ] ]
];
dlg.showDict(layout);
dlg.setVar("items", itemsText);   // 一覧データ ( 改行区切り )
dlg.setVar("rows", "%d".sprintf(itemCount));
```

- If the cells pull from the list as a «window» (`index` + `index_offset_var`), just put the same variable as `top_row_var` and the content follows the top row. The TJS side only passes the data and the row count
- When the host swaps pictures, thumbnails, and so on, changes of the top row arrive in [onAction](../reference/ElementsDialog.md#onaction) with **`payload` = top row**. After swapping, write the same row number to the variable named in `"row_ready_var"`; until then, the list waits without shifting content and position out of sync
- For the scroll bar, put `atlas_scrollbar` in **value mode** (`"value_var"` set to the same variable as the list's `pos_var`), add `"row_steps": true` (scroll by rows) and `"active_var"` (`"1"` while grabbed), and pass that variable to the list's `"bar_active_var"`. The thumb follows the list pixel by pixel, and on release the list snaps to a row
- PageUp / PageDown / Home / End, and ↑ ↓ (keys / pad) at the edge rows of the window, are also supported. Keys arrive when a button or other element inside a cell has focus

For the key list and fine tuning (animation duration, inertia coefficients, whether to snap to a row when stopping, etc.), see "スムーズスクロール一覧" (smooth-scrolling lists) in the elements_modal README.

## Reading and writing variables and change notification (setVar / getVar / onVar)

Variables in the screen JSON hang off a single store; besides writing them with [setVar](../reference/ElementsDialog.md#setvar), you can read them with [getVar](../reference/ElementsDialog.md#getvar). You can read more than the values you wrote yourself — **values written by the screen are in the same store**, such as `"vars_on_hover"` / `"vars_on_focus"`, a slider's `"value_var"`, `"drag_at_var"`, and a list's `"index_offset_var"`, so they can be read directly.

To find out the moment something changes, implement [onVar](../reference/ElementsDialog.md#onvar).

```tjs
class ListDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function ListDialog() { super.ElementsDialog(); }
    function onVar(name, value) {
        if (name == "row_hover") {
            // カーソルが乗っている行が変わった → ホスト側のレイヤを差し替える
            highlightRow(+value);
        }
    }
}
```

This enables a setup where **the picture is a host-side layer and only hit testing is done by the dialog**. For example, on a list screen whose single image is too large to pack into an atlas, the dialog contains only transparent buttons to receive hover, and the display is done by game-side layers.

- Notifications are delayed by one frame, and consecutive changes to the same variable are collapsed into the latest one. When you need "the current value", read [getVar](../reference/ElementsDialog.md#getvar)
- **Only dialogs that implement onVar are observed** (there is no cost if you do not implement it). To narrow the variables you receive, list their names in [watchVars](../reference/ElementsDialog.md#watchvars) — hover-linked variables and drag positions are rewritten every frame
- [listVars](../reference/ElementsDialog.md#listvars) lists the variables on the screen (name, current value, and the id and type of the widgets referring to it). Useful for debug panels and for checking screen JSON

## Keeping values across screens (shared_vars)

The variable store is **recreated for each screen**, so when moving between settings tabs, "the slider you just moved" goes back to its default. Declare the values to carry over at the top level of the screen JSON.

```jsonc
"shared_vars": ["cfg_*", "ui_lang"]
```

Matching variables become **two-way** with the session-shared store: when a screen is built they are initialized from the shared values (the shared value takes precedence over the screen's `"vars"` default), and every later change is written back to the shared store. A pattern is either an exact match or a prefix match with a trailing `*`. **The screen decides which values to carry, so no host-side implementation is needed**.

Saving to the game's save data and feeding values back after loading is the host's job, so only the interface for that is provided.

```tjs
// セーブ
var cfg = ElementsDialog.getSharedVars();   // %[ "cfg_bgm" => "70", ... ]
// ロード
ElementsDialog.clearSharedVars();
foreach_dict_of(cfg, function(k, v) { ElementsDialog.setSharedVar(k, v); });
```

Values go in and out as strings. Only values "written as a change" go to the shared store; widget initial values (`"initial"` / `"value"`) do not — this avoids untouched items being fixed to the defaults of whichever screen was opened first.

## Swapping values and pictures through variables (value_var / image_var / swappable atlases)

- **Two-state toggles** (`checkbox` / `toggle_button` / `slide_switch`) become two-way with the variable store through `"value_var"` (`""` / `"0"` / `"false"` = off). A click writes back, and the state follows [setVar](../reference/ElementsDialog.md#setvar) (following does not fire `onAction`). ON/OFF items on a settings screen can be handled without host callbacks.
- **Sliders** (`slider` / `slider_with_range` / `atlas_slider`) can be constrained to **one tick at a time** with `"snap": true`. The thumb jumps from tick to tick even while dragging, and key, wheel, pad, and screen reader increments also move one tick. One tick is determined by `"step"` (0..1) or by `step / (max - min)` of `"display"` (for example, `"display": { "min": 0, "max": 100, "step": 10 }` gives 10 steps).
- **The `image` widget** can swap the picture itself through `"image_var"`. The variable's value is used directly as the image path (`"resources/x.png"` / `"mem://thumb_3"` / empty = draw nothing), so screens such as a save list whose thumbnails change as you page, or a CG viewer that steps through pictures, can be written **without rebuilding**.
- To swap **a whole atlas**, declare `"atlases": { "cg": { "path": ..., "swappable": true } }` in the screen JSON and swap it with [setAtlasImage](../reference/ElementsDialog.md#setatlasimage). Widgets are not recreated, so layout and focus are kept. **The replacement must have the same rectangle layout** (frames / rect do not change, so if picture positions differ, the wrong picture appears). [swappableAtlases](../reference/ElementsDialog.md#swappableatlases) tells you which atlas names can be swapped.
- **Atlases are not released when a screen closes.** Decoded pictures are cached keyed by "path + scale" and kept across screen switches (to avoid failing to decode because a large contiguous block cannot be obtained after the heap fragments during long play, which would build a screen with no pictures). The amount held can be read with [atlasCacheStats](../reference/ElementsDialog.md#atlascachestats), and dropped by calling [trimAtlasCache](../reference/ElementsDialog.md#trimatlascache) at scene boundaries (title → main game, etc.). ⚠ **Atlases used by the screen currently shown are still referenced and are not dropped** — call it after closing the screen. To change the budget itself, use [atlasCacheBudget](../reference/ElementsDialog.md#atlascachebudget).

## Showing multiple non-modal dialogs and focus

The placement of non-modal (overlay) panels is specified with the top-level `"align"` / `"margin"` in the screen JSON, and the reference area for placement and scaling is chosen with the top-level `"base"` — `"window"` (default; relative to the whole window) / `"content"` (relative to the area where the game image is shown; for UI that should follow the game image, such as a subtitle window). Scaling follows the ratio of the window (or display area) to the game's base surface, so in full screen and similar modes the UI is enlarged at the same rate as the game. For titles whose UI is authored at a different resolution from the game screen (game screen 640x400 / UI 1920x1080, etc.), setting [ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) to the size of the authoring base surface makes that the scaling denominator, so the UI is not affected by changes to the game-side base surface size.

Non-modal dialogs ([showJson](../reference/ElementsDialog.md#showjson) / the [startFlow](../reference/ElementsDialog.md#startflow) family) are managed as an instance list with z-order, and several can be shown at once. The mouse is hit-tested from the frontmost instance, and keyboard / gamepad input goes to the instance that holds focus (the end of the z-order takes precedence). When a modal dialog is stacked on top, the instances below keep drawing but their input is blocked.

The non-modal start methods ([startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens)) have a `grabFocus` argument; passing false makes the dialog act as a "resident HUD that does not take focus". Use it to keep resident UI from swallowing the game's hotkeys.

In non-modal mode, only keys actually handled by Elements are consumed, and unhandled keys pass through to the game (handled pass-through). This allows coexistence such as opening another dialog with a game hotkey while a menu is open.

### Input delivery priority and host hotkeys

Input is delivered in the following priority order:

1. **Top-level hotkeys** ([System.registerHotKey](../reference/System.md#registerhotkey)) — at the entrance of the event pump. The only layer that **works even while a modal is shown** (works in both WINVER and SDL3 builds)
2. **Modal dialog** — takes all input (passes nothing to the dialogs below or to the game)
3. **Host hotkeys** ([registerHotKey](../reference/ElementsDialog.md#registerhotkey)) — registered keys are not passed to dialogs and go straight to [Window.onKeyDown](../reference/Window.md#onkeydown) and similar
4. **Non-modal panel with focus** — receives keys / pad input and passes through only what it does not handle
5. **Game / layers** — where unconsumed input lands

The single-display methods ([showJson](../reference/ElementsDialog.md#showjson) / showFile / showDict) can specify "non-modal + with focus" with the third argument `modal` (`showJson(json, true, false)`). Showing a control panel containing sliders or pickers this way lets you operate widgets with the pad's D-pad / A button or the keyboard, while keys the panel does not use flow to the game. The usual practice is then to reserve keys that "the host must always receive", such as ESC (return to scene) or PageUp/Down (switch screens), with registerHotKey (example: DemoShell in `data/demolib/demo_common.tjs`).

To move focus with the pad's D-pad, the screen JSON needs `"input": { "arrow_focus_nav": true }` (focus movement with arrow keys / D-pad is disabled by default). The panel uses the D-pad only when it "can move focus" or "reaches the focused element"; otherwise it flows to the game. On screens where the game uses the D-pad while the panel is shown, remove `arrow_focus_nav` from that panel. On devices without a physical keyboard, passing through a text field with the D-pad does not open the on-screen keyboard; it opens on confirm (A / Enter) (it opens immediately when pressed with mouse / touch).

- Hotkeys are suppressed by default while a text input widget has the caret (`duringTextInput = true` enables them during input)
- Hotkeys are also disabled while a modal is shown (they do not steal ESC = cancel from confirmation dialogs)
- Mouse buttons (VK_RBUTTON, etc.) can also be registered, which also helps avoid the problem of a full-screen transparent HUD catching a right click and closing
- If a top-level hotkey callback should "do nothing while a modal is shown", check [ElementsDialog.modalActive](../reference/ElementsDialog.md#modalactive) (whether a modal instance exists; resident overlays that do not take focus are not included)

### Input bindings and named actions

`"bindings"` in the `"input"` block assigns **named actions** to keys / pad / mouse / wheel. **Built-in names** such as `"accept"` / `"cancel"` / `"nav_up"` ... **are handled inside the dialog** and never reach TJS. Only when you write any other, non-built-in name is that input reported to the host.

```jsonc
"input": { "bindings": [
    { "wheel": "up",   "action": "prev_page" },   // 任意名 = ホストへ通知
    { "key": "escape", "action": "cancel" } ] }   // 組込名 = ダイアログ内で処理
```

`"key"` also accepts the function keys `"f1"` to `"f12"`.

Notifications arrive in [onAction](../reference/ElementsDialog.md#onaction), but **`id` is always `"<action>"`, and the name you assigned is in `payload`**.

```tjs
function onAction(id, payload) {
    if (id == "<action>") {
        switch (payload) {
        case "prev_page": /* ホイール上で前ページ */ break;
        }
    }
}
```

If you write code expecting your own name to arrive in `id`, **only that input silently does nothing**, and the cause is hard to notice, so be careful.

## Minimal example

Implement [onAction](../reference/ElementsDialog.md#onaction) in a class derived from [ElementsDialog](../reference/ElementsDialog.md), and show it by passing a JSON layout.

```tjs
class TestDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function TestDialog() { super.ElementsDialog(); }
    function onAction(id, payload) {
        switch (id) {
        case "ok":     System.inform("OK!");  close(); break;
        case "cancel": close(); break;
        }
    }
}

var json = @"
{
    // hspacer で 560 幅を確保 (JSONC コメント可)
    'size': [ 560, 200 ],
    'content': {
        'type': 'vtile',
        'children': [
            { 'type': 'hspacer', 'size': 560 },
            { 'type': 'label', 'text': 'Hello, Elements!' },
            { 'type': 'htile', 'children': [
                { 'type': 'button', 'id': 'ok',     'text': 'OK',     'close_on_click': true },
                { 'type': 'button', 'id': 'cancel', 'text': 'Cancel', 'close_on_click': true }
            ]}
        ]
    }
}";

var dlg = new TestDialog();
dlg.showJson(json);             // 非モーダル
// var r = dlg.showModalJson(json, "Title", 560, 200);   // 独立ウィンドウ
// var r = dlg.showModalJson(json);                       // ゲーム画面オーバーレイ
```

For the list of how to describe widgets such as buttons and text fields in JSON, see the [ElementsDialog](../reference/ElementsDialog.md) class reference.

## Registering fonts

Fonts used for dialog drawing are loaded through krkrz Storages (including XP3). To register them explicitly from script, use [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [ElementsDialog.registerFontDir](../reference/ElementsDialog.md#registerfontdir); to check or override the default font family, use the [ElementsDialog.defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) property.

The engine also automatically scans `.ttf` / `.otf` files under the resource path at startup and registers them (inferring family / weight / slant / stretch from the file name).

Icon glyphs such as the ✓ of check boxes and the ▼ of selection_menu are drawn not with the body font but with the icon font `elements_basic.ttf` (bundled in `resource/`). The engine registers it automatically, so you normally need not think about it, but if a setup that replaces resources leaves out this font, you get "the box appears but the ✓ does not".

### Variable fonts (registering with a weight)

Adding a `"#tag=val"` suffix to the path in `registerFont` registers an axis instance of a variable font under a separate name. The screen JSON can then use just a name such as `"font": "MyFont-Medium"`, while the actual data is consolidated into one variable font. Writing `"MyFont#wght=700"` directly in a widget's `"font"` uses the same notation.

```tjs
ElementsDialog.registerFont("MyFont", "fonts/MyFont-VF.ttf");                   // 素の VF ( 無指定 = wght=400 )
ElementsDialog.registerFont("MyFont-Medium", "fonts/MyFont-VF.ttf#wght=500");   // 別名 = 軸インスタンス
```

### Language-dependent font substitution (multilingual UI)

For UI with separate fonts per script, such as Japanese / Traditional Chinese / Simplified Chinese, setting a language → family substitution table in [ElementsDialog.fontLanguages](../reference/ElementsDialog.md#fontlanguages) swaps the family during font resolution in step with switching [ElementsDialog.language](../reference/ElementsDialog.md#language) (so kanji/hanzi at shared code points are drawn with the regional glyph forms that match the display language). The table can also be declared with the top-level `"font_languages"` in the screen JSON, and to fix the language of a specific widget, specify the widget's `"locale"`.

## Screen readers

The screen being shown can be read as is by the OS screen reader. For elements whose name cannot be determined automatically (such as image-only buttons), supplement it with the `"a11y"` key in the screen JSON. For details, see [Screen reader support](Accessibility.md).

## Build configuration

The dialog feature is available in engines built with `KRKRZ_USE_ELEMENTS=ON` (the default). Both the SDL3 build and the WINVER (native Windows / D3D11) build are supported. When built with `KRKRZ_USE_ELEMENTS=OFF`, the [ElementsDialog](../reference/ElementsDialog.md) / [ElementsPanel](../reference/ElementsPanel.md) classes are not registered, and the dialog-related code is excluded from linking, reducing the executable size.

## Overall picture and design policy

The layer structure (elements / elements_modal / the krkrz engine / the game side) and
the policy that "**UI processing is completed in the screen data, and the host only connects things**"
are explained in [Overview of the Elements UI mechanism](../topics/core/elements.md).
If you are unsure which layer to fix, read that first.

## Related APIs

- [ElementsDialog](../reference/ElementsDialog.md) — the TJS binding class
- [ElementsPanel](../reference/ElementsPanel.md) — a panel that draws into a host layer (same event / variable APIs)
- [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) — non-modal
- [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) — modal
- [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) — blocking flows
- [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) — non-modal (resident) flows
- [ElementsDialog.onAction](../reference/ElementsDialog.md#onaction) / [onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave) / [onDrag](../reference/ElementsDialog.md#ondrag) — events
- [ElementsDialog.active](../reference/ElementsDialog.md#active) — whether non-modal teardown has finished / [modalActive](../reference/ElementsDialog.md#modalactive) — whether a modal is shown
- [ElementsDialog.registerHotKey](../reference/ElementsDialog.md#registerhotkey) — host hotkeys (bypass dialogs) / [System.registerHotKey](../reference/System.md#registerhotkey) — top-level hotkeys (work even while modal)
- [ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) — UI authoring base surface size / [renderScale](../reference/ElementsDialog.md#renderscale) — rendering density
- [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [registerFontDir](../reference/ElementsDialog.md#registerfontdir) / [defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) — font registration
- [ElementsDialog.setVar](../reference/ElementsDialog.md#setvar) / [getVar](../reference/ElementsDialog.md#getvar) / [listVars](../reference/ElementsDialog.md#listvars) / [onVar](../reference/ElementsDialog.md#onvar) / [watchVars](../reference/ElementsDialog.md#watchvars) — per-screen variable store
- [ElementsDialog.getSharedVars](../reference/ElementsDialog.md#getsharedvars) / [setSharedVar](../reference/ElementsDialog.md#setsharedvar) / [clearSharedVars](../reference/ElementsDialog.md#clearsharedvars) — session-shared variables across screens (for save / load)
- [ElementsDialog.registerImage](../reference/ElementsDialog.md#registerimage) / [registerLayerImage](../reference/ElementsDialog.md#registerlayerimage) / [unregisterImage](../reference/ElementsDialog.md#unregisterimage) / [clearImages](../reference/ElementsDialog.md#clearimages) — run-time images (`mem://`; registerLayerImage registers a layer's pixels as they are)
- [ElementsDialog.setAtlasImage](../reference/ElementsDialog.md#setatlasimage) / [swappableAtlases](../reference/ElementsDialog.md#swappableatlases) — swappable atlases
- [ElementsDialog.language](../reference/ElementsDialog.md#language) / [fontLanguages](../reference/ElementsDialog.md#fontlanguages) — i18n (display language and language-dependent font substitution)
