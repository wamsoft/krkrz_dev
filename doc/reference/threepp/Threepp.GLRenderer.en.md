# Threepp.GLRenderer

OpenGL renderer

The renderer used to render scenes.

## Members

### Constructors

- [GLRenderer](#glrenderer)
- [GLRenderer](#glrenderer)

### Properties

- [autoClear](#autoclear)
- [autoClearColor](#autoclearcolor)
- [autoClearDepth](#autocleardepth)
- [autoClearStencil](#autoclearstencil)
- [sortObjects](#sortobjects)
- [useLegacyLights](#uselegacylights)
- [toneMappingExposure](#tonemappingexposure)

### Methods

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [render](#render)
- [setClearColor](#setclearcolor)
- [setPixelRatio](#setpixelratio)
- [setSize](#setsize)
- [setSampleCount](#setsamplecount)
- [setScissorTest](#setscissortest)
- [setShadowMapEnabled](#setshadowmapenabled)
- [setShadowMapType](#setshadowmaptype)
- [setShadowMapAutoUpdate](#setshadowmapautoupdate)
- [setShadowMapNeedsUpdate](#setshadowmapneedsupdate)
- [clear](#clear)
- [clearColor](#clearcolor)
- [clearDepth](#cleardepth)
- [clearStencil](#clearstencil)
- [dispose](#dispose)
- [resetState](#resetstate)

---

### GLRenderer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `adaptor` | `&nbsp;` | GL context provider (has GLGetProcAddress). |
| `width` | `800` | Rendering width. |
| `height` | `600` | Rendering height. |

**Description**

Constructor

A renderer (device) that draws into a GL context prepared by the host.
Pass the host's GL context provider (an object with a GLGetProcAddress property, such as GLESAdaptor from the gles plugin) as the first argument; the renderer obtains the function pointers (getProcAddress) from it and initializes glad.
This is the same wiring as the Device of the effekseer / motion plugins.

---

### GLRenderer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `800` |  |
| `height` | `600` |  |

**Description**

Constructor (legacy form)

Use this form when the caller has already made the GL context current and initialized glad. Creates the renderer headless.

---

### autoClear

Property \ Access: `r/w`

**Description**

Whether to clear automatically

---

### autoClearColor

Property \ Access: `r/w`

**Description**

Whether to clear the color buffer automatically

---

### autoClearDepth

Property \ Access: `r/w`

**Description**

Whether to clear the depth buffer automatically

---

### autoClearStencil

Property \ Access: `r/w`

**Description**

Whether to clear the stencil buffer automatically

---

### sortObjects

Property \ Access: `r/w`

**Description**

Whether to sort objects

---

### useLegacyLights

Property \ Access: `r/w`

**Description**

Legacy lighting (true) or physically correct lighting (false, default)

---

### toneMappingExposure

Property \ Access: `r/w`

**Description**

Tone mapping exposure

---

### onBeginScene

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Surface width. |
| `height` | `&nbsp;` | Surface height. |

**Description**

Begins drawing a frame (call while the host GL context is current)

Invalidates the internal state cache and sets the drawing size.
Call it inside the adaptor.capture() callback, before render().

---

### onEndScene

Method

**Description**

Ends drawing a frame

Call it after render(). It currently does nothing special, but the call site is reserved for keeping the GL state consistent with the host.

---

### render

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `scene` | `&nbsp;` | Scene. |
| `camera` | `&nbsp;` | Camera. |

**Description**

Renders a scene

---

### setClearColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | Color (0xRRGGBB). |
| `alpha` | `1` | Alpha value. |

**Description**

Sets the clear color

---

### setPixelRatio

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ratio` | `&nbsp;` |  |

**Description**

Sets the pixel ratio

---

### setSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Sets the size

---

### setSampleCount

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `count` | `&nbsp;` | 0/1 = disabled; 2/4/8 etc. Default 4. onBeginScene draws into an internal multisample FBO, and onEndScene resolves it and transfers the result to the host FBO. This reduces jagged edges.<br>If the premultiplied alpha at the edges is a concern, correct it on the host side (GLESAdaptor.unpremultiply). |

**Description**

Sets the number of MSAA (multisample anti-aliasing) samples

---

### setScissorTest

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**Description**

Enables or disables the scissor test

---

### setShadowMapEnabled

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**Description**

Enables or disables shadows (ShadowMap)

true enables shadow map rendering. In addition, the shadow-casting light needs castShadow=true, the receiving meshes need receiveShadow=true, and the shadow-casting meshes need castShadow=true. This also works on the GLES/captured FBO path (depth is rendered into a shadow FBO, and the original render target is restored for the main pass).
Example:
renderer.setShadowMapEnabled(true);
var dir = new Threepp.DirectionalLight(0xffffff, 2.0);
dir.setPosition(3, 5, 2); dir.castShadow = true;
dir.setShadowOrthoBounds(-6, 6, 6, -6); dir.setShadowNearFar(0.5, 30);
scene.add(dir);
floor.receiveShadow = true; box.castShadow = true;

---

### setShadowMapType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `type` | `&nbsp;` |  |

**Description**

0=Basic, 1=PCF (default), 2=PCFSoft, 3=equivalent to VSM

---

### setShadowMapAutoUpdate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**Description**

Updates shadows every frame (default true)

---

### setShadowMapNeedsUpdate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**Description**

Updates shadows once when autoUpdate=false

---

### clear

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `true` |  |
| `depth` | `true` |  |
| `stencil` | `true` |  |

**Description**

Clears the buffers

---

### clearColor

Method

**Description**

Clears the color buffer

---

### clearDepth

Method

**Description**

Clears the depth buffer

---

### clearStencil

Method

**Description**

Clears the stencil buffer

---

### dispose

Method

**Description**

Releases resources

---

### resetState

Method

**Description**

Resets the state

---
