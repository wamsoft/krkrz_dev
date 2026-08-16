# Threepp.Shape

Shape（穴付き2D形状）

Pathを継承し、穴を追加できる2D形状クラス
ExtrudeGeometryやShapeGeometryで使用

## メンバー一覧

### コンストラクタ

- [Shape](#shape)

### プロパティ

- [autoClose](#autoclose)
- [currentPoint](#currentpoint)

### メソッド

- [getLength](#getlength)
- [getPoint](#getpoint)
- [getPointAt](#getpointat)
- [moveTo](#moveto)
- [lineTo](#lineto)
- [quadraticCurveTo](#quadraticcurveto)
- [bezierCurveTo](#beziercurveto)
- [arc](#arc)
- [absarc](#absarc)
- [absellipse](#absellipse)
- [splineThru](#splinethru)
- [closePath](#closepath)
- [addHole](#addhole)
- [getHole](#gethole)
- [getHoleCount](#getholecount)
- [uuid](#uuid)

---

### Shape

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 初期点の配列（省略可） |

**解説**

コンストラクタ

---

### autoClose

プロパティ \ アクセス: `r/w`

**解説**

パスを自動的に閉じるか

---

### currentPoint

プロパティ \ アクセス: `r/w`

**解説**

現在のペン位置（読み取り専用）

---

### getLength

メソッド

**解説**

パスの全長を取得

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

### getPointAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `u` | `&nbsp;` |  |

**解説**

等間隔パラメータ u の点を取得

---

### moveTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

Pathと同じ描画メソッド

---

### lineTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

直線を描画

---

### quadraticCurveTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `cpX` | `&nbsp;` |  |
| `cpY` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

二次ベジェ曲線を描画

---

### bezierCurveTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `cp1x` | `&nbsp;` |  |
| `cp1y` | `&nbsp;` |  |
| `cp2x` | `&nbsp;` |  |
| `cp2y` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

三次ベジェ曲線を描画

---

### arc

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**解説**

相対位置から円弧を描画

---

### absarc

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**解説**

絶対位置で円弧を描画

---

### absellipse

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `xRadius` | `&nbsp;` |  |
| `yRadius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |
| `rotation` | `&nbsp;` |  |

**解説**

楕円を描画

---

### splineThru

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` |  |

**解説**

点の配列を通過するスプライン

---

### closePath

メソッド

**解説**

パスを閉じる

---

### addHole

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `hole` | `&nbsp;` |  |

**解説**

穴の管理

---

### getHole

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**解説**

穴を取得

---

### getHoleCount

メソッド

**解説**

穴の数を取得

---

### uuid

メソッド

**解説**

形状のUUIDを取得

---
