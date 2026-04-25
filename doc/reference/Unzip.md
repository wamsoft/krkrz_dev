# Unzip

ZIP 展開クラス

## メンバー一覧

### コンストラクタ

- [Unzip](#unzip)

### メソッド

- [open](#open)
- [list](#list)
- [extract](#extract)
- [close](#close)

---

### Unzip

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
| `force_utf8` | `0` | 0:ファイル名の文字コードは最初のファイルで自動判別 1:UTF8強制 |

**解説**

ZIPアーカイブを展開用にオープンします

---

### list

メソッド

**戻り値**

ファイル一覧(ファイル情報の配列)
ファイル情報は辞書の形で、以下の情報を含みます
<dl>
<dt>filename <dd>アーカイブ内パス名
<dt>uncompressed_size <dd>展開サイズ
<dt>compressed_size <dd>圧縮サイズ
<dt>crypted <dd>暗号化されているか
<dt>deflated <dd>圧縮されているか
<dt>deflateLevel <dd>圧縮レベル
<dt>crc <dd>ファイルのCRD
</dl>

**解説**

ZIPアーカイブ中に含まれるファイルの情報を取得します

---

### extract

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `srcname` | `&nbsp;` | 展開元ファイル(アーカイブ内パス名） |
| `destfile` | `&nbsp;` | 展開先ファイル（吉里吉里ストレージ名） |
| `password` | `void` | パスワード指定 |

**戻り値**

展開に成功したら true

**解説**

ファイルの展開

---

### close

メソッド

**解説**

ZIPアーカイブをクローズします

---
