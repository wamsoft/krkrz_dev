---
source_hash: 1b13a00a0b63
---

# Features Removed/Added in the Wamsoft Fork

This page summarizes the **removed legacy features** and **newly added features** in the fork maintained by Wamsoft Ltd. Partnership ([wamsoft/krkrz_dev](https://github.com/wamsoft/krkrz_dev)), relative to upstream Kirikiri Z / Kirikiri 2.

For removals of individual TJS APIs, also see [Features Removed in Kirikiri Z](deleted.md).

## Removed legacy features

Implementations that depended on legacy Windows APIs or stood in the way of cross-platform support have mainly been replaced or removed.

| Removed | Replacement / current status |
| --- | --- |
| DirectSound (audio output) | **miniaudio** (the audio engine shared by all builds; WASAPI shared mode, multichannel support) |
| DirectShow / EVR-based movie playback (`dsmovie` / `dslayerd`, etc.) | Unified to CPU decoding (webm=movie-player / MPEG-1=pl_mpeg / others=Media Foundation SourceReader) + **Direct3D 11 compositing** |
| The krmovie plugin boundary (tp_stub / V2Link DLL boundary) | krmovie is **built directly into the exe** (calls engine symbols directly) |
| krflash / `.swf` (Flash movies) | Removed |
| Display via Direct3D 9 / DirectDraw (exclusive fullscreen, etc.) | **Direct3D 11 / DXGI** (flip-model swap chain, borderless fullscreen) |
| DirectInput (gamepad / mouse) | **XInput** for gamepads, `WM_MOUSEWHEEL` for the mouse wheel (multi-pad support via the shared `tTVPPadManager`) |
| NASM assembly optimizations for TLG6 | C reference implementation (`tvpgl.c`). SSE2/AVX2/NEON SIMD implementations exist separately |
| JPEG XR (`.jxr`) loader | Removed (no replacement) |
| `timeBeginPeriod` / `timeGetTime` timers | **QueryPerformanceCounter** + high-resolution waitable timer |
| Various legacy Win32 compatibility shims (XP/Vista/7/8 fallbacks) | Linked directly with Windows 10 or later as the minimum target |
| Various Perl generators (`makestub.pl` / `gentext*.pl`, etc.) | **Python** generators (byte-identical output) |

### Main TJS classes / APIs removed from the core

The following were removed from the engine core and are supplemented by the bundled **Krkr2Compat** or individual plugins (details in [Removed Features](deleted.md)).

- `KAGParser` class → link and use the `KAGParser.dll` plugin
- `Menu` class → `menu.dll`
- `Console` class / debug console window (`Debug.console`) → Krkr2Compat
- `Font.doUserSelect` (font selection dialog) / `System.inputString` (single-line input) → Krkr2Compat
- `Layer.hint`, and obsolete methods such as `affineBlend` / `affinePile` / `blendRect` / `pileRect` / `stretchBlend` / `stretchPile` → can be reimplemented in TJS with `operateAffine` / `operateRect` / `operateStretch`

## Newly added features

These center on cross-platform support (SDL3) and extensions to GPU rendering, development support, and sound features.

| Added feature | Summary |
| --- | --- |
| SDL3 cross-platform build | Generic build supporting Windows / Linux / macOS / Android / Emscripten (web), plus the LIB build in static-library form |
| OpenGL ES rendering path | The lazily initialized GPU draw device [OGLDrawDevice](../../reference/OGLDrawDevice.md) and GL classes such as [Canvas](../../reference/Canvas.md) / [Texture](../../reference/Texture.md) / [ShaderProgram](../../reference/ShaderProgram.md) / [Offscreen](../../reference/Offscreen.md) / VertexBuffer / Matrix32 / Matrix44 |
| GLCompositor | A class that performs offscreen OpenGL ES compositing behind the scenes even under non-GL draw devices and writes the result back to a Layer ([GLCompositor](../../reference/GLCompositor.md)) |
| Canvas transition drawing | GPU-based screen transition drawing with `Canvas.drawTransition` |
| Elements-based general-purpose dialogs | Cross-platform UI defined in JSON / Dictionary (the [ElementsDialog](../../reference/ElementsDialog.md) class; details in [Dialog](../../guide/ElementsDialog.md)) |
| REPL (interactive TJS shell) | Script evaluation and verification via `-repl` / `-replfile` ([REPL](../core/repl.md)) |
| WebServer | Built-in HTTP + SSE server (`-replweb`). Endpoints can be registered from TJS ([WebServer](../../reference/WebServer.md)) |
| Agent | Automation API for input injection, screen capture and dialog operation ([Agent](../../reference/Agent.md)) |
| FreeType color emoji fonts | Rasterization of CBDT/COLR color emoji (`Font.emojiMode`) |
| Font metadata and lazy loading | Declared in `fonts.json`; the actual file is loaded on first use (reduces executable size) |
| Gamepad multi-pad redesign | Multiple pad support (logical pad 0 = the most recently used pad), shared `tTVPPadManager` |
| 3D sound positioning (spatializer) | miniaudio-based position/distance/Doppler/directivity (the `use3D` family of [WaveSoundBuffer](../../reference/WaveSoundBuffer.md), [SoundListener](../../reference/SoundListener.md)) |
| Lip-sync / sound analysis API | `getSoundLevel` / `getSoundSpectrum` / `getVowel` / `getVisBuffer` |
| 3D / effect plugins | threepp (a three.js port) / Effekseer / Live2D / GLES helpers |
| Media Foundation HW movies | Hardware decoding via `IMFMediaEngine` (default for mp4/wmv; disable with `-mediaengine=no`) |
| On-screen debug displays | Gamepad state (PadOverlay), memory monitoring, render thread utilization (DrawStats) |
| DPI awareness / borderless fullscreen / long paths | PerMonitorV2 DPI awareness (when moving to a monitor with a different scale factor, the pixel size of the drawing area is kept and only the frame is redrawn), `\\?\` extended path support |
| Controlling the game screen's display area (viewport) | Places the inner game screen inside the outer window with fit / zoom / align / offset and fills the margin with a background color or wallpaper ([Viewport](../core/viewport.md)) |
| Selecting the startup display | `-display` picks the monitor shown first in a multi-display environment by number / name ([Command-Line Options](../../guide/CommandLine.md)) |
| Selecting the DrawDevice at startup | `-drawdevice` selects the draw device at startup (the SDL3 default is the OpenGL ES-based [SDLOGLDrawDevice](../../reference/SDLOGLDrawDevice.md)). `-forceegl` can also force EGL for the GLES context |
| Localized messages / settings UI | Engine messages and option descriptions (`-userconf`) follow the OS language (ja / en / chs / cht). Specify explicitly with `-language` ([Command-Line Options](../../guide/CommandLine.md)) |
