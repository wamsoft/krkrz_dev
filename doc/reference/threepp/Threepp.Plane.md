# Threepp.Plane

平面クラス

## メンバー一覧

### コンストラクタ

- [Plane](#plane)

### メソッド

- [set](#set)
- [setComponents](#setcomponents)
- [setFromNormalAndCoplanarPoint](#setfromnormalandcoplanarpoint)
- [clone](#clone)
- [copy](#copy)
- [normalize](#normalize)
- [negate](#negate)
- [distanceToPoint](#distancetopoint)
- [distanceToSphere](#distancetosphere)
- [coplanarPoint](#coplanarpoint)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Plane

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `normal` | `&nbsp;` | 法線 (Vector3) |
| `constant` | `&nbsp;` | 定数 |

**解説**

コンストラクタ

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `constant` | `&nbsp;` |  |

**解説**

値を設定

---

### setComponents

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**解説**

成分で設定

---

### setFromNormalAndCoplanarPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `point` | `&nbsp;` |  |

**解説**

法線と点から設定

---

### clone

メソッド

**解説**

クローン

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**解説**

コピー

---

### normalize

メソッド

**解説**

正規化

---

### negate

メソッド

**解説**

反転

---

### distanceToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点との距離

---

### distanceToSphere

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**解説**

球との距離

---

### coplanarPoint

メソッド

**解説**

平面上の点を取得

---

### applyMatrix4

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

行列を適用

---

### translate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `offset` | `&nbsp;` |  |

**解説**

平行移動

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**解説**

等価判定

---
