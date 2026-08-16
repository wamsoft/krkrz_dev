# Threepp.Line3

3D 線分クラス

## メンバー一覧

### コンストラクタ

- [Line3](#line3)

### プロパティ

- [start](#start)
- [end](#end)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getCenter](#getcenter)
- [delta](#delta)
- [distanceSq](#distancesq)
- [distance](#distance)
- [at](#at)
- [closestPointToPoint](#closestpointtopoint)
- [closestPointToPointParameter](#closestpointtopointparameter)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Line3

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `start` | `&nbsp;` | 始点 (Vector3) |
| `end` | `&nbsp;` | 終点 (Vector3) |

**解説**

コンストラクタ

---

### start

プロパティ \ アクセス: `r/w`

**解説**

始点（読み取り専用）

---

### end

プロパティ \ アクセス: `r/w`

**解説**

終点（読み取り専用）

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `start` | `&nbsp;` |  |
| `end` | `&nbsp;` |  |

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
| `line` | `&nbsp;` |  |

**解説**

コピー

---

### getCenter

メソッド

**解説**

中心を取得

---

### delta

メソッド

**解説**

方向ベクトルを取得

---

### distanceSq

メソッド

**解説**

長さの二乗

---

### distance

メソッド

**解説**

長さ

---

### at

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

パラメータ位置の点を取得

---

### closestPointToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**解説**

最近点を取得

---

### closestPointToPointParameter

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**解説**

最近点のパラメータ

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
| `line` | `&nbsp;` |  |

**解説**

等価判定

---
