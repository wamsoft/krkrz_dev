---
source_hash: 79ab1a80fa57
---

# Common Pitfalls (TJS2 / Engine API)

A collection of practical notes on pitfalls actually encountered while writing the core demos (`src/core/data/*`).
All of them are the kind that "raise no error and silently give a different result",
so they are organized to let you look them up from the symptom.

---

## TJS2 language

### Extract a character with `str[i]`. `str[i, 1]` is something else

In `str[i, 1]`, the comma expression `(i, 1)` is evaluated, so it is **always `str[1]`**.
Since no error occurs, you only notice when the result of string processing turns out to be "all the same character".

```tjs
var s = "abcdef";
var c1 = s[2];        // "c"      … 正しい
var c2 = s.charAt(2); // "c"      … 範囲外でも例外にならない版
var c3 = s[2, 1];     // "b" (!)  … カンマ式なので常に s[1]
```

(`s[2]` is correct; `s.charAt(2)` is the variant that doesn't throw when out of range; `s[2, 1]` is always `s[1]` because of the comma expression.)

→ [Operations on Strings](../../tjs2/string.md)

### `Math.floor()` and friends return real numbers

Even if you meant to round to an integer, the type stays real, so string concatenation
prints something like `"1.000000000000000"`. Add `(int)` when using it for display or as an index.

```tjs
var n = Math.floor(payload + 0.5);
dm("index = " + n);        // "index = 1.000000000000000"
dm("index = " + (int)n);   // "index = 1"
```

### Anonymous functions don't capture outer local variables

TJS2 function expressions are not closures. Put values you want to use inside a callback
in **a member variable or global**.

```tjs
function start() {
    var scene = this;                       // これはコールバックから見えない
    var t = new Timer(function() {
        scene.close();                      // → 例外: メンバ "scene" が見つかりません
    }, "");
}
```

(The local `scene` is not visible from the callback; calling `scene.close()` throws a "member "scene" not found" exception.)

```tjs
// メンバ変数にするか、global に置く
global.__scene = this;
var t = new Timer(function() { global.__scene.close(); }, "");
```

### `if` on a non-numeric string is always false

`if("abc")` is not true (the string is converted to a number and becomes 0).
Check for existence with `typeof` or `!== void`.

```tjs
if (typeof System.appDataPath != "undefined") { ... }   // 正しい
if (obj.name !== void) { ... }                          // 正しい
```

---

## Layers / drawing

### `Layer.visible` defaults to false

A layer is not displayed just by creating it. This is the cause of almost every "nothing shows up" in the demos.

### `hitType` has two values: `htMask` and `htProvince`

To "hit anywhere in the rectangle", use **`hitThreshold = 0`**, not `htRect`.

### `drawText` colors are 24-bit RGB

Specify them as 6-digit `0xRRGGBB`. Passing 8 digits (`0xAARRGGBB`) is treated as a system color
specification and unintentionally turns black.

### `Layer.invalidate` does not invalidate child layers

The children are "just detached from the parent" and survive, and drawing to them silently succeeds.
To discard a whole subtree, invalidate it recursively
(demolib's `invalidateLayerTree` is an example implementation).

### Multiplicative modes of `operateRect` need `holdAlpha`

`omMultiplicative` and similar modes set the destination alpha to 0,
so using them on an `ltAlpha` layer turns it completely black. To preserve the destination,
specify `holdAlpha = true`.

### Keep update rectangles minimal

If you habitually call `update()` with no arguments (= the whole area), the entire screen keeps being
uploaded to the GPU every frame even when the screen is static. Updating only the "rectangle to erase" and the
"rectangle to draw" changes the transfer volume by orders of magnitude (measurements in the core demo `perf_stats` / explanation in
`src/core/doc/ScreenTransfer.md`).

---

## APIs whose availability depends on the build

If you run the same script on both the native Windows (WINVER) build and the SDL3 build,
check that the following exist with `typeof` before using them.

| API | Status |
|---|---|
| `System.appDataPath` / `personalPath` | Added to the SDL3 / generic build on 2026-08-25 (on Windows it resolves the same way as WINVER). On other OSes, since 2026-10 it returns the OS-standard folder (macOS `~/Library/Application Support/` / Linux `~/.local/share/`, etc.) (before that, the same value as `exePath`). Generic builds of engines older than that don't have it, so check with `typeof`. For the save location, use `System.dataPath` |
| `System.desktopLeft/Top/Width/Height` | WINVER only. For the resolution alone, use `System.screenWidth/Height` |
| `System.readRegValue` / `writeRegValue`, etc. | Windows extensions. Not available in the SDL3 build (`urlencode` / `urldecode` / `readEnvValue` / `writeEnvValue` / `expandEnvString` entered the engine on 2026-09-28 and are available in all builds) |
| `System.setMemoryOverlay` / `setPadOverlay` | The flags are common to all builds, but only the OGL-family / SDL DrawDevices draw them (they don't appear with D3D11, the WINVER default) |
| `Layer.imeMode` / `setAttentionPoint` | In SDL3, `imeMode` only distinguishes "`imDisable` or anything else" (text input is accepted only while a layer with another mode has focus). Fine-grained open/close and input-mode settings, and `setAttentionPoint`, only take effect in WINVER |
| `Window.setZoom` | Behavior unified across both builds on 2026-08-17 (sets the window's inner size to "layer size × factor"). Before that, WINVER only remembered the factor, so if you also target older engines, use [Window.setInnerSize](../../reference/Window.md#setinnersize) as well |
| `System.padButtonMapping` | SDL3 / generic build only. WINVER is XInput-based with fixed Xbox-style labels, so the setting itself is unnecessary |
| `Dialog` family / `WebServer` | Depends on build options (`KRKRZ_USE_ELEMENTS` / `KRKRZ_REPL_WEB`) |

---

## Input

### Text input is `onKeyPress`, keys are `onKeyDown`

`onKeyDown` handles virtual key codes, while `onKeyPress` handles the characters themselves (including characters committed by the IME).
If you write character-collecting logic in `onKeyDown`, you won't get IME input.

### Pad input is absorbed by the panel while an Elements panel is shown

`VK_PAD*` is consumed by widget operation on the panel (D-pad = move focus / A = confirm)
and does not reach the game's `onKeyDown`. Reserve buttons the game must always receive with
[ElementsDialog.registerHotKey](../../reference/ElementsDialog.md#registerhotkey) to
bypass the panel (the core demo `pad_advanced` compares ON/OFF).

### Analog sticks don't return 0 even when idle

`System.getPadAxis` returns around ±0.05 even with no input. Implement
dead-zone handling on the game side.

### `Agent.keyPress` produces no text input events

Only key events are injected (characters go through the OS's text input path).
To enter text in automated tests, use an Elements input field + `Agent.text`.

---

## Other

### `Clipboard.asText` is void when there is no text

It returns void, not an empty string. Check with `if (v === void)`.

### Don't assume a plugin for building JSON

`Scripts.toJSONString` / `evalJSON` are extensions from the json plugin. If you want to stay within core
features only, build the JSON by hand or use [`ElementsDialog.dictToJson`](../../reference/ElementsDialog.md#dicttojson) (when Elements is enabled).

---

## Related

- [TJS2 Language Specification](../../tjs2/index.md)
- [Class Reference](../../reference/System.md)
- Core demos (`src/core/data/`) — each demo's `readme.txt` describes the pitfalls
  encountered in that particular demo
