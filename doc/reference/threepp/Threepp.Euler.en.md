# Threepp.Euler

Euler angles class

Euler angles that represent a rotation.

## Members

### Constructors

- [Euler](#euler)

### Properties

- [x](#x)
- [y](#y)
- [z](#z)

### Methods

- [getOrder](#getorder)
- [setOrder](#setorder)
- [set](#set)
- [copy](#copy)
- [setFromRotationMatrix](#setfromrotationmatrix)
- [setFromQuaternion](#setfromquaternion)
- [setFromVector3](#setfromvector3)
- [equals](#equals)

---

### Euler

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `0` | Rotation around the X axis (radians). |
| `y` | `0` | Rotation around the Y axis (radians). |
| `z` | `0` | Rotation around the Z axis (radians). |

**Description**

Constructor

---

### x

Property \ Access: `r/w`

**Description**

Rotation around the X axis (read-only)

---

### y

Property \ Access: `r/w`

**Description**

Rotation around the Y axis (read-only)

---

### z

Property \ Access: `r/w`

**Description**

Rotation around the Z axis (read-only)

---

### getOrder

Method

**Description**

Gets the rotation order

---

### setOrder

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `order` | `&nbsp;` |  |

**Description**

Sets the rotation order

---

### set

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the values

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**Description**

Copies another Euler

---

### setFromRotationMatrix

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**Description**

Sets the angles from a rotation matrix

---

### setFromQuaternion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**Description**

Sets the angles from a quaternion

---

### setFromVector3

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**Description**

Sets the angles from a Vector3

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**Description**

Equality test

---
