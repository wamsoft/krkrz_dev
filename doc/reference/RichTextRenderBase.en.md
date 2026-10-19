# RichTextRenderBase

TextRender-compatible text rendering class

Provides an interface API-compatible with the TextRender class in ../textrender.
Internally it draws using the richtext library (StyledLayout).

It accepts text with TextRender escape notation and returns the layout result
as character, timing, and link information.

Special input text notation:
\n      line break
\t      tab character
\i      start indent (from the next line) *not supported
\r      end indent (from the next line) *not supported
\w      advance the position by one space
\k      generate key-wait information
\x      equivalent to a NUL character
\{char}  escape (disables the special meaning)
[xxxx]          ruby (applies to the next character)
[xxxx,{count}]  ruby (applies to the next {count} characters)

Font:
%f{name};   font face
%bX         bold (0: off, 1: on, other: default)
%iX         italic (0: off, 1: on, other: default)
%sX         shadow (0: off, 1: on, other: default)
%eX         edge (0: off, 1: on, other: default)
%{number};  font size (percentage of the default)
%B          large font
%S          small font
#xxxxxx;    color (hex RGB)
%s#xxxxxx;  shadow color
%e#xxxxxx;  edge color
%r          reset font

Style:
%C          center
%R          right-align
%L          left-align
%p{number}; pitch (letter spacing)

