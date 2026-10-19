---
source_hash: 685d3d970094
---

# Layer, Bitmap, and ImageFunction

Kirikiri Z has two classes for handling images, [Layer](../reference/Layer.md) and [Bitmap](../reference/Bitmap.md),
plus [ImageFunction](../reference/ImageFunction.md), a class made up only of methods.
This page explains how the three relate and which one to use when.

## In three lines

- **Layer** is "an image that is displayed". Besides the image buffer, it has a parent-child tree, display position, opacity, input events, and redraw notifications.
- **Bitmap** is "a single image buffer that is not displayed". It can load, save, and access pixels, but **has no drawing methods at all**.
- **ImageFunction** is **a collection of static methods that can be called directly on a Bitmap**, made by stripping the *Layer-specific concerns* (display attributes, clip rectangle, update notifications) from Layer's drawing methods.
  It exists to fill the gap left by Bitmap having no drawing methods.

## Structure

TJS2 sees three classes, but there is only one kind of engine-internal object (`tTVPBaseBitmap`) that actually holds and processes the pixels.
Layer and Bitmap simply wrap it, and the drawing algorithms (Blt / StretchBlt / AffineBlt / fill / text drawing ...) are completely shared.

```text
 TJS2 level
 ┌────────────────────────────────┐   ┌──────────────────────────────┐   ┌───────────────────────┐
 │ Layer                          │   │ Bitmap                       │   │ ImageFunction         │
 │  - parent-child tree/position  │   │  - just one image            │   │  - all methods static │
 │  - visible / opacity / type    │   │  - width / height / buffer   │   │  - no point in        │
 │  - face / holdAlpha / clip*    │   │  - load / loadAsync / save   │   │    creating instances │
 │  - input events / focus        │   │  - getPixel / setPixel       │   │                       │
 │  - many drawing methods        │   │  - no drawing methods of its │   │                       │
 │  - drawing triggers update()   │   │    own                       │   │                       │
 └───────────────┬────────────────┘   └───────────────┬──────────────┘   └───────────┬───────────┘
                 │ MainImage                          │                              │
                 │ ProvinceImage (province image)     │ (just one)                   │ takes a Bitmap
                 ▼                                    ▼                              │ as 1st argument
 C++ level   ┌───────────────────────────────────────────────────────────┐           │
             │ tTVPBaseBitmap                                            │◀──────────┘
             │  the pixel buffer (32bpp / 8bpp, copy-on-write sharing)   │
             │  Blt / StretchBlt / AffineBlt / Fill / DrawText / Blur …  │
             └───────────────────────────────────────────────────────────┘
```

In other words, **ImageFunction is "the Bitmap version of Layer's drawing methods"**.
The processing called internally is exactly the same as the Layer version; the only difference is "who decides the arguments".

## Why Bitmap and ImageFunction are needed

A Layer cannot be created on its own. Its constructor needs a [Window](../reference/Window.md) (or a
[BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md)) and a parent layer,
every drawing operation triggers a redraw-region notification (`update`), and it becomes part of the whole tree's compositing.
That is too heavy for "images you want to process without showing them" — asset preprocessing, caches, screenshot processing, asynchronous loading.

Bitmap is the lightweight container for that: it is created with just `new Bitmap(w, h)` and has nothing to do with display or trees.
However, Bitmap itself has no drawing methods, so ImageFunction is provided as the way to composite, draw text, and apply filters on a Bitmap.

