---
source_hash: 51b508dc940e
---

# System Architecture

This page describes the system architecture of Kirikiri Z (the Wamsoft derivative implementation).

## Overview

The current Kirikiri Z has two main build lines.

- **WINVER** — The native Windows implementation. It draws with Direct3D 11 and uses the Win32 API for windows and input. This line is dedicated to running on Windows.
- **SDL(GENERIC)** — A cross-platform implementation built on SDL3, and the default line. It delegates windows, input, and display to SDL3 and draws primarily with OpenGL ES. It targets Windows / Linux / macOS / Android / Emscripten (web).

In addition, there is a **LIB** form that packages the GENERIC line as a static library. It is intended for embedding into other applications as a library rather than as an executable, and its internal components are the same as SDL(GENERIC).

All lines share the core parts — the TJS2 language runtime, layer/Bitmap image processing, the OpenGL drawing classes, miniaudio sound, and the plugin ABI. The differences between lines show up mainly in the platform bindings for windows, drawing, input, movies, and sound.

## WINVER main components

| Feature | Implementation | Notes |
| --- | --- | --- |
| Drawing/display | Direct3D 11 / DXGI (BasicDrawDevice) | The default draw device. Uses a flip-model swap chain (`d3d11` / `dxgi` / `d3dcompiler`). |
| Window/input | Win32 API | Window creation, message handling, and keyboard/mouse input. |
| Gamepad | XInput | The old DirectInput implementation has been retired. |
| Movie | Media Foundation and others | Hardware decoding via Media Foundation SourceReader + IMFMediaEngine; webm via movie-player; MPEG-1 via pl_mpeg. krmovie is linked directly into the exe, and the old DirectShow/EVR/plugin boundary has been removed. |
| Sound | miniaudio (WASAPI) | miniaudio owns the output device. The old DirectSound implementation has been removed. |
| OpenGL ES path (optional) | ANGLE / EGL | `libEGL.dll` / `libGLESv2.dll`. Used when the drawDevice is switched to an OpenGL-based one. |

## SDL(GENERIC) main components

| Feature | Implementation | Notes |
| --- | --- | --- |
| Window/input/display | SDL3 | Handles window creation, input, timing, and so on. |
| Draw device | OpenGL ES based (SDLOGLDrawDevice) / SDL_Renderer based (SDLDrawDevice) | The default is the OpenGL ES based SDLOGLDrawDevice. The SDL_Renderer based SDLDrawDevice can also be selected. |
| OpenGL ES | glad + the platform's GLES/EGL | On Windows, it transparently falls back to ANGLE. |
| Movie | movie-player (webm) + pl_mpeg (MPEG-1) | On Emscripten (web), this becomes WebMoviePlayer, which uses the browser's `<video>`. |
| Sound | miniaudio (no-device mode) | miniaudio generates PCM with device I/O disabled, and SDL3 owns the output device. |

Supported platforms are Windows / Linux / macOS / Android / Emscripten (web).

## Shared components

Both lines share the following components.

- **TJS2 language runtime** (`common/tjs2`) — The compiler and runtime for the TJS2 scripting language.
- **Layer/Bitmap image processing** — Blending, resampling, and so on over the CPU-side 32bpp BGRA compositing surface. Includes SIMD implementations (SSE2 / AVX2 / NEON) and a C reference implementation (`tvpgl.c`).
- **OGLDrawDevice and the GL classes** — The OpenGL ES drawing classes such as Canvas / Texture / ShaderProgram / Offscreen. Both lines share the same GL code.
- **miniaudio sound** — Used as the single sound engine in all builds.
- **Plugin ABI** — The binary interface to plugins via `tp_stub`.

## Default draw device at startup

| Line | Default draw device at startup |
| --- | --- |
| WINVER | BasicDrawDevice (Direct3D 11) |
| SDL(GENERIC) | OpenGL ES based (SDLOGLDrawDevice) |

OGLDrawDevice is initialized lazily when a TJS script switches `drawDevice` to it. Since both lines share the same GL drawing code, behavior after the switch is the same.
