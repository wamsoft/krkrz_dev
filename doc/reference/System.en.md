# System

The System class gets and sets information about the Kirikiri engine and the environment it is running in. You cannot create objects of this class.

## Members

### Properties

- [versionString](#versionstring)
- [versionInformation](#versioninformation)
- [eventDisabled](#eventdisabled)
- [graphicCacheLimit](#graphiccachelimit)
- [platformName](#platformname)
- [osName](#osname)
- [exePath](#exepath)
- [resourcePath](#resourcepath)
- [replWebURL](#replweburl)
- [personalPath](#personalpath)
- [appDataPath](#appdatapath)
- [dataPath](#datapath)
- [exeName](#exename)
- [title](#title)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [desktopLeft](#desktopleft)
- [desktopTop](#desktoptop)
- [desktopWidth](#desktopwidth)
- [desktopHeight](#desktopheight)
- [exitOnWindowClose](#exitonwindowclose)
- [exceptionHandler](#exceptionhandler)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [onJoypadChange](#onjoypadchange)
- [drawThreadNum](#drawthreadnum)
- [savedGamesPath](#savedgamespath)
- [exeBits](#exebits)
- [osBits](#osbits)
- [exitOnNoWindowStartup](#exitonnowindowstartup)
- [isGeneric](#isgeneric)
- [isWindows](#iswindows)
- [licenseText](#licensetext)
- [openGLESVersion](#openglesversion)
- [processorNum](#processornum)
- [renderStats](#renderstats)
- [texUploadUsePBO](#texuploadusepbo)
- [touchDevice](#touchdevice)
- [platformTag](#platformtag)
- [systemLanguage](#systemlanguage)
- [uiLanguage](#uilanguage)
- [uiLanguageCandidates](#uilanguagecandidates)
- [padButtonMapping](#padbuttonmapping)
- [padStyle](#padstyle)
- [buildVariantName](#buildvariantname)
- [padAxisLeftX](#padaxisleftx)
- [padAxisLeftY](#padaxislefty)
- [padAxisRightX](#padaxisrightx)
- [padAxisRightY](#padaxisrighty)
- [padAxisLeftTrigger](#padaxislefttrigger)
- [padAxisRightTrigger](#padaxisrighttrigger)
- [padEnabled](#padenabled)
- [replActive](#replactive)

### Methods

- [terminate](#terminate)
- [exit](#exit)
- [addContinuousHandler](#addcontinuoushandler)
- [removeContinuousHandler](#removecontinuoushandler)
- [inform](#inform)
- [confirm](#confirm)
- [inputString](#inputstring)
- [choice](#choice)
- [getTickCount](#gettickcount)
- [getKeyState](#getkeystate)
- [registerHotKey](#registerhotkey)
- [unregisterHotKey](#unregisterhotkey)
- [shellExecute](#shellexecute)
- [readRegValue](#readregvalue)
- [getArgument](#getargument)
- [setArgument](#setargument)
- [toActualColor](#toactualcolor)
- [createAppLock](#createapplock)
- [createUUID](#createuuid)
- [assignMessage](#assignmessage)
- [doCompact](#docompact)
- [touchImages](#touchimages)
- [showVersion](#showversion)
- [dumpHeap](#dumpheap)
- [captureScreen](#capturescreen)
- [renderStatsReset](#renderstatsreset)
- [addFont](#addfont)
- [clearGraphicCache](#cleargraphiccache)
- [getJoypadType](#getjoypadtype)
- [nullpo](#nullpo)
- [system](#system)
- [getSystemAllocatorInfo](#getsystemallocatorinfo)
- [resetMemoryPeak](#resetmemorypeak)
- [beginAllocTag](#beginalloctag)
- [endAllocTag](#endalloctag)
- [setMemoryOverlay](#setmemoryoverlay)
- [setPadOverlay](#setpadoverlay)
- [setDrawStatsLog](#setdrawstatslog)
- [getTextureMemory](#gettexturememory)
- [setTextureMemoryLog](#settexturememorylog)
- [resetTextureMemoryPeak](#resettexturememorypeak)
- [getJoypadCount](#getjoypadcount)
- [hasJoypad](#hasjoypad)
- [getPadAxis](#getpadaxis)
- [rumblePad](#rumblepad)
- [stopRumblePad](#stoprumblepad)
- [getLicenseList](#getlicenselist)
- [getLicenseText](#getlicensetext)
- [readEnvValue](#readenvvalue)
- [writeEnvValue](#writeenvvalue)
- [expandEnvString](#expandenvstring)
- [urlencode](#urlencode)
- [urldecode](#urldecode)
- [getAboutString](#getaboutstring)
- [breathe](#breathe)
- [getMonitorInfo](#getmonitorinfo)
- [getDisplayMonitors](#getdisplaymonitors)
- [getSystemMetrics](#getsystemmetrics)

---

### versionString

Property \ Access: `r`

**Description**

Version string

Gets the version string of the Kirikiri engine.

The version string has the following form.

`1.0.0.1`

---

### versionInformation

Property \ Access: `r`

**Description**

Version information string

Gets the version information string of the Kirikiri engine.

The version information string is longer than [System.versionString](System.md#versionstring)

and looks like the following.

`吉里吉里[きりきり] Z 実行コア/1.0.0.0 (Compiled on Dec 16 2013 23:15:27) TJS2/2.4.28 Copyright (C) 1997-2013 W.Dee and contributors All rights reserved.`

---

### eventDisabled

Property \ Access: `r/w`

**Description**

Whether event delivery is stopped

true when Kirikiri's **event delivery** is stopped. This property can also be
set.

While event delivery is stopped, events in Kirikiri either do not occur or are deferred
(the behavior depends on the type of event).

---

### graphicCacheLimit

Property \ Access: `r/w`

**Description**

Image cache limit

Represents Kirikiri's **image cache limit** in bytes. This property can also be set.

If you specify `**gcsAuto**`, the value is set automatically according to the amount of memory
installed in the machine.

Rule images and region images consume width × height bytes. Other images
consume width × height × 4 bytes.

---

### platformName

Property \ Access: `r`

**Description**

Platform name

Represents the name of the platform Kirikiri is running on. On Windows it is 'Win32' when the OS is 32-bit and 'Win64' when it is 64-bit.

In 1.3.0 and earlier it is always 'Win32'.

---

### osName

Property \ Access: `r`

**Description**

OS name

Represents the name of the OS Kirikiri is running on.

---

### exePath

Property \ Access: `r`

**Description**

Path of the folder containing the Kirikiri engine

Represents the path where the Kirikiri engine is located. The path is expressed as a unified storage name.

**See also:** [System.appDataPath](System.md#appdatapath) / [System.personalPath](System.md#personalpath)

---

### resourcePath

Property \ Access: `r`

**Description**

Path of the engine's built-in resources

Returns the location of engine built-in resources such as `config.cf` / `messages.json` / bundled fonts (`roboto-regular.ttf`, etc.)
as a unified storage name ending with `/`.

What it actually points to differs by platform.

| Platform | Value | Actual location |
|---|---|---|
| WINVER / desktop SDL3 | `resource://./` | Embedded in the exe / OS resources |
| Browser (wasm) | `file://./resource/` | Preloaded into MEMFS at startup |

The browser build has no `resource://` media at all, so a script that
hardcodes `resource://...` raises an "unsupported media type" exception as soon as it reaches
[Storages.isExistentStorage](Storages.md#isexistentstorage). Always prefix this property
when referring to bundled fonts and the like.

```tjs
// 同梱の英字フォントを参照する
var path = System.resourcePath + "roboto-regular.ttf";
```

**See also:** [System.exePath](System.md#exepath)

---

### replWebURL

Property \ Access: `r`

**Description**

URL of the browser REPL viewer

Represents the URL of the browser REPL viewer opened with `-replweb`. An empty string if it is not running.

---

### personalPath

Property \ Access: `r`

**Description**

Path of the user's Documents folder

Represents the path of the user's documents folder (the OS standard "Documents" folder itself)
as a unified storage name (ending with `/`). It is not an application-specific subfolder,
so create a subfolder in your script before writing to it.

| OS | Folder returned |
|---|---|
| Windows | "Documents" (redirections such as OneDrive are resolved; RoamingAppData if unavailable) |
| macOS | `~/Documents/` |
| iOS / iPadOS | `Documents/` in the app sandbox |
| Linux | XDG documents folder (`$HOME` if not set) |
| Android | App-specific external storage (internal storage if unavailable) |
| Web (wasm) | No dedicated folder → [System.exePath](System.md#exepath) |

If the folder cannot be determined, the same folder as [System.exePath](System.md#exepath) is returned
(a script can treat a value equal to exePath as "no separate location").

!!! note "SDL3 / generic builds before 2026-10"
    On platforms other than Windows, exePath was always returned.

**See also:** [System.appDataPath](System.md#appdatapath) / [System.dataPath](System.md#datapath) / [System.exePath](System.md#exepath)

---

### appDataPath

Property \ Access: `r`

**Description**

Path of the user's application data folder

Represents the path of the OS standard folder for application data (its base, not an application-specific subfolder)
as a unified storage name (ending with `/`). This folder is
usually hidden. Before writing, create subfolders such as an organization name and application name
in your script.

| OS | Folder returned |
|---|---|
| Windows | RoamingAppData (usually `C:\Users\<ユーザ名>\AppData\Roaming`) |
| macOS | `~/Library/Application Support/` |
| iOS / iPadOS | `Library/Application Support/` in the app sandbox (created if missing) |
| Linux | `$XDG_DATA_HOME` (`~/.local/share/` if not set) |
| Android | App internal storage |
| Web (wasm) | No dedicated folder → [System.exePath](System.md#exepath) |

If the folder cannot be determined, the same folder as [System.exePath](System.md#exepath) is returned.

!!! note "SDL3 / generic builds before 2026-10"
    On platforms other than Windows, exePath was always returned. SDL3 / generic builds before
    2026-08-25 do not have this property at all, so scripts that also target older engines
    should check for it with `typeof System.appDataPath`.
    For save data and similar, using [System.dataPath](System.md#datapath) is the safe choice.

**See also:** [System.dataPath](System.md#datapath) / [System.exePath](System.md#exepath) / [System.personalPath](System.md#personalpath)

---

### dataPath

Property \ Access: `r`

**Description**

Path of the data folder

Represents the directory specified with the -datapath command-line option.

By default, logs and the like are all written here.

User scripts are recommended to save their data here as well.

When -datapath is not specified, the default is `savedata` next to the executable on Windows,
and **`~/.local/share/<orgname>/<appname>/` in the Linux build**
(since 2026-10; previously Linux also used the folder next to the executable). The organization and application names
are determined by -orgname / -appname (written in `<exe name>.cf` in distributed builds).
The Linux value is also a local path, so `Storages.getLocalName()` can be used.

**It exists in every build and points to an application-specific location**, so using
this property is the safe way to get a save location ([System.appDataPath](System.md#appdatapath) /
[System.personalPath](System.md#personalpath) are the OS standard folders themselves, and in
older SDL3 / generic builds they return exePath or do not exist at all).

**See also:** [System.appDataPath](System.md#appdatapath)

---

### exeName

Property \ Access: `r`

**Description**

Path of the Kirikiri engine

Represents the path name of the Kirikiri engine. The path is expressed as a unified storage name.

---

### title

Property \ Access: `r/w`

**Description**

Title

Represents the title of the main window as a string. This property can also be set.

**See also:** [Window.caption](Window.md#caption)

---

### screenWidth

Property \ Access: `r`

**Description**

Screen width

Represents the horizontal screen size (screen resolution) in pixels.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### screenHeight

Property \ Access: `r`

**Description**

Screen height

Represents the vertical screen size (screen resolution) in pixels.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenWidth](System.md#screenwidth) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopLeft

Property \ Access: `r`

**Description**

Desktop left edge

Represents the left edge of the desktop (the area where windows can be shown) in pixels.

!!! warning "Native Windows (WINVER) build only"
    `desktopLeft` / `desktopTop` / `desktopWidth` / `desktopHeight` do not
    exist in SDL3 / generic builds. If you only need the screen resolution, use
    [System.screenWidth](System.md#screenwidth) /
    [System.screenHeight](System.md#screenheight), which exist in every build.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopTop

Property \ Access: `r`

**Description**

Desktop top edge

Represents the top edge of the desktop (the area where windows can be shown) in pixels.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopWidth

Property \ Access: `r`

**Description**

Desktop width

Represents the width of the desktop (the area where windows can be shown) in pixels.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopHeight](System.md#desktopheight)

---

### desktopHeight

Property \ Access: `r`

**Description**

Desktop height

Represents the height of the desktop (the area where windows can be shown) in pixels.

The value refers to the display on which the main window is located.

If there is no main window, the primary display is used
(if a startup display is specified with [-display](../guide/CommandLine.md),
that display is used until the main window is created).

**See also:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth)

---

### exitOnWindowClose

Property \ Access: `r/w`

**Description**

Whether to exit when the main window closes

Indicates whether to exit when the main window (the first instance of the Window class created) closes. This property can also be set. The default is true.

Note that if the main window closes and no debugging windows are shown either, Kirikiri may remain in the system without exiting and become uncontrollable (you may have no choice but to end the process from Task Manager).

---

### exceptionHandler

Property \ Access: `r/w`

**Description**

Handler function for uncaught exceptions

Represents the function that handles uncaught exceptions (exceptions that were not caught anywhere and reached the Kirikiri engine).

Specifying null restores the default behavior.

The default behavior is to:

- stop delivery of asynchronous events (set [System.eventDisabled](System.md#eventdisabled) to true)
- start writing the log to a file (call [Debug.logAsError](Debug.md#logaserror))
- show a dialog box reporting the error and point to the location in the script editor

The handler function takes one argument, the exception object.

If no handler function is specified, if it is null, or if it returns false, the default behavior is performed.

If the handler function returns true, the default behavior above is not performed.

Keep in mind that asynchronous events may occur while the handler function is running. If the Kirikiri engine gets a chance to process asynchronous events, another unexpected exception may occur while the exception handler is running. To avoid this, if the handler function does anything that waits (giving Kirikiri a chance to process asynchronous events), you normally stop asynchronous events first.

System.exceptionHandler = function (e)

{

// どこにも捕捉されない例外がシステム側で捕捉された場合、この関数が

// 呼ばれる。e は例外オブジェクト。

if(e instanceof "ConductorException")

{

// コンダクタの投げた例外の場合

Debug.logAsError(); // ログのファイルへの書き出し動作の開始など

var event_disabled = System.eventDisabled;

System.eventDisabled = true;

// エラーの理由を表示させている間にイベントが発生すると

// やっかいなのでいったんイベント発生を停止させる

System.inform(e.message);

System.eventDisabled = event_disabled;

// イベントを発生するかどうかを元の状態に

return true; // true を返すと本体側で例外の処理は行わなくなる

}

else

{

return false; // false を返すと通常の例外処理

}

};

**See also:** [System.eventDisabled](System.md#eventdisabled) / [Debug.logAsError](Debug.md#logaserror)

---

### onActivate

Property \ Access: `r/w`

**Description**

When the application becomes active

Represents the event function called when the application becomes active.

If null, no function is called.

Unlike regular event handlers, to receive this event you set the function to be called to this property.

[Window.onActivate](Window.md#onactivate) occurs when each window in the same application becomes active, whereas this event occurs when the main window becomes active.

Note that this event may occur even when the main window is already active (it is not guaranteed to occur strictly in the order onActivate → onDeactivate → onActivate → …).

**See also:** [System.onDeactivate](System.md#ondeactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onDeactivate

Property \ Access: `r/w`

**Description**

When the application becomes inactive

Represents the event function called when the application becomes inactive.

If null, no function is called.

Unlike regular event handlers, to receive this event you set the function to be called to this property.

[Window.onDeactivate](Window.md#ondeactivate) occurs when each window in the same application becomes inactive, whereas this event occurs when the main window becomes inactive.

Note that this event may occur even when the main window is already inactive (it is not guaranteed to occur strictly in the order onActivate → onDeactivate → onActivate → …).

**See also:** [System.onActivate](System.md#onactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onJoypadChange

Property \ Access: `r/w`

**Description**

Event called when the joypad configuration changes

Represents the event function called when the joypad configuration changes, for example when a joypad is connected or disconnected.

If null, no function is called.

Unlike regular event handlers, to receive this event you set the function to be called to this property.

---

### drawThreadNum

Property \ Access: `r/w`

**Description**

Number of threads used for drawing

Represents the **number of threads** Kirikiri's layer system uses for drawing. This property can also be set.

If you specify `**dtnAuto**`, as many threads as the number of processors recognized by the OS are assigned automatically.

Using several drawing threads may improve drawing performance on multi-core systems, but it can also reduce performance.

You may get good results by applying it to drawing over large areas, heavy Affine operations, computationally heavy layer compositing and the like.

Even when multithreading is enabled, drawing may not run multithreaded if the system judges that the drawing load is too light to benefit from it.

---

### savedGamesPath

Property \ Access: `r`

**Description**

Path of Saved Games (1.1.0 and later)

Represents the path of the Saved Games folder.

It is usually the following.

C:\Users\<ユーザ名>\Saved Games

---

### exeBits

Property \ Access: `r`

**Description**

Whether the Kirikiri engine is 32-bit or 64-bit (1.3.0 and later)

Indicates whether the executable is 32-bit or 64-bit, as the integer 32 or 64.

**See also:** [System.osBits](System.md#osbits) / [System.platformName](System.md#platformname)

---

### osBits

Property \ Access: `r`

**Description**

Whether the OS is 32-bit or 64-bit (1.3.0 and later)

Indicates whether the OS is 32-bit or 64-bit, as the integer 32 or 64.

**See also:** [System.exeBits](System.md#exebits) / [System.platformName](System.md#platformname)

---

### exitOnNoWindowStartup

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Exit automatically when started without a window

If true, the engine exits automatically when startup completes without any window
having been created. Used for debugging and for controlling batch processing.

---

### isGeneric

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Whether this is a generic build

true in SDL3-based cross-platform builds (generic / SDL),
false in the native Win32 build (WINVER).
Read-only.

**See also:** [System.isWindows](System.md#iswindows)

---

### isWindows

Property \ Access: `r/w`

**Description**

Whether the system is Windows [r]

---

### licenseText

Property \ Access: `r/w`

**Type**: `String`

**Description**

License text

Returns the license text built into the Kirikiri Z engine.
Used for display in places such as the Kirikiri settings dialog.
The engine's own terms are followed by the list of licenses of bundled components
(the same content as getLicenseList). When you need the full text of each, use
getLicenseText.
Read-only.

---

### openGLESVersion

Property \ Access: `r/w`

**Description**

OpenGL ES version

Returns the actual version multiplied by 100: 200 for 2.0, 300 for 3.0.

---

### processorNum

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Number of logical processors

Returns the number of logical processors recognized by the OS.
Used, for example, to determine the number of drawing threads automatically. Read-only.

---

### renderStats

Property \ Access: `r/w`

**Type**: `Dictionary`

**Description**

Screen transfer cost measurements

Returns the time spent transferring the composited screen buffer to the GPU texture.
Read-only. The returned dictionary has the following keys.

| Key | Meaning |
|---|---|
| `texUploadUs` | Cumulative time of transfer calls (microseconds) |
| `texUploads` | Number of transfers (per dirty rectangle) |
| `texUploadBytes` | Cumulative bytes transferred |
| `frames` | Number of composited frames drawn (whether or not a transfer occurred) |

All values are cumulative, so **read twice, take the difference and divide by the elapsed real time** to see
"how many milliseconds per second were spent on transfers".
`System.renderStatsReset()` resets them to 0.

Frames with no change on screen skip the transfer entirely, so while the screen is static
`texUploads` does not increase (`frames` does). Conversely, if the screen is static but
`texUploadBytes` grows by the screen size every frame, something is
issuing full-screen updates.

Transfers may block for driver reasons (for example, when the GPU is still referencing
the destination texture), and that wait is included in this time as well.
The transfer method differs by draw device (OpenGL = glTexSubImage2D /
SDLDrawDevice = SDL_UpdateTexture / native Windows =
UpdateSubresource), so use this as a first indicator of whether transfers are a bottleneck on the target hardware.

No build option is needed; it is always measured (just a few
counter increments per frame). For the breakdown on the overlay dialog side, see
`ElementsDialog.renderStats`.

!!! tip "Reading the numbers"
    Even if the transfer ratio (transfer time / elapsed real time) is high, **if the fps holds up,
    most of the wait is vsync synchronization** (the driver waits for the
    next frame inside the transfer call). If transfers are really holding things back, the fps
    drops. These criteria, the differences between paths and how to proceed with measurement are
    covered in the core demo `perf_stats` and in the engine document
    `src/core/doc/ScreenTransfer.md`.

**See also:** [System.renderStatsReset](System.md#renderstatsreset)

---

### texUploadUsePBO

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Forces whether texture transfers use PBOs

Forces the path used to transfer the screen buffer to the GPU texture, for measurement and comparison.
The following values can be set.

| Value | Meaning |
|---|---|
| `void` (default) | Follow the default for each use (main screen = chosen automatically by transfer size / overlay = direct transfer) |
| `true` | Always transfer via a PBO |
| `false` | Always transfer directly with `glTexSubImage2D` |

By default, a PBO is used when the transfer is 256KB or larger, and a direct transfer otherwise.
This is because on screens that update many small rectangles, the fixed cost of PBOs makes them
slower. With the ANGLE implementation (GLES → D3D11 emulation on Windows),
direct transfer is always used regardless of size.

For A/B comparisons, use `System.renderStatsReset()` together with `System.renderStats`.
The environment variable `KRKRZ_GLTEXUP=pbo|direct` does the same,
but use this property in environments where you cannot pass environment variables.

Exists only in builds with OpenGL drawing enabled (enabled by default).

**See also:** [System.renderStats](System.md#renderstats)

---

### touchDevice

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Whether a touch device is available

Returns true if the environment has a touch input device.
Read-only.

---

### platformTag

Property \ Access: `r/w`

**Type**: `String`

**Description**

Platform tag

A short identifier for the running platform (`"windows"` / `"android"` /
`"macos"` / `"linux"` / `"web"`, etc.). Read-only.

[System.platformName](System.md#platformname) is the raw string from the OS and
contains spaces and inconsistent spellings, which makes it awkward for file names and conditionals. This one,
in contrast, is **normalized to lowercase with no spaces**, so you can use it directly to branch by platform.

In environments where several tags apply (such as different generations of a console), **the most specific one**
is returned.

!!! info "Per-platform engine configuration `config_<tag>.cf`"
    In addition to the common `config.cf`, you can place
    `config_<tag>.cf` among the resources to override settings per platform.
    They are read in the order "specific tag → general tag → common `config.cf`",
    and whichever is read first takes priority. Missing files are simply skipped.

**See also:** [System.platformName](System.md#platformname) / [System.osName](System.md#osname)

---

### systemLanguage

Property \ Access: `r/w`

**Type**: `String`

**Description**

System display language

Returns the display language set in the OS (or in the hardware, on game consoles) as a
[BCP-47](https://www.rfc-editor.org/info/bcp47) language tag.
Read-only. Values look like `"ja-JP"` / `"en-US"` / `"zh-Hant"` / `"zh-Hans"`.

This lets you match the game's **default** language to the hardware setting. Choosing and
saving the language is the game's responsibility; this property only returns "which language the system is set to".
If you do not need the region, look at the part before `-`.

```tjs
var lang = System.systemLanguage;
var code = lang.indexOf("-") >= 0 ? lang.substring(0, lang.indexOf("-")) : lang;
if(code == "") code = "ja";   // 取得できない環境はゲーム既定へ
```

!!! warning "Empty string where it cannot be obtained"
    In environments with no way to obtain the language, an empty string is returned.
    Fall back to the game's default language on the caller's side.

The source differs by environment (native Windows build =
`GetUserDefaultLocaleName` / SDL3 build = the first entry of `SDL_GetPreferredLocales`;
game consoles use each hardware's API). In the SDL3 build, if the region cannot be obtained,
only the language is returned, as in `"ja"`.

The language of the engine's own messages (error text, etc.) and option descriptions
(ja / en / chs / cht) also follows this value. You can override it explicitly with the `-language`
command-line option ([Command-line options](../guide/CommandLine.md)).

**See also:** [System.platformTag](System.md#platformtag)

---

### uiLanguage

Property \ Access: `r`

**Type**: `String`

**Description**

Effective display language

Returns the language tag used to choose the language of the engine's own messages (error text, etc.)
and option descriptions. Read-only.

If the `-language` command-line option (also settable in `config.cf`) is specified, its value is returned;
otherwise it is the OS language, the same as [System.systemLanguage](#systemlanguage).
In environments where neither can be obtained, an empty string is returned.

[System.systemLanguage](#systemlanguage) returns the OS setting as is, so
it does not reflect `-language`. Use this one when you want your game's localization to match
the language of the engine's messages. If you need it rounded to a language code, use
[System.uiLanguageCandidates](#uilanguagecandidates).

**See also:** [System.uiLanguageCandidates](System.md#uilanguagecandidates) / [System.systemLanguage](System.md#systemlanguage)

---

### uiLanguageCandidates

Property \ Access: `r`

**Type**: `Array`

**Description**

Effective display language candidates (in priority order)

An array of [System.uiLanguage](#uilanguage) rounded to language codes using the same rules as the engine's
message resources. The first element is the language actually used, followed by fallback languages to try
when a string is missing in that language. The last element is always `"ja"`. Read-only;
a new array is returned each time it is read.

The language code is one of `"ja"` / `"en"` / `"chs"` (Simplified Chinese) / `"cht"` (Traditional Chinese).
Examples:

| uiLanguage | uiLanguageCandidates |
|---|---|
| `ja-JP` | `["ja"]` |
| `en-US` / `fr-FR`, etc. | `["en", "ja"]` |
| `zh-CN` | `["chs", "en", "ja"]` |
| `zh-TW` / `zh-Hant-HK` | `["cht", "chs", "en", "ja"]` |

```tjs
// 文字列表 %[ ja : "…", en : "…" ] から現在の言語で引く
function pickText(entry)
{
var langs = System.uiLanguageCandidates;
for (var i = 0; i < langs.count; i++)
if (entry[langs[i]] !== void) return entry[langs[i]];
return "";
}
```

**See also:** [System.uiLanguage](System.md#uilanguage)

---

### padButtonMapping

Property \ Access: `r/w`

**Type**: `String`

**Description**

Pad button mapping scheme

A string that indicates how the physical buttons of a gamepad are mapped to `VK_PAD1`–`VK_PAD4`.
This property can also be set.

- `"label"` (default) … Maps by **button label**. `VK_PAD1` = label A
(✕ on PlayStation), `VK_PAD2` = B (○), `VK_PAD3` = X (□),
`VK_PAD4` = Y (△). Even on controllers where A/B and X/Y are **in swapped positions**,
as on Nintendo-style controllers, what the screen shows matches the button actually pressed.
- `"position"` … Maps by **position**, as before (bottom = `VK_PAD1`,
right = `VK_PAD2`, left = `VK_PAD3`, top = `VK_PAD4`).

For controllers whose labels cannot be determined, it falls back to position-based mapping automatically.
PlayStation and Xbox-style controllers give the same result with either scheme.

It can also be specified with the `-padbuttons=label|position` command-line option (also settable in `config.cf`).
Assigning anything other than `"label"` / `"position"` raises an exception.

!!! warning "SDL3 / generic builds only"
    This property exists only in SDL3 / generic builds. Pad input in the native Windows
    (WINVER) build is based on XInput, and its button labels are fixed to the
    Xbox style, so positions and labels never disagree.

**See also:** [System.getJoypadType](System.md#getjoypadtype)

---

### padStyle

Property \ Access: `r/w`

**Type**: `String`

**Description**

Button label style of the connected pad (read-only)

A string indicating the button label style of the "last used pad".
It is one of `"xbox"` / `"ps"` / `"switch"`, or an empty string if it cannot
be determined.

Use it to decide which style of button images to show on screen (in control guides, etc.).
When `"auto"` is passed to [ElementsDialog.setPadTheme](ElementsDialog.md#setpadtheme),
the automatic selection uses the same detection as this property.

**See also:** [System.padButtonMapping](System.md#padbuttonmapping) / [System.getJoypadType](System.md#getjoypadtype)

---

### buildVariantName

Property \ Access: `r`

**Type**: `String`

**Description**

Build variant name

Returns the **variant name** of the running engine build.

- `WIN` ... native Win32 build (WINVER)
- `SDL` ... SDL3-based generic build (generic / SDL)
- `LIB` ... static library form (libkrkrz)

Read-only. Use it when you need a more specific variant identification than
`System.isGeneric`.

**See also:** [System.isGeneric](System.md#isgeneric) / [System.platformName](System.md#platformname)

---

### padAxisLeftX

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: left stick X axis

Constant to pass as the axisId argument of [System.getPadAxis](System.md#getpadaxis).
Read-only.

---

### padAxisLeftY

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: left stick Y axis

---

### padAxisRightX

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: right stick X axis

---

### padAxisRightY

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: right stick Y axis

---

### padAxisLeftTrigger

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: L trigger

---

### padAxisRightTrigger

Property \ Access: `r`

**Type**: `Integer`

**Description**

Pad axis ID: R trigger

---

### padEnabled

Property \ Access: `r/w`

**Type**: `Boolean ( 真 = 有効 / 偽 = 無効。既定は有効 )`

**Description**

Enables or disables gamepad support

Assigning false disables gamepad support completely (neither state retrieval nor key event
generation is performed). Assigning true enables it again. It can be toggled at any time
at runtime.

Use it to deal with cases where another device is mistakenly recognized as a gamepad and misbehaves
(for example, as a disable option on a settings screen). The
`-joypad=no` command-line option also disables it from startup, but a value set explicitly with this property
takes priority.

---

### replActive

Property \ Access: `r`

**Type**: `Boolean`

**Description**

Whether driven by the REPL

true if the REPL (`-repl` / `-replfile` / `-replweb`) is enabled. Read-only.
Use it to change behavior only while driven by an agent (for example, using the modal response channel of
[System.choice](System.md#choice) instead of a confirmation dialog).
In builds without the REPL (MASTER, etc.) it is always false.

In the WINVER build the REPL becomes active after the startup script, so it is still false while `startup.tjs`
is running. To check right at startup, also use `System.getArgument("-replfile")` or similar.

---

### terminate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `code` | `0` | Exit code of the process |

**Description**

Exits Kirikiri asynchronously

**Exits** Kirikiri.

Kirikiri does not exit immediately when this method is called.

It exits once control has returned to Kirikiri from all event handlers.

---

### exit

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `code` | `0` | Exit code of the process |

**Description**

Exits Kirikiri synchronously

**Exits** Kirikiri.

Unlike [System.terminate](System.md#terminate), this method exits at the moment it is called, so
it never returns.

---

### addContinuousHandler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | Function to use as the handler. |

**Description**

Adds a Continuous handler

Registers a **Continuous handler**.

A Continuous handler is an event handler that is called "as often as possible".

When there is nothing else to do, Kirikiri keeps calling Continuous handlers.
When other events occur, they take priority.

However, if the call frequency is specified with the -contfreq command-line option,
that setting is followed.

---

### removeContinuousHandler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | Handler function. |

**Description**

Removes a Continuous handler

Removes a **Continuous handler**.

---

### inform

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Message to show. |
| `caption` | `""` | String to use as the window caption. |

**Description**

Shows a message

Shows a window that presents a message to the user.

The window is modal (other windows cannot be used while it is shown).

---

### confirm

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Message to show. |
| `caption` | `""` | String to use as the window caption. |
| `window` | `void` | Window to use as the parent (optional). The parent is applied only in the<br>WINVER build. |

**Return value**

true if the user chooses "Yes"; false if the user chooses "No" or closes the
dialog.

**Description**

Shows a confirmation message (Yes / No)

Shows a modal window that asks the user "Yes / No"
(the Yes/No version of [System.inform](System.md#inform)). Other windows cannot be used
while it is shown.
When driven through the REPL file channel (`-replfile`), no blocking dialog is
shown; instead the agent's answer is received through the modal response channel
(`yes` / `y` / `1` / `true` / `ok` mean true).

**See also:** [System.choice](System.md#choice)

---

### inputString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `caption` | `&nbsp;` | Title of the dialog. |
| `prompt` | `""` | Text prompting for input (caption is used if omitted). |
| `default` | `""` | Initial value of the input field (optional). |

**Return value**

The string the user entered. **void if the user cancels.**

**Description**

Inputs a string

Shows a modal dialog that lets the user enter one line of text
(Kirikiri 2 compatible).
The WINVER build shows a native input dialog, and the SDL build shows an
Elements-based input dialog. On some platforms it may be replaced by the OS
software keyboard or similar (void in unsupported environments).
While driven by the REPL, no blocking dialog is shown; input is received through the REPL
response channel (default is returned if there is no responder).

---

### choice

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `caption` | `&nbsp;` | Title of the dialog. |
| `text` | `&nbsp;` | Body text. |
| `choices` | `&nbsp;` | Array of button labels (at least one; an empty array raises an exception). |
| `default` | `0` | Number of the default button (0 if out of range). |

**Return value**

The number of the button chosen (the index into choices).

**Description**

Chooses one of several options

Shows a modal dialog with a row of option buttons and returns the number of the button chosen
(use it for questions that the two choices of [System.confirm](System.md#confirm) cannot express,
such as a three-way "Save / Don't Save / Cancel").
```tjs
var r = System.choice("確認", "変更を保存しますか?", ["保存", "保存しない", "キャンセル"], 2);
if(r == 0) save(); else if(r == 2) return;
```
The WINVER build uses a TaskDialog, and SDL3-family builds use an Elements dialog (or the OS
message box if that is unavailable). Focus is placed on the default button, and closing with Esc or the close button
also returns the default number.

When driven through the REPL file channel (`-replfile`), no dialog is shown; instead
`{"type":"choice","caption":…,"text":…,"choices":[…],"default":n}` is sent to the modal response channel
and the agent's answer is awaited. The answer is either the string of the chosen element (case-insensitive) or its number;
an empty or unmatched value results in the default number.

**See also:** [System.confirm](System.md#confirm) / [System.replActive](System.md#replactive)

---

### getTickCount

Method

**Return value**

The tick count (64-bit integer).

**Description**

Gets the tick count

The **tick count** is a number that counts up every 1/1000 second. Get the tick count with this method at
two points in time and take the difference to find the time elapsed between them.

---

### getKeyState

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `code` | `&nbsp;` | **Virtual key code** whose state to get. |

**Return value**

true if the key is pressed, false otherwise.

**Description**

Gets a key state

Gets whether the key corresponding to the key code given in code is pressed at the moment this method
is called.

---

### registerHotKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code (`VK_RETURN` / `VK_ESCAPE` / `VK_F1`, etc.). |
| `mods` | `&nbsp;` | A combination of `ssShift` / `ssAlt` / `ssCtrl`. Only these 3 bits are matched;<br>NumLock / CapsLock and similar states are ignored. |
| `callback` | `&nbsp;` | Function called when the key is pressed. It is called as `callback(key, shift)`.<br>**If it returns false (or 0), the key is not consumed** and goes on to the normal dispatch<br>(any other return value, including void, consumes it). |

**Description**

Registers a top-level hotkey

Matches keys at the entrance of the event pump and calls callback synchronously **before the focused layer, text input or
[ElementsDialog](ElementsDialog.md) (including modal ones)**.
It lets you handle in one place keys that should work "no matter what is on screen",
such as Alt+Enter to toggle full screen or Esc to confirm quitting.

Registering the same key + mods again replaces the previous registration. The registration table is shared across the process
(not per Window) and is released when the engine exits.

```tjs
// Esc は終了確認。ただしモーダルダイアログ表示中は素通しする
System.registerHotKey(VK_ESCAPE, 0, function(key, shift) {
if(ElementsDialog.modalActive) return false;   // 消費せず通常の dispatch へ
askQuit();
return true;
});
```

The callback does not fire again on key repeat while held down (the repeats are only consumed).
A key up is matched by key alone, and the up of a key whose down was consumed is always consumed
(even if the modifier is released first, the other half does not leak into the input layer). If the callback
throws an exception, the pump keeps working; the exception is logged and processing continues.

Works in both the WINVER (native Windows) build and SDL3-family builds.

If you want the host to receive only certain keys while focus stays on a dialog,
use [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey), which serves a different purpose (it passes keys through to the normal game
input path instead of to the dialog, and is disabled while a modal is active).

**See also:** [System.unregisterHotKey](System.md#unregisterhotkey) / [ElementsDialog.modalActive](ElementsDialog.md#modalactive)

---

### unregisterHotKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Virtual key code specified at registration. |
| `mods` | `&nbsp;` | Modifier combination specified at registration. |

**Return value**

Whether it was unregistered (false if there was no registration).

**Description**

Unregisters a top-level hotkey

Unregisters a hotkey registered with [registerHotKey](#registerhotkey).

**See also:** [System.registerHotKey](System.md#registerhotkey)

---

### shellExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | File or software to run.<br>If a file is given, the program associated with it is launched. |
| `param` | `""` | Parameters to pass to the software.<br>If you specify a file in the target argument, omit this argument or pass an empty<br>string.<br>**Platform differences**<br>The native Windows build uses ShellExecute and the SDL build uses SDL_OpenURL to<br>open target with the OS default handler (supports opening URLs and files).<br>In the SDL build, param (arguments) is ignored (running programs with arguments is not supported). |

**Return value**

true if it ran successfully, false otherwise.

**Description**

Runs a file or program

**Runs** the file or software given in target.

---

### readRegValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Registry key to read. |

**Return value**

The registry value on success, void on failure.

**Description**

Reads the registry

Reads the Windows registry value given in key.

The registry key can start with one of the following root key names.

`HKEY_CLASSES_ROOT
HKEY_CURRENT_CONFIG
HKEY_CURRENT_USER

HKEY_LOCAL_MACHINE
HKEY_USERS
HKEY_PERFORMANCE_DATA

HKEY_DYN_DATA
`
For example, you can pass a string like the following as key.

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\hoeg\installdir`

Only numbers and single strings can be read. A number is returned as an integer, and a string
as a string.

---

### getArgument

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the command-line option to get. Prefix it with '-'<br>(hyphen) (e.g. `'-nosplash'`). |

**Return value**

The value of the command-line option if specified, otherwise
void.

**Description**

Gets a command-line option

**Command-line options** must be passed to Kirikiri in the form

`-name=value`

or

`-name`

In the former case `value` is returned as the value, and in the latter case `'yes'` is returned.

**See also:** [System.setArgument](System.md#setargument)

---

### setArgument

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the command-line option to set. Prefix it with '-'<br>(hyphen) (e.g. `'-contfreq'`). |
| `value` | `&nbsp;` | Value to set (e.g. `'60'`). |

**Description**

Sets a command-line option

Sets a **command-line option** dynamically. Not every command-line option can be set.

For the options that can be set, see [Command-line options](../guide/CommandLine.md). Do not change options that are not marked there as dynamically changeable.

This method does not check whether the option can be changed dynamically, whether it exists, or whether the value is valid. Be very careful when setting values.

**See also:** [System.getArgument](System.md#getargument)

---

### toActualColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | Color constant (see [Color constants](../guide/ColorCodes.md)).<br>If a regular 0xRRGGBB color is given, the same value is returned. |

**Return value**

The actual color represented by the color constant, in 0xRRGGBB format.

**Description**

Gets the actual color of a color constant

Converts a color constant to the actual color and returns it in 0xRRGGBB format.

---

### createAppLock

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Key string used for the check. If another running instance of Kirikiri has passed the same<br>key string to this method, false is returned.<br>As a rule, use only characters allowed in TJS variable names in the key<br>string.<br>The key string must be sufficiently unique.<br>The WINVER build uses a named mutex, and SDL3-family builds hold an OS exclusive lock on a lock file<br>in the temporary area. Either is released when the process exits<br>(even if it terminates abnormally). |

**Return value**

false if an instance of Kirikiri with the same key string is already running, true otherwise.

**Description**

Checks for multiple instances

Returns false if another instance of Kirikiri with the same key string is running, true otherwise.

Use it to prevent multiple instances.

---

### createUUID

Method

**Return value**

The generated UUID string, in the form "e8b2a2b5-5ceb-4f75-a08b-1f1bdfdca4f1"
(each alphanumeric character other than the hyphens is a hexadecimal digit).

**Description**

Generates a UUID string

Generates and returns a UUID string. This method generates a 128-bit UUID (universal unique identifier)
from a random bit sequence.

The UUID generation algorithm implemented in Kirikiri
gathers some environmental noise to produce the random bits,
but it is not recommended for uses that require strong security. Still,
the result can be considered "very, very unlikely" to collide with any other UUID.

---

### assignMessage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Message ID to assign. |
| `msg` | `&nbsp;` | Message to assign to the ID given in id. |

**Return value**

true if the ID exists and the message was assigned, false otherwise.

**Description**

Changes a message assignment

Changes a message assignment.

This method lets you replace a message built into Kirikiri with a different one.

Normally you write these in the message map file (see [Startup](../guide/Startup.md)).

To get the list of assignable IDs and the messages currently assigned to them, run
"Create message map file" from the [Controller](Controller.md).

---

### doCompact

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `level` | `clAll` | Level.<br>**clIdle** performs the same compaction as is done when the system is idle (relatively inactive). In the current version, TJS2 garbage collection is performed.<br>**clDeactivate** performs the same compaction as is done when Kirikiri becomes inactive (when another application becomes active). In the current version, the temporary image buffers for layer operations, the layer cache, the XP3 archive segment (storage fragment) cache and the automatic search path cache are cleared.<br>**clMinimize** performs the same compaction as is done when Kirikiri is minimized. In the current version, the rendered glyph cache and the image cache are cleared.<br>**clAll** performs all of the compactions above.<br>The compaction levels get stronger in the order clIdle < clDeactivate < clMinimize < clAll. Specifying a higher level also performs the compaction done at lower levels. For example, running clDeactivate also performs the clIdle processing.<br>If the argument is omitted, clAll is assumed. |

**Description**

Compacts memory

Compacts memory. Compaction reduces memory usage by releasing unused memory and memory used by various caches.

Kirikiri does this automatically, so you usually do not need to worry about it, but you can use this method when you want to force it from your program.

---

### touchImages

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storages` | `&nbsp;` | Array (an object of the Array class) of image storage names to cache.<br>Those listed first take priority.<br>Kirikiri manages the cache using the string passed as the first argument of<br>[Layer.loadImages](Layer.md#loadimages) as is as the key,<br>so for the cache to be meaningful,<br>the image storage names given here must be identical to those passed as the first argument of<br>Layer.loadImages. |
| `limitbytes` | `0` | Limit, in bytes, on the cache capacity used by this call.<br>0 uses the whole cache.<br>A positive number tries to use the cache up to that many bytes.<br>A negative number adds that value to the current cache<br>limit ([System.graphicCacheLimit](System.md#graphiccachelimit)) (adding a negative number, so it is actually a subtraction)<br>and uses the result as the limit. If the resulting limit is<br>0 or negative, this method does nothing and returns. For example,<br>-2*1024*1024 means the current cache limit minus 2MB.<br>This is handy when you want to leave some room in the cache. |
| `timeout` | `0` | Timeout (time limit) in ms. 0 means no<br>limit.<br>When the time given in this argument has elapsed, this method stops loading further images<br>and returns. However, if the timeout expires while an image is being loaded, it does not return until<br>that image has finished loading. |

**Description**

Loads images into the cache

This method tries to put the specified images into the cache. It makes an effort to do so,
but there is no guarantee that the images actually end up in the cache.
Loading stops when the image cache limit is exceeded or the timeout expires.
Images listed earlier in the storages argument are more likely to get into the cache
(they take priority). If a specified image is already in the cache, its survival rank
in the cache is simply raised.

This method ignores all errors that occur while loading images.

In the current version, the images this method can put into the cache are those that can normally be loaded with
[Layer.loadImages](Layer.md#loadimages) without a color key
(images with an alpha channel are fine). Universal transition rule images and
region images are loaded, but they do not become valid cache data (the loaded
data is wasted), so do not specify them.

For the number of bytes images use in the cache, see [System.graphicCacheLimit](System.md#graphiccachelimit).

---

### showVersion

Method

**Description**

Shows the about dialog (1.1.0 and later)

Shows the about dialog.

---

### dumpHeap

Method

**Description**

Dumps heap information (1.1.0 and later)

Writes heap information to the console.

---

### captureScreen

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Destination unified storage path (.png) |
| `x` | `0` | = 0 Left edge of the area to save |
| `y` | `0` | = 0 Top edge of the area to save |
| `w` | `0` | = 0 Width of the area to save (0 for the whole screen) |
| `h` | `0` | = 0 Height of the area to save (0 for the whole screen) |

**Description**

Saves the actual screen as PNG

Requests that, just before the next frame is presented, the actual screen including overlays be read back and saved to path as PNG
(the actual save happens when the DrawDevice draws). You can specify the area to save with x, y, w, h;
setting w/h to 0 means the whole screen. It is equivalent to SDL's `Agent.captureScreen` and is a testing/verification feature
provided when the REPL is enabled, so that it can also be used in the WINVER build, which lacks Agent. The return value is the destination path.

---

### renderStatsReset

Method

**Description**

Resets the screen transfer cost measurements

Resets the cumulative counters of `System.renderStats` to 0.
Call it at the start of a measurement interval.

**See also:** [System.renderStats](System.md#renderstats)

---

### addFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name of the font file to add. |

**Return value**

An array of the face names provided by the added font.

**Description**

Adds a font

Adds a font file in a storage to the engine.
The added font can then be referred to by face name from layers and font drawing APIs.

**See also:** [Font](Font.md)

---

### clearGraphicCache

Method

**Description**

Discards the graphic cache

Discards the internal graphic cache used by `Layer.loadImages` and others.
Call it when you want to cut memory usage quickly or force images to be reloaded after replacing them.

---

### getJoypadType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `0` | Pad number (default 0). **0 is a special number meaning "the last used<br>pad"**; 1 and above refer to actual pads in connection order (1st, 2nd, …).<br>The pad-related APIs and key events (VK_PAD*) all follow this<br>numbering, and key events always come from pad 0 (= the last used pad).<br>The number of connected pads can be obtained with `System.getJoypadCount()`. |

**Return value**

A string representing the joypad's model name. If there is no pad with the specified number,
an empty string is returned.

**Description**

Gets the type (model name) of a connected joypad

Returns the type of the joypad with the specified number as a model name "string"
(not a numeric type ID). The string is environment-dependent: in the SDL build it is the
model name recognized by SDL (e.g. "Xbox Series X Controller"), and in the WINVER build it is a
generic name derived from XInput ("XInput Controller").

---

### nullpo

Method

**Description**

Causes a null pointer access

Do not call this.

---

### system

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `command` | `&nbsp;` | Command string to run. |

**Return value**

The return value of `_wsystem()` as is.

**Description**

Runs a shell command

Runs a shell command synchronously, equivalent to the OS `system(3)`. Win32 build only.
Immediately afterward, a compact event at the `TVP_COMPACT_LEVEL_MAX` level is issued and
all caches are discarded.

---

### getSystemAllocatorInfo

Method

**Return value**

A dictionary containing the keys above.

**Description**

Gets platform allocator information

Gets the memory state of the process and system in one call. Items whose values could not be
obtained have no key in the dictionary at all, so you can check them with `"xxx" in dict`.

Keys of the returned dictionary (some may be missing depending on the environment):

- `totalFreeSize`        : free space in the whole heap (bytes)
- `allocatableSize`      : largest contiguous allocatable region (bytes)
- `usedSize`             : current usage (bytes)
- `peakUsedSize`         : peak usage since startup (bytes)
- `totalSize`            : total heap capacity (bytes)
- `processRss`           : process RSS (bytes)
- `processPeakRss`       : process peak RSS (bytes)
- `processVsize`         : process virtual size (bytes)
- `systemTotalPhysical`  : total system physical memory (bytes)
- `systemAvailPhysical`  : available system physical memory (bytes)

**See also:** [System.resetMemoryPeak](System.md#resetmemorypeak)

---

### resetMemoryPeak

Method

**Description**

Resets memory peak measurement

Resets **peak_used** of the File / Bitmap / Sound allocators to current_used,
and also resets the peak value of the Krkrz global allocator.
Use it when you want the `(peak X.XX)` display in `MemoryOverlay` to show "the maximum from here on".
Equivalent to `.mempeakclear` in the REPL.

---

### beginAllocTag

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Tag name. |

**Description**

Begins a memory allocator tag scope

Pushes `name` onto a thread-local tag stack. Subsequent engine-side (Krkrz) memory allocations
from this thread are measured under this tag.
You must call `System.endAllocTag()` to do the matching pop.

Example:

```
System.beginAllocTag("User");
loadChapter(3);
System.endAllocTag();
```

Names that do not match a known tag name (`TVPAllocTag` enumerator names: `TJS2` / `User` / `GraphicsLoader`,
etc.) are treated as **User**.

**See also:** [System.endAllocTag](System.md#endalloctag)

---

### endAllocTag

Method

**Description**

Ends a memory allocator tag scope

Pops the tag pushed with [System.beginAllocTag](System.md#beginalloctag).

**See also:** [System.beginAllocTag](System.md#beginalloctag)

---

### setMemoryOverlay

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enable` | `&nbsp;` | true to show, false to hide. If omitted (or void),<br>the current state is toggled. |

**Return value**

The resulting state as true (1) or false (0).

**Description**

Sets the memory status overlay

Toggles the overlay that shows the engine's memory status in real time at the top right of the screen.
The flag itself toggles in every build, but
**only OGL-family draw devices (`OGLDrawDevice` / `SDLOGLDrawDevice`)
and SDL's `SDLDrawDevice` draw it**. The default `BasicDrawDevice` (D3D11) of the native Windows (WINVER) build
has no drawing hook, so the overlay is not shown there, but
it is shown in WINVER too if you switch `Window.drawDevice` to an OGL-family device.

---

### setPadOverlay

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enable` | `&nbsp;` | true to show, false to hide. If omitted (or void),<br>the current state is toggled. |

**Return value**

The resulting state as true (1) or false (0).

**Description**

Sets the gamepad status overlay

Toggles the overlay that shows the gamepad's 16 buttons and the analog values of its 6 axes at the top left of the screen.
The flag itself toggles in every build, but
**only OGL-family draw devices (`OGLDrawDevice` / `SDLOGLDrawDevice`)
and SDL's `SDLDrawDevice` draw it**. The default `BasicDrawDevice` (D3D11) of the native Windows (WINVER) build
has no drawing hook, so the overlay is not shown there, but
it is shown in WINVER too if you switch `Window.drawDevice` to an OGL-family device
(pad state is obtained through a logical layer shared by all builds, so WINVER also
shows the XInput pad name, buttons and axes).

---

### setDrawStatsLog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enable` | `&nbsp;` | true to log, false to stop. If omitted (or void),<br>the current state is toggled. |

**Return value**

The resulting state as true (1) or false (0).

**Description**

Sets drawing statistics logging

In builds with `KRKRZ_DRAW_STATS=ON`, while MemoryOverlay is shown, toggles a mode that writes
`DrawThreadPool` usage statistics to the log every 500 ms.
Use it on target hardware (game consoles, etc.) when the real-time display scrolls too fast to read.
Calling it in OFF builds or while MemoryOverlay is hidden does no harm,
but nothing is logged.

---

### getTextureMemory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tag` | `&nbsp;` | If you pass a string, the usage is also written to the log as one line labeled with that name.<br>Use it to mark points such as scene boundaries. If omitted, nothing is logged. |

**Return value**

Dictionary of usage values

**Description**

Gets GL texture memory usage

Returns the memory usage of textures and the like allocated by GL-family draw devices, as a dictionary.
The CPU-side memory covered by allocator and process usage (`.mem` in the REPL, etc.) does not include
textures allocated by the GL driver, so they are measured separately here.

The returned dictionary has the following members (in bytes).

| Member | Contents |
|---|---|
| `texture` | Total of [Texture](Texture.md) (GL texture) objects |
| `pbo` | Total of upload PBOs. **Only textures that get updated have one** (allocated lazily) |
| `total` | `texture` + `pbo` |
| `peak` | Maximum of the total |
| `textureCount` | Number of live textures |
| `pboCount` | Number of live PBOs |

`peak` is the maximum of a total that also includes the FBOs used by [Offscreen](Offscreen.md),
so when FBOs are in use it is larger than `total` (`total` does not include FBOs).

**Exists only in SDL3 / LIB builds with OpenGL drawing enabled.**
The WINVER build does not currently have it.

**See also:** [System.setTextureMemoryLog](System.md#settexturememorylog) / [System.resetTextureMemoryPeak](System.md#resettexturememorypeak)

---

### setTextureMemoryLog

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `enable` | `&nbsp;` | true to log, false to stop. If omitted (or void),<br>the current state is toggled. |

**Return value**

The resulting state as true (1) or false (0).

**Description**

Sets GL texture memory logging

Toggles a mode that writes usage to the log each time the GL texture memory total increases or decreases by 8MiB.
Disabled by default.

**Exists only in SDL3 / LIB builds with OpenGL drawing enabled.**

**See also:** [System.getTextureMemory](System.md#gettexturememory)

---

### resetTextureMemoryPeak

Method

**Description**

Resets the GL texture memory peak

Resets the `peak` returned by [System.getTextureMemory](System.md#gettexturememory) to the current value.
Use it when you want to measure "the maximum from here on".

**Exists only in SDL3 / LIB builds with OpenGL drawing enabled.**

**See also:** [System.getTextureMemory](System.md#gettexturememory)

---

### getJoypadCount

Method

**Return value**

Number of gamepads (integer).

**Description**

Gets the number of connected gamepads

Returns the number of gamepads currently recognized as connected.

**See also:** [System.hasJoypad](System.md#hasjoypad)

---

### hasJoypad

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `0` | Gamepad number (default 0). |

**Return value**

true if connected, false otherwise.

**Description**

Checks whether a gamepad is connected

Returns whether the gamepad with the specified number is connected.

**See also:** [System.getJoypadCount](System.md#getjoypadcount)

---

### getPadAxis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Pad number (0 = the last used pad, 1 and above = actual pads in connection order). |
| `axisId` | `&nbsp;` | Axis ID. |

**Return value**

The axis analog value as a real number.

**Description**

Gets a gamepad axis analog value

Returns the analog value of the specified axis of the specified pad. Use constants such as
`System.padAxisLeftX` for the axis ID.

Range of the return value:

- Stick axes (LeftX / LeftY / RightX / RightY) ... -1.0 to +1.0
- Trigger axes (LeftTrigger / RightTrigger) ... 0.0 to +1.0

0.0 is returned if the pad is not connected, the axis ID is invalid, and so on.

**See also:** [System.padAxisLeftX](System.md#padaxisleftx) / [System.padAxisLeftY](System.md#padaxislefty) / [System.padAxisRightX](System.md#padaxisrightx) / [System.padAxisRightY](System.md#padaxisrighty) / [System.padAxisLeftTrigger](System.md#padaxislefttrigger) / [System.padAxisRightTrigger](System.md#padaxisrighttrigger)

---

### rumblePad

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | Pad number (0 = the last used pad). |
| `low` | `&nbsp;` | Strength of the low-frequency motor (0–255). |
| `high` | `&nbsp;` | Strength of the high-frequency motor (0–255). |
| `duration` | `&nbsp;` | Duration in milliseconds. |

**Return value**

true if started successfully, false otherwise.

**Description**

Starts gamepad vibration

Drives the rumble motors of the specified pad.

**See also:** [System.stopRumblePad](System.md#stoprumblepad)

---

### stopRumblePad

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `0` | Pad number (default 0). |

**Return value**

true if stopped successfully, false otherwise.

**Description**

Stops gamepad vibration

Stops vibration started with [System.rumblePad](System.md#rumblepad).

**See also:** [System.rumblePad](System.md#rumblepad)

---

### getLicenseList

Method

**Return value**

Array of license information (dictionaries)

**Description**

Gets the license list

Returns a list combining the license information of third-party components built into the engine and plugins with
the license files placed in the project's `licenses/` folder
(`licenses/*.txt` or `.md`).
It is the information source for building an in-game license screen (such as a font selection screen)
freely in script.

Each element is a dictionary with the following members:
+ `name` : display name (pass it to `getLicenseText`)
+ `group` : category ("engine" / "font" / "font-engine" / "audio" / "video" /
"ui" / "platform" / "plugin:..." / "data", etc.)
+ `source` : origin ("builtin" = built into the engine / "plugin" = registered by a plugin /
"storage" = the project's licenses/ folder)

If a license with the same name comes from several origins, they are merged into one entry
(priority: plugin registration > built into the engine > storage).

**See also:** [System.getLicenseText](System.md#getlicensetext)

---

### getLicenseText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | License name |

**Return value**

License text (void if not found)

**Description**

Gets license text

Gets the full license text as a string, given a `name` from [System.getLicenseList](System.md#getlicenselist).
Returns void if not found.

Files placed in the project's `licenses/` folder (such as the license text of an added font)
can be retrieved with the same name resolution
(`licenses/<name>.txt`, or `.md` if that does not exist).

**See also:** [System.getLicenseList](System.md#getlicenselist)

---

### readEnvValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Environment variable name. |

**Return value**

The value of the environment variable. void if it is not set.

**Description**

Gets an environment variable

Available in both WINVER and SDL3-family builds.

**See also:** [System.writeEnvValue](System.md#writeenvvalue) / [System.expandEnvString](System.md#expandenvstring)

---

### writeEnvValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Environment variable name. |
| `value` | `&nbsp;` | Value to set. An empty string removes the environment variable. |

**Return value**

The value before setting. void if it was not set.

**Description**

Sets an environment variable

The setting affects only this process (and child processes launched from it).

**See also:** [System.readEnvValue](System.md#readenvvalue)

---

### expandEnvString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to expand. |

**Return value**

The expanded string.

**Description**

Expands environment variables

Replaces `%NAME%` in a string with the value of the environment variable.
A `%NAME%` with no matching environment variable is left as is, and `%%` becomes a single `%`
(the same rules as Win32 ExpandEnvironmentStrings).

**See also:** [System.readEnvValue](System.md#readenvvalue)

---

### urlencode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | String to convert. |
| `utf8` | `true` | If true (default), converts as a UTF-8 byte sequence; if false, as a system<br>multibyte string. |

**Return value**

The converted string.

**Description**

URL-encodes a string

Converts everything other than RFC 3986 unreserved characters (alphanumerics and `-` `_` `.` `~`) to `%XX`.
Spaces also become `%20` (not `+`).
```tjs
System.urlencode("a b&c=d");   // "a%20b%26c%3Dd"
System.urlencode("あ");         // "%E3%81%82"
```

**See also:** [System.urldecode](System.md#urldecode)

---

### urldecode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | String to convert. An exception is raised if it contains an invalid `%XX`. |
| `utf8` | `true` | If true (default), interprets as UTF-8; if false, as a system multibyte string. |

**Return value**

The converted string.

**Description**

URL-decodes a string

Converts `%XX` back to the original bytes and returns a string. `+` is not converted back to a space.

**See also:** [System.urlencode](System.md#urlencode)

---

### getAboutString

Method

**Return value**

The version information string.

**Description**

Gets the version information string

Returns the version information text of the engine and bundled libraries, the same as shown by the
`-about` command-line option.

---

### breathe

Method

**Description**

Processes messages

Call it in the middle of a long operation to process only OS messages so the window does not appear
unresponsive. TJS events are not delivered while it runs.

---

### getMonitorInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nearest` | `&nbsp;` | true to return the nearest monitor when no monitor overlaps the target. |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Return value**

A dictionary of monitor information.

**Description**

Gets monitor information

Returns monitor information as a dictionary of the following form. Rectangles are in screen coordinates.
```tjs
%[ name:"\\.\DISPLAY1", primary:1,
monitor:%[ x:0, y:0, w:3840, h:2160 ],   // モニタ全体
work:   %[ x:0, y:0, w:3840, h:2064 ] ]  // タスクバー等を除いた作業領域
```
The target depends on the number of arguments.

| Arguments | Target |
|---|---|
| None | Primary monitor |
| `(nearest, window)` | The monitor containing that window |
| `(nearest, x, y)` | The monitor containing that point |
| `(nearest, x, y, w, h)` | The monitor overlapping that rectangle |

If `nearest` is true, the nearest monitor is returned; if false, void is returned when no monitor overlaps.

Available in both WINVER and SDL3-family builds. In environments without the concept of a monitor
(such as platforms that are always full screen), void is returned.

**See also:** [System.getDisplayMonitors](System.md#getdisplaymonitors)

---

### getDisplayMonitors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | Left edge of the rectangle (optional). |
| `y` | `&nbsp;` | Top edge of the rectangle (optional). |
| `w` | `&nbsp;` | Width of the rectangle (optional). |
| `h` | `&nbsp;` | Height of the rectangle (optional). |

**Return value**

An array of monitor information. An empty array in environments without the concept of a monitor.

**Description**

Gets the list of monitors

Returns an array of information for all monitors (same form as [System.getMonitorInfo](System.md#getmonitorinfo)).
If you specify a rectangle, only monitors overlapping it are returned, and the overlapping part
is stored in each element's `intersect` (`%[ x, y, w, h ]`).

In SDL3-family builds, the order of monitors reflects the current moment. It changes when monitors are plugged or unplugged,
so do not store and reuse indexes.

**See also:** [System.getMonitorInfo](System.md#getmonitorinfo)

---

### getSystemMetrics

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Name of the metric. |

**Return value**

The value. void for an unknown name.

**Description**

Gets system metrics

Gets a Win32 GetSystemMetrics value by name. The name is the part without `SM_`
(`"CXSIZEFRAME"` / `"CYCAPTION"` / `"CMONITORS"`, etc.; case-insensitive).

WINVER build only. SDL3-family builds do not have this method.

---

## Plugin extension: process

### Members

#### Methods

- [commandExecute](#commandexecute)

---

### commandExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program |
| `param` | `&nbsp;` | Arguments |
| `timeout` | `0` | Timeout (ms) |

**Return value**

%[
status:   one of the strings ok/error/timeout,
stdout:   array of console output strings (split by line)
exitcode: exit code (only when status=="ok"),
message:  error message (only when status!="ok")
];

**Description**

Runs a command-line program and captures its console output

There is no background processing. Kirikiri stops until the program being run exits.

---

## Plugin extension: shellExecute

### Members

#### Methods

- [commandExecute](#commandexecute)

---

### commandExecute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Program |
| `param` | `&nbsp;` | Arguments |
| `timeout` | `0` | Timeout (ms) |

**Return value**

%[
status:   one of the strings ok/error/timeout,
stdout:   array of console output strings (split by line)
exitcode: exit code (only when status=="ok"),
message:  error message (only when status!="ok")
];

**Description**

Runs a command-line program and captures its console output

There is no background processing. Kirikiri stops until the program being run exits.

---

## Plugin extension: stdio

Standard I/O extensions to the System class

### Members

#### Properties

- [stdioState](#stdiostate)

#### Methods

- [attachConsole](#attachconsole)
- [allocConsole](#allocconsole)
- [freeConsole](#freeconsole)
- [stdin](#stdin)
- [stdout](#stdout)
- [stderr](#stderr)
- [flush](#flush)

---

### stdioState

Property \ Access: `r/w`

**Description**

Returns the connection state of standard I/O

---

### attachConsole

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bind` | `0` | 0: connect only the unconnected parts; otherwise: force-connect the specified parts<br>Bitwise OR of standard input:0x01, standard output:0x02, standard error:0x04 |

**Return value**

Whether it succeeded

**Description**

Connects standard I/O to an existing console

---

### allocConsole

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bind` | `0` | 0: connect only the unconnected parts; otherwise: force-connect the specified parts<br>Bitwise OR of standard input:0x01, standard output:0x02, standard error:0x04 |

**Return value**

Whether it succeeded

**Description**

Creates a console and connects standard I/O to it

---

### freeConsole

Method

**Return value**

Whether it succeeded

**Description**

Detaches from the console

---

### stdin

Method

**Return value**

The text read

**Description**

Reads text from standard input. Input is blocking.

---

### stdout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `string` | `&nbsp;` | Message to write |

**Description**

Writes a string to standard output

---

### stderr

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `string` | `&nbsp;` | Message to write |

**Description**

Writes a string to standard error

---

### flush

Method

**Description**

Flushes standard output

---

## Plugin extension: systemEx

Manual written as pseudo-code

### Members

#### Methods

- [writeRegValue](#writeregvalue)
- [readEnvValue](#readenvvalue)
- [writeEnvValue](#writeenvvalue)
- [expandEnvString](#expandenvstring)
- [urlencode](#urlencode)
- [urldecode](#urldecode)
- [getAboutString](#getaboutstring)
- [confirm](#confirm)
- [waitForAppLock](#waitforapplock)
- [setDpiAwareness](#setdpiawareness)
- [getOSVersion](#getosversion)
- [getKnownFolderPath](#getknownfolderpath)
- [processApplicationMessages](#processapplicationmessages)
- [handleApplicationMessage](#handleapplicationmessage)
- [setDefaultDllDirectories](#setdefaultdlldirectories)
- [addDllDirectory](#adddlldirectory)
- [removeDllDirectory](#removedlldirectory)

---

### writeRegValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | Destination key (specified as with readRegValue, e.g. HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\hoeg\\installdir) |
| `value` | `&nbsp;` | Value to write (string or integer) |

**Description**

Writes data to the registry

---

### readEnvValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Environment variable name |

**Return value**

The environment variable value (void if undefined)

**Description**

Gets an environment variable

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.readEnvValue](System.md#readenvvalue) for the specification.

---

### writeEnvValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Environment variable name |
| `value` | `&nbsp;` | Value to set |

**Return value**

The previous environment variable value (void if undefined)

**Description**

Sets an environment variable

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.writeEnvValue](System.md#writeenvvalue) for the specification.

---

### expandEnvString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to expand |

**Return value**

The expanded string

**Description**

Expands "%...%" in a string with environment variables

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.expandEnvString](System.md#expandenvstring) for the specification.

---

### urlencode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | Source string |
| `utf8` | `true` | true to output as UTF-8 |

**Return value**

The URL-encoded string

**Description**

Performs URL encoding

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.urlencode](System.md#urlencode) for the specification.

---

### urldecode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | Source string |
| `utf8` | `true` | true to process as UTF-8 |

**Return value**

The URL-decoded string

**Description**

Performs URL decoding

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.urldecode](System.md#urldecode) for the specification.

---

### getAboutString

Method

**Return value**

Text (TVPGetAboutString)

**Description**

Gets the environment information text shown with Ctrl+F12

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [System.getAboutString](System.md#getaboutstring) for the specification.

---

### confirm

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Message to show |
| `caption` | `""` | Window caption string |
| `window` | `void` | If specified, the window is shown with it as the parent |

**Return value**

true if YES was pressed

**Description**

Shows a confirmation message window. The window is modal.

Note: in environments where the engine implements System.confirm, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).

---

### waitForAppLock

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `key` | `&nbsp;` | AppLock key string |
| `timeout` | `0` | Timeout (ms) |

**Return value**

true: success (the AppLock did not exist or disappeared within the timeout), false: timed out, (void: error)

Note: you do not need to call createAppLock again with the same key after this function (it would fail because you already own it)

**Description**

Waits for the mutex created by System.createAppLock in another process to be released, and takes ownership

---

### setDpiAwareness

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `context` | `&nbsp;` | : context value (-1 to -5)<br>DPI_AWARENESS_CONTEXT_UNAWARE              : -1<br>DPI_AWARENESS_CONTEXT_SYSTEM_AWARE         : -2<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE    : -3<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 : -4 (Creators Update or later)<br>DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED    : -5 (October 2018 update or later) |

**Return value**

The previous value (0 if it could not be set)

**Description**

Sets DPI awareness

Effective on Windows 10 Redstone 1 (version 1607) and later

---

### getOSVersion

Method

**Return value**

void or %[ major, minor, build, platform, spmajor, spminor, servevicepack, suite, type ];

**Description**

Gets detailed OS version information

See the RtlGetVersion API and the RTL_OSVERSIONINFOW structure.

---

### getKnownFolderPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `folderid` | `&nbsp;` | FOLDERID to get (String or GUID octet) |
| `flags` | `0` | KF_FLAG_* value (KF_FLAG_CREATE = 0x00008000, etc.) |

**Return value**

The resulting local path string, "" (unknown), or void (failure)

**Description**

SHGetKnownFolderPath wrapper

If the FOLDERID is a string, specify the {} part of FOLDERID_{}. For a GUID, specify a 16-byte octet such as <% 00000000 0000 0000 0000 0000000000000 %>.
As a special value unique to this function, "Captures" can be specified as folderid (the Game Bar capture folder [Video\Captures]; behaves the same as specifying GUID {EDC0FE71-98D8-4F4A-B920-C8DC133CB165})

---

### processApplicationMessages

Method

**Description**

Processes messages (calls the engine's TVPProcessApplicationMessages())

Unlike System.breathe(), Kirikiri events are also processed.
Note that processApplicationMessages basically does not return until the application exits.

If an exception occurs in an event handler, it is not propagated from this method.
The plugin simply passes the call through to the engine; the exception is caught by the engine's event delivery
and handled as a normal unhandled script exception (exception dialog / log
output, or notification to System.exceptionHandler if it is set).

---

### handleApplicationMessage

Method

**Description**

Processes one message (calls the engine's TVPHandleApplicationMessage())

Exceptions are handled the same way as in processApplicationMessages.

---

### setDefaultDllDirectories

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `flags` | `&nbsp;` | Combination of lls* flags |

**Return value**

true on success

**Description**

::SetDefaultDllDirectories wrapper

---

### addDllDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Local path to add (convert it with Storages.getLocalName first) |

**Return value**

A unique value to pass to removeDllDirectory (0 means failure)
Set the llsUserDirs flag with setDefaultDllDirectories beforehand

**Description**

::AddDllDirectory wrapper

---

### removeDllDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `cookie` | `&nbsp;` | Unique value from addDllPath to remove |

**Return value**

true on success

**Description**

::RemoveDllDirectory wrapper

---

## Plugin extension: tftSave

System extensions

### Members

#### Methods

- [savePreRenderedFont](#saveprerenderedfont)
- [loadPreRenderedFont](#loadprerenderedfont)
- [modifyPreRenderedFont](#modifyprerenderedfont)

---

### savePreRenderedFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | File name to save to |
| `characters` | `&nbsp;` | Array of characters (character codes) to save |
| `callback` | `&nbsp;` | Callback that provides the information and image<br>It must be a function that takes a character code and returns a layer (PreRenderedFontImage)<br>function(ch) { return layer; } |

**Description**

Saves pre-rendered font data to a file

---

### loadPreRenderedFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | File name to load |
| `characters` | `&nbsp;` | Array that receives the list of characters |
| `callback` | `&nbsp;` | A callback that receives images is planned for the future (currently you must always pass void) |

**Description**

Loads pre-rendered font data from a file

---

### modifyPreRenderedFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | File name to load |
| `callback` | `&nbsp;` | Callback for getting and updating information<br>function(ch, info = %[ blackbox_x\|y, origin_x\|y, inc_x\|y, inc ]) { return true_if_modofied; } |

**Description**

Updates glyph information in pre-rendered font data (only origin_x|y, inc_x|y and inc can be changed; blackbox is fixed)

---

## Plugin extension: windowEx

System extensions

Note: the engine's System also has getMonitorInfo / getDisplayMonitors / breathe /
readEnvValue / expandEnvString (WINVER / SDL3 family) and getSystemMetrics (WINVER).
Loading this plugin replaces them with the plugin versions.

### Members

#### Methods

- [getDisplayMonitors](#getdisplaymonitors)
- [getDisplayMonitors](#getdisplaymonitors)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [setDpiAwareness](#setdpiawareness)
- [setCursorPos](#setcursorpos)
- [getCursorPos](#getcursorpos)
- [setClipCursor](#setclipcursor)
- [getSystemMetrics](#getsystemmetrics)
- [getDoubleClickTime](#getdoubleclicktime)
- [readEnvValue](#readenvvalue)
- [expandEnvString](#expandenvstring)
- [setApplicationIcon](#setapplicationicon)
- [setIconicPreview](#seticonicpreview)
- [breathe](#breathe)
- [isBreathing](#isbreathing)
- [findWindowEx](#findwindowex)
- [classLongPtr](#classlongptr)
- [loadCursor](#loadcursor)
- [mapVirtualKey](#mapvirtualkey)

---

### getDisplayMonitors

Method

**Return value**

[ %[ name, primary, monitor:%[ x, y, w, h ], work:%[ x,y,w,h ], intersect:%[ x,y,w,h ] ], ... ];
name:      monitor name ('\\.\DISPLAY?', etc.)
primary:   whether it is the primary monitor
monitor:   dictionary of the monitor's area
work:      the monitor's work area (the visible area when a window is maximized, etc.)
intersect: area intersecting the specified range (same as monitor if no range is specified)

**Description**

Gets the list of monitor information

If a range (x, y, w, h) is specified, only monitors that intersect it are returned. If all are omitted, all monitors are returned.
Enumerates all monitors.

---

### getDisplayMonitors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Description**

Enumerates only monitors intersecting the specified range

---

### getMonitorInfo

Method

**Return value**

%[ name, primary, monitor:%[ x, y, w, h ], work:%[ x, y, w, h ] ];
Monitor information. The dictionary contents are the same as getDisplayMonitors (but without intersect).
When near=false and there is no monitor, void is returned.

**Description**

Gets monitor information

Returns the primary monitor.

---

### getMonitorInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Description**

Returns the monitor at the specified coordinates

---

### getMonitorInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Description**

Returns the monitor that most overlaps the specified range

---

### getMonitorInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `window` | `&nbsp;` |  |

**Description**

Returns the monitor that most overlaps the specified window

---

### setDpiAwareness

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `context` | `&nbsp;` |  |

**Description**

Calls SetThreadDpiAwarenessContext

---

### setCursorPos

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**Return value**

When getting: %[ x, y ], or void if it could not be obtained

**Description**

Sets or gets the screen coordinates of the mouse cursor

---

### getCursorPos

Method

---

### setClipCursor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `win_or_rect` | `&nbsp;` |  |

**Description**

Clips the cursor position

---

### getSystemMetrics

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | The "*" part of SM_* as a string (case-insensitive) |

**Return value**

Metric value (meaning depends on index)

**Description**

Gets system metrics information

See the GetSystemMetrics() API documentation for details.
SW_ARRANGE has no ARW_* definitions, so compare against numeric values directly.

---

### getDoubleClickTime

Method

**Return value**

Time (ms). The default is 500 ms

**Description**

Gets the system double-click time

See the GetDoubleClickTime() API documentation for details.
The allowed movement range for a double click can be obtained with CXDOUBLECLK/CYDOUBLECLK of getSystemMetrics.
Use this when detecting double clicks in software without Layer.onDoubleClick (a fixed time would also work, but just in case...).

---

### readEnvValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Environment variable name |

**Return value**

The environment variable value (void if undefined)

**Description**

Gets an environment variable

---

### expandEnvString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to expand |

**Return value**

The expanded string

**Description**

Expands "%...%" in a string with environment variables

---

### setApplicationIcon

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | Icon file or void (void or "" resets to the initial state) |

**Description**

Changes the application icon shown in the taskbar, Alt+Tab and so on

Note: files inside archives cannot be specified. If an exe or DLL is specified, its first icon is used.

---

### setIconicPreview

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `iconic` | `&nbsp;` | true to show the icon instead of a thumbnail; false to clear the setting |

**Return value**

Whether it succeeded (always fails on XP and earlier)

**Description**

Forces the thumbnail in the taskbar and Alt+Tab (Vista and later) to show the application icon

Note: DWMWA_FORCE_ICONIC_REPRESENTATION is set on the application window.

---

### breathe

Method

**Description**

Wrapper for TVPBreathe and TVPGetBreathing

---

### isBreathing

Method

---

### findWindowEx

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `winname` | `void` | Window name |
| `clsname` | `void` | Class name |
| `parwin` | `void` | Parent window (a Window object or an HWND number) |
| `childafter` | `void` | Window to start searching after (same as above) |

**Return value**

The HWND as a number on success

**Description**

Wrapper for the Win32 API FindWindowEx

---

### classLongPtr

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `win` | `&nbsp;` | Target window (a Window object or an HWND number) |
| `key` | `&nbsp;` | Target index. The current implementation accepts one of the strings {cursor,icon,iconsm,brbackground} |
| `setvalue_or_getasvoid` | `void` | void to get; a number to set (for key=brbackground, a stock brush from {black,white,gray,ltgray,dkgray} can also be specified) |

**Return value**

On success, the current (or previous) LONG_PTR value; void on failure

**Description**

Wrapper for {Get,Set}ClassLongPtr

---

### loadCursor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `idc_or_res` | `&nbsp;` | A number >= 0 is treated as MAKEINTRESOURCE, a number < 0 as crXXXX, and a string as a resource name |
| `hmodule` | `void` | HMODULE value of the resource's module |

**Return value**

HCURSOR value

**Description**

Wrapper for LoadCursor

---

### mapVirtualKey

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `code` | `&nbsp;` | Virtual key code or scan code |
| `maptype` | `&nbsp;` | MAPVK_* value |

**Return value**

keycode

**Description**

Wrapper for MapVirtualKey

---
