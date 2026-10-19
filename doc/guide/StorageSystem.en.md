---
source_hash: 09444b2646ee
---

# Storage System

## About the Storage System

In Kirikiri, files, files inside archives, and other resources are deliberately called "storages" rather than files.

## Unified Storage Names

A unified storage name is a name for a storage used only within Kirikiri. It represents a storage in a URI-like way.

The notation is



`media://domain/path`



The path separator is / (slash).

## Local Storage

A unified storage name for local storage ( a local file ) uses file as the media and . (dot) as the domain. On Windows, the path starts with the drive letter.



For example, C:\Program Files\Game\game.exe becomes

`file://./c/program files/game/game.exe`



The [Storages.getFullPath](../reference/Storages.md#getfullpath) method converts an OS file name into a unified storage name. In the process, all uppercase letters in the file name are converted to lowercase ( local storage is case-insensitive ). Any \ used as a path separator is converted to /.

The [Storages.getLocalName](../reference/Storages.md#getlocalname) method converts a unified storage name into an OS file name. Use this method when, for example, passing a storage name to an application other than Kirikiri.

## Archive Storage

To specify a storage inside an archive, separate it with >: the part before > is the storage name of the archive storage, and the part after > is the path inside the archive.



For example, the storage image/base.jpg inside file://./c/program files/game/game.xp3 is

`file://./c/program files/game/game.xp3>image/base.jpg`



Since 2.19 beta 14, the archive separator has changed from '#' to '>'.



By default, Kirikiri can handle XP3, Kirikiri's own archive storage format ( it is the third generation of the XPK format, hence XP3 ). For how to create XP3 archives, see [xp3 Archive Tool](Xp3Tool.md).

## Project Folder

When creating a game or tool with Kirikiri, it is common to put all the necessary files together in a "project folder" for development. At startup, Kirikiri sets the project folder as the current folder.

If you specify everything with paths relative to the project folder, you do not need to change any paths even after turning the project into a single executable with Releaser.

## Data Save Location

The data save location is the folder specified by the -datapath option of

. You can get it with the [System.dataPath](../reference/System.md#datapath) property.

The various logs and per-user configuration files that Kirikiri outputs are written here.

If -datapath is not specified, it is `savedata` next to the executable on Windows, and **`~/.local/share/<orgname>/<appname>/` on the Linux build** ( since 2026-10 ). For details, see -datapath in [Command-Line Options](CommandLine.md).

When users create games or tools, saving data here is also recommended.
