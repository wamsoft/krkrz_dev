# CSVParser

## メンバー一覧

### コンストラクタ

- [CSVParser](#csvparser)

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

### CSVParser

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | イベントを転送するターゲット。未指定時は自分に送る |
| `separator` | `&nbsp;` | 区切り文字。デフォルトは "," |
| `newline` | `&nbsp;` | 中途で区切られた場合のデータでの改行文字。デフォルトは "\\r\\n" |

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
| `readmode` | `false` | 読み込みモード<br>typeof readmode == "String"  : Array.load相当のテキスト読み込み処理として動作<br>typeof readmode == "Integer" : trueの場合はUTF-8読み込みモードとして動作，それ以外はCP_ACPテキスト読み込み<br>※プラグインコンパイル時に /D:CSVPARSER_DEFAULT_TEXTSTREAM=1 とすると，readmode='' の省略時デフォルトになります |

**解説**

処理対象テキストの初期化

---

### getNextLine

メソッド

**戻り値**

カラムデータ(Array)

**解説**

次の行の情報を配列として取得する

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
| `readmode` | `&nbsp;` | 読み込みモード（詳細説明はinitStorageの項目を参照） |

**解説**

テキストに対するパース処理を実行する。

---

### doLine

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `columns` | `&nbsp;` | カラムデータ(Array) |
| `lineNo` | `&nbsp;` | 論理行番号(1～) |

**解説**

parse/parseStorage で呼び出されるイベント

---
