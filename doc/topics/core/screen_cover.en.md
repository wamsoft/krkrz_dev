---
source_hash: 40e58e320d86
---

# Fades and crossfades over the whole screen (screen cover)

A mechanism that lays a single color or a still image over the whole window to add a fade to black, a fade to white
or a crossfade when switching screens. The API is [Window.screenCover](../../reference/Window.md#screencover) /
[Window.fadeScreenCover](../../reference/Window.md#fadescreencover) /
[Window.snapshotScreenCover](../../reference/Window.md#snapshotscreencover) /
[Window.onScreenCoverDone](../../reference/Window.md#onscreencoverdone).

## Why use it

- **It is drawn in front of the Elements dialogs (overlay).** A cover made of layers (such as KAG's `syscover`) sits
  behind the Elements overlay, so it cannot cover save, load or settings screens built with Elements. The screen cover
  is not a layer, so it covers the whole screen regardless of the stacking order of layers and dialogs
- **Fades run on the engine's clock.** Each frame is drawn with the opacity of that moment even when scripts are busy,
  so the change stays smooth
- **It looks the same with every DrawDevice** (basic / ogl on WINVER, sdl / sdlogl / ogl on the SDL3 build)

Stacking order (back → front):

```
layers (under primaryLayer) → Elements dialogs → screen cover → debugging displays (memory, pad)
```

## Fade to black and back

```tjs
// To black in 0.25 seconds → switch the screen when it ends → back in 0.25 seconds
window.fadeScreenCover(255, 250);   // window.onScreenCoverDone(255) when it ends
// …after switching the screen in onScreenCoverDone…
window.fadeScreenCover(0, 250);     // window.onScreenCoverDone(0) when it ends
```

- To fade to white, pass the color: `window.fadeScreenCover(255, 300, 0xFFFFFF);`
- To cover or uncover right away, write to `screenCover`: `window.screenCover = %[ color: 0x000000, opacity: 255 ];`
- To fade in from black, for example right after loading, "cover in black right away → fade to 0"

```tjs
window.screenCover = %[ color: 0x000000, opacity: 255 ];
window.fadeScreenCover(0, 500);
```

### Waiting for the end of the fade in KAG3

Pull a trigger in the completion event `onScreenCoverDone`, and the scenario can wait with `[waittrig]`.

```
[iscript]
kag.onScreenCoverDone = function(opacity) { trigger("screencover"); } incontextof kag;
[endscript]

[eval exp="kag.fadeScreenCover(255, 250)"]
[waittrig name="screencover"]
; …switch the screen here…
[eval exp="kag.fadeScreenCover(0, 250)"]
[waittrig name="screencover"]
```

## Crossfade (covering with a still image of the current screen)

`snapshotScreenCover()` turns the screen at the moment of the call (layers and Elements dialogs) into a still image
and covers the whole screen with it. Switch the screen underneath and clear it with `fadeScreenCover(0, ms)`, and the
result is a crossfade to the new screen. The Elements screens fade too.

```tjs
window.snapshotScreenCover();      // cover with the current screen (opacity 255)
// …switch the screen underneath (show layers, show / close Elements screens)…
window.fadeScreenCover(0, 500);    // crossfade to the new screen over 0.5 seconds
```

- The still image is taken right at the call, so even if the same code goes on to change the screen, the screen before
  the change is what appears
- Only layers and Elements dialogs go into the still image; the screen cover itself and the debugging displays do not
- When the opacity reaches 0, the still image is discarded (it uses memory only while covering; its size matches the
  window's drawing buffer)
- Writing a color, or passing a color to `fadeScreenCover`, returns to a single-color cover
- On DrawDevices that cannot take a still image (such as DrawDevices from plugins), it does nothing and returns false

## Input while covered

With `blockInput` set to true, mouse, key and touch input is passed to none of layers, Elements or the Window's events
while the cover is shown (the opacity is not 0, or a fade is in progress). This prevents accidents such as a button being
pressed during a fade and a screen opening twice. The default is false (input passes).

```tjs
window.screenCover = %[ blockInput: true ];          // from now on, block input while covered
window.fadeScreenCover(255, 250, void, true);        // can also be set together with a fade
```

Input that releases a button or key (onMouseUp / onKeyUp and so on) is not blocked, so nothing stays pressed.

## Captures and thumbnails

- It appears in screen captures ([System.captureScreen](../../reference/System.md#capturescreen)) just as it is seen
  (including the screen cover)
- It does not appear in images taken from layers (such as save thumbnails), because it is not a layer

## Checking the current state

Reading `screenCover` returns `%[ color, opacity, blockInput, fading, snapshot ]`. `opacity` is the opacity at that
moment (the intermediate value during a fade), `fading` is 1 during a fade, and `snapshot` is 1 while covering with a
still image.
