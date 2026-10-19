# Threepp.LineCurve

2D line curve

A curve representing a straight line between two points.

## Members

### Constructors

- [LineCurve](#linecurve)

### Properties

- [v1](#v1)
- [v2](#v2)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)
- [getPointAt](#getpointat)
- [getTangent](#gettangent)

---

### LineCurve

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v1` | `&nbsp;` | Start point (Vector2 or [x, y]). |
| `v2` | `&nbsp;` | End point (Vector2 or [x, y]). |

**Description**

Constructor

---

### v1

Property \ Access: `r/w`

**Description**

Start point (read-only)

---

### v2

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

### getPointAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `u` | `&nbsp;` |  |

**Description**

Gets the point at arc-length parameter u

---

### getTangent

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Gets the tangent vector

---
