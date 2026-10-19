# Threepp.Plane

Plane class

## Members

### Constructors

- [Plane](#plane)

### Methods

- [set](#set)
- [setComponents](#setcomponents)
- [setFromNormalAndCoplanarPoint](#setfromnormalandcoplanarpoint)
- [clone](#clone)
- [copy](#copy)
- [normalize](#normalize)
- [negate](#negate)
- [distanceToPoint](#distancetopoint)
- [distanceToSphere](#distancetosphere)
- [coplanarPoint](#coplanarpoint)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Plane

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `normal` | `&nbsp;` | Normal (Vector3). |
| `constant` | `&nbsp;` | Constant. |

**Description**

Constructor

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `constant` | `&nbsp;` |  |

**Description**

Sets the values

---

### setComponents

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**Description**

Sets the plane from individual components

---

### setFromNormalAndCoplanarPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `point` | `&nbsp;` |  |

**Description**

Sets the plane from a normal and a point

---

### clone

Method

**Description**

Clones the plane

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**Description**

Copies another plane

---

### normalize

Method

**Description**

Normalizes the plane

---

### negate

Method

**Description**

Negates the plane

---

### distanceToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Distance to a point

---

### distanceToSphere

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**Description**

Distance to a sphere

---

### coplanarPoint

Method

**Description**

Gets a point on the plane

---

### applyMatrix4

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Applies a matrix

---

### translate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `offset` | `&nbsp;` |  |

**Description**

Translates the plane

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**Description**

Equality test

---
