# VertexBuffer

VertexBufferは頂点情報を保持するクラスです。

位置の指定やUV座標、頂点カラーなどを細かく設定したい場合に使用します。
単純な矩形ではなくメッシュ変形などを行いたい場合やポイントスプライトを使用したい場合などにも使用します。

プラグインで頂点の配列を直接変更できるようにポインタアクセスも可能です(ただしOpenGLES3.0以降)。
シェーダー+TJS2スクリプト+プラグインでの頂点操作で従来のようなLayer拡張性を確保できます。
従来のプラグイン内でほぼ完結していたものに比べるとやや複雑にはなります。

## メンバー一覧

### コンストラクタ

- [VertexBuffer](#vertexbuffer)
- [VertexBuffer](#vertexbuffer)

### プロパティ

- [size](#size)
- [dataType](#datatype)
- [updateType](#updatetype)
- [isIndex](#isindex)
- [nativeHandle](#nativehandle)

### メソッド

- [setVertex](#setvertex)
- [lock](#lock)
- [unlock](#unlock)

### 定数

- [dtByte](#dtbyte)
- [dtUByte](#dtubyte)
- [dtShort](#dtshort)
- [dtUShort](#dtushort)
- [dtInt](#dtint)
- [dtUInt](#dtuint)
- [dtFixed](#dtfixed)
- [dtFloat](#dtfloat)
- [utStream](#utstream)
- [utStatic](#utstatic)
- [utDynamic](#utdynamic)
- [ptPoints](#ptpoints)
- [ptLineStrip](#ptlinestrip)
- [ptLineLoop](#ptlineloop)
- [ptLines](#ptlines)
- [ptTriangleStrip](#pttrianglestrip)
- [ptTriangleFan](#pttrianglefan)
- [ptTriangles](#pttriangles)

---

### VertexBuffer

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `size` | `int` | `&nbsp;` | バッファのバイト数 |
| `dataType` | `int` | `&nbsp;` | データの型。dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat |
| `updateType` | `int` | `&nbsp;` | データ更新頻度。utStream/utStatic/utDynamic |
| `isIndex` | `bool` | `false` | インデックスバッファかどうか。頂点バッファならfalse |

**解説**

未初期化の頂点バッファを作ります

---

### VertexBuffer

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `data` | `Array` | `&nbsp;` | 頂点配列。バッファサイズはこの配列の要素数×データ型サイズ。 |
| `dataType` | `int` | `&nbsp;` | データの型。dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat |
| `updateType` | `int` | `&nbsp;` | データ更新頻度。utStream/utStatic/utDynamic |
| `isIndex` | `bool` | `false` | インデックスバッファかどうか。頂点バッファならfalse |

**解説**

頂点配列を指定して頂点バッファを作ります

---

### size

プロパティ \ アクセス: `r/w`

**解説**

バッファサイズ(readonly)

---

### dataType

プロパティ \ アクセス: `r/w`

**解説**

頂点データの型(readonly)

---

### updateType

プロパティ \ アクセス: `r/w`

**解説**

データ更新頻度(readonly)

---

### isIndex

プロパティ \ アクセス: `r/w`

**解説**

インデックスバッファかどうか(readonly)

---

### nativeHandle

プロパティ \ アクセス: `r/w`

**解説**

ネイティブハンドル

---

### setVertex

メソッド

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `array` | `Array` | `&nbsp;` | 頂点配列 |
| `offset` | `int` | `0` | 変更を開始する配列オフセットインデックス(非バイトサイズ) |

**解説**

頂点データを設定/更新

Staticの時は失敗します(例外)。

---

### lock

メソッド

**戻り値**

頂点データへのポインタ、ロックに失敗した時はnull

**解説**

頂点データをロックし、データへのポインタ(read/write指定)を返します

プラグイン用( OpenGL ES 3.0以降でないと使えません )

---

### unlock

メソッド

**解説**

頂点データのロックを解除します

プラグイン用( OpenGL ES 3.0以降でないと使えません )。
データの受け渡しが終わったら、バッファが使用される前に呼び出します。
lockを維持せず、更新したら即座にunlockするのが好ましいです。

---

### dtByte

定数

**解説**

データ型定数(byte)

---

### dtUByte

定数

**解説**

データ型定数(unsigned byte)

---

### dtShort

定数

**解説**

データ型定数(short)

---

### dtUShort

定数

**解説**

データ型定数(unsigned short)

---

### dtInt

定数

**解説**

データ型定数(int) ES3.0以降必要

---

### dtUInt

定数

**解説**

データ型定数(unsinged int) ES3.0以降必要

---

### dtFixed

定数

**解説**

データ型定数(fixed:固定少数点)

---

### dtFloat

定数

**解説**

データ型定数(float)

---

### utStream

定数

**解説**

更新頻度定数:毎フレーム更新

---

### utStatic

定数

**解説**

更新頻度定数:変更なし

---

### utDynamic

定数

**解説**

更新頻度定数:頻繁に更新される

---

### ptPoints

定数

**解説**

プリミティブ型定数(ポイントリスト)

---

### ptLineStrip

定数

**解説**

プリミティブ型定数(ラインストリップ)

---

### ptLineLoop

定数

**解説**

プリミティブ型定数(ラインループ)

---

### ptLines

定数

**解説**

プリミティブ型定数(ラインリスト)

---

### ptTriangleStrip

定数

**解説**

プリミティブ型定数(トライアングルストラップ)

---

### ptTriangleFan

定数

**解説**

プリミティブ型定数(トライアングルファン)

---

### ptTriangles

定数

**解説**

プリミティブ型定数(トライアングルリスト)

---
