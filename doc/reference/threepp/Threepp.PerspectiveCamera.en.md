# Threepp.PerspectiveCamera

Perspective camera

A camera that uses perspective projection, mimicking the way the human eye sees.

## Members

### Constructors

- [PerspectiveCamera](#perspectivecamera)

### Properties

- [type](#type)
- [fov](#fov)
- [aspect](#aspect)
- [focus](#focus)
- [filmGauge](#filmgauge)
- [filmOffset](#filmoffset)

### Methods

- [setFocalLength](#setfocallength)
- [getFocalLength](#getfocallength)
- [getEffectiveFOV](#geteffectivefov)
- [getFilmWidth](#getfilmwidth)
- [getFilmHeight](#getfilmheight)
- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)
- [applyScreenAffine](#applyscreenaffine)

---

### PerspectiveCamera

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fov` | `60` | Field of view (degrees). |
| `aspect` | `1` | Aspect ratio. |
| `near` | `0.1` | Near clipping plane. |
| `far` | `2000` | Far clipping plane. |

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

"PerspectiveCamera" (read-only)

---

### fov

Property \ Access: `r/w`

**Description**

Field of view (degrees)

---

### aspect

Property \ Access: `r/w`

**Description**

Aspect ratio

---

### focus

Property \ Access: `r/w`

**Description**

Focus distance

---

### filmGauge

Property \ Access: `r/w`

**Description**

Film gauge (mm)

---

### filmOffset

Property \ Access: `r/w`

**Description**

Film offset

---

### setFocalLength

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `focalLength` | `&nbsp;` |  |

**Description**

Sets the focal length

---

### getFocalLength

Method

**Description**

Gets the focal length

---

### getEffectiveFOV

Method

**Description**

Gets the effective field of view

---

### getFilmWidth

Method

**Description**

Gets the film width

---

### getFilmHeight

Method

**Description**

Gets the film height

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

### applyScreenAffine

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |
| `d` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |

**Description**

Post-multiplies the projection matrix by a 2D on-screen affine transform (call after updateProjectionMatrix; common to all cameras).

In NDC: x' = a*x + b*y + tx, y' = c*x + d*y + ty. Because the camera's entire view can be mapped to any parallelogram on the screen, 2D-side scaling, rotation and positioning are applied to the rendering itself rather than as scaling after drawing.

---
