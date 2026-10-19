---
source_hash: 8a87b09a91a9
---

# Dealing with Out-of-Memory Errors

You may see errors such as "ビットマップ用メモリを確保できません/……" or "Cannot allocate memory for Bitmap : ……".  
They seem to occur more often as screen resolutions get larger.  
Kirikiri Z is less prone to them than Kirikiri 2, but they can still happen.  
Settings can reduce how often they occur, however.  

## Cause
When a game hits this error, the cause is more often memory fragmentation than an actual shortage of memory.  
Fragmentation tends to occur when large allocations, such as for images, are mixed with small allocations for small objects, strings and so on.  
As fragmentation progresses, large blocks can no longer be allocated, and attempts to allocate large areas such as bitmap memory fail.

## Countermeasures
Some memory management algorithms are less prone to fragmentation, so adopting one of them is one approach. Windows Vista and later use such an algorithm, and fragmentation appears to be reduced.  
On XP, enabling [LFH](https://msdn.microsoft.com/ja-jp/library/windows/desktop/aa366750%28v=vs.85%29.aspx) has a similar effect (Kirikiri Z targets Vista and later, so it is always enabled).  
Even with this feature enabled, the error can still occur, so other countermeasures include running compaction and putting image memory in a separate region.

### Compaction
Compaction joins adjacent free areas of memory into large contiguous free areas.  
After many allocations and frees it becomes fairly expensive, so run it only occasionally.  
In Kirikiri Z, adding the -ghcompact option (configurable from the engine settings) compacts the global heap whenever System.doCompact is called.  
Because it adds some load, it is disabled by default.  
If it runs without strain on the lowest-spec CPU you target, it is fine to release with it enabled by default.

### Separate heap
Separating bitmap memory, which allocates only relatively large blocks, from everything else prevents fragmentation from progressing.  
This can be configured from the engine settings.  
By default memory is allocated from the process heap, which is fine in most cases.  
If the error shows up in testing, try it, and if it helps, make the separate heap the default setting.

### Calling GC
Calling System.doCompact from your script during scene transitions (for example, while the screen is blacked out) probably helps a little.

### Not using the graphic cache
Not using the graphic cache, or keeping it as small as possible, helps prevent memory fragmentation.  
If the countermeasures above have no effect, consider disabling the graphic cache.  
Without the graphic cache things feel noticeably slower, especially when skipping, but on recent CPUs and machines with SSDs the difference is not very noticeable, so going without the cache should be fine.

### Using the 64-bit build
If none of the countermeasures above help, consider the ultimate countermeasure: the 64-bit build.  
It can make full use of the installed memory, which also resolves the complaint that the error occurs despite plenty of installed memory.  
64-bit is becoming standard everywhere, so it is probably worth providing a 64-bit build from now on regardless of memory issues.
