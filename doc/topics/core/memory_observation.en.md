---
source_hash: 5551c6826b96
---

# Memory Observation and Leak Investigation

The Kirikiri Z engine includes a set of facilities for observing memory usage
and per-allocator breakdowns in real time. This page is a guide to the
**entry points**. For design details and rationale, see the developer
documentation in src/core.

- Detailed guide: [doc/MemoryGuide.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryGuide.md)
- Design and implementation rationale: [doc/MemoryDesign.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryDesign.md)
- Leak audit workflow: [doc/LeakAudit.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LeakAudit.md)

---

## Allocator Layout

Memory inside the engine is measured in four categories by purpose, plus external memory.

| Allocator | Main use |
|---|---|
| **FileAllocator** | Binaries held by StorageCache (file-layer cache) |
| **BitmapAllocator** | The bits area of `Bitmap` |
| **SoundAllocator** | Work areas for PCM / ring buffers / DSP |
| **GlobalAlloc[Krkrz]** | Allocations through `operator new` / `TJS_malloc` (TLSF pool) |
| **GlobalAlloc[SDL]** | Allocations inside SDL3 (only in builds with `KRKRZ_SDLMEMORY_STAT=ON`) |
| External | Internal mallocs in C libraries such as ANGLE / miniaudio / opus / libpng, GL textures, direct HeapAlloc |

`GlobalAlloc[Krkrz]` is further broken down by thread-local **tags**
( `TJS2` / `GraphicsLoader` / `User` / `Unknown` ).

---

## Observing from TJS2

The [System](../../reference/System.md) class provides observation APIs.

- [System.getSystemAllocatorInfo](../../reference/System.md#getsystemallocatorinfo) — Gets a dictionary including process RSS / VSize and free system memory.
- [System.resetMemoryPeak](../../reference/System.md#resetmemorypeak) — Resets peak measurements to the current values.
- [System.beginAllocTag](../../reference/System.md#beginalloctag) / [System.endAllocTag](../../reference/System.md#endalloctag) — Measure script-originated allocations separately under a tag.
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — Toggles the on-screen overlay at runtime.

For the file cache ( file layer ) and the image decode cache ( decode layer ),
[Storages](../../reference/Storages.md) provides observation APIs.

- [Storages.getFileCacheList](../../reference/Storages.md#getfilecachelist) / [Storages.getImageCacheList](../../reference/Storages.md#getimagecachelist) — Get the list of entries as an array of dictionaries
- [Storages.dumpFileCacheList](../../reference/Storages.md#dumpfilecachelist) / [Storages.dumpImageCacheList](../../reference/Storages.md#dumpimagecachelist) — Dump to the log at WARNING level
- [Storages.pinCache](../../reference/Storages.md#pincache) / [Storages.unpinCache](../../reference/Storages.md#unpincache) / [Storages.isCachePinned](../../reference/Storages.md#iscachepinned) — Per-entry pin management
- [Storages.clearTransientCaches](../../reference/Storages.md#cleartransientcaches) / [Storages.clearAllCaches](../../reference/Storages.md#clearallcaches) — Bulk clearing

---

## Command-Line Options

Command-line options for memory investigation are available ( details: [Command-line options](../../guide/CommandLine.md) ).

| Option | Function |
|---|---|
| `-memoverlay=1` | Shows a memory status overlay in the top-right corner of the screen from startup ( drawn by the OGL-family / SDL `DrawDevice`; not shown with D3D11, the WINVER default ) |
| `-memstatinterval=N` | Logs memory statistics every N seconds |
| `-memstatonexit=1` | Logs memory statistics once on exit |
| `-cachelistonexit=<mode>` | Dumps the Storages cache list on exit ( `1`/`all`/`file`/`image`/`0`/`none` ) |

In builds with `KRKRZ_ENABLE_PERIODIC_DUMP=OFF`, the periodic dump options (`memstat*`/`cachelistonexit`) are ignored.

---

## Observing from the REPL

In builds with the [REPL](repl.md) enabled, you can inspect memory status
directly from the interactive shell ( `.mem` / `.memdump` / `.memoverlay` /
`.mempeakclear` / `.sysalloc` / `.filecache` / `.imagecache`, etc. ).

---

## Finding What Holds Memory ( Diagnostic Build )

When the live size of `GlobalAlloc[Krkrz]` is too large to be explained by the
number of TJS objects, investigate the breakdown with a diagnostic build using
`KRKRZ_ENABLE_MEMSTAT_DETAIL=ON`. It is not included in release builds ( Windows only ).

The following items are added to the `.memdump` output.

| Item | Contents |
|---|---|
| `live by size` | Count and bytes of live allocations by size ( in half-octave steps ) |
| `member tables` / `per-class member table bytes` | Total and per-class size of TJS object member tables ( hash table slot arrays and chain nodes ) |
| `string heap` | Block count, fill ratio, and duplicate strings with identical contents in the TJS string heap |

In addition, the command-line option `-memstatsite=<depth>` ( `yes` means 16 frames )
captures a stack for each allocation and counts live bytes and allocations **per call site**.
At the end of `.memdump` and with the REPL command `.memsites [count] [part of function name]`,
results are listed in descending order, per first function outside the allocator internals and
per call chain. Modules with a PDB show function names and source lines; plugin DLLs without
a PDB are shown with their module name.

- Because a stack is captured for every allocation, startup and processing become considerably slower.
- The diagnostic build widens the allocation header from 16 bytes to 32 bytes to hold the site number, so the overall process memory cannot be compared with a release build ( the live size of `GlobalAlloc[Krkrz]` can be compared, since it is the sum of requested sizes ).
- Logs go to the console log ( `-forcelog=yes` ).
