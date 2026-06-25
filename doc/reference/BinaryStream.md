# BinaryStream

## メンバー一覧

### コンストラクタ

- [BinaryStream](#binarystream)

### プロパティ

- [storage](#storage)
- [mode](#mode)

### メソッド

- [finalize](#finalize)
- [open](#open)
- [close](#close)
- [read](#read)
- [write](#write)
- [readI8](#readi8)
- [readI16LE](#readi16le)
- [readI32LE](#readi32le)
- [readI64LE](#readi64le)
- [readI16BE](#readi16be)
- [readI32BE](#readi32be)
- [readI64BE](#readi64be)
- [writeI8](#writei8)
- [writeI16LE](#writei16le)
- [writeI32LE](#writei32le)
- [writeI64LE](#writei64le)
- [writeI16BE](#writei16be)
- [writeI32BE](#writei32be)
- [writeI64BE](#writei64be)
- [copy](#copy)
- [compress](#compress)
- [decompress](#decompress)
- [setProgressCallback](#setprogresscallback)
- [setFilter](#setfilter)
- [seek](#seek)
- [tell](#tell)

### 定数

- [bsRead](#bsread)
- [bsWrite](#bswrite)
- [bsAppend](#bsappend)
- [bsUpdate](#bsupdate)
- [bsSeekSet](#bsseekset)
- [bsSeekCur](#bsseekcur)
- [bsSeekEnd](#bsseekend)

---

### BinaryStream

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` |  |
| `mode` | `&nbsp;` |  |

**解説**

コンストラクタ／デストラクタ

---

### storage

プロパティ \ アクセス: `r`

**解説**

現在開いているストレージ

開いていない場合はvoid

---

### mode

プロパティ \ アクセス: `r`

**解説**

現在のモード

開いていない場合は-1

---

### finalize

メソッド

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 対象ストレージ |
| `mode` | `&nbsp;` | モード指定(bsRead, bsWrite, bsAppend, bsUpdate) |

**解説**

ストレージを開く

---

### close

メソッド

**解説**

オープン中のストレージを閉じる

---

### read

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `size` | `&nbsp;` | 読み込むサイズ（バイト） |

**戻り値**

読み込んだデータ（octet形式） 終端などで読めなかった場合はvoid（length=0のoctetではないので注意）

**解説**

指定バイト読み込む

---

### write

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `data` | `&nbsp;` | 書き込むデータ（octet形式または文字列） |

**戻り値**

書き込んだバイト数

**解説**

データを書き込む

dataが文字列の場合は wchar で書き込まれます（コード変換はサポートされません）

---

### readI8

メソッド

**戻り値**

読み込んだ数値 / 終端などで読めなかった場合はvoid

**解説**

{1,2,4,8}バイトを数値として読み込む

※数値は8byte以外はunsigned読み込みになります（符号拡張されません）
※voidを返すのは1byteも読めなかった場合のみとなります
1byte以上指定byte未満しか読めなかった場合は足りない部分を0で埋めた値が返されるので注意

---

### readI16LE

メソッド

**解説**

2byte 読み込み (Little Endian)

---

### readI32LE

メソッド

**解説**

4byte 読み込み (Little Endian)

---

### readI64LE

メソッド

**解説**

8byte 読み込み (Little Endian)

---

### readI16BE

メソッド

**解説**

2byte 読み込み (Big Endian)

---

### readI32BE

メソッド

**解説**

4byte 読み込み (Big Endian)

---

### readI64BE

メソッド

**解説**

8byte 読み込み (Big Endian)

---

### writeI8

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` | 書き込む数値 |

**戻り値**

書き込んだバイト数

**解説**

{1,2,4,8}バイトで数値を書き込む

---

### writeI16LE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

2byte 書き込み (Little Endian)

---

### writeI32LE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

4byte 書き込み (Little Endian)

---

### writeI64LE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

8byte 書き込み (Little Endian)

---

### writeI16BE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

2byte 書き込み (Big Endian)

---

### writeI32BE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

4byte 書き込み (Big Endian)

---

### writeI64BE

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

8byte 書き込み (Big Endian)

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | コピー元のストレージ（現在開いているストレージと同じ場合は例外） |
| `elm` | `void` | 動作指定用の辞書（in/out）内容は下記：（省略時は単純コピー，[out]なし）<br>offset  :[in] コピー元ストレージの読み込み開始オフセット（省略時先頭）<br>length  :[in] コピー元ストレージの最大読み込みサイズ（省略時ファイルサイズ）<br>filter  :[in] フィルタ処理を行う関数名（省略時はフィルタ処理なし）<br>fparam  :[in] フィルタに渡すパラメータ値(int)<br>nocopy  :[in] trueを指定すると出力を書き込まない（省略時はfalse，hashのみ取得したい場合などに指定）<br>md5     :[in] trueを指定すると出力のMD5ダイジェストを返す<br>hash    :[out]読み込んだファイルのハッシュ値（Adler32）<br>read    :[out]読み込んだバイト数<br>digest  :[out]書き込んだデータのMD5ダイジェスト（octet） ※md5がtrueの場合にのみ有効 |

**戻り値**

書き込んだバイト数

**解説**

別のストレージからデータをコピー

対象ストレージのoffsetからlength分の内容が，現在のストリームのポジションから書き込まれます
フィルタの詳細は setFilter() の説明を参照してください

---

### compress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | コピー元のストレージ（現在開いているストレージと同じ場合は例外） |
| `elm` | `void` | 動作指定用の辞書（in/out）内容は copy() と同じものに加えて下記：<br>comp_lv :[in] zlibによる圧縮レベル（1～9）省略時，またはelmそのものの指定がない場合は 9 |

**戻り値**

書き込んだバイト数

**解説**

別のストレージからデータを圧縮しつつコピー

対象ストレージを zlib/deflate で圧縮しつつ，現在のストリームのポジションから書き込みます
フィルタ関数は圧縮前のバイナリに対して適用されます

---

### decompress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | コピー元のストレージ（現在開いているストレージと同じ場合は例外） |
| `elm` | `void` | 動作指定用の辞書（in/out）内容は copy() と同じ |

**戻り値**

書き込んだバイト数

**解説**

別のストレージからデータを展開しつつコピー

対象ストレージを zlib/inflate で展開しつつ，現在のストリームのポジションから書き込みます
展開に失敗すると例外が発生します
フィルタ関数は展開後のバイナリに対して適用されます
hash[out] は展開後／フィルタ後のバイナリに対して計算されます

---

### setProgressCallback

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | コールバック関数 function(storage, read_size) { return true_if_cancel; }<br>voidの場合は解除 |

**解説**

プログレスコールバックを設定する

copy/compress/decompress の処理中からコールバックする関数を設定します。
コールバックは（現在の実装では） 1MiB 読む毎時および最後まで読んだ時に呼び返されます。
コールバックから true を返すと処理がキャンセルできます。
※コールバックの間隔は変更される場合があります

TJS的には処理が固まってしまうのは仕様ですが，別途 windowExProgress プラグインなどを
使用することで，ユーザーからのキャンセルを受け付けられるようになります。

---

### setFilter

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dll` | `&nbsp;` | 対象のDLLファイル（voidの場合は設定解除） |

**解説**

フィルタDLLを設定する

copy/compress/decompressのデータに対して外部DLLを使用したフィルタを設定します
elm.filter に関数名を指定た場合に，このDLL中の下記の形式でエクスポートされた関数をフィルタとして使用します
void (__stdcall *FilterProc)(uint32 hash, uint64 offset, void *buffer, uint32 length);

---

### seek

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `pos` | `&nbsp;` | 位置 |
| `whence` | `&nbsp;` | 基準位置(bsSeekSet, bsSeekCur, bsSeekEnd) |

**戻り値**

移動後の位置

**解説**

ストリームのポジションを変更する

---

### tell

メソッド

**戻り値**

位置

**解説**

ストリームの現在のポジションを取得する

---

### bsRead

定数

値: `0`

**解説**

読み込み

---

### bsWrite

定数

値: `1`

**解説**

書き込み

---

### bsAppend

定数

値: `2`

**解説**

追記

---

### bsUpdate

定数

値: `3`

**解説**

更新

---

### bsSeekSet

定数

値: `0`

**解説**

先頭から

---

### bsSeekCur

定数

値: `1`

**解説**

現在位置から

---

### bsSeekEnd

定数

値: `2`

**解説**

末尾から

---
