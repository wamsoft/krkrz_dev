---
source_hash: 5e623e59194b
---

# Image Processing

This page describes the image processing features supported by Kirikiri Z.

## Overview

Image processing in Kirikiri Z uses a CPU-side 32bpp BGRA bitmap (`tTVPBaseBitmap`) as the compositing surface. Pixel operations such as blending (compositing operations) and resampling (scaling and rotation) are accelerated with SIMD implementations (SSE2 / AVX2 / NEON), and a C reference implementation (`tvpgl.c`) is provided for environments where SIMD is not available.

There is also a GPU drawing path based on the OpenGL ES Canvas / Texture classes, which performs texture compositing and shader-based drawing on the GPU.

### Contents

[Specifications](#spec)

[Readable and writable image formats](#imageformat)

[Compositing operations](#blend_mode)

## Specifications { #spec }

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- | --- |
| Compositing<br>operations | Opaque | Multiplicative | Photoshop-compatible<br>Linear Dodge (additive) | Photoshop-compatible<br>Hard Light | Photoshop-compatible<br>Lighten |
| Compositing<br>operations | Alpha | Dodge | Photoshop-compatible<br>Linear Burn (subtractive) | Photoshop-compatible<br>Soft Light | Photoshop-compatible<br>Darken |
| Compositing<br>operations | Additive alpha | Lighten | Photoshop-compatible<br>Multiply | Photoshop-compatible<br>Color Dodge | Photoshop-compatible<br>Difference |
| Compositing<br>operations | Additive | Darken | Photoshop-compatible<br>Screen | Photoshop 5.x and earlier compatible<br>Color Dodge | Photoshop 5.x and earlier compatible<br>Difference |
| Compositing<br>operations | Subtractive | Screen | Photoshop-compatible<br>Overlay | Photoshop-compatible<br>Color Burn | Photoshop-compatible<br>Exclusion |

## Readable and writable image formats { #imageformat }

The following image formats can be both read and written out of the box.

| Format | Extension | Notes |
| --- | --- | --- |
| BMP | .bmp | The standard Windows bitmap format. A 32bpp BMP is treated as having an alpha channel. |
| JPEG | .jpg / .jpeg | Decoded and encoded with libjpeg-turbo. |
| PNG | .png | Decoded and encoded with libpng. Supports alpha channels. |
| TLG5 / TLG6 | .tlg | Kirikiri's own lossless compression format. TLG5 is designed for fast decoding, TLG6 for a high compression ratio. |

The **main/mask split format** is also supported, in which the color image (main) and the alpha channel (mask) are stored separately. The mask image's file name is the main image's file name with `_m` appended (for example, `abc_m.jpg` for `abc.jpg`). The main and mask images may use different formats.

Plugins can add support for more image formats.

## Compositing operations { #blend_mode }

The table below lists the layer compositing operations (layer types). In the formulas, *result* is the result, *dest* is the luminance of the destination, *src* is the luminance of the image being composited, and *α* is the per-pixel alpha value; all values range from 0.0 to 1.0. `blend(a, b, r)` means `a × (1.0 - r) + b × r`.

| No. | Type | Formula | Description |
| --- | --- | --- | --- |
| 1 | Opaque | result = src | Composites without referring to the alpha channel. |
| 2 | Alpha | result = blend(dest, src, α) | Performs alpha compositing.<br>This is the most basic type for transparency. |
| 3 | Additive alpha | result = min(1.0, dest × ( 1.0 - α ) + src) | Performs additive alpha compositing. |
| 4 | Additive | result = min(1.0, dest + src) | Performs additive compositing. Well suited to glow effects.<br>Equivalent to Photoshop's "Linear Dodge" (see 11), except that alpha is ignored in this operation.<br>The neutral color (the color that causes no change when composited) is black. |
| 5 | Subtractive | result = max(0.0, dest + src - 1.0)<br>* The only difference from result = dest - src is whether src is inverted. | Performs subtractive compositing. α is ignored.<br>The neutral color is white. |
| 6 | Multiplicative | result = dest × src | Performs multiplicative compositing.<br>α is ignored.<br>The neutral color is white. |
| 7 | Dodge | result = min(1.0, dest ÷ ( 1.0 - src ) ) | Performs dodge compositing.<br>Well suited to depicting objects lit by light.<br>α is ignored.<br>The neutral color is black. |
| 8 | Lighten | result = max(dest, src) | Performs "Lighten" compositing.<br>α is ignored.<br>The neutral color is black. |
| 9 | Darken | result = min(dest, src) | Performs "Darken" compositing.<br>α is ignored.<br>The neutral color is white. |
| 10 | Screen | result = 1.0 - ( 1.0 - dest ) × ( 1.0 - src ) | Performs "Screen" compositing.<br>α is ignored.<br>The neutral color is black. |
| 11 | Photoshop-compatible<br>Linear Dodge<br>(additive) | result = blend(dest, min(1.0, dest + src), α) | Performs Photoshop-compatible "Linear Dodge" (additive) compositing.<br>Unlike 4 (Additive), α is not ignored.<br>The neutral color is black. |
| 12 | Photoshop-compatible<br>Linear Burn<br>(subtractive) | result = blend(dest, max(0.0, dest + src - 1.0), α) | Performs Photoshop-compatible "Linear Burn" (subtractive) compositing.<br>Unlike 5 (Subtractive), α is not ignored.<br>The neutral color is white. |
| 13 | Photoshop-compatible<br>Multiply | result = blend(dest, dest × src, α) | Performs Photoshop-compatible "Multiply" compositing.<br>Unlike 6 (Multiplicative), α is not ignored.<br>The neutral color is white. |
| 14 | Photoshop-compatible<br>Screen | result = blend(dest, 1.0 - (1.0 - dest) × (1.0 - src), α) | Performs Photoshop-compatible "Screen" compositing.<br>Unlike 10 (Screen), α is not ignored.<br>The neutral color is black. |
| 15 | Photoshop-compatible<br>Overlay | result = blend(dest, overlay(dest, src), α)<br>where overlay(a, b) =<br>a × b × 2.0 (if a < 0.5)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (otherwise) | Performs Photoshop-compatible "Overlay" compositing.<br>The neutral color is 50% gray. |
| 16 | Photoshop-compatible<br>Hard Light | result = blend(dest, hardlight(dest, src), α)<br>where hardlight(a, b) =<br>a × b × 2.0 (if b < 0.5)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (otherwise) | Performs Photoshop-compatible "Hard Light" compositing.<br>The neutral color is 50% gray. |
| 17 | Photoshop-compatible<br>Soft Light | result = blend(dest, softlight(dest, src), α)<br>where softlight(a, b) =<br>a<sup>0.5 ÷ b</sup> (when b ≥ 0.5)<br>a<sup>2.0 × (1.0 - b)</sup> (otherwise) | Performs Photoshop-compatible "Soft Light" compositing.<br>The neutral color is 50% gray. |
| 18 | Photoshop-compatible<br>Color Dodge | result = blend(dest, min(1.0, dest ÷ ( 1.0 - src ) ), α) | Performs Photoshop-compatible "Color Dodge" compositing.<br>Unlike ltDodge, α is not ignored.<br>The neutral color is black. |
| 19 | Photoshop 5.x and earlier compatible<br>Color Dodge | result = min(1.0, dest ÷ ( 1.0 - src × α) ) | Performs "Color Dodge" compositing compatible with Photoshop 5.x and earlier.<br>The formula differs slightly from 18 (Photoshop-compatible Color Dodge).<br>The neutral color is black. |
| 20 | Photoshop-compatible<br>Color Burn | result = blend(dest, max(0.0, 1.0 - (1.0 - dest) ÷ src), α) | Performs Photoshop-compatible "Color Burn" compositing.<br>The neutral color is white. |
| 21 | Photoshop-compatible<br>Lighten | result = blend(dest, max(dest, src), α) | Performs Photoshop-compatible "Lighten" compositing.<br>Unlike 8 (Lighten), α is not ignored.<br>The neutral color is black. |
| 22 | Photoshop-compatible<br>Darken | result = blend(dest, min(dest, src), α) | Performs Photoshop-compatible "Darken" compositing.<br>Unlike 9 (Darken), α is not ignored.<br>The neutral color is white. |
| 23 | Photoshop-compatible<br>Difference | result = blend(dest, abs(dest - src), α) | Performs Photoshop-compatible "Difference" compositing.<br>The neutral color is black. |
| 24 | Photoshop 5.x and earlier compatible<br>Difference | result = abs(dest - src × α) | Performs "Difference" compositing compatible with Photoshop 5.x and earlier.<br>The formula differs slightly from 23 (Photoshop-compatible Difference).<br>The neutral color is black. |
| 25 | Photoshop-compatible<br>Exclusion | result = blend(dest, dest + src - 2.0 × src × dest, α) | Performs Photoshop-compatible "Exclusion" compositing.<br>The neutral color is black. |
