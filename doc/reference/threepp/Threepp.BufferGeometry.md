# Threepp.BufferGeometry

バッファジオメトリ基底クラス

頂点データを格納するジオメトリの基底クラスです。

## メンバー一覧

### コンストラクタ

- [BufferGeometry](#buffergeometry)

### プロパティ

- [type](#type)
- [id](#id)
- [name](#name)

### メソッド

- [hasIndex](#hasindex)
- [hasAttribute](#hasattribute)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [computeVertexNormals](#computevertexnormals)
- [normalizeNormals](#normalizenormals)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [translate](#translate)
- [scale](#scale)
- [center](#center)
- [dispose](#dispose)

---

### BufferGeometry

コンストラクタ

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

ジオメトリの種類（読み取り専用）

---

### id

プロパティ \ アクセス: `r/w`

**解説**

ID（読み取り専用）

---

### name

プロパティ \ アクセス: `r/w`

**解説**

名前

---

### hasIndex

メソッド

**解説**

インデックスを持つか

---

### hasAttribute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

指定した属性を持つか

---

### computeBoundingBox

メソッド

**解説**

境界ボックスを計算

---

### computeBoundingSphere

メソッド

**解説**

境界球を計算

---

### computeVertexNormals

メソッド

**解説**

頂点法線を計算

---

### normalizeNormals

メソッド

**解説**

法線を正規化

---

### rotateX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

X軸回転

---

### rotateY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

Y軸回転

---

### rotateZ

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

Z軸回転

---

### translate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

平行移動

---

### scale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

スケーリング

---

### center

メソッド

**解説**

中心に移動

---

### dispose

メソッド

**解説**

リソースを解放

---
