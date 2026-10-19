# GPUDrawDevice

GPUDrawDevice is a DrawDevice that you register in [Window.drawDevice](Window.md#drawdevice); it runs the [Canvas](Canvas.md) family of classes on the SDL3 GPU API (SDL_GPU). It is an **in-development feature** included only in builds where Canvas runs on SDL_GPU (CMake option `KRKRZ_CANVAS_GPU=ON`; SDL3 build only, mutually exclusive with the OpenGL version).

In such builds this class is the default DrawDevice at startup (`-drawdevice=gpu`; `-drawdevice=sdl` switches back to [SDLDrawDevice](SDLDrawDevice.md); see [command-line options](../guide/CommandLine.md)). The SDL_GPU driver is chosen automatically and can be set explicitly with `-gpudriver` (the Windows default is `vulkan`; `-gpudriver=direct3d12` also works with D3D12, in which case script shaders need a DXIL pack).

In builds without the OpenGL version, this class is also registered under the name `Window.OGLDrawDevice`. Existing scripts that use [OGLDrawDevice](OGLDrawDevice.md) (including `super.OGLDrawDevice()` in derived classes) work with this class as-is.

While this device is active, [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) / [Offscreen](Offscreen.md) / [Matrix32](Matrix32.md) / [VertexBuffer](VertexBuffer.md) / [VertexBinder](VertexBinder.md) work on top of SDL_GPU. The main differences from the OpenGL ES version are:

- Shaders are not compiled at run time; they are looked up in a pre-converted pack (`canvas_shaders.kzgs`). Using a shader that is not in the pack throws an exception (dump them with `-gpushadercollect` and convert them; `-gpushaderpack` specifies the pack)
- drawText is not supported (clipping with masks and stencils (beginMaskClip / beginStencilClip), post effects (beginEffect / endEffect), TextureLayerTreeOwner, and [GLCompositor](GLCompositor.md) are available; overlay movies appear above the Canvas through the same path as [SDLDrawDevice](SDLDrawDevice.md))
- [Texture.nativeHandle](Texture.md#nativehandle) is an SDL_GPU texture rather than a GL texture number
- There are no [matrix](OGLDrawDevice.md#matrix) / [glVideoPresenterHost](OGLDrawDevice.md#glvideopresenterhost) properties

Presentation to the screen works as in [SDLDrawDevice](SDLDrawDevice.md): SDL_Renderer runs on the same GPU device as Canvas, and the screen drawn by Canvas is output to the same rectangle as the primary layer image. The Canvas coordinate system has the same size as the primary layer.

## Members

### Constructors

- [GPUDrawDevice](#gpudrawdevice)

### Properties

- [interface](#interface)
- [window](#window)
- [canvas](#canvas)
- [texture](#texture)
- [sdlVideoPresenterHost](#sdlvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

### Methods

- [recreate](#recreate)
- [createCanvas](#createcanvas)
- [resumeOnDraw](#resumeondraw)

### Events

- [onInit](#oninit)
- [onDone](#ondone)
- [onDraw](#ondraw)

---

### GPUDrawDevice

Constructor

**Description**

Constructs a GPUDrawDevice object

Constructs an object of the GPUDrawDevice class.

When this class is the startup default, an instance of it is already registered in Window.drawDevice, so you do not need to register one yourself. To use Canvas, call [createCanvas](#createcanvas).

---

### interface

Property \ Access: `r`

**Description**

Gets the interface object

Provided so that plugins and the like can use the DrawDevice object.

---

### window

Property \ Access: `r`

**Description**

Gets the associated Window object

Returns the Window object this DrawDevice is set on.

---

### canvas

Property \ Access: `r`

**Description**

Gets the Canvas object used for drawing

Returns the [Canvas](Canvas.md) object managed by this device.
Access it from onDraw and the like to issue drawing commands.

---

### texture

Property \ Access: `r`

**Description**

Gets the primary layer texture

Returns the [Texture](Texture.md) object that holds the primary layer image.
Drawing it to the Canvas in onDraw lets you bring the layer screen into the Canvas drawing.

---

### sdlVideoPresenterHost

Property \ Access: `r`

**Description**

Registration point for the overlay movie presenter (pointer value)

A pointer value to the presenter host that the overlay movie reads in order to composite into this device in a pull model
(the same convention as [SDLDrawDevice.sdlVideoPresenterHost](SDLDrawDevice.md#sdlvideopresenterhost)).
Normally used by the engine internals or plugins.

---

### dialogRendererHost

Property \ Access: `r`

**Description**

Elements dialog renderer host (pointer value)

A pointer value to the host used to obtain the Elements overlay drawing adapter.
Normally used by the engine internals or plugins.

---

### viewportBackgroundHost

Property \ Access: `r`

**Description**

Registration point for filling the viewport margins (pointer value)

A pointer value to the `iTVPViewportBackgroundHost` that receives the margin settings used when the game screen does not cover the whole
drawing area ([Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper)). Normally used by the engine internals or plugins.

---

### recreate

Method

**Description**

Recreates the internal device

Provided for compatibility with [OGLDrawDevice](OGLDrawDevice.md). Does nothing in this class.

---

### createCanvas

Method

**Description**

Creates a Canvas object

Requests creation of a [Canvas](Canvas.md) object bound to this device.
The created Canvas is available from the [canvas](#canvas) property.

If the GPU device is not ready yet, the Canvas is created once it is ready (just before [onInit](#oninit)).

---

### resumeOnDraw

Method

**Description**

Resumes firing onDraw after it was stopped automatically

If the onDraw handler keeps throwing exceptions every frame and reaches the limit for consecutive exceptions
(command-line option `-eventexceptionlimit`, default 10),
onDraw stops firing automatically (the screen display itself continues).
Calling this method resumes firing.

---

### onInit

Event

**Description**

Event called when the GPU device is ready

Fires after this device's drawing target (SDL_Renderer) has been created on the GPU device and Canvas is ready to use (not immediately, but on the next event dispatch, so that an exception inside onInit does not freeze the error display).

Allocate initial resources such as shaders and textures here. In environments where the GPU device is unavailable, it does not fire and Canvas cannot be used (`GPU device is not available` appears in the log).

**See also:** [GPUDrawDevice.onDone](GPUDrawDevice.md#ondone)

---

### onDone

Event

**Description**

Event called before the drawing target is destroyed

Fires just before this device's drawing target is destroyed.

Release the resources allocated in onInit here.

**See also:** [GPUDrawDevice.onInit](GPUDrawDevice.md#oninit)

---

### onDraw

Event

**Description**

Event called when the screen is drawn

Fires on every drawing cycle while a Canvas exists. It is called internally between the Canvas's BeginDrawing and EndDrawing, so you can issue drawing commands through the [canvas](#canvas) property inside the handler.

It does not fire while an overlay movie is playing.

---
