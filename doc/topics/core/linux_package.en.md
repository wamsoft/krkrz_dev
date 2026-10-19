---
source_hash: 3b64345ac2fd
---

# Linux Distribution Packages (krkrz_linux)

This describes how to bundle the Kirikiri Z engine with your game data into a distributable package for Linux.
The tool is the wrapper repository [krkrz_linux](https://github.com/wamsoft/krkrz_linux).
Like krkrz_android / krkrz_ios / krkrz_web, it references krkrz_dev as the engine via `KRKRZ_BASE`
and handles only the Linux-specific build and packaging.

## Linux distribution formats and policy

Linux has no single app format like Android's APK; the format differs by distribution channel.
However, each one is just a "runnable folder" repackaged with freedesktop
metadata (`.desktop` / icon / AppStream).

| Format | Main distribution channels | krkrz_linux |
|---|---|---|
| Folder / tar.gz | Steam depots, itch.io, GOG, Humble | ✅ Produced |
| AppImage | Your own site, itch.io | Not implemented (can be built from the same folder; the `.desktop` file and icon are already generated) |
| Flatpak | Flathub | Undecided (requires AppStream metadata and a manifest) |

Steam, which matters most for games, accepts the folder itself, so the policy is: **the folder is the official
deliverable, and other formats are repackagings of it**.

## Build environment

Builds run in a container of Valve's **Steam Linux Runtime 3.0 "sniper" SDK** (Debian 11 / glibc 2.31).
The resulting binaries run on native SteamOS, the Steam Linux Runtime, and common distributions with
glibc 2.31 or later. The image used is `deckbuild-sniper`, created with
`deckbuild/deckbuild.sh image` from [steamdev](https://github.com/wamsoft/steamdev). The acceptance criteria
(required glibc ≤ 2.31 / no GLIBCXX dependency) are defined in the engine's `src/core/doc/LinuxBuild.md` (SSOT).

## Usage

```bash
export KRKRZ_BASE=~/kirikiri                 # krkrz_dev のある親フォルダ
cd ~/kirikiri/krkrz_linux
make all                                     # サンプル案件 (コアデモ)
PROJECT_DIR=/path/to/mygame make all         # 自分の案件
```

(`KRKRZ_BASE` is the parent folder containing krkrz_dev; plain `make all` builds the sample project (the core
demos), and `PROJECT_DIR=... make all` builds your own project.)

Output goes under `${PROJECT_DIR}/build/linux/`.

- `package/<exeName>/` … the runnable folder
- `dist/<exeName>-<version>-linux-x86_64.tar.gz` … the same folder archived

The project definition is `${PROJECT_DIR}/linux-config.json`. `cmake` (plugin configuration) and
`assetPack` (asset import, first match wins) use the same format as krkrz_android's `app-config.json`,
so the asset definitions in your project folder can be shared. For the full list of fields, see the krkrz_linux
README.

## Package contents

```
mygame/
  mygame                 実行ファイル ( KRKRZ_EXE_NAME )
  libSDL3.so.0 ( .x.y )  同梱 SDL3
  plugin/*.so            プラグイン
  mygame.cf              orgname / appname ほか ( 生成 )
  <id>.desktop, <id>.svg freedesktop のメタデータ ( 生成 )
  license.txt, licenses/
  data/ または data.xp3  引数なしで起動すると自動検出される
```

(In order: the executable (`KRKRZ_EXE_NAME`), the bundled SDL3, plugins, `orgname` / `appname` and other settings
(generated), freedesktop metadata (generated), licenses, and the game data — `data/` or `data.xp3` is detected
automatically when launched without arguments.)

### Resolving bundled .so files (RPATH)

The executable has `$ORIGIN`, and plugins built with `krkrz_plugin()` have
`$ORIGIN:$ORIGIN/..`, embedded as **DT_RPATH**. The bundled SDL3 and
.so files that plugins depend on (placed in `plugin/` or the executable's folder) are loaded
without `LD_LIBRARY_PATH` or a launcher script.

When launched from Steam, the Steam runtime and `/usr/lib` are prepended to `LD_LIBRARY_PATH`,
so with RUNPATH (the default of newer linkers) or `LD_LIBRARY_PATH=.`, a SteamOS .so with the same
name would be loaded first. DT_RPATH is searched before that, so
the bundled version is reliably used. Plugins that set RPATH in their own CMake should use
`--disable-new-dtags` (if a plugin has RUNPATH, the executable's
DT_RPATH also stops taking effect).

### Plugin symbol visibility (2026-10 onward)

Shared plugins built with `krkrz_plugin()` no longer export their symbols by default on
platforms other than Windows (equivalent to `-fvisibility=hidden`). Only `V2Link` /
`V2Unlink`, which are marked `DLL_EXPORT`, are visible. The ncbind and simplebinder
scaffolds already mark them, so they work as is. If your plugin defines its own entry
points, mark them with `DLL_EXPORT`.

Previously everything was exported, so on Linux inline static members with the same name
(such as ncbind's auto-registration list) were merged across plugins, and loading a second
ncbind plugin stopped during its load (the same happened on macOS). If you build a plugin
with your own CMake, use the same settings (`C_VISIBILITY_PRESET` / `CXX_VISIBILITY_PRESET hidden`
and `VISIBILITY_INLINES_HIDDEN`).

## Save data location (2026-10 onward)

!!! warning "Important (changed in 2026-10)"
    The default data location on Linux (when `-datapath` is not specified) has changed from
    `savedata` next to the executable to **`~/.local/share/<orgname>/<appname>/`** (under `$XDG_DATA_HOME`
    if set). For details, see
    [-datapath in Command-Line Options](../../guide/CommandLine.md).

- The rule is to **take `orgname` / `appname` from the project settings and write them into `<exeName>.cf`**.
  krkrz_linux writes them automatically from `orgName` / `appName` in `linux-config.json`.
  This gives each title its own folder
- Because nothing is written next to the executable, it works even when installed in a read-only location (AppImage, Flatpak,
  `/opt`, etc.)
- `System.dataPath` is a local path (`file://./home/…`), so
  `Storages.getLocalName()` can also be used
- You can check the actual save location in the `datapath (Linux default, …)` line of the startup log

### Steam Cloud

When using Steamworks Auto-Cloud, set the Linux root to `LinuxXdgDataHome`
(= `~/.local/share`) and the subdirectory to `<orgname>/<appname>`.
The save location differs from the Windows version, so when shipping both, use "root overrides" to
specify it per OS (check the root type names in the Steamworks settings page).

## Testing on Steam Deck

The krkrz_linux output folder can be sent to a Deck as-is with steamdev.

```bash
steamdev -d <deck> deploy --gameid mygame_linux \
    --dir build/linux/package/mygame --command "./mygame" --start
```

A gameid may contain only alphanumerics, `_` and `.` (no hyphens). Verified on 2026-10-06 with the krkrz_linux
sample project (the core demos): running natively on the Deck, all 24 `-demotest` scenes were ok,
the bundled SDL3 was loaded, and the save location was `/home/deck/.local/share/wamsoft/krkrz-sample/`.

For the full procedure and common pitfalls, see [Steam Deck Hardware Testing](steamdeck.md).

## Future work

- AppImage output (add `AppRun` and package with `appimagetool`)
- As with krkrz_android, xp3 archives are created beforehand on the project side and imported with `assetPack`'s
  `flatten` (the wrapper does not create them). A common CLI for creating plain, unencrypted xp3 archives is
  planned on the krkrz_dev side
- Flatpak when there is demand
- macOS (.app) / Windows / Xbox are being investigated, aligning them with wrappers that share the
  `cmake` / `assetPack` format of `*-config.json`

## Related

- [krkrz_linux](https://github.com/wamsoft/krkrz_linux) — the README lists the configuration fields
- [Steam Deck Hardware Testing (pre-release check)](steamdeck.md)
- [Command-Line Options](../../guide/CommandLine.md) — `-datapath` / `-orgname` / `-appname` and the `.cf` format
