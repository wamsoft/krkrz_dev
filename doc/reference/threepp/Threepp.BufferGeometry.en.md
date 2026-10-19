# Threepp.BufferGeometry

Buffer geometry base class

Base class for geometries that store vertex data.

## Members

### Constructors

- [BufferGeometry](#buffergeometry)

### Properties

- [type](#type)
- [id](#id)
- [name](#name)

### Methods

- [hasIndex](#hasindex)
- [hasAttribute](#hasattribute)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [computeVertexNormals](#computevertexnormals)
- [normalizeNormals](#normalizenormals)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [translate](#translate)
- [scale](#scale)
- [center](#center)
- [dispose](#dispose)

---

### BufferGeometry

Constructor

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

Geometry type (read-only)

---

### id

Property \ Access: `r/w`

**Description**

ID (read-only)

---

### name

Property \ Access: `r/w`

**Description**

Name

---

### hasIndex

Method

**Description**

Whether the geometry has an index

---

### hasAttribute

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

Whether the geometry has the given attribute

---

### computeBoundingBox

Method

**Description**

Computes the bounding box

---

### computeBoundingSphere

Method

**Description**

Computes the bounding sphere

---

### computeVertexNormals

Method

**Description**

Computes vertex normals

---

### normalizeNormals

Method

**Description**

Normalizes the normals

---

### rotateX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the X axis

---

### rotateY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the Y axis

---

### rotateZ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**Description**

Rotates around the Z axis

---

### translate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Translates the geometry

---

### scale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Scales the geometry

---

### center

Method

**Description**

Centers the geometry

---

### dispose

Method

**Description**

Releases resources

---
