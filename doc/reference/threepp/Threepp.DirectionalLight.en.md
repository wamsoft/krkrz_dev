# Threepp.DirectionalLight

Directional light (like sunlight)

A light whose rays are emitted in parallel from infinitely far away. It can cast shadows.

To cast shadows, set castShadow=true, call renderer.setShadowMapEnabled(true),
and set receiveShadow=true on the receiving objects.
Directional light shadows are rendered with an orthographic camera, so specify the area covering the scene with setShadowOrthoBounds.

## Members

### Constructors

- [DirectionalLight](#directionallight)

### Properties

- [type](#type)

### Methods

- [setShadowMapSize](#setshadowmapsize)
- [setShadowBias](#setshadowbias)
- [setShadowNormalBias](#setshadownormalbias)
- [setShadowRadius](#setshadowradius)
- [setShadowNearFar](#setshadownearfar)
- [setShadowOrthoBounds](#setshadoworthobounds)
- [dispose](#dispose)

---

### DirectionalLight

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `0xffffff` | Light color (0xRRGGBB). |
| `intensity` | `void` | Light intensity. |

**Description**

Constructor

---

### type

Property \ Access: `r/w`

**Description**

"DirectionalLight" (read-only)

---

### setShadowMapSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**Description**

Shadow map resolution (default 2048x2048)

---

### setShadowBias

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**Description**

Shadow bias to reduce shadow acne (e.g. -0.0005)

---

### setShadowNormalBias

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**Description**

Bias along the normal

---

### setShadowRadius

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |

**Description**

Soft shadow radius (PCF)

---

### setShadowNearFar

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**Description**

near/far of the shadow camera

---

### setShadowOrthoBounds

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |

**Description**

Shadow area of the directional light (orthographic)

---

### dispose

Method

**Description**

Releases resources

---
