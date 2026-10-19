---
source_hash: 6146398207fe
---

# 3D Graphic System

## Overview

In addition to the regular layer drawing (BasicDrawDevice / SDLDrawDevice) described in [Graphic System](GraphicSystem.md), Kirikiri Z has a GPU drawing path based on OpenGL ES. This path is built around [OGLDrawDevice](../reference/OGLDrawDevice.md) together with classes such as [Canvas](../reference/Canvas.md) / [Texture](../reference/Texture.md) / [ShaderProgram](../reference/ShaderProgram.md) / [Offscreen](../reference/Offscreen.md), and lets you handle texture drawing, shader processing, transitions, and so on directly on the GPU.

These GL classes work only while [OGLDrawDevice](../reference/OGLDrawDevice.md) is active (set on a window). They are tied to the OpenGL context managed by OGLDrawDevice, so they cannot be used while a regular layer draw device (BasicDrawDevice / SDLDrawDevice) is in use.

## SDL_GPU build (in development)

For environments without OpenGL, there is a build that runs the same classes on the SDL3 GPU API (SDL_GPU) (CMake option `KRKRZ_CANVAS_GPU=ON`; SDL3 builds only, mutually exclusive with the OpenGL version). The class names and APIs are the same as the OpenGL ES version, and the draw device is [GPUDrawDevice](../reference/GPUDrawDevice.md) (in this build it is also available under the name `OGLDrawDevice`, so scripts work unchanged). The differences are:

- Shaders are not compiled at run time; they are looked up in a pre-converted pack (`canvas_shaders.kzgs`). Using a shader that is not in the pack raises an exception (dump them with the command-line option [-gpushadercollect](CommandLine.md) and convert them)
- drawText is not supported (clipping with masks/stencils (beginMaskClip / beginStencilClip), post effects (beginEffect / endEffect), TextureLayerTreeOwner, and GLCompositor are available. Overlay movies appear on top of the Canvas through the same path as SDLDrawDevice)
- `Texture.nativeHandle` is an SDL_GPU texture rather than a GL texture name

Details of the current status are in `doc/CanvasGPU.md` in the engine source.

## Switching to OGLDrawDevice

