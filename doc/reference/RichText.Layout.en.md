# RichText.Layout

Single-line text layout class

Holds the layout result for a single line of text.
Separating layout from drawing lets you reuse measurements
and draw pre-laid-out text.

Example:
var tl = new RichText.Layout();
tl.layout("Hello World", style);
Debug.message("幅: " + tl.width + ", 高さ: " + tl.height);
layer.drawTextLayout(tl, 10, 50, appearance);

## Members

### Constructors

- [Layout](#layout)

### Properties

- [width](#width)
- [height](#height)
- [ascent](#ascent)
- [descent](#descent)
- [charCount](#charcount)

### Methods

- [layout](#layout)
- [clone](#clone)

---

### Layout

Constructor

**Description**

Constructor

---

### width

Property \ Access: `r/w`

**Description**

Text width (read-only)

---

### height

Property \ Access: `r/w`

**Description**

Text height (ascent + descent) (read-only)

---

### ascent

Property \ Access: `r/w`

**Description**

Ascent (from the baseline to the top, negative) (read-only)

---

### descent

Property \ Access: `r/w`

**Description**

Descent (from the baseline to the bottom, positive) (read-only)

---

### charCount

Property \ Access: `r/w`

**Description**

Number of characters (read-only)

---

### layout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text |
| `style` | `&nbsp;` | RichText.Style object |

**Description**

Lays out (measures) the text

---

### clone

Method

**Return value**

The duplicated Layout object

**Description**

Duplicates the layout

---
