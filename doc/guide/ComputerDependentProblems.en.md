---
source_hash: 7bbf820749ca
---

# Environment-Dependent Problems

## Environment-Dependent Problems

This page describes Kirikiri problems caused by issues in end users' (secondary users') environments, and how to deal with them.

Kirikiri is developed with great effort to avoid environment-dependent problems, but computer settings and configurations are extremely diverse, so environment-dependent problems inevitably occur.

Some problems can be solved by addressing the individual symptom, but in general, please have users take measures such as the following.

- Update drivers to the latest stable versions
- Disable resident programs (especially ones that tend to conflict with other software, such as antivirus software, memory cleaners, window appearance customizers, and Windows-compatible shells)
- Check the computer with various check tools ("Check Disk" (the OS's standard disk check tool), [memtest86](http://www.memtest86.com/), etc.)
- Check that there is enough free space on the HDD
- Refer to sites such as [WinFAQ](http://homepage2.nifty.com/winfaq/) (Mr. Oda's page) to look for similar symptoms, and act accordingly
- Boot once in safe mode, then restart in normal mode
- If a CPU accelerator is in use, some CPU features may be restricted. Read the CPU accelerator's manual carefully; in some cases, individual CPU features need to be disabled in the engine settings (e.g. for [http://buffalo.melcoinc.co.jp/qa/cpu/b4590010.html](http://buffalo.melcoinc.co.jp/qa/cpu/b4590010.html), disable SSE)
- Reinstall the OS

Most of the options that can be set for the Kirikiri engine exist to deal with environment-dependent problems.

Please also see [Command-Line Options](CommandLine.md).

## Environment-Dependent Symptoms

Below, "engine settings" refers to the configuration tool for end users (エンジン設定.exe, "Engine Settings").

- **The installed data is corrupted**  
  Symptoms include read errors such as "a read error occurred", "freezes while the game is running", "EAccessViolation errors", and other unpredictable behavior.
  
  The installed data may be corrupted, so have the user check whether the installed data is damaged using a tool such as the "file corruption check tool".
- **Freezes during screen transitions or skipping**  
  If it freezes in situations where screen drawing happens frequently, such as screen transitions or fast skipping, there may be a problem with the display driver.
  
  Have the user check whether the display driver is the latest stable version, and if it is old, update it to the latest stable version.
  
  Alternatively, changing the "double buffering method" or "wait for vertical sync" setting in the engine settings may help.
  
  If the user uses "nView Desktop Manager", a utility bundled with nVIDIA graphics cards, have them uninstall or disable it.
- **Screen drawing is abnormally slow**  
  If screen drawing is abnormally slow, especially when Kirikiri scales up the image in full screen or when double buffering is explicitly enabled, changing the "double buffering method" or "wait for vertical sync" setting in the engine settings may help.
  
  Also, if scaling is done by the engine rather than the monitor, performance may degrade due to the scaling. In this case, setting "screen resolution in full screen" to "closest resolution" in the engine settings makes the display do the scaling, but depending on the display, the image may not be shown with the correct aspect ratio.
- **The screen stays black, or the image is garbled**  
  If the screen stays black, the image is garbled, or it freezes, especially when Kirikiri scales up the image in full screen, changing the "double buffering method" or "wait for vertical sync" setting in the engine settings may help.
- **Video playback fails**  
  If video playback using overlays fails (an error is shown, or it freezes), or if it freezes right after video playback starts, disabling hardware acceleration may help. In "Display Properties" (the dialog box shown by right-clicking the desktop and choosing "Properties" from the context menu), on the "Settings" tab, press the "Advanced" button, and in the resulting dialog box's "Troubleshoot" tab, move the "Hardware acceleration" slider step by step from full toward "None" and try each setting.
  
  It is also recommended to provide a setting in your script that turns off video playback.
  
  Alternatively, changing the "double buffering method" or "wait for vertical sync" setting in the engine settings may help.
- **Sound cuts out, stops playing, or freezes during sound playback**  
  Depending on the sound card and environment, playback may stutter, have noise, or become inaudible partway through. In some cases, symptoms such as freezing only during sound playback appear.
  
  If this happens during transitions (screen changes) or heavy effects, setting "System - low priority" to "Yes" or "System - reduce CPU usage" to "Yes" in the engine settings may help.
  
  (Kirikiri Z's audio output uses miniaudio (WASAPI shared mode). Settings specific to the old DirectSound have been removed.)
- **Controls do not work properly**  
  If software such as mouse movement assistants or mouse gesture tools is resident, the user may be unable to operate the game. Have them stop such resident software.
  
  Third-party (non-OS-standard) mouse drivers may cause problems with controls. In that case, have the user disable or uninstall the third-party driver and use the OS's standard driver.
  
  In software that supports gamepads, if a gamepad (joystick) is connected, a pad malfunction may prevent operating the game. Have the user check that nothing is resting on the pad and holding a button down.
  
  Also, in some environments, a pad button is detected as pressed when no gamepad (joystick) is connected. In that case, have the user disable the pad driver.
  
  Insufficient center calibration of gamepad or joystick axes can cause control problems. In that case, have the user calibrate the game controller from "Game Controllers" in the Control Panel.
  
  If the pad driver really cannot be disabled, Kirikiri can be set not to use the pad. Have the user set "use pad" to "Do not use" in the engine settings.
  
  With a third-party mouse driver, wheel input may not work. In that case, setting "mouse wheel detection method" to "window messages" in the engine settings may help.
- **Thrashing occurs frequently**  
  Due to insufficient memory, thrashing (heavy swapping in and out) may occur frequently.
  
  Setting "System - memory usage" to "Low" in the engine settings may help.
  
  However, this lowers performance. Instead of changing the "System - memory usage" option, setting "Graphics - image cache limit" to a relatively low value such as "4MB" or "8MB" may reduce memory usage without lowering performance much.
