---
source_hash: 291419958a82
---

# Windows Distribution Packages (krkrz_windows)

This describes how to bundle the Kirikiri Z engine with your game data into a distributable package for Windows.
The tool is the wrapper repository [krkrz_windows](https://github.com/wamsoft/krkrz_windows). Like krkrz_linux / krkrz_android / krkrz_ios / krkrz_web,
it references krkrz_dev as the engine via `KRKRZ_BASE` and handles only the Windows-specific build and
packaging. The list of settings and the build steps are in the krkrz_windows README.

Packages for the Microsoft Store / Xbox (msixvc) are handled by krkrz_gdk and are not covered here.

## Distribution formats and policy

| Format | Main destinations | krkrz_windows |
|---|---|---|
| Folder / zip | Steam depots, itch.io, DLsite, your own site | ✅ produced |
| Installer (Inno Setup) | Your own site, boxed editions | ✅ produced (optional) |
| MSI / MSIX | — | Not used (MSI is meant for company-wide deployment and is heavy; MSIX outside the Store needs a trusted certificate and redirects writes to AppData, which affects where saves go) |

As with the Linux version, **the "run as is" folder is the real product, and the zip and the installer are
repackagings of it**. Steam takes the folder itself.

- Only **x64** is supported (x86 is not handled; arm64 is on hold until it can be tested on real hardware)
- The default is the **SDL build**, which matches Linux / macOS / consoles in rendering, text and behavior.
  Existing titles that rely on Win32-only plugins (windowEx / layerExDraw / win32dialog and so on) or on how
  GDI draws text can choose the WINVER build with `variant: "win"`
- The MSVC runtime and the vcpkg libraries are linked statically, so the VC++ redistributable is not needed

## Usage

Run from a Visual Studio 2022 developer shell (x64).

```bat
set KRKRZ_BASE=D:\work                    & rem the parent folder of krkrz_dev
cd D:\work\krkrz_windows
python tools\krkrz_windows.py all         & rem the sample (core demos)
set PROJECT_DIR=D:\work\mygame
python tools\krkrz_windows.py all         & rem your own game
```

`all` runs `build` (engine, plugins, standard tools) → `stage` (make the exe with the releaser and assemble the
package folder) → `sign` (signing) → `package` (zip / installer). Output goes under `${PROJECT_DIR}/build/windows/`.

- `package/<exeName>/` … the folder that runs as is
- `dist/<exeName>-<version>-windows-x64.zip`
- `dist/<exeName>-<version>-windows-x64-setup.exe` (when `installer` is in `package.formats`)

The game is defined in `${PROJECT_DIR}/windows-config.json`. `cmake` (plugin configuration) and `assetPack`
(asset import) use the same format as the other wrappers ([Shared settings of the platform wrappers](platform_config.md)).

!!! note "Keep the project folder shallow"
    Some libraries fetched during the build contain test files with long names. If the project folder is deep,
    configure fails at the Windows path length limit. Put it somewhere shallow, such as `D:\work\mygame`.

## The exe is made by the releaser

The distributed exe is made with the standard releaser tool (`krkrrelease`). The wrapper only builds the
releaser's settings from `release` in `windows-config.json` and calls it, instead of reimplementing the same work.

- Icon, version information (FileVersion / ProductVersion come from `version`), embedded options, security settings
- Data is `none` (place `data/` and so on with `assetPack`) / `copy` (data.xp3 next to the exe) / `bind`
  (appended to the exe). Passing a folder creates the xp3
- With a private key, Kirikiri signatures (`.sig`) are added to the exe and the xp3

## Save data location

On Windows the engine's default is `savedata` next to the exe, which cannot be written when the game is placed
somewhere read-only (such as Program Files). The wrapper builds `-datapath` from `saveData`, embeds it in the exe,
and **defaults to the Documents folder**.

| `saveData.location` | Location | Use |
|---|---|---|
| `documents` (default) | Documents\\`<folder>` | Players can see where saves are. Same place for the zip and the installer |
| `appdata` | AppData\\Roaming\\`<folder>` | When saves should stay out of sight. Steam Cloud Windows root `WinAppDataRoaming` |
| `exe` | `savedata` next to the exe | Compatibility with existing titles |

- Do not change the location between the zip and the installer of the same title (saves would seem to vanish
  when a player switches)
- To check the embedded location, start the distributed exe with `-printdatapath`
  (both the WINVER and SDL builds; in the SDL build it is the last line, after the startup log)

## Installer

The installer is made with Inno Setup (6.3 or later; verified with 7). Without Inno Setup, only the installer is
skipped with a warning (the zip is still made).

- **The default is a per-user installation**. No administrator rights are needed and no UAC prompt appears
  (`%LOCALAPPDATA%\Programs\<name>`). `installMode` can switch to an all-users installation (Program Files)
  or let the player choose during installation
- Screens in Japanese and English. A Start menu shortcut, an optional desktop shortcut, and an uninstaller
  (listed in Windows "Apps") are installed
- **Uninstalling does not delete save data** (Inno Setup only removes the files it installed)
- With the same `appId` (GUID), Windows treats it as the same app, so a newer version can be installed over the
  old one. **Once you choose the `appId` for a title, never change it**
- The wrapper rejects an all-users installation combined with "save next to the exe", because saving would fail

## Signing and the file corruption check

There are two kinds of signatures.

| Signature | Purpose | How |
|---|---|---|
| Authenticode | The "publisher" shown by Windows; fewer SmartScreen warnings | A code signing certificate. The wrapper's `sign` applies it with `signtool`; the certificate is passed through environment variables |
| Kirikiri `.sig` | Detecting modified or damaged files (the sigcheck plugin, the file corruption check tool) | A key made with `krkrsign`. The releaser adds it |

Authenticode rewrites the exe, so the order is **Authenticode → remake the `.sig` files**. The wrapper's `sign`
keeps this order. DLLs the vendor has already signed (such as `d3dcompiler_47.dll`) are not re-signed. Without a
timestamp server, signatures become invalid when the certificate expires, so specify one for releases.

Titles with `.sig` files can ship the standard file corruption check tool (`krkrcheck`) under any name. The public
key and the window texts go into an .ini with the same name, and players just start the tool to check whether the
files in its folder are damaged (used the same way as the Kirikiri 2 "file corruption check tool").
In the installer it becomes the optional component "File corruption check".

## Verified (2026-10-27)

- For both the SDL and WINVER builds (x64), the sample (core demos) was built and zipped, and all 24 `-demotest`
  scenes passed from the extracted zip, with saves going to the Documents folder
- Installer (verified with the WINVER build): per-user installation, the Start menu shortcuts, the entry in "Apps",
  running and checking files in the installed folder, and uninstalling removes the app while keeping save data
- Check tool: "all OK" as shipped, and "damaged" after changing one byte of data.xp3
- Signing (with a test certificate): Authenticode on the exe, DLLs, check tool and installer; the check stays OK
  with the remade `.sig` files, and the signed exe starts

## Related

- [krkrz_windows](https://github.com/wamsoft/krkrz_windows) — the README lists the configuration fields
- [Shared settings of the platform wrappers](platform_config.md) — the `cmake` / `assetPack` / `${...}` expansion formats
- [Linux distribution packages](linux_package.md) — krkrz_linux
- [Command-line options](../../guide/CommandLine.md) — `-datapath` / `-printdatapath`
- [Kirikiri Z specific anti-cracking measures](anti_cracking.md)
