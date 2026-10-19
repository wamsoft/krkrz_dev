# ImageFunction

The ImageFunction class manipulates images.

You cannot create objects of this class. All methods are class methods (static) and are called directly, as in
`ImageFunction.operateRect(...)`.

Only [Bitmap](Bitmap.md) objects can be operated on; [Layer](Layer.md) objects cannot be specified.
Think of these as the drawing methods of the same name on Layer with the Layer-specific aspects (properties such as face / holdAlpha / the clip rectangle,
and the redraw notification after drawing) removed and everything turned into explicit arguments.
If `omAuto` is specified as the operation mode, it is always treated as `omAlpha`, because a Bitmap has no information
corresponding to [Layer.type](Layer.md#type).

For how Layer and Bitmap relate and when to use each, see [Layer, Bitmap, and ImageFunction](../guide/LayerAndBitmap.md).

## Members

### Methods

- [operateAffine](#operateaffine)
- [operateRect](#operaterect)
- [operateStretch](#operatestretch)
- [flipLR](#fliplr)
- [flipUD](#flipud)
- [adjustGamma](#adjustgamma)
- [doBoxBlur](#doboxblur)
- [doGrayScale](#dograyscale)
- [colorRect](#colorrect)
- [drawText](#drawtext)
- [drawGlyph](#drawglyph)
- [fillRect](#fillrect)
- [copy9Patch](#copy9patch)

---

### operateAffine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dst` | `&nbsp;` | The destination Bitmap object. |
| `src` | `&nbsp;` | The source Bitmap object. |
| `A` | `&nbsp;` | Parameter A. Its interpretation depends on the affine argument. |
| `B` | `&nbsp;` | Parameter B. Its interpretation depends on the affine argument. |
| `C` | `&nbsp;` | Parameter C. Its interpretation depends on the affine argument. |
| `D` | `&nbsp;` | Parameter D. Its interpretation depends on the affine argument. |
| `E` | `&nbsp;` | Parameter E. Its interpretation depends on the affine argument. |
| `F` | `&nbsp;` | Parameter F. Its interpretation depends on the affine argument. |
| `srcrect` | `null` | The rectangle to composite, as a Rect object in pixels (in image coordinates of the source Bitmap).<br>If omitted, the whole image is used. |
| `cliprect` | `null` | The clipping rectangle, as a Rect object (in image coordinates of the destination Bitmap).<br>If omitted, no clipping is performed. |
| `affine` | `&nbsp;` | How the following six arguments (parameters A to F) are interpreted.<br>If true, the six parameters are interpreted as follows.<br>`A   : a of the 2D affine transform matrix`<br>`B   : b of the 2D affine transform matrix`<br>`C   : c of the 2D affine transform matrix`<br>`D   : d of the 2D affine transform matrix`<br>`E   : tx of the 2D affine transform matrix`<br>`F   : ty of the 2D affine transform matrix`<br>With the affine transform, a source image position (x, y) (where the top-left corner of the source rectangle is (0, 0)) is transformed into the destination image position (x', y') by the following formulas.<br>x' =  a*x + c*y + tx<br>y' =  b*x + d*y + ty<br>If false, the six parameters are interpreted as follows.<br>`A   : X coordinate in the destination image of the top-left corner of the source rectangle (x0)`<br>`B   : Y coordinate in the destination image of the top-left corner of the source rectangle (y0)`<br>`C   : X coordinate in the destination image of the top-right corner of the source rectangle (x1)`<br>`D   : Y coordinate in the destination image of the top-right corner of the source rectangle (y1)`<br>`E   : X coordinate in the destination image of the bottom-left corner of the source rectangle (x2)`<br>`F   : Y coordinate in the destination image of the bottom-left corner of the source rectangle (y2)`<br>If false, the destination position (x3, y3) corresponding to the bottom-right corner of the source is calculated automatically by the following formulas.<br>x3 = x1 - x0 + x2<br>y3 = y1 - y0 + y2 |
| `mode` | `omAlpha` | The operation mode.<br>`**omPsNormal**`: Photoshop-compatible alpha blending is performed (not implemented in the current version).<br>`**omPsAdditive**`: Photoshop-compatible Linear Dodge blending is performed (not implemented in the current version).<br>`**omPsSubtractive**`: Photoshop-compatible Linear Burn blending is performed (not implemented in the current version).<br>`**omPsMultiplicative**`: Photoshop-compatible Multiply blending is performed (not implemented in the current version).<br>`**omPsScreen**`: Photoshop-compatible Screen blending is performed (not implemented in the current version).<br>`**omPsOverlay**`: Photoshop-compatible Overlay blending is performed (not implemented in the current version).<br>`**omPsHardLight**`: Photoshop-compatible Hard Light blending is performed (not implemented in the current version).<br>`**omPsSoftLight**`: Photoshop-compatible Soft Light blending is performed (not implemented in the current version).<br>`**omPsColorDodge**`: Photoshop-compatible Color Dodge blending is performed (not implemented in the current version).<br>`**omPsColorDodge5**`: Color Dodge blending compatible with Photoshop 5.x and earlier is performed (not implemented in the current version).<br>`**omPsColorBurn**`: Photoshop-compatible Color Burn blending is performed (not implemented in the current version).<br>`**omPsLighten**`: Photoshop-compatible Lighten blending is performed (not implemented in the current version).<br>`**omPsDarken**`: Photoshop-compatible Darken blending is performed (not implemented in the current version).<br>`**omPsDifference**`: Photoshop-compatible Difference blending is performed (not implemented in the current version).<br>`**omPsDifference5**`: Difference blending compatible with Photoshop 5.x and earlier is performed (not implemented in the current version).<br>`**omPsExclusion**`: Photoshop-compatible Exclusion blending is performed (not implemented in the current version).<br>`**omAdditive**`: additive blending is performed (not implemented in the current version).<br>`**omSubtractive**`: subtractive blending is performed (not implemented in the current version).<br>`**omMultiplicative**`: multiplicative blending is performed (not implemented in the current version).<br>`**omDodge**`: dodge blending is performed (not implemented in the current version).<br>`**omDarken**`: darken (comparison) blending is performed (not implemented in the current version).<br>`**omLighten**`: lighten (comparison) blending is performed (not implemented in the current version).<br>`**omScreen**`: screen blending is performed (not implemented in the current version).<br>`**omAlpha**`: alpha blending is performed.<br>`**omAddAlpha**`: additive alpha blending is performed. In this case, when face is dfOpaque and hda is false, linear interpolation is possible by specifying stFastLinear as the type argument.<br>`**omOpaque**`: the alpha information of src is ignored and src is always treated as fully opaque. In this case, when face is dfOpaque and hda is false, linear interpolation is possible by specifying stFastLinear as the type argument. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `opa` | `255` | The opacity of the composite (0 to 255). |
| `type` | `stNearest` | The type of affine transform.<br>`**stNearest**    ` : nearest neighbor is used<br>`**stFastLinear** ` : low-precision linear interpolation is used (partially implemented)<br>`**stLinear**     ` : linear interpolation is used (not implemented)<br>`**stCubic**      ` : bicubic interpolation is used (not implemented)<br>Speed is fastest in the order stNearest > stFastLinear > stLinear > stCubic, but the faster the mode,<br>the lower the image quality.<br>For stFastLinear, stLinear, and stCubic, you can add stRefNoClip with a bitwise OR;<br>this allows colors outside the area of the bitmap being copied to be referenced when compositing.<br>Without it, pixels outside the source bitmap's range are never referenced, even if the source bitmap<br>has room around it (colors outside the range are treated as the color of the nearest pixel<br>within the range). |
| `hda` | `false` | Whether to protect the alpha channel. |

**Description**

Composites with an affine transform

Composites the specified rectangle of the source Bitmap onto the destination while applying an affine transform.

---

### operateRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dst` | `&nbsp;` | The destination Bitmap object. |
| `dleft` | `&nbsp;` | Left edge of the destination rectangle, in pixels (in image coordinates of the destination Bitmap). |
| `dtop` | `&nbsp;` | Top edge of the destination rectangle, in pixels (in image coordinates of the destination Bitmap). |
| `src` | `&nbsp;` | The source Bitmap object.<br>If omitted, the whole image is used. |
| `srcrect` | `null` | The rectangle to operate on, as a Rect object in pixels (in image coordinates of the source Bitmap).<br>If omitted, the whole image is used. |
| `cliprect` | `null` | The clipping rectangle, as a Rect object (in image coordinates of the destination Bitmap).<br>If omitted, no clipping is performed. |
| `mode` | `omAuto` | The operation mode.<br>`**omPsNormal**`: Photoshop-compatible alpha blending is performed.<br>`**omPsAdditive**`: Photoshop-compatible Linear Dodge blending is performed.<br>`**omPsSubtractive**`: Photoshop-compatible Linear Burn blending is performed.<br>`**omPsMultiplicative**`: Photoshop-compatible Multiply blending is performed.<br>`**omPsScreen**`: Photoshop-compatible Screen blending is performed.<br>`**omPsOverlay**`: Photoshop-compatible Overlay blending is performed.<br>`**omPsHardLight**`: Photoshop-compatible Hard Light blending is performed.<br>`**omPsSoftLight**`: Photoshop-compatible Soft Light blending is performed.<br>`**omPsColorDodge**`: Photoshop-compatible Color Dodge blending is performed.<br>`**omPsColorDodge5**`: Color Dodge blending compatible with Photoshop 5.x and earlier is performed.<br>`**omPsColorBurn**`: Photoshop-compatible Color Burn blending is performed.<br>`**omPsLighten**`: Photoshop-compatible Lighten blending is performed.<br>`**omPsDarken**`: Photoshop-compatible Darken blending is performed.<br>`**omPsDifference**`: Photoshop-compatible Difference blending is performed.<br>`**omPsDifference5**`: Difference blending compatible with Photoshop 5.x and earlier is performed.<br>`**omPsExclusion**`: Photoshop-compatible Exclusion blending is performed.<br>`**omAdditive**`: additive blending is performed.<br>`**omSubtractive**`: subtractive blending is performed.<br>`**omMultiplicative**`: multiplicative blending is performed.<br>`**omDodge**`: dodge blending is performed.<br>`**omDarken**`: darken (comparison) blending is performed.<br>`**omLighten**`: lighten (comparison) blending is performed.<br>`**omScreen**`: screen blending is performed.<br>`**omAlpha**`: alpha blending is performed.<br>`**omAddAlpha**`: additive alpha blending is performed.<br>`**omOpaque**`: the alpha information of src is ignored and src is always treated as fully opaque. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `opa` | `255` | The strength of the operation (0 to 255). |
| `hda` | `false` | Whether to protect the alpha channel. |

**Description**

Composites a rectangle

Composites the rectangle of the specified source Bitmap at the specified position of the destination Bitmap using the specified mode.

---

### operateStretch

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dst` | `&nbsp;` | The destination Bitmap object. |
| `src` | `&nbsp;` | The source Bitmap object. |
| `dstrect` | `null` | The destination rectangle, as a Rect object in pixels (in image coordinates of the destination Bitmap).<br>If omitted, the whole image is used. |
| `srcrect` | `null` | The rectangle to composite, as a Rect object in pixels (in image coordinates of the source Bitmap).<br>If omitted, the whole image is used. |
| `cliprect` | `null` | The clipping rectangle, as a Rect object (in image coordinates of the destination Bitmap).<br>If omitted, no clipping is performed. |
| `mode` | `omAuto` | The operation mode.<br>`**omPsNormal**`: Photoshop-compatible alpha blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsAdditive**`: Photoshop-compatible Linear Dodge blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsSubtractive**`: Photoshop-compatible Linear Burn blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsMultiplicative**`: Photoshop-compatible Multiply blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsScreen**`: Photoshop-compatible Screen blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsOverlay**`: Photoshop-compatible Overlay blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsHardLight**`: Photoshop-compatible Hard Light blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsSoftLight**`: Photoshop-compatible Soft Light blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsColorDodge**`: Photoshop-compatible Color Dodge blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsColorDodge5**`: Color Dodge blending compatible with Photoshop 5.x and earlier is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsColorBurn**`: Photoshop-compatible Color Burn blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsLighten**`: Photoshop-compatible Lighten blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsDarken**`: Photoshop-compatible Darken blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsDifference**`: Photoshop-compatible Difference blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsDifference5**`: Difference blending compatible with Photoshop 5.x and earlier is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omPsExclusion**`: Photoshop-compatible Exclusion blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omAdditive**`: additive blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omSubtractive**`: subtractive blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omMultiplicative**`: multiplicative blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omDodge**`: dodge blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omDarken**`: darken (comparison) blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omLighten**`: lighten (comparison) blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omScreen**`: screen blending is performed (since 1.3, implemented for types other than stNearest and stFastLinear).<br>`**omAlpha**`: alpha blending is performed.<br>`**omAddAlpha**`: additive alpha blending is performed. In this case, when face is dfOpaque and hda is false, linear interpolation is possible by specifying stFastLinear as the type argument.<br>`**omOpaque**`: the alpha information of src is ignored and src is always treated as fully opaque. In this case, when face is dfOpaque and hda is false, linear interpolation is possible by specifying stFastLinear as the type argument. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `opa` | `255` | The strength of the operation (0 to 255). |
| `type` | `stNearest` | The type of scaling.<br>`**stNearest**          ` : nearest neighbor is used<br>`**stFastLinear**       ` : low-precision linear interpolation is used (partially implemented)<br>`**stSemiFastLinear**   ` : fixed-point linear interpolation is used (since 1.3)<br>`**stLinear**           ` : linear interpolation is used (implementation changed in 1.3)<br>`**stFastCubic**        ` : fixed-point bicubic interpolation is used (since 1.3)<br>`**stCubic**            ` : bicubic interpolation is used (implementation changed in 1.3)<br>`**stFastLanczos2**     ` : fixed-point Lanczos interpolation over a 4x4 range is used (since 1.3)<br>`**stLanczos2**         ` : Lanczos interpolation over a 4x4 range is used (since 1.3)<br>`**stFastLanczos3**     ` : fixed-point Lanczos interpolation over a 6x6 range is used (since 1.3)<br>`**stLanczos3**         ` : Lanczos interpolation over a 6x6 range is used (since 1.3)<br>`**stFastSpline16**     ` : fixed-point 4x4 spline interpolation is used (since 1.3)<br>`**stSpline16**         ` : 4x4 spline interpolation is used (since 1.3)<br>`**stFastSpline36**     ` : fixed-point 6x6 spline interpolation is used (since 1.3)<br>`**stSpline36**         ` : 6x6 spline interpolation is used (since 1.3)<br>`**stFastAreaAvg**      ` : fixed-point area-averaging reduction is used; cannot enlarge (since 1.3)<br>`**stAreaAvg**          ` : area-averaging reduction is used; cannot enlarge (since 1.3)<br>`**stFastGaussian**     ` : fixed-point 4x4 Gaussian interpolation is used (since 1.3)<br>`**stGaussian**         ` : 4x4 Gaussian interpolation is used (since 1.3)<br>`**stFastBlackmanSinc** ` : fixed-point 8x8 Blackman-Sinc interpolation is used (since 1.3)<br>`**stBlackmanSinc**     ` : 8x8 Blackman-Sinc interpolation is used (since 1.3)<br>Speed is fastest in the order stNearest > stFastLinear > stLinear > stCubic, but the faster the type,<br>the lower the image quality.<br>The interpolation methods from stCubic onward all give sufficiently high quality; choosing among them is largely a matter of taste.<br>Gaussian interpolation, however, produces a somewhat blurry result.<br>The difference between stFastLinear and the other linear interpolations (stSemiFastLinear and stLinear) is most visible when reducing.<br>stFastLinear always references the 4 surrounding pixels, whereas stSemiFastLinear and stLinear, when reducing,<br>reference a range scaled so that it corresponds to 4 pixels at 1x, that is, a wider range of pixels, which gives higher quality<br>(algorithmically, this is true linear interpolation).<br>For stFastLinear, you can add stRefNoClip with a bitwise OR; this<br>allows colors outside the area of the bitmap being copied to be referenced when compositing. Without it,<br>pixels outside the source bitmap's range are never referenced, even if the source bitmap has room around it<br>(colors outside the range are treated as the color of the nearest pixel within the range). |
| `hda` | `false` | Whether to protect the alpha channel. |
| `option` | `-1.0` | Added in 1.3.<br>Sharpness for bicubic interpolation. Currently has no meaning for other interpolation methods.<br>Increasing the sharpness value in the positive direction makes the result blurrier; increasing it in the negative direction makes it sharper. |

**Description**

Composites with scaling

Composites the specified rectangle of the source Bitmap into a rectangle of the destination Bitmap.

If the source and destination rectangles differ in size, the image is enlarged or reduced.

---

### flipLR

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to flip. |
| `rect` | `null` | The area to flip, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Description**

Flips horizontally

Flips the image horizontally.

---

### flipUD

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to flip. |
| `rect` | `null` | The area to flip, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Description**

Flips vertically

Flips the image vertically.

---

### adjustGamma

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to gamma-correct. |
| `rgamma` | `1.0` | Gamma value of the red component (0.0 through 1.0 to 9.0). |
| `rfloor` | `0` | Minimum output value of the red component (0 to 255). |
| `rceil` | `255` | Maximum output value of the red component (0 to 255). |
| `ggamma` | `1.0` | Gamma value of the green component (0.0 through 1.0 to 9.0). |
| `gfloor` | `0` | Minimum output value of the green component (0 to 255). |
| `gceil` | `255` | Maximum output value of the green component (0 to 255). |
| `bgamma` | `1.0` | Gamma value of the blue component (0.0 through 1.0 to 9.0). |
| `bfloor` | `0` | Minimum output value of the blue component (0 to 255). |
| `bceil` | `255` | Maximum output value of the blue component (0 to 255). |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |
| `isaddalpha` | `false` | Whether the image is in additive alpha format. |

**Description**

Gamma correction

Applies gamma correction to the image.

A gamma value of 1.0 makes the gamma curve a straight line.

The minimum and maximum output values specify the lowest and highest luminance of each component.

Setting the maximum lower than the minimum inverts the image.

If isaddalpha is true, this method uses a special gamma correction routine for additive alpha blending.

This routine applies gamma correction to the part of additive alpha blending that corresponds to alpha blending, but not to the part that corresponds to additive blending.

---

### doBoxBlur

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to blur. |
| `xblur` | `1` | The horizontal blur range. |
| `yblur` | `1` | The vertical blur range. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |
| `isalpha` | `true` | Whether the image has an alpha channel. |

**Description**

Applies a box blur

Applies a blur. The algorithm is a box blur.

A box blur takes the average luminance of the pixels within the range given by the two parameters xblur and yblur. For example, with xblur=10 and yblur=2, the average luminance of the pixels in the rectangle from -10 to 10 horizontally and -2 to 2 vertically, centered on the target pixel, becomes that pixel's final luminance.

The area of the range is (xblur x 2 + 1) x (yblur x 2 + 1). In the current version, if this area is less than 256, a faster algorithm is used than when it is 256 or more.

If isalpha is true, a special algorithm for alpha blending is used, which is somewhat slower.

If false, a faster algorithm is used.

---

### doGrayScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to convert to grayscale. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |
| `rweight` | `&nbsp;` | Weight of the red component. Omit all three or specify all three. |
| `gweight` | `&nbsp;` | Weight of the green component. |
| `bweight` | `&nbsp;` | Weight of the blue component. |

**Description**

Converts to grayscale

Converts the image to grayscale.

If rweight / gweight / bweight are omitted, BT.709-equivalent weights
(0.2126 / 0.7152 / 0.0722) are used (the previous behavior). The weights are handled the same way as in
[Layer.doGrayScale](Layer.md#dograyscale).

---

### colorRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to fill. |
| `value` | `&nbsp;` | The color or value to fill with.<br>Its meaning depends on the face argument.<br>`**dfAlpha**    ` : specify a color in 0xRRGGBB format<br>`**dfAddAlpha** ` : specify a color in 0xRRGGBB format<br>`**dfOpaque**   ` : specify a color in 0xRRGGBB format<br>`**dfMask**     ` : specify a mask (opacity) value (0 to 255)<br>With dfOpaque, the mask information is ignored. With dfMask, the color information is left unchanged.<br>With dfAlpha and a negative opa, this argument is ignored. |
| `opa` | `255` | The fill opacity (-255 through 0 to 255).<br>This argument is ignored when face is dfMask or dfProvince (always fully opaque).<br>Negative values are valid only when face is dfAlpha;<br>in that case the value argument is ignored and opacity is removed from the image<br>(specifying -255 makes the rectangle fully transparent). |
| `rect` | `null` | The rectangle to fill, as a Rect object in pixels (in image coordinates).<br>If omitted, the whole image is used. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Description**

Fills a rectangle semi-transparently

Fills a rectangle of the specified Bitmap image using the specified method.

Unlike [ImageFunction.fillRect](ImageFunction.md#fillrect), you can specify an opacity and fill semi-transparently.

---

### drawText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to draw text on. |
| `font` | `&nbsp;` | The font to draw with, as a Font object. |
| `x` | `&nbsp;` | The x coordinate, in pixels, of the origin where text drawing starts (in image coordinates). |
| `y` | `&nbsp;` | The y coordinate, in pixels, of the origin where text drawing starts (in image coordinates). |
| `text` | `&nbsp;` | The text to draw. |
| `color` | `&nbsp;` | The text color, in 0xRRGGBB format. |
| `opa` | `255` | The opacity of the text (-255 through 0 to 255).<br>Negative values are valid only when face is dfAlpha;<br>in that case opacity is removed in the shape of the text (the smaller the value,<br>the stronger the effect). |
| `aa` | `true` | Whether to anti-alias.<br>True enables anti-aliasing; false disables it. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `shadowlevel` | `0` | The opacity of the shadow. The appropriate value depends on the shadowwidth argument.<br>Specifying 0 draws no shadow. |
| `shadowcolor` | `0x000000` | The shadow color, in 0xRRGGBB format. |
| `shadowwidth` | `0` | The width (blur) of the shadow. 0 is the sharpest (no blur); larger<br>values blur the shadow more. |
| `shadowofsx` | `0` | The x offset of the shadow, in pixels. Specifying 0 draws the shadow directly below. |
| `shadowofsy` | `0` | The y offset of the shadow, in pixels. Specifying 0 draws the shadow directly below. |
| `hda` | `false` | Whether to protect the alpha channel. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Return value**

The drawn area (a Rect object).

**Description**

Draws text

Draws text on a Bitmap.

When face is dfOpaque, whether the destination mask is destroyed or protected depends on hda.

---

### drawGlyph

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to draw text on. |
| `x` | `&nbsp;` | The x coordinate, in pixels, of the origin where text drawing starts (in image coordinates). |
| `y` | `&nbsp;` | The y coordinate, in pixels, of the origin where text drawing starts (in image coordinates). |
| `glyph` | `&nbsp;` | The glyph to draw. |
| `color` | `&nbsp;` | The text color, in 0xRRGGBB format. |
| `opa` | `255` | The opacity of the text (-255 through 0 to 255).<br>Negative values are valid only when face is dfAlpha;<br>in that case opacity is removed in the shape of the text (the smaller the value,<br>the stronger the effect). |
| `aa` | `true` | Whether to anti-alias.<br>True enables anti-aliasing; false disables it. |
| `face` | `dfAlpha` | The drawing method.<br>`**dfAlpha**`: the image is treated as an image with an alpha channel when drawn.<br>`**dfAddAlpha**`: the image is treated as an image with an additive alpha channel when drawn.<br>`**dfOpaque**`: the image is treated as fully opaque when drawn. |
| `shadowlevel` | `0` | The opacity of the shadow. The appropriate value depends on the shadowwidth argument.<br>Specifying 0 draws no shadow. |
| `shadowcolor` | `0x000000` | The shadow color, in 0xRRGGBB format. |
| `shadowwidth` | `0` | The width (blur) of the shadow. 0 is the sharpest (no blur); larger<br>values blur the shadow more. |
| `shadowofsx` | `0` | The x offset of the shadow, in pixels. Specifying 0 draws the shadow directly below. |
| `shadowofsy` | `0` | The y offset of the shadow, in pixels. Specifying 0 draws the shadow directly below. |
| `hda` | `false` | Whether to protect the alpha channel. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Return value**

The drawn area (a Rect object).

**Description**

Draws text

Draws a glyph on a Bitmap.

When face is dfOpaque, whether the destination mask is destroyed or protected depends on hda.

The glyph is specified as an array of the form glyph : Array[9] = [ width, height, originx, originy, incx, incy, inc, bitmap(Octet), colors ].

If colors is omitted from the glyph, 256 levels are assumed.

---

### fillRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bmp` | `&nbsp;` | The Bitmap object to fill. |
| `value` | `&nbsp;` | The color or value to fill with.<br>Its meaning depends on isalpha.<br>`**true**  ` : specify opacity and color in 0xAARRGGBB format. Both the main image and the mask are filled.<br>`**false** ` : specify a color in 0xRRGGBB format. |
| `rect` | `null` | The rectangle to fill, as a Rect object in pixels (in image coordinates).<br>If omitted, the whole image is used. |
| `isalpha` | `true` | Whether the image has an alpha channel. |
| `cliprect` | `null` | The clipping area, as a Rect object (in image coordinates of the Bitmap).<br>If omitted, the whole image is used. |

**Description**

Fills a rectangle

Fills a rectangle of the specified Bitmap image using the specified method.

---

### copy9Patch

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `dst` | `Bitmap` | `&nbsp;` | Destination Bitmap. |
| `src` | `Bitmap` | `&nbsp;` | Source Bitmap. |

**Return value**

The margin information.

**Description**

Copies an image using 9-patch (multi-platform version and later)

Copies an image using 9-patch (slicing).
The returned margin information is a Rect object.
Draw text and the like within these margins.

---
