# Threepp.OrthographicCamera

Orthographic camera

A camera suited to 2D scenes and isometric views.

## Members

### Constructors

- [OrthographicCamera](#orthographiccamera)

### Properties

- [type](#type)
- [left](#left)
- [right](#right)
- [top](#top)
- [bottom](#bottom)

### Methods

- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)

---

### OrthographicCamera

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `-1` | Left plane. |
| `right` | `1` | Right plane. |
| `top` | `1` | Top plane. |
| `bottom` | `-1` | Bottom plane. |
| `near` | `0.1` | Near clipping plane. |
| `far` | `2000` | Far clipping plane. |

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

"OrthographicCamera" (read-only)

---

### left

Property \ Access: `r/w`

**Description**

Left plane

---

### right

Property \ Access: `r/w`

**Description**

Right plane

---

### top

Property \ Access: `r/w`

**Description**

Top plane

---

### bottom

Property \ Access: `r/w`

**Description**

Bottom plane

---

### setViewOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fullWidth` | `&nbsp;` |  |
| `fullHeight` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**Description**

Sets the view offset

---

### clearViewOffset

Method

**Description**

Clears the view offset

---

### updateProjectionMatrix

Method

**Description**

Updates the projection matrix

---
