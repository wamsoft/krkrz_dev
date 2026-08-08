# Threepp.Triangle

三角形クラス

## メンバー一覧

### コンストラクタ

- [Triangle](#triangle)

### プロパティ

- [a](#a)
- [b](#b)
- [c](#c)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getArea](#getarea)
- [getMidpoint](#getmidpoint)
- [getNormal](#getnormal)
- [getPlane](#getplane)
- [getBarycoord](#getbarycoord)
- [containsPoint](#containspoint)
- [isFrontFacing](#isfrontfacing)
- [closestPointToPoint](#closestpointtopoint)
- [equals](#equals)

---

### Triangle

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` | 頂点A (Vector3) |
| `b` | `&nbsp;` | 頂点B (Vector3) |
| `c` | `&nbsp;` | 頂点C (Vector3) |

**解説**

コンストラクタ

---

### a

プロパティ \ アクセス: `r/w`

**解説**

頂点A（読み取り専用）

---

### b

プロパティ \ アクセス: `r/w`

**解説**

頂点B（読み取り専用）

---

### c

プロパティ \ アクセス: `r/w`

**解説**

頂点C（読み取り専用）

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |

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
| `triangle` | `&nbsp;` |  |

**解説**

コピー

---

### getArea

メソッド

**解説**

面積

---

### getMidpoint

メソッド

**解説**

重心

---

### getNormal

メソッド

**解説**

法線

---

### getPlane

メソッド

**解説**

三角形を含む平面

---

### getBarycoord

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

重心座標を取得

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

### isFrontFacing

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `direction` | `&nbsp;` |  |

**解説**

前面を向いているか

---

### closestPointToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

最近点

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `triangle` | `&nbsp;` |  |

**解説**

等価判定

---
