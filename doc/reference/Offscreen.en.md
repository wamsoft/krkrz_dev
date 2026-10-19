# Offscreen

An offscreen surface.
This is what is usually called a render target. It can also be used as a texture.
Internally, an FBO, a renderbuffer, and a texture are created.
If you do not use it as a render target, there is no need to use this class.
The Texture class is more memory-efficient.

## Members

### Constructors

- [Offscreen](#offscreen)

### Properties

- [width](#width)
- [height](#height)
- [nativeHandle](#nativehandle)

### Methods

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [exchangeTexture](#exchangetexture)

---

### Offscreen

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | Offscreen width. |
| `height` | `int` | `&nbsp;` | Offscreen height. |

**Description**

Creates an offscreen surface.

Resources are released on invalidate, so explicitly invalidating the object once it is no longer needed is recommended.

---

### width

Property \ Access: `r/w`

**Description**

Width, as specified at creation [r]

---

### height

Property \ Access: `r/w`

**Description**

Height, as specified at creation [r]

---

### nativeHandle

Property \ Access: `r/w`

**Description**

Platform-dependent handle [r]

Under OpenGL ES this is the texture ID.

---

### copyRect

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | Left edge of the destination. |
| `dtop` | `int` | `&nbsp;` | Top edge of the destination. |
| `src` | `Bitmap` | `&nbsp;` | A Bitmap object. |
| `srcRect` | `Rect` | `&nbsp;` | Source rectangle in src. |

**Description**

Copies a rectangle

---

### copyRect

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | Left edge of the destination. |
| `dtop` | `int` | `&nbsp;` | Top edge of the destination. |
| `src` | `Bitmap` | `&nbsp;` | A Bitmap object. |
| `sleft` | `int` | `&nbsp;` | Left position of the source. |
| `stop` | `int` | `&nbsp;` | Top position of the source. |
| `swidth` | `int` | `&nbsp;` | Source width. |
| `sheight` | `int` | `&nbsp;` | Source height. |

**Description**

Copies a rectangle

---

### copyTo

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | Destination bitmap. |
| `dleft` | `int` | `&nbsp;` | Left edge of the destination. |
| `dtop` | `int` | `&nbsp;` | Top edge of the destination. |
| `sleft` | `int` | `&nbsp;` | Left edge of the source. |
| `stop` | `int` | `&nbsp;` | Top edge of the source. |
| `width` | `int` | `&nbsp;` | Width. |
| `height` | `int` | `&nbsp;` | Height. |

**Description**

Copies to a Bitmap

---

### copyTo

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | Destination bitmap. |

**Description**

Copies to a Bitmap

The Bitmap is resized to match the size of the Offscreen.

---

### copyTo

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | Destination bitmap. |
| `dleft` | `int` | `&nbsp;` | Left edge of the destination. |
| `dtop` | `int` | `&nbsp;` | Top edge of the destination. |
| `srcRect` | `Rect` | `&nbsp;` | Source rectangle. |

**Description**

Copies to a Bitmap

---

### exchangeTexture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | The Texture instance to swap with. |

**Description**

Swaps the texture attached to the framebuffer with the texture referenced by a Texture object.

The textures being swapped must have the same size, or an exception is thrown.
The color format must also be RGBA.
It may be best not to swap in the middle of rendering (to be confirmed).
When you do not need to draw to both, as in a crossfade, you can reduce overhead by taking out the previous image as a Texture and swapping in a new Texture.

---
