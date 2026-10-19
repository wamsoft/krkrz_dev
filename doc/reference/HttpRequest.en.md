# HttpRequest

HttpRequest class

Provides asynchronous HTTP/HTTPS communication.
Sending and receiving run in the background.

## Members

### Constructors

- [HttpRequest](#httprequest)

### Properties

- [readyState](#readystate)
- [response](#response)
- [responseData](#responsedata)
- [status](#status)
- [statusText](#statustext)
- [contentType](#contenttype)
- [contentTypeEncoding](#contenttypeencoding)
- [contentLength](#contentlength)

### Methods

- [open](#open)
- [setRequestHeader](#setrequestheader)
- [send](#send)
- [sendStorage](#sendstorage)
- [abort](#abort)
- [getAllResponseHeaders](#getallresponseheaders)
- [getResponseHeader](#getresponseheader)
- [getResponseText](#getresponsetext)
- [onReadyStateChange](#onreadystatechange)
- [onProgress](#onprogress)

### Constants

- [UNINITIALIZED](#uninitialized)
- [OPEN](#open)
- [SENT](#sent)
- [RECEIVING](#receiving)
- [LOADED](#loaded)

---

### HttpRequest

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `window` | `&nbsp;` | Parent window used for thread synchronization. |
| `cert` | `true` | Whether to check certificates during HTTP communication. false accepts any certificate. |
| `agentName` | `"KIRIKIRI"` | User agent name used for HTTP communication. |

**Description**

Constructor

---

### readyState

Property \ Access: `r`

**Description**

Communication state. Read-only

---

### response

Property \ Access: `r`

**Description**

Response. Read-only

---

### responseData

Property \ Access: `r`

**Description**

Response. Read-only

---

### status

Property \ Access: `r`

**Description**

HTTP status code of the response. Read-only

---

### statusText

Property \ Access: `r`

**Description**

HTTP status text of the response

---

### contentType

Property \ Access: `r`

**Description**

Content-Type of the response (without the encoding)

---

### contentTypeEncoding

Property \ Access: `r`

**Description**

Encoding specified in the response's Content-Type

The header takes precedence. If it is not specified and the received data is text/html,
the META tag at the beginning of the file is also checked.

---

### contentLength

Property \ Access: `r`

**Description**

Content-Length of the response

If it is not in the header, the size is determined once the download completes.

---

### open

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `method` | `&nbsp;` | Request method. |
| `url` | `&nbsp;` | URL to request. |
| `userName` | `void` | User name. If given, an authentication header is added. |
| `password` | `void` | Password. |

**Description**

Prepares a request to the given URL with the given method

The call is always asynchronous.

---

### setRequestHeader

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Header name. |
| `value` | `&nbsp;` | Value. |

**Description**

Adds a header to send with the request

---

### send

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `data` | `void` | Data to send.<br>octet  : sent as-is<br>string : encoded with the default encoding and sent<br>other  : no data is sent |
| `storeStorage` | `void` |  |

**Description**

Sends the request. Sending runs asynchronously

No exception is thrown on errors; check readyState and status instead.

---

### sendStorage

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | File data to send. |
| `storeStorage` | `void` |  |

**Description**

Sends the request. Sending and receiving run asynchronously

No exception is thrown on errors; check readyState and status instead.

---

### abort

Method

**Description**

Cancels the transfer in progress

---

### getAllResponseHeaders

Method

**Return value**

A dictionary containing the HTTP headers.

**Description**

Gets all HTTP headers

---

### getResponseHeader

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Header name. |

**Return value**

The header value.

**Description**

Gets the given HTTP header

---

### getResponseText

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `encoding` | `void` | Encoding. If omitted, the Content-Type is used. |

**Description**

Gets the response as text

---

### onReadyStateChange

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `readyState` | `&nbsp;` | The new state. |

**Description**

Event raised when readyState changes

---

### onProgress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `upload` | `&nbsp;` | true while sending. |
| `percent` | `&nbsp;` | Progress (0 to 100%). |

**Description**

Data transfer event

---

### UNINITIALIZED

Constant

Value: `0`

**Description**

readyState: initial state

---

### OPEN

Constant

Value: `1`

**Description**

readyState: processing started

---

### SENT

Constant

Value: `2`

**Description**

readyState: request sent

---

### RECEIVING

Constant

Value: `3`

**Description**

readyState: receiving

---

### LOADED

Constant

Value: `4`

**Description**

readyState: loading complete

---
