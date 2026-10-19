---
source_hash: eb53fe88e869
---

# Command-Line Options

## Command-Line Options

In addition to specifying Kirikiri's command-line options on the command line, you can save them to a configuration file with

( krkrrel.exe ) or

( -userconf ).

Options are read in the following order:

1. Options embedded in the Kirikiri engine
2. The .cf file in the same directory as the Kirikiri core
3. The .cfu file in the data storage location, written by "Engine Configuration" (-userconf)
4. Options specified on the command line

If a .cf or .cfu file does not exist, it is simply ignored. Options read later take precedence.

### Configuration File Names and Locations

| | Native Windows build | SDL3 build (desktop) | SDL3 build (other) |
|---|---|---|---|
| Same location as the exe | `<exe name>.cf` | `<exe name>.cf` → `config.cf` | `config.cf` |
| Data storage location | `<exe name>.cfu` | `<exe name>.cfu` | ( not read ) |

`<exe name>.cf` is the executable's file name with the extension changed to `.cf` (`krkrz64.cf` for
`krkrz64.exe`). The SDL3 build on desktop (Windows / macOS / Linux) follows the same convention as the
native Windows build. The traditional fixed name `config.cf` is still read, but
**if both exist, `<exe name>.cf` takes precedence**.

On Android / iOS / browsers (wasm) / embedded devices, "next to the executable" and the data storage
location are not necessarily local paths, so only `config.cf` is read, as before.

### Configuration Files Embedded in the Executable

There are also configuration files inside the resources embedded in the executable
(SDL3-based builds; the native Windows build keeps its embedded options as resources
of the executable).

