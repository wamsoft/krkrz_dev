# Threepp.EllipseCurve

楕円カーブ

楕円または円弧を表現するカーブです。

## メンバー一覧

### コンストラクタ

- [EllipseCurve](#ellipsecurve)

### プロパティ

- [aX](#ax)
- [aY](#ay)
- [xRadius](#xradius)
- [yRadius](#yradius)
- [aStartAngle](#astartangle)
- [aEndAngle](#aendangle)
- [aClockwise](#aclockwise)
- [aRotation](#arotation)

### メソッド

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### EllipseCurve

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `aX` | `0` | 中心X座標 |
| `aY` | `0` | 中心Y座標 |
| `xRadius` | `1` | X方向の半径 |
| `yRadius` | `1` | Y方向の半径 |
| `aStartAngle` | `0` | 開始角度 (ラジアン) |
| `aEndAngle` | `Math.PI*2` | 終了角度 (ラジアン) |
| `aClockwise` | `false` | 時計回りかどうか |
| `aRotation` | `0` | 楕円の回転角度 (ラジアン) |

**解説**

コンストラクタ

---

### aX

プロパティ \ アクセス: `r/w`

**解説**

中心X座標

---

### aY

プロパティ \ アクセス: `r/w`

**解説**

中心Y座標

---

### xRadius

プロパティ \ アクセス: `r/w`

**解説**

X方向の半径

---

### yRadius

プロパティ \ アクセス: `r/w`

**解説**

Y方向の半径

---

### aStartAngle

プロパティ \ アクセス: `r/w`

**解説**

開始角度

---

### aEndAngle

プロパティ \ アクセス: `r/w`

**解説**

終了角度

---

### aClockwise

プロパティ \ アクセス: `r/w`

**解説**

時計回りフラグ

---

### aRotation

プロパティ \ アクセス: `r/w`

**解説**

回転角度

---

### getLength

メソッド

**解説**

曲線の長さを取得

---

### getPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

パラメータ t (0-1) の点を取得

---
