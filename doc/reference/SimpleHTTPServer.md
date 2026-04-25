# SimpleHTTPServer

## メンバー一覧

### コンストラクタ

- [SimpleHTTPServer](#simplehttpserver)

### プロパティ

- [port](#port)
- [timeout](#timeout)
- [codepage](#codepage)

### メソッド

- [start](#start)
- [start](#start)
- [onRequest](#onrequest)

### 定数

- [cpACP](#cpacp)
- [cpOEM](#cpoem)
- [cpUTF8](#cputf8)
- [cpSJIS](#cpsjis)
- [cpEUC](#cpeuc)
- [cpJIS](#cpjis)

---

### SimpleHTTPServer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `port` | `0` | 使用するポート番号（0で自動割り当て） |
| `timeout` | `10` | onRequestコールバックのタイムアウト時間(sec) |
| `codepage` | `&nbsp;` |  |

**解説**

コンストラクタ

---

### port

プロパティ \ アクセス: `r`

---

### timeout

プロパティ \ アクセス: `r`

---

### codepage

プロパティ \ アクセス: `r/w`

**解説**

セッション毎のコードページ変更ができないので途中変更は推奨されない

---

### start

メソッド

**戻り値**

ポート番号

**解説**

サービス開始

---

### start

メソッド

**解説**

サービス停止

---

### onRequest

メソッド

**戻り値**

response = %[
status:ステータスコード（省略可能，エラーが無ければ自動で200）
content_type: Content-Type名
error_type:エラーの種類（text/file/binaryが無い場合に有効）
error_desc:エラーの説明（text/file/binaryが無い場合に有効）
redirect: リダイレクトする場合のURI（省略可能）

以下は排他（どれかひとつ，上から優先）
text:返すテキスト（codepageで自動エンコードされる）
file:返すファイル
binary:返すバイナリ（ArrayまたはOctet）
];

**解説**

リクエスト処理（イベント）

---

### cpACP

定数

値: `CP_ACP`

**解説**

コードページ（static value）

---

### cpOEM

定数

値: `CP_OEMCP`

---

### cpUTF8

定数

値: `CP_UTF8`

---

### cpSJIS

定数

値: `CP_932`

---

### cpEUC

定数

値: `CP_20932`

---

### cpJIS

定数

値: `CP_50220`

**解説**

51932

---
