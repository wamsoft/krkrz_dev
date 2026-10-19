# Threepp.Matrix3

3x3 matrix class

## Members

### Constructors

- [Matrix3](#matrix3)

### Methods

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [setFromMatrix4](#setfrommatrix4)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [invert](#invert)
- [transpose](#transpose)
- [getNormalMatrix](#getnormalmatrix)
- [scale](#scale)
- [rotate](#rotate)
- [translate](#translate)
- [equals](#equals)

---

### Matrix3

Constructor

**Description**

Constructor

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |

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

### setFromMatrix4

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Sets the matrix from a Matrix4

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

### invert

Method

**Description**

Inverts the matrix

---

### transpose

Method

**Description**

Transposes the matrix

---

### getNormalMatrix

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Gets the normal matrix

---

### scale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

**Description**

Scales the matrix

---

### rotate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**Description**

Rotates the matrix

---

### translate

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |

**Description**

Translates the matrix

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
