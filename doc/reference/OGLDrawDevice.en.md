# OGLDrawDevice

OGLDrawDevice is a DrawDevice that you register in [Window.drawDevice](Window.md#drawdevice); it provides drawing with OpenGL ES (glad / ANGLE / EGL).

It is not the default DrawDevice at startup. The internal OpenGL context is created when a TJS script explicitly sets it in Window.drawDevice, and from then on all drawing goes through the GL path. You can also select this device from startup with the command-line option `-drawdevice=ogl` ([command-line options](../guide/CommandLine.md)).

It requires an environment where OpenGL ES is available. The WINVER build always goes through EGL (ANGLE's `libEGL.dll` / `libGLESv2.dll`), so these DLLs must be shipped with it. The SDL3 build prefers the ES profile of the OS OpenGL driver and falls back to the same ANGLE DLLs when it is unavailable (`-forceegl` forces EGL). If the SDL3 build is started with `-drawdevice=sdl`, you cannot switch to this device at run time.

In builds where Canvas runs on the SDL3 GPU API (SDL_GPU) (under development), [GPUDrawDevice](GPUDrawDevice.md) is also registered under the name `OGLDrawDevice` in place of this class.

The TJS classes [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) / [Offscreen](Offscreen.md) / [Matrix32](Matrix32.md) / [VertexBuffer](VertexBuffer.md) / [VertexBinder](VertexBinder.md) work only while this device is active.

## Members

### Constructors

- [OGLDrawDevice](#ogldrawdevice)

### Properties

- [interface](#interface)
- [window](#window)
- [canvas](#canvas)
- [texture](#texture)
- [matrix](#matrix)
- [glVideoPresenterHost](#glvideopresenterhost)
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

### OGLDrawDevice

Constructor

**Description**

Constructs an OGLDrawDevice object

Constructs an object of the OGLDrawDevice class.

The OpenGL context is not created right after construction. It is initialized when the device is set in Window.drawDevice.

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

Gets the texture object

Returns the [Texture](Texture.md) object managed by this device.

---

### matrix

Property \ Access: `r`

**Description**

Gets the matrix object

Returns the [Matrix32](Matrix32.md) object managed by this device.
Used for coordinate transformation when drawing.

---

### glVideoPresenterHost

Property \ Access: `r`

**Description**

Registration point for the overlay movie presenter (pointer value)

A pointer value to the presenter host that the overlay movie reads in order to composite into this GL device in a pull model
(the same convention as [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) in WINVER /
[sdlVideoPresenterHost](SDLDrawDevice.md#sdlvideopresenterhost) in SDL).
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
[Window.setViewportWallpaper](Window.md#setviewportwallpaper)). Window applies the margin settings only when this property
is nonzero (with a draw device that lacks this property, the margins cannot be filled separately
and keep that device's default fill). Normally used by the engine internals or plugins.

---

### recreate

Method

**Description**

Recreates the internal device

Recreates the internal device.

You normally do not need to call this.

---

### createCanvas

Method

**Description**

Creates a Canvas object

Requests creation of a [Canvas](Canvas.md) object bound to this device.
The created Canvas is available from the [canvas](#canvas) property.

---

### resumeOnDraw

Method

**Description**

Resumes firing onDraw after it was stopped automatically

If the onDraw handler keeps throwing exceptions every frame and reaches the limit for consecutive exceptions
(command-line option `-eventexceptionlimit`, default 10),
onDraw stops firing automatically (the drawing cycle itself, such as clearing the screen, continues).
Calling this method resumes firing.

---

### onInit

Event

**Description**

Event called when the GL context is initialized

Fires right after this device is set in Window.drawDevice and the internal OpenGL ES context has been created and initialized.

Allocate initial resources such as shaders and textures here.

**See also:** [OGLDrawDevice.onDone](OGLDrawDevice.md#ondone)

---

### onDone

Event

**Description**

Event called before the GL context is destroyed

Fires just before this device is detached or the context is destroyed.

Release the resources allocated in onInit here.

**See also:** [OGLDrawDevice.onInit](OGLDrawDevice.md#oninit)

---

### onDraw

Event

**Description**

Event called when the screen is drawn

Fires on every drawing cycle. When a Canvas is assigned, it is called internally between BeginDrawing and EndDrawing, so you can issue drawing commands through the [canvas](#canvas) property inside the handler.

---
