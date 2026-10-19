---
source_hash: e55e8ab4560a
---

# Observing Gamepad State (PadOverlay)

The SDL3 build of the engine includes a debug overlay that shows the gamepad
state ( on/off for 16 buttons and analog values for 6 axes ) in real time in
the upper-left corner of the screen. It is useful when checking controller
behavior on actual hardware ( for example, the Switch ).

For the detailed display specification and internals, see the guides in src/core:

- [doc/PadOverlay.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/PadOverlay.md)
- [doc/Gamepad.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Gamepad.md)

---

## Example display

```
+--------------------------------+
| Pad: Xbox Series X Controller  |
| [A ][B ][X ][Y ]               |
| [L1][R1][L2][R2]               |
| [BK][ST][LS][RS]               |
| [Lf][Up][Rt][Dn]               |
| LX +0.45 LY -0.32              |
| RX +0.00 RY +0.00              |
| LT +0.00 RT +0.80              |
+--------------------------------+
```

- Header: SDL gamepad name ( `(none)` when nothing is connected )
- Cells: green while pressed, dark gray otherwise
- Axes: stick axes range `-1.00 〜 +1.00`, trigger axes `0.00 〜 +1.00`

The WINVER build has no gamepad abstraction API, so when shown through the
OGLDrawDevice path, every button is off and every axis reads +0.00.

---

## Enabling the overlay

- From startup: [`-padoverlay=1`](../../guide/CommandLine.md)
- Toggle at run time: [System.setPadOverlay](../../reference/System.md#setpadoverlay)
- From the [REPL](repl.md): `.padoverlay [on|off]`

It works independently of [`-memoverlay=1`](../../guide/CommandLine.md)
( upper-right corner ), and both can be shown at the same time.

---

## Reading axes directly from TJS2

The overlay is for observation; to read analog axis values from a script, use
[System.getPadAxis](../../reference/System.md#getpadaxis).

```tjs
var v = System.getPadAxis(0, System.padAxisLeftX);
// v は -1.0 〜 +1.0 の実数 (未接続/無効値で 0.0)
```

Six axis ID constants are provided, such as
[System.padAxisLeftX](../../reference/System.md#padaxisleftx).

Use [System.rumblePad](../../reference/System.md#rumblepad) /
[System.stopRumblePad](../../reference/System.md#stoprumblepad) for vibration.
To check the number of connected gamepads or whether one is present, use
[System.getJoypadCount](../../reference/System.md#getjoypadcount) /
[System.hasJoypad](../../reference/System.md#hasjoypad).
