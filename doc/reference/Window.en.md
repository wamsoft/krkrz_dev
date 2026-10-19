# Window

The Window class manages a **window**.

## Members

### Constructors

- [Window](#window)

### Properties

- [visible](#visible)
- [caption](#caption)
- [width](#width)
- [height](#height)
- [minWidth](#minwidth)
- [minHeight](#minheight)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [left](#left)
- [top](#top)
- [focusable](#focusable)
- [trapKey](#trapkey)
- [innerWidth](#innerwidth)
- [innerHeight](#innerheight)
- [frameWidth](#framewidth)
- [frameHeight](#frameheight)
- [zoomNumer](#zoomnumer)
- [zoomDenom](#zoomdenom)
- [aspectLock](#aspectlock)
- [viewportFit](#viewportfit)
- [viewportZoom](#viewportzoom)
- [viewportAlignX](#viewportalignx)
- [viewportAlignY](#viewportaligny)
- [viewportOffsetX](#viewportoffsetx)
- [viewportOffsetY](#viewportoffsety)
- [viewportBgColor](#viewportbgcolor)
- [drawDevice](#drawdevice)
- [borderStyle](#borderstyle)
- [stayOnTop](#stayontop)
- [imeMode](#imemode)
- [mouseCursorState](#mousecursorstate)
- [useMouseKey](#usemousekey)
- [fullScreen](#fullscreen)
- [mainWindow](#mainwindow)
- [focusedLayer](#focusedlayer)
- [primaryLayer](#primarylayer)
- [HWND](#hwnd)
- [touchScaleThreshold](#touchscalethreshold)
- [touchRotateThreshold](#touchrotatethreshold)
- [touchPointCount](#touchpointcount)
- [enableTouch](#enabletouch)
- [waitVSync](#waitvsync)
- [hintDelay](#hintdelay)
- [displayOrientation](#displayorientation)
- [displayRotate](#displayrotate)
- [displayDensity](#displaydensity)
- [enableTouchMouse](#enabletouchmouse)
- [innerSunken](#innersunken)
- [layerEventTarget](#layereventtarget)
- [layerLeft](#layerleft)
- [layerTop](#layertop)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [mouseCursor](#mousecursor)
- [showScrollBars](#showscrollbars)
- [GLGetProcAddress](#glgetprocaddress)
- [maximized](#maximized)
- [minimized](#minimized)
- [disableResize](#disableresize)
- [disableMove](#disablemove)

### Methods

- [close](#close)
- [bringToFront](#bringtofront)
- [update](#update)
- [showModal](#showmodal)
- [setMaskRegion](#setmaskregion)
- [removeMaskRegion](#removemaskregion)
- [add](#add)
- [remove](#remove)
- [setSize](#setsize)
- [setMinSize](#setminsize)
- [setMaxSize](#setmaxsize)
- [setPos](#setpos)
- [setInnerSize](#setinnersize)
- [setZoom](#setzoom)
- [setViewport](#setviewport)
- [setViewportWallpaper](#setviewportwallpaper)
- [clearViewportWallpaper](#clearviewportwallpaper)
- [postInputEvent](#postinputevent)
- [hideMouseCursor](#hidemousecursor)
- [registerMessageReceiver](#registermessagereceiver)
- [postMessage](#postmessage)
- [getTouchPoint](#gettouchpoint)
- [getMouseVelocity](#getmousevelocity)
- [getTouchVelocity](#gettouchvelocity)
- [resetMouseVelocity](#resetmousevelocity)
- [beginMove](#beginmove)
- [requestUpdate](#requestupdate)
- [setLayerPos](#setlayerpos)
- [maximize](#maximize)
- [minimize](#minimize)
- [showRestore](#showrestore)
- [getNormalRect](#getnormalrect)
- [getWindowRect](#getwindowrect)
- [getClientRect](#getclientrect)
- [setCursorPos](#setcursorpos)
- [getCursorPos](#getcursorpos)
- [setClientRect](#setclientrect)
- [registerExEvent](#registerexevent)
- [registerDeviceChange](#registerdevicechange)

### Events

- [onMouseEnter](#onmouseenter)
- [onMouseLeave](#onmouseleave)
- [onClick](#onclick)
- [onDoubleClick](#ondoubleclick)
- [onMouseDown](#onmousedown)
- [onMouseUp](#onmouseup)
- [onMouseMove](#onmousemove)
- [onMouseWheel](#onmousewheel)
- [onTouchDown](#ontouchdown)
- [onTouchUp](#ontouchup)
- [onTouchMove](#ontouchmove)
- [onTouchScaling](#ontouchscaling)
- [onTouchRotate](#ontouchrotate)
- [onMultiTouch](#onmultitouch)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [onKeyPress](#onkeypress)
- [onTextInput](#ontextinput)
- [onResize](#onresize)
- [onFileDrop](#onfiledrop)
- [onCloseQuery](#onclosequery)
- [onPopupHide](#onpopuphide)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [onHintChanged](#onhintchanged)
- [onDisplayRotate](#ondisplayrotate)
- [onPointerDown](#onpointerdown)
- [onPointerMove](#onpointermove)
- [onPointerUp](#onpointerup)
- [onMaximizeQuery](#onmaximizequery)
- [onMove](#onmove)
- [onMoving](#onmoving)
- [onResizing](#onresizing)
- [onMoveSizeBegin](#onmovesizebegin)
- [onMoveSizeEnd](#onmovesizeend)
- [onMinimize](#onminimize)
- [onMaximize](#onmaximize)
- [onDPIChanged](#ondpichanged)
- [onDisplayChanged](#ondisplaychanged)
- [onDeviceChanged](#ondevicechanged)
- [onPaste](#onpaste)

---

### Window

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `parent` | `&nbsp;` | Parent window.<br>If a parent window is given, the window is created as its child.<br>Omit it if not needed. |

**Description**

Constructs a Window object

Constructs an object of the Window class.

The window is created hidden, and its position and size are undefined (some arbitrary position and size).

---

### visible

Property \ Access: `r/w`

**Description**

Whether the window is visible

Indicates whether the window is visible. This property can also be set.

If true, the window is visible; if false, it is hidden.

---

### caption

Property \ Access: `r/w`

**Description**

Window caption

The window **caption** (the title in the title bar).
This property can also be set.

---

### width

Property \ Access: `r/w`

**Description**

Window width

The window width (the outer width including window decorations). This property can also be set.

!!! tip "Prefer the inner (drawing area) based API"
    This value is the size of the **outer frame including window decorations**. Whether decorations exist and how thick they are
    depends on the platform, the OS theme and [Window.borderStyle](Window.md#borderstyle);
    in environments without decorations (mobile / consoles, or with `bsNone`) it is
    equal to the inner size. For portable code, use
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize), which correspond directly to the game screen.
    When you need the frame, you can add [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight).

**See also:** [Window.innerWidth](Window.md#innerwidth) / [Window.frameWidth](Window.md#framewidth) / [Window.height](Window.md#height) / [Window.setSize](Window.md#setsize)

---

### height

Property \ Access: `r/w`

**Description**

Window height

The window height (the outer height including window decorations). This property can also be set.

!!! tip "Prefer the inner (drawing area) based API"
    This value is the size of the **outer frame including window decorations**. Whether decorations exist and how thick they are
    depends on the platform, the OS theme and [Window.borderStyle](Window.md#borderstyle);
    in environments without decorations (mobile / consoles, or with `bsNone`) it is
    equal to the inner size. For portable code, use
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize), which correspond directly to the game screen.
    When you need the frame, you can add [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight).

**See also:** [Window.innerHeight](Window.md#innerheight) / [Window.frameHeight](Window.md#frameheight) / [Window.width](Window.md#width) / [Window.setSize](Window.md#setsize)

---

### minWidth

Property \ Access: `r/w`

**Description**

Minimum window width

The minimum window width (inner = drawing area width). This property can also be set. 0 removes the limit.

**See also:** [Window.innerWidth](Window.md#innerwidth) / [Window.minHeight](Window.md#minheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### minHeight

Property \ Access: `r/w`

**Description**

Minimum window height

The minimum window height (inner = drawing area height). This property can also be set. 0 removes the limit.

**See also:** [Window.innerHeight](Window.md#innerheight) / [Window.minWidth](Window.md#minwidth) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxWidth

Property \ Access: `r/w`

**Description**

Maximum window width

The maximum window width (inner = drawing area width). This property can also be set. 0 removes the limit.

**See also:** [Window.innerWidth](Window.md#innerwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxHeight

Property \ Access: `r/w`

**Description**

Maximum window height

The maximum window height (inner = drawing area height). This property can also be set. 0 removes the limit.

**See also:** [Window.innerHeight](Window.md#innerheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### left

Property \ Access: `r/w`

**Description**

Left edge position of the window

The left edge position of the window. This property can also be set.

The left edge position is the x coordinate from the screen origin (top-left corner).

**See also:** [Window.top](Window.md#top) / [Window.setPos](Window.md#setpos)

---

### top

Property \ Access: `r/w`

**Description**

Top edge position of the window

The top edge position of the window. This property can also be set.

The top edge position is the y coordinate from the screen origin (top-left corner).

**See also:** [Window.left](Window.md#left) / [Window.setPos](Window.md#setpos)

---

### focusable

Property \ Access: `r/w`

**Description**

Whether the window can receive focus

Indicates whether the window can receive focus. This property can also be set.

If set to false, the window can no longer receive focus, i.e. it never becomes active. As a side effect, you can no longer move the window by dragging the title bar, resize it, or close it with the close button.

To get keyboard input, you can use the [Window.trapKey](Window.md#trapkey) property.

This is normally used to implement windows that appear frontmost but do not take focus themselves, such as popup menus.

In the current version, this setting may be lost when the window switches to or returns from full screen.

**See also:** [Window.trapKey](Window.md#trapkey) / [Window.onPopupHide](Window.md#onpopuphide)

---

### trapKey

Property \ Access: `r/w`

**Description**

Whether to trap key input

Indicates whether to trap key input. This property can also be set.

If set to true, key input events that occur in other windows are intercepted and fired on this window.

If this property is true on multiple windows, key input events fire on the most recently created one.

**See also:** [Window.focusable](Window.md#focusable)

---

### innerWidth

Property \ Access: `r/w`

**Description**

Width of the client area

The width of the client area.
This property can also be set.

**See also:** [Window.innerHeight](Window.md#innerheight) / [Window.setInnerSize](Window.md#setinnersize)

---

### innerHeight

Property \ Access: `r/w`

**Description**

Height of the client area

The height of the client area.
This property can also be set.

**See also:** [Window.innerWidth](Window.md#innerwidth) / [Window.setInnerSize](Window.md#setinnersize)

---

### frameWidth

Property \ Access: `r/w`

**Description**

Width of the window decorations

The difference between the outer width and the inner (drawing area) width of the window ( = [Window.width](Window.md#width) - [Window.innerWidth](Window.md#innerwidth) ). This is the left and right frames combined.

It is 0 in environments without window decorations (mobile / consoles, and when [Window.borderStyle](Window.md#borderstyle) is `bsNone`).

Useful for converting code written against the outer size to the inner size. Read-only.

**See also:** [Window.frameHeight](Window.md#frameheight) / [Window.width](Window.md#width) / [Window.innerWidth](Window.md#innerwidth)

---

### frameHeight

Property \ Access: `r/w`

**Description**

Height of the window decorations

The difference between the outer height and the inner (drawing area) height of the window ( = [Window.height](Window.md#height) - [Window.innerHeight](Window.md#innerheight) ). This is the title bar and the top and bottom frames combined.

It is 0 in environments without window decorations (mobile / consoles, and when [Window.borderStyle](Window.md#borderstyle) is `bsNone`).

Useful for converting code written against the outer size to the inner size. Read-only.

**See also:** [Window.frameWidth](Window.md#framewidth) / [Window.height](Window.md#height) / [Window.innerHeight](Window.md#innerheight)

---

### zoomNumer

Property \ Access: `r/w`

**Description**

Layer zoom ratio (numerator)

The numerator of the layer zoom ratio.
This property can technically be set, but use the [Window.setZoom](Window.md#setzoom) method to set it.

The denominator is given by the [Window.zoomDenom](Window.md#zoomdenom) property.

See the [Window.setZoom](Window.md#setzoom) method for details.

**See also:** [Window.setZoom](Window.md#setzoom) / [Window.zoomDenom](Window.md#zoomdenom)

---

### zoomDenom

Property \ Access: `r/w`

**Description**

Layer zoom ratio (denominator)

The denominator of the layer zoom ratio.
This property can technically be set, but use the [Window.setZoom](Window.md#setzoom) method to set it.

The numerator is given by the [Window.zoomNumer](Window.md#zoomnumer) property.

See the [Window.setZoom](Window.md#setzoom) method for details.

**See also:** [Window.setZoom](Window.md#setzoom) / [Window.zoomNumer](Window.md#zoomnumer)

---

### aspectLock

Property \ Access: `r/w`

**Description**

Locks the window aspect ratio

Locks the aspect ratio of the inner area of the window ( [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) ). Specify a string in `"width:height"` form such as `"16:9"`; setting an empty string `""` removes the lock. The default is `""` (no lock). The value can also be read.

Use this when you want to **separate** the aspect ratio of the game screen (primaryLayer) from that of the whole window. For example, you can keep the whole window at 16:9 while placing a 640x400 (8:5) game screen inside it pixel-perfect ( `viewportFit = "integer"` ) or fitted ( `"contain"` ). If your UI (Elements, etc.) is designed at a 16:9 base size and the window is not kept at 16:9, the UI and the game screen frame will be misaligned.

When the lock is enabled,

- user resizing of the window is constrained to this ratio (the ratio is kept even while dragging).
- [Window.setZoom](Window.md#setzoom) determines the height from this ratio (previously it used "primaryLayer size × ratio", so the window reverted to the layer's aspect ratio every time the zoom was set).
- the inner size at the time of setting is also adjusted to this ratio, **based on the width**.

How the game screen is placed within that frame is still determined by the viewport settings such as [Window.viewportFit](Window.md#viewportfit). This property determines only the shape of the window.

```
window.aspectLock = "16:9";        // ウインドウを 16:9 に固定
window.viewportFit = "integer";    // その中にゲーム画面をドットバイドットで配置
window.aspectLock = "";            // 固定を解除
```

!!! warning "SDL3 / generic builds only"
    In the native Windows (WINVER) build this **does nothing**. Setting it is ignored, and reading it always returns an empty string.

!!! note "Limitation on macOS"
    On macOS, even after a locked ratio is released with `""`, the constraint on user resizing remains until the window is recreated (the value reads back as empty). This avoids an OS-side bug that crashes on window operations. For the same reason, switching ratios (such as `"4:3"` → `"16:9"`) may leave the previous constraint in place.

**See also:** [Window.viewportFit](Window.md#viewportfit) / [Window.setZoom](Window.md#setzoom) / [Window.setInnerSize](Window.md#setinnersize)

---

### viewportFit

Property \ Access: `r/w`

**Description**

Viewport fit mode

A string indicating how the inner game screen is fitted into the outer window (surface).
This property can also be set.

One of `"contain"` (largest size that fits while keeping the aspect ratio, letterboxed; default) / `"cover"` (smallest size that fills while keeping the aspect ratio; overflow is clipped) / `"fill"` (stretch to fill, ignoring the aspect ratio) / `"none"` (original size) / `"integer"` (largest integer multiple that fits; at least 1x) / `"custom"` (use the ratio in [Window.viewportZoom](Window.md#viewportzoom)).


!!! note "For the same display as legacy versions (Kirikiri 2 / Kirikiri Z)"
    The default `"contain"` scales the game while keeping the aspect ratio when the window
    has a different size from the inner game screen. If you want the **legacy display**, where the game stays
    at its original size in the top-left even when the window is enlarged,
    explicitly set `viewportFit = "none"` and [Window.viewportAlignX](Window.md#viewportalignx) /
    [Window.viewportAlignY](Window.md#viewportaligny) `= 0`.

    As long as you keep the inner size of the window equal to "primaryLayer size × the
    [Window.setZoom](Window.md#setzoom) ratio" with [Window.setInnerSize](Window.md#setinnersize),
    every fit mode displays at 1:1, so there is no difference.
    Differences appear when the user resizes or maximizes the window, when it is moved to a monitor
    with a different scaling factor, and in environments where the window size cannot be changed
    (mobile / consoles).

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.setViewport](Window.md#setviewport) / [Window.viewportZoom](Window.md#viewportzoom)

---

### viewportZoom

Property \ Access: `r/w`

**Description**

Viewport zoom ratio

A real number giving the zoom ratio used when [Window.viewportFit](Window.md#viewportfit) is `"custom"` (e.g. 1.8 = 180%). The default is 1.0.
This property can also be set.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportFit](Window.md#viewportfit) / [Window.setViewport](Window.md#setviewport)

---

### viewportAlignX

Property \ Access: `r/w`

**Description**

Viewport horizontal alignment

A real number giving the horizontal alignment of the inner game screen when margins appear. 0 = left / 0.5 = center / 1 = right. The default is 0.5.
This property can also be set.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportAlignY](Window.md#viewportaligny) / [Window.setViewport](Window.md#setviewport)

---

### viewportAlignY

Property \ Access: `r/w`

**Description**

Viewport vertical alignment

A real number giving the vertical alignment of the inner game screen when margins appear. 0 = top / 0.5 = center / 1 = bottom. The default is 0.5.
This property can also be set.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportAlignX](Window.md#viewportalignx) / [Window.setViewport](Window.md#setviewport)

---

### viewportOffsetX

Property \ Access: `r/w`

**Description**

Viewport horizontal offset

An integer giving the horizontal offset of the inner game screen added after alignment (px, surface coordinates).
This property can also be set.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportOffsetY](Window.md#viewportoffsety) / [Window.setViewport](Window.md#setviewport)

---

### viewportOffsetY

Property \ Access: `r/w`

**Description**

Viewport vertical offset

An integer giving the vertical offset of the inner game screen added after alignment (px, surface coordinates).
This property can also be set.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportOffsetX](Window.md#viewportoffsetx) / [Window.setViewport](Window.md#setviewport)

---

### viewportBgColor

Property \ Access: `r/w`

**Description**

Background color of viewport margins

The background color used to fill margins created by the viewport, as an integer in `0xAARRGGBB` form (the upper 8 bits are alpha; add `0xff` for an opaque color). The default is `0xff000000` (opaque black).
This property can also be set. If a wallpaper ([Window.setViewportWallpaper](Window.md#setviewportwallpaper)) is set, the wallpaper takes priority.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.setViewportWallpaper](Window.md#setviewportwallpaper) / [Window.setViewport](Window.md#setviewport)

---

### drawDevice

Property \ Access: `r/w`

**Description**

Draw device

The draw device object.

This property can also be set. When set, the draw device previously assigned to this window is automatically
invalidated.

The default instance depends on the build. In the native Windows (WINVER) build it is
[Window.BasicDrawDevice](Window.BasicDrawDevice.md) (Direct3D 11); in the SDL3 build it is
[SDLOGLDrawDevice](SDLOGLDrawDevice.md) (in builds with OpenGL enabled; in builds without it,
[SDLDrawDevice](SDLDrawDevice.md), and in builds that run Canvas on SDL_GPU, [GPUDrawDevice](GPUDrawDevice.md)). The default at startup can be chosen
with the `-drawdevice` command-line option ( [Command-line options](../guide/CommandLine.md) ). Note that when an SDL3 build is
started with `-drawdevice=sdl`, you cannot switch to an OpenGL-based device at runtime.

To use a custom draw device (one provided by a plugin), follow that plugin's
documentation.

---

### borderStyle

Property \ Access: `r/w`

**Description**

Window appearance

The appearance of the window. This property can also be set.

The following values can be set.

`**bsDialog**      :` Non-resizable, with an appearance like a dialog box.

`**bsSingle**      :` Non-resizable window.

`**bsNone**        :` Window without a border.

`**bsSizeable**    :` Ordinary resizable window. This is the default.

`**bsToolWindow**  :` Non-resizable tool window (a window with a small caption).

`**bsSizeToolWin** :` Like bsToolWindow, but resizable.

---

### stayOnTop

Property \ Access: `r/w`

**Description**

Whether to always stay on top

Indicates whether the window always stays on top (frontmost). This property can also be set.

If true, the window always stays on top.

In the current version, this setting may be lost when the window switches to or returns from full screen.

---

### imeMode

Property \ Access: `r/w`

**Description**

Default IME mode

The default IME mode.

The mode given here is applied when no layer has focus.

If not specified, it is **imClose**, meaning the IME is closed (alphanumeric input) when no layer has focus.

For the allowed values, see [Layer.imeMode](Layer.md#imemode).

Writing is effective only in the native Windows (WINVER) build. In the SDL3 build,
both reading and writing are not implemented (an exception is thrown).

The setting takes effect immediately when no layer has focus. When a layer has focus,
that layer's [Layer.imeMode](Layer.md#imemode) takes priority,
and the default given here is restored when focus leaves.

While a text input field of an ElementsDialog has editing focus, the IME is open regardless of this setting
(when focus leaves, the default given here is restored).
During that time, applying the layer's [Layer.imeMode](Layer.md#imemode) is also deferred,
and it is applied when focus leaves.

Note that this property returns only the **default**. It does not return the IME state actually applied
by the focused layer or an ElementsDialog, so it cannot be used to check whether the IME is open
(use `textFocus` of [Agent.dialogs](Agent.md#dialogs) for that).

---

### mouseCursorState

Property \ Access: `r/w`

**Description**

Mouse cursor visibility state

The visibility state of the mouse cursor. This property can also be set.

With `**mcsVisible**`, the mouse cursor is visible. This is the default.

With `**mcsTempHidden**`, the mouse cursor is hidden, but as soon as the mouse moves even slightly it changes to `mcsVisible` and becomes visible. Calling the [Window.hideMouseCursor](Window.md#hidemousecursor) method puts it in this state.

With `**mcsHidden**`, the mouse cursor is hidden. It does not become visible even when the mouse moves.

---

### useMouseKey

Property \ Access: `r/w`

**Description**

Whether to use mouse keys

Indicates whether to use mouse keys. This property can also be set.

If true, mouse keys can be used.

When mouse keys are enabled, you can move the mouse cursor with the cursor keys,
but no key input events fire at all.

---

### fullScreen

Property \ Access: `r/w`

**Description**

Whether in full screen

Indicates whether the window is in **full screen**. This property can also be set.

If true, the client area of the current window becomes full screen. The screen resolution in full screen
is the size of the client area.

If false, the window is shown in windowed mode.

---

### mainWindow

Property \ Access: `r`

**Description**

Main window

The main window (the first window created).

---

### focusedLayer

Property \ Access: `r/w`

**Description**

Layer object that has focus

The layer object that currently has **focus**.
This property can also be set.

If null, no layer has focus. Setting a layer object
moves focus to that layer.

---

### primaryLayer

Property \ Access: `r`

**Description**

Primary layer object

The **primary layer** object.

---

### HWND

Property \ Access: `r`

**Description**

Window handle

The window handle.

It is returned as an integer; when using this value in a plugin or the like, cast it to the HWND type.

**See also:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### touchScaleThreshold

Property \ Access: `r/w`

**Description**

Multi-touch zoom threshold

The threshold for starting a multi-touch zoom.

A zoom event fires when the distance between the two touch points changes by this value or more.

Once the threshold is exceeded, zoom events stay enabled until the fingers are lifted.

**See also:** [Window.onTouchScaling](Window.md#ontouchscaling)

---

### touchRotateThreshold

Property \ Access: `r/w`

**Description**

Multi-touch rotation threshold

The threshold for starting a multi-touch rotation.

A rotate event fires when the movement distance of each touch point changes by this value or more.

Once the threshold is exceeded, rotate events stay enabled until the fingers are lifted.

**See also:** [Window.onTouchRotate](Window.md#ontouchrotate)

---

### touchPointCount

Property \ Access: `r`

**Description**

Number of touches

The number of points currently touching the touch panel.

**See also:** [Window.getTouchPoint](Window.md#gettouchpoint)

---

### enableTouch

Property \ Access: `r/w`

**Description**

Enables / disables touch events

Indicates whether **touch events** are enabled. This property can also be set.

If true, events such as [Window.onTouchDown](Window.md#ontouchdown) are enabled, and touch operations no longer fire [Window.onMouseDown](Window.md#onmousedown) and the like.

In environments with a touch device and multi-touch enabled, the default is true.

---

### waitVSync

Property \ Access: `r/w`

**Description**

Wait for vertical sync

Whether to wait for the display's vertical sync before drawing, e.g. during transitions (screen switching).

Changing this may reduce screen flicker, but may also lower drawing performance.

The default is true (to suppress excessive redraws that push out too many frames in scenes with light drawing). Set it to false if you want to always redraw as before.

---

### hintDelay

Property \ Access: `r/w`

**Description**

Hint display delay

The delay before showing a hint, in milliseconds. This property can also be set.

The default is 500 milliseconds.

If set to 0, [Window.onHintChanged](Window.md#onhintchanged) is called immediately (always shown).

If set to -1, hints are never shown.

**See also:** [Window.onHintChanged](Window.md#onhintchanged)

---

### displayOrientation

Property \ Access: `r`

**Description**

Display orientation (1.1.0 and later)

The orientation of the display.

One of oriUnknown (failed to get / unknown), oriPortrait (portrait), or oriLandscape (landscape).

**See also:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayRotate](Window.md#displayrotate)

---

### displayRotate

Property \ Access: `r`

**Description**

Display rotation angle (1.1.0 and later)

The rotation angle of the display.

One of 0, 90, 180, 270, or -1; it is -1 if it could not be obtained.

**See also:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayOrientation](Window.md#displayorientation)

---

### displayDensity

Property \ Access: `r/w`

**Description**

Display density (dpi)

Returns the dpi value (96 is 1x = 100%; 192 is 200%).
Read-only.

Returns the value of the display the window is on. With multiple displays, the value changes
when the window moves to a monitor with a different scaling factor.

!!! note "Moving to another monitor does not change the window size"
Even when moved to a monitor with a different scaling factor,
[Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)
(the pixel size of the drawing area) are kept. Only the frame thickness changes,
and the game screen looks the same. On the other hand, on a monitor with a higher scaling factor
the window appears smaller.
Both the native Windows (WINVER) build and the SDL3 / generic builds
return the actual value (the SDL3 side was fixed at 96 until 2026-08-17).

---

### enableTouchMouse

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Enables / disables mouse emulation for touch

If true, touch events are converted into pseudo mouse events and
delivered to the `Window.onMouseDown` family of handlers.

!!! note "Touch on iOS / iPadOS (since 2026-10)"
    On iOS, the engine converts touches to mouse events itself and adds the following two-finger gestures.
    Setting this property to false stops the conversion, including the gestures.

    | Gesture | What is delivered |
    |---|---|
    | Touch with one finger | Left button press after a hold of about 100 ms (confirmed as soon as the finger starts moving). After that, ordinary drag / click |
    | Tap with two fingers (lift without moving) | ESC key ("back"; delivered as a key event, so it can be handled with `onKeyDown` or hotkeys) |
    | Move two fingers up or down | Mouse wheel (fingers up = scroll down) |

    If the second finger touches within about 100 ms after the first, it becomes a two-finger gesture and no left click occurs.
    Coordinates are delivered in game screen coordinates (the drawing area, taking letterboxing into account).

---

### innerSunken

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Enables / disables the sunken inner border (deprecated)

If true, a "sunken" style border is shown around the client area of the window.
A compatibility property for builds with `USE_OBSOLETE_FUNCTIONS` enabled;
not recommended for new code.

---

### layerEventTarget

Property \ Access: `r/w`

**Description**

Target object for layer events

Specifies the object that receives layer events such as mouse and key input.
Normally the `Window` itself is used. Setting null restores the default.

---

### layerLeft

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

X position of the primary layer (deprecated)

Gets or sets the left edge position of the primary layer within the client area of the window.
A compatibility property for builds with `USE_OBSOLETE_FUNCTIONS` enabled.
In new code, use the alternative path of `Window.setLayerPos`.

---

### layerTop

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Y position of the primary layer (deprecated)

Gets or sets the top edge position of the primary layer within the client area of the window.
A compatibility property for builds with `USE_OBSOLETE_FUNCTIONS` enabled.

---

### layerTreeOwnerInterface

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

LayerTreeOwner interface pointer

Returns the C++ pointer to the `iTVPLayerTreeOwner` interface as a 64-bit integer.
Used by plugins to access the window's layer tree owner directly.
Read-only.

---

### mouseCursor

Property \ Access: `r/w`

**Description**

Mouse cursor setting

Gets or sets the current mouse cursor.

If a string is given when setting, a cursor image is loaded using it as a storage name.
If a number is given, it is interpreted as a standard mouse cursor constant (`crArrow`, etc.).

**See also:** [Window.mouseCursorState](Window.md#mousecursorstate)

---

### showScrollBars

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Enables / disables scroll bars (deprecated)

Gets or sets whether to show scroll bars when the primary layer is larger than the window.
A compatibility property for builds with `USE_OBSOLETE_FUNCTIONS` enabled.

---

### GLGetProcAddress

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pointer to the GL entry point resolver function (integer)

Used as oglbase by GLES-based plugins (EffekseerDevice, etc.). On first
access, if the GL context has not been initialized yet, it is created lazily and made current
(it can be obtained from the window even when using OGLDrawDevice / Canvas). In environments where GL
cannot be obtained, it returns 0 (null).

---

### maximized

Property \ Access: `r`

**Type**: `Boolean`

**Description**

Whether maximized

True if the window is maximized. To change it, use
[Window.maximize](Window.md#maximize) / [Window.showRestore](Window.md#showrestore).

Available in both WINVER and SDL3-based builds.

**See also:** [Window.maximize](Window.md#maximize) / [Window.minimized](Window.md#minimized)

---

### minimized

Property \ Access: `r`

**Type**: `Boolean`

**Description**

Whether minimized

True if the window is minimized (iconified).

**See also:** [Window.minimize](Window.md#minimize) / [Window.maximized](Window.md#maximized)

---

### disableResize

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Disables resizing

If true, the user can no longer resize the window by dragging its frame.
Also effective in SDL3-based builds.

**See also:** [Window.disableMove](Window.md#disablemove)

---

### disableMove

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Disables moving

If true, the user can no longer move the window by dragging it.
Used when showing the window without a frame.

Effective only in the WINVER build. SDL3-based builds only store the value
(because SDL has no way to stop moving).

**See also:** [Window.disableResize](Window.md#disableresize)

---

### close

Method

**Description**

Closes the window

Closes a window shown with the [Window.showModal](Window.md#showmodal) method. Before the window closes, the [Window.onCloseQuery](Window.md#onclosequery) event fires, which lets you confirm whether the window can be closed.

**See also:** [Window.showModal](Window.md#showmodal) / [Window.onCloseQuery](Window.md#onclosequery)

---

### bringToFront

Method

**Description**

Brings the window to the front

Brings the window to the front. If the application is inactive, it also activates the application itself.

---

### update

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `tutNormal` | Type of window drawing.<br>`**tutNormal**` draws normally (incremental drawing);<br>`**tutEntire**` draws the entire window contents. |

**Description**

Forces the window contents to be drawn

The argument is ignored in the current version.

tutNormal and tutEntire are not implemented.

---

### showModal

Method

**Description**

Shows the window modally

Shows the window **modally**.
This method makes the window visible
and temporarily disables the other windows, so that the user can access only this window
(this is called the modal state). When the window is closed,
the modal state ends.

The window must be hidden when this method is called.
Also, it cannot be called when there is only one window (an exception is thrown).

When [Window.close](Window.md#close) is called or the window's
close button is pressed, the window leaves the modal state and `showModal` returns.

> In environments where multiple windows cannot be created (mobile / consoles, etc.),
> the second window itself cannot be created, so an exception is thrown. In such environments,
> design without modal windows.

While in the modal state, a nested event loop runs internally, so **drawing, timers and
continuous handlers keep running**. Only user input to other windows is blocked.
Available in both the native Windows (WINVER) build and the SDL3 build
(the SDL3 build supports it since 2026-08-15).

The core demo `window_multi` shows this in action.

---

### setMaskRegion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `threshold` | `1` | Mask threshold.<br>The window is cut out to the shape of the parts of the primary layer's mask (layer opacity information)<br>that are greater than this value. |

**Description**

Sets the window region from the mask

Sets the window region according to the mask (layer opacity information) of the primary layer.

This lets you make the window an irregular shape.

To keep the displayed primary layer aligned with the window size and position,
you need to do the following.

- Set [Window.borderStyle](Window.md#borderstyle) to bsNone.
- Set [Layer.imageLeft](Layer.md#imageleft) and [Layer.imageTop](Layer.md#imagetop) to 0.

**See also:** [Window.removeMaskRegion](Window.md#removemaskregion)

---

### removeMaskRegion

Method

**Description**

Removes the window region

Removes the window region set with [Window.setMaskRegion](Window.md#setmaskregion) and returns the window to a rectangle.

**See also:** [Window.setMaskRegion](Window.md#setmaskregion)

---

### add

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `object` | `&nbsp;` | Object to be managed. |

**Description**

Adds a managed object

Adds a managed object. The object given here is automatically invalidated
when the window is invalidated.

**See also:** [Window.remove](Window.md#remove)

---

### remove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `object` | `&nbsp;` | Object to remove from the list of managed objects. |

**Description**

Removes a managed object

Removes the given object from the list of managed objects.

**See also:** [Window.add](Window.md#add)

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Window width. |
| `height` | `&nbsp;` | Window height. |

**Description**

Sets the window size

Sets the size of the window.

When setting the window size, it is more efficient to set it at once with this method
than to set the [Window.width](Window.md#width) and
[Window.height](Window.md#height) properties individually.

!!! tip "Prefer the inner (drawing area) based API"
    This value is the size of the **outer frame including window decorations**. Whether decorations exist and how thick they are
    depends on the platform, the OS theme and [Window.borderStyle](Window.md#borderstyle);
    in environments without decorations (mobile / consoles, or with `bsNone`) it is
    equal to the inner size. For portable code, use
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize), which correspond directly to the game screen.
    When you need the frame, you can add [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight).

**See also:** [Window.width](Window.md#width) / [Window.height](Window.md#height) / [Window.setPos](Window.md#setpos) / [Window.setInnerSize](Window.md#setinnersize) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize)

---

### setMinSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Minimum window width. 0 removes the limit. |
| `height` | `&nbsp;` | Minimum window height. 0 removes the limit. |

**Description**

Sets the minimum window size

Sets the minimum size of the window. The window cannot become smaller than the size given here.

!!! note "Based on the inner (drawing area) size"
    The values are the size of the drawing area excluding the window frame, the same as
    [Window.innerWidth](Window.md#innerwidth) /
    [Window.innerHeight](Window.md#innerheight) (changed from the outer size on 2026-08-17,
    because an outer size cannot be defined on platforms without decorations). If you need values including the frame,
    add [Window.frameWidth](Window.md#framewidth) / [Window.frameHeight](Window.md#frameheight).

**See also:** [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight)

---

### setMaxSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Maximum window width. 0 removes the limit. |
| `height` | `&nbsp;` | Maximum window height. 0 removes the limit. |

**Description**

Sets the maximum window size

Sets the maximum size of the window. The window cannot become larger than the size given here.

!!! note "Based on the inner (drawing area) size"
    The values are the size of the drawing area excluding the window frame, the same as
    [Window.innerWidth](Window.md#innerwidth) /
    [Window.innerHeight](Window.md#innerheight) (changed from the outer size on 2026-08-17,
    because an outer size cannot be defined on platforms without decorations). If you need values including the frame,
    add [Window.frameWidth](Window.md#framewidth) / [Window.frameHeight](Window.md#frameheight).

**See also:** [Window.setMinSize](Window.md#setminsize) / [Window.setSize](Window.md#setsize) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight)

---

### setPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge position of the window. |
| `top` | `&nbsp;` | Top edge position of the window. |

**Description**

Sets the window position

Sets the position of the window.

When setting the window position, it is more efficient to set it at once with this method
than to set the [Window.left](Window.md#left) and
[Window.top](Window.md#top) properties individually.

**See also:** [Window.left](Window.md#left) / [Window.top](Window.md#top) / [Window.setSize](Window.md#setsize)

---

### setInnerSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Client width. |
| `height` | `&nbsp;` | Client height. |

**Description**

Sets the client size

Sets the client size of the window.

The client is the area inside the window where layers can be displayed.

Setting this size also changes the window size accordingly.

When setting the client size, it is more efficient to set it at once with this method
than to set the [Window.innerWidth](Window.md#innerwidth) and
[Window.innerHeight](Window.md#innerheight) properties individually.

**See also:** [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)

---

### setZoom

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `numer` | `&nbsp;` | Numerator of the ratio, as an integer. |
| `denom` | `&nbsp;` | Denominator of the ratio, as an integer. |

**Description**

Sets the layer zoom ratio

Sets the zoom ratio of the layers. The image is displayed enlarged or reduced by numerator/denominator.

If the numerator and denominator have a common divisor, the fraction is reduced automatically, so the values read from the [Window.zoomNumer](Window.md#zoomnumer) and [Window.zoomDenom](Window.md#zoomdenom) properties may differ from the values given to this method.

In the current version of Kirikiri, whether interpolation is applied when scaling depends on the graphics card hardware and driver. With hardware or drivers that do not interpolate, image quality is coarse.

Depending on options, Kirikiri examines the hardware available for scaling every time the ratio changes, so this method is not suitable for effects that change the zoom ratio continuously.

This method means "make the inner size of the window ( [Window.innerWidth](Window.md#innerwidth) /
[Window.innerHeight](Window.md#innerheight) ) equal to the layer size times the ratio".
The window is resized to that size, and the contents are scaled by the ratio.
The behavior is the same in the native Windows (WINVER) build and the SDL3 / generic builds
(the WINVER side was aligned on 2026-08-17; before that it only remembered the ratio and
did not resize the window, so you had to set the size explicitly with [Window.setInnerSize](Window.md#setinnersize)).

!!! note "When the window cannot be resized"
    In environments where the window size cannot be changed (mobile / consoles, etc.), or when the requested size is
    below the OS minimum window size, the inner size may not be as specified.
    Even then, the game screen is placed inside according to the
    [Window.setViewport](Window.md#setviewport) settings.

**See also:** [Window.zoomNumer](Window.md#zoomnumer) / [Window.zoomDenom](Window.md#zoomdenom)

---

### setViewport

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fit` | `&nbsp;` | Fit mode, as a string. One of `"contain"` (largest size that fits while keeping the aspect ratio, letterboxed; default) / `"cover"` (smallest size that fills while keeping the aspect ratio; overflow is clipped) / `"fill"` (stretch to fill, ignoring the aspect ratio) / `"none"` (original size) / `"integer"` (largest integer multiple that fits; at least 1x) / `"custom"` (use the ratio in [Window.viewportZoom](Window.md#viewportzoom)). |
| `zoom` | `&nbsp;` | Zoom ratio for `"custom"`, as a real number (e.g. 1.8 = 180%). |
| `alignX` | `&nbsp;` | Horizontal alignment, as a real number. 0 = left / 0.5 = center / 1 = right. |
| `alignY` | `&nbsp;` | Vertical alignment, as a real number. 0 = top / 0.5 = center / 1 = bottom. |
| `offsetX` | `&nbsp;` | Horizontal offset added after alignment, as an integer (px, surface coordinates). |
| `offsetY` | `&nbsp;` | Vertical offset added after alignment, as an integer (px). |

**Description**

Sets the viewport (display framing) at once

Sets, all at once, how the inner game screen (the size of primaryLayer) is placed inside the outer window (the surface represented by [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)). If the two sizes match, the game is shown full-size at 1:1 as before; if they differ, the game is placed in the surface according to these settings and margins appear. The margins can be filled with [Window.viewportBgColor](Window.md#viewportbgcolor) or [Window.setViewportWallpaper](Window.md#setviewportwallpaper) (available in both the native Windows (WINVER) build and the SDL3 / generic builds; WINVER support since 2026-08-17).

Mouse coordinates are automatically converted to game logical coordinates according to the placement, so input reaches the game correctly with any setting.

Each argument is equivalent to setting the corresponding property ([Window.viewportFit](Window.md#viewportfit) etc.) individually. Omitted arguments are left unchanged.

If you want the legacy (Kirikiri 2 / Kirikiri Z) behavior where the game stays at its original size in the top-left even when the window is enlarged,
specify `setViewport("none", 1.0, 0, 0)`
(see [Window.viewportFit](Window.md#viewportfit) for details).

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.viewportFit](Window.md#viewportfit) / [Window.viewportZoom](Window.md#viewportzoom) / [Window.viewportAlignX](Window.md#viewportalignx) / [Window.viewportAlignY](Window.md#viewportaligny) / [Window.viewportOffsetX](Window.md#viewportoffsetx) / [Window.viewportOffsetY](Window.md#viewportoffsety) / [Window.setViewportWallpaper](Window.md#setviewportwallpaper)

---

### setViewportWallpaper

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `image` | `&nbsp;` | Wallpaper image. If you pass a storage name (string), a [Bitmap](Bitmap.md) is created and loaded internally. You can also pass a [Layer](Layer.md) or [Bitmap](Bitmap.md) object directly; in that case a reference to the object is kept and the image is fetched at drawing time. |
| `fit` | `"cover"` | Fit mode of the wallpaper, as a string. The default is `"cover"`. The allowed values are the same as fit of [Window.setViewport](Window.md#setviewport). |
| `alignX` | `0.5` | Horizontal alignment of the wallpaper, as a real number. 0 = left / 0.5 = center / 1 = right. The default is 0.5. |
| `alignY` | `0.5` | Vertical alignment of the wallpaper, as a real number. 0 = top / 0.5 = center / 1 = bottom. The default is 0.5. |

**Description**

Sets the wallpaper image for viewport margins

Sets a wallpaper image that fills the margins created by the viewport (outside the inner game screen). It is drawn as a background before the game is drawn.

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.clearViewportWallpaper](Window.md#clearviewportwallpaper) / [Window.viewportBgColor](Window.md#viewportbgcolor) / [Window.setViewport](Window.md#setviewport)

---

### clearViewportWallpaper

Method

**Description**

Removes the wallpaper image for viewport margins

Removes the wallpaper set with [Window.setViewportWallpaper](Window.md#setviewportwallpaper). From then on, the margins are filled only with the background color in [Window.viewportBgColor](Window.md#viewportbgcolor).

Available in both the native Windows (WINVER) build and the SDL3 / generic builds (WINVER support since 2026-08-17).

**See also:** [Window.setViewportWallpaper](Window.md#setviewportwallpaper) / [Window.viewportBgColor](Window.md#viewportbgcolor)

---

### postInputEvent

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `eventname` | `&nbsp;` | Event name. Specify one of the following strings.<br>- "**onKeyDown**" generates the [Window.onKeyDown](Window.md#onkeydown) event.<br>- "**onKeyPress**" generates the [Window.onKeyPress](Window.md#onkeypress) event.<br>- "**onKeyUp**" generates the [Window.onKeyUp](Window.md#onkeyup) event. onKeyDown and onKeyUp come in pairs, so if you generate onKeyDown, it is recommended that you also generate the corresponding onKeyUp. |
| `params` | `null` | Dictionary containing the event parameters.<br>- For "onKeyDown" and "onKeyUp" events, put the virtual key code in "key" and the shift state in "shift". If "shift" is omitted, it is treated as 0.<br>- For the "onKeyPress" event, put the character in "key". |

**Description**

Generates an input event

Generates an input event. The current version can generate three key input events.

This method generates the event as an asynchronous event. That is, it returns without waiting for the corresponding event handler to finish. The event handler is actually called once control returns to Kirikiri.

Like ordinary input events, the generated input event also fires as the corresponding event of the Layer class, in addition to the Window class.

postInputEvent('onKeyDown', %[key: VK_UP, shift: ssShift]);

postInputEvent('onKeyUp',   %[key: VK_UP, shift: ssShift]);

// Press the left cursor key

---

### hideMouseCursor

Method

**Description**

Temporarily hides the mouse cursor

Temporarily hides the mouse cursor. As soon as the mouse moves even slightly,
the cursor is shown again.

This method has the same effect as setting [Window.mouseCursorState](Window.md#mousecursorstate) to `**mcsTempHidden**`.

---

### registerMessageReceiver

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` | Whether to register or unregister.<br>**wrmRegister** registers; **wrmUnregister**<br>unregisters.<br>The constants starting with wrm are defined in tp_stub.h. |
| `func` | `&nbsp;` | Message receiver function.<br>The function must have the form bool __stdcall func(void *userdata, tTVPWindowMessage *Message),<br>and its function pointer must be cast to an integer when passed to this method.<br>The tTVPWindowMessage structure is defined in tp_stub.h.<br>If this function returns true, the engine ignores that window message. |
| `userdata` | `&nbsp;` | Data pointer passed to the userdata argument of the receiver function given in func.<br>The pointer must be cast to an integer when passed to this method.<br>This argument is ignored unless mode is wrmRegister. |

**Description**

Registers / unregisters a message receiver function

This method is intended to be used from plugins written in C++ or the like. It cannot be used properly from TJS2.

With this method you can register a message receiver function that traps messages passing through this window. Besides ordinary window messages,
the receiver function can also trap two important messages, TVP_WM_DETACH and TVP_WM_ATTACH,
which can be used, for example, to detach child windows when the window is rebuilt or destroyed.

A brief usage example is in src/plugins/win32/wmrdump in the Kirikiri source distribution package.

**See also:** [Window.HWND](Window.md#hwnd)

---

### postMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | Window message ID to send, as an integer. |
| `wparam` | `&nbsp;` | Value to pass as wParam, as an integer. |
| `lparam` | `&nbsp;` | Value to pass as lParam, as an integer. |

**Description**

Posts a window message

Asynchronously posts the given window message to this window's native message queue.
Mainly used by C++ plugins as an entry point for sending notifications to the window.

**See also:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### getTouchPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Index in the touch coordinate array. |

**Description**

Gets touch coordinates

Gets the coordinate information at the given index of the current touch coordinate array.

The number of points can be obtained with the [Window.touchPointCount](Window.md#touchpointcount) property.

The coordinate information is returned as a dictionary containing the following elements.

`**startX**     : `x coordinate of the start position of this touch (client coordinates)

`**startY**   : `y coordinate of the start position of this touch (client coordinates)

`**x**    : `x coordinate of the current position of this touch (client coordinates)

`**y**    : `y coordinate of the current position of this touch (client coordinates)

`**ID**    : `ID identifying this touch

**See also:** [Window.touchPointCount](Window.md#touchpointcount)

---

### getMouseVelocity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Receives the mouse movement speed along the X axis. |
| `y` | `&nbsp;` | Receives the mouse movement speed along the Y axis. |
| `speed` | `&nbsp;` | Receives the mouse movement speed. |

**Return value**

Whether the value was obtained successfully

**Description**

Gets the mouse movement speed (1.1.0 and later)

Gets the current mouse movement speed in pixels/sec.

Measurement starts the moment the mouse enters the window.

You can reset the measurement with [Window.resetMouseVelocity](Window.md#resetmousevelocity) so that it is measured from any point in time you choose.

**See also:** [Window.getTouchVelocity](Window.md#gettouchvelocity) / [Window.resetMouseVelocity](Window.md#resetmousevelocity)

---

### getTouchVelocity

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Touch ID. |
| `x` | `&nbsp;` | Receives the movement speed along the X axis. |
| `y` | `&nbsp;` | Receives the movement speed along the Y axis. |
| `speed` | `&nbsp;` | Receives the movement speed. |

**Return value**

Whether the value was obtained successfully

**Description**

Gets the touch movement speed (1.1.0 and later)

Gets the current touch movement speed in pixels/sec.

It is measured from when the touch goes down until it is released.

For multi-touch support, speed is measured per ID.

Note that the measured speed information is discarded once the [Window.onTouchUp](Window.md#ontouchup) event method call finishes.

**See also:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### resetMouseVelocity

Method

**Description**

Resets mouse movement speed measurement (1.1.0 and later)

Resets the measurement of mouse movement speed.

Resetting lets you start measuring speed from any point in time.

**See also:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### beginMove

Method

**Description**

Starts dragging the window (deprecated)

Starts a move operation from the current mouse position, equivalent to dragging the window's title bar.
A compatibility method for builds with `USE_OBSOLETE_FUNCTIONS` enabled.

---

### requestUpdate

Method

**Description**

Requests a drawing update

Requests a redraw of the window (an `Update` on the next frame).
It does not draw immediately; the update is applied together at the next update timing.

**See also:** [Window.update](Window.md#update)

---

### setLayerPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | X coordinate |
| `top` | `&nbsp;` | Y coordinate |

**Description**

Sets the primary layer position (deprecated)

Sets the position (top-left) of the primary layer within the window's client area.
A compatibility method for builds with `USE_OBSOLETE_FUNCTIONS` enabled.

---

### maximize

Method

**Description**

Maximizes

Maximizes the window.
It does not go through [Window.onMaximizeQuery](Window.md#onmaximizequery)
(maximizing from the program is treated as intentional).

**See also:** [Window.showRestore](Window.md#showrestore) / [Window.maximized](Window.md#maximized)

---

### minimize

Method

**Description**

Minimizes

Minimizes (iconifies) the window.

**See also:** [Window.showRestore](Window.md#showrestore) / [Window.minimized](Window.md#minimized)

---

### showRestore

Method

**Description**

Restores the original size

Restores a maximized / minimized window to its original position and size.

**See also:** [Window.maximize](Window.md#maximize) / [Window.minimize](Window.md#minimize)

---

### getNormalRect

Method

**Return value**

A rectangle dictionary, or void if it cannot be obtained.

**Description**

Gets the normal rectangle

Returns the outer rectangle of the window (screen coordinates) when it is not maximized / minimized,
as a dictionary `%[ x, y, w, h ]`. Even while maximized you can get the "position and size when restored",
so it is useful for restoring on the next launch.

**See also:** [Window.getWindowRect](Window.md#getwindowrect)

---

### getWindowRect

Method

**Return value**

A rectangle dictionary.

**Description**

Gets the window rectangle

Returns the outer rectangle of the window, including the frame and title bar, as `%[ x, y, w, h ]` in screen coordinates.

**See also:** [Window.getClientRect](Window.md#getclientrect) / [Window.getNormalRect](Window.md#getnormalrect)

---

### getClientRect

Method

**Return value**

A rectangle dictionary.

**Description**

Gets the client rectangle

Returns the rectangle of the drawing area (client area) as `%[ x, y, w, h ]` in screen coordinates.

**See also:** [Window.setClientRect](Window.md#setclientrect) / [Window.getWindowRect](Window.md#getwindowrect)

---

### setCursorPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate in drawing area coordinates, in pixels. |
| `y` | `&nbsp;` | y coordinate in drawing area coordinates, in pixels. |

**Description**

Sets the mouse cursor position (drawing area coordinates)

Sets the mouse cursor position in **drawing area coordinates** (pixel coordinates with the top-left of the drawing area as the origin).

It has the same name as [Layer.setCursorPos](Layer.md#setcursorpos), but **the coordinate system differs**.
If you have values in layer coordinates, use that one instead. This one is for when you want to pass
values in drawing area coordinates as they are.

The typical case is `cx` / `cy` of [Window.onTouchScaling](Window.md#ontouchscaling) and
[Window.onTouchRotate](Window.md#ontouchrotate). Unlike mouse events, these arrive without being converted
to layer coordinates; converting them would require the destination rectangle, which scripts cannot obtain.
With this method you can pass them as they are.

Works in both the native Windows (WINVER) build and the SDL3 / generic builds.

**See also:** [Window.getCursorPos](Window.md#getcursorpos) / [Layer.setCursorPos](Layer.md#setcursorpos)

---

### getCursorPos

Method

**Description**

Gets the mouse cursor position (drawing area coordinates)

Returns the current mouse cursor position as a dictionary `%[ x, y ]`, in the same **drawing area coordinates**
as [Window.setCursorPos](Window.md#setcursorpos).

To read it in layer coordinates, use [Layer.cursorX](Layer.md#cursorx) /
[Layer.cursorY](Layer.md#cursory).

**See also:** [Window.setCursorPos](Window.md#setcursorpos) / [Layer.cursorX](Layer.md#cursorx)

---

### setClientRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | A dictionary `%[ x, y, w, h ]`. |

**Return value**

True if it could be set.

**Description**

Sets the client rectangle

Moves and resizes the window so that the client area becomes the given rectangle in screen coordinates.
Elements not in the dictionary keep their current values (`%[ w:320 ]` changes only the width).

**See also:** [Window.getClientRect](Window.md#getclientrect)

---

### registerExEvent

Method

**Description**

Enables extended events

Once called, the following events related to window frame operations start firing.
They do not fire until it is called.

| Event | Fires when | SDL3-based builds |
|---|---|---|
| [onMove](Window.md#onmove) | Moved | ○ |
| [onMoving](Window.md#onmoving) | Moving | × |
| [onResizing](Window.md#onresizing) | Resizing | × |
| [onMoveSizeBegin](Window.md#onmovesizebegin) / [onMoveSizeEnd](Window.md#onmovesizeend) | Frame drag starts / ends | × |
| [onMinimize](Window.md#onminimize) / [onMaximize](Window.md#onmaximize) | Minimized / maximized | ○ |
| [onMaximizeQuery](Window.md#onmaximizequery) | About to maximize | × |
| [onDPIChanged](Window.md#ondpichanged) | DPI changed | ○ |
| [onDisplayChanged](Window.md#ondisplaychanged) | Display configuration changed | ○ |

The events marked × do not fire in SDL3-based builds, because SDL has no queries during dragging
and only reports the result.

---

### registerDeviceChange

Method

**Return value**

True if enabled.

**Description**

Enables device change notifications

Once called, [Window.onDeviceChanged](Window.md#ondevicechanged)
fires when input devices are plugged in or removed. The engine's own input (mouse / pad) follows changes by itself,
so use this when a plugin or the like enumerates devices on its own.

---

### onMouseEnter

Event

**Description**

The mouse has entered

Fired when the mouse enters the client area of the window.

**See also:** [Window.onMouseLeave](Window.md#onmouseleave)

---

### onMouseLeave

Event

**Description**

The mouse has left

Fired when the mouse leaves the client area of the window.

**See also:** [Window.onMouseEnter](Window.md#onmouseenter)

---

### onClick

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position where the window was clicked. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position where the window was clicked. |

**Description**

The window has been clicked

Fired when the window is clicked.

**See also:** [Window.onMouseDown](Window.md#onmousedown) / [Window.onDoubleClick](Window.md#ondoubleclick)

---

### onDoubleClick

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position where the window was double-clicked. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position where the window was double-clicked. |

**Description**

The window has been double-clicked

Fired when the window is double-clicked.

**See also:** [Window.onClick](Window.md#onclick)

---

### onMouseDown

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position where the mouse button was pressed. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position where the mouse button was pressed. |
| `button` | `&nbsp;` | The mouse button that was pressed. One of the following values.<br>`**mbLeft**    : `Left mouse button pressed<br>`**mbMiddle**  : `Middle mouse button pressed<br>`**mbRight**   : `Right mouse button pressed<br>`**mbX1**      : `First side button pressed<br>`**mbX2**      : `Second side button pressed |
| `shift` | `&nbsp;` | State of the shift-type keys held down when the mouse button was pressed.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down |

**Description**

A mouse button has been pressed

Fired when a mouse button is pressed.

**See also:** [Window.onClick](Window.md#onclick)

---

### onMouseUp

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position where the mouse button was released. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position where the mouse button was released. |
| `button` | `&nbsp;` | The mouse button that was released. One of the following values.<br>`**mbLeft**    : `Left mouse button released<br>`**mbMiddle**  : `Middle mouse button released<br>`**mbRight**   : `Right mouse button released<br>`**mbX1**      : `First side button released<br>`**mbX2**      : `Second side button released |
| `shift` | `&nbsp;` | State of the shift-type keys held down when the mouse button was released.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down |

**Description**

A mouse button has been released

Fired when a mouse button is released.

---

### onMouseMove

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position the mouse moved to. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position the mouse moved to. |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down while the mouse was moving.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down<br>`**ssLeft**    : `Left mouse button was held down<br>`**ssMiddle**  : `Middle mouse button was held down<br>`**ssRight**   : `Right mouse button was held down |

**Description**

The mouse has moved

Fired when the mouse moves.

---

### onMouseWheel

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down while the mouse was moving.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down<br>`**ssLeft**    : `Left mouse button was held down<br>`**ssMiddle**  : `Middle mouse button was held down<br>`**ssRight**   : `Right mouse button was held down |
| `delta` | `&nbsp;` | Wheel rotation angle. Positive when rotated upward (away from the user),<br>negative when rotated downward (toward the user). The minimum step is usually 120. |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the position where the wheel was rotated. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the position where the wheel was rotated. |

**Description**

The mouse wheel has been rotated

Fired when the mouse wheel is rotated.

---

### onTouchDown

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the touched position. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the touched position. |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `id` | `&nbsp;` | Touch ID.<br>During multi-touch, each point gets a unique value, which identifies the point. |

**Description**

The screen has been touched

Fired when the touch panel is touched.

---

### onTouchUp

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the released position. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the released position. |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `id` | `&nbsp;` | Touch ID.<br>During multi-touch, each point gets a unique value, which identifies the point. |

**Description**

A finger has been lifted from the screen

Fired when a finger is lifted from the touch panel.

---

### onTouchMove

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate (in client coordinates) of the touch position. |
| `y` | `&nbsp;` | y coordinate (in client coordinates) of the touch position. |
| `cx` | `&nbsp;` | Horizontal contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `cy` | `&nbsp;` | Vertical contact size of the finger, in pixels.<br>Always 1 if the device does not support it. |
| `id` | `&nbsp;` | Touch ID.<br>During multi-touch, each point gets a unique value, which identifies the point. |

**Description**

A finger has moved

Fired when a finger touching the touch panel moves.

---

### onTouchScaling

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `startdistance` | `&nbsp;` | Distance in pixels when the multi-touch began. |
| `currentdistance` | `&nbsp;` | Distance between touches in pixels when the event occurred. |
| `cx` | `&nbsp;` | x coordinate of the center. It is passed in **drawing area coordinates** (pixel coordinates with the top-left of the drawing area as the origin)<br>(it can be passed to [Window.setCursorPos](#setcursorpos) as is). If you need layer coordinates, use [Layer.onTouchScaling](Layer.md#ontouchscaling). |
| `cy` | `&nbsp;` | y coordinate of the center. Same coordinate system as cx. |
| `flag` | `&nbsp;` | Multi-touch state flag.<br>`**0x01**     : `Set on the first event after the multi-touch began. |

**Description**

A zoom gesture has been made

Fired when a multi-touch zoom gesture is made on the touch panel.

---

### onTouchRotate

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `startangle` | `&nbsp;` | Angle in radians when the multi-touch began. |
| `currentangle` | `&nbsp;` | Angle of the touch in radians when the event occurred. |
| `distance` | `&nbsp;` | Distance between touches in pixels when the event occurred. |
| `cx` | `&nbsp;` | x coordinate of the center. It is passed in **drawing area coordinates** (pixel coordinates with the top-left of the drawing area as the origin)<br>(it can be passed to [Window.setCursorPos](#setcursorpos) as is). If you need layer coordinates, use [Layer.onTouchRotate](Layer.md#ontouchrotate). |
| `cy` | `&nbsp;` | y coordinate of the center. Same coordinate system as cx. |
| `flag` | `&nbsp;` | Multi-touch state flag.<br>`**0x01**     : `Set on the first event after the multi-touch began. |

**Description**

A rotate gesture has been made

Fired when a multi-touch rotate gesture is made on the touch panel.

---

### onMultiTouch

Event

**Description**

The multi-touch state has changed

Fired when multi-touch begins, moves, or ends.

Coordinates can be obtained with the [Window.touchPointCount](Window.md#touchpointcount) property and the [Window.getTouchPoint](Window.md#gettouchpoint) method.

**See also:** [Window.getTouchPoint](Window.md#gettouchpoint) / [Window.touchPointCount](Window.md#touchpointcount)

---

### onKeyDown

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | **Virtual key code** of the pressed key. |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down when the key was pressed.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down<br>`**ssLeft**    : `Left mouse button was held down<br>`**ssMiddle**  : `Middle mouse button was held down<br>`**ssRight**   : `Right mouse button was held down<br>In addition, if the key has been held long enough for key repeat to occur,<br>the following value is also included.<br>`**ssRepeat**  : `Key repeat occurred |

**Description**

A key has been pressed

Fired when a key is pressed.

---

### onKeyUp

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | **Virtual key code** of the released key. |
| `shift` | `&nbsp;` | State of the shift-type keys and mouse buttons held down when the key was released.<br>A bitwise OR of the following values.<br>`**ssAlt**     : `ALT key was held down<br>`**ssShift**   : `SHIFT key was held down<br>`**ssCtrl**    : `CTRL key was held down<br>`**ssLeft**    : `Left mouse button was held down<br>`**ssMiddle**  : `Middle mouse button was held down<br>`**ssRight**   : `Right mouse button was held down |

**Description**

A key has been released

Fired when a key is released.

---

### onKeyPress

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | The entered character. |

**Description**

A character has been entered

Fired when a character is entered. Unlike [Window.onKeyDown](Window.md#onkeydown), which deals with
virtual key codes, this event deals with the characters themselves. If the pressed key has nothing to do with
characters (function keys, etc.), this event does not fire.

When pressed together with the Ctrl key, control codes such as the following are sent.

`0x00 : `Ctrl+@

`0x01 : `Ctrl+A

`0x02 : `Ctrl+B

`0x03 : `Ctrl+C

`0x04 : `Ctrl+D

`0x05 : `Ctrl+E

`0x06 : `Ctrl+F

`0x07 : `Ctrl+G

`0x08 : `Ctrl+H

`0x09 : `Ctrl+I

`0x0A : `Ctrl+J

`0x0B : `Ctrl+K

`0x0C : `Ctrl+L

`0x0D : `Ctrl+M

`0x0E : `Ctrl+N

`0x0F : `Ctrl+O

`0x10 : `Ctrl+P

`0x11 : `Ctrl+Q

`0x12 : `Ctrl+R

`0x13 : `Ctrl+S

`0x14 : `Ctrl+T

`0x15 : `Ctrl+U

`0x16 : `Ctrl+V

`0x17 : `Ctrl+W

`0x18 : `Ctrl+X

`0x19 : `Ctrl+Y

`0x1A : `Ctrl+Z

`0x1B : `Ctrl+[

`0x1C : `Ctrl+\

`0x1D : `Ctrl+]

`0x1E : `Ctrl+^

`0x1F : `Ctrl+_

---

### onTextInput

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | The entered string. |

**Description**

Text input event

An event that delivers committed input strings. A string committed in the IME
arrives all at once in a single event, and characters outside the BMP (emoji, etc.) also arrive in a single event
without being split into surrogate pairs.

The traditional [onKeyPress](#onkeypress) is delivered per UTF-16 code unit,
so **use this event when implementing input fields that need whole characters**. Control characters
(BS / Enter / Tab / Esc, etc.) are not delivered to this event
(handle them in [onKeyDown](#onkeydown) / onKeyPress).

While a text input field of an [ElementsDialog](ElementsDialog.md) has focus,
the dialog consumes the input, so this event does not fire.

**Platform differences**

SDL3 builds deliver the OS text input events as they are.
WINVER (native Windows) builds synthesize them from `WM_CHAR`,
so they fire alongside onKeyPress (with the same characters).

For compatibility, layers still receive
[Layer.onKeyPress](Layer.md#onkeypress) split into UTF-16 code units as before.

**See also:** [Window.onKeyPress](Window.md#onkeypress)

---

### onResize

Event

**Description**

The window size has changed

Fired when the window size changes.

Get the actual size from properties such as [Window.width](Window.md#width) and [Window.height](Window.md#height).

---

### onFileDrop

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `files` | `&nbsp;` | Array object containing the names of the dropped files. |

**Description**

Files have been dropped

Fired when files are dropped onto the window from Explorer or the like.

Even when a single file is dropped, an array object is passed as the argument (the first element
is that file).

---

### onCloseQuery

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `canclose` | `&nbsp;` | Whether the window can be closed. As the event handlers are called from subclass up to superclass,<br>the subclass's decision on whether the window can be closed is passed here. |

**Description**

Confirms closing the window

An event for confirming whether the window can be closed. If the window cannot be closed,
pass false as the argument to the same method of the superclass.

---

### onPopupHide

Event

**Description**

Closes a popup window

An event fired when a popup window should close. It fires when the [Window.stayOnTop](Window.md#stayontop) property is true and the [Window.focusable](Window.md#focusable) property is false, and either another window is clicked or another application becomes active.

Normally you close or hide the window here.

**See also:** [Window.focusable](Window.md#focusable) / [Window.stayOnTop](Window.md#stayontop)

---

### onActivate

Event

**Description**

When the window becomes active

The event function called when the window becomes active.

Note that this event may fire even when the window is already active (there is no guarantee that events strictly alternate onActivate → onDeactivate → onActivate → ...).

**See also:** [Window.onDeactivate](Window.md#ondeactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onDeactivate

Event

**Description**

When the window becomes inactive

The event function called when the window becomes inactive.

Note that this event may fire even when the window is already inactive (there is no guarantee that events strictly alternate onActivate → onDeactivate → onActivate → ...).

**See also:** [Window.onActivate](Window.md#onactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onHintChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to display in the hint. |
| `x` | `&nbsp;` | X coordinate at which to display the hint. |
| `y` | `&nbsp;` | Y coordinate at which to display the hint. |
| `isshow` | `&nbsp;` | Whether to show or hide the hint. |

**Description**

When the hint state changes

The event function called when the hint state changes.

Show or hide the hint accordingly.

If you display the hint with a layer, set that layer's [Layer.hitThreshold](Layer.md#hitthreshold) to 256 so that its mouse messages are ignored.

Also set [Layer.ignoreHintSensing](Layer.md#ignorehintsensing) to true.

**See also:** [Window.hintDelay](Window.md#hintdelay) / [Layer.ignoreHintSensing](Layer.md#ignorehintsensing) / [Layer.hitThreshold](Layer.md#hitthreshold)

---

### onDisplayRotate

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `orientation` | `&nbsp;` | Display orientation.<br>One of the following values.<br>oriUnknown (failed to get / unknown), oriPortrait (portrait), oriLandscape (landscape) |
| `angle` | `&nbsp;` | Angle.<br>The angle is one of 0, 90, 180, 270, or -1; it is -1 if it could not be obtained.<br>The angle is the rotation from the device's default orientation, so on a portrait device it is 0 in portrait.<br>On typical devices, 0 seems to be landscape in most cases.<br>Devices where portrait is 0 are those whose standard orientation is portrait, such as recent 8-inch tablets. |
| `bpp` | `&nbsp;` | Bits per pixel. |
| `width` | `&nbsp;` | Display width. |
| `height` | `&nbsp;` | Display height. |

**Description**

When the display is rotated (1.1.0 and later)

The event function called when the display is rotated.

**See also:** [Window.displayOrientation](Window.md#displayorientation) / [Window.displayRotate](Window.md#displayrotate)

---

### onPointerDown

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Type of touch or mouse button |
| `x` | `&nbsp;` | X position |
| `y` | `&nbsp;` | Y position |
| `cx` | `&nbsp;` | Contact width (pixels); 1 for the mouse |
| `cy` | `&nbsp;` | Contact height (pixels); 1 for the mouse |
| `shift` | `&nbsp;` | Modifier key state; 0 for touch |
| `id` | `&nbsp;` | Touch ID; always 0 for the mouse |

**Description**

Pressed with some pointing device

---

### onPointerMove

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Touch or mouse. Reported as the mouse, not as a mouse button type. |
| `x` | `&nbsp;` | X position |
| `y` | `&nbsp;` | Y position |
| `cx` | `&nbsp;` | Contact width (pixels); 1 for the mouse |
| `cy` | `&nbsp;` | Contact height (pixels); 1 for the mouse |
| `shift` | `&nbsp;` | Modifier key state (including mouse button state); 0 for touch |
| `id` | `&nbsp;` | Touch ID; always 0 for the mouse |

**Description**

Some pointing device has moved

---

### onPointerUp

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Type of touch or mouse button |
| `x` | `&nbsp;` | X position |
| `y` | `&nbsp;` | Y position |
| `cx` | `&nbsp;` | Contact width (pixels); 1 for the mouse |
| `cy` | `&nbsp;` | Contact height (pixels); 1 for the mouse |
| `shift` | `&nbsp;` | Modifier key state; 0 for touch |
| `id` | `&nbsp;` | Touch ID; always 0 for the mouse |

**Description**

Some pointing device has been released

---

### onMaximizeQuery

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `canmaximize` | `true` | Whether maximizing is allowed. |

**Description**

Confirms maximizing

Fired when the user tries to maximize the window
(after [Window.registerExEvent](Window.md#registerexevent); WINVER build only).
To stop maximizing, pass false to the same method of the superclass.
If you do not call it, the window is maximized as usual
(the same design as [Window.onCloseQuery](Window.md#onclosequery)).
```tjs
function onMaximizeQuery() {
goPseudoFullScreen();           // 最大化のかわりに別の処理
super.onMaximizeQuery(false);   // 最大化そのものは止める
}
```
This differs from the windowEx plugin's approach, where returning true from the handler stops it.

---

### onMove

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X coordinate of the new position |
| `y` | `&nbsp;` | Y coordinate of the new position |

**Description**

Moved

Fired when the window has moved (requires [Window.registerExEvent](Window.md#registerexevent)).

---

### onMoving

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | Destination rectangle `%[ x, y, w, h ]` |

**Description**

Moving

Fired while the user is moving the window
(requires [Window.registerExEvent](Window.md#registerexevent); WINVER build only).
Rewriting the given rectangle constrains the destination.

---

### onResizing

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | Rectangle after the change `%[ x, y, w, h ]` |
| `edge` | `&nbsp;` | Edge being dragged |

**Description**

Resizing

Fired while the user is resizing the window
(requires [Window.registerExEvent](Window.md#registerexevent); WINVER build only).
Rewriting the given rectangle constrains the size.

---

### onMoveSizeBegin

Event

**Description**

Frame drag started

(Requires [Window.registerExEvent](Window.md#registerexevent); WINVER build only)

**See also:** [Window.onMoveSizeEnd](Window.md#onmovesizeend)

---

### onMoveSizeEnd

Event

**Description**

Frame drag ended

(Requires [Window.registerExEvent](Window.md#registerexevent); WINVER build only)

**See also:** [Window.onMoveSizeBegin](Window.md#onmovesizebegin)

---

### onMinimize

Event

**Description**

Minimized

(Requires [Window.registerExEvent](Window.md#registerexevent))

**See also:** [Window.minimize](Window.md#minimize)

---

### onMaximize

Event

**Description**

Maximized

(Requires [Window.registerExEvent](Window.md#registerexevent))

**See also:** [Window.maximize](Window.md#maximize)

---

### onDPIChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dpiX` | `&nbsp;` | Horizontal DPI |
| `dpiY` | `&nbsp;` | Vertical DPI |

**Description**

DPI changed

Fired when the window's DPI changes
(requires [Window.registerExEvent](Window.md#registerexevent)).
In SDL3-based builds, the display scale is converted to `96 × scale` and passed.

---

### onDisplayChanged

Event

**Description**

Display configuration changed

Fired when the screen resolution or monitor configuration changes
(requires [Window.registerExEvent](Window.md#registerexevent)).

---

### onDeviceChanged

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `arrival` | `&nbsp;` | True if connected, false if removed |

**Description**

An input device was plugged in or removed

(Requires [Window.registerDeviceChange](Window.md#registerdevicechange))

---

### onPaste

Event

**Description**

Paste requested

Fired when a paste is requested from outside (a launcher, etc.) ( `WM_PASTE` ).
WINVER build only.

---

## Plugin extension: layerExSave

Window extension

### Members

#### Methods

- [startSaveLayerImage](#startsavelayerimage)
- [cancelSaveLayerImage](#cancelsavelayerimage)
- [stopSaveLayerImage](#stopsavelayerimage)
- [onSaveLayerImageProgress](#onsavelayerimageprogress)
- [onSaveLayerImageDone](#onsavelayerimagedone)

---

### startSaveLayerImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer to save |
| `filename` | `&nbsp;` | File name (saved as PNG only when the extension is .png; otherwise TLG5) |
| `tags` | `&nbsp;` | Tag information |

**Return value**

Handler

**Description**

Starts saving an image in TLG5/PNG format

---

### cancelSaveLayerImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Handler |

**Description**

Cancels image saving

---

### stopSaveLayerImage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Handler |

**Description**

Aborts image saving (no completion event is sent when aborted)

---

### onSaveLayerImageProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Handler |
| `progress` | `&nbsp;` | Progress (in %) |
| `layer` | `&nbsp;` | Layer |
| `filename` | `&nbsp;` | File name |

**Description**

Saving in progress event

---

### onSaveLayerImageDone

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Handler |
| `canceled` | `&nbsp;` | 1 if canceled |
| `layer` | `&nbsp;` |  |
| `filename` | `&nbsp;` | File name |

**Description**

Saving completed event

---

## Plugin extension: menu

### Members

#### Properties

- [menu](#menu)

---

### menu

Property \ Access: `r`

**Description**

Root menu object

The root menu object (an object of the Menu class).
Menus registered as children of this root menu object appear in the menu bar.

---

## Plugin extension: messenger

Manual in pseudo-code

Provides mutual communication between Kirikiri instances running on the same machine and
communication from external applications.
Data is transferred using WM_COPYDATA.

### Members

#### Properties

- [messageEnable](#messageenable)
- [storeHWND](#storehwnd)

#### Methods

- [registerUserMessageReceiver](#registerusermessagereceiver)
- [sendUserMessage](#sendusermessage)
- [sendUserMessageDirect](#sendusermessagedirect)
- [postUserMessage](#postusermessage)
- [postUserMessageDirect](#postusermessagedirect)
- [sendMessage](#sendmessage)
- [sendMessageDirect](#sendmessagedirect)
- [onMessageReceived](#onmessagereceived)

---

### messageEnable

Property \ Access: `r/w`

**Description**

Specifies whether message receiving is enabled.

Set true to start receiving messages.
true if message receiving is enabled

---

### storeHWND

Property \ Access: `r/w`

**Description**

Specifies whether to save HWND information.

When this value is set, a file named "(executable name).(key value)" is created,
and the current HWND information is written to it.
If an external application wants to send messages, it can refer to the HWND recorded in this file.
The contents are updated automatically when the HWND changes, e.g. in full screen.
Therefore the external application must re-read the HWND value every time it sends.

---

### registerUserMessageReceiver

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` | wrmRegister=0: register, wrmUnRegister=1: unregister |
| `msg` | `&nbsp;` | Number: message number; string: value determined with RegisterWindowMessage |
| `proc` | `&nbsp;` | Function to call |
| `userdata` | `&nbsp;` | User data parameter |

**Return value**

Returns the registered message number

**Description**

Registers a user-defined message handler.

Note: When a function is registered from TJS2 (typeof proc == Object),
it is assumed to be a function of the form
function receiver(userdata, wparam, lparam).
userdata is passed as is,
and wparam, lparam are the original message data cast to integers.

Note: When a string is registered from TJS2 (typeof proc == String),
the function with that name on the object is called with the arguments function name(userdata, wparam, lparam).

Note: When a function is registered from a plugin (typeof proc == Integer),
it is assumed to be static bool __stdcall receiver(iTJSDispatch2 *winobj, void *userdata, tTVPWindowMessage *Message).
Cast it to an integer when setting.
winobj is the corresponding window object.
userdata is passed as a value cast to an integer.

---

### sendUserMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | Message number |
| `wparam` | `&nbsp;` | WPARAM (treated as an integer) |
| `lparam` | `&nbsp;` | LPARAM (treated as an integer) |

**Description**

Sends a low-level message.

The message is sent to all Kirikiri instances.

---

### sendUserMessageDirect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND value |
| `msg` | `&nbsp;` | Message number |
| `wparam` | `&nbsp;` | WPARAM (treated as an integer) |
| `lparam` | `&nbsp;` | LPARAM (treated as an integer) |

**Description**

Sends a low-level message to the given HWND.

The message is sent to the specific window.

---

### postUserMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` | Message number |
| `wparam` | `&nbsp;` | WPARAM (treated as an integer) |
| `lparam` | `&nbsp;` | LPARAM (treated as an integer) |

**Description**

Posts a low-level message.

The message is posted to all Kirikiri instances.

---

### postUserMessageDirect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND value |
| `msg` | `&nbsp;` | Message number |
| `wparam` | `&nbsp;` | WPARAM (treated as an integer) |
| `lparam` | `&nbsp;` | LPARAM (treated as an integer) |

**Description**

Posts a low-level message to the given HWND.

The message is posted to the specific window.

---

### sendMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Identification key (string; note the 256-character limit) |
| `message` | `&nbsp;` | Message (string) |

**Description**

Sends a message.

Sends a WM_COPYDATA message to all running Kirikiri instances.
Define the meaning of the identification key and message as appropriate for each application.

---

### sendMessageDirect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND value |
| `key` | `&nbsp;` | Identification key (string; note the 256-character limit) |
| `message` | `&nbsp;` | Message (string) |

**Description**

Sends a message to the given HWND.

Sends a WM_COPYDATA message to the given window.
The receiver uses the same processing as for sendMessage, so always specify the identification key.

---

### onMessageReceived

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Identification key (string; note the 256-character limit) |
| `message` | `&nbsp;` | Message (string) |

**Description**

Event: message received.

Called when a WM_COPYDATA message is received from another Kirikiri instance or an external application.
The caller is blocked until this call returns,
so finish processing promptly.

---

## Plugin extension: shellExecute

Manual in pseudo-code

Provides a mechanism for launching an external application and waiting for it to finish.
Uses WM_APP + 1 as the window message.

### Members

#### Methods

- [shellExecute](#shellexecute)
- [terminateProcess](#terminateprocess)
- [onShellExecuted](#onshellexecuted)
- [commandExecute](#commandexecute)
- [commandSendSignal](#commandsendsignal)
- [onCommandLineOutput](#oncommandlineoutput)

---

### shellExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program |
| `param` | `&nbsp;` | Arguments |

**Return value**

Process handle (-1 on failure). Can be passed to terminateProcess.

**Description**

Runs an external program in the background

The onShellExecuted event fires when it finishes.

---

### terminateProcess

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `process` | `&nbsp;` | Process handle |
| `endCode` | `&nbsp;` | Exit code |

**Description**

Forcibly terminates a running external program

---

### onShellExecuted

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `process` | `&nbsp;` | Process handle |
| `endCode` | `&nbsp;` | Exit code |

**Description**

Event: shell execution finished

---

### commandExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program |
| `param` | `&nbsp;` | Arguments |

**Return value**

Process handle (-1 on failure). Can be passed to terminateProcess.

**Description**

Runs a command-line program and captures its console output

The onCommandLineOutput event fires for each line of console output.
The onShellExecuted event fires when it finishes.

---

### commandSendSignal

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `process` | `&nbsp;` | Process handle (only processes started with commandExecute) |
| `isBreak` | `&nbsp;` | Send Ctrl+Break instead of Ctrl+C |

**Return value**

true on success

**Description**

Sends a Ctrl+C event (experimental: may not work in all environments)

---

### onCommandLineOutput

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `process` | `&nbsp;` | Process handle |
| `text` | `&nbsp;` | Output text (one line at a time) |

**Description**

Event: console output

---

## Plugin extension: sigcheck

Manual in pseudo-code

Performs signature checks in the background.
Uses WM_APP + 2 and WM_APP + 3 as window messages.

### Members

#### Methods

- [checkSignature](#checksignature)
- [cancelCheckSignature](#cancelchecksignature)
- [stopCheckSignature](#stopchecksignature)
- [onCheckSignatureProgress](#onchecksignatureprogress)
- [onCheckSignatureDone](#onchecksignaturedone)

---

### checkSignature

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File to check |
| `publickey` | `&nbsp;` | Public key |
| `info` | `&nbsp;` | User information |

**Return value**

handler: identification handler

**Description**

Starts a signature check

onCheckSignatureProgress fires during processing,
and onCheckSignatureDone fires when it finishes.
For exe and dll files, the signature is embedded in the file. For xp3 and the like,
an external file named after the original file with .sig appended is treated as the signature.

---

### cancelCheckSignature

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Identification handler |

**Description**

Cancels a signature check

Promptly stops a running signature check. It ends as canceled.

---

### stopCheckSignature

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Identification handler |

**Description**

Aborts a signature check

Promptly stops a running signature check. No completion event is sent.

---

### onCheckSignatureProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Identification handler |
| `info` | `&nbsp;` | User information |
| `percent` | `&nbsp;` | Progress, 0 to 100% |

**Description**

Event: signature check progress

---

### onCheckSignatureDone

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `handler` | `&nbsp;` | Identification handler |
| `info` | `&nbsp;` | User information |
| `result` | `&nbsp;` | Result -2: error, -1: canceled, 0: check failed, 1: check succeeded |
| `errormsg` | `&nbsp;` | Error message when the result is an error |

**Description**

Event: signature check finished

---

## Plugin extension: windowEx

Window extension

Note: The engine's own Window also includes maximize / minimize / restore (maximize / minimize / showRestore /
maximized / minimized), rectangles (getWindowRect / getClientRect / setClientRect /
getNormalRect), disableResize / disableMove, registerExEvent / registerDeviceChange
and the extended events (also available in SDL3-based builds).
Loading this plugin overrides them with the plugin versions.
New scripts should assume the engine versions.

### Members

#### Properties

- [maximized](#maximized)
- [minimized](#minimized)
- [disableResize](#disableresize)
- [exSystemMenu](#exsystemmenu)
- [enableNCMouseEvent](#enablencmouseevent)

#### Methods

- [maximize](#maximize)
- [minimize](#minimize)
- [showRestore](#showrestore)
- [resetWindowIcon](#resetwindowicon)
- [setWindowIcon](#setwindowicon)
- [setWindowCornerPreference](#setwindowcornerpreference)
- [getClientRect](#getclientrect)
- [getWindowRect](#getwindowrect)
- [getNormalRect](#getnormalrect)
- [setClientRect](#setclientrect)
- [bringTo](#bringto)
- [sendToBack](#sendtoback)
- [acquireImeControl](#acquireimecontrol)
- [resetImeContext](#resetimecontext)
- [registerExEvent](#registerexevent)
- [onMaximizeQuery](#onmaximizequery)
- [onMaximize](#onmaximize)
- [onMinimize](#onminimize)
- [onShow](#onshow)
- [onHide](#onhide)
- [onMoveSizeBegin](#onmovesizebegin)
- [onMoveSizeEnd](#onmovesizeend)
- [onMoving](#onmoving)
- [onMove](#onmove)
- [onResizing](#onresizing)
- [forceResizeRect](#forceresizerect)
- [onDisplayChanged](#ondisplaychanged)
- [onDPIChanged](#ondpichanged)
- [onEnterMenuLoop](#onentermenuloop)
- [onExitMenuLoop](#onexitmenuloop)
- [onScreenSave](#onscreensave)
- [onMonitorPower](#onmonitorpower)
- [onDeviceChanged](#ondevicechanged)
- [registerDeviceChange](#registerdevicechange)
- [onHotKeyPressed](#onhotkeypressed)
- [registerHotKey](#registerhotkey)
- [onActivateChanged](#onactivatechanged)
- [setOverlayBitmap](#setoverlaybitmap)
- [onNcMouseMove](#onncmousemove)
- [onNcMouseUp](#onncmouseup)
- [onNcMouseDown](#onncmousedown)
- [onNcMouseLeave](#onncmouseleave)
- [ncHitTest](#nchittest)
- [onNonCapMouseEvent](#onnoncapmouseevent)
- [focusMenuByKey](#focusmenubykey)
- [onStartKeyMenu](#onstartkeymenu)
- [onAccelKeyMenu](#onaccelkeymenu)
- [setMessageHook](#setmessagehook)
- [onWindowsMessageHook](#onwindowsmessagehook)
- [getNotificationNum](#getnotificationnum)
- [getNotificationName](#getnotificationname)

#### Constants

- [nchtError](#nchterror)
- [nchtTransparent](#nchttransparent)
- [nchtNoWhere](#nchtnowhere)
- [nchtClient](#nchtclient)
- [nchtCaption](#nchtcaption)
- [nchtSysMenu](#nchtsysmenu)
- [nchtSize](#nchtsize)
- [nchtGrowBox](#nchtgrowbox)
- [nchtMenu](#nchtmenu)
- [nchtHScroll](#nchthscroll)
- [nchtVScroll](#nchtvscroll)
- [nchtMinButton](#nchtminbutton)
- [nchtReduce](#nchtreduce)
- [nchtMaxButton](#nchtmaxbutton)
- [nchtZoom](#nchtzoom)
- [nchtLeft](#nchtleft)
- [nchtRight](#nchtright)
- [nchtTop](#nchttop)
- [nchtTopLeft](#nchttopleft)
- [nchtTopRight](#nchttopright)
- [nchtBottom](#nchtbottom)
- [nchtBottomLeft](#nchtbottomleft)
- [nchtBottomRight](#nchtbottomright)
- [nchtBorder](#nchtborder)

---

### maximized

Property \ Access: `r/w`

**Description**

Gets whether the window is maximized

A setter exists, but using it is not recommended.

---

### minimized

Property \ Access: `r/w`

**Description**

Gets whether the window is minimized

---

### disableResize

Property \ Access: `r/w`

**Description**

Suppresses resizing

The setter throws an exception unless extended events have been registered with registerExEvent().
When set to true, even if borderStyle == bsSizeable,
- the resize cursor no longer appears on the window border, and the size cannot be changed
- the Size item in the system menu (Alt+Space) is grayed out and cannot be selected
Resizing by other means, such as maximizing, still works (onResize is also fired).

---

### exSystemMenu

Property \ Access: `r/w`

**Description**

Adds items to the system menu

The setter throws an exception unless extended events have been registered with registerExEvent().
Specify an array of MenuItems or dictionaries.
When one of these menu items is selected, the onExSystemMenuSelected(selected object) callback fires.

---

### enableNCMouseEvent

Property \ Access: `r/w`

**Description**

Special purpose from here on: enables onNonCapMouseEvent, the WM_SETCURSOR callback (default: false)

---

### maximize

Method

**Description**

Maximizes the window

Equivalent to pressing the maximize button.
Does not work on fixed-size windows.

---

### minimize

Method

**Description**

Minimizes the window (mainWindow goes to the taskbar; other windows are minimized to the bottom-left of the screen)

Equivalent to pressing the minimize button.

---

### showRestore

Method

**Description**

Restores the window from maximized / minimized

---

### resetWindowIcon

Method

**Description**

Resets the window's title bar icon

Note: A workaround method for the problem where the icon disappears after returning from full screen on Vista (confirmed with Kirikiri v2.30).

---

### setWindowIcon

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | Icon file or void (void or "" resets to the initial state) |
| `withapp` | `&nbsp;` | Whether to also change the icon of the application window |

**Description**

Changes the window's title bar icon

Note: Files inside archives cannot be specified. If an exe or DLL is given, its first icon is used.

---

### setWindowCornerPreference

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `0` | A DWMWCP_* value (0=DEFAULT, 1=DONOTROUND, 2=ROUND, 3=ROUNDSMALL) |

**Return value**

true on success

**Description**

Changes the window corner shape

Note: Available on Windows 11 Build 22000 and later.

---

### getClientRect

Method

**Return value**

%[ x, y, w, h ] or void (on failure)

**Description**

Gets the client area, window area, and non-maximized normal area

Note: the innerSunken border is included in the client area.
Client area

---

### getWindowRect

Method

**Description**

Window area

---

### getNormalRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nofix` | `false` |  |

**Description**

Non-maximized normal display area (@param nofix true: do not apply work area correction)

---

### setClientRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x,y,w,h ] |

**Description**

Sets the client area

Values among x,y,w,h in rect that are void keep their current values.

---

### bringTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `win` | `"top"` | A Window object, a predefined string, or a number.<br>If a Window object, the window is placed behind that window.<br>If a string, one of "bottom" "notopmost" "top" "topmost" (equivalent to HWND_*); cf. SetWindowPos API.<br>If a number, it is treated as a window handle, or as a direct HWND_* macro value.<br>#define HWND_TOP        ((HWND)0)<br>#define HWND_BOTTOM     ((HWND)1)<br>#define HWND_TOPMOST    ((HWND)-1)<br>#define HWND_NOTOPMOST  ((HWND)-2) |
| `activate` | `false` | Flag indicating whether to activate the window.<br>Even if true, the application itself is not activated (no taskbar flashing, etc.). |

**Description**

Changes the window's Z order

---

### sendToBack

Method

**Description**

Alias for bringTo("bottom")

---

### acquireImeControl

Method

**Return value**

true on success

**Description**

Reconfigures the IME (Kirikiri Z only)

Posts TVP_WM_ACQUIREIMECONTROL when running on Kirikiri Z.

---

### resetImeContext

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `defval` | `true` | true: IACE_DEFAULT, false: NULL |

**Return value**

true on success

**Description**

Resets the IME context

May conflict with the engine-side settings (ImeControl.h) of Kirikiri Z if imDisable is reimplemented or if text input is used in multiple windows.

---

### registerExEvent

Method

**Description**

Enables extended events

For this window instance,
the callbacks whose description says "■ Extended event:" are enabled.

Note, however, that the following callbacks do not fire
if they do not exist on the instance at the time this function is called
(if they are missing, adding the functions to the instance later does not make them get called):
onMoving      moving
onMove        moved
onResizing    resizing
onNcMouseMove mouse movement in the non-client area

---

### onMaximizeQuery

Method

**Return value**

Return true to disallow maximizing

**Description**

■ Extended event: confirms whether to allow maximizing

Note: the engine version stops it differently. In the engine version, calling super.onMaximizeQuery(false) stops it,
and the return value is not examined (see [Window.onMaximizeQuery](Window.md#onmaximizequery)).

---

### onMaximize

Method

**Description**

■ Extended event: window maximized

When called, the window size has already been maximized.

---

### onMinimize

Method

**Description**

■ Extended event: window minimized

Called when another application is selected with Alt+Tab etc. during full screen, or when a window other than mainWindow is minimized.
Note that when the window goes to the taskbar, the onHide event is called instead.

---

### onShow

Method

**Description**

■ Extended event: window shown

Called, for example, when restored from the taskbar.

---

### onHide

Method

**Description**

■ Extended event: window hidden

Called, for example, when the window goes to the taskbar.

---

### onMoveSizeBegin

Method

**Description**

■ Extended event: resize / move start notification / end

Called when dragging of the frame or title bar starts, or when S or M is chosen from Alt+Space (start notification),
and when the move or resize ends (end notification).
If you want to refer to the original window position or size during onMoving or onResizing, save them here.
Whether it is a resize or a move cannot be determined, due to the nature of WM_ENTERSIZEMOVE/WM_EXITSIZEMOVE.

---

### onMoveSizeEnd

Method

**Description**

End notification

---

### onMoving

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h ] window coordinates |

**Description**

■ Extended event: window moving

Note: if Windows is set to show window contents while moving (no move outline), onMove is called immediately.

---

### onMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Screen X coordinate of the top-left of the client area<br>Note: the innerSunken border is included in the client area. |
| `y` | `&nbsp;` | Screen Y coordinate of the top-left of the client area |

**Description**

■ Extended event: window moved (completed)

---

### onResizing

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h, type ] size during the change (window coordinates) |

**Return value**

Return true to apply changes to rect (forcing the position and size).
In this case, note that unless you adjust the changes properly according to the grabbed position (rect.type),
the window may move during resizing (see forceResizeRect()).

**Description**

■ Extended event: resizing

Note: if Windows is set to show window contents while resizing (no size outline), onResize is called immediately.

---

### forceResizeRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rect` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### onDisplayChanged

Method

**Description**

■ Extended event: display configuration change notification

Called when the resolution, color depth, or multi-monitor configuration (including position changes) changes.

---

### onDPIChanged

Method

**Description**

■ Extended event: window DPI change notification

Notified when the DPI setting is changed or the window moves between monitors with different DPI values.

---

### onEnterMenuLoop

Method

**Description**

■ Extended event: menu processing start / end notification

Notification events for the start and end of the window's menu processing (clicking, pressing F10, etc.).
Callbacks for the WM_ENTERMENULOOP / WM_EXITMENULOOP notifications.

Note: this event does not fire for menus in full screen!

---

### onExitMenuLoop

Method

**Description**

Menu processing ended

---

### onScreenSave

Method

**Return value**

Return true to suppress the action

**Description**

■ Extended event: screen saver start notification, monitor power change notification

---

### onMonitorPower

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### onDeviceChanged

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `arrival` | `&nbsp;` | true if a device was added, false if removed.<br>Note: registerExEvent() must have been called, and registerDeviceChange() must also be called. |

**Description**

■ Extended event: device added / removed notification

---

### registerDeviceChange

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `guid` | `GUID_DEVINTERFACE_HID` | Octet value representing a GUID (HID device class if omitted).<br>Note: only one GUID can be registered per window. |

**Description**

Enables the onDeviceChanged extended event

---

### onHotKeyPressed

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID registered with registerHotKey |
| `mod` | `&nbsp;` | Modifier keys (a combination of ssShift, ssAlt, ssCtrl, etc.) |

**Description**

■ Extended event: hotkey input

---

### registerHotKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | ID to register (0x0000 to 0xBFFF only) |
| `key` | `&nbsp;` |  |
| `mod` | `&nbsp;` | Modifier keys (a combination of ssShift, ssAlt, ssCtrl, etc.) |

**Return value**

true if registered

**Description**

Registers a hotkey

---

### onActivateChanged

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `active` | `&nbsp;` | 0: deactivated, 1: activated other than by a mouse click, 2: activated by a mouse click |
| `minimize` | `&nbsp;` | 0: the window is not minimized; otherwise: minimized |

**Description**

■ Extended event: activation state change notification

Note: unlike Window.onActivate and Window.onDeactivate, the callback fires even when System.eventDisabled == true
(this applies to extended events in general).

For example, by setting System.eventDisabled=true in System.onDeactivate (which stops System.onActivate from
firing) and restoring it in this event notification, you may be able to add a feature like "stop while inactive"
(however, this only stops event delivery, so it is not very meaningful for applications using timers
that look at elapsed time).
Also, while System.eventDisabled=true, not even screen updates run, so if WM_PAINT occurs, e.g. because another window
is brought on top, the screen becomes corrupted (use the OverlayBitmap described below, etc.).

---

### setOverlayBitmap

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer to copy into the bitmap image (void or omitted removes the overlay) |

**Description**

Shows / removes an overlay bitmap

Covers the client area with a child window (a Windows one, not a Kirikiri one) showing the given image.
- Throws an exception unless extended events are enabled.
- While the overlay is shown, no mouse messages at all reach the Kirikiri layers.
- Effectively intended only for when System.eventDisabled=true.
- Removed automatically on TVP_WM_DETACH.

---

### onNcMouseMove

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Mouse X coordinate |
| `y` | `&nbsp;` | Mouse Y coordinate |
| `ht` | `&nbsp;` | Area type (NCHITTEST constant) |

**Description**

■ Extended event: non-client area mouse event

---

### onNcMouseUp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseDown

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseLeave

Method

---

### ncHitTest

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Screen X coordinate |
| `y` | `&nbsp;` | Screen Y coordinate |

**Return value**

Area type (NCHITTEST constant)

**Description**

Examines the non-client area

---

### onNonCapMouseEvent

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ht` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**Description**

WM_SETCURSOR callback: ht=LOWORD(LParam), ev=HIWORD(LParam)

---

### focusMenuByKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**Description**

Sends SC_KEYMENU

---

### onStartKeyMenu

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**Description**

SC_KEYMENU notification callback

---

### onAccelKeyMenu

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` |  |
| `st` | `&nbsp;` |  |

**Description**

WM_MENUCHAR notification callback

---

### setMessageHook

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `on` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**Description**

Sets a message hook (on: enable, ev: event number or event name string; all if omitted)

---

### onWindowsMessageHook

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wp` | `&nbsp;` |  |
| `lp` | `&nbsp;` |  |

**Description**

Callback for when an event specified with setMessageHook occurs

---

### getNotificationNum

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

Gets a WM_XXX event number (pass the name without WM_)

---

### getNotificationName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**Description**

Gets WM_XXX from an event number (returned without WM_)

---

### nchtError

Constant

**Description**

HTERROR

---

### nchtTransparent

Constant

**Description**

HTTRANSPARENT

---

### nchtNoWhere

Constant

**Description**

HTNOWHERE

---

### nchtClient

Constant

**Description**

HTCLIENT

---

### nchtCaption

Constant

**Description**

HTCAPTION

---

### nchtSysMenu

Constant

**Description**

HTSYSMENU

---

### nchtSize

Constant

**Description**

HTSIZE

---

### nchtGrowBox

Constant

**Description**

HTGROWBOX

---

### nchtMenu

Constant

**Description**

HTMENU

---

### nchtHScroll

Constant

**Description**

HTHSCROLL

---

### nchtVScroll

Constant

**Description**

HTVSCROLL

---

### nchtMinButton

Constant

**Description**

HTMINBUTTON

---

### nchtReduce

Constant

**Description**

HTREDUCE

---

### nchtMaxButton

Constant

**Description**

HTMAXBUTTON

---

### nchtZoom

Constant

**Description**

HTZOOM

---

### nchtLeft

Constant

**Description**

HTLEFT

---

### nchtRight

Constant

**Description**

HTRIGHT

---

### nchtTop

Constant

**Description**

HTTOP

---

### nchtTopLeft

Constant

**Description**

HTTOPLEFT

---

### nchtTopRight

Constant

**Description**

HTTOPRIGHT

---

### nchtBottom

Constant

**Description**

HTBOTTOM

---

### nchtBottomLeft

Constant

**Description**

HTBOTTOMLEFT

---

### nchtBottomRight

Constant

**Description**

HTBOTTOMRIGHT

---

### nchtBorder

Constant

**Description**

HTBORDER

---

## Plugin extension: windowExProgress

Window extension

### Members

#### Methods

- [startProgress](#startprogress)
- [doProgress](#doprogress)
- [setProgressMessage](#setprogressmessage)
- [endProgress](#endprogress)

#### Constants

- [PBS_SMOOTH](#pbs_smooth)
- [PBS_VERTICAL](#pbs_vertical)

---

### startProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `init` | `&nbsp;` | Initialization data (dictionary) |

**Description**

Starts progress processing.

The display continues correctly even while Kirikiri is blocked executing.
Progress bar initialization parameters
progressBarEnable: whether to show the progress bar (default: true)
progressBarStyle: progress bar style (default: none)
progressBarLeft: progress bar X position (default: centered automatically)
progressBarTop: progress bar Y position (default: centered automatically)
progressBarWidth: progress bar width (default: 1/3 of the window width)
progressBarHeight: progress bar height (default: 1/10 of the window height)
progressBarColor: progress bar color 0xRRGGBB (default: default color)
progressBarBackColor: progress bar background color 0xRRGGBB (default: default color)

Cancel button initialization parameters
cancelButtonEnable: whether to show the cancel button (default: true)
cancelButtonCaption: text shown on the cancel button (default: Cancel)
cancelButtonLeft: cancel button X position (default: centered automatically)
cancelButtonTop: cancel button Y position (default: three times height from the bottom)
cancelButtonWidth: cancel button width (default: number of text characters * 12 + 8)
cancelButtonHeight: cancel button height (default: 20)

Background image initialization parameters (not implemented)
backGround: background; layer: refers to the layer's image directly; number: fill with that color; default: none

Message initialization parameters (not implemented)
messages: message information or an array of it
left: display X coordinate
top: display Y coordinate
text: initial text
size: display size
color: display color
shadowColor: shadow color
shadowDistanceX: shadow offset
shadowDistanceY: shadow offset
font: font
fontStyle: font style

---

### doProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `percent` | `&nbsp;` | Progress, in percent |

**Return value**

true if cancellation has been requested

**Description**

Reports the progress of progress processing.

---

### setProgressMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Text ID (in registration order) |
| `text` | `&nbsp;` | Text to display |

**Description**

Replaces the text of progress processing

---

### endProgress

Method

**Description**

Ends progress processing.

---

### PBS_SMOOTH

Constant

Value: `1`

**Description**

Progress bar style: smooth progress bar

---

### PBS_VERTICAL

Constant

Value: `4`

**Description**

Progress bar vertical orientation

---
