---
source_hash: ab53ad84abf3
---

# Graphic System

## About the graphic system

Kirikiri displays graphics through a layer mechanism.

Each layer supports transparent overlaying with alpha blending and hierarchical management. Layers also have a mechanism for receiving user input (focus), so they can act as GUI parts (widgets).

Overlaid layers are drawn to a window by a mechanism called a draw device. The draw device can be swapped freely through the [Window.drawDevice](../reference/Window.md#drawdevice) property, and users can define their own effects for specific purposes (as plugins).

The engine has the following built-in draw devices. The default at startup depends on the build (you can choose one with the command-line option `-drawdevice`; see [Command-line options](CommandLine.md) for details).

| Class | Description | Notes |
|---|---|---|
| [BasicDrawDevice](../reference/Window.BasicDrawDevice.md) | Standard drawing with Direct3D 11 | Default for the native Windows (WINVER) build |
| [SDLOGLDrawDevice](../reference/SDLOGLDrawDevice.md) | Direct OpenGL ES drawing | Default for the SDL3 build (when built with OpenGL) |
| [SDLDrawDevice](../reference/SDLDrawDevice.md) | Standard drawing with SDL_Renderer | SDL3 build. Default when built without OpenGL |
| [OGLDrawDevice](../reference/OGLDrawDevice.md) | Full-featured version with OpenGL ES plus GL classes such as [Canvas](../reference/Canvas.md) | Available in both builds |
| [NullDrawDevice](../reference/NullDrawDevice.md) | Does not draw anything | For testing |

The OpenGL devices require an environment where OpenGL ES is available. Also, if the SDL3 build is started with `-drawdevice=sdl`, you cannot switch to an OpenGL device at run time.

Off-screen working images are handled with the [Bitmap](../reference/Bitmap.md) class, and processed with the [ImageFunction](../reference/ImageFunction.md) class. For how the three relate and when to use which, see [Layer, Bitmap, and ImageFunction](LayerAndBitmap.md).

## Supported image formats

In a standard Kirikiri setup, the following formats can be loaded into a layer with [Layer.loadImages](../reference/Layer.md#loadimages) or written from a layer.

- **BMP**  
  The standard Windows bitmap format. A 32 bpp BMP is treated as a bitmap with an alpha channel.
  
  RLE-compressed bitmaps cannot be loaded.
- **PNG**  
  The Portable Network Graphic format can be loaded, including PNG bitmaps with an alpha channel.
- **JPEG**  
  The JPEG format can be loaded. Arithmetic-coded and lossless JPEGs cannot be loaded, but these are rarely seen anyway, so this should not be a problem.
- **TLG5**  
  A lossless compression format specific to Kirikiri, with the extension .tlg. Images with an alpha channel can also be loaded. The compression ratio is not very high, but it decompresses quickly. This format **cannot be used for mask images (_m) or province images (_p)**. It can only handle full-color images with or without an alpha channel.
- **TLG6**  
  A lossless compression format specific to Kirikiri, with the same .tlg extension as TLG5. TLG6 features a high compression ratio. It takes a little less than twice as long to decompress as TLG5, but is still more than twice as fast as PNG, and files are 20 to 40 percent smaller than PNG.
- **Separate main/mask format**  
  In this format, the color image (main) and the alpha channel (mask) are separate images. The mask image's file name is the main image's file name with _m appended (for example, abc_m.jpeg for abc.jpeg).
  
  The main and mask images may be in different formats.

You can also add loadable image formats with Susie plug-ins. A Susie plug-in can be loaded with the [Plugins.link](../reference/Plugins.md#link) method.

When a Susie plug-in hands over a 32bpp bitmap, it is treated as a bitmap with an alpha channel.

## Layer types

Kirikiri layers can be displayed with various blend modes (layer types).

The following blend modes are available; set the [Layer.type](../reference/Layer.md#type) property to one of the layer type constants starting with lt.

In the formulas, *result* is the result, *dest* is the luminance of the destination image, *src* is the luminance of the image being overlaid, and *α* is the per-pixel alpha of the image being overlaid. All values range from 0.0 to 1.0.

For explanation, the following functions are defined here:

- abs(*a*) : the absolute value of *a*
- max(*a*, *b*) : the larger of *a* and *b*
- min(*a*, *b*) : the smaller of *a* and *b*
- blend(*a*, *b*, *r*) = *a* × (1.0 - *r*) + *b* × *r*

- ****ltOpaque** (**ltCoverRect**)**  
  ltOpaque displays without transparency. The whole layer rectangle is always shown fully opaque (as with any layer type, if you lower the opacity with [Layer.opacity](../reference/Layer.md#opacity), that is applied).
  
  
  
  Formula: *result* = *src*
  
  > **Note:**
  > ltCoverRect has the same meaning; it is the old name used before 2.23 beta 2.
- ****ltAlpha** (**ltTransparent**)**  
  ltAlpha performs alpha blending. It is the most basic type for transparency. The formula below is also used for alpha channel input from BMP files and Susie plug-ins.
  
  
  
  Formula: *result* = blend(*dest*, *src*, *α*)
  
  > **Note:**
  > ltTransparent has the same meaning; it is the old name used before 2.23 beta 2.
- ****ltAddAlpha****  
  ltAddAlpha performs additive alpha blending.
  
  Images suited to this format can be output with the [image format converter](TPC.md). You can also convert from ltAlpha to this format with the [Layer.convertType](../reference/Layer.md#converttype) method.
  
  An ltAddAlpha layer does not display correctly when it is a direct child of an ltAlpha layer.
  
  
  
  Formula: *result* = min(1.0, *dest* × ( 1.0 - *α* ) + *src*)
- ****ltAdditive****  
  ltAdditive performs additive blending. It is suited to expressing glow. It corresponds to Photoshop's "Linear Dodge"; if you want the same effect as Photoshop, use ltPsAdditive, described below. Unlike ltPsAdditive, ltAdditive ignores *α*.
  
  The neutral color (the color that causes no change when overlaid) is black.
  
  
  
  Formula: *result* = min(1.0, *dest* + *src*)
- ****ltSubtractive****  
  ltSubtractive performs subtractive blending. *α* is ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = max(0.0, *dest* + *src* - 1.0)
  
  > **Note:**
  > The only difference from *result* = *dest* - *src* is whether src is inverted.
- ****ltMultiplicative****  
  ltMultiplicative performs multiplicative blending. *α* is ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = *dest* × *src*
- ****ltDodge****  
  ltDodge performs "dodge" blending. It is suited to expressing objects lit by light. *α* is ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = min(1.0, *dest* ÷ ( 1.0 -  *src* ) )
- ****ltLighten****  
  ltLighten performs "Lighten" blending. *α* is ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = max(*dest*, *src*)
- ****ltDarken****  
  ltDarken performs "Darken" blending. *α* is ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = min(*dest*, *src*)
- ****ltScreen****  
  ltScreen performs "Screen" blending. *α* is ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = 1.0 - ( 1.0 - *dest* ) × ( 1.0 - *src* )
- ****ltPsNormal****  
  ltPsNormal has the same effect as ltAlpha. For historical reasons it uses a separate routine and name from ltAlpha.
- ****ltPsAdditive****  
  ltPsAdditive performs Photoshop-compatible "Linear Dodge" blending (additive blending). Unlike ltAdditive, *α* is not ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*, min(1.0, *dest* + *src*), *α*)
- ****ltPsSubtractive****  
  ltPsSubtractive performs Photoshop-compatible "Linear Burn" blending (subtractive blending). Unlike ltSubtractive, *α* is not ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = blend(*dest*, max(0.0, *dest* + *src* - 1.0), *α*)
- ****ltPsMultiplicative****  
  ltPsMultiplicative performs Photoshop-compatible "Multiply" blending. Unlike ltMultiplicative, *α* is not ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = blend(*dest*, *dest* × *src*, *α*)
- ****ltPsScreen****  
  ltPsScreen performs Photoshop-compatible "Screen" blending. Unlike ltScreen, *α* is not ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*, 1.0 - (1.0 - *dest*) × (1.0 - *src*), *α*)
- ****ltPsOverlay****  
  ltPsOverlay performs Photoshop-compatible "Overlay" blending.
  
  The neutral color is 50% gray.
  
  
  
  Formula: *result* = blend(*dest*, overlay(*dest*, *src*), *α*)
  
  where overlay(*a*, *b*) =
  
  *a* × *b* × 2.0  (when *a* < 0.5)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (otherwise)
- ****ltPsHardLight****  
  ltPsHardLight performs Photoshop-compatible "Hard Light" blending.
  
  The neutral color is 50% gray.
  
  
  
  Formula: *result* = blend(*dest*, hardlight(*dest*, *src*), *α*)
  
  where hardlight(*a*, *b*) =
  
  *a* × *b* × 2.0  (when *b* < 0.5)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (otherwise)
- ****ltPsSoftLight****  
  ltPsSoftLight performs Photoshop-compatible "Soft Light" blending.
  
  The neutral color is 50% gray.
  
  
  
  Formula: *result* = blend(*dest*, softlight(*dest*, *src*), *α*)
  
  where softlight(*a*, *b*) =
  
  *a*<sup>0.5 ÷ *b*</sup>  (when *b* ≥ 0.5)
  
  *a*<sup>(1.0 - *b*) × 2</sup>  (otherwise)
- ****ltPsColorDodge****  
  ltPsColorDodge performs Photoshop-compatible "Color Dodge" blending. Unlike ltDodge, *α* is not ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*, min(1.0, *dest* ÷ ( 1.0 -  *src* ) ), *α*)
- ****ltPsColorDodge5****  
  ltPsColorDodge5 performs "Color Dodge" blending compatible with Photoshop 5.x and earlier. Its formula differs slightly from ltPsColorDodge.
  
  The neutral color is black.
  
  
  
  Formula: *result* = min(1.0, *dest* ÷ ( 1.0 - *src* × *α*) )
- ****ltPsColorBurn****  
  ltPsColorBurn performs Photoshop-compatible "Color Burn" blending.
  
  The neutral color is white.
  
  
  
  Formula: *result* = blend(*dest*, max(0.0, 1.0 - (1.0 - *dest*) ÷ *src*), *α*)
- ****ltPsLighten****  
  ltPsLighten performs Photoshop-compatible "Lighten" blending. Unlike ltLighten, *α* is not ignored.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*, max(*dest*, *src*), *α*)
- ****ltPsDarken****  
  ltPsDarken performs Photoshop-compatible "Darken" blending. Unlike ltDarken, *α* is not ignored.
  
  The neutral color is white.
  
  
  
  Formula: *result* = blend(*dest*, min(*dest*, *src*), *α*)
- ****ltPsDifference****  
  ltPsDifference performs Photoshop-compatible "Difference" blending.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*, abs(*dest* - *src*), *α*)
- ****ltPsDifference5****  
  ltPsDifference5 performs "Difference" blending compatible with Photoshop 5.x and earlier. Its formula differs slightly from ltPsDifference.
  
  The neutral color is black.
  
  
  
  Formula: *result* = abs(*dest* - *src* × *α*)
- ****ltPsExclusion****  
  ltPsExclusion performs Photoshop-compatible "Exclusion" blending.
  
  The neutral color is black.
  
  
  
  Formula: *result* = blend(*dest*,  *dest* + *src* - 2.0 × *src* × *dest*, *α*)

## Alpha blending and additive alpha blending

Kirikiri has two alpha blending modes.

- **Alpha blending**  
  Setting the [Layer.type](../reference/Layer.md#type) property to **ltAlpha** selects this display type.
  
  ltAlpha is the alpha blending mode used by most graphics software. It is the right choice when loading data output by other graphics software as is.
- **Additive alpha blending**  
  Setting the [Layer.type](../reference/Layer.md#type) property to **ltAddAlpha** selects this display type.
  
  Compared with alpha blending, this format has the following advantages and disadvantages:
  
  - The formula is simpler than alpha blending, so display is faster, and many drawing methods can also draw faster
  - It can express additive blending together with alpha blending
  - Almost no graphics software supports this format
  
  Since few graphics programs support the same blend mode as ltAddAlpha, to use another program's output in this format in Kirikiri, you need to output images of this type with the [image format converter](TPC.md), or convert from ltAlpha with the [Layer.convertType](../reference/Layer.md#converttype) method.
  
  The image format converter accepts Photoshop-format input that combines "Normal" layers and "Linear Dodge" layers as input for additive alpha blending images.

## Layer types, drawing faces, and operation modes

Kirikiri has layer types (specified with constants starting with lt), drawing faces (specified with constants starting with df), and operation modes (specified with constants starting with om).

They have similar names, but their uses differ as follows:

- **Layer type**  
  The layer type is the value set in the [Layer.type](../reference/Layer.md#type) property, and specifies how the layer is displayed.
- **Drawing face**  
  The drawing face is the value set in the [Layer.face](../reference/Layer.md#face) property, and specifies how drawing into the layer is done. With dfAuto, an appropriate drawing face is chosen according to the layer type. You can also draw with a drawing face different from the one best suited to the layer type.
  
  For methods that copy between layers, such as [Layer.copyRect](../reference/Layer.md#copyrect), it also selects which information is copied. With dfBoth (or dfAlpha or dfAddAlpha), both main and mask are copied. With dfMain (or dfOpaque), only the main image is copied. With dfMask only the mask, and with dfProvince only the province image, is copied.
  
  Likewise, for the [Layer.fillRect](../reference/Layer.md#fillrect) method, it selects which information is filled. With dfBoth (or dfAlpha or dfAddAlpha), both main and mask are filled. With dfMain (or dfOpaque), only the main image is filled. With dfMask only the mask, and with dfProvince only the province image, is filled.
- **Operation mode**  
  The operation mode is a value passed as an argument to methods such as [Layer.operateRect](../reference/Layer.md#operaterect), and specifies how the source (the layer being overlaid) is treated. With omAuto, an appropriate mode is chosen according to the source's layer type.

## Protecting the alpha channel

When the drawing face set in the [Layer.face](../reference/Layer.md#face) property is **dfOpaque**, the [Layer.holdAlpha](../reference/Layer.md#holdalpha) property specifies whether to protect the alpha channel of the destination (the layer on which the method is executed).

When the alpha channel is protected, the alpha channel (opacity) is preserved, and transparent areas stay transparent.

When it is not protected, the alpha channel (opacity) is destroyed. "Destroyed" means its resulting state is undefined.

However, if the [Layer.type](../reference/Layer.md#type) property is neither **ltAlpha** nor **ltAddAlpha**, the layer's alpha channel is not used, so setting Layer.holdAlpha to false usually causes no problem. Setting it to false also lets many methods draw faster than when it is true.
