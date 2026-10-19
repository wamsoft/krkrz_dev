# WebServer

!!! warning "Experimental (not covered by stability guarantees)"
    The shape of this API is not settled yet. **It may change or be removed
    without notice** (the major version is not bumped even for incompatible changes).
    See [versioning](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)
    for how versions are bumped.

    開発・検証用の API です。REPL / デバッグ窓の整備にあわせて変わります。 組み込みルートは予告なく増えることがあります ( 増えたパスは register で上書きできません )。

The WebServer class controls the HTTP + SSE server built into Kirikiri Z. You cannot create objects from this class; like System, call its members directly, as in `WebServer.start(...)`.

This server is the one used by the `-replweb` command-line option. By registering endpoints from TJS, you can build a browser UI or control the engine externally. This class is only available in builds with `KRKRZ_REPL_WEB` enabled.

A registered handler has the form `handler(req)`, where `req` is a dictionary with the following keys. Handlers always run on the main thread.

- `method` ... HTTP method ( "GET" / "POST", etc. )
- `path`   ... request path
- `query`  ... query string
- `body`   ... request body ( string )
- `bytes`  ... request body ( octet; present only when body is not empty )

The handler's return value determines the response.

- string   ... returned as 200 application/json
- octet    ... returned as 200 application/octet-stream
- integer  ... returns that status code with an empty body
- void     ... returns 204
- dictionary `%[status, mime, body]` ... returned exactly as specified
- if a TJS exception is thrown, 500 is returned

The following routes are built into the server ( they are not TJS members ).

- `GET /`              ... the viewer itself ( tabbed UI with Console / Watch / Pad )
- `GET /events`        ... SSE stream for the REPL console
- `POST /cmd`          ... sends a command to the REPL
- `GET /sub/<channel>` ... SSE subscription to an arbitrary channel
- `GET`/`POST /watch`  ... get / manipulate watch expressions
- `GET`/`POST /state`  ... controller ( `System.eventDisabled` / exit request )
- `POST /pad/exec` , `GET`/`POST /pad/file` ... Pad ( script editor )
- `GET /panels`      ... list of registered panels ( used by the built-in UI to build its tabs )
- `POST /bye`          ... signal that the page is closing

