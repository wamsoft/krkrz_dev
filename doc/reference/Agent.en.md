# Agent

!!! warning "Experimental (not covered by stability guarantees)"
    The shape of this API is not settled yet. **It may change or be removed
    without notice** (the major version is not bumped even for incompatible changes).
    See [versioning](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)
    for how versions are bumped.

    開発・検証用の API です。REPL / デバッグ窓の整備にあわせて変わります。

The Agent class provides an API for agent-driven operation (testing / automation). You cannot create objects from this class; like System, call its members directly, as in `Agent.click(...)`.

This class provides injection of input events ( mouse / key / wheel ), capture of the actual screen, and observation and manipulation of Elements dialogs. It is intended for driving Kirikiri from an external agent to verify behavior.

This class is only available when the REPL feature is enabled ( any of the command-line options `-repl` / `-replfile` / `-replweb` ) and in builds with Elements enabled ( see REPL.md for REPL-driven operation ).

All coordinates are logical coordinates. The `shift` argument is a bit flag of the shift state; the default is 0. The `button` argument is 0 = left button / 1 = right button / 2 = middle button. The `vk` argument is a numeric virtual key code. The dialog-related methods ( `dialogs` / `dialogTree` / `closeDialog` / `closeAllDialogs` / `dialogClick` / `dialogFocus` / `text` ) only work in builds with Elements enabled.

## Members

### Properties