Special:
%d{number}; display time per character (percentage of standard; 100 = standard speed)
%a{number}; display time per character (ms)
%w{number}; wait (percentage of one character's time; 100 = one character)
%t{number}; wait (ms)
%D{number}; time sync (ms)
%D$xxx;     time sync (label reference)

$xxx;       embedding (variable name) *handled by onEval
&xxx;       graphic character (image name) *handled by onGetGraphSize

Links:
%l{link name};  start link
%l;             end link

Not supported:
vertical text, rubyoffset, word-break control (%k0/%k1)

Workflow:
clear() → setFont/setStyle → render() [can be called multiple times] → done()
→ get results with getCharacters() / calcShowCount() / getKeyWait(), etc.

Example:
var tr = new TextRenderBase();
tr.setDefault(%[ face: "MSゴシック", fontsize: 24, color: 0xFFFFFF ]);
tr.setRenderSize(400, 300);
tr.clear();
tr.render("こんにちは%B世界%r！\n2行目", 0, 30, 0, false);
tr.done();

var chars = tr.getCharacters(0, 0);  // 全文字情報取得
var count = tr.calcShowCount(500);    // 500ms時点の表示文字数

## Members

### Properties

- [timeScale](#timescale)
- [fontScale](#fontscale)
- [defaultFace](#defaultface)
- [defaultFontSize](#defaultfontsize)
- [defaultBigFontSize](#defaultbigfontsize)
- [defaultSmallFontSize](#defaultsmallfontsize)
- [defaultLineSize](#defaultlinesize)
- [defaultLineSpacing](#defaultlinespacing)
- [defaultPitch](#defaultpitch)
- [defaultAlign](#defaultalign)
- [defaultValign](#defaultvalign)
- [defaultRubySize](#defaultrubysize)
- [defaultColor](#defaultcolor)
- [defaultShadow](#defaultshadow)
- [defaultShadowColor](#defaultshadowcolor)
- [defaultEdge](#defaultedge)
- [defaultEdgeColor](#defaultedgecolor)
- [defaultBold](#defaultbold)
- [defaultItalic](#defaultitalic)
- [renderOver](#renderover)
- [renderLines](#renderlines)
- [renderCount](#rendercount)
- [renderDelay](#renderdelay)
- [renderLeft](#renderleft)
- [renderTop](#rendertop)
- [renderRight](#renderright)
- [renderBottom](#renderbottom)
- [renderText](#rendertext)

### Methods

- [TextRenderBase](#textrenderbase)
- [setOption](#setoption)
- [setDefault](#setdefault)
- [setRenderSize](#setrendersize)
- [clear](#clear)
- [setFont](#setfont)
- [resetFont](#resetfont)
- [setStyle](#setstyle)
- [resetStyle](#resetstyle)
- [render](#render)
- [newline](#newline)
- [done](#done)
- [onEval](#oneval)
- [onLabel](#onlabel)
- [onGetGraphSize](#ongetgraphsize)
- [getKeyWait](#getkeywait)
- [calcShowCount](#calcshowcount)
- [calcLineOffset](#calclineoffset)
- [getCharacters](#getcharacters)
- [getLinkNames](#getlinknames)
- [getLinkRects](#getlinkrects)
- [getLinkCharacters](#getlinkcharacters)
- [isLinkContains](#islinkcontains)
- [getLinkOfPosition](#getlinkofposition)
- [drawToLayer](#drawtolayer)

---

### timeScale

Property \ Access: `r/w`

**Description**

Rendering time scale

---

### fontScale

Property \ Access: `r/w`

**Description**

Font size scale factor

---

### defaultFace

Property \ Access: `r/w`

**Description**

Default value properties

---

### defaultFontSize

Property \ Access: `r/w`

---

### defaultBigFontSize

Property \ Access: `r/w`

---

### defaultSmallFontSize

Property \ Access: `r/w`

---

### defaultLineSize

Property \ Access: `r/w`

---

### defaultLineSpacing

Property \ Access: `r/w`

---

### defaultPitch

Property \ Access: `r/w`

---

### defaultAlign

Property \ Access: `r/w`

---

### defaultValign

Property \ Access: `r/w`

---

### defaultRubySize

Property \ Access: `r/w`

---

### defaultColor

Property \ Access: `r/w`

---

### defaultShadow

Property \ Access: `r/w`

---

### defaultShadowColor

Property \ Access: `r/w`

---

### defaultEdge

Property \ Access: `r/w`

---

### defaultEdgeColor

Property \ Access: `r/w`

---

### defaultBold

Property \ Access: `r/w`

---

### defaultItalic

Property \ Access: `r/w`

---

### renderOver

Property \ Access: `r/w`

**Description**

Whether the rendering result overflows the area

---

### renderLines

Property \ Access: `r/w`

**Description**

Number of lines in the rendering result

---

### renderCount

Property \ Access: `r/w`

**Description**

Number of characters in the rendering result

---

### renderDelay

Property \ Access: `r/w`

**Description**

Total display time of the rendering result

---

### renderLeft

Property \ Access: `r/w`

**Description**

Left edge of the rendering result area

---

### renderTop

Property \ Access: `r/w`

**Description**

Top edge of the rendering result area

---

### renderRight

Property \ Access: `r/w`

**Description**

Right edge of the rendering result area

---

### renderBottom

Property \ Access: `r/w`

**Description**

Bottom edge of the rendering result area

---

### renderText

Property \ Access: `r/w`

**Description**

Text of the rendering result (escapes removed)

---

### TextRenderBase

Method

**Description**

Constructor

---

### setOption

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Dictionary |

**Description**

Sets rendering options

Available keys:
ignore_color  ignore color specifications
ignore_size   ignore size specifications
ignore_type   ignore font type specifications (bold/italic/shadow/edge)
ignore_face   ignore font face specifications
ignore_style  ignore style specifications (align/pitch)
ignore_ruby   ignore ruby specifications
ignore_delay  ignore timing specifications
width_time_scale  adjust timing by character width (0: no, 1: yes)
locale        locale string (e.g. "ja_JP")

---

### setDefault

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Dictionary |

**Description**

Sets default values

Only keys present in the dictionary are applied (other keys keep their current values).
After setDefault, the equivalent of resetFont() / resetStyle() runs internally,
syncing the current font and style state to the defaults.

Available keys:
face          font face
Besides a collection name registered with registerCollection, it can be
a name registered with registerFont, a family name in the font file
(e.g. "Noto Sans JP"), or a combined "family Style" name
(e.g. "Noto Sans JP Bold").
fontsize      font size
bigfontsize   large font size (for %B)
smallfontsize small font size (for %S)
bold          bold
italic        italic
color         text color (RGB)
shadow        shadow
shadowcolor   shadow color
edge          edge
edgecolor     edge color
linespacing   line spacing
pitch         letter spacing
linesize      line size
align         horizontal alignment (-1: left, 0: center, 1: right)
valign        vertical alignment (-1: top, 0: middle, 1: bottom)
rubysize      ruby size

---

### setRenderSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `width` | `&nbsp;` | Area width (0 for unlimited) |
| `height` | `&nbsp;` | Area height (0 for unlimited) |

**Description**

Sets the size of the rendering area

---

### clear

Method

**Description**

Clears the rendering result

---

### setFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Dictionary |

**Description**

Sets the font

Available keys:
face, fontsize, bold, italic, color, shadow, shadowcolor, edge, edgecolor

---

### resetFont

Method

**Description**

Resets the font state to the defaults

---

### setStyle

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `elm` | `&nbsp;` | Dictionary |

**Description**

Sets the style

Available keys:
linespacing, pitch, linesize, align, valign

---

### resetStyle

Method

**Description**

Resets the style to the defaults

---

### render

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `str` | `&nbsp;` | String to render (may contain escape notation) |
| `autoIndent` | `0` | Auto indent (0: disabled, 1: enabled, -1: hanging indent) *currently not supported |
| `diff` | `0` | Display time per character (ms) |
| `all` | `0` | Total time (0 for automatic, ms) |
| `noResetDelay` | `false` | If true, the previous display time is kept |

**Return value**

true if rendering succeeded without overflowing

**Description**

Renders text

Can be called multiple times after clear(). The result is not finalized until done() is called.

---

### newline

Method

**Description**

Starts a new line

---

### done

Method

**Description**

Finishes rendering

Lays out all the text accumulated by render() at once
and finalizes timing, link, and other information.

---

### onEval

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Variable name |

**Return value**

Variable value (string)

**Description**

Handles variable references during rendering

Called when referenced with the $xxx; notation.
Can be overridden in a subclass.

---

### onLabel

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Label name |

**Return value**

Tick value (ms)

**Description**

Handles label references during rendering

Called when referenced with the %D$xxx; notation.

---

### onGetGraphSize

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` | Image name |

**Return value**

%[width: width, height: height]

**Description**

Gets the size of a graphic character

Called when referenced with the &xxx; notation.

---

### getKeyWait

Method

**Return value**

[%[pos: character position, time: time], ...]

**Description**

Returns an array of key-wait information

---

### calcShowCount

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `time` | `&nbsp;` | Time (ms) |

**Return value**

Number of characters displayed

**Description**

Returns the number of characters displayed at the given time

---

### calcLineOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `lineno` | `&nbsp;` | Line number |

**Return value**

Offset value

**Description**

Returns the offset of the given line

---

### getCharacters

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `start` | `&nbsp;` | Start character position |
| `num` | `&nbsp;` | Number of characters to get (0 for up to the end) |

**Return value**

Array of drawing information

**Description**

Gets character information of the rendering result

Each element is a dictionary with the following keys:
text       text to display
graph      image name when displaying a graphic (void for normal characters)
x          display X coordinate
y          display Y coordinate
cw         display width
size       font size
face       font face
color      display color
bold       bold
italic     italic
shadow     shadow
edge       edge
shadowColor  shadow color
edgeColor    edge color
delay      display timing (elapsed time from the start of display)
link       link number (-1 if none)
linkName   link name (void if none)
ruby       ruby array [%[text, x, y, size], ...]

---

### getLinkNames

Method

**Return value**

Array of link names (duplicate names are listed as is)

**Description**

Returns the list of link names contained

---

### getLinkRects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `link` | `&nbsp;` | Link number |

**Return value**

Array of areas [%[left, top, width, height], ...]

**Description**

Gets the area information of a link

If the link spans multiple lines, multiple rectangles are returned.

---

### getLinkCharacters

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `link` | `&nbsp;` | Link number |

**Return value**

Array of drawing information (same format as getCharacters)

**Description**

Gets the character information belonging to a link

---

### isLinkContains

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `link` | `&nbsp;` | Link number |
| `x` | `&nbsp;` | X position |
| `y` | `&nbsp;` | Y position |

**Return value**

true if the position is inside the link

**Description**

Checks whether a position is inside a link

---

### getLinkOfPosition

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` | X position |
| `y` | `&nbsp;` | Y position |

**Return value**

Link number (-1: none)

**Description**

Returns the link number at the given position

---

### drawToLayer

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Destination layer object |
| `x` | `&nbsp;` | Drawing start X coordinate |
| `y` | `&nbsp;` | Drawing start Y coordinate |
| `maxChars` | `-1` | Maximum number of characters to draw (-1 for all; default: -1) |

**Return value**

Array of the drawn area [x, y, width, height]

**Description**

Draws the rendering result to a layer

Draws the rendering result finalized by done() to the given layer.
Specifying maxChars enables character-by-character display animations.

Example:
tr.render("テキスト", 0, 50, 0);
tr.done();
tr.drawToLayer(layer, 10, 10);

// 文字送り
var count = tr.calcShowCount(elapsed);
tr.drawToLayer(layer, 10, 10, count);

---