- `resource/config.cf` … common to all platforms
- `resource/config_<tag>.cf` … per platform ( tag = [System.platformTag](../reference/System.md#platformtag) )

Use these when you want to share the same resource files across multiple platforms while keeping
only the per-device settings separate. They are read in the order "specific tag → general tag → common `config.cf`",
and **whichever is read first takes precedence** (files that do not exist are simply skipped).

### Configuration File Format

Write one option per line, **without the leading `-`**.

```
; 行頭が ';' の行はコメント
datapath="$(exepath)\savedata"
readencoding=UTF-8
lowpri
```

- The format is `name=value`. If you omit `=` and what follows, the value is `yes` (`lowpri` above).
- A value enclosed in `"` or `'` is interpreted as a TJS string literal
  (escapes are available). The `.cfu` written by `-userconf` uses this form.
- Trailing line breaks, surrounding whitespace, and a leading BOM are removed automatically. Line endings
  can be either CRLF or LF.

> **Note:**
> Trailing line-break removal is the behavior of builds from 2026-08 onward. Before that, the trailing line break
> was included in the value, so unquoted values and lines with the value omitted did not work correctly.



A command-line option basically consists of a '-' (hyphen) followed by the option name, then '=' and the option value.

For example, if the value of the -cdvol option is direct, specify -cdvol=direct.



Apart from the "startup options", "debugging options", and "system compatibility options", most of these options are for fine-tuning to work around environment-specific problems.

For solving environment-specific problems, see also [Environment-Dependent Problems](ComputerDependentProblems.md).

> **Note:**
> Releaser and -userconf can change these options by rewriting the Kirikiri executable or an external configuration file, but the defaults are usually fine. **We do not recommend distributing executables or configuration files with these options left at non-default values just because there was a problem in the creator's own environment** (of course, some options, such as -datapath, should be set according to how the product is distributed and used).

Options marked "can be changed dynamically" in the list below can be changed with the [System.setArgument](../reference/System.md#setargument) method. Other options cannot be changed dynamically.

### Argument Separator ( `--` ) and File Arguments

Command-line arguments are handled as follows.

- `-name[=value]` is an option (if the value is omitted, it is `yes`).
- An argument without a leading hyphen specifies the project folder (or archive).
- Everything after a standalone `--` is not read as options but passed to the script as arguments.
  They can be retrieved in order with [System.getArgument](../reference/System.md#getargument) under the names `-arg0` / `-arg1` / ….

```text
krkrz64.exe D:/game/ -loglevel=info -- -mode a.txt
→ プロジェクト: D:/game/、オプション: -loglevel=info、-arg0=-mode、-arg1=a.txt
```

If you want to treat "all arguments as file names received by the script", for example in a tool that opens associated files,
use the security option `acceptfilenameargument` embedded in the engine
(an item of `TVPSystemSecurityOptions`; determined by the value at build time, or by a same-length rewrite of the executable).

| `acceptfilenameargument` | Behavior |
|---|---|
| 0 ( default ) | As described above |
| 1 | All arguments become `-argN`. Neither options nor the project are read |
| 2 | If there is a standalone `--`, the `-name[=value]` arguments before it are read as options, and the arguments without a hyphen before it plus everything after `--` become `-argN` (in that order). Without `--`, same as 1 |

With 1 and 2, arguments without a hyphen are not used to specify the project (the project is found automatically from
`data.xp3` / the `data` folder next to the executable, etc.). With 2, even a tool that receives file arguments can take
options such as `-datapath` / `-loglevel` / `-replfile` on the command line.

```text
( acceptfilenameargument=2 )
tool.exe -replfile=D:/ch -datapath=D:/ch/sd -- -batch a.mmo
→ オプション: -replfile / -datapath、-arg0=-batch、-arg1=a.mmo
```

## Startup Options

The following options invoke only specific features of Kirikiri.

- **-**userconf** (launch the end-user configuration tool)**  
  Launches the end-user configuration tool built into the engine ( [Kirikiri Configuration](Configure.md) ). The game does not start; the configuration screen opens in a browser (Windows / Linux / macOS; shared by the native Windows (WINVER) build and the SDL build).
- **-**userconfbrowser** (how to open the configuration screen)**  
  Specifies how the -userconf configuration screen is opened. The value is one of **'app' (default; Edge / Chrome app window, or the default browser if neither is available)**, **'default' (the default browser)**, or **'none' (do not open)**. With 'none', the URL of the configuration screen is written to the log; open it in a browser.
- **-**about** (show the copyright information dialog)**  
  Shows the "Version, copyright, and environment information" dialog. It also shows the list of licenses of the bundled components (the full text can be retrieved with -license=<name>).
- **-**sel** (show the "Select folder/archive" dialog)**  
  Shows the "Select folder/archive" dialog. Data such as data.xp3 is not detected automatically.
  
  If you specify a folder as a command-line parameter (without a leading hyphen), the "Select folder/archive" dialog opens with that folder initially selected.
- **-**nosel** (suppress the "Select folder/archive" dialog / native Windows (WINVER) build only)**  
  Does not show the "Select folder/archive" dialog that appears when the data folder cannot be determined, and continues the startup process. No value is needed.
  
  Specify this when a dialog stopping the process would be a problem, such as when printing information and exiting like -about / -license, or when starting without data and beginning processing from the REPL.
- **-**printdatapath** (print the data storage location)**  
  Prints the data storage location setting (the -datapath option) followed by a newline to standard output, and exits. This option is intended for external applications that manage save data in cooperation with the Kirikiri engine.
  
  Special strings such as $(exepath) in the data storage location are printed after substitution.
  
  Because the Kirikiri engine is a GUI application, simply running the Kirikiri executable with -printdatapath from the command prompt displays nothing. Use a pipe or redirection to capture the output.
- **-**license** (print the bundled licenses)**  
  Prints the license information held by the engine, plugins, and project data to standard output, and exits.

  | Specification | Output |
  |---|---|
  | `-license` | List ( name / category / supplier ) |
  | `-license=<name>` | Full license text of that one entry |
  | `-license=all` | Full license text of all entries |

  In addition to the entries built into the engine, the list includes entries registered by loaded plugins and text files placed in the project's `licenses` folder ( `licenses/*.txt` ). To retrieve them from TJS at run time, use [System.getLicenseList](../reference/System.md#getlicenselist) / [System.getLicenseText](../reference/System.md#getlicensetext).

  Even if started without a project, the folder selection dialog is not shown (the license information is printed and the engine exits). If you start with a project, the entries in that project's `licenses` folder are also listed.

  As with -printdatapath, because the Kirikiri engine is a GUI application, simply running it from the command prompt displays nothing. Use a pipe or redirection to capture the output. Note that the startup information log goes to the same standard output, so extract the license information part when processing it by machine.
- **-**startup** (specify the startup script)**  
  Specifies the name of the script file to execute first.
  
  If not specified, startup.tjs is executed.
- **-**nostartup** (suppress automatic execution of the startup script / for `KRKRZ_REPL` builds)**  
  When specified, suppresses automatic execution of startup.tjs (and of the startup script specified with `-startup`). Use this with agent-driven `-repl` / `-replfile` setups when you want to start in an idle state without opening a window and begin processing by explicitly calling scripts from the REPL.
  
  The value is **'1'**, **'yes'**, **'true'**, **'on'** (enabled) or no value (enabled), or **'0'**, **'no'**, **'false'**, **'off'** (disabled). Disabled if not specified.
  
  When `-nostartup` is specified, the engine does not exit immediately even if the startup script is disabled and no window is created.

## General System Options

- **-**datapath** (data storage location)**  
  Sets the location (folder) where Kirikiri saves various data.
  
  The value is a string.
  
  You can simply specify a full folder path, but normally you embed the following special strings.
  
  - **$(exepath)**  
    Replaced with System.exePath (the folder containing the Kirikiri core).
  - **$(appdatapath)**  
    Replaced with System.appDataPath (the user's home folder). This folder is usually hidden.
  - **$(personalpath)**  
    Replaced with System.personalPath (the My Documents folder).
  - **$(vistapath)**  
    Replaced with $(appdatapath) on Vista or later, and with $(exepath) on earlier OSes.
  - **$(savedgamespath)**  
    Replaced with System.savedGamesPath (the folder for game save data). (1.1.0 or later)
  
  The description above applies to the Windows version. In **SDL3 builds other than Windows**, `$(appdatapath)` / `$(personalpath)` / `$(vistapath)` / `$(savedgamespath)` are all replaced with the **per-app user area** ( `user://`; the local paths described below on Linux and macOS ), which does not match the OS standard folders returned by [System.appDataPath](../reference/System.md#appdatapath) / [System.personalPath](../reference/System.md#personalpath) (such as `~/Library/Application Support/` on macOS).
  
  The default is "$(exepath)\savedata" (**except on Linux and macOS**; see below). This setting suits a distribution style where the program is compressed/archived as a zip or similar without an installer, and users extract it and run the program right away.
  
  However, with this default, if the program is placed under Program Files, writing files may fail with an error because there is no permission to write under Program Files, or when the program is run as a "limited user" on Windows XP and the like.
  
  Using a name such as "$(appdatapath)\application name" or "$(personalpath)\application name" writes to a per-user folder, which makes such problems less likely, but users may be confused because it is less obvious where the save data is stored.
  
  
  
  !!! warning "Important (changed in 2026-10): default storage location on Linux"
      The default on Linux (SDL3) is now **the per-user folder `~/.local/share/<organization name>/<application name>/`** (under `$XDG_DATA_HOME` if set; the organization and application names come from -orgname / -appname, or `wamsoft` / `krkrz` if not specified). It used to be `savedata` next to the executable, but that location is not writable when deployed as an AppImage / Flatpak / under `/opt`, and so on.

      - In distributed products, write `orgname` and `appname` in `<exe name>.cf` to determine a per-title folder. Match the Steam Cloud sync path to this folder as well.
      - To keep it next to the executable as before, specify `datapath="$(exepath)/savedata"`.
      - On Linux, `$(appdatapath)` / `$(personalpath)` / `$(vistapath)` / `$(savedgamespath)` are also replaced with this per-user folder (a local path). Values written with `\` separators are converted to `/`, and a trailing separator is added.
      - You can check the actual storage location in the startup log line `datapath (Linux default, ...)` / the data storage location line. If old default save data (`savedata*`) remains next to the executable, a warning prompting migration is shown.
      - Earlier Linux versions did not append `/` to the end of the default storage location, so `System.dataPath + "file name"` was written next to the executable as `savedatafile name`. If such files remain, move them to the new location.

  The default on macOS (SDL3) is also **the per-user folder `~/Library/Application Support/<organization name>/<application name>/`** (the same location as before). Since 2026-10-12 it is treated as a local path, and -datapath now takes effect (previously -datapath was ignored).

  A relative path is resolved against the current folder at startup (the same applies to the Windows version).

  When Kirikiri starts, it tries to create the data storage location specified by this option if it does not exist. Even if creation fails, processing continues instead of terminating, so handle errors in your own scripts (by catching exceptions such as failures to save data).
  
  
  
  Settings made with "Engine Configuration" are created in the folder specified as this data storage location. Various logs are also created in this folder by default.
- **-**contfreq** (processing wait)**  
  Sets whether to reduce CPU usage by calling processing such as transitions at a specified frequency with waits in between.
  
  The value is **'0' (no wait)** or a positive integer; if this option is not specified, '0' is assumed. A positive integer specifies the frequency in Hz.
  
  This option affects transitions and Continuous handlers registered with System.addContinuousHandler.
  
  With '0', processing uses the CPU fully while a transition is running, for example.
  
  With a number, processing runs at that frequency, and the CPU rests for the remaining time. This reduces the impact on other applications, CPU temperature rise, and the computer's power consumption. The lower the number, the stronger this effect. However, a low number may make transitions and the like less smooth.
  
  When vertical sync waiting is enabled with the waitvsync option, Continuous handlers are driven in step with vertical sync, and the contfreq setting is ignored.
  
  This option can be changed dynamically, but the change takes effect the next time transitions or Continuous handlers stop running.
- **-**eventexceptionlimit** (limit on consecutive exceptions from per-frame events)**  
  A guard for when events that fire repeatedly every frame, such as onDraw or Timer handlers, keep throwing exceptions. Consecutive exceptions are counted per source; when the limit is reached, that source is stopped automatically and a WARNING log is written.
  
  The value is a positive integer; if this option is not specified, **'10'** is assumed. Specifying **'0'** disables the guard.
  
  This is mainly to keep the same exception from occurring endlessly every frame in setups that "do not exit on exceptions", such as REPL-driven ones.
- **-**memusage** (memory usage)**  
  Sets memory usage.
  
  The value is **'normal'** or **'low'**; if this option is not specified, 'normal' is assumed.
  
  Choosing "low" uses memory more sparingly than "normal". However, "low" limits various caching mechanisms inside Kirikiri and the size of TJS2 hash tables, so performance drops. Also, with "low", "Graphics - image cache limit" is forced to "no caching".
- **-**laxtimer** (limit on accumulated timer events)**  
  Sets whether to limit the number of timer events that can be accumulated in the system at once (the maximum allowed backlog), avoiding situations where timer events pile up beyond what can be processed.
  
  The value is **'no'** or **'yes'**; if this option is not specified, 'no' is assumed.
  
  On very slow computers, or when very heavy processing is driven by a timer, Kirikiri may not keep up with timer events and may become slow to respond to user input. Specifying 'yes' always fixes the maximum backlog of timer events in the system at 1 (as if the Timer class's capacity property were 1). This suppresses timer events the system cannot keep up with, but timer precision and accuracy are usually lost.
- **-**lowpri** (low priority)**  
  Sets whether to lower the priority during transitions and the like.
  
  The value is **'no'** or **'yes'**; if this option is not specified, 'no' is assumed.
  
  With 'yes', the execution priority of the main thread is lowered when Kirikiri's main thread uses the CPU continuously, such as while a transition is running. This may relieve symptoms such as sound skipping during transitions or other applications becoming hard to use during transitions.
- **-**language** (explicitly set the message / display language)**  
  Explicitly sets the language of engine messages (error text, etc.) and option descriptions (the `-userconf` configuration UI).
  
  The value is in BCP-47 form ( **'ja-JP'**, **'en-US'**, **'zh-Hans'**, etc. ) or a short form ( **'ja'**, **'en'**, **'chs'**, **'cht'** ). If not specified, it follows the OS language setting ( [System.systemLanguage](../reference/System.md#systemlanguage) ). Supported languages are ja / en / chs / cht; languages without matching resources fall back to English (or Japanese if English is also unavailable).
  
  On the native Windows (WINVER) build it affects PE resource language resolution (message strings and the configuration dialog); on the SDL3 build it affects the selection of `messages*.json` / `optiondesc*.json`. **It affects message strings only when specified directly on the command line** (when specified in a configuration file, it affects only the language of option descriptions).
- **-**exceptionexe** (editor launched on exceptions)**  
  Specifies the editor to launch when an exception occurs.
- **-**exceptionarg** (options for the editor launched on exceptions)**  
  Specifies the options passed when launching the editor on an exception.
  
  You can simply specify arguments, but normally you embed the following special strings.
  
  - **%filepath%**  
    Replaced with the file path of the script where the exception occurred.
  - **%line%**  
    Replaced with the line number where the exception occurred.
- **-**appname** (application name / SDL3 build only)**  
  Specifies the application name used to determine the user data storage location ( `user://` ). If not specified, 'krkrz' is used.
  
  The storage location follows each OS's conventions (on Windows, organization name/application name under `%APPDATA%`). Specify it together with -orgname when you want to keep data of multiple applications separate on the same engine.
- **-**orgname** (organization name / SDL3 build only)**  
  Specifies the organization name used to determine the user data storage location ( `user://` ). If not specified, 'wamsoft' is used.
- **-**uselfh** (use LFH / native Windows (WINVER) build only)**  
  The value is **'yes'** or **'true'** (use); any other value, or no specification, means it is not used.
  
  Enables LFH (Low Fragmentation Heap), which reduces memory fragmentation. Since Windows Vista, the OS enables it by default, so you normally do not need to specify this.

### Memory Pool Sizes

At startup, the engine allocates a TLSF pool for each purpose-specific allocator all at once (for how to read the breakdown, see [Memory Observation](../topics/core/memory_observation.md)).

All of the following options take **an integer in MB**. Specifying **'none'** / **'off'** / **'0'** does not create that pool and uses malloc as before.

| Option | Target | Default |
|---|---|---|
| `-bitmappoolsize` | BitmapAllocator ( image areas of [Bitmap](../reference/Bitmap.md). The image cache limit also follows this ) | 512MB ( 128MB for 32-bit processes ) |
| `-filepoolsize` | FileAllocator ( file-layer cache. The cache budget also follows this ) | 256MB ( 64MB for 32-bit processes ) |
| `-krkrzpoolsize` | GlobalAlloc[Krkrz] ( allocations via `operator new` / `TJS_malloc` ) | 256MB ( 64MB for 32-bit processes ) |
| `-soundpoolsize` | SoundAllocator ( PCM / ring buffer / DSP work areas ) | 16MB |
| `-sdlpoolsize` | GlobalAlloc[SDL] ( only SDL3-based builds built with `KRKRZ_SDLMEMORY_STAT=ON` ) | 64MB |

Pools are allocated in full at startup, so making them larger reduces the memory available to the general-purpose heap (GL / TJS / image decoding, etc.). Especially in environments where the memory assigned to the application is fixed, adjust by increasing only the pools that turn out to be insufficient at the defaults. If a pool runs out, the engine simply falls back to malloc; it does not stop working.

### On-Demand Delivery with web:// ( browser (wasm) build only )

Settings for placing data on a server as individual files, without packing it into xp3, and fetching them one by one via `web://./<path>`.

- **-**webbase** (base URL for web://)**  
  Specifies the base URL used to resolve `web://` paths.
- **-**webmanifest** (name of the file list manifest)**  
  Specifies the name of the file list manifest (JSON) placed directly under the base URL. If not specified, 'krkrz_files.json' is used.
  
  Folder contents cannot be enumerated for individual files on a server, so the search table of [Storages.addAutoPath](../reference/Storages.md#addautopath) is built from this manifest.

## Input Options

- **-**wheel** (mouse wheel detection method)**  
  Sets how mouse wheel rotation is detected.
  
  The value is **'no' (do not use)** or **'message' (window messages)**; if this option is not specified, 'message' is assumed. Choosing "do not use" disables the mouse wheel.
  
  Note: the former 'dinput' (DirectInput) value has been removed. DirectInput was a workaround for
  old environments where `WM_MOUSEWHEEL` did not arrive in exclusive fullscreen, but
  the engine now uses D3D11 (borderless window), so window messages always detect the wheel,
  and the DirectInput dependency has been removed. For compatibility, 'dinput' is treated
  as 'message'.
- **-**joypad** (whether to use gamepads)**  
  Sets whether to use gamepads (joysticks).
  
  The only value is **'no' (do not use)**; specifying it disables gamepad functionality
  completely (neither state retrieval nor key event generation is performed). If not
  specified, gamepads are enabled, and are disabled automatically when none is connected.
  
  Note: the gamepad implementation has been redesigned on XInput (WINVER) / SDL_Gamepad (others)
  (the old 'dinput' value has been removed). Use 'no' for support purposes in rare cases where
  another device is mistakenly recognized as a gamepad and causes malfunctions
  (for the gamepad specification, see the Gamepad section).
- **-**paddelay** (gamepad key repeat delay)**  
  Specifies the time until gamepad (joystick) key repeat starts, in milliseconds.
  
  The value is a positive number or -1; -1 disables key repeat. If this option is not specified, 500 is assumed.
  
  This option can be changed dynamically.  
  
  **Effect on Elements screen navigation**: **only when this option is specified explicitly**, the same value is also used as the default for focus movement in Elements dialogs (holding the gamepad D-pad / stick). If not specified, the Elements defaults (400ms / linked to how far the stick is pushed) remain as before. If the screen JSON has `"input": { "repeat_delay_ms", "repeat_rate_ms" }`, that takes precedence (priority = screen JSON > this option > `input_defaults.jsonc` > built-in default).
- **-**padinterval** (gamepad key repeat interval)**  
  Specifies the gamepad (joystick) key repeat interval in milliseconds. The smaller the value, the faster the repeat.
  
  The value is a positive number; if this option is not specified, 30 is assumed.
  
  This option can be changed dynamically.  
  
  **Effect on Elements screen navigation**: **only when this option is specified explicitly**, the same value is also used as the default for focus movement in Elements dialogs (holding the gamepad D-pad / stick). If not specified, the Elements defaults (400ms / linked to how far the stick is pushed) remain as before. If the screen JSON has `"input": { "repeat_delay_ms", "repeat_rate_ms" }`, that takes precedence (priority = screen JSON > this option > `input_defaults.jsonc` > built-in default).
- **-**padbuttons** (gamepad button mapping scheme / SDL3 and generic builds only)**  
  Sets how physical gamepad buttons are mapped to `VK_PAD1`–`VK_PAD4`.
  
  The value is **'label' (map by the button's printed label)** or **'position' (map by the button's position)**; if this option is not specified, 'label' is assumed.
  
  With 'label', `VK_PAD1` is mapped to the button labeled A (✕ on PlayStation), `VK_PAD2` to B (○), `VK_PAD3` to X (□), and `VK_PAD4` to Y (△). Even on controllers where the A/B and X/Y positions are swapped, such as Nintendo-style controllers, the on-screen labels match the buttons actually pressed.
  
  'position' is the traditional mapping: bottom = `VK_PAD1`, right = `VK_PAD2`, left = `VK_PAD3`, top = `VK_PAD4`. On controllers whose labels cannot be determined, this mapping is used automatically even when 'label' is specified. PlayStation / Xbox-style controllers give the same result with either scheme.
  
  To change it at run time, use [System.padButtonMapping](../reference/System.md#padbuttonmapping).
  
  This option is effective only on SDL3 / generic builds. Gamepad input on the native Windows (WINVER) build is based on XInput, whose button labels are fixed to the Xbox layout, so positions and labels never disagree.
- **-**controlime** (IME state control)**  
  Sets whether to control the state of the IME (input method software for languages such as Japanese), e.g. enabling or disabling it.
  
  The value is **'yes'** or **'no'**; if this option is not specified, 'yes' is assumed.
  
  Choosing "no" may work around problems such as being unable to enter text in languages like Japanese that are entered through an IME.

## Sound Options

- **-**wsfreq** (sound output frequency)**  
  Sets the sampling frequency of sound output (the mixer).
  
  The value is a positive integer representing the frequency in Hz; if this option is not specified, '44100' is assumed.
  
  Especially in environments using WDM sound drivers (Windows 2000, XP or later, etc.), changing this setting may not change playback.
- **-**wspreinit** (initialize the audio device in advance)**  
  The value is **'yes'** or **'no'**; if this option is not specified, 'yes' is assumed.
  
  With 'yes', the audio device (the miniaudio engine) is initialized in advance at startup. With 'no', it is initialized when sound is first played, as before.
  
  If the device is opened only when sound is first played, playback starts late by the time it takes to open the device, and the beginning of the sound may be cut off. With 'yes' (the default), initialization is done at startup, which prevents this.
  
  If for some reason you want to avoid opening the device at startup (an unstable sound driver, etc.), specify 'no'.
- **-**opus_pcm_format** / **-**ogg_pcm_format** (decode output format)**  
  Specifying **'f32'** makes that codec's decode output IEEE 32-bit float. If not specified, output is 16-bit integer ( `-opus_pcm_format` applies to opus, `-ogg_pcm_format` to ogg (Vorbis) ).
  
  Use this when you want to avoid 16-bit clipping, for example when adding a large gain (-opus_gain / -ogg_gain / ReplayGain below). Each sample grows from 2 bytes to 4 bytes, using correspondingly more memory and bandwidth.

### Sound Gain

A mechanism that **adds gain (volume) in dB** when decoding compressed audio. It integrates the gain extension of the old wuvorbis / wuopus plugins into the engine's built-in decoders. The sum of the global gain (options below), ReplayGain tags, and per-track callbacks ( [WaveSoundBuffer.setGainQueryCallback](../reference/WaveSoundBuffer.md) ) is applied.

- **-**opus_gain** (global opus gain)**  
  Specifies the gain in dB applied to all opus playback. opus applies the output gain in its header (R128) inside the decoder, so this value is added to it.
- **-**ogg_gain** / **-**vorbis_gain** (global ogg/Vorbis gain)**  
  Specifies the gain in dB applied to all ogg (Vorbis) playback (the two names are synonyms; `-vorbis_gain` is for compatibility with the old plugin). Vorbis has no concept of gain in its format, so it is applied by scaling the output PCM in the float domain.
- **-**ogg_rg** / **-**vorbis_rg** (ogg/Vorbis ReplayGain)**  
  The value is **'none' (do not use)**, **'track' (track gain)**, or **'album' (album gain)**; the default is 'none'. Reads the file's `replaygain_track_gain` / `replaygain_album_gain` tags and adds that dB value (disabled by default so as not to change existing playback).

> **Recommendation**: by specification, opus has an output gain (R128) in its header, and the decoder can apply gain accurately and cheaply. If you work actively with gain or loudness, **we recommend using opus**.

### Removed Sound Options

- **-**wsdecpri** (PCM decode thread priority)**  
  Removed when the sound infrastructure moved to miniaudio. If specified, it is simply ignored.

## Graphics Options

- **-**display** (specify the display to start on)**  
  In a multi-display environment, specifies the display (monitor) on which the window is first shown. Available on both WINVER and SDL3 builds.

  The value is one of the following.

  - **Number**  
    A display number starting from 1. On Windows, it corresponds to the number in `\\.\DISPLAY1` … (the number shown in Settings → System → Display). Example: `-display=2`
  - **Name**  
    Part of the monitor name (case-insensitive). Example: `-display=DELL`  
    If it matches multiple displays, the one with the smallest number is chosen.
  - **primary**  
    Specifies the primary display.
  - **list**  
    Only writes the list of displays to the log and does not select a display (`?` / `help` do the same). Use it to look up numbers and names.

  If no display matches, a warning and the list are written to the log, and the behavior is the same as when nothing is specified.

  The window is moved into the work area of the specified display (the area excluding the taskbar, etc.) when it is created and right before it is first shown. If the script specifies a window position, the position relative to the origin of that display's work area is preserved. The move happens only once at startup, so it does not prevent the user from moving the window to another display afterward.

  Fullscreen applies to the display the window is on, so the window goes fullscreen on the display specified by this option.

  This option is mainly intended for testing (checking behavior without disturbing work on the main display).
- **-**maximizebox** (enable/disable the window maximize button / SDL3 build on Windows only)**  
  Sets whether to show the maximize button in the title bar.

  The value is **'yes' (enabled)** or **'no' (disabled)**. If this option is not specified, 'yes' is assumed.

  With 'no', the maximize button disappears, and maximizing by double-clicking the title bar or with Win+↑ is also disabled. **Resizing by dragging the window frame and toggling fullscreen with Alt+Enter still work as before**. Use this in setups with a fixed aspect ratio ( [Window.aspectLock](../reference/Window.md#aspectlock) ) when you want to prevent only maximizing to fill the work area.

  Effective only on the SDL3 build on Windows (does nothing on other platforms or on the WINVER build).
- **-**gclim** (image cache limit)**  
  Sets the maximum amount of memory used for the image cache.
  
  The value is **'auto'** or an integer; an integer specifies the memory for the image cache in MB. If this option is not specified, 'auto' is assumed.
  
  Kirikiri has a mechanism that caches images once loaded so they can be accessed quickly. This sets the memory limit for it.
  
  With 'auto', the value is determined automatically from the amount of physical memory installed in the computer.
  
  '0' disables caching.
  
  If swapping occurs frequently while Kirikiri is running, specifying a smaller value or '0' may help.
- **-**fsres** (screen resolution in fullscreen)**  
  Sets the screen resolution in fullscreen.
  
  The value is one of  **'auto'**, **'proportional' (a resolution with the same aspect ratio)** , **'nearest' (the closest resolution)** , or **'nochange' (do not change the resolution)**; if this option is not specified, 'nochange' is assumed.
  
  Note: effective only on the native Windows (WINVER) build (the same applies to -fszoom). Fullscreen on the SDL3 build is borderless and does not change the resolution; the display scale follows the Window geometry settings.
  
  With 'auto', the most suitable screen resolution is chosen automatically. In this case, if there is a resolution with the same aspect ratio that fits the resolution specified in the program, it is chosen; if there is none, the resolution is not changed and the engine scales the display up. With this setting, 'outer' (fit within the monitor) is always assumed even if 'no' is specified for the -fszoom (engine scaling in fullscreen) option.
  
  With 'proportional', among resolutions with the same aspect ratio as in non-fullscreen mode, the closest resolution that is equal to or larger than the resolution specified in the program is chosen.
  
  With 'nearest', the closest resolution that is equal to or larger than the resolution specified in the program is chosen, but there is no guarantee that it has the same aspect ratio as in non-fullscreen mode. This setting may suit CRT monitors and LCD monitors that support scaling while keeping the aspect ratio.
  
  With 'nochange', the resolution is kept as in non-fullscreen mode and is not changed.
  
  This option can be changed dynamically, but the value takes effect the next time fullscreen is entered.
- **-**fszoom** (engine scaling in fullscreen)**  
  Specifies how the engine scales the screen in fullscreen.
  
  The value is one of  **'inner' (fit within the monitor)**, **'outer' (scale to fill the monitor)**, or **'no' (do not scale)**; if this option is not specified, 'inner' is assumed.
  
  With 'inner', the engine scales the screen if necessary, that is, when the screen resolution differs from the resolution specified in the program (if the screen resolution is lower than the one specified in the program, the screen is scaled down). The aspect ratio of the resolution specified in the program is preserved, so if the monitor's aspect ratio differs, gaps may appear at the top and bottom or at the left and right. These gaps are always shown in black.
  
  With 'outer', as with 'inner', the engine scales the screen if necessary. Unlike 'inner', however, if the monitor's aspect ratio differs from the one specified in the program, the screen is scaled as far as possible so that no gaps appear at the top and bottom or left and right. As a result there are no gaps, but the screen may extend beyond the monitor. With this setting, for example, 16:9 content can be shown on a 16:10 monitor scaled to the fullest without gaps. Of course, this makes some areas extend beyond the left and right edges, so if you create content intended for this kind of display, you need measures such as not placing important UI or text in the areas that are cut off.
  
  With 'no', the engine does not scale even when necessary. In this case, even if the screen resolution differs from the resolution specified in the program, the engine does not scale (as a result, the image may be shown small in the center of the screen).
  
  When the monitor's native resolution differs from the resolution of the signal output by the graphics card, LCD monitors and the like may scale the display themselves. If the engine scales as well on top of that, the image is scaled twice and may look poor (the "auto" option of -fsres automatically chooses a combination that prevents such double scaling).
  
  This option can be changed dynamically, but the value takes effect the next time fullscreen is entered.
- **-**fsmethod** (fullscreen switching method)**  
  This option used to switch between Direct3D 9 fullscreen mode and resolution changes via `ChangeDisplaySettings`, but with the removal of the Direct3D 9 path, **it is ignored** (the `ChangeDisplaySettings` path is always used).
- **-**gsplit** (split image operations)**  
  Sets whether to perform image operations split into small pieces.
  
  The value is one of **'yes' (split)**, **'int' (interlaced splitting)**, **'bidi' (bidirectional splitting)**, or **'no' (do not split)**. On the WINVER build, 'yes' is assumed if not specified, but on the SDL3 build, 'no' is assumed (the CPU cache locality optimization from the single-threaded GDI era is outweighed by driver synchronization / dispatch overhead in SDL3 / OpenGL environments, which makes it much slower, especially for full-screen movie playback).
  
  To use the CPU's memory cache effectively, Kirikiri performs operations while splitting images into small regions when drawing. In some environments this seems to cause screen flicker. In such environments, specifying 'no' may reduce flicker, but drawing performance may drop. When double buffering is enabled, there is little point in not splitting, so we recommend enabling splitting.
  
  'int' processes every other unit of the image operation, but stripes may be visible when the screen is updated. 'bidi' alternates the order of image operations between top → bottom and bottom → top ('yes' is always top → bottom).
- **-**smoothzoom** (smoothing when scaling the display)**  
  Sets whether to apply smoothing (interpolation when enlarging) when the display content is scaled with Window.setZoom and the like, or when Kirikiri scales the screen up (or down) because of the -fsres option (unrelated to scaling with Layer.affineCopy and the like).
  
  The value is **'no'** or **'yes'**; if this option is not specified, 'yes' is assumed.
  
  Smoothing makes images smoother but slightly blurry. Without smoothing, images are sharper but jaggies are more noticeable.
  
  In some environments, disabling smoothing may lower performance. There may also be environments where smoothing has no effect.
  
  Some third-party draw devices (devices set with the Window.drawDevice property) may not be affected by this option.
  
  This option can be changed dynamically, but there is no guarantee that the value takes effect immediately.
- **-**deffont** (default font)**  
  Specifies the face name of the default font used when no font name is specified.
  
  If not specified, it is chosen from fonts declared in `fonts.json`, bundled fonts, and OS fonts according to the language setting of the runtime environment. On the native Windows (WINVER) build, stock font names such as `DEFAULT_GUI_FONT` can also be specified.
- **-**systemfont** (use OS fonts)**  
  Specify **'yes' (use)** (default) or **'no' (do not use)**. On SDL and other non-WINVER builds, sets whether fonts installed in the OS can be used by name.
  
  With 'yes', at startup only the mapping from names to files is registered from the OS font list (DirectWrite on Windows, fontconfig on Linux), and the actual file is read when that font is first used. You can write OS font names such as "Meiryo" or "Noto Sans CJK JP" in `Font.face`, and OS Japanese fonts are also included among the default font candidates. macOS / Android are not supported (nothing is registered).
  
  Specify 'no' if you do not want the appearance of your product to depend on the fonts of the runtime environment. On the WINVER build, GDI handles OS fonts directly, so this option has no effect.
- **-**aamethod** (antialiased text drawing method)**  
  Sets the method for drawing antialiased text.
  
  The value is one of **'auto'**, **'res4' (4×4 resampling)**,  **'res8' (8×8 resampling)**, or **'api' (Windows API)**; if this option is not specified, 'auto' is assumed.
  
  With 'auto', the current version selects 'api' automatically.
  
  With 'res4' or 'res8', text is drawn at several times the size (4×4 or 8×8) and then scaled down to achieve antialiasing. res4 is faster than res8 but less accurate.
  
  With 'api', antialiased text is drawn using the GetGlyphOutline API, but this API seems to have many problems and may not draw correctly in some environments.
- **-**jpegdec** (JPEG decoding precision)**  
  Sets the precision of JPEG image decoding.
  
  The value is one of **'high'**, **'normal'**, or **'low'**; if this option is not specified, 'normal' is assumed.
  
  'high' makes decoding slower but improves quality. 'low' makes decoding faster but lowers quality. However, there is hardly any visible difference.
- **-**drawthread** (number of draw threads)**  
  Sets the number of threads used for drawing.
  
  The value is **any number** or **'auto'**; if this option is not specified, '1' is assumed.
  
  With 'auto', as many threads as the number of processors recognized by the OS are assigned automatically.
  
  Using multiple draw threads may improve drawing performance on multi-core systems, but it can also lower performance.
  
  Good results may be obtained when applied to operations that draw large areas, heavy affine operations, and computationally heavy layer compositing.
  
  Even if multithreading is enabled, processing may not run multithreaded if the system judges that the drawing load is light and multithreading would not help.
- **-**bitmapallocator** (bitmap memory allocation method, Ver 1.1 or later)**  
  Specifies how memory for bitmaps is allocated.
  
  The value is one of **'globalalloc' (allocate with GlobalAlloc)**, **'separateheap' (use a separate heap)**,  or **'malloc' (use malloc)**; if this option is not specified, 'globalalloc' is assumed.
  
  Using separateheap reduces memory fragmentation and may avoid out-of-memory errors.
- **-**bitmapheapsize** (initial separate heap size, Ver 1.1 or later)**  
  Specifies the initial size when a separate heap is chosen as the bitmap memory allocation method.
  
  The value is one of **'auto' (automatic, recommended)**, **'0' (grow automatically)**,  **'64' (64MB)**,  **'128' (128MB)**,  **'256' (256MB)**,  **'512' (512MB)**,  **'1024' (1024MB)**, or  **'2048' (2048MB)**; if this option is not specified, 'auto' is assumed.
  
  auto is normally fine, but adjusting the initial value may reduce memory fragmentation and avoid out-of-memory errors.
- **-**drawdevice** (DrawDevice selection at startup)**  
  Selects the default DrawDevice used at startup. The available values depend on the build.
  
  SDL3 build:
  
    - **'sdl'**: [SDLDrawDevice](../reference/SDLDrawDevice.md) via SDL_Renderer ( backend selected automatically )
    - **'sdlogl'**: direct OpenGL ES version ( via PBO, a pure version without Canvas support ) ( only with `TVP_USE_OPENGL=ON` )
    - **'ogl'**: full-featured [OGLDrawDevice](../reference/OGLDrawDevice.md) with OpenGL ES + Canvas / Texture / Shader / Offscreen ( only with `TVP_USE_OPENGL=ON` )
    - **'gpu'**: [GPUDrawDevice](../reference/GPUDrawDevice.md) with SDL_GPU + Canvas / Texture / Shader / Offscreen ( only in `KRKRZ_CANVAS_GPU=ON` builds, which run Canvas on SDL_GPU. In this build it is also available under the name `Window.OGLDrawDevice` )
  
  If not specified, `sdlogl` is selected in `TVP_USE_OPENGL=ON` builds, `gpu` in `KRKRZ_CANVAS_GPU=ON` builds, and `sdl` otherwise.
  
  Native Windows (WINVER) build:
  
    - **'basic'**: Direct3D 11 [BasicDrawDevice](../reference/Window.BasicDrawDevice.md) ( default )
    - **'ogl'**: [OGLDrawDevice](../reference/OGLDrawDevice.md) ( only with `TVP_USE_OPENGL=ON` )
    - **'null'**: NullDrawDevice, which does not draw ( for verification )
  
  If not specified, `basic` is used. In either build, an unknown value produces a warning and falls back to the default.
  
  This specifies the **default at startup**; you can still switch at run time by assigning to [Window.drawDevice](../reference/Window.md#drawdevice). However, **if an SDL3 build is started with 'sdl', it cannot switch to the OpenGL-based devices ( sdlogl / ogl ) at run time** (OpenGL initialization fails). If you use OpenGL features (Canvas, etc.), start with 'sdlogl' / 'ogl' from the beginning.
  
  OpenGL-based DrawDevices require an environment where OpenGL ES is available. WINVER always goes through EGL ( ANGLE's libEGL.dll / libGLESv2.dll ), so bundling the DLLs is mandatory. On SDL3 for Windows, the ES profile of the OS OpenGL driver is preferred, and if it is not available, the engine falls back to the same ANGLE DLLs (see also -forceegl below).
- **-**renderer** (explicit SDL3 backend / SDL3 build only)**  
  Explicitly specifies the SDL_Renderer backend name used by SDLDrawDevice
  ( e.g. `direct3d11`, `vulkan`, `opengl`, `software` ).
  
  If not specified, the choice is left to SDL3's automatic selection.
  
  Meaningful only on SDL3 builds when SDLDrawDevice is used ( = when `-drawdevice=sdl` is specified ).
- **-**forceegl** (force EGL for the OpenGL ES context / SDL3 build only)**  
  Makes the OpenGL ES context be created with EGL from the start ( on Windows, ANGLE's libEGL.dll / libGLESv2.dll ).
  
  The value is **'no' (default, do not force)** or **'yes' (force EGL)**.
  
  By default, the SDL3 build prefers the graphics driver's OpenGL implementation if it supports the ES profile ( `WGL_EXT_create_context_es2_profile` ), and falls back to EGL only if it does not. In environments where the driver's ES profile implementation is faulty and rendering is corrupted or initialization fails, specifying 'yes' pins the path to EGL (ANGLE) for isolating or working around the problem (internally, it sets the SDL hint `SDL_OPENGL_ES_DRIVER=1`; the environment variable of the same name has the same effect).
  
  The requested context version is ES 3.2; if that cannot be created, it automatically retries with 3.1 → 3.0 → 2.0 (ANGLE's D3D11 backend supports only up to ES 3.0/3.1, so through EGL the context is established by this retry). The version actually obtained can be checked in the startup log line `Loaded GLES x.y`.
  
  OpenGL on the WINVER build always goes through EGL (ANGLE), so this option is meaningful only on SDL3 builds.
- **-**dpiscaling** (follow the OS display scaling)**
  Specifies whether to enlarge the window according to the OS display scaling ( Windows "Scale", macOS Retina, etc. ).

  The value is **'no' (default, actual pixels)** or **'yes' (follow the OS scaling)**.

  With 'no', window sizes ( [Window.innerWidth](../reference/Window.md#innerwidth) / innerHeight, setInnerSize, etc. ) are in actual screen pixels. On a 200% display a 1280x720 window looks half as large, but the picture is shown pixel for pixel ( Windows and macOS behave the same ).

  With 'yes', window sizes are in virtual pixels (actual pixels divided by the OS scaling), and the picture is enlarged by the scaling factor ( at 200%, a 1280x720 window is actually 2560x1440 pixels and looks the same size as on a 100% display ). Mouse coordinates are converted to virtual pixels as well. The size is the same with every DrawDevice ( sdl / sdlogl / ogl on SDL3 builds, basic / ogl on the WINVER build ). Moving the window to a display with a different scaling changes the virtual pixel size and raises onResize.

  It can also be set in `config.cf`. It works on both SDL3 builds and the WINVER build. The window position ( left / top ) and the screen size and position ( System.screenWidth / screenHeight, desktopLeft / Top / Width / Height, getMonitorInfo ) use the same unit, so centering a window based on the screen works as is ( all in actual pixels with 'no', all in virtual pixels with 'yes' ).
- **-**gpudriver** (explicit SDL_GPU driver / `KRKRZ_CANVAS_GPU` builds only)**  
  Explicitly specifies the SDL_GPU driver name used by GPUDrawDevice ( e.g. `vulkan` ). If not specified, the choice is left to SDL3's automatic selection.
  
  On Windows, `vulkan` ( shaders in SPIR-V ) is selected by default. Specifying `direct3d12` runs on D3D12 ( shaders in DXIL ). In this case, the script's shaders also need a pack prepared in DXIL ( created with the conversion tool's `--target dxil` ).
- **-**gpushaderpack** (shader pack for Canvas (GPU version) / `KRKRZ_CANVAS_GPU` builds only)**  
  Specifies, by storage name, a pack ( `.kzgs` ) of pre-converted shaders used by the script. Multiple packs can be specified, separated by `;`.
  
  If not specified, `canvas_shaders.kzgs` in the data is read, or, if absent, `canvas_shaders.kzgs` in the same folder as the executable.
- **-**gpushadercollect** (write out shaders that need conversion / `KRKRZ_CANVAS_GPU` builds only, for development)**  
  When a shader not in the pack is used, writes its source to the specified folder. Turn what is written out into a pack with the conversion tool ( `gpushaderc.py pack` ).
  
  Canvas (GPU version) does not compile shaders at run time, so using a shader not in the pack throws an exception. For the procedure, see `doc/CanvasGPU.md` in the engine source.
- **-**mediaengine** (hardware movie decoding / Windows only)**  
  Specifies whether MF-native formats such as mp4/H.264/HEVC/wmv/asf are hardware-decoded with
  Media Foundation ( IMFMediaEngine ) in overlay playback ( `vomOverlay` ) of
  [VideoOverlay](../reference/VideoOverlay.md).
  
  The value is **'yes' (default, use hardware decoding)** or
  **'no' / 'off' / 'false' / '0' (do not use)**. With 'no', all formats use
  software decoding ( MF SourceReader / pl_mpeg / movie-player ).
  
  webm ( VP8/VP9 ) and mpeg ( MPEG-1 ) have no decoder in Media Foundation, so they are always
  software-decoded regardless of this setting. Also, `vomMixer` mode ( additional image compositing ) always
  uses the software compositing path (see the `mode` property of
  [VideoOverlay](../reference/VideoOverlay.md) ).

## CPU Feature Options

All of the following options take one of the values **'yes' (use if available)**, **'no' (do not use even if available)**, or **'force' (force use)**; if an option is not specified, 'yes' is assumed.

If a CPU detection problem occurs, setting 'no' stops using that feature.

'force' uses the CPU feature even if it is not detected, but of course this does not work correctly if the CPU lacks the feature.

In addition, specifying **'no'** for -**cpusimd** disables all detected SIMD features and runs with the C implementations only (only 'no' can be specified for this option). Use it to isolate differences between the SIMD and C implementations.

The Kirikiri engine detects MMX / SSE to SSE4.2 / AVX / AVX2 / FMA3 (x86) and NEON / ASIMD (ARM) at run time and uses them selectively for image operations and the like, so each corresponding option has an effect. The OggVorbis / opus decoders are now built into the engine, so settings for external decoders such as the old wuvorbis.dll are no longer needed. Some other (third-party) plugins may also be affected by the CPU feature settings.

- -**cpummx** (MMX)
- -**cpu3dn** (3DNow!)
- -**cpusse** (SSE)
- -**cpucmov** (CMOVcc)
- -**cpue3dn** (Enhanced 3DNow!)
- -**cpuemmx** (EMMX (MMX2))
- -**cpusse2** (SSE2)
- -**cpusse3** (SSE3)
- -**cpussse3** (SSSE3)
- -**cpusse41** (SSE4.1)
- -**cpusse42** (SSE4.2)
- -**cpusse4a** (SSE4a)
- -**cpuavx** (AVX)
- -**cpuavx2** (AVX2)
- -**cpufma3** (FMA3)
- -**cpuaes** (AES)
- -**cpuneon** (NEON / ARM builds only)
- -**cpuasimd** (ASIMD / ARM64 builds only)

## Debugging Options

- **-**debug** (debug mode)**  
  Sets whether to run Kirikiri in debug mode  ( → [Debug](Debug.md) ).
  
  The value is **'no' (disabled)** or **'yes' (enabled)**; if this option is not specified, 'no' is assumed.
  
  When enabled, Kirikiri runs in debug mode and several debugging aids are enabled, but execution is slower than in normal mode.
- **-**forcelog** (log to file)**  
  Sets whether to write the console log to a file.
  
  The value is one of **'no' (do not write)**, **'yes' (append to the existing file)**, or **'clear' (clear the existing file before writing)**; if this option is not specified, 'no' is assumed.
- **-**logerror** (log to file on errors)**  
  Sets whether to write the console log to a file when an error occurs.
  
  The value is one of **'no' (do not write)**, **'yes' (append to the existing file)**, or **'clear' (clear the existing file before writing)**; if this option is not specified, 'yes' is assumed.
- **-**loglevel** (log output level)**  
  Overrides the log output level at startup.
  
  The value is one of **'debug'**, **'info'**, **'warning'**, **'error'**, or **'off'** (case-insensitive). Only logs at or above the specified level are output.
  
  If not specified, the default is `warning` for `MASTER` builds, `info` for other Release builds, and `debug` for Debug builds. Use it to temporarily collect detailed logs from a distributed binary.
- **-**repl** (enable the interactive TJS shell / for `KRKRZ_REPL` builds)**  
  Enables the interactive TJS REPL ( Read-Eval-Print Loop ) at startup.
  
  The value is **'yes'**, **'1'**, **'on'**, **'true'** (enabled) or no value (enabled), or **'no'**, **'0'**, **'off'**, **'false'** (disabled). Disabled if not specified.
  
  The following value also changes how the console is opened and displayed (it also enables the REPL).
  
  - **'new'** ( aliases **'window'** / **'separate'** ) : always opens a new console window instead of attaching to the parent's or an inherited console. Even when launched from a terminal or another application, it does not take over the launching console.
  
  Note that this exe uses the GUI ( windowed ) subsystem, so the console it allocates at run time is conhost regardless of the "Default terminal application" setting (it cannot be hosted in Windows Terminal). To work without terminal limitations, `-replweb` (browser viewer) below is convenient.
  
  For how to use the REPL and details of special commands such as `.help`, see the [REPL guide](../topics/core/repl.md). Ignored in executables built with `KRKRZ_REPL=OFF`.
- **-**replfile** (enable the REPL file channel / for `KRKRZ_REPL` builds)**  
  For external agents / automated tests, enables a channel that accepts REPL commands through files instead of the console. TJS expressions can be executed through input/output files in the specified directory.
  
  The value is the communication directory path as a string. Specifying **'no'**, **'0'**, **'off'**, **'false'**, or an empty string disables it (default).
  
  It can be started independently of `-repl` (the console version), and both can be used at the same time. For details, see the [REPL guide](../topics/core/repl.md).
- **-**replsocket** (enable the REPL socket channel / `KRKRZ_REPL` builds on Linux-like systems only)**  
  Enables a channel that accepts REPL commands through a Unix domain socket in the abstract namespace. It receives 1 line = 1 command (a TJS expression) and responds with a single line of JSON.
  
  The value is the socket name as a string. It can also be specified with the environment variable `KRKRZ_REPL_SOCKET`.
  
  It can be started independently of `-repl` / `-replfile` and used at the same time. Ignored on builds other than Linux-like systems. For details, see the [REPL guide](../topics/core/repl.md).
- **-**replweb** (enable the browser REPL viewer / for `KRKRZ_REPL_WEB` builds)**  
  Starts a lightweight HTTP + SSE server so the REPL can be used from a browser, with the log at the top and input at the bottom. It is free of terminal ( conhost ) limitations, and text selection, copy, paste, scrolling, and search work natively in the browser.
  
  The value is `[host:]port`. Example: `-replweb=8899` ( `http://127.0.0.1:8899/` ). The default binding is **127.0.0.1 (local only)**. Specifying something like `-replweb=0.0.0.0:8899` binds to all interfaces so that **browsers on other machines can connect** (for devkits / LANs; this exposes it to the network, so use it only in trusted environments). On macOS / iOS / Linux, when all interfaces are specified ( `0.0.0.0` / `*` / `::` ), it listens on both IPv6 and IPv4 (so that a development Mac can open it over a USB connection to a physical iOS device ( `<device name>.coredevice.local` ), which only passes IPv6; if IPv6 is unavailable, IPv4 only). `no` / `0` / `off` / `false` disables it.
  
  The implementation supports both WIN32 ( Winsock ) and POSIX sockets, and can be started independently of and simultaneously with `-repl` / `-replfile` / `-replsocket`. For details, see [Console](Console.md#replweb).
- **-**replwebidle** (seconds until the app exits after the browser closes)**  
  **Exits the app when there has been no `-replweb` SSE subscription for the specified number of seconds**. In setups that use the browser as the UI, this prevents the engine from lingering after the window is closed.
  
  **Enabled by default (5 seconds)**. `-replwebidle=no` / `off` / `0` disables it, and `-replwebidle=<seconds>` changes the number of seconds.
  
  **It arms only after at least one subscription has arrived**, so agent-driven setups that do not open a browser, or setups that use `-replweb` merely as an API surface, stay at zero subscriptions and do not exit even though it is enabled by default. If multiple tabs are open, it does not exit until the last one is closed.
  
  When a page is closed, the browser sends a close signal ( `POST /bye` ), so the app normally exits in about 2 seconds. If the signal does not arrive (a crash, etc.), detecting the disconnection takes as long as the SSE heartbeat, so the exit can be delayed up to about twice the specified number of seconds.
- **-**replwatchfile** (where the watch expression list is saved)**  
  REPL watch expressions ( `.watch` / the Watch tab of the browser UI ) **save the list of expressions and the auto-refresh interval to `.krkrz_watch` in the current directory**, and load them back at the next startup (the same approach as the REPL history `.krkrz_history`). The file is written back only when an expression is added / removed / edited or the interval is changed.
  
  `-replwatchfile=<path>` changes where it is saved, and `-replwatchfile=no` / `off` / `0` disables persistence. If the location is not writable, it silently gives up (failing to save never stops the app).
- **-**replwebpad** (directory where saving from the browser Pad is allowed)**  
  The **storage path prefix where [Save] is allowed** in the "Pad" tab (script editor) of the `-replweb` browser UI. For example, with `-replwebpad=work`, writing is allowed only under `work/`.
  
  **Writing is forbidden by default** (saving returns 403). Reading is always possible. A trailing `/` is added internally for the prefix comparison, so `-replwebpad=work` never matches `work_other/...`.
  
  ⚠ **This is not a security boundary**. Once `-replweb` is open, arbitrary TJS can be executed from the browser, and all of the process's privileges are exposed. Think of it as a fence to "keep from accidentally pressing [Save] in the UI and overwriting assets". When opening it to the network ( `-replweb=0.0.0.0:...` ), use it only in trusted environments.
- **-**replwebopen** (open a browser together with `-replweb`)**  
  By default, the browser is opened automatically in app mode only when "bound to loopback and without a console (GUI launch)". **It does not open when launched from a terminal** (if there is a terminal, you can open it yourself, and this avoids interfering with CI / agent-driven runs). This option explicitly overrides that default.
  
  | Value | Behavior |
  |---|---|
  | `app` ( same when the value is omitted ) | App mode ( Edge / Chrome `--app`; a frameless window ) |
  | `tab` / `yes` | A normal window of the default browser |
  | `no` / `off` | Do not open ( also suppresses automatic opening ) |
  
  Use `-replwebopen=app` **when you want to open a browser even when launching from a terminal**. From TJS you can also open it with `WebServer.openBrowser(url, appMode)`.
- **-**replmodaltimeout** (timeout in seconds for REPL modal responses)**  
  While the REPL is running, modals such as `System.inputString` / `System.confirm` / file selection wait on the modal response channel (agent responses) instead of showing native dialogs. If no response arrives within the specified number of seconds, a catchable exception is thrown and propagated to the caller, preventing an infinite wait.
  
  The default is **30** (seconds). **0** waits forever (the old behavior).
- **-**memoverlay** (memory state overlay)**  
  Enables, from startup, an overlay in the upper-right corner of the screen that shows the engine's memory state in real time (usage of each allocator — File / Bitmap / Sound / Krkrz / SDL — plus process RSS / VSize, etc.).
  
  The value is **'1' (enabled)** or **'0' (disabled)**; if this option is not specified, '0' is assumed.
  
  To toggle it at run time, use [System.setMemoryOverlay](../reference/System.md#setmemoryoverlay) or the REPL's `.memoverlay`. The option itself is effective on all builds, but drawing is done by the OGL-based DrawDevices ( `OGLDrawDevice` / `SDLOGLDrawDevice` ) and SDL's `SDLDrawDevice`. The WINVER default `BasicDrawDevice` (D3D11) has no drawing hook, so the overlay is not shown there, but **it is shown on WINVER too if you switch drawDevice to an OGL-based one**.
- **-**padoverlay** (gamepad state overlay)**  
  Enables, from startup, an overlay in the upper-left corner of the screen that shows the gamepad's 16-button matrix and 6-axis analog values in real time.
  
  The value is **'1' (enabled)** or **'0' (disabled)**; if this option is not specified, '0' is assumed.
  
  To toggle it at run time, use [System.setPadOverlay](../reference/System.md#setpadoverlay) or the REPL's `.padoverlay`. The option itself is effective on all builds, but drawing is done by the OGL-based DrawDevices ( `OGLDrawDevice` / `SDLOGLDrawDevice` ) and SDL's `SDLDrawDevice`. The WINVER default `BasicDrawDevice` (D3D11) has no drawing hook, so the overlay is not shown there, but **it is shown on WINVER too if you switch drawDevice to an OGL-based one**.
- **-**drawstatslog** (periodic DrawStats log output / SDL3 and LIB builds only)**  
  In `KRKRZ_DRAW_STATS=ON` builds, while the MemoryOverlay is shown, writes DrawThreadPool utilization statistics to the log every 500ms (useful when the on-screen display scrolls too fast to read, e.g. on target hardware).
  
  The value is **'1' (enabled)** or **'0' (disabled)**; if this option is not specified, '0' is assumed. It can also be toggled at run time with [System.setDrawStatsLog](../reference/System.md#setdrawstatslog).
  
  In `KRKRZ_DRAW_STATS=OFF` builds, only the flag is set and nothing happens.
- **-**memstatinterval** (periodic memory statistics dump)**  
  When a positive integer is specified, memory statistics equivalent to `System.dumpHeap` are written to the log every that many seconds.
  
  The default is 0 (disabled). Short intervals (1 to a few seconds) greatly affect log volume and performance, so use them only during investigation. Ignored when built with `KRKRZ_ENABLE_PERIODIC_DUMP=OFF`.
- **-**memstatonexit** (memory statistics dump on exit)**  
  The value is **'1' (enabled)** or **'0' (disabled)**; when enabled, memory statistics are dumped once when the engine exits. The default is '0'.
  
  Ignored when built with `KRKRZ_ENABLE_PERIODIC_DUMP=OFF`.
- **-**memstatsite** (allocation tally by call site)**  
  Specifying **'yes'** or a stack depth (1–32) captures the stack for each allocation and counts live allocations by call site. 'yes' means 16 frames. The results are written to the log at the end of `.memdump` and by the REPL's `.memsites`.
  
  Effective only on Windows builds with `KRKRZ_ENABLE_MEMSTAT_DETAIL=ON`; ignored otherwise. It slows processing considerably, so use it only during investigation. For details, see [Memory Observation and Leak Investigation](../topics/core/memory_observation.md).
- **-**cachelistonexit** (cache list dump on exit)**  
  Dumps the list of Storages file-layer / decode-layer cache entries to the log when the engine exits. Use it to investigate what remained in the cache right before exit.
  
  The value is one of the following:
  
    - **'1' / 'all'**: both the file layer and the decode layer
    - **'file'**: file layer only
    - **'image'**: decode layer only
    - **'0' / 'none'**: disabled ( default )
  
  To see the list at run time, use [Storages.dumpFileCacheList](../reference/Storages.md#dumpfilecachelist) / [Storages.dumpImageCacheList](../reference/Storages.md#dumpimagecachelist).
- **-**textencodingwarn** (warn on automatic text encoding fallback)**  
  When a text file without a BOM cannot be interpreted in the default encoding (normally UTF-8; Shift_JIS in `KRKRZ_USE_SJIS` builds), the engine tries to reinterpret it in the other encoding (automatic fallback). This option sets whether to write the file name to the warning log when that fallback occurs.
  
  The value is **'1' (write)** or **'0' (do not write)**; if this option is not specified, '0' is assumed.
  
  In projects with mixed encodings the log would fill up, so it is off by default. Enable it when investigating garbled text.
- **-**navlog** (navigation diagnostic log for Elements dialogs)**  
  Writes focus movement, cursor-warp (moving the cursor to the focus target), and the arrival of gamepad direction keys in Elements dialogs ( → [ElementsDialog](../reference/ElementsDialog.md) ) to the log, with milliseconds elapsed since startup. It is for isolating timing mismatches between input and navigation, such as the description text and the highlight getting out of sync while a direction key is held.
  
  This option is **enabled just by specifying it**; the value is ignored (disabled if not specified). Logging on both the engine side and the elements_modal side is enabled at the same time.
  
  When enabled, a `slow frame` line is also written for frames that took 100ms or more to present. The breakdown stages are the same as [ElementsDialog.renderStats](../reference/ElementsDialog.md#renderstats) — update / raster / acquire / upload / present — and can be used to isolate which stage is stalling.
  
  The log volume is large, and the output itself affects processing time, so use it only during investigation.

- **-**ignoremouse** (discard real mouse input / for behavior testing)**  
  When true, **all real mouse input is discarded**, and only input injected from [Agent](../reference/Agent.md) passes through. This sets up the premise for automated tests that "all input comes from Agent". Measurements are not disturbed if someone accidentally moves the pointer.
  
  The value is **'yes' (enabled)** or **'no' (disabled)**; disabled if this option is not specified. To toggle it at run time, use [Agent.ignoreRealMouse](../reference/Agent.md#ignorerealmouse).
  
  Hover detection and cursor queries look at the **virtual cursor position**, which is updated by Agent injection, so hover and focus work as before even when this is enabled (design: `src/core/doc/VirtualCursor.md`).
  
  ⚠ When enabled, **the mouse cannot be operated by hand**. Ignored in builds without `Agent` ( `MASTER`, etc. ).

## System Compatibility Options

- **-**arcdelim** (archive delimiter)**  
  Specifies the archive delimiter (the character separating the archive storage name from the storage name inside the archive).
  
  The value is **'>' (use '>')** or **'#' (use '#')**; if this option is not specified, '>' is assumed.
  
  The archive delimiter was changed from '#' to '>' in Kirikiri 2 2.19 beta 14.
  
  Applications that ran on versions before 2.19 beta 14 may stop working because of this change, but they can be made to work by changing the delimiter to '#' with this option.
- **-**evalcontext** (behavior of the postfix '!' operator)**  
  Specifies the behavior of the TJS2 postfix '!' operator.
  
  The value is **'this' (evaluate the expression on this)** or **'global' (evaluate the expression on global)**; if this option is not specified, 'this' is assumed.
  
  The TJS2 postfix '!' operator used to execute the expression in the global context, but since 2.21 beta 9 it executes it in the this context.
  
  Applications written for versions before 2.21 beta 9 may not work unless this is set to "evaluate the expression on global".
- **-**holdalpha** (default value of the Layer.holdAlpha property)**  
  Specifies the default value of the [Layer.holdAlpha](../reference/Layer.md#holdalpha) property.
  
  The value is **'false'** or **'true'**; if this option is not specified, 'false' is assumed.
  
  In Kirikiri 2 2.23 beta 4, the hda option (whether to protect the alpha channel) given to various operation functions was removed, and the Layer.holdAlpha property was added instead. At that point, the default value of Layer.holdAlpha was true. When Layer.holdAlpha is true, the behavior of older applications is not affected.
  
  In Kirikiri 2 2.23 beta 5, this default became false. To run applications written for versions before Kirikiri 2 2.23 beta 5, they may not work correctly unless "true" is specified for this option.
- **-**unaryaster** (behavior of the prefix '*' operator)**  
  Specifies the behavior of the TJS2 prefix '*' operator.
  
  The value is **'default' (behavior of 2.25 or later)** or **'compat' (behavior before 2.25)**; if this option is not specified, 'default' is assumed.
  
  The TJS2 prefix '*' operator used to retrieve the property object itself without going through the property handler, but since 2.25 beta 1 the operator with this function is the prefix '&', and the prefix '*' operator now invokes the property handler of a property object. Applications written for versions before 2.25 beta 1 may not work correctly unless this is set to "compatible with versions before 2.25".
- **-**lazyarraymember** (how Array methods are held)**  
  The value is **'no' (traditional behavior)** or **'yes' (look up from the class)**; if this option is not specified, 'no' is assumed.
  
  Traditionally, every time an Array object was created, the methods and properties of the Array class (add, count, etc.) were copied as members of each instance, so even an empty array used several KB. With 'yes', they are not copied into instances; names that are not among the instance's own members are looked up from the class and bound to that instance. Scripts that create many arrays see large reductions in memory usage and creation time.
  
  As before, a member of the same name set on the instance takes precedence. The difference is that after deleting a method set on the instance, the method used to be gone, whereas with 'yes' the class's method is called. Instances of script classes that inherit from Array are copied as before.
- **-**wsvolfactor** (volume curve)**  
  The value is **'3322' (behavior of 2.31 2011/6/14 or later)** or **'5000' (behavior before 2.31 2011/6/14)**; if this option is not specified, '3322' is assumed.
  
  Since 2.31 2011/6/14, the volume curve is more intuitive.
- **-**readencoding** (character encoding for reading scripts)**  
  The value is **'Shift_JIS' (Kirikiri 2-compatible behavior)** or **'UTF-8' (Kirikiri Z behavior)**; if this option is not specified, 'UTF-8' is assumed.
  
  The character encoding used to read scripts.
- **-**ignoretouch** (disable touch events, 1.3.0 or later)**  
  The value is **'false'** or **'true'**; if this option is not specified, 'false' is assumed.
  
  Specifying 'true' disables touch events and generates mouse events instead.
