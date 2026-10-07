# ResourceReader

## メンバー一覧

### コンストラクタ

- [ResourceReader](#resourcereader)

### メソッド

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [isExistentResource](#isexistentresource)
- [readToText](#readtotext)
- [readToFile](#readtofile)
- [readToOctet](#readtooctet)
- [enumTypes](#enumtypes)
- [enumNames](#enumnames)
- [enumLangs](#enumlangs)

---

### ResourceReader

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` |  |

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | ファイル名(exeまたはdll) |

**解説**

操作対象のファイルをオープン

---

### close

メソッド

**解説**

操作対象のファイルをクローズ

---

### setLang

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` | 主言語 |
| `subLang` | `&nbsp;` | 副言語 |

**戻り値**

設定されたWORD値
いずれもLANG_*やSUBLANG_*の文字列か，数値を指定します。
詳細は MAKELANGID などで検索してください。

**解説**

読み出しの言語を指定

---

### isExistentResource

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |
| `name` | `&nbsp;` | リソース名（文字列か数値） |

**戻り値**

存在する場合はtrue

**解説**

リソースが存在するかどうか

---

### readToText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |
| `name` | `&nbsp;` | リソース名（文字列か数値） |
| `utf8` | `false` | (readToTextのみ)対象がUTF-8エンコードの場合はtrue（falseの場合はUnicode） |

**戻り値**

voidの場合はリソースが存在しない，存在する場合は関数ごとに値が異なる

**解説**

リソースの読み込み

---

### readToFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

**解説**

-> 書き出したファイルサイズ

---

### readToOctet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |

**解説**

-> リソースのoctet

---

### enumTypes

メソッド

**戻り値**

[ type1, type2, ... ]

**解説**

リソースタイプ一覧取得

---

### enumNames

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |

**戻り値**

[ name1, name2, ... ]

**解説**

リソース名一覧取得

---

### enumLangs

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |
| `name` | `&nbsp;` | リソース名（文字列か数値） |

**戻り値**

[ lang1, lang2, ... ]
返る言語はprimaryLang,subLangを統合した数値なので注意してください。
この値をsetLangに渡したい場合は，setLang(lang&0x3FF, lang>>10) とします。

**解説**

リソース言語一覧取得

---
