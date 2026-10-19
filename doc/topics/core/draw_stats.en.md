---
source_hash: 74108e1f11b5
---

# Measuring DrawThreadPool Utilization (DrawStats)

Kirikiri Z's drawing runs internally through a parallel thread pool called
**DrawThreadPool** ( `TVPBeginThreadTask` / `TVPExecThreadTask` /
`TVPEndThreadTask` ). In a `KRKRZ_DRAW_STATS=ON` build, its utilization is
collected with atomic counters and can be observed in an on-screen overlay
and in the log.

The main purpose is **finding the cause when the main CPU is saturated while
the other cores sit idle**. This situation is typical on embedded platforms
such as the Switch, and this tool lets you narrow it down just by watching
from the outside.

Detailed usage and how to read the output are covered in the guide in src/core:

- [doc/DrawStats.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/DrawStats.md)

---

## Build

Toggle it with a CMake option. **Default is OFF (no effect on production builds)**.

```bash
cmake --preset x64-windows -DKRKRZ_DRAW_STATS=ON
cmake --build build/x64-windows --config Release
```

When OFF, the measurement macros expand to nothing and no atomic operations are generated.

### Threshold tuning

The **SCALE** in the threshold check `pixelNum >= factor * SCALE` of
`GetAdaptiveThreadNum` can be overridden at build time.

```bash
# 旧 PC 挙動 (1T 多め) で動かしたい場合
cmake --preset x64-windows -DKRKRZ_THREAD_PIXEL_SCALE=500
```

- **Default is 100** ( chosen from comparisons on actual Switch hardware )
- With 500 (the old value), single-thread execution dominates on the Switch and the workers go unused

---

## Display and how to read it

Enabling [`-memoverlay=1`](../../guide/CommandLine.md) also shows DrawStats
in the upper-right corner of the screen.

If the display scrolls too fast to read (for example on actual hardware), use
[System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) to switch
to log output every 500 ms ( in an OFF build or when the MemoryOverlay is
hidden, it harmlessly does nothing ).

---

## Related APIs

- [System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) — toggle DrawStats log output at run time
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — toggle the MemoryOverlay shown alongside it
- [System.drawThreadNum](../../reference/System.md#drawthreadnum) — get / set the number of drawing threads
