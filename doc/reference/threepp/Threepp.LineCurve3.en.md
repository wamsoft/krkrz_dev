# Threepp.LineCurve3

3D line curve

A curve representing a straight line between two points in 3D space.

## Members

### Constructors

- [LineCurve3](#linecurve3)

### Properties

- [v1](#v1)
- [v2](#v2)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)
- [getPointAt](#getpointat)
- [getTangent](#gettangent)

---

### LineCurve3

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v1` | `&nbsp;` | Start point (Vector3 or [x, y, z]). |
| `v2` | `&nbsp;` | End point (Vector3 or [x, y, z]). |

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
