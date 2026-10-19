# Window.BasicDrawDevice

The Window.BasicDrawDevice class is a DrawDevice that provides standard drawing; register an instance in [Window.drawDevice](Window.md#drawdevice) to use it.

## Members

### Constructors

- [BasicDrawDevice](#basicdrawdevice)

### Properties

- [interface](#interface)
- [videoPresenterHost](#videopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)
- [d3d11Device](#d3d11device)

### Methods

- [recreate](#recreate)
- [captureWithOverlay](#capturewithoverlay)

---

### BasicDrawDevice

Constructor

**Description**

Constructs a BasicDrawDevice object

Constructs an object of the Window.BasicDrawDevice class.

Window.drawDevice holds an instance of this class from the start, so you do not need to register one yourself.

---

### interface

Property \ Access: `r`

**Description**

Gets the interface object

Provided so that plugins and the like can use the DrawDevice object.

---

### videoPresenterHost

Property \ Access: `r`

**Description**

Registration point for overlay movie presenters (pointer value)

Pointer value of the `iTVPVideoPresenterHost` that the overlay movie side (VideoOverlay) reads in order to
composite into this DrawDevice's D3D11 back buffer in pull mode.
If non-zero, the presenter registers itself and uses pull compositing; if 0 or undefined, it falls back to
presenting through a child window. Normally used by the engine internals or plugins.

---

### dialogRendererHost

Property \ Access: `r`

**Description**

Elements dialog renderer host (pointer value)

Pointer value of the `iTVPDialogRendererHost` used to obtain the Elements overlay drawing adapter.
Normally used by the engine internals or plugins.

---

### viewportBackgroundHost

Property \ Access: `r`

**Description**

Registration point for viewport margin fill (pointer value)

Pointer value of the `iTVPViewportBackgroundHost` that receives the margin settings used when the game screen does not cover the whole drawing area ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ). Window applies the margin settings only when this property is non-zero
(on draw devices without this property, margin fill has no effect and the device's default fill remains). Normally used by the engine internals or plugins.

---

### d3d11Device

Property \ Access: `r`

**Description**

ID3D11Device pointer (pointer value)

Pointer value of the `ID3D11Device` exposed so that hardware movie playback (IMFMediaEngine) can bind to the engine's D3D11 device for hardware decoding (VIDEO_SUPPORT, with multithread protection enabled).
WINVER (D3D11) build only. Normally used by the engine internals or plugins.

---

### recreate

Method

**Description**

Recreates the internal device

Recreates the internal device.

Normally you do not need to call this.

---

### captureWithOverlay

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bitmap` | `&nbsp;` | Destination [Bitmap](Bitmap.md) object. It is resized as needed. |

**Return value**

true on success

**Description**

Captures the screen including Elements screens

Draws the current screen, i.e. the layer compositing result with overlays such as [ElementsDialog](ElementsDialog.md) on top, reads it back,
and copies the game screen area into bitmap. The captured image has the size displayed in the window.

Methods that capture only layers (copying a Layer's image, or KAG's screen capture) do not include Elements screens,
so use this when you want Elements screens included, e.g. in save thumbnails.

---
