# RichText.StyledLayout

Layout class for text with style tags

Holds the layout result for text with style tags.
Separating layout from drawing makes redrawing the same text and
character-by-character display animations efficient.

Example:

```tjs
var sl = new RichText.StyledLayout();
sl.layout(
"<style:bold>太字</style>と通常テキスト",
400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]
);
layer.drawStyledLayout(sl, 10, 10);
```

## Members

### Constructors

- [StyledLayout](#styledlayout)

### Properties

- [lineCount](#linecount)
- [totalCharCount](#totalcharcount)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [isValid](#isvalid)
- [totalRenderDelay](#totalrenderdelay)

### Methods

- [layout](#layout)
- [resolveAllTimings](#resolvealltimings)
- [calcShowCount](#calcshowcount)
- [getKeyWaits](#getkeywaits)
- [getResolvedTimings](#getresolvedtimings)

---

### StyledLayout

Constructor

**Description**

Constructor

---

### lineCount

Property \ Access: `r/w`

**Description**

Number of lines (read-only)

---

### totalCharCount

Property \ Access: `r/w`

**Description**

Total number of characters (read-only)

Used as the upper bound for character-by-character display animations

---

### maxWidth

Property \ Access: `r/w`

**Description**

Maximum width of the layout (read-only)

---

### maxHeight

Property \ Access: `r/w`

**Description**

Maximum height of the layout (read-only)

---

### isValid

Property \ Access: `r/w`

**Description**

Whether the layout is valid (read-only)

Becomes true after layout() is called.

---

### totalRenderDelay

Property \ Access: `r/w`

**Description**

Maximum overall display delay (ms) (read-only)

The time until all characters have been displayed.
Use it as the timer limit for character-by-character display animations.

---

### layout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | Text with style tags |
| `maxWidth` | `&nbsp;` | Maximum width |
| `maxHeight` | `&nbsp;` | Maximum height |
| `hAlign` | `&nbsp;` | Horizontal alignment (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | Vertical alignment (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `styles` | `&nbsp;` | A single Style, or a dictionary mapping style names to Style objects |
| `appearances` | `&nbsp;` | A single Appearance, or a dictionary mapping style names to Appearance objects |
| `lineSpacing` | `0` | Line spacing (default: 0) |

**Description**

Computes the text layout

If a single object is passed for styles / appearances, it is treated as the "default" key.

Example:
// 単一スタイル
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, appearance);

// 複数スタイル
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]);

---

### resolveAllTimings

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `timeScale` | `1.0` | Time scale factor (default: 1.0) |
| `widthTimeScale` | `false` | Whether to adjust timing by character width (default: false) |

**Description**

Resolves timing information

Resolves the timing information produced by layout() (the `<start>`, `<delay>`, `<wait>`, `<sync>`, and `<keywait>` tags)
and computes the display start time of each character.

Even if you do not call it explicitly, it is resolved automatically with default values (timeScale=1.0, widthTimeScale=false)
on the first access to getResolvedTimings / getKeyWaits / totalRenderDelay /
calcShowCount.

Example:
sl.resolveAllTimings(1.0, false);
// 倍速表示
sl.resolveAllTimings(0.5, false);

---

### calcShowCount

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `time` | `&nbsp;` | Elapsed time (ms) |

**Return value**

Number of characters to display

**Description**

Computes the number of characters to display by the given time

Pass the result as the maxChars argument of drawStyledLayout
to implement time-based character-by-character display animations.

Example:
var count = sl.calcShowCount(elapsed);
layer.drawStyledLayout(sl, x, y, count);

---

### getKeyWaits

Method

**Return value**

Array of key-wait information

**Description**

Gets key-wait information

Each element is a dictionary %[pos, time].
- pos: character position (charIndex)
- time: elapsed time at that point (ms)

Returns the positions of `<keywait/>` tags and the cumulative display time up to each.

---

### getResolvedTimings

Method

**Return value**

Array of timing information

**Description**

Gets the resolved timing information

Each element is a dictionary %[charIndex, delay].
- charIndex: character position
- delay: display start time (ms)

Detailed information about when each character is displayed.

---
