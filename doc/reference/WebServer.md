# WebServer

WebServer クラスは吉里吉里Z に組み込まれた HTTP + SSE サーバを制御するためのクラスです。このクラスからオブジェクトを作成することはできません。System と同様に `WebServer.start(...)` のように直接呼び出して使用します。

このサーバはコマンドラインオプションの `-replweb` によって使用されるもので、TJS からエンドポイントを登録することで、ブラウザ UI や外部からの制御を組むことができます。このクラスは `KRKRZ_REPL_WEB` を有効にしたビルドでのみ利用できます。

登録するハンドラは `handler(req)` の形式で、`req` は以下のキーを持つ辞書です。ハンドラは必ずメインスレッドで実行されます。

- `method` ... HTTP メソッド ( "GET" / "POST" 等 )
- `path`   ... リクエストパス
- `query`  ... クエリ文字列
- `body`   ... リクエストボディ ( 文字列 )
- `bytes`  ... リクエストボディ ( オクテット。body が空でない場合のみ存在 )

ハンドラの戻り値によってレスポンスが決まります。

- 文字列   ... 200 application/json として返します
- オクテット ... 200 application/octet-stream として返します
- 整数     ... そのステータスコードで空ボディを返します
- void     ... 204 を返します
- 辞書 `%[status, mime, body]` ... 指定した通りに返します
- TJS 例外が発生した場合は 500 を返します

また、以下のルートはサーバ側に組み込まれています ( TJS のメンバではありません )。

- `GET /`            ... ビューワー本体
- `GET /events`      ... REPL コンソール用の SSE ストリーム
- `POST /cmd`        ... REPL へのコマンド送信
- `GET /sub/<channel>` ... 任意チャンネルの SSE 購読

## メンバー一覧

### プロパティ

- [active](#active)
- [url](#url)

### メソッド

- [register](#register)
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

プロパティ \ アクセス: `r`

**解説**

サーバが稼働中かどうか

サーバが稼働中の場合に真を返します。読み出し専用。

**関連:** [WebServer.url](WebServer.md#url)

---

### url

プロパティ \ アクセス: `r`

**解説**

待受 URL

サーバの待受 URL ( `http://host:port/` 形式 ) を表します。稼働していない
場合は空文字列になります。読み出し専用。

**関連:** [WebServer.active](WebServer.md#active)

---

### register

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | ハンドラを割り当てるパスの接頭辞を指定します。 |
| `handler` | `&nbsp;` | `handler(req)` 形式のハンドラ関数を指定します。 |

**解説**

動的ハンドラの登録

指定した prefix に対して動的ハンドラを登録します。マッチングは最長一致で
行われます。同一の prefix に登録した場合は上書きされます。

**関連:** [WebServer.unregister](WebServer.md#unregister)

---

### unregister

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 削除するハンドラの接頭辞を指定します。 |

**戻り値**

ハンドラが見つかって削除できた場合は 1、見つからなかった場合は 0 が返ります。

**解説**

動的ハンドラの削除

[WebServer.register](WebServer.md#register) で登録したハンドラを削除します。

**関連:** [WebServer.register](WebServer.md#register)

---

### serveStatic

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 配信対象とするパスの接頭辞を指定します。 |
| `storageDir` | `&nbsp;` | 配信元となるストレージのディレクトリを指定します。 |

**解説**

静的配信のマウント

prefix 以下への GET リクエストを、storageDir に相対パスを連結した
ストレージから配信します。相対パスに `..` が含まれる場合は 403 を返します。

**関連:** [WebServer.unserveStatic](WebServer.md#unservestatic)

---

### unserveStatic

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 削除する静的配信の接頭辞を指定します。 |

**戻り値**

マウントが見つかって削除できた場合は 1、見つからなかった場合は 0 が返ります。

**解説**

静的配信のアンマウント

[WebServer.serveStatic](WebServer.md#servestatic) で登録した静的配信の
マウントを削除します。

**関連:** [WebServer.serveStatic](WebServer.md#servestatic)

---

### broadcast

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `channel` | `&nbsp;` | 配信先のチャンネル名を指定します。 |
| `text` | `&nbsp;` | 配信するテキストを指定します。 |

**解説**

SSE 購読者への配信

`/sub/<channel>` を購読しているすべての SSE クライアントへ text を push します。
text には複数行を含めることができます。

---

### start

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `port` | `8899` | 待受ポート番号を指定します。 |

**戻り値**

起動後の稼働状態が返ります。

**解説**

サーバの起動

127.0.0.1 でサーバを起動します。

**関連:** [WebServer.startAt](WebServer.md#startat) / [WebServer.stop](WebServer.md#stop)

---

### startAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `host` | `&nbsp;` | 待受ホストを指定します。 |
| `port` | `&nbsp;` | 待受ポート番号を指定します。 |

**戻り値**

起動後の稼働状態が返ります。

**解説**

ホストを指定したサーバの起動

明示したホストでサーバを起動します。"0.0.0.0" を指定するとすべての
ネットワークインターフェースで待ち受けます。

**関連:** [WebServer.start](WebServer.md#start) / [WebServer.stop](WebServer.md#stop)

---

### stop

メソッド

**解説**

サーバの停止

サーバを停止します。接続中のクライアントを閉じ、accept スレッドを終了します。

**関連:** [WebServer.start](WebServer.md#start)

---

### openBrowser

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `url` | `""` | 開く URL を指定します。省略した場合は稼働中のサーバの URL を<br>使用します。 |
| `appMode` | `true` | 真を指定すると、まず Edge → Chrome の順に `--app=` による<br>アプリモードでの起動を試み、いずれも無い場合は OS の既定ブラウザで開きます。 |

**戻り値**

成否が返ります。

**解説**

ブラウザで開く

ブラウザで指定した url を開きます。

**関連:** [WebServer.url](WebServer.md#url)

---
