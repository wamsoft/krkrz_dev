---
source_hash: 2aaa6c7a0159
---

# Standard Tools

## About the standard tools

Kirikiri Z ships with standard tools for preparing game assets and getting ready for distribution.
They succeed the tools bundled with Kirikiri 2 (Releaser, the image format converter, the loop tuner, and others),
and run on Windows / Linux / macOS (only the Releaser is Windows-only).

| Tool | Executable | Purpose |
|---|---|---|
| [xp3 archive tool](Xp3Tool.md) | `krkrxp3` | Packs a folder into an xp3 archive; lists, extracts, and verifies archive contents |
| [Key and signing tool](SignTool.md) | `krkrsign` | Creates signing keys, digitally signs distribution files, and verifies signatures |
| [File corruption check tool](FileChkTool.md) | `krkrcheck` | Checks distribution files for corruption on the end user's machine, using their signatures |
| [Image format converter](TPC.md) | `krkrimg` | Converts BMP / PNG / JPEG / TLG / PSD / CLIP to TLG5, TLG6, and other formats; exports PSD and CLIP layers |
| [Audio format converter](AudioConverter.md) | `krkraudio` | Converts between WAV / Ogg Vorbis / Ogg Opus; adjusts and measures loudness |
| [Loop tuner](LoopTuner.md) | `krkrloop` | Edits and previews the links and labels of loop information (.sli) while viewing the waveform |
| [Releaser](Releaser.md) | `krkrrelease` | Builds the executable for distribution (embeds command-line options, icon, and version information; binds xp3; signs). **Windows only** |

Pre-rendered fonts (.tft) are created with the tftSave plugin rather than a tool
(see [Creating Pre-rendered Font Data](FontMaker.md)).

## Getting the tools

The source of the tools lives in the [krkrz_tools](https://github.com/wamsoft/krkrz_tools) repository,
and is included in the Kirikiri Z development repository (krkrz_dev) as `src/tools/krkrz_tools`.

When you build the engine in krkrz_dev, the tools are built along with it, and `make install`
places them in the `tools/` folder of the install destination.

```
make prebuild
make
make install          # bin/<プリセット>/Release/tools/ にツールが入る
```

- Each tool runs as a single executable (no DLLs or other files need to be placed alongside it)
- To skip building the tools, run `make prebuild` with `CMAKEOPT='-DKRKRZ_BUILD_TOOLS=OFF'`
- krkrz_tools can also be built on its own (see the krkrz_tools README for the steps)

> **Note:**
> The tools are for desktop platforms (Windows / Linux / macOS). They are not built for Android, iOS, or the browser version.

## Using the GUI

When you launch a tool's executable (with no arguments, or with files or folders as arguments),
its GUI opens in a browser window. The GUI is embedded in the executable,
so no internet connection is needed. Closing the GUI also exits the tool.

- The GUI is served by a server the tool itself runs locally (127.0.0.1). It cannot be reached from outside
- Choose files and folders with the «参照…» (Browse...) button in the GUI

## Using the command line

Every tool, when given `--cli`, processes on the command line without opening the GUI and then exits.
This is useful for batch processing and build automation.

```
krkrxp3 --cli pack data --out=release/data.xp3
krkrimg --cli convert images/*.png --out=converted --opaque=tlg5 --alpha=tlg6
krkrloop --cli check bgm/*.ogg
```

- Options that take a value are written as `--name=value` (`--out=dir`; `--out dir` does not work)
- `--help` shows the list of options
- When you want to process the results by machine, many commands support `--json`
- Progress is shown on standard error (only on a terminal; not when piped or redirected). `--quiet` turns it off
- For every tool, the exit code is «0 = success, anything else = problems found or failure». See each tool's page for details

## Developer options

These options are for modifying a tool's GUI. They are not normally needed.

- `--web-root=folder`: uses the GUI in the specified folder instead of the embedded one
- `--no-embedded`: does not use the embedded GUI; looks for `web/` and similar in the current folder instead
- `--browser=none --port=N`: runs only the GUI server on the specified port, without opening a browser