Some features exist only on Bitmap. The main one is **asynchronous image loading** ([Bitmap.loadAsync](../reference/Bitmap.md#loadasync));
Layer has no corresponding method. The usual approach is to load into a Bitmap and then pass it to a Layer with
[Layer.copyFromBitmapToMainImage](../reference/Layer.md#copyfrombitmaptomainimage).

## Method correspondence

| Operation | Layer | ImageFunction (target is a Bitmap) | Bitmap itself |
| --- | --- | --- | --- |
| Rectangle fill | `fillRect` | `fillRect` | — |
| Translucent / mask fill | `colorRect` | `colorRect` | — |
| Text drawing | `drawText` | `drawText` (Font given explicitly) | — |
| Glyph drawing | `drawGlyph` | `drawGlyph` | — |
| Shaped text drawing | `drawShapedText` / `drawShapedTextArea` | **none** | — |
| Vertical text drawing | `drawVerticalTextArea` | **none** | — |
| Rectangle copy | `copyRect` | `operateRect` + `omOpaque` / `dfOpaque` | — |
| Rectangle blend | `operateRect` | `operateRect` | — |
| Scaled copy | `stretchCopy` | `operateStretch` + `omOpaque` / `dfOpaque` | — |
| Scaled blend | `operateStretch` | `operateStretch` | — |
| Affine copy | `affineCopy` | `operateAffine` + `omOpaque` / `dfOpaque` | — |
| Affine blend | `operateAffine` | `operateAffine` | — |
| 9-patch copy | `copy9Patch` | `copy9Patch` | — |
| Box blur | `doBoxBlur` | `doBoxBlur` | — |
| Gamma correction | `adjustGamma` | `adjustGamma` | — |
| Grayscale | `doGrayScale` | `doGrayScale` | — |
| Horizontal / vertical flip | `flipLR` / `flipUD` | `flipLR` / `flipUD` | — |
| Tree composite copy | `piledCopy` | **none** (no concept of child layers) | — |
| Pixel read/write | `getMainPixel` / `setMainPixel` / `getMaskPixel` / `setMaskPixel` | — | `getPixel` / `setPixel` / `getMaskPixel` / `setMaskPixel` |
| Image loading | `loadImages` | — | `load` / `loadAsync` / `loadHeader` |
| Image saving | `saveLayerImage` | — | `save` |
| Unsharing | `independMainImage` | — | `independ` |
| Image resizing | `setImageSize` | — | `setSize` |

!!! note "Why ImageFunction has no copy methods"
    ImageFunction has no dedicated methods corresponding to `copyRect` / `stretchCopy` / `affineCopy`.
    This is because `operate*` with `mode = omOpaque`, `face = dfOpaque`, `hda = false` is already a plain copy (`bmCopy`).
    However, there is no equivalent of the `clear` argument of `affineCopy` (which clears the area outside the transformed region).

## Values Layer uses implicitly are all explicit arguments in ImageFunction

For the same drawing operation, the Layer version builds its arguments from its own properties. Bitmap has none of those properties,
so with ImageFunction the caller passes everything explicitly. **This is where discrepancies tend to appear when porting.**

| What Layer uses implicitly | ImageFunction equivalent |
| --- | --- |
| [Layer.face](../reference/Layer.md#face) | `face` argument (default `dfAlpha`) |
| [Layer.holdAlpha](../reference/Layer.md#holdalpha) | `hda` argument (default `false`) |
| [Layer.clipLeft](../reference/Layer.md#clipleft) and the rest of the clip rectangle | `cliprect` argument (default is **the whole image**; `null` means no clipping) |
| [Layer.font](../reference/Layer.md#font) | The `font` argument of `drawText`. A [Font](../reference/Font.md) object is required (can be created standalone with `new Font()`) |
| Resolution of `omAuto` from the source [Layer.type](../reference/Layer.md#type) | There is nothing to resolve from, so **`omAuto` always falls back to `omAlpha`** |
| Redraw notification via `update()` after drawing | **None** (not needed, since a Bitmap is not displayed) |
| [Layer.imageModified](../reference/Layer.md#imagemodified) | None |

!!! warning "How `omAuto` is handled"
    `omAuto` means "decide the blend method from the `type` property of the source **Layer**".
    Bitmap has no `type`, so in ImageFunction `omAuto` unconditionally becomes `omAlpha`.
    The same happens when you **pass a Bitmap as the source** to `Layer.operateRect` and similar methods
    (`omAuto` is treated as `omAlpha` in that case too). If you want additive or screen blending, specify `mode` explicitly.

## Moving between Layer and Bitmap

### Passing a Bitmap to Layer drawing methods (1.1.0 and later)

The following Layer methods accept **either a Layer or a Bitmap** as the copy / blend source (`src`):

`copyRect` / `copy9Patch` / `operateRect` / `stretchCopy` / `operateStretch` / `affineCopy` / `operateAffine`

When you keep assets as Bitmaps and draw them into a Layer, this is the method with the fewest steps.
Note that `piledCopy` (composite copy including child layers) and `assignImages` are Layer-only and do not accept a Bitmap.

### Layer → Bitmap

```tjs
var bmp = new Bitmap();
layer.copyToBitmapFromMainImage(bmp);   // メイン画像を bmp へ
```

Internally this only sets up **copy-on-write sharing**, so no actual pixel copy happens and it is fast
(the two are separated automatically as soon as either is written to). The 32bpp image including the mask (alpha) is passed as is, but
**the province image is not passed**.

### Bitmap → Layer

```tjs
layer.copyFromBitmapToMainImage(bmp);   // bmp をレイヤのメイン画像に
```

This also uses copy-on-write sharing, but on the Layer side it has these side effects:

- The layer's image size is changed to the Bitmap's size
- The clip rectangle is reset
- `update` runs and the layer is redrawn

If you want to replace only part of the image while keeping the layer's image size,
pass the Bitmap to `copyRect` / `operateRect` instead.

### ImageFunction does not accept a Layer

Every ImageFunction method **accepts only Bitmap objects**. Passing a Layer raises an invalid-argument exception.
To process a Layer's image with ImageFunction, first receive it into a Bitmap with `copyToBitmapFromMainImage`,
then write it back with `copyFromBitmapToMainImage` after processing.

### Getting the composited result of a layer tree as a Bitmap

To build a layer tree without a Window and get its composited result as a Bitmap,
use [BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md).
Pass it as the first argument of the Layer constructor instead of a Window, and the tree's rendered result is available
as a Bitmap from `BitmapLayerTreeOwner.bitmap`.

## Pitfalls

**Nothing is redrawn**
: A Bitmap is not a display element, so drawing into it with ImageFunction changes nothing on screen.
  It becomes visible only after you transfer it to a Layer.

**Copy-on-write sharing**
: `Bitmap.copyFrom` / `assignImages` / `copyToBitmapFromMainImage` and similar only share the actual buffer.
  Normally they are separated automatically right before a write, so you need not think about it, but if you know you will overwrite the whole image,
  passing `false` to [Bitmap.independ](../reference/Bitmap.md#independ) to separate them first avoids a wasted copy.

**Direct buffer access**
: [Bitmap.buffer](../reference/Bitmap.md#buffer) is a read-only pointer; to write, use
  [Bitmap.bufferForWrite](../reference/Bitmap.md#bufferforwrite) (sharing is released as soon as you read it).
  [Bitmap.bufferPitch](../reference/Bitmap.md#bufferpitch) **can be negative** (bottom-up storage).
  Bitmap also has alias properties with the same names as Layer's (`imageWidth` / `imageHeight` / `mainImageBuffer` /
  `mainImageBufferForWrite` / `mainImageBufferPitch`), so plugins and DrawDevices can get images
  without distinguishing between Layer and Bitmap.

**8bpp Bitmaps**
: `new Bitmap(w, h, 8)` creates an 8bpp image, but operations that assume color and alpha
  (the `operate*` family, some uses of `fillRect`, etc.) throw exceptions on 8bpp. 8bpp is intended for province-image-like uses.

**Destroying the alpha channel**
: Arithmetic blends such as multiply, add, and screen do not protect the destination alpha when `hda` (= Layer's `holdAlpha`) is false.
  When blending onto an image with alpha (as with `ltAlpha`), specify `hda = true`.
  Forgetting it leads to symptoms such as the result turning completely black (alpha becoming 0).

**Shaped text drawing is Layer-only**
: The `drawShapedText` / `drawShapedTextArea` / `measureShapedText` family, and the vertical-text
  `drawVerticalTextArea` / `measureVerticalTextArea`, exist only on Layer.
  If you need complex text layout on a Bitmap, draw on a Layer first and then receive the result into a Bitmap.

## Typical patterns

### Composite assets off screen, then pass them to a Layer

```tjs
// 640x480 の作業用 Bitmap を作り、不透明な黒でクリア
var work = new Bitmap(640, 480);
ImageFunction.fillRect(work, 0xff000000);          // isalpha=true なので 0xAARRGGBB

// 背景素材を単純コピー (copyRect 相当)
var bg = new Bitmap("bg.png");
ImageFunction.operateRect(work, 0, 0, bg, null, null, omOpaque, dfOpaque);

// 文字を載せる (Font は明示的に用意する)
var font = new Font();
font.face   = "IPAGothic";
font.height = 24;
ImageFunction.drawText(work, font, 16, 16, "スコア: 1200", 0xffffff);

// できあがった画像をレイヤへ (ここで初めて画面に反映される)
layer.copyFromBitmapToMainImage(work);
```

### Load an image asynchronously and feed it into a layer

```tjs
class AsyncImage extends Bitmap {
    var target;
    function AsyncImage(target) {
        super.Bitmap();
        this.target = target;
    }
    function onLoaded(meta, async, error, message) {
        if (error) { Debug.message("読み込み失敗: " + message); return; }
        if (target !== null && target isvalid) target.copyFromBitmapToMainImage(this);
    }
}

var img = new AsyncImage(layer);
img.loadAsync("bg.png");    // 完了は onLoaded に通知される
```

!!! warning
    While asynchronous loading is in progress, accessing any member other than [Bitmap.loading](../reference/Bitmap.md#loading) raises an exception.
    Also, the target Layer may already be invalidated by the time `onLoaded` is called, so check its validity as in the example above.

### Process a Layer's image and write it back

```tjs
var tmp = new Bitmap();
layer.copyToBitmapFromMainImage(tmp);    // 共有されるだけなので速い
ImageFunction.doGrayScale(tmp);          // ここで初めて実体が分離される
ImageFunction.doBoxBlur(tmp, 4, 4);
layer.copyFromBitmapToMainImage(tmp);    // 書き戻し (update が走る)
```

## See also

- [Layer class reference](../reference/Layer.md)
- [Bitmap class reference](../reference/Bitmap.md)
- [ImageFunction class reference](../reference/ImageFunction.md)
- [BitmapLayerTreeOwner class reference](../reference/BitmapLayerTreeOwner.md)
- [Graphic System](GraphicSystem.md) — meaning of layer types, drawing faces (`df*`), and operation modes (`om*`)
