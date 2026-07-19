# XMLParser

擬似コードによるマニュアル

Copyright 2005-2009 GoWatanabe

expat による処理がおこなわれて自動的にメソッド呼び返し処理が行われます
具体的な DOM の実装例は XML.tjs 参照

## メンバー一覧

### プロパティ

- [errorCode](#errorcode)
- [errorString](#errorstring)
- [currentByteIndex](#currentbyteindex)
- [currentLineNumber](#currentlinenumber)
- [currentColumnNumber](#currentcolumnnumber)
- [currentButeCount](#currentbutecount)

### メソッド

- [parse](#parse)
- [parseStorage](#parsestorage)

---

### errorCode

プロパティ \ アクセス: `r/w`

**解説**

エラーコード数値

---

### errorString

プロパティ \ アクセス: `r/w`

**解説**

エラーコード文字列

---

### currentByteIndex

プロパティ \ アクセス: `r/w`

**解説**

現在のバイトインデックス

---

### currentLineNumber

プロパティ \ アクセス: `r/w`

**解説**

現在の行番号

---

### currentColumnNumber

プロパティ \ アクセス: `r/w`

**解説**

現在の行番号

---

### currentButeCount

プロパティ \ アクセス: `r/w`

**解説**

現在のバイトカウント

---

### parse

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト。省略時は現在設定中のテキストに対して処理を行なう |

**解説**

テキストに対するパース処理を実行する。

---

### parseStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | テキストのファイル名 |

**解説**

テキストに対するパース処理を実行する。

---
