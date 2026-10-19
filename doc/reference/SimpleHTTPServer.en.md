# SimpleHTTPServer

## Members

### Constructors

- [SimpleHTTPServer](#simplehttpserver)

### Properties

- [port](#port)
- [timeout](#timeout)
- [codepage](#codepage)

### Methods

- [start](#start)
- [stop](#stop)
- [onRequest](#onrequest)

### Constants

- [cpACP](#cpacp)
- [cpOEM](#cpoem)
- [cpUTF8](#cputf8)
- [cpSJIS](#cpsjis)
- [cpEUC](#cpeuc)
- [cpJIS](#cpjis)

---

### SimpleHTTPServer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `port` | `0` | Port number to use (0 assigns one automatically). |
| `timeout` | `10` | Timeout for the onRequest callback, in seconds. |
| `codepage` | `&nbsp;` |  |

**Description**

Constructor

---

### port

Property \ Access: `r`

---

### timeout

Property \ Access: `r`

---

### codepage

Property \ Access: `r/w`

**Description**

The code page cannot be changed per session, so changing it while running is not recommended

---

### start

Method

**Return value**

Port number.

**Description**

Starts the service

---

### stop

Method

**Description**

Stops the service

---

### onRequest

Method

**Return value**

response = %[
status: status code (optional; 200 automatically if there is no error)
content_type: Content-Type name
error_type: error type (used when there is no text/file/binary)
error_desc: error description (used when there is no text/file/binary)
redirect: URI to redirect to (optional)

The following are mutually exclusive (only one; earlier ones take precedence):
text: text to return (encoded automatically using codepage)
file: file to return
binary: binary to return (Array or Octet)
];

**Description**

Request handling (event)

---

### cpACP

Constant

Value: `CP_ACP`

**Description**

Code page (static value)

---

### cpOEM

Constant

Value: `CP_OEMCP`

---

### cpUTF8

Constant

Value: `CP_UTF8`

---

### cpSJIS

Constant

Value: `CP_932`

---

### cpEUC

Constant

Value: `CP_20932`

**Description**

51932

---

### cpJIS

Constant

Value: `CP_50220`

---
