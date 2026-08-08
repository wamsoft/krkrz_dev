# Threepp.Spherical

球面座標クラス

## メンバー一覧

### コンストラクタ

- [Spherical](#spherical)

### プロパティ

- [radius](#radius)
- [phi](#phi)
- [theta](#theta)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeSafe](#makesafe)
- [setFromVector3](#setfromvector3)
- [setFromCartesianCoords](#setfromcartesiancoords)

---

### Spherical

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `radius` | `1` | 半径 |
| `phi` | `0` | 極角 (ラジアン) |
| `theta` | `0` | 方位角 (ラジアン) |

**解説**

コンストラクタ

---

### radius

プロパティ \ アクセス: `r/w`

**解説**

半径

---

### phi

プロパティ \ アクセス: `r/w`

**解説**

極角

---

### theta

プロパティ \ アクセス: `r/w`

**解説**

方位角

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |
| `phi` | `&nbsp;` |  |
| `theta` | `&nbsp;` |  |

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
| `s` | `&nbsp;` |  |

**解説**

コピー

---

### makeSafe

メソッド

**解説**

安全な値に補正

---

### setFromVector3

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

Vector3から設定

---

### setFromCartesianCoords

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

直交座標から設定

---
