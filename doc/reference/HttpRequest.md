# HttpRequest

HttpRequestクラス

HTTP/HTTPS による非同期通信機能を提供します。
ファイルの送受信処理はバックグラウンド実行されます。
疑似コードによるマニュアル

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
| `window` | `&nbsp;` | スレッド同期処理用親ウインドウ |
| `cert` | `true` | HTTP通信時に証明書チェックを行うかどうか。falseにすると強制許可になります。 |
| `agentName` | `"KIRIKIRI"` | HTTP通信時のエージェント名 |

**解説**

コンストラクタ

---

### readyState

プロパティ \ アクセス: `r`

**解説**

通信状態。読み込み専用

---

### response

プロパティ \ アクセス: `r`

**解説**

レスポンス。読み込み専用。

---

### responseData

プロパティ \ アクセス: `r`

**解説**

レスポンス。読み込み専用

---

### status

プロパティ \ アクセス: `r`

**解説**

レスポンスの HTTPステータスコード。読み込み専用

---

### statusText

プロパティ \ アクセス: `r`

**解説**

レスポンスの HTTPステータスの文字列

---

### contentType

プロパティ \ アクセス: `r`

**解説**

レスポンスの Content-Type (エンコーディング指定は含まない)

---

### contentTypeEncoding

プロパティ \ アクセス: `r`

**解説**

レスポンスの Content-Type のエンコード指定

ヘッダの指定が優先されますが、未指定、かつ受信データが text/html の場合は
ファイル冒頭にある META 指定も参照します。

---

### contentLength

プロパティ \ アクセス: `r`

**解説**

レスポンスの Content-Length

ヘッダに無い場合はファイルダウンロード完了後にサイズ確定します。

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `method` | `&nbsp;` | アクセスメソッド |
| `url` | `&nbsp;` | リクエスト先のURL |
| `userName` | `void` | ユーザ名。指定すると認証ヘッダをつけます |
| `password` | `void` | パスワード |

**解説**

指定したメソッドで指定URLにリクエストする

※常に非同期での呼び出しになります

---

### setRequestHeader

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ヘッダ名 |
| `value` | `&nbsp;` | 値 |

**解説**

送信時に送られるヘッダーを追加する

---

### send

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `data` | `void` | 送信するデータ<br>octetの場合  : そのまま送信<br>文字列の場合 : 規定のエンコードで処理して送信<br>その他       : データは送信されません |
| `storeStorage` | `void` |  |

**解説**

リクエストの送信。送信処理は非同期実行されます。

エラー時も例外は発生しませんので、readyState と status で判定してください。

---

### sendStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 送信するファイルデータ |
| `storeStorage` | `void` |  |

**解説**

リクエストの送信。送受信は非同期実行されます。

エラー時も例外は発生しませんので、readyState と status で判定してください。

---

### abort

メソッド

**解説**

現在実行中の送受信のキャンセル

---

### getAllResponseHeaders

メソッド

**戻り値**

HTTPヘッダが格納された辞書

**解説**

すべての HTTPヘッダを取得する

---

### getResponseHeader

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ヘッダラベル名 |

**戻り値**

ヘッダの値

**解説**

指定したHTTPヘッダを取得する

---

### getResponseText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `encoding` | `void` | エンコード指定。省略時は Content-type の指定に従います。 |

**解説**

レスポンスをテキストの形で取得

---

### onReadyStateChange

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `readyState` | `&nbsp;` | 新しいステート |

**解説**

readyState が変化した場合のイベント

------------------------------------ ------------------------------------

---

### onProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `upload` | `&nbsp;` | 送信中は true |
| `percent` | `&nbsp;` | 進捗状態(0〜100%) |

**解説**

データ送受信イベント

---

### UNINITIALIZED

定数

値: `0`

**解説**

readyState 初期状態

---

### OPEN

定数

値: `1`

**解説**

readyState 処理開始

---

### SENT

定数

値: `2`

**解説**

readyState リクエスト送信

---

### RECEIVING

定数

値: `3`

**解説**

readyState 受信中

---

### LOADED

定数

値: `4`

**解説**

readyState 読み込み完了

---
