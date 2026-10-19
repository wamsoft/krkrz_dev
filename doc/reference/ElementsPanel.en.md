# ElementsPanel

!!! warning "Experimental (not covered by stability guarantees)"
    The shape of this API is not settled yet. **It may change or be removed
    without notice** (the major version is not bumped even for incompatible changes).
    See [versioning](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)
    for how versions are bumped.

    Elements ベースの UI 機構はまだ形が固まっていません。イベント / 変数まわりの API は ElementsDialog と揃えて変わることがあります。

Panel that draws an Elements screen onto a host layer

A class that draws the same screen JSON as [ElementsDialog](ElementsDialog.md) **onto the bitmap of a given [Layer](Layer.md)**
instead of as an overlay ( always on top ).
Z-order, transitions ( `[trans]` ), screenshots ( piledCopy ), and input
ownership all follow Kirikiri's layer mechanisms, so use it for HUDs that must not
cover the text, UI that is part of the game screen, screens you want to carry through a transition,
and so on.

```tjs
var lay = new Layer(win, win.primaryLayer);
lay.setImageSize(400, 300);
lay.setSizeToImageSize();
lay.type = ltAlpha;      // ltAddAlpha なら変換なしでさらに軽い
lay.hitThreshold = 0;    // すべてのマウスメッセージを受ける
lay.visible = true;

var panel = new ElementsPanel(lay);
panel.onAction = function(id, payload) { ... };
panel.showFile("ui/hud.jsonc");

// レイヤの入力をパネルへ流す ( Layer 派生で 1 回書けばよい )
lay.onMouseDown = function(x, y, b, f) { panel.mouseDown(x, y, b, f); };
lay.onMouseUp   = function(x, y, b, f) { panel.mouseUp  (x, y, b, f); };
lay.onMouseMove = function(x, y, f)    { panel.mouseMove(x, y, f); };
```

