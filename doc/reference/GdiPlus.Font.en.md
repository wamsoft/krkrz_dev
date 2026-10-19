# GdiPlus.Font

This class is extended by several plugins.

## Plugin extension: layerExDraw

Font information

### Members

#### Constructors

- [Font](#font)

#### Properties

- [familyName](#familyname)
- [emSize](#emsize)
- [style](#style)
- [forceSelfPathDraw](#forceselfpathdraw)
- [ascent](#ascent)
- [descent](#descent)
- [lineSpacing](#linespacing)
- [ascentLeading](#ascentleading)
- [descentLeading](#descentleading)

---

### Font

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `familyName` | `&nbsp;` | Font family |
| `emSize` | `&nbsp;` | Font size |
| `style` | `&nbsp;` | Font style |

**Description**

Constructor

---

### familyName

Property \ Access: `r/w`

**Description**

Font family

---

### emSize

Property \ Access: `r/w`

**Description**

Font size

---

### style

Property \ Access: `r/w`

**Description**

Font style

---

### forceSelfPathDraw

Property \ Access: `r/w`

**Description**

Sets whether to draw text by obtaining glyph paths itself instead of using GDI+'s text rendering.

---

### ascent

Property \ Access: `r`

**Description**

Ascent (read-only)

---

### descent

Property \ Access: `r`

**Description**

Descent (read-only)

---

### lineSpacing

Property \ Access: `r`

**Description**

Line spacing (read-only).

---

### ascentLeading

Property \ Access: `r`

**Description**

Internal leading on the ascent side (read-only)

---

### descentLeading

Property \ Access: `r`

**Description**

Internal leading on the descent side (read-only)

---

## Plugin extension: layerExVector

Font information

Holds settings for drawing text with a font registered by loadFont().

### Members

#### Constructors

- [Font](#font)

#### Properties

- [fontFamily](#fontfamily)
- [fontSize](#fontsize)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [lineSpacing](#linespacing)

---

### Font

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fontFamily` | `&nbsp;` | Font family name (the name registered with loadFont()) |
| `fontSize` | `&nbsp;` | Font size |

**Description**

Constructor

---

### fontFamily

Property \ Access: `r/w`

**Description**

Font family name (the name registered with loadFont())

---

### fontSize

Property \ Access: `r/w`

**Description**

Font size

---

### italic

Property \ Access: `r/w`

**Description**

Italic slant (0 = none, 0.18 = standard)

---

### letterSpacing

Property \ Access: `r/w`

**Description**

Letter spacing scale (1.0 = standard; larger values are wider)

---

### lineSpacing

Property \ Access: `r/w`

**Description**

Line spacing scale (1.0 = standard; larger values are wider)

---
