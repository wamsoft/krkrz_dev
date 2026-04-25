# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`krkrz_dev` is the **umbrella development repository** for 吉里吉里Z (Kirikiri Z). It does not contain engine source code of its own — instead it aggregates, via git submodules, the engine core, every plugin, TJS2 script libraries (KAG3, Krkr2Compat, samples, tests) under a single CMake build. Almost every path under `src/plugins/*`, `src/core`, `script/*`, and `src/tools/*/` is a submodule with its own upstream repo (see `.gitmodules`). Clone with `--recursive` or run `git submodule update --init --recursive` before building. Documentation is now SSOT in `doc/` (mkdocs site) — no submodule.

The top-level `CMakeLists.txt` only picks which plugins to build and then delegates to `src/core` (the engine) via `add_subdirectory`. For engine-internal architecture — WINVER vs SDL3 vs LIB variants, the OpenGL ES draw-device path, SIMD layout, generated files, build flags, the SIMD parity CTest harness, etc. — **read `src/core/CLAUDE.md`**. Do not duplicate that information here.

## Build commands (umbrella level)

vcpkg is required; set `VCPKG_ROOT` before configuring. The top-level `Makefile` is a thin wrapper around CMake presets defined in `src/core/CMakePresets.json`.

```bash
# Configure + build + install (preset auto-picked from OS; defaults to Release)
make prebuild          # cmake --preset $(PRESET) $(CMAKEOPT)
make                   # cmake --build
make install           # installs under bin/$(PRESET)/$(BUILD_TYPE)
make clean
make run               # Windows only: builds, copies plugin DLLs next to exe, runs krkrz(64).exe $(DATAPATH)

# Override preset / config / cmake args
PRESET=x64-windows-sdl BUILD_TYPE=Debug CMAKEOPT='-DKRKRZ_USE_SJIS=ON' make prebuild build
```

- Default `CMAKEOPT` in the root Makefile is `-DKRKRZ_USE_SJIS=YES`. Override it (don't append to it) when you need different flags — the Makefile assigns, it doesn't append.
- `make run` uses `DATAPATH` (default `src/core/data`) as the game data argument and on Windows copies `plugin/` or `plugin64/` DLLs (ANGLE `libEGL.dll` / `libGLESv2.dll`) into the build output so OpenGL works at runtime.
- For SJIS win32 legacy builds, launch from the Visual Studio **x86** Developer Command Prompt — vcpkg misbehaves otherwise (see `README.md`).
- Available presets and preset naming are documented in `src/core/CLAUDE.md`; the umbrella Makefile only auto-picks a default.

There are no automated tests at this umbrella level. The only test target is the SIMD parity CTest harness inside `src/core` (`krkrz_simd_parity_test`, CTest name `simd_parity`), described in `src/core/CLAUDE.md`.

## Plugin selection

Plugins to build live in the top-level `CMakeLists.txt` as two lists consumed by `src/core`:

- `TVP_PLUGINS` — shared, portable plugins built for every variant.
- A second block gated on `KRKRZ_VARIANT STREQUAL "WIN"` — Win32-only plugins (`addFont`, `windowEx`, `layerExDraw`, `win32ole`, …) that still use Win32 APIs and have not been ported.
- `TVP_PLUGINS_STATIC` (passed via `CMAKEOPT`) — subset to link statically into the exe; see the plugin-system section of `src/core/CLAUDE.md` for the static-registration contract.

Commented-out entries (`minizip`, `psdfile`, `sigcheck`, `krkrlua`, `resourceRW`, `httpserv`, `steam`) are intentionally excluded from the default build — don't re-enable without checking why. The `steam` plugin only appears when `$STEAMWORKS_SDK` is set in the environment.

When you need to modify plugin code itself, remember each `src/plugins/<name>/` is its own submodule: commits go to that plugin's upstream repo, not to `krkrz_dev`. The same applies to `src/core` and `script/*`.

## Conventions

Source is UTF-8; comments, identifiers, and commit messages are frequently in Japanese — keep that style when editing existing files. The default branch here is `develop` (not `master`); PRs typically target `master` only for releases.
