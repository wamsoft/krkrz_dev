# PreRenderedFontImage

Font image (note: this class does not actually exist!)

Defines the extra information attached to the layer object returned from the callback.
Assign these values to an ordinary layer object and return it.
Only the alpha of the region (0,0)-(blackbox_x-1,blackbox_y-1) of the layer image is used, resampled to 65 levels (0 to 64).

The callback may return the same instance over and over.

Extends: [Layer](Layer.md)

## Members

### Properties

- [blackbox_x](#blackbox_x)
- [blackbox_y](#blackbox_y)
- [origin_x](#origin_x)
- [origin_y](#origin_y)
- [inc_x](#inc_x)
- [inc_y](#inc_y)
- [inc](#inc)

---

### blackbox_x

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmBlackBoxX

---

### blackbox_y

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmBlackBoxY

---

### origin_x

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmptGlyphOrigin.x

---

### origin_y

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmptGlyphOrigin.y

---

### inc_x

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmCellIncX

---

### inc_y

Property \ Access: `r/w`

**Description**

GLYPHMETRICS.gmCellIncY

---

### inc

Property \ Access: `r/w`

**Description**

SIZE.cx of the size returned by GetTextExtentPoint32

---
