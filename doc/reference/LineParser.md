# LineParser

## メンバー一覧

### コンストラクタ

- [LineParser](#lineparser)

### プロパティ

- [currentLineNumber](#currentlinenumber)

### メソッド

- [init](#init)
- [initStorage](#initstorage)
- [getNextLine](#getnextline)
- [parse](#parse)
- [parseStorage](#parsestorage)
- [doLine](#doline)

---

### LineParser

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | イベントを転送するターゲット。未指定時は自分に送る |

**解説**

コンストラクタ

---

### currentLineNumber

プロパティ \ アクセス: `r/w`

**解説**

現在の処理済み行番号を取得する

---

### init

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト |

**解説**

処理対象テキストの初期化

---

### initStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | テキストのファイル名 |
| `utf8` | `false` | UTF-8 のファイルを使う場合は true |

**解説**

処理対象テキストの初期化

---

### getNextLine

メソッド

**戻り値**

行

**解説**

次の行の情報を文字列として取得する

---

### parse

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト。省略時は現在設定中のテキストに対して処理を行なう |

**解説**

テキストに対するパース処理を実行する。

行ごとに doLine() イベントを呼び出す。

---

### parseStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | テキストのファイル名 |
| `utf8` | `false` | UTF-8 のファイルを使う場合は true |

**解説**

テキストに対するパース処理を実行する。

---

### doLine

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 行のテキスト情報 |
| `lineNo` | `&nbsp;` | 行番号(1からになる) |

**解説**

parse/parseStorage で呼び出されるイベント

---
