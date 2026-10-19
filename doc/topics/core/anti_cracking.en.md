---
source_hash: 9f68a6340c87
---

# Anti-Cracking Measures Specific to Kirikiri Z
Because Kirikiri 2/Z is highly extensible, it offers several footholds for anyone trying to crack it.  
This page describes countermeasures specific to Kirikiri.

## Preventing Executable Replacement
If you perform authentication but the game still runs after its executable is swapped for one without any checks, you have effectively no protection at all.  
The game must not run when its executable is replaced with any other obtainable executable.  
Also watch out for replacement with executables that have been made public, such as those shipped in patches or trial versions.  
Make the game data, DLLs, and so on work only with a specific executable.  
Building the decryption routine for encrypted xp3 archives into the executable prevents the game from starting with any other executable.  
However, this becomes meaningless once someone produces a decrypted archive, so it is better to also add other unique features.  
Continuous development is needed so that previously cracked executables can no longer be used.

## Suppressing Auto-Loaded Plugins
The engine automatically loads DLLs with the tpm extension. An auto-loaded plugin can replace built-in APIs and so on, so this must be prevented.  
Note, however, that with this countermeasure in place, encryption that relies on such a built-in plugin can no longer be used.

## Suppressing Auto-Loaded Scripts
The scripts loaded at startup, such as startup.tjs in data.xp3, are fixed. If they are replaced, built-in APIs and so on can be replaced as well, so this must be prevented.  
Fixing the location of the initial script to a single place, detecting script tampering, or encrypting xp3 archives and decrypting them on every load lets you largely prevent the injection of anything other than the intended scripts.  
Compiling with TVP\_START\_UP\_SCRIPT\_NAME set to an arbitrary string makes the engine run the script of your choice at startup and disables running arbitrary scripts via the -startup option.  
TVPSystemSecurityOptions can also specify things such as forcing scripts to be loaded from data.xp3.

## Preventing Plugin Replacement
Renaming the original plugin and placing a plugin with the same name lets an attacker load any plugin they like, hijack the APIs that plugin exposes, or replace built-in APIs.  
Replacing a DLL that reads files, such as krmovie.dll, makes it easy to capture the data passed to that DLL (from 1.3 onward krmovie.dll is built into the engine, so this problem no longer applies to krmovie.dll itself).  
For krmovie.dll this means movie files; for the KAGParser.dll family, KAG scripts.  
To prevent this, DLL tampering must be detected,  
for example by checking the hash of each loaded DLL or verifying its digital signature.  
However, a slow check affects execution, so the check must be fast.  
If you build the plugins into the engine and disable plugins altogether, you do not need to worry about any of this.  
The [Extension](http://www.kaede-software.com/2014/01/extension.html) feature makes it possible to add functionality, but this currently cannot be done without modifying the plugin's source code.  
The goal is to make plugins embeddable in the engine without source changes, by changing only the build process to produce a static library and link it with the engine.

## Suppressing the Controller, Script Editor, Watch Expressions, and Console via Hotkeys
In Kirikiri Z, the controller, script editor, and watch expressions were removed, and the console became a command line.  
[Removed features](../tjs2/deleted.md)  
Disable these features.  
In Kirikiri Z, plugins can obtain console output, so suppress that as well.  
Disabling console output itself probably makes things slightly faster.
Building without TVP\_LOG\_TO\_COMMANDLINE\_CONSOLE stops logs from being written to the command line (the public binaries are built with it ON, so they do output logs).  
If you disable console output, note that some plugins write their OSS licenses to the log; when using such plugins, you must ship a separate text file containing the license.

## Bytecode Compilation
TJS2 scripts stored as-is are easy to analyze, so compile them to bytecode.  
Bytecode compilation is done with Scripts.compileStorage.  
Even an encrypted archive can be broken, so making the scripts hard to analyze is still worthwhile.  
Bytecode also loads faster than scripts (since compilation has already been done in advance).

## Bytecode Obfuscation
Obfuscate the bytecode to make it harder to analyze.  
Obfuscation mainly replaces human-readable strings, making it hard to infer what the code does.  
It is even stronger if built-in functions can be obfuscated at the same time.  
No obfuscation tool for TJS2 bytecode is currently provided.

## Archive Encryption
xp3 archives can be encrypted by passing an encryption DLL to the Releaser.  
Decryption is done by having the engine load a tpm plugin.  
