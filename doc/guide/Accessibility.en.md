---
source_hash: 9df237092816
---

# Screen Reader Support

## About screen reader support

Kirikiri Z game screens can be read by the OS screen reader (Narrator on Windows, VoiceOver on macOS, Orca on Linux, and so on). The engine passes the name, role, value, and state of each on-screen element to the OS accessibility API (UI Automation / NSAccessibility / AT-SPI), so blind and low-vision players can play with the keyboard while listening to the screen reader.

This is supported in regular desktop builds (Windows / macOS / Linux), in both the SDL3 build and the native Windows (WINVER) build. The browser (Web) build does not have this interface.

What the screen reader receives comes from three sources:

| Source | Read without extra work? | Interface |
|---|---|---|
| Elements dialogs / panels | Yes | Supplement with the `"a11y"` key in the screen JSON |
| UI drawn on Layers (choices, menus, settings screens, etc.) | No | [ElementsDialog.setGameA11y](../reference/ElementsDialog.md#setgamea11y) or [ElementsDialog.a11yLayers](../reference/ElementsDialog.md#a11ylayers) |
| Arbitrary text (story text, result notifications, etc.) | — | [ElementsDialog.announce](../reference/ElementsDialog.md#announce) |

Nothing happens until a screen reader connects, so the overhead while none is connected is negligible.

A working example is the core demo `src/core/data/a11y` ("Screen reader" in the gallery).

## Elements dialogs

Screens shown with a [dialog](ElementsDialog.md) are read as they are. The engine automatically derives the name from button text, labeled rows, group headings, and so on; the role from the element type (button, check box, slider, ...); and the value from what is displayed. Text fields can be read by character, word, or line, and caret movement is tracked.

Where the automatic result is not enough, add an `"a11y"` key to the element. A string sets the name; a dictionary gives detailed settings.

```jsonc
{ "type": "sprite_button", "id": "btn_save", "a11y": "セーブ" }
{ "type": "slider", "id": "vol_bgm",
  "a11y": { "label_id": "cfg.bgm", "description_id": "cfg.bgm.help", "value_var": "vol_bgm_disp" } }
{ "type": "label", "text_var": "msg_body", "a11y": { "live": "polite" } }
{ "type": "image", "a11y": { "hidden": true } }
```

| Key | Meaning |
|---|---|
| `label` / `label_id` | Name (`_id` looks the text up in the string table, so it follows language switches) |
| `description` / `description_id` | Additional description |
| `role` | Overrides the role (`"heading"` / `"status"`, etc.) |
| `value_var` | Name of the variable that holds the value to present |
| `live` | `"polite"` / `"assertive"`. Reads the text aloud when `text_var` changes |
| `hidden` | Removes the element and its children from the screen reader (for decorative images, etc.) |

Putting `"a11y": { "title": "…" }` at the top level of a screen makes it announced by that name when the screen is entered.

Image-only buttons (`sprite_button` / `atlas_*`) have no text, so give them a name with `"a11y"`.

## Making UI drawn on Layers readable

UI drawn on Layers is outside Elements, so it is not read unless you do something. There are two ways to expose it, and they can be combined.

| Method | Suited for | Effort |
|---|---|---|
| [a11yLayers](../reference/ElementsDialog.md#a11ylayers) | UI operated through the Layer focus chain (`focusable`), where each button is its own Layer | Small. Just set it to true; supplement by adding members to Layers |
| [setGameA11y](../reference/ElementsDialog.md#setgamea11y) | UI that draws several items on one Layer (choices, lists, menus), or UI that manages focus itself | Build a node table in script and pass it |

### Exposing focus-chain Layers automatically (a11yLayers)

```tjs
ElementsDialog.a11yLayers = true;
```

With this, Layers in the focus chain (`focusable` and `joinFocusChain`) appear in the accessibility tree. The name comes from [hint](../reference/Layer.md#hint), and the role is button. Focus follows [Window.focusedLayer](../reference/Window.md#focusedlayer).

When the screen reader "presses" one, the engine moves focus to that Layer and then sends the Enter key. If the UI can be pressed with Enter, nothing else is needed.

To change how a Layer is read, add members to it.

```tjs
class AutoModeButton extends Layer
{
    var a11yRole = "check_box";   // クラスで持たせるときは var で宣言する
    var checked = false;          // check_box は checked メンバから状態を読む
    // ...
}

heading.a11yName = "セーブとロード";   // フォーカスできない見出しも載る
heading.a11yRole = "heading";
deco.a11yHidden  = true;               // 飾りは子ごと外す
```

| Member | Content |
|---|---|
| `a11yName` / `a11yRole` | Name / role. If either is present, even a non-focusable Layer is exposed |
| `a11yValue` / `a11yDescription` | Value / additional description |
| `a11yStates` | States, as an array or in the form `"checked,selected"` |
| `a11yHidden` | If true, removes the Layer and its children |
| `onA11yAction(action, arg)` | Receives actions from the screen reader. Return false to also run the default handling |

Elements that hold a value (sliders, etc.) have no default handling for increment/decrement. Handle them in `onA11yAction`.

```tjs
class VolumeSlider extends Layer
{
    var a11yRole = "slider";
    var value = 50;
    property a11yValue { getter() { return value + "%"; } }

    function onA11yAction(action, arg)
    {
        switch (action) {
        case "increment": setValue(value + 10); return true;
        case "decrement": setValue(value - 10); return true;
        case "set_value": setValue(+arg); return true;
        }
        return false;   // focus は既定の処理 ( focus() ) に任せる
    }
    // ...
}
```

Layers are re-read at most once every 150 ms (immediately when focus changes). If you make `a11yValue` and similar members properties, keep them lightweight. A Layer's `name` becomes its id in the accessibility tree (`layer:<name>`), so setting it makes the Layer easier to point at when checking.

### Passing a node table (setGameA11y)

When several items are drawn on one Layer, as with choices, the script builds one node per item and passes them.

```tjs
function pushChoices()
{
    var nodes = [ %[ id:"choices", role:"list", name:"どうする?" ] ];
    for (var i = 0; i < choices.count; i++) {
        nodes.add(%[
            id:"choice" + i, role:"list_item", name:choices[i], parent:"choices",
            states:(i == current) ? "focusable,selected" : "focusable",
            rect:[ 100, 400 + i * 60, 600, 48 ]   // primary layer の座標
        ]);
    }
    // 第 2 引数はフォーカスを置くノード。選択肢を操作している間だけ渡す
    ElementsDialog.setGameA11y(nodes, choiceLayer.focused ? "choice" + current : void);
}

ElementsDialog.onGameA11yAction = function(id, action, arg) {
    var i = +id.substr(6);                       // "choice<N>"
    if (action == "focus") { current = i; redraw(); pushChoices(); }
    else if (action == "click") { current = i; decide(); }
} incontextof this;
```

- Each call replaces the whole table. The engine computes the difference, so it is fine to pass everything every time the selection changes.
- The engine never moves focus or changes values on its own. When `focus` / `click` arrives from the screen reader, update the game state and then call `setGameA11y` again.
- With `rect`, the screen reader highlights that position with a frame (such as Narrator's blue box). The engine accounts for window scaling and letterboxing.
- While you pass `focus` as the second argument, the screen reader's focus stays fixed on that node. When combining with `a11yLayers`, pass it only while your own UI is being operated.
- Set `a11yHidden = true` on Layers you expose yourself, so they are not exposed twice by the automatic `a11yLayers`.
- Game nodes are placed below dialogs, and are hidden while a modal dialog is shown.

For the list of available roles, states, and keys, see [setGameA11y](../reference/ElementsDialog.md#setgamea11y).

## Reading arbitrary text (announce)

```tjs
ElementsDialog.announce("セーブしました");
ElementsDialog.announce("体力が残りわずかです", true);   // 割り込み
```

Use this for things that focus movement does not read (story text, results of actions, state changes). The text goes to the frontmost dialog, or, if there is no dialog, to the game's live region. Passing the same text repeatedly reads it every time.

To switch story-text reading depending on whether a screen reader is connected, check [a11yActive](../reference/ElementsDialog.md#a11yactive) right before reading, or handle [onA11yActiveChanged](../reference/ElementsDialog.md#ona11yactivechanged). On Windows, the connection is not established until the window comes to the foreground.

KAG3 has no screen reader extension. For KAG-based titles, the title's own scripts pass message text to `announce` and expose choices with `setGameA11y`.

## How to check

- **Listen to it**: start the game, then start Narrator (Win + Ctrl + Enter on Windows) or another screen reader, and bring the window to the foreground.
- **Inspect it in the REPL**: running the REPL (for example with `-replfile`) lets you check without a screen reader ([REPL](../topics/core/repl.md)).

| Command | Content |
|---|---|
| `.a11y` | Shows the accessibility tree (what the screen reader sees) as JSON ([Agent.a11yTree](../reference/Agent.md#a11ytree)) |
| `.a11ylog [N]` | Screen reader log: roughly what would be spoken, one line per entry ([Agent.a11yLog](../reference/Agent.md#a11ylog)) |
| `.a11ydo <node> <action> [arg]` | Performs an action through the same path as the screen reader ([Agent.a11yAction](../reference/Agent.md#a11yaction)) |
| `.say <text>` | announce |

The screen reader log looks like this:

```
[focus] 南へ行く, list item, selected
[polite] 「南へ行く」を選びました
[focus] 音量, slider, 50%
[value] 音量, 60%
```

## Caveats

- `setGameA11y` / `a11yLayers` / `onGameA11yAction` and similar are settings that **apply to the whole class**. When leaving a scene, reset them with `clearGameA11y()` / `a11yLayers = false`.
- Only the main window is supported. The dedicated window opened by `showModalJson` and second and later `Window`s are not supported yet.
- Text still being composed in a text field (before IME confirmation) is not exposed by the application. The OS IME itself conveys composing text and candidates to the screen reader. The text field holds only confirmed text.
- Turning off the build option `KRKRZ_USE_A11Y` (ON by default in regular desktop builds) stops output to the OS. The REPL inspection interface remains.
- To suppress output to the OS at run time, set `ElementsDialog.a11yMode = "off"`.

The full specification and design notes are in [Accessibility (screen reader) support](../specification/accessibility.md).

## Related APIs

- [ElementsDialog](../reference/ElementsDialog.md): `announce` / `a11yActive` / `onA11yActiveChanged` / `a11yMode` / `a11yLabel` / `setGameA11y` / `clearGameA11y` / `onGameA11yAction` / `a11yLayers`
- [Layer](../reference/Layer.md): screen reader members added to Layers (see the class description)
- [Agent](../reference/Agent.md): `a11yTree` / `a11yLog` / `a11yAction`
