---
source_hash: 8a34e23b3251
---

# Gamepad

This page explains how to use gamepad (joystick) input in Kirikiri Z. For details on
individual APIs, see the [System class reference](../../reference/System.md).

## Pad numbers (logical index)

Every pad API takes a pad number `no`. The meaning of the number is the same throughout.

- **`0`** … a special number meaning "**the most recently operated pad**". It
  automatically follows whichever pad was actually touched.
- **`1` and above** … physical pads in connection order (`1` = first, `2` = second, …).
  The number of connected pads is available from `System.getJoypadCount()`.

**Key events for button presses (described below) always originate from pad `0` =
the most recently operated pad.** With only one pad connected, `0` and `1` refer to
the same pad.

Switching of "the most recently operated pad" is decided by button / D-pad presses
(small analog stick drift does not cause a switch).

## Button input (key events)

Buttons arrive as key events. Receive `VK_PAD1`–`VK_PAD12` / `VK_PADLEFT`–`VK_PADDOWN`
/ `VK_PAD_L_*` / `VK_PAD_R_*` in `Window.onKeyDown` / `onKeyUp` (see the
[key code table](../../guide/KeyCodes.md) for the list of key codes).
The current pressed state is also available from `System.getKeyState(VK_PADn)`.

```tjs
// Window を継承したクラスで
function onKeyDown(key, shift) {
    if (key == VK_PAD1) {  /* A ボタン */ }
    if (key == VK_PADLEFT) { /* 十字左 */ }
}
```

The D-pad and left/right stick directions are quantized to 8 directions and arrive as
the direction keys above (for raw stick values, see the next section).

### `VK_PAD1`–`VK_PAD4` are determined by the button **label** (SDL3 / generic build)

`VK_PAD1` = label **A** (**✕** on PlayStation), `VK_PAD2` = **B** (**○**),
`VK_PAD3` = **X** (**□**), `VK_PAD4` = **Y** (**△**).

Nintendo-style controllers swap the **positions** of A/B and X/Y relative to
Xbox-style ones, so assigning by position causes a mismatch like "the screen says
'Press A to confirm' but the button labeled B confirms". Assigning by label makes the
on-screen prompt match the button actually pressed on any manufacturer's controller.

| | Xbox-style | PlayStation-style | Nintendo-style |
|---|---|---|---|
| `VK_PAD1` | A (bottom) | ✕ (bottom) | **A (right)** |
| `VK_PAD2` | B (right) | ○ (right) | **B (bottom)** |
| `VK_PAD3` | X (left) | □ (left) | **X (top)** |
| `VK_PAD4` | Y (top) | △ (top) | **Y (left)** |

Pad input in the native Windows (WINVER) build is based on XInput, where button
labels are fixed to the Xbox layout, so position and label never disagree (the
setting below does not exist in WINVER either).

