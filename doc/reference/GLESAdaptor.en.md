# GLESAdaptor

Adapter that holds an OpenGL ES rendering context (EGL-based)

Objects used for drawing are expected to handle the context via EGL.

## Members

### Constructors

- [GLESAdaptor](#glesadaptor)

### Properties

- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [blendMode](#blendmode)

### Methods

- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)
- [capture](#capture)
- [copyLayer](#copylayer)
- [drawLayer](#drawlayer)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [setClipRect](#setcliprect)
- [clearClipRect](#clearcliprect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)

---

### GLESAdaptor

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Target window |

**Description**

Constructor

---

### screenWidth

Property \ Access: `r/w`

**Description**

Screen width

---

### screenHeight

Property \ Access: `r/w`

**Description**

Screen height

---

### blendMode

Property \ Access: `r/w`

**Description**

Blend mode (equivalent to tTVPBlendMode: 0=Disable,1=Opaque,2=Alpha,3=Add,...)

---

### setScreenSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Sets the screen size

---

### makeCurrent

Method

**Description**

Makes the OpenGL context current

---

### capture

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer that receives the result |
| `callback` | `&nbsp;` | Drawing function  function(width, height, param)  Runs in this object's context |
| `param` | `&nbsp;` | Extra parameter |
| `color` | `&nbsp;` | Fill color |

**Description**

Runs OpenGL drawing

---

### copyLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer or GLESTexture |
| `left` | `&nbsp;` | Left position |
| `top` | `&nbsp;` | Top position |

**Description**

Copies a layer

---

### drawLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer or GLESTexture |
| `a` | `&nbsp;` | a component of the affine transformation matrix (2x2) |
| `b` | `&nbsp;` | b component of the affine transformation matrix (2x2) |
| `c` | `&nbsp;` | c component of the affine transformation matrix (2x2) |
| `d` | `&nbsp;` | d component of the affine transformation matrix (2x2) |
| `tx` | `&nbsp;` | Translation X |
| `ty` | `&nbsp;` | Translation Y |
| `opacity` | `&nbsp;` | Opacity 0-255 (255 if omitted) |

**Description**

Draws a layer

---

### beginEffect

Method

**Description**

Starts capturing for an effect

Subsequent drawing goes to an intermediate framebuffer (cleared to transparent).
Always call the matching endEffect().

Drawing enclosed in beginEffect() ... endEffect() is captured into an intermediate buffer,
a sequence of image-processing commands is applied on the GPU, and the result is composited onto the previous render target.
Inside a capture() callback, this lets you apply a separate effect to each module's drawing
(Live2D, drawLayer, etc.). Can be nested.

---

### endEffect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `commands` | `&nbsp;` | Array of processing commands. Each element is a dictionary whose cmd member gives the type<br>and whose other members are parameters. See "Commands" below. |
| `opacity` | `255` | Opacity used when compositing (0-255, 255 if omitted). Multiplied into alpha.<br>Use it to reflect the layer opacity of modules that draw by themselves and do not<br>interpret opacity, such as Live2D.<br>If no processing is needed, pass an empty array as commands to simply<br>capture and composite with opacity. |

**Description**

Applies the effect and composites

Applies commands in order to what has been drawn since the last beginEffect(), then
composites it onto the previous render target using the current blendMode.

Example: [ %[ cmd:"grayscale" ], %[ cmd:"gamma", value:1.2 ] ]

**Commands**

Point operations (consecutive ones are fused into a single pass):

- `%[ cmd:"grayscale" ]` — converts to grayscale Y=(19*B+183*G+54*R)>>8
- `%[ cmd:"gamma", value:r ]` (all channels at once) /
`%[ cmd:"gamma", rgamma:.., rfloor:.., rceil:.., ggamma:.., gfloor:.., gceil:.., bgamma:.., bfloor:.., bceil:.. ]` (per channel)
— gamma correction out = pow(in/255, 1/gamma)*(ceil-floor)+floor
(same as the engine's Layer.adjustGamma; floor defaults to 0 / ceil defaults to 255)
- `%[ cmd:"light", brightness:b, contrast:c ]` — brightness b (-255 to 255) / contrast c (-100 to 100)
- `%[ cmd:"lut", table:[ ...256要素... ] ]` — 256-entry lookup table shared by all channels
- `%[ cmd:"colorize", hue:h, sat:s, blend:b ]` — hue h (0 to 255) / saturation s (0 to 255) / blend ratio b (0 to 1)
- `%[ cmd:"modulate", hue:h, saturation:s, luminance:l ]` — hue h (-180 to 180) / saturation s (-100 to 100) / luminance l (-100 to 100)
- `%[ cmd:"noise", level:n ]` — adds noise n (0 to 255)
- `%[ cmd:"generateWhiteNoise" ]` — generates grayscale white noise (alpha is preserved)
- `%[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ]`
— composites a fill of the given color over the whole image (follows Kirikiri's fillOperateRect).
The upper 8 bits of color (AA) and opacity (0 to 255, default 255) form the compositing alpha.
type is a Kirikiri blend mode value (tTVPBlendOperationMode):
1=Opaque 2=Alpha(default) 3=Additive 4=Subtractive 5=Multiplicative
8=Dodge 9=Darken 10=Lighten 11=Screen 12=AddAlpha
13=PsNormal 14=PsAdditive 15=PsSubtractive 16=PsMultiplicative
17=PsScreen 18=PsOverlay 19=PsHardLight 20=PsSoftLight
21=PsColorDodge 22=PsColorDodge5 23=PsColorBurn
24=PsLighten 25=PsDarken 26=PsDifference 27=PsDifference5 28=PsExclusion

Neighborhood operations (two passes, H/V, via an intermediate buffer):

- `%[ cmd:"boxBlur", area:r, iter:n ]` — uniform blur of radius r, applied n times (iter defaults to 1)
- `%[ cmd:"gaussianBlur", radius:r ]` — Gaussian blur of radius r

Note: noise, the outermost edge of blurs, and colorize are visually equivalent to, but not bit-exact with, the CPU versions.

---

### setClipRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` | Left edge of the clip rectangle (layer coordinates, top-left origin) |
| `top` | `&nbsp;` | Top edge of the clip rectangle (layer coordinates, top-left origin) |
| `width` | `&nbsp;` | Width of the clip rectangle |
| `height` | `&nbsp;` | Height of the clip rectangle |

**Description**

Sets a rectangular clip

Subsequent compositing by drawLayer / endEffect / endMaskClip is limited to the rectangle.
It also affects direct drawing if the drawing module respects the scissor state, but
to clip reliably, wrap the drawing in beginMaskClip/endMaskClip.

**Clipping methods** (equivalent to AffineLayer's clip / clipImage)

- Rectangular clip: setClipRect / clearClipRect. Implemented with scissor.
- Image clip (mask method): drawing enclosed in beginMaskClip() ... endMaskClip() is captured
into an intermediate buffer and composited onto the previous render target while multiplying by the mask image's alpha.
Outside the mask rectangle, alpha is 0 (equivalent to passing 0 as the 8th argument of the CPU Layer.clipAlphaRect).
Safe to use with drawing modules (Live2D, etc.) as well.
- Image clip (stencil method): beginStencilClip() ... endStencilClip().
Writes the mask alpha into the stencil buffer to cut out the drawing. Alpha is binarized by a threshold.
This conflicts with drawing modules that use the stencil themselves, so it is
only for simple texture drawing with drawLayer.

```tjs
// 矩形クリップ (単純テクスチャ描画)
setClipRect(100, 100, 200, 150);
drawLayer(src, 1, 0, 0, 1, 0, 0);
clearClipRect();

// 画像クリップ mask 方式 (モジュール描画にも安全)
beginMaskClip();
drawLayer(src, 1, 0, 0, 1, 0, 0);   // または player.render() 等
endMaskClip(maskTexture, 100, 100);

// 画像クリップ stencil 方式 (drawLayer 専用)
beginStencilClip(maskTexture, 100, 100, 1);
drawLayer(src, 1, 0, 0, 1, 0, 0);
endStencilClip();
```

---

### clearClipRect

Method

**Description**

Clears the rectangular clip

---

### beginMaskClip

Method

**Description**

Starts capturing for a mask clip

Subsequent drawing goes to an intermediate framebuffer (cleared to transparent).
Always call the matching endMaskClip(). Can be nested with beginEffect().

---

### endMaskClip

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mask` | `&nbsp;` | Mask image (GLESTexture or Layer). If void, composites without masking<br>(useful when you only want the rectangular clip to be reliably applied at compositing time) |
| `x` | `&nbsp;` | Mask position X (layer coordinates) |
| `y` | `&nbsp;` | Mask position Y (layer coordinates) |

**Description**

Composites with the mask applied

Multiplies what has been drawn since the last beginMaskClip() by the mask image's alpha
and composites it onto the previous render target using the current blendMode.
Outside the mask rectangle, alpha is 0 (fully clipped).

---

### beginStencilClip

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mask` | `&nbsp;` | Mask image (GLESTexture or Layer) |
| `x` | `&nbsp;` | Mask position X (layer coordinates) |
| `y` | `&nbsp;` | Mask position Y (layer coordinates) |
| `threshold` | `&nbsp;` | Alpha threshold at which clipping takes effect (1-255, required) |

**Description**

Starts a stencil clip

Writes the area where the mask image's alpha is at or above the threshold into the stencil,
and clips subsequent drawLayer calls to that area.

---

### endStencilClip

Method

**Description**

Ends the stencil clip

---
