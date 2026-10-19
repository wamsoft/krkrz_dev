# GLCompositor

A class that performs offscreen compositing with OpenGL ES behind the scenes and writes the result back to a Layer,
even when OGLDrawDevice is not in use (when the screen's draw device is D3D11,
SDL_Renderer, or the like).

It provides the functionality of GLESAdaptor from the former krkrgles plugin, built into the engine and sharing
the existing GL drawing code of Canvas / Offscreen. It does not depend on the draw device: it obtains
a GL context from the window and makes it current itself (it does not present to the screen;
it only draws into an offscreen FBO). When the OGL draw device is running, it shares
that context.

The capture() callback runs "incontextof this compositor", so
this inside the callback is this GLCompositor. You can therefore use the full API of this.canvas
(the internal Canvas), such as drawTexture / beginEffect / endEffect / clipping, as well as
this.drawLayer / this.copyLayer, directly (compatible with GLESAdaptor).

In builds where Canvas runs on SDL_GPU (builds with [GPUDrawDevice](GPUDrawDevice.md)), it becomes a GPU version with the same
name and the same API. Drawing happens on the shared GPU device; since there is no GL context,
makeCurrent does nothing and GLGetProcAddress returns 0 (it cannot be used as a drawing target for GLES-based plugins).

## Members

### Constructors

- [GLCompositor](#glcompositor)

### Properties

- [canvas](#canvas)
- [blendMode](#blendmode)
- [unpremultiply](#unpremultiply)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [GLGetProcAddress](#glgetprocaddress)

### Methods

- [capture](#capture)
- [drawLayer](#drawlayer)
- [copyLayer](#copylayer)
- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)

---

### GLCompositor

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `window` | `Window` | `&nbsp;` | The target Window object. |

**Description**

Creates a GLCompositor.

Initializes it with the GL context of the specified window.

---

### canvas

Property \ Access: `r`

**Description**

The internal Canvas.

You can use the full Canvas API, such as drawTexture / beginEffect / endEffect /
clipping.

---

### blendMode

Property \ Access: `r/w`

**Description**

Blend mode for drawing.

Corresponds to the blendMode of the internal Canvas.

---

### unpremultiply

Property \ Access: `r/w`

**Description**

Whether capture un-premultiplies on readback (default false).

If true, capture() converts premultiplied alpha back to
straight alpha (RGB = RGB x 255 / A) on readback before writing to the Layer. This prevents white fringes
at the edges with normal alpha blending (ltAlpha) when the semi-transparent edges of MSAA-rendered
3D content (such as VRM character art) are read back still premultiplied. Equivalent to the former GLESAdaptor.unpremultiply.

---

### screenWidth

Property \ Access: `r/w`

**Description**

Default width for offscreen compositing.

---

### screenHeight

Property \ Access: `r/w`

**Description**

Default height for offscreen compositing.

---

### GLGetProcAddress

Property \ Access: `r`

**Description**

Pointer to the GL entry-point resolver function (integer).

Used as oglbase by GLES-based plugins (EffekseerDevice and so on).
Example: new EffekseerDevice(compositor).

---

### capture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | The Layer to write the drawing result back to. |
| `callback` | `&nbsp;` | `&nbsp;` | Drawing callback function(w:int, h:int, param) (this=GLCompositor). |
| `param` | `&nbsp;` | `&nbsp;` | An arbitrary value passed to callback. |
| `color` | `int` | `&nbsp;` | Clear color (ARGB). |

**Description**

Performs offscreen compositing and writes the result back to layer.

Clears an offscreen FBO the size of layer with color, then
calls callback(w, h, param) "incontextof this compositor" to let it draw, and
reads the result back into the main image of layer. Inside callback, this is
this GLCompositor, so you can draw with this.canvas (drawTexture / beginEffect /
clipping, and so on) and use this.drawLayer / this.copyLayer directly
(compatible with GLESAdaptor; the canvas is referenced as this.canvas, not passed as an argument).

---

### drawLayer

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | Source Layer. |
| `a` | `real` | `&nbsp;` | Transform matrix m11. |
| `b` | `real` | `&nbsp;` | Transform matrix m12. |
| `c` | `real` | `&nbsp;` | Transform matrix m21. |
| `d` | `real` | `&nbsp;` | Transform matrix m22. |
| `tx` | `real` | `&nbsp;` | Translation x. |
| `ty` | `real` | `&nbsp;` | Translation y. |
| `opacity` | `int` | `255` | = 255 Opacity (0 to 255). |

**Description**

Draws layer to the current target with an affine transform and opacity.

Call this from inside the capture() callback. The transform is
specified as a 2x2 part (a,b,c,d) plus a translation (tx,ty).

---

### copyLayer

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | Source Layer. |
| `left` | `int` | `&nbsp;` | Position x. |
| `top` | `int` | `&nbsp;` | Position y. |

**Description**

Draws layer as-is at (left, top).

A simple-translation version of drawLayer. Call this from inside the capture()
callback.

---

### setScreenSize

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | Width. |
| `height` | `int` | `&nbsp;` | Height. |

**Description**

Sets the default size for offscreen compositing.

---

### makeCurrent

Method

**Description**

Makes this GLCompositor's GL context current.

---