To go back to the old position-based assignment, set
[System.padButtonMapping](../../reference/System.md#padbuttonmapping) `= "position"`
or specify the command-line option `-padbuttons=position`. Controllers whose labels
cannot be determined automatically fall back to position-based assignment.

This assignment happens at the single branch point "SDL button → `VK_PAD*`", so it
**applies to both** the game's `padKeyMap` and panel navigation in Elements dialogs.
The result is logged once per pad, which is useful for checking on real hardware.

### Use `VK_PAD_FACE_*` for buttons you want to address by position

For the four face buttons, there are virtual keys that address them by **position**,
separate from the label-based `VK_PAD1`–`VK_PAD4`.

| Key code | Position | Xbox-style label | Nintendo-style label |
|---|---|---|---|
| `VK_PAD_FACE_SOUTH` (0x1D4) | Bottom | A | B |
| `VK_PAD_FACE_EAST` (0x1D5) | Right | B | A |
| `VK_PAD_FACE_WEST` (0x1D6) | Left | X | Y |
| `VK_PAD_FACE_NORTH` (0x1D7) | Top | Y | X |

A single press of a physical button delivers **key events for both the label side and
the position side**, so whoever assigns the controls can choose per button whether to
"align by label" or "align by position" (e.g. confirm on label A = `VK_PAD1`, and a
"menu opened with the top button" on `VK_PAD_FACE_NORTH`). Regardless of the
`padButtonMapping` setting, the position side always refers to the physical layout.

The button guide display side has the same two schemes (Elements' `pad_icon` accepts
both names, such as `face_north` and `y`). Pair assignments and displays that use the
same scheme.

⚠ **Assigning both schemes to the same physical button fires twice per press.** Since
both key events are delivered, if you assign both `VK_PAD1` (label A) and
`VK_PAD_FACE_SOUTH` (bottom button) to "confirm", on an Xbox-style controller both
refer to the same physical button and the action runs twice. Pick one scheme per
button. If an Elements screen JSON mixes both schemes, a warning is logged when the
screen is built.

### `System.padStyle` — which button artwork to use

The button labeling scheme of the connected pad is available from
[System.padStyle](../../reference/System.md#padstyle) (read-only). It is one of
`"xbox"` / `"ps"` / `"switch"`, or an empty string when it cannot be determined. Use
it to choose the button artwork shown in control guides. Passing `"auto"` to
Elements' [ElementsDialog.setPadTheme](../../reference/ElementsDialog.md#setpadtheme)
selects the button artwork theme automatically based on this detection. The detection
watches the number of connected pads and their scheme and is redone the moment they
change, so you don't need to reopen the screen after plugging or unplugging a
controller (button artwork on a screen being displayed is replaced on the next draw).
On platforms where the scheme cannot be determined, it becomes `"xbox"` if at least
one pad is connected, and `"keyboard"` if none are.

### Relationship with Elements dialogs

When a [Dialog](../../reference/ElementsDialog.md) panel has keyboard focus,
`VK_PAD*` is consumed by widget operation in the panel (D-pad = focus navigation /
A = confirm / B = cancel). If you want "this pad button to always reach the game",
register it with
[ElementsDialog.registerHotKey](../../reference/ElementsDialog.md#registerhotkey); it
then bypasses the dialog and goes straight to `Window.onKeyDown` (see the
[Dialog guide](../../guide/ElementsDialog.md) for input delivery priority). Conversely,
to declare from the screen JSON side that "this input belongs to the game", specify
`"action": "passthrough"` in `"bindings"` (the panel passes it through without
consuming it; `"none"` differs in that it consumes the input and does nothing).

The core demo `pad_advanced` has a checkbox to turn this reservation on and off, so you
can compare on the spot how the same button switches between "reaching the game" and
"being absorbed by the panel".

## Analog axes

Stick tilt and trigger depression are read with `System.getPadAxis(no, axisId)`.

```tjs
var x = System.getPadAxis(0, System.padAxisLeftX);       // -1.0 〜 +1.0
var y = System.getPadAxis(0, System.padAxisLeftY);       // -1.0 〜 +1.0 (下が正)
var t = System.getPadAxis(0, System.padAxisLeftTrigger); //  0.0 〜 +1.0
```

There are 6 axis IDs: `System.padAxisLeftX` / `padAxisLeftY` / `padAxisRightX` /
`padAxisRightY` / `padAxisLeftTrigger` / `padAxisRightTrigger`. The TJS global
constants `paLeftX` … `paRightTrigger` specify the same values. No dead zone is
applied, so handle it on the caller side as needed.

!!! tip "Values are not 0 even when idle"
    Because no dead zone is applied, measured values of around ±0.05 are returned
    even when the stick is untouched. To avoid "the character moves even though I'm
    not touching anything", discard small values on the caller side. You can see the
    behavior in the core demo `pad_advanced` (stick grid + raw value display).

## Connection detection / rumble

- `System.getJoypadCount()` … number of physical pads connected
- `System.hasJoypad(no)` … whether the given number is valid
- `System.getJoypadType(no)` … model name string (environment-dependent: the
  recognized name in the SDL version, `"XInput Controller"` in the WINVER version)
- `System.padStyle` … button labeling scheme of the most recently operated pad
  (`"xbox"` / `"ps"` / `"switch"`, or an empty string if unknown). Used to choose
  button artwork (previous section)
- `System.onJoypadChange(no, name)` … callback invoked when the identifier name of the
  most recently operated pad changes (`name` is an empty string when no pad remains)
- `System.rumblePad(no, low, high, durationMs)` / `System.stopRumblePad(no)` …
  rumble (low/high are 0–255)

## Disabling pad support (for support cases)

As a workaround when another device is mistakenly recognized as a gamepad and causes
misbehavior, pad support can be disabled entirely. When disabled, neither state
polling nor key event generation takes place.

- At runtime: `System.padEnabled = false;` (re-enable with `= true;`)
- At startup: command-line option `-joypad=no` ([command line](../../guide/CommandLine.md))

An explicit setting via `System.padEnabled` takes precedence over the command line.

## Platforms and implementation

Pad input consists of a logical management layer shared by all builds
(`tTVPPadManager`) with platform-specific backends on top.

- **SDL3 / others**: based on `SDL_Gamepad`, supporting many models. If a bundled
  `gamecontrollerdb.txt` is present, it is loaded before pads are opened, so
  controllers missing from SDL's standard mappings can also be recognized.
- **WINVER (native Windows)**: based on **XInput** (up to 4 pads, rumble supported).
  Targets Xbox-style controllers; generic DirectInput pads are not supported.

For the debug display (button matrix + axis value overlay), see
[PadOverlay](pad_overlay.md). Internal engine design details are in
`src/core/doc/Gamepad.md` (SSOT).
