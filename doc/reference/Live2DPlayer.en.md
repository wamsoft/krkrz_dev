# Live2DPlayer

Player for drawing

Has the same interface as Live2DModel plus methods for drawing.
Requires a Live2DDevice to create.

## Members

### Constructors

- [Live2DPlayer](#live2dplayer)

### Methods

- [clear](#clear)
- [load](#load)
- [loadModel](#loadmodel)
- [clone](#clone)
- [setScale](#setscale)
- [getScale](#getscale)
- [setMatrix](#setmatrix)
- [render](#render)
- [setVoiceValue](#setvoicevalue)
- [setVoiceWeight](#setvoiceweight)
- [setVoiceMode](#setvoicemode)
- [setBlinkingInterval](#setblinkinginterval)
- [setBlinkingSettings](#setblinkingsettings)
- [setBlinkingMode](#setblinkingmode)
- [setMosaicParam](#setmosaicparam)

---

### Live2DPlayer

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `device` | `&nbsp;` | Live2DDevice instance |

**Description**

Constructor

---

### clear

Method

**Description**

Clears the contents

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### loadModel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `model` | `&nbsp;` | Live2DModel instance |

**Description**

Creates the player from a Live2DModel instance

Inherits the state of the loaded model.

---

### clone

Method

**Description**

Duplicates the player

---

### setScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**Description**

Sets the display scale

---

### getScale

Method

---

### setMatrix

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**Description**

Sets the display matrix

---

### render

Method

**Description**

Renders the model. Drawing happens when called on an OpenGL context

---

### setVoiceValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `voice` | `&nbsp;` |  |

---

### setVoiceWeight

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `weight` | `&nbsp;` |  |

---

### setVoiceMode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setBlinkingInterval

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `interal` | `&nbsp;` |  |

---

### setBlinkingSettings

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `closing` | `&nbsp;` |  |
| `closed` | `&nbsp;` |  |
| `opening` | `&nbsp;` |  |

---

### setBlinkingMode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setMosaicParam

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

---
