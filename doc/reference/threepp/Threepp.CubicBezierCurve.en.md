# Threepp.CubicBezierCurve

2D cubic Bezier curve

A cubic Bezier curve with two control points.

## Members

### Constructors

- [CubicBezierCurve](#cubicbeziercurve)

### Properties

- [v0](#v0)
- [v1](#v1)
- [v2](#v2)
- [v3](#v3)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### CubicBezierCurve

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v0` | `&nbsp;` | Start point. |
| `v1` | `&nbsp;` | First control point. |
| `v2` | `&nbsp;` | Second control point. |
| `v3` | `&nbsp;` | End point. |

**Description**

Constructor

---

### v0

Property \ Access: `r/w`

**Description**

Start point (read-only)

---

### v1

Property \ Access: `r/w`

**Description**

First control point (read-only)

---

### v2

Property \ Access: `r/w`

**Description**

Second control point (read-only)

---

### v3

Property \ Access: `r/w`

**Description**

End point (read-only)

---

### getLength

Method

**Description**

Gets the length of the curve

---

### getPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Gets the point at parameter t (0-1)

---
