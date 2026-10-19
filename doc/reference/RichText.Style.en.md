# RichText.Style

Text style class

Defines the logical style of text (font, size, weight, etc.).
The drawing appearance (color, outline, etc.) is set with the Appearance class.

## Members

### Constructors

- [Style](#style)

### Properties

- [fontSize](#fontsize)
- [fontWeight](#fontweight)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [wordSpacing](#wordspacing)
- [scaleX](#scalex)
- [skewX](#skewx)
- [fontWidth](#fontwidth)
- [bidi](#bidi)

### Methods

- [setFonts](#setfonts)
- [setLocale](#setlocale)
- [clone](#clone)

---

### Style

Constructor

**Description**

Constructor

---

### fontSize

Property \ Access: `r/w`

**Description**

Font size (in pixels)

Default: 16

---

### fontWeight

Property \ Access: `r/w`

**Description**

Font weight

A value from 100 to 900. 400 = regular, 700 = bold
Default: 400

---

### italic

Property \ Access: `r/w`

**Description**

Italic

Default: false

---

### letterSpacing

Property \ Access: `r/w`

**Description**

Letter spacing (in em)

0.1 = extra space of 10% of the font size
Default: 0

---

### wordSpacing

Property \ Access: `r/w`

**Description**

Word spacing (in em)

Default: 0

---

### scaleX

Property \ Access: `r/w`

**Description**

Horizontal scale

1.0 = normal, 0.5 = half width
Default: 1.0

---

### skewX

Property \ Access: `r/w`

**Description**

Oblique skew value

0 = normal; negative values slant to the right
Default: 0

---

### fontWidth

Property \ Access: `r/w`

**Description**

Font width (the wdth axis of variable fonts, in percent)

100 = normal width, 50 = half width, 200 = double width.
Effective only with variable fonts that support the wdth axis.
Default: 100

---

### bidi

Property \ Access: `r/w`

**Description**

Bidirectional text control

RichText.BIDI_LTR / BIDI_RTL / BIDI_DEFAULT_LTR / BIDI_DEFAULT_RTL
Default: BIDI_DEFAULT_LTR

---

### setFonts

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `names` | `&nbsp;` | Array of font names (in priority order) |

**Description**

Sets the font collection

The order of the array is the fallback priority.
Characters that the first font cannot draw are drawn with the next font.

Each element can be a name registered with registerFont; if no registered name matches,
it can also refer to the family name inside the font file
(e.g. "Noto Sans JP") or the combined "family Style" name
(e.g. "Noto Sans JP Bold").
Example:
style.setFonts(["メインフォント", "絵文字フォント", "フォールバック"]);

---

### setLocale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `locale` | `&nbsp;` | Locale string |

**Description**

Sets the locale

Affects line-breaking rules such as kinsoku (Japanese line-breaking rules).
Example:
style.setLocale("ja_JP");

---

### clone

Method

**Return value**

The duplicated Style object

**Description**

Duplicates the style

---
