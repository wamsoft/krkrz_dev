# GdiPlus.Matrix

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

### メンバー一覧

#### コンストラクタ

- [Matrix](#matrix)
- [Matrix](#matrix)
- [Matrix](#matrix)

#### メソッド

- [OffsetX](#offsetx)
- [OffsetY](#offsety)
- [Equals](#equals)
- [SetElemetns](#setelemetns)
- [GetLastStatus](#getlaststatus)
- [Invert](#invert)
- [IsIdentity](#isidentity)
- [IsInvertible](#isinvertible)
- [Multiply](#multiply)
- [Reset](#reset)
- [Rotate](#rotate)
- [RotateAt](#rotateat)
- [Scale](#scale)
- [Share](#share)
- [Translate](#translate)

---

### Matrix

コンストラクタ

---

### Matrix

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rectF` | `&nbsp;` |  |
| `pointF` | `&nbsp;` |  |

---

### Matrix

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### OffsetX

メソッド

---

### OffsetY

メソッド

---

### Equals

メソッド

---

### SetElemetns

メソッド

---

### GetLastStatus

メソッド

---

### Invert

メソッド

---

### IsIdentity

メソッド

---

### IsInvertible

メソッド

---

### Multiply

メソッド

---

### Reset

メソッド

---

### Rotate

メソッド

---

### RotateAt

メソッド

---

### Scale

メソッド

---

### Share

メソッド

---

### Translate

メソッド

---

## プラグイン拡張: layerExVector

マトリックス情報を取り扱うクラス

### メンバー一覧

#### コンストラクタ

- [Matrix](#matrix)
- [Matrix](#matrix)

#### メソッド

- [OffsetX](#offsetx)
- [OffsetY](#offsety)
- [Equals](#equals)
- [SetElements](#setelements)
- [Invert](#invert)
- [IsIdentity](#isidentity)
- [IsInvertible](#isinvertible)
- [Multiply](#multiply)
- [Reset](#reset)
- [Rotate](#rotate)
- [Scale](#scale)
- [Translate](#translate)

---

### Matrix

コンストラクタ

**解説**

コンストラクタ

正規マトリックスを生成する

---

### Matrix

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m11` | `&nbsp;` | 第1行1列 |
| `m12` | `&nbsp;` | 第1行2列 |
| `m21` | `&nbsp;` | 第2行1列 |
| `m22` | `&nbsp;` | 第2行2列 |
| `dx` | `&nbsp;` | 第3行1列 |
| `dy` | `&nbsp;` | 第3行2列 |

**解説**

コンストラクタ

---

### OffsetX

メソッド

---

### OffsetY

メソッド

---

### Equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

---

### SetElements

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### Invert

メソッド

---

### IsIdentity

メソッド

---

### IsInvertible

メソッド

---

### Multiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Reset

メソッド

---

### Rotate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Scale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Translate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---