- [ignoreRealMouse](#ignorerealmouse)

### Methods

- [mouseMove](#mousemove)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [click](#click)
- [wheel](#wheel)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [keyPress](#keypress)
- [text](#text)
- [dialogs](#dialogs)
- [imeStatus](#imestatus)
- [dialogTree](#dialogtree)
- [closeDialog](#closedialog)
- [closeAllDialogs](#closealldialogs)
- [dialogClick](#dialogclick)
- [dialogFocus](#dialogfocus)
- [captureScreen](#capturescreen)
- [lastCapture](#lastcapture)
- [a11yTree](#a11ytree)
- [a11yLog](#a11ylog)
- [a11yAction](#a11yaction)

---

### ignoreRealMouse

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Discards real mouse input ( for behavior testing )

When true, **all real mouse input is discarded** and only input injected by Agent
is passed through. This establishes the premise that "all input comes from Agent" in automated tests,
so a person accidentally moving the pointer does not spoil the measurement.

The command-line option `-ignoremouse=yes` enables it from startup.

Hover detection and cursor queries look at the **virtual cursor position**,
which Agent's injected input updates, so hover and focus keep working
as usual even when this is enabled.

⚠ When enabled, **the mouse can no longer be operated by hand**. It is meant for verification.

---

### mouseMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Destination X coordinate, in logical coordinates. |
| `y` | `&nbsp;` | Destination Y coordinate, in logical coordinates. |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a mouse move

Injects a mouse move event to the given logical coordinates.

---

### mouseDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate, in logical coordinates. |
| `y` | `&nbsp;` | Y coordinate, in logical coordinates. |
| `button` | `0` | Button number ( 0 = left / 1 = right / 2 = middle ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a mouse button press

Injects a mouse button press event at the given logical coordinates.

---

### mouseUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate, in logical coordinates. |
| `y` | `&nbsp;` | Y coordinate, in logical coordinates. |
| `button` | `0` | Button number ( 0 = left / 1 = right / 2 = middle ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a mouse button release

Injects a mouse button release event at the given logical coordinates.

---

### click

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate, in logical coordinates. |
| `y` | `&nbsp;` | Y coordinate, in logical coordinates. |
| `button` | `0` | Button number ( 0 = left / 1 = right / 2 = middle ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a click

Injects hover ( move ) → press → release at the given logical coordinates in one go,
reproducing a single click.

---

### wheel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `delta` | `&nbsp;` | Rotation amount ( 1 notch = 120 units ). |
| `x` | `&nbsp;` | X coordinate, in logical coordinates. |
| `y` | `&nbsp;` | Y coordinate, in logical coordinates. |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a mouse wheel event

Injects a mouse wheel rotation event.

---

### keyDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vk` | `&nbsp;` | Numeric virtual key code ( VK_* ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a key press

Injects a key press event.

---

### keyUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vk` | `&nbsp;` | Numeric virtual key code ( VK_* ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a key release

Injects a key release event.

---

### keyPress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vk` | `&nbsp;` | Numeric virtual key code ( VK_* ). |
| `shift` | `0` | Bit flag of the shift state. |

**Description**

Injects a key press + release

Injects a key press and release in one go, reproducing a single keystroke.

Only **key events** are injected. Character input events
( [Window.onKeyPress](Window.md#onkeypress) ) are generated through the OS text input path,
so this method does not trigger them. To enter text in automated tests,
use an Elements input field together with [Agent.text](Agent.md#text).

---

### text

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | UTF-8 text to send. |

**Description**

Sends text

Sends UTF-8 text to the input field ( input_box ) of the active Elements dialog.
Ignored if there is no target input field.

---

### dialogs

Method

**Return value**

An array of dialog descriptors. Each element is a dictionary of the form
`%[index, modal, active, screen, focused, textFocus, x, y, w, h]`.

`textFocus` indicates whether a text input widget ( input_box, etc. ) has editing focus;
it is the very value used to decide whether to open the software keyboard or IME.
Useful for isolating problems such as Japanese input not starting.

`screen` is the current screen name of a flow ( navigator ); it is empty for a standalone dialog.
`focused` is the id of the focused widget, but **it is filled in only on screens that have
a mechanism for tracking ids**. Empty does not mean there is no focus
( to check whether anything has focus, use `textFocus` or
[Agent.dialogTree](Agent.md#dialogtree) ).

**Description**

Gets the list of active dialogs

Returns an array of descriptors of the currently active Elements dialogs.

**See also:** [Agent.dialogTree](Agent.md#dialogtree)

---

### imeStatus

Method

**Return value**

An array of dictionaries describing each window's state. The main items are as follows.

`contextAttached` … whether an input context is associated. **If false, the IME is completely
disabled**: neither [Window.imeMode](Window.md#imemode) nor the Hankaku/Zenkaku key has any effect,
and `conversion` is also 0.

It becomes false when the focused layer's
[imeMode](Layer.md#imemode) is `imDisable` (the default), or when
the context has been cut externally, e.g. by `Window.resetImeContext(false)`.
The former is **a normal state**; the context is reassociated automatically when focus moves
to a layer other than `imDisable`. If it stays false while in a text field, suspect the latter.

`hasFocus` … whether this window has keyboard focus. While false, the IME mode
is not applied at all.

`keyTrapperIsSelf` … if false, the mode of another window whose `trapKey` is true is applied.

`imeMode` … the mode actually applied. `defaultImeMode` is the default value returned by
[Window.imeMode](Window.md#imemode).

`overrideActive` … whether an ElementsDialog text field holds the IME.
`contextForced` indicates whether the input context was reassociated for that purpose.

`areaX` / `areaY` / `areaW` / `areaH` / `areaCursor` … the rectangle last passed to the host to position
the IME composition / candidate windows ( window client
coordinates in px ), and the caret x relative to its left edge. If `areaValid` is false,
no text field has editing focus.

Other items are `visible` / `trapKeys` / `attentionPoint` / `controlImeState` /
`disabledBySelf` / `imeAvailable` / `open` / `savedImeMode` / `conversion` /
`sentence` / `index` / `isMain`. SDL3 builds only fill in
`textInputActive` and the area items above.

**Description**

Gets the IME state

Returns IME-related state for each window. Intended for isolating problems such as
"the caret appears in the input field, but Japanese cannot be typed".

It only has content in the native Windows ( WINVER ) build. Other builds
always return an empty array.

**See also:** [Agent.dialogs](Agent.md#dialogs)

---

### dialogTree

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index of the target dialog. |

**Return value**

An array of widgets. Each element is a dictionary of the form `%[id, type, value]`.

**Description**

Gets the list of a dialog's widgets

Returns the list of widgets with an id in the given dialog.

**See also:** [Agent.dialogs](Agent.md#dialogs)

---

### closeDialog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `0` | Index of the target dialog ( currently this<br>argument is ignored and the frontmost dialog is always closed ). |

**Description**

Closes a dialog

Closes the frontmost Elements dialog.

**See also:** [Agent.closeAllDialogs](Agent.md#closealldialogs)

---

### closeAllDialogs

Method

**Description**

Closes all dialogs

Forcibly closes all Elements dialogs.

**See also:** [Agent.closeDialog](Agent.md#closedialog)

---

### dialogClick

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index of the target dialog. |
| `id` | `&nbsp;` | id of the widget to activate. |

**Description**

Activates a dialog widget

Moves focus to the widget with the given id in the given dialog and activates it
( equivalent to Enter ). No coordinates are needed.

**See also:** [Agent.dialogFocus](Agent.md#dialogfocus)

---

### dialogFocus

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index of the target dialog. |
| `id` | `&nbsp;` | id of the widget to move focus to. |

**Description**

Moves focus to a dialog widget

Moves focus to the widget with the given id in the given dialog.

**See also:** [Agent.dialogClick](Agent.md#dialogclick)

---

### captureScreen

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Destination unified storage path ( .png ). |
| `x` | `0` | Left edge of the area to save. |
| `y` | `0` | Top edge of the area to save. |
| `w` | `0` | Width of the area to save ( 0 for the whole screen ). |
| `h` | `0` | Height of the area to save ( 0 for the whole screen ). |

**Return value**

The destination path.

**Description**

Saves the actual screen as PNG

Requests that the actual screen be read back, including the next frame's present, and saved as PNG to path.
x, y, w, h specify the area to save; setting w / h to 0 captures the whole
screen.

**See also:** [System.captureScreen](System.md#capturescreen) / [Agent.lastCapture](Agent.md#lastcapture)

---

### lastCapture

Method

**Return value**

A dictionary of the form `%[path, width, height, ok]`.

**Description**

Gets the most recent capture result

Returns the result of the most recent [Agent.captureScreen](Agent.md#capturescreen).

**See also:** [Agent.captureScreen](Agent.md#capturescreen)

---

### a11yTree

Method

**Return value**

The accessibility tree as a JSON string.

**Description**

Gets the accessibility tree

Returns the accessibility tree seen by screen readers as a JSON string.
It is available even when no screen reader is connected.

The form is `{"dialogs":[{"index","screen","modal","tree"}],"game":{"hidden","tree"}}`;
`dialogs` are the dialogs being shown, and `game` is the node for the game itself
( [ElementsDialog.setGameA11y](ElementsDialog.md#setgamea11y) /
[ElementsDialog.a11yLayers](ElementsDialog.md#a11ylayers) )
( `null` if absent; `hidden` indicates whether it is hidden under a modal dialog ).
A node's `id` is the `"id"` from the screen JSON or the id given to setGameA11y; nodes without one
get `"#<hex>"`. Same as the REPL `.a11y` command.

**See also:** [Agent.a11yAction](Agent.md#a11yaction)

---

### a11yLog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `since` | `0` | Returns lines from this position on ( from the beginning if omitted ). |

**Return value**

A dictionary of the form `%[lines, next]`. Passing `next` as since next time returns only the new lines.

**Description**

Gets the screen reader log

Returns a log that records, one line at a time, roughly what a screen reader would say.
Lines start with `[focus]` / `[value]` / `[state]` / `[caret]` / `[selected]` / `[polite]`, etc.,
and [ElementsDialog.announce](ElementsDialog.md#announce) is recorded here too.
The log only accumulates while the REPL is running. Same as the REPL `.a11ylog` command.

```tjs
var r = Agent.a11yLog(since);
for (var i = 0; i < r.lines.count; i++) Debug.message(r.lines[i]);
since = r.next;   // 次回は差分だけ
```

---

### a11yAction

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `node` | `&nbsp;` | `id` of the node to operate. |
| `action` | `&nbsp;` | `"click"` / `"focus"` / `"increment"` / `"decrement"` / `"set_value"`. |
| `arg` | `&nbsp;` | Value for `"set_value"`. |

**Return value**

True if the operation succeeded.

**Description**

Operates via the same path as a screen reader

Operates a node of [Agent.a11yTree](Agent.md#a11ytree) through the same path as operations from
a screen reader ( not synthesized key input ). Used to verify screen reader support.
Searches from the frontmost dialog; if there is no modal dialog, the game's own nodes are
searched too. Same as the REPL `.a11ydo` command.

**See also:** [Agent.a11yTree](Agent.md#a11ytree)

---
