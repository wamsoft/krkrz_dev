# GdiPlus.Image

This class is extended by several plugins.

## Plugin extension: layerExDraw

Class that handles image information

Note: the area of vector image data may extend into negative coordinates.

### Members

#### Constructors

- [Image](#image)

#### Methods

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)
- [GetHorizontalResolution](#gethorizontalresolution)
- [GetVerticalResolution](#getverticalresolution)
- [GetWidth](#getwidth)
- [GetHeight](#getheight)
- [GetFlags](#getflags)
- [GetLastStatus](#getlaststatus)
- [GetPixelFormat](#getpixelformat)
- [GetType](#gettype)
- [RotateFlip](#rotateflip)

---

### Image

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `void` | File name. If specified, the image is loaded automatically. |

**Description**

Constructor

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Image file name |

**Description**

Loads an image

---

### Clone

Method

**Return value**

A copy of this object (Image)

---

### GetBounds

Method

**Return value**

Bounds (RectF), in pixels

**Description**

Gets the bounds

---

### GetHorizontalResolution

Method

**Return value**

Horizontal resolution (dpi)

---

### GetVerticalResolution

Method

**Return value**

Vertical resolution (dpi)

---

### GetWidth

Method

**Return value**

Width (pixels, integer)

---

### GetHeight

Method

**Return value**

Height (pixels, integer)

---

### GetFlags

Method

---

### GetLastStatus

Method

---

### GetPixelFormat

Method

---

### GetType

Method

---

### RotateFlip

Method

---

## Plugin extension: layerExVector

Class that handles image information.
Note: the area of vector image data may extend into negative coordinates.

### Members

#### Constructors

- [Image](#image)

#### Properties

- [width](#width)
- [height](#height)
- [isLoaded](#isloaded)

#### Methods

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)

---

### Image

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `void` | File name. If specified, the image is loaded automatically. |

**Description**

Constructor

---

### width

Property \ Access: `r`

**Description**

Width (read-only)

---

### height

Property \ Access: `r`

**Description**

Height (read-only)

---

### isLoaded

Property \ Access: `r`

**Description**

Whether an image is loaded (read-only)

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` | Image file name |

**Description**

Loads an image

---

### Clone

Method

**Return value**

A copy of this object (Image)

---

### GetBounds

Method

**Return value**

Bounds (RectF), in pixels

**Description**

Gets the bounds

---
