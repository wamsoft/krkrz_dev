# HttpRequest

## メンバー一覧

### コンストラクタ

- [HttpRequest](#httprequest)

### プロパティ

- [readyState](#readystate)
- [response](#response)
- [responseData](#responsedata)
- [status](#status)
- [statusText](#statustext)
- [contentType](#contenttype)
- [contentTypeEncoding](#contenttypeencoding)
- [contentLength](#contentlength)

### メソッド

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

### 定数

- [UNINITIALIZED](#uninitialized)
- [OPEN](#open)
- [SENT](#sent)
- [RECEIVING](#receiving)
- [LOADED](#loaded)

---

### HttpRequest

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` |  |
| `cert` | `true` |  |
| `agentName` | `"KIRIKIRI"` |  |

---

### readyState

プロパティ \ アクセス: `r`

---

### response

プロパティ \ アクセス: `r`

---

### responseData

プロパティ \ アクセス: `r`

---

### status

プロパティ \ アクセス: `r`

---

### statusText

プロパティ \ アクセス: `r`

---

### contentType

プロパティ \ アクセス: `r`

---

### contentTypeEncoding

プロパティ \ アクセス: `r`

---

### contentLength

プロパティ \ アクセス: `r`

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `method` | `&nbsp;` |  |
| `url` | `&nbsp;` |  |
| `userName` | `void` |  |
| `password` | `void` |  |

---

### setRequestHeader

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### send

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `data` | `void` |  |
| `storeStorage` | `void` |  |

---

### sendStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` |  |
| `storeStorage` | `void` |  |

---

### abort

メソッド

---

### getAllResponseHeaders

メソッド

---

### getResponseHeader

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### getResponseText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `encoding` | `void` |  |

---

### onReadyStateChange

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `readyState` | `&nbsp;` |  |

---

### onProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `upload` | `&nbsp;` |  |
| `percent` | `&nbsp;` |  |

---

### UNINITIALIZED

定数

値: `0`

---

### OPEN

定数

値: `1`

---

### SENT

定数

値: `2`

---

### RECEIVING

定数

値: `3`

---

### LOADED

定数

値: `4`

---
