---
source_hash: fe6c5bc29b02
---

# Files and Folders

## Files and Folders

This page describes the files and folders related to Kirikiri.

It does not cover every file; it focuses on files that need particular attention. For the folder structure of the Kirikiri Z SDK distribution archive, see readme.txt.

## Folders

- ****plugin** and **plugin64****  
  The folders where Kirikiri looks for plugins. If this folder exists in the folder containing the Kirikiri executable, Kirikiri refers to the plugins placed in it. `plugin64` is used only by the 64-bit Windows build; Linux and other platforms use `plugin` even in 64-bit builds ([Plugin folder names](Plugins.md#plugin-folder)). → [About Plugins](Plugins.md)
- ****data** and **content-data****  
  If this folder exists in the folder containing the Kirikiri executable, Kirikiri treats it as the project folder and runs it. → [Starting Kirikiri](Startup.md)

## Files

- ***.**xp3****  
  Archive files for Kirikiri. → [Storage System](StorageSystem.md), [xp3 Archive Tool](Xp3Tool.md)
- ****data.xp3** and **data.exe****  
  If this file is in the same folder as the Kirikiri executable, Kirikiri treats it as the project folder and runs it. → [Starting Kirikiri](Startup.md)
- ***.**tpm****  
  Plugins for Kirikiri that are loaded automatically at startup. → [About Plugins](Plugins.md)
- ****tools** folder**  
  Contains the Kirikiri Z [standard tools](Tools.md) (krkrxp3 / krkrsign / krkrcheck / krkrimg / krkraudio / krkrloop). They are for development, so you do not need to include them in distributions for end users (except the file corruption check tool). The krdevui.dll used by the Kirikiri 2 development tools is no longer needed.
- ****krmovie (movie playback)****  
  In current Kirikiri Z, movie playback is integrated into the engine executable, so you do not need to bundle `krmovie.dll` separately (no additional DLL is needed to play WebM/MP4/WMV/MPEG-1, etc.). → [VideoOverlay class](../reference/VideoOverlay.md)
- ***.**dll****  
  If it is a plugin for Kirikiri, you must include it in the distribution for end users. Of course, there is no need to include plugins you do not need. → [About Plugins](Plugins.md)
- ***.**so** ( Linux build )**  
  Plugins for the Linux build ( in `plugin/` ) and bundled libraries ( such as `libSDL3.so.0` next to the executable ). The executable and plugins have an RPATH of `$ORIGIN` embedded, so the bundled versions are loaded without setting `LD_LIBRARY_PATH`. → [Linux distribution package](../topics/core/linux_package.md)
- ****krkr.eXe****  
  The Kirikiri engine itself. You may rename it when distributing to end users.
- ***.**cf** and *.**cfu****  
  Files that contain options for the Kirikiri engine. To make the options set for the engine in "Kirikiri Settings" (-userconf) take effect (these include settings such as the -datapath option), you also need to include these files in the distribution for end users. → [Kirikiri Configuration](Configure.md)
  In Linux distributions, write `orgname` / `appname`, which determine the save data location ( `~/.local/share/<orgname>/<appname>/` ), in `<exe name>.cf` and bundle it ( krkrz_linux in [Linux distribution package](../topics/core/linux_package.md) generates it automatically ).
- ****krkrcheck** (file corruption check tool) and its .**ini** file**  
  The [file corruption check tool](FileChkTool.md). You may rename it when distributing to end users, but in that case the executable and the .ini file must have the same name (the Kirikiri 2 «ファイル破損チェックツール.ini» also works as is). When distributing to end users, you usually place it in the same folder as the Kirikiri executable.
- ****startup.tjs****  
  A TJS script file. Kirikiri looks for this file directly under the project folder and runs it first. → [Starting Kirikiri](Startup.md)
- ***.**tjs****  
  TJS script files.
- ****msgmap.tjs****  
  A message map file. If you do not remember creating it, you do not need to include it in the distribution for end users. → [Starting Kirikiri](Startup.md)
- ***.**sig****  
  Signature files output by the [key and signature tool](SignTool.md). They are referenced by the [file corruption check tool](FileChkTool.md) and others.
- ***.**rpf****  
  Profiles for the [xp3 archive tool](Xp3Tool.md) (and the Kirikiri 2 Releaser). They record the settings used to create archives. You do not need to include them in the distribution for end users (they are excluded automatically when creating archives).
- ****hwexcept.log****  
  May be created in the location specified by the -datapath option when the Kirikiri engine crashes. Crashes come in many forms, but if this file was created, it was a very serious crash, so collect it from the end user and, if necessary, send it to the Kirikiri author. You do not need to include this file in the distribution for end users.
- ***.**console.log****  
  Log files of the Kirikiri console. They are usually created in the location specified by the -datapath option when, for example, Kirikiri crashes. In most cases, the logs recorded in this file are caused by mistakes in scripts. Use them for debugging during application development, or collect them from end users after distribution. You do not need to include this file in the distribution for end users.
- ***.**dump.txt****  
  TJS dump files. You do not need to include them in the distribution for end users. → [Scripts.dump](../reference/Scripts.md#dump)
- ***.**sli****  
  Loop definition files output by [Loop Tuner](LoopTuner.md).
- ***.**tft****  
  Pre-rendered font data output by the tftSave plugin ([Creating pre-rendered font data](FontMaker.md)).
- ***.png *.jpeg *.jpg *.tlg *.bmp**  
  Image files. → [Graphic System](GraphicSystem.md)
- ***.wav *.tcw *.ogg *.opus**  
  Sound files. → [Sound System](SoundSystem.md)
- ***.wmv *.mpg *.mp4 *.ogv**  
  Movie files. → [VideoOverlay class](../reference/VideoOverlay.md)
