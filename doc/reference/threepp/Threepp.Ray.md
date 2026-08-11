# Threepp.Ray

光線クラス

## メンバー一覧

### コンストラクタ

- [Ray](#ray)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [at](#at)
- [lookAt](#lookat)
- [recast](#recast)
- [closestPointToPoint](#closestpointtopoint)
- [distanceToPoint](#distancetopoint)
- [distanceSqToPoint](#distancesqtopoint)
- [distanceSqToSegment](#distancesqtosegment)
- [intersectSphere](#intersectsphere)
- [intersectsSphere](#intersectssphere)
- [intersectBox](#intersectbox)
- [intersectsBox](#intersectsbox)
- [intersectPlane](#intersectplane)
- [intersectsPlane](#intersectsplane)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Ray

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `origin` | `&nbsp;` | 原点 (Vector3) |
| `direction` | `&nbsp;` | 方向 (Vector3) |

**解説**

コンストラクタ

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

**解説**

値を設定

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
| `ray` | `&nbsp;` |  |

**解説**

コピー

---

### at

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

光線上の点を取得

---

### lookAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

方向を設定

---

### recast

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

原点を移動

---

### closestPointToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

最近点を取得

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

### distanceSqToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

距離の二乗

---

### distanceSqToSegment

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v0` | `&nbsp;` |  |
| `v1` | `&nbsp;` |  |

**解説**

線分との距離の二乗

---

### intersectSphere

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**解説**

球との交点

---

### intersectsSphere

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**解説**

球と交差するか

---

### intersectBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

ボックスとの交点

---

### intersectsBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

ボックスと交差するか

---

### intersectPlane

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**解説**

平面との交点

---

### intersectsPlane

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**解説**

平面と交差するか

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

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `ray` | `&nbsp;` |  |

**解説**

等価判定

---
