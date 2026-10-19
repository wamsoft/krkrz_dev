# RichText.ParagraphLayout

Paragraph (multi-line) text layout class

Holds the layout result for multi-line text.
Separating layout from drawing lets you reuse measurements
and display text progressively (with maxChars).

Example:
var pl = new RichText.ParagraphLayout();
pl.layout("長いテキスト...", 300, style);
Debug.message("行数: " + pl.lineCount);
layer.drawParagraphLayout(pl, 10, 10, 300, 200,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);

## Members

### Constructors

- [ParagraphLayout](#paragraphlayout)

### Properties

- [lineCount](#linecount)
- [totalHeight](#totalheight)
- [maxWidth](#maxwidth)
- [totalCharCount](#totalcharcount)
- [lineSpacing](#linespacing)
- [breakStrategy](#breakstrategy)

### Methods

- [layout](#layout)
- [getLineInfo](#getlineinfo)
- [clone](#clone)

---

### ParagraphLayout

Constructor

**Description**

Constructor

---

### lineCount

Property \ Access: `r/w`

**Description**

Number of lines (read-only)

---

### totalHeight

Property \ Access: `r/w`

**Description**

Total height of all lines (read-only)

---

### maxWidth

Property \ Access: `r/w`

**Description**

Maximum line width (read-only)

---

### totalCharCount

Property \ Access: `r/w`

**Description**

Total number of characters in all lines (read-only)

---

### lineSpacing

Property \ Access: `r/w`

**Description**

Line spacing

Default: 0

---

### breakStrategy

Property \ Access: `r/w`

**Description**

Line-breaking strategy

RichText.BREAK_GREEDY / BREAK_HIGH_QUALITY / BREAK_BALANCED
Default: BREAK_HIGH_QUALITY

---

### layout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text |
| `maxWidth` | `&nbsp;` | Maximum width |
| `style` | `&nbsp;` | RichText.Style object |

**Description**

Lays out (measures) the paragraph

---

### getLineInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` | Line index (0 to lineCount-1) |

**Return value**

Line information dictionary %[startIndex, endIndex, width, height]

**Description**

Gets line information

---

### clone

Method

**Return value**

The duplicated ParagraphLayout object

**Description**

Duplicates the layout

---