The events ( [onAction](#onaction) / [onDrag](#ondrag) / [onVar](#onvar) /
[onClose](#onclose) ) and the variable store API ( [setVar](#setvar) /
[getVar](#getvar) / [listVars](#listvars) / [watchVars](#watchvars) ) have
the same shape as in ElementsDialog, so existing screen drivers can be reused almost as is.

Differences from ElementsDialog ( overlay ):

- Does not affect input interception or window-close suppression
- Does not appear in `Agent.dialogs()` / `closeAllDialogs()`
- Has no modal result, navigator flow, virtual keyboard, or host hotkey table
( 1 panel = 1 screen. To switch screens, call showJson again, or
use two layers and let `[trans]` handle it )
- Does not receive key / pad input by default. For screens that need it,
feed [keyDown](#keydown) / [keyUp](#keyup) / [text](#text) from
script

The theme, display language, and the runtime image store of
[ElementsDialog.registerImage](ElementsDialog.md#registerimage)
are shared across the whole process and also apply to panels.

## Members

### Constructors

- [ElementsPanel](#elementspanel)

### Properties

- [active](#active)
- [focused](#focused)
- [watchVars](#watchvars)

### Methods

- [showFile](#showfile)
- [showJson](#showjson)
- [showDict](#showdict)
- [close](#close)
- [notifyResized](#notifyresized)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [mouseMove](#mousemove)
- [mouseWheel](#mousewheel)
- [mouseLeave](#mouseleave)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [text](#text)
- [setVar](#setvar)
- [getVar](#getvar)
- [listVars](#listvars)
- [invalidate](#invalidate)
- [focus](#focus)
- [activate](#activate)

### Events

- [onAction](#onaction)
- [onDrag](#ondrag)
- [onVar](#onvar)
- [onClose](#onclose)

---

### ElementsPanel

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination [Layer](Layer.md). |

**Description**

Constructs an ElementsPanel object

Constructs a panel that draws onto the given layer. Drawing fills the layer's entire
image size.

---

### active

Property \ Access: `r`

**Description**

Whether a screen is open

---

### focused

Property \ Access: `r`

**Description**

id of the currently focused widget

Empty string if nothing has focus.

---

### watchVars

Property \ Access: `r/w`

**Description**

Which variable changes are delivered to onVar

Same as [ElementsDialog.watchVars](ElementsDialog.md#watchvars).
void ( default ) = all variables, only when onVar is implemented / `"*"` = all variables /
`[]` = observe none / `[name, ...]` = only those variables.

---

### showFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Unified storage path of the screen JSON. |

**Return value**

Whether it was opened.

**Description**

Opens screen JSON from a file

Loads screen JSON ( jsonc allowed ) from a file and starts drawing onto the layer.
Relative asset paths in the screen are resolved from the directory containing the JSON.

---

### showJson

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `json` | `&nbsp;` | Screen JSON string. |

**Return value**

Whether it was opened.

**Description**

Opens screen JSON from a string

---

### showDict

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dict` | `&nbsp;` | Layout Dictionary. |

**Return value**

Whether it was opened.

**Description**

Opens a layout written as a Dictionary

Opens a layout written with TJS Dictionary / Array ( same format as
[ElementsDialog.showDict](ElementsDialog.md#showdict) ).

---

### close

Method

**Description**

Closes the panel

Discards the screen and stops drawing. The layer itself remains ( and the last drawn content
is not erased ), so clear it on the host side if needed.

---

### notifyResized

Method

**Description**

Notifies the panel of a layer size change

Call this after changing the image size of the destination layer. Drawing uses the new
size from the next frame.

---

### mouseDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Layer-local X coordinate. |
| `y` | `&nbsp;` | Layer-local Y coordinate. |
| `button` | `0` | = 0 Mouse button ( 0 = left / 1 = right / 2 = middle ). |
| `shift` | `0` | = 0 Shift state bit flags. |

**Description**

Feeds a mouse press to the panel

Coordinates are layer-local ( the Layer.onMouseDown arguments as is ).

---

### mouseUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Layer-local X coordinate. |
| `y` | `&nbsp;` | Layer-local Y coordinate. |
| `button` | `0` | = 0 Mouse button. |
| `shift` | `0` | = 0 Shift state bit flags. |

**Description**

Feeds a mouse release to the panel

---

### mouseMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Layer-local X coordinate. |
| `y` | `&nbsp;` | Layer-local Y coordinate. |
| `shift` | `0` | = 0 Shift state bit flags. |

**Description**

Feeds a mouse move to the panel

---

### mouseWheel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `delta` | `&nbsp;` | Rotation amount ( in units of 120 ). |
| `x` | `&nbsp;` | Layer-local X coordinate. |
| `y` | `&nbsp;` | Layer-local Y coordinate. |
| `shift` | `0` | = 0 Shift state bit flags. |

**Description**

Feeds a wheel rotation to the panel

---

### mouseLeave

Method

**Description**

Tells the panel that the mouse left the layer

---

### keyDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code. |
| `shift` | `0` | = 0 Shift state bit flags. |

**Return value**

Whether the panel consumed it.

**Description**

Feeds a key press to the panel

The panel does not take keyboard focus by default, so feed keys from script
only for screens that need them.

---

### keyUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code. |
| `shift` | `0` | = 0 Shift state bit flags. |

**Return value**

Whether the panel consumed it.

**Description**

Feeds a key release to the panel

---

### text

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | String to input. |

**Description**

Feeds text input to the panel

Text input to an input_box ( equivalent to IME / paste ).

---

### setVar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |
| `value` | `&nbsp;` | Value to set ( string ). |

**Return value**

Whether it was written.

**Description**

Writes a variable of the displayed screen

Same as [ElementsDialog.setVar](ElementsDialog.md#setvar).

---

### getVar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |

**Return value**

The variable's value ( string ). void for an unknown variable or when nothing is open.

**Description**

Reads a variable of the displayed screen

Same as [ElementsDialog.getVar](ElementsDialog.md#getvar).

---

### listVars

Method

**Return value**

An array of variable descriptor Dictionaries. An empty array when nothing is open.

**Description**

Gets the list of variables of the displayed screen

Same as [ElementsDialog.listVars](ElementsDialog.md#listvars).

---

### invalidate

Method

**Description**

Requests an explicit redraw

Redraws the whole screen on the next frame. Normally unnecessary ( screen changes
are reflected automatically ).

---

### focus

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id of the widget to focus. |

**Return value**

Whether the request was made. false when nothing is open.

**Description**

Moves focus to the widget with the given id

Same as [ElementsDialog.focus](ElementsDialog.md#focus). An input_box
receives editing focus ( caret shown + accepts text ).

---

### activate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id of the widget to activate. |

**Return value**

Whether it was activated. false for an unknown id or when nothing is open.

**Description**

Activates the widget with the given id

Moves focus to it and activates it ( equivalent to Enter ).
Same as [ElementsDialog.activate](ElementsDialog.md#activate).

---

### onAction

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | id of the operated widget. |
| `payload` | `&nbsp;` | Value ( void for a button click, the actual value for a state widget ). |

**Description**

Widget operation notification

Same as [ElementsDialog.onAction](ElementsDialog.md#onaction).

---

### onDrag

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `payload` | `&nbsp;` | Dictionary of drag information. |

**Description**

Drag notification

Same as [ElementsDialog.onDrag](ElementsDialog.md#ondrag).

---

### onVar

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name. |
| `value` | `&nbsp;` | New value ( string ). |

**Description**

Variable change notification

Same as [ElementsDialog.onVar](ElementsDialog.md#onvar).

---

### onClose

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `action` | `&nbsp;` | The action that triggered the close. |

**Description**

Notification when the screen closes

Same as [ElementsDialog.onClose](ElementsDialog.md#onclose).

---
