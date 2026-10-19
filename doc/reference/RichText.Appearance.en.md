# RichText.Appearance

Drawing appearance class

Corresponds to Illustrator's Appearance.
Decorations are produced by stacking multiple fills and strokes (outlines).
Items added earlier are drawn underneath (further back).

Typical order:
1. Shadow (addShadow, or addFill with an offset)
2. Outline (addStroke)
3. Main fill (addFill)

## Members

### Constructors

- [Appearance](#appearance)

### Properties

- [isEmpty](#isempty)
- [count](#count)

### Methods

- [addFill](#addfill)
- [addStroke](#addstroke)
- [addShadow](#addshadow)
- [setColor](#setcolor)
- [addColor](#addcolor)
- [setOutline](#setoutline)
- [addOutline](#addoutline)
- [setShadow](#setshadow)
- [clear](#clear)
- [clone](#clone)

---

### Appearance

Constructor

**Description**

Constructor

---

### isEmpty

Property \ Access: `r/w`

**Description**

Whether there are no styles (read-only)

---

### count

Property \ Access: `r/w`

**Description**

Number of styles (read-only)

---

### addFill

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value (e.g. 0xFFFFFFFF = white, 0xFF000000 = black) |
| `offsetX` | `0` | X offset (default: 0) |
| `offsetY` | `0` | Y offset (default: 0) |

**Description**

Adds a fill

Example:
app.addFill(0xFFFFFFFF);  // 白で塗り
app.addFill(0x80000000, 2, 2);  // 半透明黒で影効果

---

### addStroke

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value |
| `width` | `&nbsp;` | Line width |
| `offsetX` | `0` | X offset (default: 0) |
| `offsetY` | `0` | Y offset (default: 0) |

**Description**

Adds a stroke (outline)

Example:
app.addStroke(0xFF000000, 2);  // 黒2pxの縁取り

---

### addShadow

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | Shadow color (ARGB) |
| `offsetX` | `&nbsp;` | X offset |
| `offsetY` | `&nbsp;` | Y offset |

**Description**

Adds a shadow

Shadows are always added at the bottom (furthest back).
Example:
app.addShadow(0x80000000, 2, 2);  // 半透明黒の影

---

### setColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value |

**Description**

Sets the text color (replaces the existing normal fill)

Replaces the existing normal fill (the fill with offset 0,0) with the given color.
If there is no normal fill, a new one is added.
Example:
app.setColor(0xFFFF0000);  // テキスト色を赤に変更

---

### addColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value |
| `offsetX` | `0` | X offset (default: 0) |
| `offsetY` | `0` | Y offset (default: 0) |

**Description**

Adds a text color (on top)

Like addFill, but added in front of everything else.

---

### setOutline

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value |
| `width` | `&nbsp;` | Line width |
| `offsetX` | `0` | X offset (default: 0) |
| `offsetY` | `0` | Y offset (default: 0) |

**Description**

Sets the outline (replaces the existing stroke)

Replaces the existing stroke with the given one.
If there is no stroke, a new one is added.

---

### addOutline

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB color value |
| `width` | `&nbsp;` | Line width |
| `offsetX` | `0` | X offset (default: 0) |
| `offsetY` | `0` | Y offset (default: 0) |

**Description**

Adds an outline (as the rearmost stroke)

---

### setShadow

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `color` | `&nbsp;` | Shadow color (ARGB) |
| `offsetX` | `&nbsp;` | X offset |
| `offsetY` | `&nbsp;` | Y offset |

**Description**

Sets the shadow (replaces the existing shadow fill)

Replaces the existing shadow (a fill with an offset) with the given one.

---

### clear

Method

**Description**

Clears all styles

---

### clone

Method

**Return value**

The duplicated Appearance object

**Description**

Duplicates the appearance

---