!!! warning "Built-in routes are matched before register"
    The paths above **cannot be overridden** with [WebServer.register](WebServer.md#register) or
    [serveStatic](WebServer.md#servestatic).
    Use a different prefix for your own endpoints
    ( e.g. `/api/` `/ui/` ).

!!! warning "Receive multibyte values such as Japanese text in body"
    `query` is passed as the still percent-encoded string. `System.urldecode`,
    which decodes it, is limited to the native Windows build, so
    **SDL3 builds cannot receive non-ASCII values through the query**.
    It is safest to pass strings in `body` ( UTF-8 ) and keep `query` to
    ASCII values such as numbers and identifiers.

A minimal implementation example is in the core demo `webui` ( static serving, dynamic
endpoints, and push from the game combined on one screen ).

## Members

### Properties

- [active](#active)
- [url](#url)

### Methods

- [register](#register)
- [registerPanel](#registerpanel)
- [unregisterPanel](#unregisterpanel)
- [unregister](#unregister)
- [serveStatic](#servestatic)
- [unserveStatic](#unservestatic)
- [broadcast](#broadcast)
- [start](#start)
- [startAt](#startat)
- [stop](#stop)
- [openBrowser](#openbrowser)

---

### active

Property \ Access: `r`

**Description**

Whether the server is running

True while the server is running. Read-only.

**See also:** [WebServer.url](WebServer.md#url)

---

### url

Property \ Access: `r`

**Description**

Listening URL

The server's listening URL ( in the form `http://host:port/` ). Empty string when
the server is not running. Read-only.

**See also:** [WebServer.active](WebServer.md#active)

---

### register

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `prefix` | `&nbsp;` | Path prefix to assign the handler to. |
| `handler` | `&nbsp;` | Handler function of the form `handler(req)`. |

**Description**

Registers a dynamic handler

Registers a dynamic handler for the given prefix. Matching uses the longest
prefix. Registering the same prefix again overwrites the previous handler.

**See also:** [WebServer.unregister](WebServer.md#unregister)

---

### registerPanel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Panel identifier. Used as the key for overwriting and removal. |
| `label` | `&nbsp;` | Name shown on the tab. |
| `path` | `&nbsp;` | URL path of the panel content. Specify **a server path starting with `/`**<br>( not a local file path ). If it is invalid, the panel is not<br>registered and the reason is written to the log. |

**Description**

Adds a panel ( tab ) to the built-in UI

Adds **one panel of your own as a tab** to the right of the built-in `-replweb`
browser UI ( Console / Watch / Pad ). Serve your own page with
[serveStatic](WebServer.md#servestatic) and pass its path as
`path`.

The content is **loaded in an iframe**. Scripts are not injected into the built-in page
so that your project does not depend on the built-in UI's internal DOM
( which would break your project whenever the built-in UI changes ). The panel is on the same
origin, so it can freely call the server with `fetch` or `EventSource`
( the built-in `/cmd` `/watch` `/pad/exec`, or endpoints you
[register](WebServer.md#register) yourself ).

Calling again with the same `id` overwrites the panel. Registration and removal are
**reflected immediately in open pages** ( tabs appear or disappear ). A panel's content is
**loaded the first time its tab is opened**, so registering a heavy tool does not slow down startup.

```tjs
WebServer.serveStatic("/tool/", "web/");
WebServer.registerPanel("mytool", "Tool", "/tool/tool.html");
```

**See also:** [WebServer.unregisterPanel](WebServer.md#unregisterpanel)

---

### unregisterPanel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` | Identifier of the panel to remove. |

**Return value**

1 if the panel was found and removed, 0 if it was not found.

**Description**

Removes a panel from the built-in UI

Removes a tab added with [registerPanel](WebServer.md#registerpanel).
It also disappears immediately from open pages.

**See also:** [WebServer.registerPanel](WebServer.md#registerpanel)

---

### unregister

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `prefix` | `&nbsp;` | Prefix of the handler to remove. |

**Return value**

1 if the handler was found and removed, 0 if it was not found.

**Description**

Removes a dynamic handler

Removes a handler registered with [WebServer.register](WebServer.md#register).

**See also:** [WebServer.register](WebServer.md#register)

---

### serveStatic

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `prefix` | `&nbsp;` | Path prefix to serve. |
| `storageDir` | `&nbsp;` | Storage directory to serve from. |

**Description**

Mounts static file serving

Serves GET requests under prefix from storage, using storageDir joined with the relative path.
Returns 403 if the relative path contains `..`.

**See also:** [WebServer.unserveStatic](WebServer.md#unservestatic)

---

### unserveStatic

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `prefix` | `&nbsp;` | Prefix of the static serving mount to remove. |

**Return value**

1 if the mount was found and removed, 0 if it was not found.

**Description**

Unmounts static file serving

Removes a static serving mount registered with [WebServer.serveStatic](WebServer.md#servestatic).

**See also:** [WebServer.serveStatic](WebServer.md#servestatic)

---

### broadcast

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `channel` | `&nbsp;` | Name of the destination channel. |
| `text` | `&nbsp;` | Text to push. |

**Description**

Pushes to SSE subscribers

Pushes text to every SSE client subscribed to `/sub/<channel>`.
text may contain multiple lines.

---

### start

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `port` | `8899` | Port number to listen on. |

**Return value**

Whether the server is running after the call.

**Description**

Starts the server

Starts the server on 127.0.0.1.

**See also:** [WebServer.startAt](WebServer.md#startat) / [WebServer.stop](WebServer.md#stop)

---

### startAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `host` | `&nbsp;` | Host to listen on. |
| `port` | `&nbsp;` | Port number to listen on. |

**Return value**

Whether the server is running after the call.

**Description**

Starts the server on a given host

Starts the server on the given host. Specifying "0.0.0.0" listens on all
network interfaces.

**See also:** [WebServer.start](WebServer.md#start) / [WebServer.stop](WebServer.md#stop)

---

### stop

Method

**Description**

Stops the server

Stops the server. Closes connected clients and ends the accept thread.

**See also:** [WebServer.start](WebServer.md#start)

---

### openBrowser

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `url` | `""` | URL to open. If omitted, the URL of the running server is<br>used. |
| `appMode` | `true` | If true, first tries launching Edge, then Chrome, in app mode with `--app=`;<br>if neither is available, opens the OS default browser. |

**Return value**

Whether it succeeded.

**Description**

Opens a browser

Opens the given url in a browser.

**See also:** [WebServer.url](WebServer.md#url)

---
