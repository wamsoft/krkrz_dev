---
source_hash: 16f9754600c1
---

# Controlling the Game Screen's Display Area (Viewport)

You can place the inner game screen inside the outer window (surface) at any size, position and
scale, and fill the surrounding margin with a background color or wallpaper image. Use this when you want
letterboxing, integer scaling, centering and so on to fit the window size while keeping the game's native resolution.

For details of the internals, see the guide on the src/core side:

- [doc/Viewport.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Viewport.md)

!!! note "Supported builds / supported DrawDevices"
    Placement settings (fit / zoom / align / offset) are available in **both the native Windows (WINVER)
    build and the SDL3 / generic build** (WINVER support since 2026-08-17).

    **Filling** the margin ([Window.viewportBgColor](../../reference/Window.md#viewportbgcolor) /
    [Window.setViewportWallpaper](../../reference/Window.md#setviewportwallpaper)) only takes effect when
    the draw device supports it. The bundled
    [BasicDrawDevice](../../reference/Window.BasicDrawDevice.md) (WINVER default) /
    [SDLDrawDevice](../../reference/SDLDrawDevice.md) / SDLOGL /
    [OGLDrawDevice](../../reference/OGLDrawDevice.md) all support it.
    With draw devices that don't (NullDrawDevice or plugin-provided ones), the margin
    keeps that device's default fill
    (check whether `drawDevice.viewportBackgroundHost` is non-zero).

---

## Getting the traditional display

The default is `fit = "contain"` / `align = center`. When the window has a different size from the
inner game screen, the game is scaled while preserving its aspect ratio and placed in the center.

If you want the traditional Kirikiri 2 / Kirikiri Z behavior of "the game stays at its original size in the top-left
even when the window is enlarged", specify the following explicitly.

```tjs
window.setViewport("none", 1.0, 0, 0);   // fit=none, zoom=1.0, alignX=0, alignY=0
```

!!! tip "Usually there is no difference"
    As long as you keep the inner size at "the primaryLayer size × the [setZoom](../../reference/Window.md#setzoom) factor"
    with [Window.setInnerSize](../../reference/Window.md#setinnersize), every fit mode displays the game at 1:1.
    Differences appear **when the user resizes or maximizes the window**, **when the window moves to a monitor
    with a different scale factor**, and **in environments where the window size cannot be changed (mobile /
    consoles)**.

---

## Conceptual model

```
[外側 surface] = Window.innerWidth / innerHeight = OS ウインドウ client
        │  ビューポート設定 (fit / zoom / align / offset)
        ▼
[内側ゲーム]  = primaryLayer のサイズ (TJS から setSize で指定)
```

(Outer surface = `Window.innerWidth` / `innerHeight` = the OS window's client area; the viewport settings
(fit / zoom / align / offset) map it to the inner game = the primaryLayer size, set from TJS with `setSize`.)

- **Outer surface** … [Window.innerWidth](../../reference/Window.md#innerwidth) /
  [Window.innerHeight](../../reference/Window.md#innerheight). The Elements UI
  overlay also uses this coordinate system.
- **Inner game** … The primaryLayer size. Determined by `primaryLayer.setSize(w, h)`,
  independently of [Window.setInnerSize](../../reference/Window.md#setinnersize).
- If the two match, the game is shown full-size at 1:1 as before. If they differ, the game is
  placed within the surface according to the settings, leaving a margin.

Mouse coordinates are automatically converted to game logical coordinates according to the placement, so
input reaches the game correctly with any fit/zoom.

---

## Fit modes

| Value | Behavior |
|---|---|
| `"contain"` | Largest size that fits while preserving aspect ratio (letterbox). **Default** |
| `"cover"` | Smallest size that fills while preserving aspect ratio (overflow is clipped) |
| `"fill"` | Stretched to the whole surface, ignoring aspect ratio |
| `"none"` | Original size (scale 1.0) |
| `"integer"` | Largest integer multiple that fits (at least 1×, preserving pixel-perfect scaling) |
| `"custom"` | Uses the scale in [Window.viewportZoom](../../reference/Window.md#viewportzoom) |

---

## Locking the window's aspect ratio (aspectLock)

The viewport decides "**how to place the game screen within the outer surface**";
the **shape** of the outer surface itself is left to user resizing and the platform.
Use [Window.aspectLock](../../reference/Window.md#aspectlock) when you want to lock it.

```tjs
window.aspectLock = "16:9";        // ウインドウの内側を 16:9 に固定
window.viewportFit = "integer";    // その中にゲーム画面をドットバイドットで配置
window.aspectLock = "";            // 固定を解除
```

This is useful when you want to **separate** the aspect ratio of the game screen (primaryLayer) from that of the
whole window. For example, the game screen may be 640x400 (8:5) while the whole window stays 16:9
and the game is placed inside it at an integer scale. If your UI (an Elements overlay, etc.) is designed
at a 16:9 base size, the UI and the game screen frame drift apart unless the window stays 16:9,
so this lock is needed.

Enabling it changes two things.

- User resizing of the window is constrained to this ratio (the ratio is kept even while
  dragging).
- [Window.setZoom](../../reference/Window.md#setzoom) determines the height from this ratio
  (previously it used "the primaryLayer size × the factor", so every time you set the factor
  the window reverted to the layer's ratio).

The inner size at the time of setting is also adjusted to this ratio, **based on the width**.

!!! warning "SDL3 / generic build only"
    In the native Windows (WINVER) build it does nothing. Setting it is ignored,
    and reading it always returns an empty string.

---

## TJS API

The following members have been added to the [Window](../../reference/Window.md) class.

### Properties

| Member | Description |
|---|---|
| [viewportFit](../../reference/Window.md#viewportfit) | Fit mode (string). Default `"contain"` |
| [viewportZoom](../../reference/Window.md#viewportzoom) | Scale for `"custom"`. Default 1.0 |
| [viewportAlignX](../../reference/Window.md#viewportalignx) | Horizontal alignment: 0=left / 0.5=center / 1=right |
| [viewportAlignY](../../reference/Window.md#viewportaligny) | Vertical alignment: 0=top / 0.5=center / 1=bottom |
| [viewportOffsetX](../../reference/Window.md#viewportoffsetx) | Horizontal offset (px) |
| [viewportOffsetY](../../reference/Window.md#viewportoffsety) | Vertical offset (px) |
| [viewportBgColor](../../reference/Window.md#viewportbgcolor) | Margin background color `0xAARRGGBB` ( the top 8 bits are alpha; use `0xff` for opaque. Default `0xff000000` ) |
| [aspectLock](../../reference/Window.md#aspectlock) | Locks the aspect ratio of the window itself (`"16:9"`, etc.). Default `""` = no lock. **SDL3 / generic build only** |

### Methods

| Member | Description |
|---|---|
| [setViewport](../../reference/Window.md#setviewport)(fit [,zoom [,alignX [,alignY [,offsetX [,offsetY]]]]]) | Sets the placement all at once |
| [setViewportWallpaper](../../reference/Window.md#setviewportwallpaper)(image [,fit [,alignX [,alignY]]]) | Sets a wallpaper image for the margin |
| [clearViewportWallpaper](../../reference/Window.md#clearviewportwallpaper)() | Removes the wallpaper |

For the wallpaper `image` you can pass a storage name (string), or a [Layer](../../reference/Layer.md) /
[Bitmap](../../reference/Bitmap.md) object directly (a reference to it is kept).

---

## Example

```tjs
var win = new Window();
win.setInnerSize(1280, 720);       // 外側ウインドウ

var lay = new Layer(win, null);    // primaryLayer
lay.setSize(640, 400);             // 内側ゲーム解像度
win.add(lay);

win.viewportBgColor = 0xff203060;  // 余白の色
win.viewportFit = "integer";       // 整数倍 (640x400 → 1280x800 は不可なので 1 倍)

// または 180% センタリング:
win.setViewport("custom", 1.8);

// 余白に壁紙 (ストレージ名でもオブジェクトでも可):
win.setViewportWallpaper("bg_pattern.png", "cover");
// win.setViewportWallpaper(myBitmap, "cover");   // Layer / Bitmap を直接渡す
```
