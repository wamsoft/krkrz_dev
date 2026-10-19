# Storages

The Storages class has methods and properties related to the Kirikiri engine's **storage system**. You cannot create objects of this class.

## Members

### Properties

- [currentPath](#currentpath)

### Methods

- [addAutoPath](#addautopath)
- [removeAutoPath](#removeautopath)
- [getFullPath](#getfullpath)
- [getPlacedPath](#getplacedpath)
- [isExistentStorage](#isexistentstorage)
- [extractStorageExt](#extractstorageext)
- [extractStorageName](#extractstoragename)
- [extractStoragePath](#extractstoragepath)
- [chopStorageExt](#chopstorageext)
- [searchCD](#searchcd)
- [getLocalName](#getlocalname)
- [selectFile](#selectfile)
- [selectDirectory](#selectdirectory)
- [addCacheTargetExtension](#addcachetargetextension)
- [addDecodeTargetExtension](#adddecodetargetextension)
- [removeDecodeTargetExtension](#removedecodetargetextension)
- [clearArchiveCache](#cleararchivecache)
- [clearCache](#clearcache)
- [clearAllCaches](#clearallcaches)
- [clearTransientCaches](#cleartransientcaches)
- [clearFastCache](#clearfastcache)
- [clearOldCache](#clearoldcache)
- [commitSavedata](#commitsavedata)
- [deleteFile](#deletefile)
- [dirlist](#dirlist)
- [dirtree](#dirtree)
- [getFileProperty](#getfileproperty)
- [isCacheLoading](#iscacheloading)
- [isExistentDirectory](#isexistentdirectory)
- [isFastCacheLoading](#isfastcacheloading)
- [getLastModifiedFileTime](#getlastmodifiedfiletime)
- [moveFile](#movefile)
- [requestCache](#requestcache)
- [requestFastCache](#requestfastcache)
- [isImagePrefetchLoading](#isimageprefetchloading)
- [pinCache](#pincache)
- [unpinCache](#unpincache)
- [isCachePinned](#iscachepinned)
- [getFileCacheList](#getfilecachelist)
- [getImageCacheList](#getimagecachelist)
- [dumpFileCacheList](#dumpfilecachelist)
- [dumpImageCacheList](#dumpimagecachelist)
- [rollbackSavedata](#rollbacksavedata)
- [setCacheMaxSize](#setcachemaxsize)
- [fstat](#fstat)
- [getTime](#gettime)
- [createDirectory](#createdirectory)
- [removeDirectory](#removedirectory)
- [copyFile](#copyfile)
- [exportFile](#exportfile)
- [truncateFile](#truncatefile)
- [getMD5HashString](#getmd5hashstring)
- [getTemporaryName](#gettemporaryname)
- [isExistentStorageNoSearchNoNormalize](#isexistentstoragenosearchnonormalize)
- [clearStorageCaches](#clearstoragecaches)

---

### currentPath

Property \ Access: `r`

**Type**: `String`

**Description**

Current directory

Returns the process's current directory as a storage name (ending with `/`).
You can use it as the base for relative paths, as in `Storages.getFullPath(Storages.currentPath + name)`.
In environments without the concept of a current directory, it is an empty string.

The engine version is read-only. When the fstat plugin is loaded (WINVER), it is replaced
by the plugin version, and you can change the current directory by assigning to it.

---

### addAutoPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Path to add to the automatic search path.<br>The path must end with '>' when it specifies the root folder inside an archive, and with '/' when it<br>specifies a regular folder<br>(e.g. `"Archive/arc.xp3>"` or `"System/"`).<br>Since 2.19 beta 14, the archive delimiter has changed from '#' to '>'. |

**Description**

Adds to the automatic search path

Adds the specified path to the **automatic search path**. When Kirikiri looks for an available storage,
it searches the paths registered in this automatic search path.

Paths added later are searched with higher priority.

The project folder is always searched first.

**See also:** [Storages.removeAutoPath](Storages.md#removeautopath)

---

### removeAutoPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Path to remove from the automatic search path. |

**Description**

Removes from the automatic search path

Removes the specified path from the automatic search path.

**See also:** [Storages.addAutoPath](Storages.md#addautopath)

---

### getFullPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name to convert into a full unified storage name. |

**Return value**

The full unified storage name

**Description**

Gets the full unified storage name

Converts the storage name given in path into a full **unified storage name**.

Redundant path components (for example `system/flags/../data/`) are all collapsed.

If no current media or current folder is specified, they are filled in.

**See also:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### getPlacedPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to search for. |

**Return value**

The location where it was found, as a unified storage name. An empty string if it was not found.

**Description**

Searches for a storage

Searches the **automatic search path** for the storage given in storage.

**See also:** [Storages.getFullPath](Storages.md#getfullpath) / [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### isExistentStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to check. |

**Return value**

true if it exists, false otherwise.

**Description**

Checks whether a storage exists

Checks whether the storage given in storage exists. This is faster than using getPlacedPath.

**See also:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### extractStorageExt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to extract the extension from. |

**Return value**

The extension part, including the `.` (dot). If there is no
extension, an empty string is returned.

**Description**

Extracts the extension of a storage name

Extracts and returns the extension part of the specified storage name.

**See also:** [Storages.extractStorageName](Storages.md#extractstoragename) / [Storages.extractStoragePath](Storages.md#extractstoragepath) / [Storages.chopStorageExt](Storages.md#chopstorageext)

---

### extractStorageName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to extract the name from. |

**Return value**

The storage name. If there is none, an empty string is returned.

**Description**

Extracts the storage name

Extracts and returns the name part (without the path) of the specified storage name.

For example, passing `"System/hoge.txt"` returns `"hoge.txt"`.

**See also:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStoragePath](Storages.md#extractstoragepath)

---

### extractStoragePath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to extract the path from. |

**Return value**

The path. If there is none, an empty string is returned.

**Description**

Extracts the path of a storage name

Extracts and returns the path part of the specified storage name.

For example, passing `"file://home/dee/hoge.txt"` returns `"file://home/dee/"`.

**See also:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStorageName](Storages.md#extractstoragename)

---

### chopStorageExt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to remove the extension from. |

**Return value**

The storage name with the extension removed.

**Description**

Removes the extension from a storage name

Returns the specified storage name with its extension removed.

For example, passing `"file://home/dee/hoge.txt"` returns `"file://home/dee/hoge"`.

**See also:** [Storages.extractStorageExt](Storages.md#extractstorageext)

---

### searchCD

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `volume` | `&nbsp;` | Volume label of the CD to search for. |

**Return value**

The drive letter of the CD-ROM drive found.

**Description**

Searches for a CD

Looks for a CD drive with the specified volume label and returns its drive letter (such as 'H').

Of course, the matching CD-ROM must be inserted in the drive.

---

### getLocalName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Unified storage name to convert into a **local file name**. |

**Return value**

The local file name. If it cannot be converted to a local file name, either an empty string is returned or
an exception is raised.

**Description**

Gets the local file name

Converts the specified unified storage name into the OS-native form (local file name) and returns it.

---

### selectFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `params` | `&nbsp;` | Dictionary used to pass data in and out.<br>You can specify the following members when calling this method. Some members<br>are changed when the method returns.<br>**filter**<br>An array of filter strings.<br>A filter string consists of a filter description and a filter separated by \| (vertical bar);<br>the filter is a wildcard pattern. If one filter covers several extensions,<br>separate them with ; (semicolon).<br>To specify several filters, use an array.<br>If omitted, no filter is used.<br>Example:<br>`["画像ファイル(*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg)\|*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg", `<br>` "スクリプトファイル(*.tjs;*.ks)\|*.tjs;*.ks"]`<br>**filterIndex**<br>Number of the selected filter (one of those given in filter).<br>If you specify 1, the first filter in filter is selected<br>initially. If you specify 2, the second filter is selected<br>(note that this is not a 0-based index;<br>the first one is 1).<br>If omitted, the first filter is selected.<br>When the user presses OK, this member is set to the index of the filter that was<br>last selected in the dialog box.<br>**name**<br>File name. If omitted or an empty string, no file is selected<br>initially.<br>When the user presses OK, this member is set to the selected file.<br>**initialDir**<br>Folder shown initially.<br>If omitted, the current directory is used.<br>**title**<br>Title of the dialog box.<br>If omitted, the default "Open" or "Save As" title is used<br>(depending on the save member).<br>**save**<br>Type of dialog box.<br>If false (default), an "Open" dialog box is used.<br>If true, a "Save As" dialog box is used.<br>**defaultExt**<br>Default extension. It is appended automatically when the user does not specify an<br>extension. Do not include the . (period) in the extension<br>specified here.<br>If omitted, no extension is appended.<br>**Platform differences**<br>The native Windows build uses the OS standard file dialog (GetOpenFileName),<br>and the SDL build uses SDL's file dialog (both for desktop).<br>In the SDL build, the filter wildcards (e.g. `*.png;*.jpg`) are converted to SDL format<br>and applied, but title / defaultExt / filterIndex (initial selection and return value) may be ignored<br>depending on the environment. The resulting name is written back as a normalized<br>storage name, as in the Windows build. |

**Return value**

true if the user selects a file and presses OK, false if the user presses Cancel.

**Description**

Shows a file selection dialog box

Opens a file selection dialog box.

var params = %[

filter : [ "テキストファイル(*.txt)|*.txt", "バイナリファイル(*.bin)|*.bin" ],

filterIndex : 1,

name : "",

initialDir : System.exePath,

title : "ファイルを開く",

save : false,

];

if(Storages.selectFile(params))

System.inform("選択したファイルは : " + params.name);

---

### selectDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `params` | `&nbsp;` | Dictionary used to pass data in and out. The following members<br>can be specified.<br>**name**<br>Folder selected initially. When the user presses OK, the normalized storage name of the<br>selected folder is written back to this member.<br>**title**<br>Title of the dialog box (applies only to the WINVER build).<br>**rootDir**<br>Folder shown initially (fallback when name is not specified).<br>**window**<br>Window to use as the parent (optional).<br>**Platform differences**<br>The native Windows build uses the OS standard folder selection dialog (IFileOpenDialog),<br>and the SDL build uses SDL's folder selection dialog (SDL_ShowOpenFolderDialog).<br>In the SDL build, title may be ignored. |

**Return value**

true if the user selects a folder and presses OK, false if the user cancels.

**Description**

Shows a folder selection dialog box

Opens a folder (directory) selection dialog box modally.

var params = %[

name : "",

title : "フォルダを選択",

rootDir : System.exePath,

];

if(Storages.selectDirectory(params))

System.inform("選択したフォルダは : " + params.name);

---

### addCacheTargetExtension

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ext` | `&nbsp;` | Target extension. If it does not start with `.` (period),<br>one is added automatically. |
| `minSize` | `0` | Minimum file size (in bytes) for this extension.<br>0 (default) means no size threshold; files smaller than the threshold<br>are not cached. |

**Description**

Adds an extension to the in-memory cache targets

Adds an extension whose files are placed in the in-memory cache (file layer) when loaded.
For files with a registered extension, the contents are kept in memory when read from storage,
so disk I/O is skipped on later access.

**See also:** [Storages.requestCache](Storages.md#requestcache) / [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)

---

### addDecodeTargetExtension

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ext` | `&nbsp;` | Target extension. If it does not start with `.` (period),<br>one is added automatically. |
| `minSize` | `0` | Minimum file size (in bytes) for this extension.<br>0 (default) means no size threshold. |

**Description**

Adds an extension to the decode cache targets

Adds an extension whose files are placed in the image decode result cache (decode layer).
Files with a registered extension are decoded in the background by [Storages.requestCache](Storages.md#requestcache)
and placed in the cache.

**See also:** [Storages.removeDecodeTargetExtension](Storages.md#removedecodetargetextension) / [Storages.requestCache](Storages.md#requestcache)

---

### removeDecodeTargetExtension

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ext` | `&nbsp;` | Extension to remove. |

**Description**

Removes an extension from the decode cache targets

Removes an extension added with [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)
from the decode cache targets.

**See also:** [Storages.addDecodeTargetExtension](Storages.md#adddecodetargetextension)

---

### clearArchiveCache

Method

**Description**

Discards the archive cache

Discards all cached archive metadata and extraction buffers that the engine keeps internally
after opening archives such as XP3.

Use it to reduce memory usage, for example when switching through many archives
one after another.

---

### clearCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `""` | Path of the file to discard. If omitted or an empty string,<br>all transient caches (those not pinned) are<br>discarded. |

**Description**

Discards the cache

Discards file caches loaded with `Storages.requestCache`.
Both the file layer and the decode layer are affected.

**See also:** [Storages.requestCache](Storages.md#requestcache) / [Storages.clearAllCaches](Storages.md#clearallcaches) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### clearAllCaches

Method

**Description**

Discards all caches

Discards all caches in the file layer and the decode layer.
Pinned entries are removed as well, so this is equivalent to the strongest `doCompact(clAll)`.

**See also:** [Storages.clearCache](Storages.md#clearcache) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### clearTransientCaches

Method

**Description**

Discards transient caches

Discards unpinned (transient) cache entries from both the file layer and the decode layer.
Intended for lightweight cache clearing, such as when returning to the title screen.

**See also:** [Storages.pinCache](Storages.md#pincache) / [Storages.clearAllCaches](Storages.md#clearallcaches)

---

### clearFastCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `""` | Path of the file to discard. If omitted or an empty string,<br>all caches are discarded. |

**Description**

Discards the fast cache

Discards file caches loaded with `Storages.requestFastCache`.

**See also:** [Storages.requestFastCache](Storages.md#requestfastcache)

---

### clearOldCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `keepTime` | `0` | Number of seconds to keep entries. 0 targets all<br>caches. |
| `force` | `0` | If nonzero, entries are discarded even while in use.<br>The default is 0 (entries in use are not discarded). |

**Description**

Discards old caches

Discards cache entries that have not been accessed for a certain time.

---

### commitSavedata

Method

**Description**

Commits save data

Commits what has been written to the save data area.
On some platforms, writes to the savedata area may be buffered until this call.

**See also:** [Storages.rollbackSavedata](Storages.md#rollbacksavedata)

---

### deleteFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to delete. |

**Return value**

true if the file was deleted, false otherwise.

**Description**

Deletes a file

Deletes the specified storage file. The corresponding entry is also removed from the
automatic search path cache.

**See also:** [Storages.moveFile](Storages.md#movefile)

---

### dirlist

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the directory to list.<br>It must end with `/`. |

**Return value**

An array of file and directory names.

**Description**

Lists a directory

Returns an array of the file names and subdirectory names directly under the specified directory.

Subdirectory entries end with `/`.
In builds where `TVP_NO_NORMALIZE_PATH` is not defined, all results are normalized
to lowercase.

`.` / `..` (the directory itself and its parent) are not included.

Besides real local folders, you can also list folders inside archives and on media provided by plugins
(such as `proxy://`).

**See also:** [Storages.dirtree](Storages.md#dirtree)

---

### dirtree

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the directory to walk. |
| `dironly` | `false` | If true, only directories are returned. Default is false. |

**Return value**

An array of paths.

**Description**

Gets a directory tree

Recursively walks the specified directory and returns an array of file and directory
names.

**See also:** [Storages.dirlist](Storages.md#dirlist)

---

### getFileProperty

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | File name whose properties to get. |

**Return value**

The properties as a dictionary. null if there are no properties.

**Description**

Gets file properties

Gets and returns the properties of the specified storage.

---

### isCacheLoading

Method

**Return value**

true if loading, false otherwise.

**Description**

Checks whether the regular cache is loading

Returns true if files requested with `Storages.requestCache` are still being loaded on the
background thread.

**See also:** [Storages.requestCache](Storages.md#requestcache)

---

### isExistentDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the directory to check.<br>It must end with `/`. |

**Return value**

true if it exists, false otherwise. false is also returned for a storage name that does not
correspond to a real local folder (such as one inside an archive);
no exception is raised.

**Description**

Checks whether a directory exists

Checks whether the specified directory exists.

**See also:** [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### isFastCacheLoading

Method

**Return value**

true if loading, false otherwise.

**Description**

Checks whether the fast cache is loading

Returns true if files requested with `Storages.requestFastCache` are still being loaded on the
background thread.

**See also:** [Storages.requestFastCache](Storages.md#requestfastcache)

---

### getLastModifiedFileTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file whose last modified time to get. |

**Return value**

The last modified time as a 64-bit integer in Windows FILETIME format
(elapsed time in 100-nanosecond units since 1601-01-01 00:00:00 UTC).
Returns 0 on failure.
Because the same unit and epoch are used on all platforms, you can compare values and detect changes,
and also interpret the value itself as an absolute time
(same specification as Storages.getLastModifiedFileTime in the fstat plugin).

**Description**

Gets a file's last modified time

Gets the last modified time of the specified storage file.

---

### moveFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | Source storage name. |
| `to` | `&nbsp;` | Destination storage name. |

**Return value**

true if the file was moved, false otherwise.

**Description**

Moves (renames) a file

Moves (renames) the specified storage file to another location.
On success, the automatic search path cache is updated as well.

**See also:** [Storages.deleteFile](Storages.md#deletefile)

---

### requestCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to load. |
| `minSize` | `0` | Minimum file size threshold (in bytes) for this call only.<br>0 (default) follows the setting registered for the extension. |

**Description**

Requests loading into the file cache

Loads the specified file into the regular file cache in the background.
Extensions registered with `Storages.addCacheTargetExtension` go into the file-layer cache, and
image extensions registered with `Storages.addDecodeTargetExtension` go into the decode-layer cache
(decoded results). For extensions registered in both, both layers are triggered in parallel.

**See also:** [Storages.clearCache](Storages.md#clearcache) / [Storages.isCacheLoading](Storages.md#iscacheloading) / [Storages.isImagePrefetchLoading](Storages.md#isimageprefetchloading) / [Storages.requestFastCache](Storages.md#requestfastcache)

---

### requestFastCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to load. |
| `minSize` | `0` | Minimum file size threshold (in bytes) for this call only.<br>0 (default) follows the setting registered for the extension. |

**Description**

Requests loading into the fast file cache

Loads the specified file into the fast cache in the background.
Its internal queue is separate from the regular cache and is processed
with higher priority than `Storages.requestCache`.

**See also:** [Storages.clearFastCache](Storages.md#clearfastcache) / [Storages.isFastCacheLoading](Storages.md#isfastcacheloading) / [Storages.requestCache](Storages.md#requestcache)

---

### isImagePrefetchLoading

Method

**Return value**

true if in progress, false otherwise.

**Description**

Checks the progress of image decode prefetch

Returns true while image decode prefetch jobs (decode layer) triggered by
[Storages.requestCache](Storages.md#requestcache) and the like are still being
processed in the background.
Whereas `Storages.isCacheLoading` looks at the file layer, this one is for polling the
decode layer.

**See also:** [Storages.requestCache](Storages.md#requestcache) / [Storages.isCacheLoading](Storages.md#iscacheloading)

---

### pinCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to pin. |

**Description**

Pins a cache entry

Puts the cache entry for the specified path into the **pinned** state in both the file layer and the decode layer,
excluding it from `clearCache(empty string)` and `clearTransientCaches`.
If it is not in the cache yet, an asynchronous load is triggered automatically.
Files found through the autopath are pinned after being normalized to their actual path.

**See also:** [Storages.unpinCache](Storages.md#unpincache) / [Storages.isCachePinned](Storages.md#iscachepinned) / [Storages.clearTransientCaches](Storages.md#cleartransientcaches)

---

### unpinCache

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to unpin. |

**Description**

Unpins a cache entry

Unpins an entry pinned with [Storages.pinCache](Storages.md#pincache).
Afterwards it is again subject to transient clearing (it is not discarded immediately).

**See also:** [Storages.pinCache](Storages.md#pincache)

---

### isCachePinned

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the file to check. |

**Return value**

true if pinned, false otherwise.

**Description**

Checks whether a cache entry is pinned

Returns whether the specified path is pinned in the file layer or the decode layer.

**See also:** [Storages.pinCache](Storages.md#pincache) / [Storages.unpinCache](Storages.md#unpincache)

---

### getFileCacheList

Method

**Return value**

An array of cache entry dictionaries.

**Description**

Gets the file-layer cache list

Returns the entries of the file-layer cache (binaries held by the `requestCache` family)
as an array of dictionaries.

Each entry has the following keys.

- `path`        : normalized storage path (String)
- `size`        : number of bytes (Integer)
- `lastaccess`  : last access time (platform-dependent integer)
- `usecount`    : current reference count (Integer)
- `pinned`      : pinned state (0 or 1)

**See also:** [Storages.dumpFileCacheList](Storages.md#dumpfilecachelist) / [Storages.getImageCacheList](Storages.md#getimagecachelist)

---

### getImageCacheList

Method

**Return value**

An array of cache entry dictionaries.

**Description**

Gets the decode-layer cache list

Returns the entries of the decode-layer cache (decoded Bitmaps) as an array of
dictionaries.

Each entry has the following keys.

- `path`    : normalized storage path (String)
- `keyidx`  : variation number within the same path (Integer)
- `mode`    : load mode (Integer; internal constant)
- `dw, dh`  : display size (Integer)
- `width, height` : original Bitmap size (Integer)
- `bytes`   : bytes occupied (Integer)
- `pinned`  : pinned state (0 or 1)

**See also:** [Storages.dumpImageCacheList](Storages.md#dumpimagecachelist) / [Storages.getFileCacheList](Storages.md#getfilecachelist)

---

### dumpFileCacheList

Method

**Description**

Logs the file-layer cache list

Writes the list of file-layer cache entries to the log at WARNING level.
It is output even in MASTER builds. Equivalent to `.fcache` in the REPL.

**See also:** [Storages.getFileCacheList](Storages.md#getfilecachelist) / [Storages.dumpImageCacheList](Storages.md#dumpimagecachelist)

---

### dumpImageCacheList

Method

**Description**

Logs the decode-layer cache list

Writes the list of decode-layer cache entries to the log at WARNING level.
It is output even in MASTER builds. Equivalent to `.icache` in the REPL.

**See also:** [Storages.getImageCacheList](Storages.md#getimagecachelist) / [Storages.dumpFileCacheList](Storages.md#dumpfilecachelist)

---

### rollbackSavedata

Method

**Description**

Rolls back save data

Discards writes to the save data area and returns to the last committed state.

**See also:** [Storages.commitSavedata](Storages.md#commitsavedata)

---

### setCacheMaxSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `size` | `&nbsp;` | Maximum cache size in bytes<br>(not a number of entries). |

**Description**

Sets the maximum file cache size

Sets the maximum total size of the file cache held by the `Storages.requestCache` family.
When the total size of cached files exceeds this value, entries are discarded starting
with the oldest. The default is 200MB (200 * 1024 * 1024).

---

### fstat

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Target storage name. |

**Return value**

A dictionary `%[ size, mtime ]`. An exception is raised if the storage cannot be opened.

**Description**

Gets a file's size and modified time

Returns the size and last modified time of the specified storage as a dictionary.

- `size` … file size (number of bytes)
- `mtime` … last modified time (Date object). Omitted if the time cannot be obtained

Files inside archives and on media provided by plugins (such as `proxy://`)
have no real file, so only `size` is included.

When the fstat plugin is loaded, it is replaced by the plugin version (which also returns `atime` / `ctime`).
To compare modified times numerically, use
[Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime).

**See also:** [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)

---

### getTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Storage name of the target file or folder. |

**Return value**

A dictionary `%[ mtime ]`. An exception is raised if the target is not found.

**Description**

Gets the modified time

Returns the last modified time of a real local file or folder as a dictionary `%[ mtime ]`
(`mtime` is a Date object). Files inside archives are not supported.

When the fstat plugin is loaded, it is replaced by the plugin version (which also returns `ctime` / `atime`).

**See also:** [Storages.fstat](Storages.md#fstat) / [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime)

---

### createDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the directory to create. |

**Return value**

true if it was created, false otherwise.

**Description**

Creates a directory

Creates the specified directory, including any missing intermediate directories.

**See also:** [Storages.removeDirectory](Storages.md#removedirectory)

---

### removeDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` | Storage name of the directory to remove. |

**Return value**

true if it was removed, false otherwise.

**Description**

Removes a directory

Removes the specified directory. It is not removed if files remain in it.

**See also:** [Storages.createDirectory](Storages.md#createdirectory)

---

### copyFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | Source storage name. |
| `to` | `&nbsp;` | Destination storage name. |
| `failIfExist` | `false` | If true and the destination already exists, does nothing and returns false.<br>If false (default), the destination is overwritten. |

**Return value**

true if copied; false if it stopped because the destination already exists.

**Description**

Copies a file

Copies a file in the storage space to another storage name.
The source may be a file inside an archive.

**See also:** [Storages.exportFile](Storages.md#exportfile)

---

### exportFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name of the file to export. |
| `dest` | `&nbsp;` | Destination storage name. |

**Description**

Exports a file

Writes a file in the storage space (including one inside an archive) to the specified storage name.
An existing destination is overwritten.

**See also:** [Storages.copyFile](Storages.md#copyfile)

---

### truncateFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Target storage name. |
| `size` | `&nbsp;` | Size after truncation (in bytes). |

**Return value**

true if truncated, false otherwise.

**Description**

Truncates a file

Truncates a real local file to the specified size.
On success, the read cache for that file is also discarded.

---

### getMD5HashString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Target storage name. |

**Return value**

A 32-character lowercase hexadecimal string. An exception is raised if the storage cannot be opened.

**Description**

Gets the MD5 hash

Returns the MD5 hash of the contents of the specified storage.
Files inside archives are also supported.

---

### getTemporaryName

Method

**Return value**

A temporary file name.

**Description**

Gets a temporary file name

Issues one local file name that can be used for a temporary file.

The location is the OS temporary folder (on Windows, the TMP, TEMP, then USERPROFILE environment variables, in that order).
If that folder cannot be written to, or if the engine was started with no environment variables at all and it resolved
to the Windows directory, a warning is logged and the save data folder
([System.dataPath](System.md#datapath)) is used instead. The same location is used when extracting plugin DLLs
from archives.

---

### isExistentStorageNoSearchNoNormalize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Storage name to check. |

**Return value**

true if it exists, false otherwise.

**Description**

Checks existence without normalization or search

Checks whether a storage exists without normalizing the path or searching the automatic search path.

**See also:** [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### clearStorageCaches

Method

**Description**

Discards storage caches

Discards the archive (XP3) segment cache and the automatic search path cache.
Call it after adding or deleting files outside the engine.

---

## Plugin extension: fstat

Manual written as pseudo-code

Copyright 2007 GoWatanabe

### Members

#### Methods

- [fstat](#fstat)
- [exportFile](#exportfile)
- [deleteFile](#deletefile)
- [truncateFile](#truncatefile)
- [moveFile](#movefile)
- [dirlist](#dirlist)
- [dirlistEx](#dirlistex)
- [dirtree](#dirtree)
- [removeDirectory](#removedirectory)
- [createDirectory](#createdirectory)
- [createDirectoryNoNormalize](#createdirectorynonormalize)
- [changeDirectory](#changedirectory)
- [setFileAttributes](#setfileattributes)
- [resetFileAttributes](#resetfileattributes)
- [getFileAttributes](#getfileattributes)
- [selectDirectory](#selectdirectory)
- [isExistentDirectory](#isexistentdirectory)
- [getTime](#gettime)
- [setTime](#settime)
- [getLastModifiedFileTime](#getlastmodifiedfiletime)
- [setLastModifiedFileTime](#setlastmodifiedfiletime)
- [copyFile](#copyfile)
- [copyFileNoNormalize](#copyfilenonormalize)
- [isExistentStorageNoSearchNoNormalize](#isexistentstoragenosearchnonormalize)
- [getDisplayName](#getdisplayname)
- [getMD5HashString](#getmd5hashstring)
- [searchPath](#searchpath)
- [getTemporaryName](#gettemporaryname)

---

### fstat

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**Return value**

Dictionary containing attribute information
size: file size
mtime: modified time (Date object)
atime: access time (Date object)
ctime: creation time (Date object)

**Description**

Gets file attributes

Note: the engine also has a method of the same name, but loading this plugin
replaces it with this version. Difference from the engine version: the engine version returns only size and mtime, not atime / ctime.

---

### exportFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` | Source file |
| `dest` | `&nbsp;` | Destination file |

**Description**

Extracts a file from the Kirikiri storage space

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.exportFile](Storages.md#exportfile) for the specification.

---

### deleteFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | File to delete |

**Return value**

true if the file was actually deleted
Only real files are deleted

**Description**

Deletes the specified file in the Kirikiri storage space.

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.deleteFile](Storages.md#deletefile) for the specification.

---

### truncateFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `file` | `&nbsp;` | File |
| `size` | `&nbsp;` | New size |

**Return value**

true if the size was changed
Only real files are processed

**Description**

Changes (truncates) the size of the specified file in the Kirikiri storage space

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.truncateFile](Storages.md#truncatefile) for the specification.

---

### moveFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fromFile` | `&nbsp;` | File to move |
| `toFile` | `&nbsp;` | Destination path |

**Return value**

true if the file was actually moved
The file is moved only if it exists and there is no file at the destination path
Note: paths are not normalized or checked with getPlacedPath, so write full paths

**Description**

Moves the specified file.

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.moveFile](Storages.md#movefile) for the specification.

---

### dirlist

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

Array containing the file names

**Description**

Gets the list of files in the specified directory

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.dirlist](Storages.md#dirlist) for the specification.

---

### dirlistEx

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

Array containing file information
[ %[ name:file name, size, attrib, mtime, atime, ctime ], ... ]
Note that unlike dirlist, name does not get a trailing "/" for folders (use attrib to tell them apart)

**Description**

Gets the list of files in the specified directory with details

---

### dirtree

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |
| `dironly` | `false` | List folder names only, excluding files |

**Return value**

Array containing the list (a flat enumeration including subfolders, not a tree)
The list does not include self or parent references such as ./ and ../

**Description**

Gets the list of files and folders under the specified directory (including subfolders)

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.dirtree](Storages.md#dirtree) for the specification.

---

### removeDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

true if the directory was actually removed
It is removed only if it contains no files

**Description**

Removes the specified directory

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.removeDirectory](Storages.md#removedirectory) for the specification.

---

### createDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

true if the directory was actually created

**Description**

Creates a directory

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.createDirectory](Storages.md#createdirectory) for the specification.

---

### createDirectoryNoNormalize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

true if the directory was actually created

**Description**

Creates a directory without normalizing the path

(The directory name is not converted to lowercase.)

---

### changeDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

true if the directory was actually changed

**Description**

Changes the current directory

---

### setFileAttributes

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File or directory name |
| `attr` | `&nbsp;` | Attributes to set (FILE_ATTRIBUTE_READONLY, FILE_ATTRIBUTE_HIDDEN, ...) |

**Description**

Sets file attributes

---

### resetFileAttributes

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File or directory name |
| `attr` | `&nbsp;` | Attributes to clear (FILE_ATTRIBUTE_READONLY, FILE_ATTRIBUTE_HIDDEN, ...) |

**Description**

Clears file attributes

---

### getFileAttributes

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File or directory name |

**Return value**

The attributes (FILE_ATTRIBUTE_READONLY, FILE_ATTRIBUTE_HIDDEN, ...)

**Description**

Gets file attributes

---

### selectDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `params` | `%[name:"", title:"", window:void, rootDir:""]` | Parameters, set in the same way as for selectFile |

**Return value**

true if a folder is selected and OK is pressed, false if Cancel is pressed
params.name Folder name. When OK is pressed, the selected folder is set in this member
params.title Title of the dialog box
params.window Window object that opens the dialog (if void, mainWindow is the owner window; if not specified, the desktop is the owner. When the desktop is the owner, the dialog is modeless)
params.rootDir Root of the folder selection (only folders under it are shown)

**Description**

Opens a folder selection dialog

Note: in environments where the engine implements Storages.selectDirectory, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).

---

### isExistentDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dir` | `&nbsp;` | Directory name |

**Return value**

true if the directory exists, -1 if it does not exist, false if it is not a directory

**Description**

Checks whether a directory exists

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.isExistentDirectory](Storages.md#isexistentdirectory) for the specification.

---

### getTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target file or directory |

**Return value**

Dictionary containing timestamp information
mtime: modified time (Date object)
atime: access time (Date object)
ctime: creation time (Date object)
Unlike fstat, it works only on non-archive files and does not return size
Note: the engine also has a method of the same name, but loading this plugin
replaces it with this version. Difference from the engine version: the engine version returns only mtime, not ctime / atime.

**Description**

Gets timestamps

---

### setTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target file or directory |
| `times` | `&nbsp;` | Dictionary containing timestamp information<br>mtime: modified time (Date object)<br>atime: access time (Date object)<br>ctime: creation time (Date object) |

**Return value**

Whether it succeeded

**Description**

Sets timestamps

---

### getLastModifiedFileTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target file or directory |

**Return value**

Time (64-bit Windows FILETIME value)

**Description**

Gets the modified time (fast version)

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.getLastModifiedFileTime](Storages.md#getlastmodifiedfiletime) for the specification.

---

### setLastModifiedFileTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `target` | `&nbsp;` | Target file or directory |
| `time` | `&nbsp;` | Time (64-bit Windows FILETIME value) |

**Return value**

Whether it succeeded

**Description**

Sets the modified time (fast version)

---

### copyFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | Source file |
| `to` | `&nbsp;` | Destination file |
| `failIfExist` | `&nbsp;` | true to fail if the file exists, false to overwrite |

**Return value**

true if the file was actually copied

**Description**

Copies the specified file in the Kirikiri storage space

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.copyFile](Storages.md#copyfile) for the specification.

---

### copyFileNoNormalize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `from` | `&nbsp;` | Source file |
| `to` | `&nbsp;` | Destination file |
| `failIfExist` | `&nbsp;` | true to fail if the file exists, false to overwrite |

**Return value**

true if the file was actually copied
Note: to must be written as a full path such as "file://./c/...", or an exception is raised

**Description**

Copies the specified file in the Kirikiri storage space without normalizing the path

(The destination file name is not converted to lowercase.)

---

### isExistentStorageNoSearchNoNormalize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name |

**Return value**

true if the file exists

**Description**

Checks whether a file exists without normalizing the path or searching autoPath

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.isExistentStorageNoSearchNoNormalize](Storages.md#isexistentstoragenosearchnonormalize) for the specification.

---

### getDisplayName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name (note that the parent directory and the rest of the path are dropped). |

**Return value**

Display name

**Description**

Gets the display name

Returns the file name as actually shown in Explorer (via SHGetFileInfo).

---

### getMD5HashString

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target file name |

**Return value**

Hash value (32-character lowercase hexadecimal string)

**Description**

Gets the MD5 hash

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.getMD5HashString](Storages.md#getmd5hashstring) for the specification.

---

### searchPath

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | File name to search for |
| `searchpath` | `&nbsp;` | Paths to search (local notation such as c:\\..., separated by ";"; if omitted, the system's default search path) |

**Return value**

void if not found; if found, the full path of the file (file://./...)

**Description**

Searches a path

---

### getTemporaryName

Method

**Return value**

Temporary file name (the string from TVPGetTemporaryName())

**Description**

Gets a temporary file name

Note: in environments where the engine has a method of the same name, the engine version is used
(this plugin registers it only as a fallback in older environments where the engine lacks it).
See the engine's [Storages.getTemporaryName](Storages.md#gettemporaryname) for the specification.

---

## Plugin extension: memfile

Manual written as pseudo-code

Files allocated in memory become accessible as mem://./filename.

### Members

#### Methods

- [isExistMemoryFile](#isexistmemoryfile)
- [isExistMemoryDirectory](#isexistmemorydirectory)
- [deleteMemoryFile](#deletememoryfile)
- [deleteMemoryDirectory](#deletememorydirectory)
- [getMemoryFileInfo](#getmemoryfileinfo)
- [getMemoryFileData](#getmemoryfiledata)
- [getMemoryDirectory](#getmemorydirectory)

---

### isExistMemoryFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target file name (without mem:///) |

**Return value**

true if it exists

**Description**

Checks whether a memory file exists

---

### isExistMemoryDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**Return value**

true if it exists

**Description**

Checks whether a memory directory exists

---

### deleteMemoryFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target file name (without mem:///) |

**Return value**

true if the file was deleted

**Description**

Deletes a memory file

---

### deleteMemoryDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dirname` | `&nbsp;` | Target directory name (without mem:///) |

**Return value**

true if the directory was deleted

**Description**

Deletes a memory directory

---

### getMemoryFileInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target file name (without mem:///) |

**Return value**

File information %[name:name, size:size, isDirectory:true if a directory]

**Description**

Gets memory file information

---

### getMemoryFileData

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Target file name (without mem:///) |

**Return value**

The file contents as an octet if the file exists; otherwise void

**Description**

Gets memory file information

---

### getMemoryDirectory

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dirname` | `&nbsp;` | Target directory name (without mem:///) |

**Return value**

Array of file information %[name:name, size:size, isDirectory:true if a directory]

**Description**

Gets memory directory information

---

## Plugin extension: minizip

Storages class extensions

### Members

#### Methods

- [mountZip](#mountzip)
- [unmountZip](#unmountzip)

---

### mountZip

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Domain name |
| `zipfile` | `&nbsp;` | Name of the ZIP file to mount |

**Return value**

true if mounted successfully

**Description**

Mounts a zip file as a file system

It becomes accessible as zip://domain/filename. It is read-only.

---

### unmountZip

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Domain name |

**Return value**

true if unmounted successfully

**Description**

Unmounts a zip file

---
