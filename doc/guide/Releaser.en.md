---
source_hash: fd233c30d20b
---

# Releaser

## About the Releaser

The Releaser (`krkrrelease`) is a tool that builds the executable you distribute to end users from a Kirikiri Z executable.
It performs the following steps, in this order.

1. Copies the base executable and renames it to your product's name (the original file is not modified)
2. Embeds command-line options in the executable
3. Replaces the icon and version information (product name, copyright notice, and so on)
4. Rewrites the security settings (`forcedataxp3` and others)
5. Places the project's xp3 archive next to the executable, or binds it to the executable (if you specify a folder, the xp3 is created on the spot)
6. Creates a digital signature (`.sig`)

The Releaser is one of the [standard tools](Tools.md), but it is **Windows only** (because it rewrites the resources of a Windows executable).
It works on Windows Kirikiri Z executables (both the WINVER and SDL builds).

> **Note:**
> The Kirikiri 2 Releaser (krkrrel.exe) also created xp3 archives. In Kirikiri Z, xp3 archive creation is split out into the [xp3 archive tool (krkrxp3)](Xp3Tool.md). The Releaser still creates an xp3 with the same processing internally when you specify a folder.
>
> Kirikiri 2 executables had areas for writing options and signatures (`XOPT_EMBED_AREA_` and others), but Kirikiri Z executables do not. Kirikiri Z stores embedded options as Windows resources. For this reason, the Kirikiri 2 Releaser cannot embed options in a Kirikiri Z executable.

## Release settings

Release settings are saved in a JSON file (for example `release.json`). The GUI and the command line use the same settings file.
Relative paths in the settings file are resolved against the folder containing the settings file.

```json
{
 "exe": "krkrz64.exe",
 "output": "release/game.exe",
 "setOptions": true,
 "options": "; 起動オプション\ndebugwin=no\n",
 "icon": "game.ico",
 "version": {
  "FileDescription": "ゲームの名前",
  "ProductName": "ゲームの名前",
  "CompanyName": "制作者",
  "LegalCopyright": "(C) 2026 制作者",
  "FileVersion": "1.0.0.0",
  "ProductVersion": "1.0.0.0"
 },
 "security": { "forcedataxp3": 1, "acceptfilenameargument": 0 },
 "dataMode": "copy",
 "data": "data",
 "rpf": "",
 "dataName": "data.xp3",
 "signKey": "private.txt"
}
```

- **exe**  
  The base Kirikiri Z executable. Specify one with nothing appended to it (an executable with a bound xp3 or an Authenticode signature cannot be used as the base).
- **output**  
  The executable to create. You can name it freely.
- **setOptions / options**  
  When `setOptions` is true, `options` is embedded as command-line options. The format is the same as a `.cf` file: one `name=value` per line. Lines starting with `;` are comments.
  
  Embedded options have the lowest priority. A `.cf` file with the same name as the executable (`game.cf` for `game.exe`) and options given on the command line take precedence ([command-line options](CommandLine.md)).
- **icon**  
  The icon (`.ico`) to use instead. Icon files containing multiple sizes can be used. If empty, the icon is left unchanged.
- **version**  
  Version information strings (shown in the file's Properties in Explorer). Empty entries are left unchanged. If you write a version in the form `1.2.3.4` in `FileVersion` and `ProductVersion`, the numeric version is rewritten to match.
- **security**  
  List only the security settings you want to change.
  
  - `forcedataxp3`: when set to 1, the project is loaded only from xp3 archives (data.xp3, data.exe, or one bound to the executable), and the data folder and the like are no longer used
  - `acceptfilenameargument`: when set to 0, command-line arguments are not treated as the project folder
  - `disablemsgmap` and `disableapplock` (plus `disabled3d9` for the WINVER build) can also be changed
- **dataMode / data**  
  How the project is handled. In `data`, specify an xp3 file or the project folder (for a folder, the Releaser creates the xp3).
  
  - `none`: no data is handled
  - `copy`: places it in the same folder as the executable, named `dataName` (default `data.xp3`). Kirikiri automatically loads the data.xp3 in the executable's folder as the project
  - `bind`: appends it to the end of the executable, so the game can be distributed as a single file
- **rpf**  
  The profile (`.rpf`) used when creating an xp3 from a folder. If empty, the folder's `default.rpf` is used if present; otherwise the default classification is used ([xp3 archive tool](Xp3Tool.md)).
- **signKey**  
  The private key used for signing (created with the [key and signing tool](SignTool.md)). When specified, `.sig` files are created for the executable and for an xp3 placed next to it. If empty, nothing is signed.

> **Note:**
> If an embedded option value contains Japanese or other non-ASCII text, the Releaser rewrites it into the form `name="\x65e5\x672c..."` (TJS string escapes) before embedding. This is because different kinds of Kirikiri executables handle the character encoding of option lines differently.

## Using the GUI

Launching `krkrrelease` opens the release settings screen (if you pass a settings file as an argument, it opens with that file loaded).

- «開く…» (Open...) / «保存» (Save) read and write the settings file
- When you choose «元にする exe» (Base exe) (or press «調べる» (Inspect)), the screen shows the kind of executable (WINVER build / SDL build), its current security settings, and its embedded options, and lists that executable's items in the security settings section
- Fill in each field and press «作成する» (Create) to make the release. The steps performed and the list of created files are shown

## Using the command line

```
krkrrelease --cli run      release.json [--force]
krkrrelease --cli info     krkrz64.exe
krkrrelease --cli template release.json [--exe=krkrz64.exe]
```

- **run**: makes a release according to the settings file. If the output already exists, overwrite it with `--force`
- **info**: shows the kind of executable, the security settings, whether it has an icon, the version information, and the embedded options
- **template**: writes out a template settings file

`--json` outputs the results as JSON. The exit code is 0 = success, 2 = failure.

## Processing order and caveats

The Releaser processes in this order: rewriting resources → security settings → binding xp3 → signing.
There are reasons for this order.

- Rewriting Windows resources discards any data appended to the end of the executable (a bound xp3 or an Authenticode signature). For this reason, resources are rewritten before binding
- A signature (`.sig`) covers the whole file, so changing the executable after signing makes the signature no longer match

If you modify the executable after building it with the Releaser, for example by adding an Authenticode signature or applying a distribution service's DRM, regenerate the `.sig` afterwards with the [key and signing tool](SignTool.md).

## Binding xp3 to the executable

When an xp3 archive is bound to the end of the executable, Kirikiri Z loads it as the project (the Windows build, and the SDL build on Windows / Linux).
For the search order, see «プロジェクトフォルダの決定順序» (how the project folder is determined) in [Startup](Startup.md).

The Releaser's `bind` appends the xp3 archive to the end of the executable, starting at a 16-byte boundary.
To bind to a Linux executable, append it by hand instead of using the Releaser (for example: `cat krkrz data.xp3 > game`; if the executable's size is not a multiple of 16, pad with zeros in between to align it).
