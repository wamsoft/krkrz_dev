# Threepp.Box3

軸平行境界ボックス (AABB) クラス

## メンバー一覧

### コンストラクタ

- [Box3](#box3)

### プロパティ

- [min](#min)
- [max](#max)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeEmpty](#makeempty)
- [isEmpty](#isempty)
- [getCenter](#getcenter)
- [getSize](#getsize)
- [expandByPoint](#expandbypoint)
- [expandByVector](#expandbyvector)
- [expandByScalar](#expandbyscalar)
- [containsPoint](#containspoint)
- [containsBox](#containsbox)
- [intersectsBox](#intersectsbox)
- [intersectsSphere](#intersectssphere)
- [intersectsPlane](#intersectsplane)
- [distanceToPoint](#distancetopoint)
- [intersect](#intersect)
- [union_](#union_)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Box3

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` | 最小座標 (Vector3) |
| `max` | `&nbsp;` | 最大座標 (Vector3) |

**解説**

コンストラクタ

---

### min

プロパティ \ アクセス: `r/w`

**解説**

最小座標（読み取り専用）

---

### max

プロパティ \ アクセス: `r/w`

**解説**

最大座標（読み取り専用）

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

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
| `box` | `&nbsp;` |  |

**解説**

コピー

---

### makeEmpty

メソッド

**解説**

空にする

---

### isEmpty

メソッド

**解説**

空かどうか

---

### getCenter

メソッド

**解説**

中心を取得

---

### getSize

メソッド

**解説**

サイズを取得

---

### expandByPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点で拡張

---

### expandByVector

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vector` | `&nbsp;` |  |

**解説**

ベクトルで拡張

---

### expandByScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `scalar` | `&nbsp;` |  |

**解説**

スカラーで拡張

---

### containsPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点を含むか

---

### containsBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

ボックスを含むか

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

### intersectsSphere

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**解説**

球と交差するか

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

### distanceToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点との距離

---

### intersect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

交差部分を取得

---

### union_

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

和集合を取得

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
| `box` | `&nbsp;` |  |

**解説**

等価判定

---
