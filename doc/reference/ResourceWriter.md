# ResourceWriter

## メンバー一覧

### コンストラクタ

- [ResourceWriter](#resourcewriter)

### メソッド

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [clear](#clear)
- [writeFromText](#writefromtext)
- [writeFromFile](#writefromfile)
- [writeFromOctet](#writefromoctet)

---

### ResourceWriter

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` |  |
| `clean` | `&nbsp;` |  |

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | ファイル名(exeまたはdll) |
| `clean` | `false` | 既存のリソースを全てクリアするかどうか<br>基本的にオープンされていないファイルのみ操作可能です<br>＞自分自身のkrkr.exeやPlugins.linkでリンク済みのプラグインは操作できません |

**解説**

操作対象のファイルをオープン

---

### close

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `write` | `true` | 書き出す場合はtrue<br>write=falseの場合，writeFrom～やclearの処理がすべてキャンセルされ，書き出しは行われません<br>write=trueでも一度もwriteFrom～/clearを呼ばなかった場合も書き出しは行われません |

**解説**

操作対象のファイルをクローズ＆実書き出し

---

### setLang

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` |  |
| `subLang` | `&nbsp;` |  |

**解説**

書き出しの言語を指定

パラメータ内容は ResourceReader.setLang と同じです

---

### clear

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |
| `name` | `&nbsp;` | リソース名（文字列か数値）<br>※この関数を呼んでもclose(true)するまでは書き出しは保留されています |

**解説**

対象のリソースを削除

---

### writeFromText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | リソースタイプ（文字列か数値，もしくは rt*定数を指定） |
| `name` | `&nbsp;` | リソース名（文字列か数値） |
| `text` | `&nbsp;` | (writeFromTextのみ)対象のテキスト |
| `utf8` | `false` | (writeFromTextのみ)UTF-8エンコードで書き出す場合はtrue（falseの場合はUnicode） |

**解説**

リソースの書き出し

---

### writeFromFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

---

### writeFromOctet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `oct` | `&nbsp;` |  |

---
