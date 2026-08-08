# Threepp.InstancedMesh

インスタンスメッシュ

同じジオメトリとマテリアルを複数インスタンス描画します。

## メンバー一覧

### コンストラクタ

- [InstancedMesh](#instancedmesh)

### プロパティ

- [type](#type)
- [count](#count)

### メソッド

- [getMatrixAt](#getmatrixat)
- [setMatrixAt](#setmatrixat)
- [getColorAt](#getcolorat)
- [setColorAt](#setcolorat)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [dispose](#dispose)

---

### InstancedMesh

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `geometry` | `&nbsp;` | ジオメトリ (BufferGeometry) |
| `material` | `&nbsp;` | マテリアル (Material) |
| `count` | `&nbsp;` | インスタンス数 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"InstancedMesh"（読み取り専用）

---

### count

プロパティ \ アクセス: `r/w`

**解説**

インスタンス数

---

### getMatrixAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**解説**

インスタンスの変換行列を取得

---

### setMatrixAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**解説**

インスタンスの変換行列を設定

---

### getColorAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**解説**

インスタンスの色を取得

---

### setColorAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**解説**

インスタンスの色を設定

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

### dispose

メソッド

**解説**

リソースを解放

---
