# Threepp.Spherical

Spherical coordinates class

## Members

### Constructors

- [Spherical](#spherical)

### Properties

- [radius](#radius)
- [phi](#phi)
- [theta](#theta)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeSafe](#makesafe)
- [setFromVector3](#setfromvector3)
- [setFromCartesianCoords](#setfromcartesiancoords)

---

### Spherical

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `radius` | `1` | Radius. |
| `phi` | `0` | Polar angle (radians). |
| `theta` | `0` | Azimuthal angle (radians). |

**Description**

Constructor

---

### radius

Property \ Access: `r/w`

**Description**

Radius

---

### phi

Property \ Access: `r/w`

**Description**

Polar angle

---

### theta

Property \ Access: `r/w`

**Description**

Azimuthal angle

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |
| `phi` | `&nbsp;` |  |
| `theta` | `&nbsp;` |  |

**Description**

Sets the values

---

### clone

Method

**Description**

Clones the object

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Copies another object

---

### makeSafe

Method

**Description**

Clamps the values to a safe range

---

### setFromVector3

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Sets the values from a Vector3

---

### setFromCartesianCoords

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the values from Cartesian coordinates

---
