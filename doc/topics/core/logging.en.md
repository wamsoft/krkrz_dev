---
source_hash: 2f0c94232724
---

# Logging

Kirikiri Z writes a runtime log to the console and/or a file.
The output level and format can be controlled in several ways.

For the detailed specification and design, see the guide in src/core:

- [doc/Logging.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Logging.md)

---

## Log levels

Kirikiri Z has the following five log levels (higher in the list means more important).

- `error` — errors
- `warning` — warnings ( `TVPAddImportantLog` )
- `info` — normal log ( `TVPAddLog` )
- `debug` — debug information
- `off` — suppress everything

The build-time defaults are:

| Build | Default level |
|---|---|
| `MASTER` | `warning` |
| Release ( non-MASTER ) | `info` |
| Debug | `debug` |

To override it at run time, use the command-line option
[`-loglevel=<level>`](../../guide/CommandLine.md).
This is handy for temporarily collecting a detailed log from a distributed binary.

```
krkrz64 -loglevel=debug data/
```

---

## Related options

| Option | Function |
|---|---|
| `-loglevel=<level>` | Set the log level at run time |
| `-debug=yes` | Debug mode ( enables debugging aids ) |
| `-forcelog=yes` | Always write the console log to a file |
| `-logerror=yes` | Write the log to a file on error |
| `-memstatinterval=N` | Periodic memory statistics log |
| `-memstatonexit=1` | Statistics log on exit |
| `-cachelistonexit=<mode>` | Cache list log on exit |
