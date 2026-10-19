# Bitmap

The Bitmap class holds an image.

Unlike [Layer](Layer.md), it is not a display element, so it can be created on its own, independent of any window or layer tree,
and drawing to it does not trigger redraw notifications. Use it for off-screen working images and for holding assets.

Bitmap itself has no drawing methods. To composite, fill, draw text, apply filters and so on,
pass the Bitmap object to methods of the [ImageFunction](ImageFunction.md) class.

To exchange images with a Layer, use [Layer.copyToBitmapFromMainImage](Layer.md#copytobitmapfrommainimage) /
[Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage). In addition, a Bitmap can be passed directly as the source (operand) of
Layer's `copyRect` / `operateRect` / `stretchCopy` / `operateStretch` / `affineCopy` / `operateAffine` /
`copy9Patch`.

For how the three relate and when to use which, see [Layer, Bitmap and ImageFunction](../guide/LayerAndBitmap.md).

## Members

### Constructors

- [Bitmap](#bitmap)
- [Bitmap](#bitmap)
- [Bitmap](#bitmap)

### Properties

- [width](#width)
- [height](#height)
- [buffer](#buffer)
- [bufferForWrite](#bufferforwrite)
- [bufferPitch](#bufferpitch)
- [loading](#loading)
- [imageWidth](#imagewidth)
- [imageHeight](#imageheight)
- [mainImageBuffer](#mainimagebuffer)
- [mainImageBufferForWrite](#mainimagebufferforwrite)
- [mainImageBufferPitch](#mainimagebufferpitch)

### Methods

- [getPixel](#getpixel)
- [setPixel](#setpixel)
- [getMaskPixel](#getmaskpixel)
- [setMaskPixel](#setmaskpixel)
- [independ](#independ)
- [setSize](#setsize)
- [copyFrom](#copyfrom)
- [save](#save)
- [load](#load)
- [loadAsync](#loadasync)
- [loadHeader](#loadheader)
- [getSaveOption](#getsaveoption)

### Events

- [onLoaded](#onloaded)

---

### Bitmap

Constructor

**Description**

Constructs a Bitmap object

Constructs an object of the Bitmap class.

Initially, the width and height are 32 pixels.

---

### Bitmap

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Image width. |
| `height` | `&nbsp;` | Image height. |
| `bpp` | `32` | Number of bits per pixel.<br>Specify either 32 or 8. |

**Description**

Constructs a Bitmap object

Constructs an object of the Bitmap class with the given size.

---

### Bitmap

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Image file name. |
| `colorkey` | `clNone` | Color key.<br>The values are the same as for [Layer.loadImages](Layer.md#loadimages). |

**Description**

Constructs a Bitmap object

Constructs an object of the Bitmap class from a file.

---

### width

Property \ Access: `r/w`

**Description**

Image width

Image width in pixels.

This property can also be set.

**See also:** [Bitmap.setSize](Bitmap.md#setsize)

---

### height

Property \ Access: `r/w`

**Description**

Image height

Image height in pixels.

This property can also be set.

**See also:** [Bitmap.setSize](Bitmap.md#setsize)

---

### buffer

Property \ Access: `r`

**Description**

Image buffer pointer

Pointer to the top-left corner of the image buffer (a 32bpp bitmap containing color and mask (opacity) information).

This property provides direct access to the image buffer for plugins and the like.

It is returned as an integer; in a plugin, cast it to an appropriate type (const unsigned long * etc.) before use.

Do not write to the pointer obtained from this property.
You can write to the pointer obtained from [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite).

The image size is given by the [Bitmap.width](Bitmap.md#width) and [Bitmap.height](Bitmap.md#height) properties.

For how to compute pointers, see [Bitmap.bufferPitch](Bitmap.md#bufferpitch).

**See also:** [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### bufferForWrite

Property \ Access: `r`

**Description**

Image buffer pointer (for writing)

Pointer to the top-left corner of the image buffer (a 32bpp bitmap containing color and mask (opacity) information).

This property provides direct access to the image buffer for plugins and the like.

It is returned as an integer; in a plugin, cast it to an appropriate type (unsigned long * etc.) before use.

Unlike [Bitmap.buffer](Bitmap.md#buffer), you can write to the pointer obtained from this property. Internally, Kirikiri shares identical images among multiple objects;
reading this property breaks that sharing.

The image size is given by the [Bitmap.width](Bitmap.md#width) and [Bitmap.height](Bitmap.md#height) properties.

For how to compute pointers, see [Bitmap.bufferPitch](Bitmap.md#bufferpitch).

**See also:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### bufferPitch

Property \ Access: `r`

**Description**

Image buffer pitch

Pitch of the image buffer (a 32bpp bitmap containing color and mask (opacity) information),
i.e. the number of bytes to the next scan line down.

This property provides direct access to the image buffer for plugins and the like.

With tjs_uint32 as a 32-bit integer type and tjs_uint8 as an 8-bit (1-byte) integer type, the pointer to image position (x, y)
can be computed in C as follows.

`( (tjs_uint32*)( (tjs_uint8*)buffer + y*bufferPitch )) + x`

Note that this property returns the number of bytes to the next scan line, not the number of pixels.
The value may be somewhat larger than the number of bytes strictly required for the image width.

Note that this value can be negative.

**See also:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite)

---

### loading

Property \ Access: `r`

**Description**

Whether asynchronous loading is in progress

Indicates whether asynchronous loading is in progress.

While this is true, asynchronous loading is in progress.

Note that accessing other members during asynchronous loading throws an exception.

**See also:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### imageWidth

Property \ Access: `r`

**Description**

Image width (alias of [Bitmap.width](Bitmap.md#width))

Image width in pixels. A read-only alias that returns the same value as [Bitmap.width](Bitmap.md#width).

It exists so that draw devices and plugins can get the image through a property of the same name without distinguishing between [Layer](Layer.md) and Bitmap (same name as [Layer.imageWidth](Layer.md#imagewidth)).

**See also:** [Bitmap.width](Bitmap.md#width) / [Bitmap.imageHeight](Bitmap.md#imageheight)

---

### imageHeight

Property \ Access: `r`

**Description**

Image height (alias of [Bitmap.height](Bitmap.md#height))

Image height in pixels. A read-only alias that returns the same value as [Bitmap.height](Bitmap.md#height).

It exists so that draw devices and plugins can get the image through a property of the same name without distinguishing between [Layer](Layer.md) and Bitmap (same name as [Layer.imageHeight](Layer.md#imageheight)).

**See also:** [Bitmap.height](Bitmap.md#height) / [Bitmap.imageWidth](Bitmap.md#imagewidth)

---

### mainImageBuffer

Property \ Access: `r`

**Description**

Image buffer pointer (alias of [Bitmap.buffer](Bitmap.md#buffer))

Pointer to the top-left corner of the image buffer. A read-only alias that returns the same value as [Bitmap.buffer](Bitmap.md#buffer).

It exists so that draw devices and plugins can get the image through a property of the same name without distinguishing between [Layer](Layer.md) and Bitmap (same name as [Layer.mainImageBuffer](Layer.md#mainimagebuffer)). Do not write to this pointer; to write, use [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite).

**See also:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite) / [Bitmap.mainImageBufferPitch](Bitmap.md#mainimagebufferpitch)

---

### mainImageBufferForWrite

Property \ Access: `r`

**Description**

Image buffer pointer for writing (alias of [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite))

Pointer to the top-left corner of the writable image buffer. A read-only alias that returns the same value as [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) (reading it breaks image sharing).

It exists so that draw devices and plugins can get the image through a property of the same name without distinguishing between [Layer](Layer.md) and Bitmap (same name as [Layer.mainImageBufferForWrite](Layer.md#mainimagebufferforwrite)).

**See also:** [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) / [Bitmap.mainImageBuffer](Bitmap.md#mainimagebuffer) / [Bitmap.mainImageBufferPitch](Bitmap.md#mainimagebufferpitch)

---

### mainImageBufferPitch

Property \ Access: `r`

**Description**

Image buffer pitch (alias of [Bitmap.bufferPitch](Bitmap.md#bufferpitch))

Pitch of the image buffer (the number of bytes to the next scan line down). A read-only alias that returns the same value as [Bitmap.bufferPitch](Bitmap.md#bufferpitch) (the value can be negative).

It exists so that draw devices and plugins can get the image through a property of the same name without distinguishing between [Layer](Layer.md) and Bitmap (same name as [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch)).

**See also:** [Bitmap.bufferPitch](Bitmap.md#bufferpitch) / [Bitmap.mainImageBuffer](Bitmap.md#mainimagebuffer) / [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite)

---

### getPixel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate to read, in pixels. |
| `y` | `&nbsp;` | y coordinate to read, in pixels. |

**Return value**

Pixel value

**Description**

Gets a pixel value

Gets a pixel value of the image.

**See also:** [Bitmap.setPixel](Bitmap.md#setpixel)

---

### setPixel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate to write, in pixels. |
| `y` | `&nbsp;` | y coordinate to write, in pixels. |
| `value` | `&nbsp;` | Pixel value to set. |

**Description**

Sets a pixel value

Sets a pixel value of the image.

**See also:** [Bitmap.getPixel](Bitmap.md#getpixel)

---

### getMaskPixel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate to read, in pixels. |
| `y` | `&nbsp;` | y coordinate to read, in pixels. |

**Return value**

Alpha value of the pixel

**Description**

Gets the alpha value of a pixel

Gets the alpha value of a pixel of the image.

**See also:** [Bitmap.setMaskPixel](Bitmap.md#setmaskpixel)

---

### setMaskPixel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | x coordinate to write, in pixels. |
| `y` | `&nbsp;` | y coordinate to write, in pixels. |
| `value` | `&nbsp;` | Alpha value of the pixel to set. |

**Description**

Sets the alpha value of a pixel

Sets the alpha value of a pixel of the image.

**See also:** [Bitmap.getMaskPixel](Bitmap.md#getmaskpixel)

---

### independ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `copy` | `true` | Whether to copy the original image when breaking the sharing.<br>If true, the original image is copied. If false, it is not copied and the image<br>contents are undefined. |

**Description**

Stops sharing the image

Forces the image out of the shared state.

When you copy a whole image, e.g. with assignImages, Kirikiri does not actually copy the
image buffer; the objects share the same image instead.

Normally the sharing is broken automatically just before the image is modified,
but this method lets you break it explicitly.

If you pass false for the copy argument, the sharing is broken but the original image is not
guaranteed to be carried over (the image contents become undefined); in exchange, breaking the sharing
is faster. If you are going to rewrite the whole image you do not need the original,
so calling this method with false before drawing may be more efficient.

This method does nothing if the image is not shared.

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Image width in pixels.<br>This value can also be read and written via the [Bitmap.width](Bitmap.md#width) property. |
| `height` | `&nbsp;` | Image height in pixels.<br>This value can also be read and written via the [Bitmap.height](Bitmap.md#height) property. |

**Description**

Sets the image size

Sets the image size.

---

### copyFrom

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` | Source Bitmap object. |

**Description**

Copies an image

Copies an image.

The "copy" merely makes two or more objects share the same image,
so this method takes almost no time.

---

### save

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the storage to save to. |
| `type` | `"bmp"` | Image format to save in, as a string. The current version supports the following formats.<br>"**bmp**" or "**bmp32**"<br>32bpp BMP. The alpha channel (mask) is saved too.<br>"**bmp24**"<br>24bpp BMP. The alpha channel (mask) is not saved.<br>"**bmp8**"<br>8bpp BMP. The alpha channel (mask) is not saved. The image is<br>color-reduced with 4x4 ordered dithering to a fixed 252-color palette.<br>"**jpg**"<br>JPEG. The alpha channel (mask) is not saved. The image is<br>saved at 90% quality.<br>"**jpg###**"<br>JPEG. The alpha channel (mask) is not saved. The image is<br>saved at the quality given by ###: "jpg010" is 10%, "jpg100" is 100%, "jpg080" is 80%.<br>"**png**"<br>32bpp PNG. The alpha channel (mask) is saved too.<br>"**png24**"<br>24bpp PNG. The alpha channel (mask) is not saved.<br>"**tlg5**"<br>32bpp TLG5. The alpha channel (mask) is saved too.<br>"**tlg524**"<br>24bpp TLG5. The alpha channel (mask) is not saved.<br>"**tlg6**"<br>32bpp TLG6. The alpha channel (mask) is saved too.<br>"**tlg624**"<br>24bpp TLG6. The alpha channel (mask) is not saved. |
| `meta` | `null` | For TLG formats, the tag information to save, as a dictionary.<br>For other formats, additional options (1.3.0 and later).<br>The available options can be obtained with getSaveOption. |

**Description**

Saves the image

Saves the image to the storage (file) specified by name, in the image format specified by type.

**See also:** [Bitmap.getSaveOption](Bitmap.md#getsaveoption)

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `image` | `&nbsp;` | Image storage to load. |
| `colorkey` | `clNone` | Color key (transparent color) of the image to load.<br>If you specify a color in 0xRRGGBB format, that color becomes the color key.<br>If you specify `**clPalIdx**` plus a palette index,<br>that palette index becomes transparent (for images with 256 colors or fewer).<br>If you specify `**clAdapt**`, the color used most often in the top line of the image<br>automatically becomes transparent.<br>If you specify `**clAlphaMat**` plus a color in 0xRRGGBB<br>format, the image is composited onto that color<br>using alpha blending (the ltAlpha method).<br>For example, specifying (clAlphaMat + 0xffffff)<br>composites the loaded image onto white.<br>The resulting image is fully opaque<br>(note that although the image becomes fully opaque,<br>this mode does not change the tag information at all). |

**Return value**

Dictionary of tag information

**Description**

Loads an image

Loads an image.

Returns a dictionary of tag information (information about the image itself, such as its layer type and display position).

If the image has no tag information, null is returned.

In the current version, only PNG and TLG5/6 images can carry tag information. For the information available, see [Image Format Converter](../guide/TPC.md).

---

### loadAsync

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `image` | `&nbsp;` | Image storage to load.<br>Note that the file name must include the extension.<br>Without an extension the file is not found and an error occurs. |

**Description**

Loads an image asynchronously

Loads an image asynchronously.

Completion is reported via [Bitmap.onLoaded](Bitmap.md#onloaded).

You can check whether asynchronous loading is in progress with [Bitmap.loading](Bitmap.md#loading).

While asynchronous loading is in progress, accessing any member other than [Bitmap.loading](Bitmap.md#loading) throws an exception.

See also the description of [Bitmap.onLoaded](Bitmap.md#onloaded).

**See also:** [Bitmap.onLoaded](Bitmap.md#onloaded) / [Bitmap.loading](Bitmap.md#loading) / [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage)

---

### loadHeader

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `image` | `&nbsp;` | Image storage to load.<br>Note that the file name must include the extension.<br>Without an extension the file is not found and an error occurs. |

**Return value**

Dictionary of information

**Description**

Loads image information (1.3.0 and later)

Loads only the image information.

The image itself is not loaded, so this is fast when you only need the information.

The returned dictionary always contains width and height; other information depends on the image format.

---

### getSaveOption

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` | Image format.<br>Specified in the same form as for the save method. |

**Return value**

Dictionary of additional information

**Description**

Gets additional save options (1.3.0 and later)

Gets the additional information that can be specified when saving an image.

**See also:** [Bitmap.save](Bitmap.md#save)

---

### onLoaded

Event

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `meta` | `&nbsp;` | Tag information of the loaded image. |
| `async` | `&nbsp;` | Whether the image was loaded asynchronously.<br>If the image data is in the cache, this event fires while [Bitmap.loadAsync](Bitmap.md#loadasync) is still executing. |
| `error` | `&nbsp;` | Whether an error occurred while loading the image. |
| `message` | `&nbsp;` | Error message.<br>If an error occurred, the error message is passed here. |

**Description**

Asynchronous loading has completed

Fired when asynchronous loading completes.

The loaded image can be copied to a Layer with [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage).

Because loading is asynchronous, the Layer you intend to pass the image to may already have been invalidated when loading completes.

If you access other objects in this event, check that they have not been invalidated.

Alternatively, make sure the target objects are not invalidated until this event completes.

**See also:** [Bitmap.loadAsync](Bitmap.md#loadasync) / [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage)

---
