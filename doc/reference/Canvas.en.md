# Canvas

Canvas provides drawing functionality.
When a Window is created, its canvas property is created automatically.
To draw, use the canvas property of that Window.

## Members

### Properties

- [clearColor](#clearcolor)
- [renderTarget](#rendertarget)
- [blendMode](#blendmode)
- [matrix](#matrix)
- [defaultShader](#defaultshader)
- [defaultFillShader](#defaultfillshader)
- [width](#width)
- [height](#height)
- [clipRect](#cliprect)
- [enableClipRect](#enablecliprect)
- [enableCulling](#enableculling)

### Methods

- [clear](#clear)
- [capture](#capture)
- [save](#save)
- [restore](#restore)
- [fill](#fill)
- [drawMesh](#drawmesh)
- [drawMesh](#drawmesh)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTransition](#drawtransition)
- [drawTransition](#drawtransition)
- [drawTextureAtlas](#drawtextureatlas)
- [drawTextureAtlas](#drawtextureatlas)
- [draw9Patch](#draw9patch)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)
- [flush](#flush)
- [drawText](#drawtext)

---

### clearColor

Property \ Access: `r/w`

**Description**

Clear color: the color used to clear the screen before drawing

---

### renderTarget

Property \ Access: `r/w`

**Description**

Render target

An Offscreen object can be specified.
Specify null/void to draw directly.

---

### blendMode

Property \ Access: `r/w`

**Description**

Blend mode for drawing

bmDisable, bmOpaque, bmAlpha, bmAdd, and bmAddWithAlpha can be specified.
If you need a blend method not listed here, write a shader.

---

### matrix

Property \ Access: `r/w`

**Description**

Drawing matrix

(Matrix32 class)

---

### defaultShader

Property \ Access: `r/w`

**Description**

The default shader used to draw textures (the shader used when drawTexture is given a single texture)

It can be set, but there is basically no need to change it.
Assigning void restores the built-in initial default shader.

The a_opacity uniform of the default shader is set to 1.0 when the Canvas is created.
Change `canvas.defaultShader.a_opacity` only when you want to draw semi-transparently.
If your own shader declares a_opacity, the caller must set it
(note that an unset uniform has the GL initial value 0, which is fully transparent).

---

### defaultFillShader

Property \ Access: `r/w`

**Description**

The default shader used by fill

It can be set, but there is basically no need to change it.
Assigning void restores the built-in initial default shader.

---

### width

Property \ Access: `r/w`

**Description**

Width of the drawing area

Normally matches the client area, but there is a brief period (one frame) between a Window resize and the redraw when they differ.

---

### height

Property \ Access: `r/w`

**Description**

Height of the drawing area

Normally matches the client area, but there is a brief period (one frame) between a Window resize and the redraw when they differ.

---

### clipRect

Property \ Access: `r/w`

**Description**

Rect object for the clipping rectangle

Use it as in canvas.clipRect.set( l, t, r, b );.
Enable or disable it with enableClipRect.

---

### enableClipRect

Property \ Access: `r/w`

**Description**

Whether to clip with a rectangle

When true, drawing is clipped by the clipRect property.

---

### enableCulling

Property \ Access: `r/w`

**Description**

Whether to perform face culling

true enables it and false disables it. The default is false.

---

### clear

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `argb` | `int` | `&nbsp;` | Clear color (if omitted, the clearColor property is used). |

**Description**

Clears the whole drawing area

---

### capture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `dest` | `&nbsp;` | `&nbsp;` | The destination Bitmap/Texture/Offscreen. |
| `front` | `bool` | `true` | Whether to capture from the front buffer or the back buffer. true for front, false for back. |

**Description**

Captures the entire current drawing into a Bitmap/Texture/Offscreen

A Bitmap is resized to the screen size.
A Texture/Offscreen is not resized.

---

### save

Method

**Description**

Saves the matrix and clip state (stack)

---

### restore

Method

**Description**

Restores the matrix and clip state (stack)

---

### fill

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | Width of the area to fill. |
| `height` | `int` | `&nbsp;` | Height of the area to fill. |
| `colors` | `&nbsp;` | `0xffffffff` | ARGB vertex colors for the 4 vertices. A single number gives a solid color; an array specifies each of the 4 vertices. |
| `shader` | `&nbsp;` | `null` | Fill shader. If null, defaultFillShader is used. |

**Description**

Fills with a color

The XY position is specified with matrix.

---

### drawMesh

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | A shader with textures and vertex data already associated. |
| `count` | `int` | `&nbsp;` | Number of vertices to draw. |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | Primitive type, such as triangles. |
| `offset` | `int` | `0` | Offset in the vertex array at which to start drawing. |

**Description**

Draws a mesh

The mesh (VertexBinder: vertex data) must be associated with shader (set through its properties) before the call.
Texture information must be associated in the same way.
After the call, clear the information associated with shader (set it to void).

---

### drawMesh

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | A shader with textures and vertex data already associated. |
| `index` | `VertexBinder` | `&nbsp;` | The index buffer. |
| `count` | `int` | `&nbsp;` | Number of indices to draw. |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | Primitive type, such as triangles. |

**Description**

Draws a mesh using an index buffer

The mesh (VertexBinder: vertex data) must be associated with shader (set through its properties) before the call.
Texture information must be associated in the same way.
After the call, clear the information associated with shader (set it to void).

---

### drawTexture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |

**Description**

Draws one texture

Drawn with defaultShader.
Position, scaling, and rotation are specified with matrix.
You can specify an Offscreen object as well as a Texture object.
When you specify an Offscreen, it must not be the current renderTarget (to avoid a cycle).

---

### drawTexture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |
| `shader` | `ShaderProgram` | `&nbsp;` | The shader to use for drawing. |

**Description**

Draws one texture with a specified shader

Position, scaling, and rotation are specified with matrix.
You can specify an Offscreen object as well as a Texture object.
When you specify an Offscreen, it must not be the current renderTarget (to avoid a cycle).

---

### drawTexture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |
| `texture2` | `Texture` | `&nbsp;` | The second texture to use for drawing. |
| `shader` | `ShaderProgram` | `&nbsp;` | The shader to use for drawing. |

**Description**

Draws two textures with a specified shader

Position, scaling, and rotation are specified with matrix.
You can specify an Offscreen object as well as a Texture object.
When you specify an Offscreen, it must not be the current renderTarget (to avoid a cycle).

---

### drawTexture

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |
| `texture2` | `Texture` | `&nbsp;` | The second texture to use for drawing. |
| `texture3` | `Texture` | `&nbsp;` | The third texture to use for drawing. |
| `shader` | `ShaderProgram` | `&nbsp;` | The shader to use for drawing. |

**Description**

Draws three textures with a specified shader

Position, scaling, and rotation are specified with matrix.
You can specify an Offscreen object as well as a Texture object.
When you specify an Offscreen, it must not be the current renderTarget (to avoid a cycle).
OpenGL ES 2.0 allows up to 8 textures, and 3.0 allows up to 16 on the vertex side and 16 on the fragment side, so more could be added, but for now up to 3 are defined.
A future version that takes textures as an array may be added to handle 4 or more.

---

### drawTransition

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | Front texture (shown at phase=0.0). |
| `back` | `Texture` | `&nbsp;` | Back texture (shown at phase=1.0). |
| `phase` | `real` | `&nbsp;` | Progress from 0.0 to 1.0 (values outside the range are clamped). |

**Description**

Draws a crossfade between front and back textures

Draws front blended toward back according to the progress value phase.
The shader is built in, so you do not need to prepare a ShaderProgram.
Position, scaling, and rotation are specified with matrix (the same convention as drawTexture;
blendMode and clipping are also respected).
You can specify an Offscreen object as well as a Texture object.

---

### drawTransition

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | Front texture. |
| `back` | `Texture` | `&nbsp;` | Back texture. |
| `phase` | `real` | `&nbsp;` | Progress from 0.0 to 1.0. |
| `rule` | `Texture` | `&nbsp;` | Rule image texture (tcfAlpha). null for a crossfade. |
| `vague` | `int` | `64` | Boundary blur width (on the rule value scale, 0 to 255). |

**Description**

Draws a universal transition between front and back textures

Pixels with smaller values in the rule image (grayscale) switch to back
sooner. The switching threshold sweeps phase * (1 + vague/255), so
every pixel is back at phase=1.0. The boundary is blurred over a width of vague.

Create the rule texture in tcfAlpha format
(for example, `new Texture("rule.png", tcfAlpha)`). Passing null for rule
makes it behave as a crossfade.

It has the same semantics as, and can use the same rule assets as, the screen-transition effects of Elements dialog flows
(`effect` / `rule` / `vague` in the JSON `transitions`).

---

### drawTextureAtlas

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | The rectangle within the texture to draw. |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |

**Description**

Draws part of a texture

Drawn with defaultShader.

---

### drawTextureAtlas

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | The rectangle within the texture to draw. |
| `texture` | `Texture` | `&nbsp;` | The texture to draw. |
| `shader` | `ShaderProgram` | `&nbsp;` | The shader to use for drawing. |

**Description**

Draws part of a texture (with a shader)

---

### draw9Patch

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `txture` | `Texture` | `&nbsp;` |  |
| `width` | `int` | `&nbsp;` | Width to draw. |
| `height` | `int` | `&nbsp;` | Height to draw. |
| `shader` | `ShaderProgram` | `null` | The shader to use for drawing. Optional. |

**Return value**

The margin information.

**Description**

Draws using 9-patch

The Texture used for drawing must have 9-patch information loaded.
Only Texture objects can be specified.

---

### beginEffect

Method

**Description**

Starts capturing for a post effect

Captures the drawing from here until [endEffect](#endeffect) into an intermediate buffer
(cleared to transparent). Can be nested. If you forget to close it, it is discarded at the end of the frame
and a warning is logged.
For details of the command specification and internal structure, see
[3D Graphics System](../guide/Graphic3DSystem.md).

**See also:** [Canvas.endEffect](Canvas.md#endeffect)

---

### endEffect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `commands` | `null` | An array of processing commands (Dictionaries). If omitted, the capture is composited unchanged. |
| `opacity` | `255` | Opacity when compositing (0 to 255). |

**Description**

Applies a sequence of processing commands to the captured drawing and composites it

Applies commands in order to the drawing since [beginEffect](#begineffect)
and composites the result into the previous drawing target with the current blendMode. The processing completes
entirely on the GPU without reading back to the CPU.

Commands are specified as an array of Dictionaries of the form `%[ cmd:"name", ... ]`:
LUT-based (gamma / adjustGamma / light / lut),
mixing (grayscale / colorize / modulate / noise / generateWhiteNoise /
overcolor), and neighborhood (boxBlur / gaussianBlur).
For the parameters of each command and the fusion rules, see
[3D Graphics System](../guide/Graphic3DSystem.md).

If opacity (0 to 255) is specified, it is multiplied into the alpha of the captured content when compositing (the same as
GLESAdaptor.endEffect in the gles plugin). The result is the same for both OpenGL-based and GPU-based Canvas.

**See also:** [Canvas.beginEffect](Canvas.md#begineffect)

---

### beginMaskClip

Method

**Description**

Starts capturing for a mask clip

Captures the drawing from here until [endMaskClip](#endmaskclip).
An image-based clipping method that is safe to use with any kind of drawing.

**See also:** [Canvas.endMaskClip](Canvas.md#endmaskclip)

---

### endMaskClip

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | The Texture / Offscreen to use as the mask. void composites unchanged. |
| `x` | `int` | `&nbsp;` | X position at which to place the mask. |
| `y` | `int` | `&nbsp;` | Y position at which to place the mask. |

**Description**

Multiplies the captured drawing by the mask alpha and composites it

Multiplies by the alpha of mask and composites into the previous drawing target. Outside the mask
rectangle, alpha=0 (fully clipped). Equivalent to the CPU-side Layer.clipAlphaRect.

**See also:** [Canvas.beginMaskClip](Canvas.md#beginmaskclip)

---

### beginStencilClip

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | The Texture / Offscreen to use as the mask. |
| `x` | `int` | `&nbsp;` | X position at which to place the mask. |
| `y` | `int` | `&nbsp;` | Y position at which to place the mask. |
| `threshold` | `int` | `1` | Alpha threshold (1 to 255). |

**Description**

Starts a stencil clip

Writes the mask alpha into the stencil buffer and clips the drawing until
[endStencilClip](#endstencilclip). A lightweight method for simple texture
drawing (it conflicts with drawing that uses the stencil itself; in that
case use a mask clip).

**See also:** [Canvas.endStencilClip](Canvas.md#endstencilclip)

---

### endStencilClip

Method

**Description**

Ends the stencil clip

**See also:** [Canvas.beginStencilClip](Canvas.md#beginstencilclip)

---

### flush

Method

**Description**

Flushes drawing

Used, for example, when switching the renderTarget whose drawing you want to commit.
Switching renderTarget during onDraw calls flush internally, so an explicit call is not needed.

---

### drawText

Method

**Arguments**

| Arguments | Type | Default | Description |
| --- | --- | --- | --- |
| `font` | `Font` | `&nbsp;` | Font. |
| `x` | `int` | `&nbsp;` | X position. |
| `y` | `int` | `&nbsp;` | Y position. |
| `text` | `string` | `&nbsp;` | Text. |
| `color` | `int` | `&nbsp;` | Color. |

**Description**

Draws text (not implemented)

---
