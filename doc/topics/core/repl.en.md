---
source_hash: 2be0e9c2214a
---

# REPL (Read-Eval-Print Loop)

Launching a binary built with `KRKRZ_REPL=ON` with the command-line argument `-repl`
(or `-repl=yes`) enables an interactive TJS shell. Supported on Windows, macOS, and
Linux. Line editing is provided by
[icline](https://github.com/deths74r/icline) (a fork of isocline).

For the full specification (command list, editing features, troubleshooting),
see the guide in src/core:

- [doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)

---

## Launching

```bash
krkrz -repl data/      # SDL 版
krkrz64 -repl data/    # Win32 版 (親コンソールに AttachConsole)
```

Without `-repl`, the REPL does not start (there is no automatic TTY detection).
You can also disable it explicitly with `-repl=no` / `-repl=off` / `-repl=false` / `-repl=0`.

Building with `KRKRZ_REPL_LINE_EDIT=OFF` produces a minimal mode with no icline
dependency (line editing such as arrow keys is disabled).

### Options

All REPL-related options are collected here (see each section for details, and
[Command-line options](../../guide/CommandLine.md) for the syntax). They are all
independent and can be combined.

| Option | Default | Description |
|---|---|---|
| `-repl[=yes\|no\|new]` | Off | Console REPL. `new` forces a new console |
| `-replfile=<dir>` | Off | File channel (**the primary choice for agent-driven use**) |
| `-replsocket=<name>` | Off | Abstract Unix socket channel (Linux-family systems) |
| `-replweb[=[host:]port]` | Off | HTTP + SSE server + browser UI (default 127.0.0.1:8899) |
| `-replwebopen=app\|tab\|no` | Auto, conditional | Opens the browser automatically. **Not opened by default when launched from a terminal** |
| `-replwebidle=<sec>\|no` | **5 seconds** | Delay before exiting once no browser is connected |
| `-replwebpad=<dir>` | Writes disabled | Storage prefix under which the Pad tab's [Save] is allowed |
| `-replwatchfile=<path>\|no` | `.krkrz_watch` | Where the watch expression list is saved |
| `-replmodaltimeout=<sec>` | 30 | Timeout when waiting for a modal response (0 = infinite) |

`-nostartup` (do not run startup.tjs) and `-loglevel=` are not REPL-specific, but
they are often used together with agent-driven sessions.

---

## Main special commands

The prompt is `krkrz>` and continuation lines show `...`. You can enter TJS
expressions and statements directly; history is saved to `.krkrz_history`.

| Command | Description |
|---|---|
| `exit` / `quit` / `Ctrl+D` | Leave the REPL and quit the application |
| `.help` | Show help |
| `.clear` | Clear the buffer of a pending multi-line input |
| `.depth [N]` | Show / set the expansion depth of result output |
| `.compact [on\|off]` | Toggle compact mode for result output |
| `.mem` | One-line summary of allocator + process memory |
| `.memdump` | Dump detailed memory statistics to the log |
| `.memsites [N] [function]` | Dump the top N live allocations grouped by call site to the log (diagnostic build + launched with `-memstatsite`. Passing a function name limits output to call chains containing that function) |
| `.memoverlay [on\|off]` | Toggle the on-screen overlay (SDL3 build) |
| `.mempeakclear` | Reset the peak measurement to current_used |
| `.sysalloc` | Show system allocator info (free / allocatable / RSS) on one line |
| `.padoverlay [on\|off]` | Toggle the pad overlay (SDL3 build) |
| `.filecache` | Dump all StorageCache (file layer) entries to the log |
| `.imagecache` | Dump all TVPGraphicCache (decode layer) entries to the log |
| `.cap [path]` | Save the actual screen of the next frame (including overlays) as PNG |
| `.dlg` | List active dialogs |
| `.dlgclose` | Close the frontmost dialog |
| `.click X Y` | Inject a mouse click at (X,Y) (`Agent.click`) |
| `.watch` | List watch expressions as `id: expr = value` (all are evaluated before display) |
| `.watch add EXPR` | Add a watch expression and evaluate it immediately |
| `.watch rm ID` / `.watch rm all` | Remove a watch expression / remove all |
| `.watch edit ID EXPR` | Replace a watch expression |
| `.watch auto [ms\|on\|off]` | Show / set the auto-refresh interval (`on` = 500ms, `0` = every frame, minimum 100ms) |
| `.event [on\|off\|toggle]` | Show / toggle `System.eventDisabled` |

For details on the memory commands see the [memory observation guide](memory_observation.md);
for the pad overlay see [PadOverlay](pad_overlay.md).

`.watch` corresponds to the "watch expressions" debug window that Kirikiri 2 had
built into the engine. Once expressions are registered, each `.watch` (or each
auto-refresh tick) evaluates them all and lists expressions alongside their values.
The evaluation context is always global, and if an expression throws, it just shows
`(error) <message>` **as the value**, so one broken watch expression never kills
the REPL or the application.

The expression list and auto-refresh interval are **saved to `.krkrz_watch` in the
current directory** and loaded back on the next launch (change it with
`-replwatchfile=<path>`, disable with `=no`).

---

## Error handler behavior while the REPL is active

When the REPL is enabled with `-repl` or `-replfile`, an uncaught exception no longer
terminates Kirikiri Z immediately. Instead of showing a native dialog, the exception
is only logged with a stack trace, so you can fix the problem and eval again.
Likewise, output from `System.inform` and `Application::MessageDlg` is redirected to
the REPL console (only the default response is returned, and no dialog is shown), so
headless automated tests do not stall.

Combined with `-nostartup`, automatic execution of startup.tjs is also suppressed,
which lets you start idle with no window and then kick off processing explicitly
from the REPL (see `-nostartup` in [Command-line options](../../guide/CommandLine.md)
for details).

---

## File channel (-replfile)

Specifying `-replfile=<dir>` starts a file-based REPL channel that does not go
through the console. An external agent writes a command file in the specified
directory to submit a TJS expression, then reads the result JSON from a response
file (lockstep). It can be enabled independently of `-repl`, and both can be used
at the same time.

```bash
krkrz -replfile=./replbus data/
```

It is intended for headless automated tests and for controlling krkrz from an agent
running in another process. See the src/core documentation for protocol details.

Lines starting with `.` are treated as **special commands**, and the same output as
the console REPL goes into the `result` field of the response JSON (an agent can call
`.watch` / `.mem` / `.cap` and so on directly).

---

## Browser UI (-replweb)

The embedded page returned by `GET /` is organized as **Console / Watch tabs**.

| Tab | Contents |
|---|---|
| Console | Log on top / input at the bottom (the original page) |
| Watch | Table of watch expressions (expression / value) + add, remove, inline edit (double-click) + auto-refresh interval |
| Pad | Script editor. Run multiple lines with Ctrl+Enter, load / save from storage |

**You can add your own panels as tabs** (`WebServer.registerPanel`). Serve your own
page with `serveStatic` and pass its path; it appears to the right of the built-in
tabs. The content is an iframe, so it does not depend on the built-in UI's internal
structure, and the panel can call `/cmd`, `/watch`, `/pad/exec`, or your own
endpoints on the same origin.

```tjs
WebServer.serveStatic("/tool/", "web/");
WebServer.registerPanel("mytool", "案件ツール", "/tool/tool.html");
```

Hosting an entire page of your own (`serveStatic` alone) loses Console / Watch / Pad
and the controller, so **if you just want to add an observation panel, this is the
better fit**.

Since it is built into the engine, `-replweb` alone is all you need (no plugin or
script required). To replace it with your own UI, use `WebServer.serveStatic`.

### Keeping the browser UI and the application lifetimes in sync

With a browser as the UI, the worst outcome is **one side being left behind** (the
window is closed but the engine keeps running / the engine has exited but a
«disconnected» page remains). Both directions are handled.

**Engine side** — exits when no browser remains (`-replwebidle`)

| State | Behavior |
|---|---|
| From launch **until the first connection** | Waits (never exits) |
| One or more connections | Keeps running |
| All connections gone | Exits after `<sec>` |

**Enabled by default (5 seconds)**. Disable with `-replwebidle=no`, or set the
number of seconds with `=<sec>`. It is armed **only when launched with `-replweb`**;
a server started from TJS with `WebServer.start()` is not armed (so a server the
application manages itself is never shut down behind its back).
**It arms only after at least one connection has arrived**, so agent-driven use that
never opens a browser, or use as an API surface, is unaffected. Closing the page
sends a signal (`POST /bye`), so the engine normally exits in about 2 seconds.

**Browser side** — closes when the engine is gone

| State | Behavior |
|---|---|
| Engine announces it is exiting (`exiting` on `/sub/state`) | Closes the window immediately |
| SSE drops and does not recover within 5 seconds (crash, etc.) | Closes the window |
| `window.close()` has no effect (regular tab) | Shows "Kirikiri Z has exited" full-page |

### Display language

**By default it follows the engine's language setting** (`-language=` and the OS
language are reflected as-is, matching the engine's messages). You can also switch
on the spot with the language selector at the top; the choice is remembered by that
browser.

Currently **Japanese / English** are supported. If the engine has selected another
language (Chinese, etc.), it falls back to English the same way the engine does.

### Pad (script editor)

Write multi-line TJS and **run it all at once with Ctrl+Enter** (unlike the
single-line execution of `/cmd`, you can submit function definitions and loops
as-is). The text is auto-saved to the browser's `localStorage`, so it survives
a reload.

The path field + [Load] / [Save] exchange files with storage, but **saving is
disabled by default**. Only when `-replwebpad=<dir>` is specified can you write
under that directory (a fence against "accidentally hitting [Save] in the UI and
overwriting assets". Anyone who can open `-replweb` can already run arbitrary TJS,
so this is not a security boundary).

### Automatic browser launch (-replwebopen)

By default it opens in app mode only when "bound to loopback and there is no console
(GUI launch)". **It does not open when launched from a terminal**. Explicit values
are `-replwebopen=app` (app mode) / `tab` (regular window) / `no` (do not open).
To launch from a terminal and still open the browser, use `-replwebopen=app`.

---

## Watch expression HTTP API (-replweb)

With `-replweb`, watch expressions can also be handled from a browser or curl.

| Route | Description |
|---|---|
| `GET /watch` | List + current values (JSON). **Does not evaluate**, so polling is safe. `?eval=1` evaluates before returning |
| `POST /watch` | Operations (form-urlencoded). `op=add&expr=…` / `op=rm&id=…` / `op=edit&id=…&expr=…` / `op=clear` / `op=interval&ms=…` / `op=eval` |
| `GET /sub/watch` | Auto-refresh push (SSE). Sent when a value changes, and on changes that involve no evaluation (remove / clear / interval change) |

!!! warning "Built-in routes are matched before register"
    `/` `/events` `/cmd` `/sub/<ch>` `/watch` `/state` `/pad/exec` `/pad/file`
    `/bye` **cannot be overridden** by [WebServer.register](../../reference/WebServer.md#register) /
    [serveStatic](../../reference/WebServer.md#servestatic).
    Use a different prefix (`/api/`, `/ui/`, etc.) for your own endpoints.

```bash
curl -s -X POST -d 'op=add&expr=System.getTickCount()' localhost:8899/watch
curl -s -X POST -d 'op=interval&ms=500'                localhost:8899/watch
curl -N localhost:8899/sub/watch
```

Responses and pushes have the same shape.

```json
{"interval":500,"entries":[{"id":1,"expr":"System.getTickCount()","value":"32470","error":false}]}
```

---

## Socket channel (-replsocket / Linux-family only)

Specifying `-replsocket=<name>` (or the environment variable `KRKRZ_REPL_SOCKET`)
starts a command channel listening on an abstract-namespace Unix domain socket
(Linux-family builds only; ignored on other OSes). It is the socket version of the
file channel: it accepts one command (TJS expression) per line, runs it on the main
thread, and replies with one line of JSON. It can be started independently of
`-repl` / `-replfile`, and they can be used together.

- A `\` at the end of a line marks a continuation line, so multiple lines can be run
  as one command with line breaks preserved (a continuation marker on the wire that
  also works from tools like `nc`).
- A single line beginning with `.` is interpreted as a channel-side dot command
  (`.help` / `.depth` / `.compact`).

---

## Agent class for agent-driven use (SDL3 build)

The SDL3 version of a `KRKRZ_REPL` build includes the
[Agent](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)
TJS class for driving krkrz from external agents and automated tests. Like the
`System` class, it is called through class methods (no instantiation needed).

| Feature | API (main methods) |
|---|---|
| Input injection | `Agent.mouseMove / mouseDown / mouseUp / click / wheel`, `Agent.keyDown / keyUp / keyPress`, `Agent.text` |
| Dialog observation / control | `Agent.dialogs()` / `Agent.dialogTree(index)` / `Agent.dialogClick(index, id)` / `Agent.dialogFocus(index, id)` / `Agent.closeDialog()` / `Agent.closeAllDialogs()` |
| Screen capture | `Agent.captureScreen(path[, x, y, w, h])` / `Agent.lastCapture()` |

Input via `Agent` goes through the same `TTVPWindowForm::Send*` path as real input,
so it reaches both the game and [Dialog](../../reference/ElementsDialog.md).
`captureScreen` reads back the actual screen, including overlays, just before the
next frame's present and saves it as PNG (even if the engine is idle when requested,
it is saved one frame later).

The class is registered only in SDL3 builds with `KRKRZ_REPL=ON`. For specification
details (button constants, shift mask, the file channel protocol, etc.) see
[doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md).
