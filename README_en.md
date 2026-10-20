<!-- source_hash: 4130d201b41a -->
# krkrz_dev — Kirikiri Z integrated development repository

[日本語](README.md) | English

The integrated development repository of Kirikiri Z. It bundles the engine, plugins, TJS2 script
libraries and the standard tools as git submodules into one CMake build. The desktop builds for
Windows / Linux / macOS are built from this repository.

- **Documentation**: the [documentation site](https://wamsoft.github.io/krkrz_dev/en/) (Japanese / English).
  Its source is `doc/` in this repository
- **Branches**: `develop` is the main development branch and `master` is for releases (the engine
  `src/core` points to a different repository per branch; on master it is the public engine
  [krkrz](https://github.com/wamsoft/krkrz))
- The browser, Android, iOS, Linux distribution packages and Microsoft GDK are built in separate
  "wrapper" repositories that use this repository as their engine source ([below](#wrapper-repositories))

## Repository layout

| Folder | Contents |
|---|---|
| `src/core` | The engine (a submodule). Build details and internals are in [src/core/README.md](src/core/README.md) |
| `src/plugins/*` | Plugins (each a submodule). The list is in [Plugins](https://wamsoft.github.io/krkrz_dev/en/guide/Plugins/) on the documentation site |
| `src/tools/krkrz_tools` | The standard tools (a submodule, [krkrz_tools](https://github.com/wamsoft/krkrz_tools)) |
| `script/*` | TJS2 script libraries (KAG3 / Krkr2Compat / samples / tests; each a submodule) |
| `data/` | Plugin / feature samples and the integrated demo gallery (`startup.tjs` at its root). The engine's core feature demos are in `src/core/data/` |
| `doc/` | The source of the documentation site (mkdocs). How it is generated is described in [tools/docgen/README.md](tools/docgen/README.md) (in Japanese) |
| `tools/` | Helper tools such as documentation generation and the Claude Code skills |

Each submodule is an independent repository. Commits that change one go to that submodule's
repository. The list of open issues is in [TODO.md](TODO.md) (in Japanese).

## Wrapper repositories

| Repository | Target | Settings file |
|---|---|---|
| [krkrz_web](https://github.com/wamsoft/krkrz_web) | Browser (Emscripten / wasm32) | `web-config.json` |
| [krkrz_android](https://github.com/wamsoft/krkrz_android) | Android (Gradle + NDK) | `app-config.json` |
| [krkrz_ios](https://github.com/wamsoft/krkrz_ios) | iOS / iPadOS (CMake's Xcode generator) | `ios-config.json` |
| [krkrz_linux](https://github.com/wamsoft/krkrz_linux) | Linux distribution packages (built in the Steam Linux Runtime SDK container) | `linux-config.json` |
| [krkrz_gdk](https://github.com/wamsoft/krkrz_gdk) | Microsoft GDK (PC / Xbox) | `gdk-config.json` |

- Clone each one into the same folder as this repository and set the environment variable
  `KRKRZ_BASE` to that parent folder (so `KRKRZ_BASE/krkrz_dev`, `KRKRZ_BASE/krkrz_android` and so on sit side by side)
- They do not modify the engine or the plugins; they hold only the per-platform build definitions and packaging
- A title's settings and assets can live in a separate folder (the project folder). The `cmake`
  (plugin configuration) and `assetPack` (asset collection) parts of the settings share one format,
  so you can put the settings for every platform in one project folder and reuse the same data. See
  [Shared settings of the platform wrappers](https://wamsoft.github.io/krkrz_dev/en/topics/core/platform_config/)
  on the documentation site for the format

The details for each platform are in its README.

## Requirements

- **Windows**: Visual Studio 2022 (v17.14) with its bundled CMake / Ninja. Other versions and
  toolchains have not been tested
- **Linux**: the reference is the Docker build environment created by `deckbuild/` of
  [steamdev](https://github.com/wamsoft/steamdev) (the Steam Linux Runtime 3.0 "sniper" SDK,
  Debian 11 / glibc 2.31) ([below](#building-on-linux))
- **macOS**: built with the `x64-osx` / `arm64-osx` presets (the written procedure is still in progress)
- [vcpkg](https://github.com/microsoft/vcpkg) — set the environment variable `VCPKG_ROOT` to where it is installed

  ```
  export VCPKG_ROOT=d:/vcpkg
  ```

- To use make, an environment that provides make, such as cygwin or msys2 (you can then use the Makefile below)

## Getting the source

```
git clone --recursive https://github.com/wamsoft/krkrz_dev.git
```

Fetch all submodules recursively. To fetch them later, use `git submodule update --init --recursive`.

## Building

The build uses the CMake presets (`src/core/CMakePresets.json`). The build folder is `build/<preset name>`.
The list of presets and the main build options are in [src/core/README.md](src/core/README.md).

```
cmake --preset=x64-windows                                      # prepare the build
cmake --build build/x64-windows --config Release                # build
cmake --install build/x64-windows --config Release --prefix bin # install
```

The Makefile does the same.

```
make prebuild     # cmake --preset
make              # cmake --build
make install      # install to bin/<preset>/<build type>
make run          # (Windows) build and start the demos
```

| Kind | Name | Description |
|---|---|---|
| Environment variable | `PRESET` | The CMake preset name (chosen from the OS when not set) |
| | `BUILD_TYPE` | `Debug` / `RelWithDebInfo` / `Release` (default `Release`) |
| | `CMAKEOPT` | Extra options passed to CMake |

```
# 32-bit (SJIS-enabled) build
export PRESET=x86-windows
export CMAKEOPT="-DKRKRZ_USE_SJIS=ON"
make prebuild && make && make install
```

To build the 32-bit version, work from Visual Studio's x86 command prompt. If the environment is not
set up for x86, vcpkg misbehaves.

### Placing the ANGLE DLLs for OpenGL (Windows)

Using the engine's OpenGL (GLES) features on Windows needs ANGLE's `libEGL.dll` / `libGLESv2.dll`
(required for the WINVER build; for the SDL3 build, a fallback for environments where the OpenGL
driver's ES profile is not available). They are not in the repository, so put them in `plugin/`
(32-bit) / `plugin64/` (64-bit) at the repository root. `make run` copies them to the build output.
The Releases of [mmozeiko/build-angle](https://github.com/mmozeiko/build-angle) are an easy source.
See "OpenGL ES の実行環境" in [src/core/README.md](src/core/README.md) for the caveats.

### Building on Linux

Build in the Docker build environment created by steamdev's `deckbuild/` (Valve's Steam Linux Runtime
3.0 "sniper" SDK). What you build there runs on SteamOS, in Steam Linux Runtime containers and on
common distributions with glibc 2.31 or later.

```bash
# With docker on WSL2. Create the image the first time only
<steamdev>/deckbuild/deckbuild.sh image

# Build (configure + build + install → bin/x64-linux/Release/)
<steamdev>/deckbuild/deckbuild.sh -s /mnt/d/work/kirikiri/krkrz_dev all
```

`deckproject.toml` at the repository root is the project definition for the steamdev CLI; it runs
everything from the build to transferring and starting it on a Steam Deck in one go
(`steamdev -d <deck> project -p . ship linux`). The compatibility policy and the acceptance criteria
for the binary (the required glibc symbols are 2.31 or lower, and so on) are in
[src/core/doc/LinuxBuild.md](src/core/doc/LinuxBuild.md) (in Japanese).

## Standard tools (krkrz_tools)

The tools in `src/tools/krkrz_tools` (corruption check, signing, xp3, audio / image converters, loop
tuner, releaser) are built along with the engine and placed in `<install folder>/tools/` by `make install`.

- The tools are linked statically (`x64-windows-static` and so on) so each can ship as a single exe,
  so they are a separate build from the engine (`build/<preset>/krkrz_tools`, always Release; `cmake/KrkrzTools.cmake`)
- The first time, building the static vcpkg libraries for the tools takes a while
- Enabled by default on the desktop (Windows / Linux / macOS). `CMAKEOPT='-DKRKRZ_BUILD_TOOLS=OFF'` leaves them out

How to use each tool is in the [krkrz_tools README](src/tools/krkrz_tools/README_en.md).

## Choosing plugins

The plugins to build are set by `TVP_PLUGINS` (a list of folder names) in the top-level `CMakeLists.txt`.
Those listed in `TVP_PLUGINS_STATIC` are linked statically into the executable. These are CMake lists,
separated by `;`.

```
CMAKEOPT='-DKRKRZ_USE_SJIS=ON -DTVP_PLUGINS_STATIC="json;csvParser"' make prebuild
make
make install
```

When a plugin uses external libraries, put a `vcpkg.json` in that plugin's folder. Its dependencies
are merged automatically only when the plugin is part of the build (there is no `vcpkg.json` at the
repository root; CMake combines the engine's and each plugin's `vcpkg.json` in the build folder). The
merge rules and how to exclude entries are at the top of
[src/core/cmake/MergeVcpkgManifest.cmake](src/core/cmake/MergeVcpkgManifest.cmake).

```json
{
  "name": "minizip",
  "version": "0.0.1",
  "dependencies": [ "minizip-ng" ]
}
```

## Claude Code skills

This repository includes [Claude Code](https://claude.com/claude-code) skills for Kirikiri Z
development, so you do not have to explain "how to write TJS2", "the Layer API" or "how to check things
through the REPL" to Claude every time.

| Skill | Contents |
|---|---|
| `krkrz` | The engine's class API (Layer / Window / Bitmap / Storages / DrawDevice / OpenGL drawing / sound / the main plugins) |
| `tjs2` | The TJS2 language and its built-in classes, focusing on the differences from JavaScript |
| `elements` | Building dialogs and screen UIs with Elements |
| `krkrz-repl` | Driving the engine from an agent with `-repl` / `-replfile`, the Agent API, screen capture |
| `krkrz-webui` | Putting a browser UI on the `-replweb` HTTP + SSE server |

The originals are in `.claude/skills/` and **work as is while you work in this repository**. How to
install them for use in other repositories (`bash tools/skills/install.sh --user` and so on), and notes
on updating and editing them, are in [tools/skills/README.md](tools/skills/README.md) (in Japanese).

## License

This repository bundles its components as submodules, and each component defines its own license.
See [src/core/LICENSE](src/core/LICENSE) for the engine and the LICENSE / README in each folder for the
plugins. A summary is in [LICENSE.md](LICENSE.md) (in Japanese). The list of third-party components
included in distributions is [Bundled Licenses](https://wamsoft.github.io/krkrz_dev/en/guide/BundledLicenses/)
on the documentation site.
