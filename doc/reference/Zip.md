# Zip

ZIP 圧縮クラス

## メンバー一覧

### コンストラクタ

- [Zip](#zip)

### メソッド

- [open](#open)
- [add](#add)
- [close](#close)

---

### Zip

コンストラクタ

**解説**

コンストラクタ

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名 |
| `overwrite` | `0` | 0:通常作成 1:上書き 2:追記 |

**解説**

ZIPアーカイブを書き込み用にオープンします

---

### add

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `srcfile` | `&nbsp;` | 追加するファイル（吉里吉里ストレージ名） |
| `destfile` | `&nbsp;` | アーカイブ中での名前(アーカイブ内パス名） |
| `commpressLevel` | `void` |  |
| `password` | `void` | 暗号化パスワード指定 |
| `compressionMethod` | `Zip.CompressionMethodDeflate` | 圧縮メソッド |
| `clearDate` | `false` | 日付指定を空にする指定。デフォルトはファイルの日付を格納 |

**戻り値**

追加に成功したら true

**解説**

アーカイブにファイルを追加します

---

### close

メソッド

**解説**

ZIPアーカイブをクローズします

---
