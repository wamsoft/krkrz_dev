# Threepp.Ray

Ray class

## Members

### Constructors

- [Ray](#ray)

### Methods

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [at](#at)
- [lookAt](#lookat)
- [recast](#recast)
- [closestPointToPoint](#closestpointtopoint)
- [distanceToPoint](#distancetopoint)
- [distanceSqToPoint](#distancesqtopoint)
- [distanceSqToSegment](#distancesqtosegment)
- [intersectSphere](#intersectsphere)
- [intersectsSphere](#intersectssphere)
- [intersectBox](#intersectbox)
- [intersectsBox](#intersectsbox)
- [intersectPlane](#intersectplane)
- [intersectsPlane](#intersectsplane)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Ray

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `origin` | `&nbsp;` | Origin (Vector3). |
| `direction` | `&nbsp;` | Direction (Vector3). |

**Description**

Constructor

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

**Description**

Sets the values

---

### clone

Method

**Description**

Clones the ray

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ray` | `&nbsp;` |  |

**Description**

Copies another ray

---

### at

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Gets a point on the ray

---

### lookAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Sets the direction

---

### recast

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Moves the origin along the ray

---

### closestPointToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Gets the closest point

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

### distanceSqToPoint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**Description**

Squared distance to a point

---

### distanceSqToSegment

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v0` | `&nbsp;` |  |
| `v1` | `&nbsp;` |  |

**Description**

Squared distance to a line segment

---

### intersectSphere

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**Description**

Intersection point with a sphere

---

### intersectsSphere

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**Description**

Whether the ray intersects a sphere

---

### intersectBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Intersection point with a box

---

### intersectsBox

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**Description**

Whether the ray intersects a box

---

### intersectPlane

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**Description**

Intersection point with a plane

---

### intersectsPlane

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**Description**

Whether the ray intersects a plane

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

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `ray` | `&nbsp;` |  |

**Description**

Equality test

---
