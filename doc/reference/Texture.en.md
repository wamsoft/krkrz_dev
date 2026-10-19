# Texture

The texture class.
It corresponds closely to a texture on the hardware.

Invalidating the object releases the texture, so calling invalidate explicitly once it is no longer needed is recommended.

## Members

### Constructors

- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)

### Properties

- [width](#width)
- [height](#height)
- [memoryWidth](#memorywidth)
- [memoryHeight](#memoryheight)
- [isGray](#isgray)
- [isPowerOfTwo](#ispoweroftwo)
- [nativeHandle](#nativehandle)
- [stretchType](#stretchtype)
- [wrapModeHorizontal](#wrapmodehorizontal)
- [wrapModeVertical](#wrapmodevertical)
- [margin9Patch](#margin9patch)

### Methods

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [setDrawSize](#setdrawsize)

### Constants

- [stNearest](#stnearest)
- [stLinear](#stlinear)
- [wmRepeat](#wmrepeat)
- [wmClampToEdge](#wmclamptoedge)
- [wmMirror](#wmmirror)

---

### Texture

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `filename` | `string` | `&nbsp;` | Image file name. |
| `format` | `int` | `tcfRGBA` | Color format (tcfRGBA / tcfAlpha / tcfAlphaChannel).<br>With `**tcfAlpha**`, color information is converted to grayscale (the **luminance** becomes an 8-bit texture).<br>With `**tcfAlphaChannel**`, the alpha channel is used as-is for an 8-bit texture.<br>This suits clipping-mask images that only reference alpha; it needs 1/4 of the memory of RGBA,<br>and no upload PBO is allocated. Common mask assets that are "solid white in luminance with the data in alpha"<br>cannot be handled with tcfAlpha, so use this format for them. If you pass an image that is not 32bpp,<br>it falls back to the conventional grayscale handling. |
| `is9patch` | `bool` | `false` | Whether to read 9-patch information and use the texture for 9-patch drawing. |

**Description**

Constructor that loads from a file

---

### Texture

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `bitmap` | `Bitmap` | `&nbsp;` | The Bitmap instance to create the texture from. |
| `format` | `int` | `tcfRGBA` | Color format (tcfRGBA / tcfAlpha / tcfAlphaChannel).<br>The values mean the same as in the file-loading constructor.<br>`**tcfAlpha**` converts the luminance to grayscale; `**tcfAlphaChannel**` uses the alpha channel<br>as-is for an 8-bit texture. |
| `is9patch` | `bool` | `false` | Whether to read 9-patch information and use the texture for 9-patch drawing. |

**Description**

Constructor that copies from a Bitmap

---

### Texture

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | Texture width. |
| `height` | `int` | `&nbsp;` | Texture height. |
| `format` | `int` | `tcfRGBA` | Color format (tcfRGBA / tcfAlpha / tcfAlphaChannel).<br>Since this is an empty texture with uninitialized contents, `**tcfAlphaChannel**` is treated the same as `**tcfAlpha**`. |

**Description**

Constructor with a given size

The texture contents are uninitialized and contain garbage.

---

### Texture

Constructor

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `sizelist` | `Array` | `&nbsp;` | The sizes at which to generate mipmaps, as an array of width/height pairs. |
| `filename` | `string` | `&nbsp;` | Image file name. |
| `type` | `&nbsp;` | `stFastAreaAvg` | The reduction algorithm. Same as the type argument of ImageFunction.operateStretch or Layer.operateStretch. |
| `typeopt` | `real` | `-1.0` | Sharpness for bicubic interpolation. Currently has no meaning for other interpolation methods. |

**Description**

Constructor that generates mipmaps

---

### width

Property \ Access: `r/w`

**Description**

Width (valid area)

Same as memoryWidth unless pot was specified.

---

### height

Property \ Access: `r/w`

**Description**

Height (valid area)

Same as memoryHeight unless pot was specified.

---

### memoryWidth

Property \ Access: `r/w`

**Description**

Actual width (on the hardware)

---

### memoryHeight

Property \ Access: `r/w`

**Description**

Actual height (on the hardware)

---

### isGray

Property \ Access: `r/w`

**Description**

Whether the texture is 8-bit color (internally an alpha texture)

---

### isPowerOfTwo

Property \ Access: `r/w`

**Description**

Whether the texture size is a power of two

---

### nativeHandle

Property \ Access: `r/w`

**Description**

Native handle (platform-dependent)

Under OpenGL ES 2/3 this is the texture ID.

---

### stretchType

Property \ Access: `r/w`

**Description**

Interpolation method for scaling

---

### wrapModeHorizontal

Property \ Access: `r/w`

**Description**

Horizontal wrap mode

---

### wrapModeVertical

Property \ Access: `r/w`

**Description**

Vertical wrap mode

---

### margin9Patch

Property \ Access: `r/w`

**Description**

9-patch margins

If the texture was loaded with is9patch, a read-only Rect object is available.
If is9patch was not specified or the information could not be read, this is void.

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

Copies a rectangle (position and Rect)

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

Copies a rectangle (positions)

---

### copyRect

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `src` | `Bitmap` | `&nbsp;` | A Bitmap object. |

**Description**

Copies a rectangle (whole bitmap)

Copies the whole bitmap. Anything that does not fit is clipped.

---

### setDrawSize

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | Reference display width. |
| `height` | `int` | `&nbsp;` | Reference display height. |

**Description**

Sets the reference drawing size

When drawn at 1x with Canvas.drawTexture, a texture is normally drawn at its own size; if you set a width and height with this method, drawing with this texture instance uses the size you set.
Scaling is also based on this size.
Setting it when the size of the internal image data differs from the size you usually draw at lets you specify scale factors relative to the size you want to display.

---

### stNearest

Constant

**Description**

Nearest neighbor. Set in the stretchType property.

---

### stLinear

Constant

**Description**

Linear interpolation. Set in the stretchType property.

---

### wmRepeat

Constant

**Description**

Repeat. Set in the wrapModeHorizontal/wrapModeVertical properties.

---

### wmClampToEdge

Constant

**Description**

Clamp to edge (stretches the edge color). Set in the wrapModeHorizontal/wrapModeVertical properties. Required when the size is not a power of two (default).

---

### wmMirror

Constant

**Description**

Mirrored repeat. Set in the wrapModeHorizontal/wrapModeVertical properties.

---
