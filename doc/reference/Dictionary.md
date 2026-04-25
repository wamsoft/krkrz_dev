# Dictionary

## メンバー一覧

### メソッド

- [saveStruct2](#savestruct2)
- [toStructString](#tostructstring)

---

### saveStruct2

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 格納先ファイル |
| `utf8` | `false` | 出力エンコーディング指定。true なら UTF-8、falseなら現在のコードページ |
| `newline` | `0` | 改行コード 0:CRLF 1:LF |
| `option` | `0` | 整形オプション sso* の組み合わせ（後述）もしくは直接数値指定 |

**解説**

データを saveStruct に準じる形式で保存する

---

### toStructString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `newline` | `1` | 改行コード 0:CRLF 1:LF |
| `option` | `0` | 整形オプション sso* の組み合わせ（後述）もしくは直接数値指定 |

**戻り値**

saveStruct に準じた形の文字列を返す

---
