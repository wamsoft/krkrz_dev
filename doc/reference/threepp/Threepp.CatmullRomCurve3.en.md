# Threepp.CatmullRomCurve3

Catmull-Rom spline curve

Generates a smooth curve that passes through the control points.

## Members

### Constructors

- [CatmullRomCurve3](#catmullromcurve3)

### Properties

- [closed](#closed)
- [tension](#tension)

### Methods

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### CatmullRomCurve3

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `points` | `&nbsp;` | Array of control points (an array of Vector3 or of [x,y,z]). |
| `closed` | `false` | Whether the curve is closed. |
| `curveType` | `0` | Curve type (centripetal, chordal, catmullrom). |
| `tension` | `0.5` | Tension (for the catmullrom type). |

**Description**

Constructor

---

### closed

Property \ Access: `r/w`

**Description**

Whether the curve is closed

---

### tension

Property \ Access: `r/w`

**Description**

Tension

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