To use GPU drawing, switch the draw device by setting an [OGLDrawDevice](../reference/OGLDrawDevice.md) to the [Window.drawDevice](../reference/Window.md#drawdevice) property.

```tjs
var dev = new OGLDrawDevice();
window.drawDevice = dev;
```

Right after an OGLDrawDevice is constructed, no OpenGL context exists yet. The internal OpenGL ES context is created and initialized lazily when the device is set to `Window.drawDevice`. This initialization and the subsequent drawing cycle are handled through the following events.

| Event | When it fires | Purpose |
|---|---|---|
| [onInit](../reference/OGLDrawDevice.md#oninit) | Right after the GL context is created and initialized | Allocate initial resources such as shaders and textures |
| [onDraw](../reference/OGLDrawDevice.md#ondraw) | Every drawing cycle | Issue the frame's drawing commands |
| [onDone](../reference/OGLDrawDevice.md#ondone) | Right before the device is detached / the context is destroyed | Release resources allocated in onInit |

## Drawing in onDraw

Per-frame drawing happens in the [onDraw](../reference/OGLDrawDevice.md#ondraw) event. When OGLDrawDevice manages a [Canvas](../reference/Canvas.md), onDraw is called internally between the Canvas's BeginDrawing and EndDrawing. So inside the handler you can issue drawing commands such as drawTexture directly through the device's [canvas](../reference/OGLDrawDevice.md#canvas) property (you do not need to call BeginDrawing / EndDrawing yourself).

```tjs
class MyGLDevice extends OGLDrawDevice {
    var tex;
    function onInit() {
        tex = new Texture("image.png");   // 初期リソース確保
    }
    function onDraw() {
        canvas.drawTexture(tex);          // BeginDrawing〜EndDrawing の内側
    }
    function onDone() {
        if (tex !== void) invalidate tex; // リソース解放
        tex = void;
    }
}
```

Placement and transformation are controlled by the Canvas `matrix` ([Matrix32](../reference/Canvas.md) family), and the compositing method by `blendMode`.

## Post effects / clipping

[Canvas](../reference/Canvas.md) drawing can have post effects (color adjustment, blur, etc.) and image clipping applied entirely on the GPU. Processing completes on the GPU without reading back to the CPU, and works only while [OGLDrawDevice](../reference/OGLDrawDevice.md) is active.

### Post effects

```tjs
canvas.beginEffect();
    canvas.drawTexture(tex);        // 捕捉対象 (何を描いてもよい)
canvas.endEffect([
    %[ cmd:"grayscale" ],
    %[ cmd:"gamma", value:1.3 ],
]);
```

Drawing enclosed in `beginEffect()` ... `endEffect(commands)` is captured into an intermediate buffer (cleared to transparent), `commands` (an array of processing commands) is applied in order, and the result is composited onto the previous render target with the current `blendMode`. These can be nested. If `commands` is omitted, the capture is composited as is.

Processing commands fall broadly into point operations (each pixel processed independently; consecutive ones are fused into one pass internally) and neighborhood operations (blurs that refer to surrounding pixels).

```
Point operations (consecutive ones are fused into one pass):
  %[ cmd:"grayscale" ]
      Grayscale  Y = (19*B + 183*G + 54*R) >> 8

  %[ cmd:"gamma", value:γ ]                         // all channels at once
  %[ cmd:"gamma", rgamma:.., rfloor:.., rceil:..,
                  ggamma:.., gfloor:.., gceil:..,
                  bgamma:.., bfloor:.., bceil:.. ]   // per channel
      Gamma correction  out = pow(in/255, 1/γ)*(ceil-floor)+floor
      (follows the engine's Layer.adjustGamma; floor defaults to 0 / ceil to 255)

  %[ cmd:"light", brightness:b, contrast:c ]
      Brightness b (-255 to 255) / contrast c (-100 to 100)

  %[ cmd:"lut", table:[ ...256 elements... ] ]
      256-entry lookup table shared by all channels

  %[ cmd:"colorize", hue:h, sat:s, blend:b ]
      Hue h (0 to 255) / saturation s (0 to 255) / blend ratio b (0 to 1)

  %[ cmd:"modulate", hue:h, saturation:s, luminance:l ]
      Hue h (-180 to 180) / saturation s (-100 to 100) / luminance l (-100 to 100)

  %[ cmd:"noise", level:n ]
      Adds noise n (0 to 255)

  %[ cmd:"generateWhiteNoise" ]
      Generates grayscale white noise (alpha is kept)

  %[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ]
      Fills the whole area with the given color and composites it (follows Kirikiri's fillOperateRect).
      Compositing alpha is the top 8 bits of color (AA) x opacity (0 to 255, default 255).
      type is a Kirikiri blend mode value (tTVPBlendOperationMode).

Neighborhood operations (two passes, H and V, through an intermediate buffer):
  %[ cmd:"boxBlur", area:r, iter:n ]
      Uniform blur of radius r, applied n times (iter defaults to 1)

  %[ cmd:"gaussianBlur", radius:r ]
      Gaussian blur of radius r
```

Each operation is matched to the results of the Kirikiri engine (`TVPDoGrayScale` / `TVPAdjustGamma`) and the layerExImage plugin, but the following cannot match exactly by nature and aim for visual equivalence:

- `noise` / `generateWhiteNoise` — the CPU `rand()` sequence cannot be reproduced, so a coordinate hash is used instead
- The outermost edge of `boxBlur` / `gaussianBlur` — the CPU renormalizes weights at the edge, while the GPU uses `CLAMP_TO_EDGE`
- `colorize` — the CPU rounds HSL with integers, the GPU uses a floating-point version of the same algorithm

### Clipping

Rectangular clipping uses the existing `canvas.clipRect` (Rect) + `canvas.enableClipRect` as is. The scissor is also applied when compositing effects / masks.

Clipping by an image (arbitrary shape) comes in two flavors.

```tjs
// mask 方式 (どんな描画にも安全)
canvas.beginMaskClip();
    canvas.drawTexture(src);
canvas.endMaskClip(maskTex, 100, 100);   // mask の α を乗算、矩形外は α=0
                                          // mask に void で素通し合成

// stencil 方式 (単純テクスチャ描画専用)
canvas.beginStencilClip(maskTex, 100, 100, 1);  // α 閾値 1〜255
    canvas.drawTexture(src);
canvas.endStencilClip();
```

- `endMaskClip(mask, x, y)` — mask is a [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md). This is equivalent to the CPU `Layer.clipAlphaRect` with 0 as the eighth argument (everything outside the mask rectangle is fully clipped).
- `beginStencilClip` writes the mask alpha into the stencil buffer to cut out the drawing. It conflicts with drawing that uses the stencil itself; in that case use the mask method.

### Notes

- Shaders are GLSL ES 3.00. In a GLES2 fallback environment (EGL 2.0 context), effects fail to compile and pass through unchanged (this is logged). Mask / stencil clipping uses ES2 shaders, so it works.
- A `beginEffect` / `beginMaskClip` left unclosed is discarded at EndDrawing (end of frame) with a warning log.
- The `a_opacity` uniform of the Canvas default shader defaults to 1.0 (set when the Canvas is created). Change `canvas.defaultShader.a_opacity` only when you want translucency. If your own shader declares `a_opacity`, you still need to set it yourself as before (an unset uniform has the GL initial value 0 = fully transparent).

## Transition drawing (drawTransition)

A built-in Canvas feature that composites and draws two textures, front and back, according to the progress `phase`. It provides crossfades and universal transitions with a rule image, using built-in shaders. Transitions previously implemented in the TJS layer by building your own [ShaderProgram](../reference/ShaderProgram.md) can be replaced by a single method.

```tjs
// クロスフェード
canvas.drawTransition(front, back, phase);

// ユニバーサルトランジション (rule 画像)
canvas.drawTransition(front, back, phase, ruleTex);        // vague 既定 64
canvas.drawTransition(front, back, phase, ruleTex, 128);   // vague 指定
```

| Argument | Meaning |
|---|---|
| `front` / `back` | [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md). phase=0 shows only front, 1 only back |
| `phase` | Progress from 0.0 to 1.0 (out-of-range values are clamped) |
| `rule` | Rule image texture. **Create it with `tcfAlpha`** (`new Texture("rule.png", tcfAlpha)`). Pixels with smaller values switch to back earlier. Omitted / null gives a crossfade |
| `vague` | Width of the blurred boundary (on the rule value scale 0 to 255, default 64) |

- Placement, transformation, and blending follow the same rules as `drawTexture` (`canvas.matrix` / `blendMode` / clipping).
- The universal threshold sweeps `phase * (1 + vague/255)` (at phase=1 every pixel is always back). The semantics are the same as the flow screen-switch effects of [dialogs](ElementsDialog.md) (`effect` / `rule` / `vague` in the JSON `transitions`), so the same rule assets can be used.
- The built-in shaders are created lazily on first use and cached. The `a_opacity` uniform (default 1.0) applies an overall opacity.

### Example (screen transition)

```tjs
// onDraw 内: old / cur は Offscreen (旧画面と新画面をそれぞれ描いたもの)
var t = (System.getTickCount() - startTick) / duration;
if (t < 1.0) {
    canvas.drawTransition(oldScreen, curScreen, t, ruleTex, 64);
} else {
    canvas.drawTexture(curScreen);
}
```

## See also

- [ShaderProgram / detailed shader guide (multi_platform_design)](https://krkrz.github.io/multi_platform_design/shader_program.html) — how to write shader programs and design details
- [OGLDrawDevice](../reference/OGLDrawDevice.md) — OpenGL ES draw device
- [Canvas](../reference/Canvas.md) — the entry point for drawing commands
- [ShaderProgram](../reference/ShaderProgram.md) — shader programs
- [Texture](../reference/Texture.md) — GPU textures
- [Offscreen](../reference/Offscreen.md) — offscreen render targets
