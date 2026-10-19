# SDLDrawDevice

SDLDrawDevice is a DrawDevice that you register in [Window.drawDevice](Window.md#drawdevice); it provides standard drawing using SDL3 (`SDL_Renderer` + `SDL_Texture`). It is available only in the SDL3 build (KRKRZ_VARIANT=SDL) and is not included in the WINVER build.

In the SDL3 build, the default DrawDevice at startup is the OpenGL ES-based [SDLOGLDrawDevice](SDLOGLDrawDevice.md) in builds with OpenGL enabled, and this class in builds with OpenGL disabled. Specifying the command-line option `-drawdevice=sdl` starts with this class even in a build with OpenGL enabled ([command-line options](../guide/CommandLine.md)). The `SDL_Renderer` backend is chosen automatically and can be set explicitly with the `-renderer` option.

If you start with this class, you cannot switch to an OpenGL device ([SDLOGLDrawDevice](SDLOGLDrawDevice.md) / [OGLDrawDevice](OGLDrawDevice.md)) at run time (OpenGL initialization fails). To use OpenGL features ([Canvas](Canvas.md) and so on), start with an OpenGL DrawDevice from the beginning.

## Members

### Constructors

- [SDLDrawDevice](#sdldrawdevice)

### Properties

- [interface](#interface)
- [window](#window)
- [sdlVideoPresenterHost](#sdlvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLDrawDevice

Constructor

**Description**

Constructs an SDLDrawDevice object

Constructs an object of the SDLDrawDevice class.

When this class is the startup default (in a build with OpenGL disabled, or when `-drawdevice=sdl` is specified), an instance of it is already registered in Window.drawDevice, so you do not need to register one yourself.

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

### sdlVideoPresenterHost

Property \ Access: `r`

**Description**

Registration point for the overlay movie presenter (pointer value)

A pointer value to the presenter host that the overlay movie reads in order to composite into this DrawDevice in a pull model
(the same convention as [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) in WINVER).
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
