---
source_hash: 75511afdf2fa
---

# Shared settings of the platform wrappers (cmake / assetPack)

Builds for the browser, Android, iOS, Linux and Microsoft GDK are done in separate "wrapper"
repositories (krkrz_web / krkrz_android / krkrz_ios / krkrz_linux / krkrz_gdk). Each wrapper reads
one settings file per title (`app-config.json` and so on), and the following parts of it have the
same format and behave the same way in every wrapper:

- **`cmake`** — which plugins to build in
- **`assetPack`** — where to collect the game's data and assets from, and where to place them in the distribution
- **`${...}` expansion** of path strings and how relative paths are resolved

This page describes those shared parts. For the platform-specific keys (application ID, signing,
icons and so on), see the README of each wrapper.

Because the format is shared, you can put the settings files for every platform side by side in
one project folder and reuse the same `data/`.

```
mygame/                     ← PROJECT_DIR
├── data/                   ← game data (shared by all platforms)
├── archive/                ← xp3 archives you build yourself (optional)
├── app-config.json         ← krkrz_android
├── ios-config.json         ← krkrz_ios
├── linux-config.json       ← krkrz_linux
├── gdk-config.json         ← krkrz_gdk
└── web-config.json         ← krkrz_web
```

## Support in each wrapper

| Wrapper | Settings file | `cmake` | Where `assetPack` places files | Main keys specific to the wrapper |
|---|---|---|---|---|
| [krkrz_android](https://github.com/wamsoft/krkrz_android) | `app-config.json` | Yes | `assets/` of the APK | `resOverride` (overriding res), `padPacks` (Play Asset Delivery) |
| [krkrz_ios](https://github.com/wamsoft/krkrz_ios) | `ios-config.json` | Yes (all plugins linked statically) | Directly under the app bundle | `graphics` (gles / metal), `icon`, `infoPlist` |
| [krkrz_linux](https://github.com/wamsoft/krkrz_linux) | `linux-config.json` | Yes (plus `buildType` / `options`) | The executable's folder | `exeName`, `orgName` / `appName`, `desktop` |
| [krkrz_gdk](https://github.com/wamsoft/krkrz_gdk) | `gdk-config.json` | Yes (all plugins linked statically, plus `options`) | The executable's folder | `targets`, `identity`, `gpuShaderDir` |
| [krkrz_web](https://github.com/wamsoft/krkrz_web) | `web-config.json` | — (a shared binary, not built per title) | `gamedata/` (served through `web://`) | `sources[].delivery` (prefetch), `lowercase`, `args` |

## Path expansion

Path strings in the settings file can contain `${...}`.

| Syntax | Expands to |
|---|---|
| `${PROJECT_DIR}` | The absolute path of the project folder (the folder that contains the settings file). When it is not specified, the root of the wrapper repository (so the bundled sample works) |
| `${BUILD_SYSTEM_DIR}` | The absolute path of the wrapper repository's root. Use it to point at plugins and the like that ship with the wrapper |
| `${KRKRZ_BASE}` and other environment variables | The value of the process's environment variable. **An undefined variable expands to an empty string** (`${KRKRZ_BASE}/foo` becomes `/foo`) |

- A path that is still relative after expansion is resolved **relative to `${PROJECT_DIR}`**
- Expansion applies to keys that hold paths (`assetPack.baseFolder`, `assetPack.sources[].from`,
  `cmake.pluginFolders[]` and so on). Plugin names (`cmake.plugins` and so on) are not expanded

## cmake — plugins to build in

```jsonc
"cmake": {
    "pluginFolders": [
        "${KRKRZ_BASE}/krkrz_dev/src/plugins",
        "${PROJECT_DIR}/plugins"
    ],
    "plugins": ["json", "csvParser", "saveStruct"],
    "staticPlugins": ["json"]
}
```

| Key | Description | CMake variable |
|---|---|---|
| `pluginFolders` | Where to look for plugin folders. Relative paths (based on `${PROJECT_DIR}`), absolute paths and `${...}` can be used | `TVP_PLUGIN_FOLDERS` |
| `plugins` | Plugins to build in (folder names) | `TVP_PLUGINS` |
| `staticPlugins` | Plugins to link statically into the engine (a subset of `plugins`) | `TVP_PLUGINS_STATIC` |

- iOS and GDK link every plugin statically, so `staticPlugins` is not needed there
- To use plugins inside the wrapper (`${BUILD_SYSTEM_DIR}/...`), write `${BUILD_SYSTEM_DIR}` explicitly.
  Relative paths are based on the project folder, so they are not found if they do not exist there
- The CMake file made from these settings is generated in the build folder. Editing it directly is
  overwritten by the next build, so make changes in the settings file
- Without `cmake`, no plugins are built in

For choosing plugins (including how folder names relate to CMake target names), see the
[plugin list](../../guide/Plugins.md) of krkrz_dev.

## assetPack — collecting assets

Collects data that lives outside the wrapper, such as your project folder, at build time and places
it in the distribution.

```jsonc
"assetPack": {
    "baseFolder": "${PROJECT_DIR}",
    "sources": [
        {
            "comment": "Place the game data with its folder structure",
            "type": "mirror",
            "from": "data",
            "exclude": ["**/*.bak", "**/*.psd"]
        },
        {
            "comment": "Put the xp3 archives you built at the root",
            "type": "flatten",
            "from": "archive",
            "include": ["*.xp3"]
        }
    ]
}
```

| Key | Required | Description |
|---|---|---|
| `baseFolder` | Required when a relative `from` is used | The base for relative `from` paths. Relative paths (based on `${PROJECT_DIR}`), absolute paths and `${...}` can be used |
| `transfer` | | `"copy"` (default) / `"hardlink"` (see below). Whether it is supported depends on the wrapper; see its README |
| `sources` | Yes | An array of collection rules. **Processed in the order written** |
| `sources[].type` | Yes | `"mirror"` / `"flatten"` |
| `sources[].from` | Yes | The folder to collect from. A relative path is based on `baseFolder`; an absolute path is used as is |
| `sources[].include` | | An array of patterns for files to collect (for example `"**/*.png"`). Default `["**/*"]` |
| `sources[].exclude` | | An array of patterns for files to leave out. Default `[]` |
| `sources[].to` | | The destination folder (relative to the root of the distribution's assets). See below when omitted |

Unknown keys such as `comment` are ignored, so you can use them to note what each rule is for.

### type

- **`mirror`** — places the files under `from` below `to`, keeping the folder structure
- **`flatten`** — drops the folder structure and places the files directly under `to` by file name only

Destination when `to` is omitted:

| Condition | Destination |
|---|---|
| `mirror` with a relative `from` | The same name as `from` (`from: "data"` → `data/...`) |
| `mirror` with an absolute `from` | The last folder name of `from` |
| `flatten` | Directly under the root |

To expand directly under the root, write `"to": ""` explicitly.

The patterns (`include` / `exclude`) are Ant-style globs. `*` matches any string that does not
contain a folder separator, and `**` matches zero or more folders (`**/*.psd` is every .psd at any depth).

### Conflicts at the same destination (first wins)

When several `sources` (or separate folders of a `flatten`) try to write to the same destination,
**the file that appears first is used**, and later ones are skipped with a warning. To override a
file on your side, write its source earlier; it then takes precedence over the same-named file in
a later source.

The order relative to the files the wrapper places itself (the engine files, files generated from
the settings and so on) differs by wrapper.

- **krkrz_linux / krkrz_gdk** — place the engine files and generated files first, and then process
  `assetPack`. So a file with the same name cannot be overridden through `assetPack`
- **krkrz_android** — the engine's required resources (`src/core/resource`) are also written as one
  item of `sources`. Write the `resource/` of your project folder before it to replace individual files

### Incremental updates

When run again, only what has changed is updated. Files removed from the source are removed from the
destination too, and files whose content has not changed are not copied again (their timestamps are
kept as well, so later steps are not run needlessly).

### transfer: hardlink

When the source and the destination are on the same drive (the same file system), `"transfer": "hardlink"`
creates hard links instead of copies. Even several GB of assets use almost no disk space and take
almost no time.

- Editing a source file is reflected in the destination immediately (they are the same file).
  If you rewrite the sources before building, use the default `copy`
- Files that cannot be hard-linked (another drive, a network location, FAT and so on) automatically
  fall back to copying
- No administrator rights are needed on Windows (NTFS). Symbolic links are not used

## Related

- The README of each wrapper — platform-specific keys and build steps
- [Linux distribution package](linux_package.md) — how krkrz_linux's distribution format is designed
