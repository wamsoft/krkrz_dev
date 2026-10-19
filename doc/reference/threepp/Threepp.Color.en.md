# Threepp.Color

Color class

Represents an RGB color. It can also be converted from an array [r, g, b], a dictionary %[r:, g:, b:] or an integer (0xRRGGBB).

## Members

### Constructors

- [Color](#color)

### Properties

- [r](#r)
- [g](#g)
- [b](#b)

### Methods

- [setScalar](#setscalar)
- [setRGB](#setrgb)
- [setHSL](#sethsl)
- [setHex](#sethex)
- [copy](#copy)
- [add](#add)
- [addColors](#addcolors)
- [addScalar](#addscalar)
- [sub](#sub)
- [multiply](#multiply)
- [multiplyScalar](#multiplyscalar)
- [lerp](#lerp)
- [lerpColors](#lerpcolors)
- [lerpHSL](#lerphsl)
- [randomize](#randomize)
- [getHex](#gethex)
- [getHexString](#gethexstring)
- [getStyle](#getstyle)
- [equals](#equals)

---

### Color

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `1` | Red component (0.0-1.0), or a hex value (0xRRGGBB). |
| `g` | `1` | Green component (0.0-1.0). |
| `b` | `1` | Blue component (0.0-1.0). |

**Description**

Constructor

---

### r

Property \ Access: `r/w`

**Description**

Red component (0.0-1.0)

---

### g

Property \ Access: `r/w`

**Description**

Green component (0.0-1.0)

---

### b

Property \ Access: `r/w`

**Description**

Blue component (0.0-1.0)

---

### setScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Sets all components to the same value

---

### setRGB

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Sets the RGB values

---

### setHSL

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `h` | `&nbsp;` |  |
| `s` | `&nbsp;` |  |
| `l` | `&nbsp;` |  |

**Description**

Sets the color from HSL values

---

### setHex

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `hex` | `&nbsp;` |  |

**Description**

Sets the color from a hexadecimal value

---

### copy

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**Description**

Copies another color

---

### add

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**Description**

Adds a color

---

### addColors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `c1` | `&nbsp;` |  |
| `c2` | `&nbsp;` |  |

**Description**

Sets this color to the sum of two colors

---

### addScalar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Adds a scalar

---

### sub

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**Description**

Subtracts a color

---

### multiply

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**Description**

Multiplies by a color

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

### lerp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**Description**

Linear interpolation

---

### lerpColors

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `c1` | `&nbsp;` |  |
| `c2` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**Description**

Linear interpolation between two colors

---

### lerpHSL

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**Description**

Linear interpolation in HSL space

---

### randomize

Method

**Description**

Generates a random color

---

### getHex

Method

**Description**

Gets the hexadecimal value

---

### getHexString

Method

**Description**

Gets the hexadecimal string

---

### getStyle

Method

**Description**

Gets a CSS-style string

---

### equals

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**Description**

Equality test

---
