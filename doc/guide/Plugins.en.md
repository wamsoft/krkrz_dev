---
source_hash: f8981ae38180
---

# About Plugins

## What Are Plugins

Plugins connect to Kirikiri and are used to extend its functionality.

Currently, there are three kinds of plugins that Kirikiri can use:

- Susie Plug-ins (image loading and archive access)
- Plugins that extend the formats WaveSoundBuffer can play
- Other Kirikiri-specific plugins



To use a plugin, you need to connect it to the Kirikiri engine with the [Plugins.link](../reference/Plugins.md#link) method.

## Plugin Search

The [Plugins.link](../reference/Plugins.md#link) method looks for the specified plugin in the following order.

1. The folder containing the Kirikiri engine
2. The plugin folder (plugin64 on 64-bit Windows) in the folder containing the Kirikiri engine
3. The auto search paths

### Plugin Folder Names (by Platform) {#plugin-folder}

| Platform | Plugin folder |
|---|---|
| Windows 64-bit (WINVER / SDL) | `plugin64/` |
| Windows 32-bit | `plugin/` |
| Linux / other desktops (including 64-bit) | `plugin/` |
| macOS | The folder containing the executable (`Contents/MacOS` in the app bundle) |
| Android | None (plugins are statically linked) |

!!! warning "Important (change in 2026-10)"
    `plugin64/` is used **only by the 64-bit Windows build**. On Linux and other platforms, `plugin/` is searched even in 64-bit builds. This follows the same rule as the CMake install destination (`plugin/`), and the behavior on Linux has not changed.

    - On Linux and other platforms, if there is a `plugin64/` folder next to the executable, a warning saying it will not be searched is logged at startup. Move its contents to `plugin/`.
    - You can check which folder is actually searched in the `pluginPath:` line of the startup log (SDL build).
    - Only for the **64-bit Windows SDL build** built with gcc / clang (MinGW, etc.), the search location has changed from `plugin/` to `plugin64/` (the MSVC build has always used `plugin64/`).

If an auto search path is somewhere that cannot be accessed as a local file, such as inside an archive, Kirikiri tries to extract the plugin into **the folder containing the Kirikiri engine**. This can cause problems, so it is **strongly recommended** to put plugins either in "the folder containing the Kirikiri engine" or in "the plugin folder in the folder containing the Kirikiri engine".


Putting them in the plugin/plugin64 folders is also important for loading the right 32-bit or 64-bit plugins on Windows.

In addition, Kirikiri's configuration tools ( Releaser and the -userconf option ) look for plugins to collect the embedded option information of each plugin, in the following order.

1. The folder containing the Kirikiri engine
2. The plugin folder in the folder containing the Kirikiri engine

The SDL build's -userconf reads `<plugin name>.options.json` next to each plugin from "the folder containing the Kirikiri engine" and from "the plugin folder".

Kirikiri's configuration tools do not search the auto search paths, so plugins that have configuration items must be placed in "the folder containing the Kirikiri engine" or "the plugin folder in the folder containing the Kirikiri engine".

## Automatic Plugin Loading

Kirikiri can automatically find plugins and load them at startup. To have a plugin loaded automatically, change its extension from dll to tpm.

At startup (just before running startup.tjs), Kirikiri looks for files with the tpm extension in the following folders and loads them automatically as plugins.

- The folder containing the Kirikiri engine
- The plugin folder (plugin64 on 64-bit Windows) in the folder containing the Kirikiri engine

Kirikiri sorts the found plugins by name in ascending order and loads them in that order. For example, aaa.tpm is loaded before aab.tpm. The order depends only on the plugin names, not on the folders they are in (even if z.tpm is in the same folder as the Kirikiri engine, a.tpm in the plugin folder is loaded first). If you want to control the loading order, you need to change the plugin file names.

## Creating Plugins

The Kirikiri source includes the source of the bundled plugins, so use them as a reference.

At this stage, the specification for "other Kirikiri-specific plugins" is **not finalized**. Even if the specification changes in the future, source-level compatibility should be maintained, so even if binary compatibility is lost, plugins should work again after being rebuilt against the Kirikiri engine.

## About Susie Plug-ins

You can use plugins for "Susie32", the image viewer by Takechin.

Both the 00IN type (image plugins) and the 00AM type (archive plugins) can be used, with the following limitations and Kirikiri-specific behaviors.

- Kirikiri determines the image format by extension, so it cannot handle images whose extension differs from the proper one ( the one returned by the GetPluginInfo function ) ( archives are checked against all supported formats, so a different extension is OK )
- 32bpp bitmaps are treated as bitmaps with an alpha channel
- Some bitmap formats are not accepted (such as RLE-compressed ones or ones with BITFIELDS specified )
- Image loading and archive access through Susie plugins are much slower than the image formats and xp3 archives Kirikiri handles natively
- Files inside archives are extracted into memory, so this is not suitable for large files
- Archives inside archives are not supported
- Mac binary is not supported

Also, some plugins that do not fully conform to the Susie plug-in specification do not work well with Kirikiri.

## Plugins Bundled with Kirikiri

The following is a list of plugins bundled with Kirikiri Z by default. The source code of each plugin is maintained in its own repository under [wamsoft](https://github.com/wamsoft).

For plugins that add classes, see the page for each class in the reference; for plugins that extend existing classes, see the "Plugin extensions" section on the page of the extended class.

### All Platforms

| Plugin | Description |
|---|---|
| **AlphaMovie** | Adds the [AlphaMovie](../reference/AlphaMovie.md) class, which plays movies with an alpha channel ( .amv ). |
| **clipfile** | Adds the [CLIP](../reference/CLIP.md) / [CLIPWriter](../reference/CLIPWriter.md) classes, which load, edit, and save CLIP STUDIO PAINT files ( .clip ). You can also load layer images directly with `clip://`. |
| **csvParser** | Adds the [CSVParser](../reference/CSVParser.md) class, which parses CSV files. |
| **expat** | Adds the [XMLParser](../reference/XMLParser.md) class, which parses XML. |
| **extrans** | Registers seven additional transitions: wave / mosaic / turn / rotatezoom / rotatevanish / rotateswap / ripple. For details, see [Transitions](Transition.md). |
| **extNagano** | Registers twelve additional transitions: 3duniversal / blurfade / scanline / zoomfade / rgbfade / spin / flutter / book / imagewipe / honeyturn / morphing / multiripple. For details, see [Transitions](Transition.md). |
| **getSample** | Adds a method to [WaveSoundBuffer](../reference/WaveSoundBuffer.md) that gets the sample values of the sound being played. |
| **json** | Adds JSON reading and writing ( evalJSON / saveJSON, etc. ) to [Scripts](../reference/Scripts.md). |
| **KAGParserEx** | Adds the [KAGParser](../reference/KAGParser.md) class, which parses KAG scenarios ( replaces the built-in version with an extended one ). |
| **krkr_richtext** | Adds the [RichText](../reference/RichText.md) classes, which draw multilingual, styled rich text, and [Layer](../reference/Layer.md) extensions. |
| **layerExAreaAverage** | Adds high-quality shrink copying using area averaging to [Layer](../reference/Layer.md). |
| **layerExBTOA** | Adds a method to [Layer](../reference/Layer.md) that converts the blue component into alpha values. |
| **layerExImage** | Adds image processing such as brightness / contrast / hue / saturation adjustment and noise to [Layer](../reference/Layer.md). |
| **layerExLongExposure** | Adds a long-exposure-like effect ( accumulating frames ) to [Layer](../reference/Layer.md). |
| **layerExRaster** | Adds a raster scroll effect to [Layer](../reference/Layer.md). |
| **layerExSave** | Adds asynchronous saving of layer images ( PNG / TLG5 ) to [Layer](../reference/Layer.md) / [Window](../reference/Window.md). |
| **layerExVector** | Adds vector drawing such as SVG via thorvg to [Layer](../reference/Layer.md) ( [GdiPlus](../reference/GdiPlus.md)-compatible API ). |
| **lineParser** | Adds the [LineParser](../reference/LineParser.md) class, which parses text line by line. |
| **minizip** | Adds the [Zip](../reference/Zip.md) / [Unzip](../reference/Unzip.md) classes, which read ZIP archives ( zip:// auto search path ) and create them. |
| **psdfile** | Adds the [PSD](../reference/PSD.md) class, which loads, edits, and saves Photoshop PSD files. You can also load layer images directly with `psd://`. It can also composite from the layer states (including adjustment layers and layer effects), draw individual layers, and rasterize shapes / paths. |
| **saveStruct** | Extends saveStruct of Array / Dictionary so you can specify the output encoding, such as UTF-8 ( see [Scripts](../reference/Scripts.md) ). |
| **scriptsEx** | Adds script execution utilities to [Scripts](../reference/Scripts.md). |
| **shrinkCopy** | Adds fast shrink copying to [Layer](../reference/Layer.md). |
| **sigcheck** | Adds background verification of file signatures to [Window](../reference/Window.md). |

#### OpenGL ES Rendering

Plugins that render with GLES ( ANGLE/glad ). The target GL context is supplied by the Kirikiri engine's `OGLDrawDevice` or, on Windows, by `GLESAdaptor` in `krkrgles`.

| Plugin | Description |
|---|---|
| **krkreffekseer** | Adds the `EffekseerDevice` / `EffekseerEffect` / `EffekseerPlayer` classes, which draw [Effekseer](https://effekseer.github.io/) effects ( .efk / .efkefc / .efkzip ) to a host-supplied GL context. |
| **krkrlive2d** | Adds the `Live2DDevice` / `Live2DModel` / `Live2DPlayer` / `Live2DMatrix` classes, which play and draw Live2D Cubism models. **Because it requires the Live2D Cubism Core, it is built only when the `CUBISM_SDK` environment variable is set** ( the driver-side CMake refers to `$CUBISM_SDK/Core` ). |
| **krkrgles** | Adds the `GLESAdaptor` / `GLESTexture` classes, which pull the results rendered with OpenGL ES ( via ANGLE/EGL ) into a [Layer](../reference/Layer.md). It includes a post-effect mechanism that runs entirely on the GPU. **It creates the EGL/ANGLE context from `Window.HWND`, so it is Windows only** ( on macOS / Linux, use the engine's `OGLDrawDevice` for the GL context ). |

### Windows Only ( WINVER Build )

These depend on the Win32 API, so they are currently available only in the WINVER build.

| Plugin | Description |
|---|---|
| **addFont** | Dynamically adds private fonts ( .ttf / .otf ) ( the engine's [System.addFont](../reference/System.md#addfont) can do the same ). |
| **binaryStream** | Adds the [BinaryStream](../reference/BinaryStream.md) class, which reads and writes files at the binary level. |
| **fpslimit** | Limits how often the main loop runs ( now replaceable with the engine's -contfreq option ). |
| **fstat** | Adds getting file sizes, modification times, etc. to [Storages](../reference/Storages.md). Basic file operations ( `fstat` / `getTime` / `copyFile` / `dirlist`, etc. ) are also in the engine and available in every build. Loading this plugin replaces `fstat` / `getTime` / `currentPath` / `dirlistEx` with versions that also return creation / access times and attributes, and adds Win32-specific operations such as setting attributes. |
| **gamepad** | Adds the [Pad](../reference/Pad.md) class, which handles gamepads directly. |
| **httprequest** | Adds the [HttpRequest](../reference/HttpRequest.md) class, which performs HTTP communication. |
| **layerExDraw** | Adds the [GdiPlus](../reference/GdiPlus.md) classes, which draw shapes and text with GDI+. |
| **memfile** | Adds in-memory virtual files ( mem:// ) to [Storages](../reference/Storages.md). |
| **menu** | Adds the [MenuItem](../reference/MenuItem.md) class, which builds window menus. |
| **messenger** | Adds WM_COPYDATA-based message exchange with external processes to [Window](../reference/Window.md). |
| **msgreceiver** | Adds an entry point for external control ( receiving WM_COPYDATA ) ( deprecated; use messenger instead ). |
| **process** | Adds the [Process](../reference/Process.md) class, which launches and monitors external processes. |
| **shellExecute** | Adds opening files / URLs with their associated applications to [System](../reference/System.md). |
| **stdio** | Adds access to standard input and output to [System](../reference/System.md). |
| **systemEx** | Adds utilities such as getting OS information to [System](../reference/System.md). Environment variables and URL encoding ( `readEnvValue` / `urlencode`, etc. ) are also in the engine, and the engine versions are used. What remains in this plugin are Win32-specific features such as the registry, OS version, known folders, and the DLL search path. |
| **tftSave** | Adds saving of pre-rendered font data to [System](../reference/System.md) / [Layer](../reference/Layer.md). |
| **varfile** | Adds var:// access, which references TJS variable space ( octets in dictionaries ) as files. |
| **win32dialog** | Adds the [WIN32Dialog](../reference/WIN32Dialog.md) class, which builds native Win32 dialogs. |
| **win32ole** | Adds the [WIN32OLE](../reference/WIN32OLE.md) / [ActiveX](../reference/ActiveX.md) / [JScriptHost](../reference/JScriptHost.md) classes, which handle OLE Automation / ActiveX. |
| **windowEx** | Adds various window operation extensions to [Window](../reference/Window.md) / [System](../reference/System.md) / [Console](../reference/Console.md), etc. Maximizing / rectangles / extended events / monitor information are also in the engine and available in every build ( loading this plugin overrides them with the plugin versions ). Scheduled for deprecation. |
| **windowExProgress** | Adds to [Window](../reference/Window.md) a window display with a progress bar that stays visible even while execution is blocked. |
