# Threepp.InstancedMesh

Instanced mesh

Renders multiple instances that share the same geometry and material.

## Members

### Constructors

- [InstancedMesh](#instancedmesh)

### Properties

- [type](#type)
- [count](#count)

### Methods

- [getMatrixAt](#getmatrixat)
- [setMatrixAt](#setmatrixat)
- [getColorAt](#getcolorat)
- [setColorAt](#setcolorat)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [dispose](#dispose)

---

### InstancedMesh

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `geometry` | `&nbsp;` | Geometry (BufferGeometry). |
| `material` | `&nbsp;` | Material (Material). |
| `count` | `&nbsp;` | Number of instances. |

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

"InstancedMesh" (read-only)

---

### count

Property \ Access: `r/w`

**Description**

Number of instances

---

### getMatrixAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**Description**

Gets the transformation matrix of an instance

---

### setMatrixAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**Description**

Sets the transformation matrix of an instance

---

### getColorAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**Description**

Gets the color of an instance

---

### setColorAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**Description**

Sets the color of an instance

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

### dispose

Method

**Description**

Releases resources

---
