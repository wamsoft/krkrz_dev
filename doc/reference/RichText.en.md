# RichText

Manual in pseudo-code

richtext - rich text rendering plugin for Kirikiri

Provides high-quality text rendering by combining typesetting with minikin (the Android text layout engine)
and glyph drawing with the Kirikiri Z engine's unified font engine (glyphware).
Because font data and glyph rasterization are shared with the engine,
the output matches Layer.drawText and Elements dialogs in appearance.

Features:
- Fallback across multiple fonts
- Multilingual support (including RTL)
- Emoji support
- Styling with HTML-like tags
- Decorations such as outlines and shadows
- Paragraph layout (automatic line wrapping)
- Progressive display (using ParagraphLayout / StyledLayout)

## Members

### Methods

- [registerFont](#registerfont)
- [registerVariableFont](#registervariablefont)
- [unregisterFont](#unregisterfont)
- [registerCollection](#registercollection)
- [unregisterCollection](#unregistercollection)
- [registerLocale](#registerlocale)

### Constants

- [HALIGN_LEFT](#halign_left)
- [HALIGN_CENTER](#halign_center)
- [HALIGN_RIGHT](#halign_right)
- [HALIGN_JUSTIFY](#halign_justify)
- [VALIGN_TOP](#valign_top)
- [VALIGN_MIDDLE](#valign_middle)
- [VALIGN_BOTTOM](#valign_bottom)
- [BREAK_GREEDY](#break_greedy)
- [BREAK_HIGH_QUALITY](#break_high_quality)
- [BREAK_BALANCED](#break_balanced)
- [BIDI_LTR](#bidi_ltr)
- [BIDI_RTL](#bidi_rtl)
- [BIDI_DEFAULT_LTR](#bidi_default_ltr)
- [BIDI_DEFAULT_RTL](#bidi_default_rtl)

---

### registerFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `index` | `0` |  |

---

### registerVariableFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |
| `italic` | `false` |  |
| `index` | `0` |  |

---

### unregisterFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### registerCollection

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |
| `fontNames` | `&nbsp;` |  |

---

### unregisterCollection

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |

---

### registerLocale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `locale` | `&nbsp;` |  |

---

### HALIGN_LEFT

Constant

Value: `0`

**Description**

Left-aligned

---

### HALIGN_CENTER

Constant

Value: `1`

**Description**

Centered

---

### HALIGN_RIGHT

Constant

Value: `2`

**Description**

Right-aligned

---

### HALIGN_JUSTIFY

Constant

Value: `3`

**Description**

Justified

---

### VALIGN_TOP

Constant

Value: `0`

**Description**

Top-aligned

---

### VALIGN_MIDDLE

Constant

Value: `1`

**Description**

Vertically centered

---

### VALIGN_BOTTOM

Constant

Value: `2`

**Description**

Bottom-aligned

---

### BREAK_GREEDY

Constant

Value: `0`

**Description**

Fast (decides immediately at each break opportunity)

---

### BREAK_HIGH_QUALITY

Constant

Value: `1`

**Description**

High quality (Knuth-Plass algorithm)

---

### BREAK_BALANCED

Constant

Value: `2`

**Description**

Balanced (evens out line lengths)

---

### BIDI_LTR

Constant

Value: `0`

**Description**

Left to right

---

### BIDI_RTL

Constant

Value: `1`

**Description**

Right to left

---

### BIDI_DEFAULT_LTR

Constant

Value: `2`

**Description**

Default left to right

---

### BIDI_DEFAULT_RTL

Constant

Value: `3`

**Description**

Default right to left

---
