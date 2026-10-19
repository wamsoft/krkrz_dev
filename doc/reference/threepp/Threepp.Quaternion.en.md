# Threepp.Quaternion

Quaternion class

A quaternion representing a rotation. It does not suffer from gimbal lock.

## Members

### Constructors

- [Quaternion](#quaternion)

### Properties

- [x](#x)
- [y](#y)
- [z](#z)
- [w](#w)

### Methods

- [set](#set)
- [copy](#copy)
- [setFromEuler](#setfromeuler)
- [setFromAxisAngle](#setfromaxisangle)
- [setFromRotationMatrix](#setfromrotationmatrix)
- [setFromUnitVectors](#setfromunitvectors)
- [angleTo](#angleto)
- [rotateTowards](#rotatetowards)
- [identity](#identity)
- [invert](#invert)
- [conjugate](#conjugate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [normalize](#normalize)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyQuaternions](#multiplyquaternions)
- [slerp](#slerp)
- [slerpQuaternions](#slerpquaternions)
- [equals](#equals)

---

### Quaternion

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `0` | X component. |
| `y` | `0` | Y component. |
| `z` | `0` | Z component. |
| `w` | `1` | W component. |

**Description**

Constructor

---

### x

Property \ Access: `r/w`

**Description**

X component (read-only)

---

### y

Property \ Access: `r/w`

**Description**

Y component (read-only)

---

### z

Property \ Access: `r/w`

**Description**

Z component (read-only)

---

### w

Property \ Access: `r/w`

**Description**

W component (read-only)

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**Description**

Sets the values

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Copies another quaternion

---

### setFromEuler

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**Description**

Sets the quaternion from Euler angles

---

### setFromAxisAngle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**Description**

Sets the quaternion from an axis and an angle

---

### setFromRotationMatrix

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Sets the quaternion from a rotation matrix

---

### setFromUnitVectors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vFrom` | `&nbsp;` |  |
| `vTo` | `&nbsp;` |  |

**Description**

Sets the quaternion from two unit vectors

---

### angleTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Angle to another quaternion

---

### rotateTowards

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `step` | `&nbsp;` |  |

**Description**

Rotates toward another quaternion

---

### identity

Method

**Description**

Resets to the identity quaternion

---

### invert

Method

**Description**

Inverts the quaternion

---

### conjugate

Method

**Description**

Conjugate

---

### dot

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Dot product

---

### lengthSq

Method

**Description**

Squared length

---

### length

Method

**Description**

Length

---

### normalize

Method

**Description**

Normalizes the quaternion

---

### multiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Multiplies by a quaternion

---

### premultiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Premultiplies by a quaternion

---

### multiplyQuaternions

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Product of two quaternions

---

### slerp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**Description**

Spherical linear interpolation

---

### slerpQuaternions

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `qa` | `&nbsp;` |  |
| `qb` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**Description**

Spherical linear interpolation between two quaternions

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Equality test

---
