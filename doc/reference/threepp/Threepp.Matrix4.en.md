# Threepp.Matrix4

4x4 matrix class

Represents a transformation matrix.

## Members

### Constructors

- [Matrix4](#matrix4)

### Methods

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [copyPosition](#copyposition)
- [extractBasis](#extractbasis)
- [makeBasis](#makebasis)
- [extractRotation](#extractrotation)
- [makeRotationFromEuler](#makerotationfromeuler)
- [makeRotationFromQuaternion](#makerotationfromquaternion)
- [lookAt](#lookat)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [transpose](#transpose)
- [setPosition](#setposition)
- [invert](#invert)
- [scale](#scale)
- [getMaxScaleOnAxis](#getmaxscaleonaxis)
- [makeTranslation](#maketranslation)
- [makeRotationX](#makerotationx)
- [makeRotationY](#makerotationy)
- [makeRotationZ](#makerotationz)
- [makeRotationAxis](#makerotationaxis)
- [makeScale](#makescale)
- [makeShear](#makeshear)
- [compose](#compose)
- [decompose](#decompose)
- [makePerspective](#makeperspective)
- [makeOrthographic](#makeorthographic)
- [equals](#equals)

---

### Matrix4

Constructor

**Description**

Constructor

Creates an identity matrix.

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n14` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n24` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |
| `n34` | `&nbsp;` |  |
| `n41` | `&nbsp;` |  |
| `n42` | `&nbsp;` |  |
| `n43` | `&nbsp;` |  |
| `n44` | `&nbsp;` |  |

**Description**

Sets the elements

---

### identity

Method

**Description**

Resets to the identity matrix

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Copies another matrix

---

### copyPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Copies only the translation component

---

### extractBasis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**Description**

Extracts the basis vectors

---

### makeBasis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**Description**

Creates a matrix from basis vectors

---

### extractRotation

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Extracts the rotation component

---

### makeRotationFromEuler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**Description**

Creates a rotation matrix from Euler angles

---

### makeRotationFromQuaternion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Creates a rotation matrix from a quaternion

---

### lookAt

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `eye` | `&nbsp;` |  |
| `target` | `&nbsp;` |  |
| `up` | `&nbsp;` |  |

**Description**

Creates a look-at matrix

---

### multiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Multiplies by a matrix

---

### premultiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Premultiplies by a matrix

---

### multiplyMatrices

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Product of two matrices

---

### multiplyScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Multiplies by a scalar

---

### determinant

Method

**Description**

Determinant

---

### transpose

Method

**Description**

Transposes the matrix

---

### setPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Sets the position

---

### invert

Method

**Description**

Inverts the matrix

---

### scale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Scales the matrix

---

### getMaxScaleOnAxis

Method

**Description**

Maximum scale along any axis

---

### makeTranslation

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Creates a translation matrix

---

### makeRotationX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**Description**

Creates a rotation matrix around the X axis

---

### makeRotationY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**Description**

Creates a rotation matrix around the Y axis

---

### makeRotationZ

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**Description**

Creates a rotation matrix around the Z axis

---

### makeRotationAxis

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**Description**

Creates a rotation matrix around an arbitrary axis

---

### makeScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Creates a scale matrix

---

### makeShear

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `xy` | `&nbsp;` |  |
| `xz` | `&nbsp;` |  |
| `yx` | `&nbsp;` |  |
| `yz` | `&nbsp;` |  |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**Description**

Creates a shear matrix

---

### compose

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**Description**

Composes the matrix from position, rotation and scale

---

### decompose

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**Description**

Decomposes the matrix into position, rotation and scale

---

### makePerspective

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**Description**

Creates a perspective projection matrix

---

### makeOrthographic

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**Description**

Creates an orthographic projection matrix

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Equality test

---
