# GdiPlus.Matrix

This class is extended by several plugins.

## Plugin extension: layerExDraw

Class that handles matrix information

### Members

#### Constructors

- [Matrix](#matrix)
- [Matrix](#matrix)
- [Matrix](#matrix)

#### Methods

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

Constructor

**Description**

Constructor

Creates an identity matrix.

---

### Matrix

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `rectF` | `&nbsp;` | Rectangle (RectF class): the rotation part of the matrix |
| `pointF` | `&nbsp;` | Point (PointF class): the translation part of the matrix |

**Description**

Constructor

---

### Matrix

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m11` | `&nbsp;` | Row 1, column 1 |
| `m12` | `&nbsp;` | Row 1, column 2 |
| `m21` | `&nbsp;` | Row 2, column 1 |
| `m22` | `&nbsp;` | Row 2, column 2 |
| `dx` | `&nbsp;` | Row 3, column 1 |
| `dy` | `&nbsp;` | Row 3, column 2 |

**Description**

Constructor

---

### OffsetX

Method

---

### OffsetY

Method

---

### Equals

Method

---

### SetElemetns

Method

---

### GetLastStatus

Method

---

### Invert

Method

---

### IsIdentity

Method

---

### IsInvertible

Method

---

### Multiply

Method

---

### Reset

Method

---

### Rotate

Method

---

### RotateAt

Method

---

### Scale

Method

---

### Share

Method

---

### Translate

Method

---

## Plugin extension: layerExVector

Class that handles matrix information

### Members

#### Constructors

- [Matrix](#matrix)
- [Matrix](#matrix)

#### Methods

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

Constructor

**Description**

Constructor

Creates an identity matrix.

---

### Matrix

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m11` | `&nbsp;` | Row 1, column 1 |
| `m12` | `&nbsp;` | Row 1, column 2 |
| `m21` | `&nbsp;` | Row 2, column 1 |
| `m22` | `&nbsp;` | Row 2, column 2 |
| `dx` | `&nbsp;` | Row 3, column 1 |
| `dy` | `&nbsp;` | Row 3, column 2 |

**Description**

Constructor

---

### OffsetX

Method

---

### OffsetY

Method

---

### Equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

---

### SetElements

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### Invert

Method

---

### IsIdentity

Method

---

### IsInvertible

Method

---

### Multiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Reset

Method

---

### Rotate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Scale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Translate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---
