# Threepp.Matrix3

3x3 行列クラス

## メンバー一覧

### コンストラクタ

- [Matrix3](#matrix3)

### メソッド

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [setFromMatrix4](#setfrommatrix4)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [invert](#invert)
- [transpose](#transpose)
- [getNormalMatrix](#getnormalmatrix)
- [scale](#scale)
- [rotate](#rotate)
- [translate](#translate)
- [equals](#equals)

---

### Matrix3

コンストラクタ

**解説**

コンストラクタ

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |

**解説**

要素を設定

---

### identity

メソッド

**解説**

単位行列に設定

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

コピー

---

### setFromMatrix4

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

Matrix4から設定

---

### multiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

乗算

---

### premultiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

前置乗算

---

### multiplyMatrices

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つの行列の積

---

### multiplyScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラー乗算

---

### determinant

メソッド

**解説**

行列式

---

### invert

メソッド

**解説**

逆行列

---

### transpose

メソッド

**解説**

転置

---

### getNormalMatrix

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

法線行列を取得

---

### scale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

**解説**

スケーリング

---

### rotate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**解説**

回転

---

### translate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |

**解説**

平行移動

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

等価判定

---
