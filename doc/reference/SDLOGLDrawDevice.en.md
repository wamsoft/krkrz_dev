# SDLOGLDrawDevice

SDLOGLDrawDevice is a DrawDevice that you register in [Window.drawDevice](Window.md#drawdevice); in the SDL3 build it draws the layer compositing result to the screen using OpenGL ES directly. It is available only in the SDL3 build (KRKRZ_VARIANT=SDL) and is not included in the WINVER build.

In the SDL3 build with OpenGL enabled (the default configuration), it is registered from the start as the **default DrawDevice at startup**, so you normally do not need to think about it. You can also select it explicitly with the command-line option `-drawdevice=sdlogl` ([command-line options](../guide/CommandLine.md)).

The difference from [SDLDrawDevice](SDLDrawDevice.md) (which goes through `SDL_Renderer`) is that it updates textures and draws with OpenGL ES directly, without SDL's renderer abstraction. It is a simplified version of [OGLDrawDevice](OGLDrawDevice.md) (the full-featured version with the GL classes exposed to TJS, such as [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md)) that drops the TJS-exposed logic and keeps only "layer drawing + movie playback". The GL context can be shared with OGLDrawDevice, so if you want to use Canvas and the like, you can switch by setting an [OGLDrawDevice](OGLDrawDevice.md) in Window.drawDevice.

It requires an environment where OpenGL ES is available (the ES profile of the OS OpenGL driver, or ANGLE's `libEGL.dll` / `libGLESv2.dll`; `-forceegl` forces EGL).

## Members

### Constructors

- [SDLOGLDrawDevice](#sdlogldrawdevice)

### Properties

- [interface](#interface)
- [window](#window)
- [glVideoPresenterHost](#glvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLOGLDrawDevice

Constructor

**Description**

Constructs an SDLOGLDrawDevice object

Constructs an object of the SDLOGLDrawDevice class.

In the SDL3 build with OpenGL enabled, it is registered in Window.drawDevice from the start as the default DrawDevice, so you do not need to register one yourself.

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
