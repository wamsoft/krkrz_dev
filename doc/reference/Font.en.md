# Font

The Font class manages **fonts**.

## Members

### Constructors

- [Font](#font)

### Properties

- [face](#face)
- [height](#height)
- [bold](#bold)
- [italic](#italic)
- [strikeout](#strikeout)
- [underline](#underline)
- [angle](#angle)
- [rasterizer](#rasterizer)
- [emojiMode](#emojimode)
- [weight](#weight)
- [variations](#variations)
- [defaultUseVarStyle](#defaultusevarstyle)
- [defaultEmojiMode](#defaultemojimode)
- [emojiFaceName](#emojifacename)
- [colorEmojiFaceName](#coloremojifacename)
- [defaultFaceName](#defaultfacename)
- [faceIsFileName](#faceisfilename)

### Methods

- [getTextWidth](#gettextwidth)
- [getTextHeight](#gettextheight)
- [getEscWidthX](#getescwidthx)
- [getEscWidthY](#getescwidthy)
- [getEscHeightX](#getescheightx)
- [getEscHeightY](#getescheighty)
- [getGlyphDrawRect](#getglyphdrawrect)
- [getList](#getlist)
- [mapPrerenderedFont](#mapprerenderedfont)
- [unmapPrerenderedFont](#unmapprerenderedfont)
- [addFont](#addfont)
- [registerFontFile](#registerfontfile)
- [queryFonts](#queryfonts)
- [getFontInfo](#getfontinfo)
- [getVarAxes](#getvaraxes)
- [setDefaultVariations](#setdefaultvariations)
- [getDefaultVariations](#getdefaultvariations)

---

### Font

Constructor

**Description**

Constructor

The font member of Layer is a special version created with a Layer as its argument.
To use a Font on its own, create it without arguments.

---

### face

Property \ Access: `r/w`

**Description**

Font name

The font name. This property can also be set.

You can specify multiple candidates separated by commas. In that case a font that actually exists is used, with earlier candidates taking priority. Whether a font exists is determined by consulting the OS font list. If no candidate matches, the default font is used (fixed to "ＭＳ Ｐゴシック" (MS PGothic) in the current version).

If you start with a comma followed by a font name, the engine tries to pass that font to the OS even if the OS does not enumerate it (e.g. ",My Original Font"). This lets you use non-enumerable fonts registered with the Win32 AddFontResource API and the like.

For variable fonts, you can append `#tag=val[,tag=val...]` to the font name
to specify a variable axis instance (e.g. `"MyFont#wght=700"`,
`"MyFont#wght=700,wdth=75"`). It can be given separately for each element of the fallback chain,
and unlike [variations](#variations) it applies per face. It is effective only on the glyphware path
( [Layer.drawShapedText](Layer.md#drawshapedtext) and related methods, and [rasterizer](#rasterizer) = 2 ).

When a variable font is referenced without axes, it is normalized to the equivalent of wght=400
(the same as the CSS font-weight default). To change the default used when nothing is specified,
use [setDefaultVariations](#setdefaultvariations).

---

### height

Property \ Access: `r/w`

**Description**

Font height

Height of the drawn characters, in pixels. This property can also be set.

---

### bold

Property \ Access: `r/w`

**Description**

Bold

Whether the font is bold. This property can also be set.

Set true for bold.

---

### italic

Property \ Access: `r/w`

**Description**

Italic

Whether the font is italic. This property can also be set.

Set true for italic.

---

### strikeout

Property \ Access: `r/w`

**Description**

Strikeout

Whether to draw a strikeout line. This property can also be set.

Set true to draw a strikeout line over the characters.

---

### underline

Property \ Access: `r/w`

**Description**

Underline

Whether to draw an underline (or a side line in vertical text). This property can also be set.

Set true to draw an underline.

---

### angle

Property \ Access: `r/w`

**Description**

Text drawing angle

The text drawing angle. This property can also be set.

The unit is tenths of a degree. The value ranges from 0 to 3600.

For vertical text, specify a vertical-writing font name as the font name and
set this property to 2700.

---

### rasterizer

Property \ Access: `r/w`

**Description**

Text rendering method

The rasterizer (text rendering method) used by [Layer.drawText](Layer.md#drawtext).
This property can also be set.

The value is an integer index, and the numbering is **the same in all builds**:

`**0**` : FreeType rasterizer (included in all builds; the default for SDL / generic builds)

`**1**` : GDI rasterizer (WINVER only; the default for WINVER)

`**2**` : glyphware (the unified font engine; FreeType + HarfBuzz). This does not change the default;
only when selected does drawText generate glyphs through glyphware (outline rendering rather than embedded bitmaps,
with color emoji support).
Note that the drawText path steps one code point per cell and **does not perform shaping**
(if you need BiDi or complex script shaping, use
[Layer.drawShapedText](Layer.md#drawshapedtext)).

If you set a number not included in the build (e.g. 1 in an SDL / generic build),
it falls back to FreeType (0), and reading the property back returns the effective value after fallback.
So you can detect support by setting the value and reading it back: if it does not match, that rasterizer is not included.

With FreeType / glyphware, only horizontal text is supported. Other directions are not supported.

This property is static. Set it via Font.rasterizer.

---

### emojiMode

Property \ Access: `r/w`

**Description**

Emoji drawing mode

The mode for drawing applicable code points by falling back to an emoji font.
This property can also be set.

`**-1** ` : Follow the global default ( `Font.defaultEmojiMode` ) (default)

`** 0** ` : Do not use emoji fonts (original font only)

`** 1** ` : Draw with a monochrome emoji font

`** 2** ` : Draw with a color emoji font

This feature is effective only with the FreeType rasterizer ( `rasterizer` = 0 ).
It has no effect with the GDI rasterizer (the WINVER default).

Emoji fonts are embedded in the executable by default (monochrome = Noto Emoji,
color = Noto Color Emoji). You can replace them with any emoji font using `emojiFaceName` / `colorEmojiFaceName` and `addFont`.

Note: code points such as ★ and ❤ that also have glyphs in the original font may be drawn from the original font
and appear monochrome.

To control this per character, append a variation selector right after the character in the text.
Appending **VS16** (U+FE0F) makes that one character prefer the emoji font,
and appending **VS15** (U+FE0E) forces the original font (text presentation).
(e.g. "❤"+U+FE0F for color, "❤"+U+FE0E for monochrome). There is no automatic selection without a selector
(Emoji_Presentation default) (advanced multilingual processing is out of scope).

---

### weight

Property \ Access: `r/w`

**Description**

Font weight (variable fonts)

The font weight. This property can also be set. Specify a number from 100 to 900,
or void (unspecified = the font's default).

It acts as a variable axis on variable font faces that have a `wght` axis
(if `wght` is given explicitly in [variations](#variations), that takes priority).

It is effective only on the glyphware path: [Layer.drawShapedText](Layer.md#drawshapedtext) and related methods
(always), and [Layer.drawText](Layer.md#drawtext) when [rasterizer](#rasterizer) = 2.
The older FreeType / GDI rasterizers ignore it (with a warning once after startup).

---

### variations

Property \ Access: `r/w`

**Description**

Variable axis settings (variable fonts)

Specifies the variable axes of a variable font in the form `"wght=700,wdth=87.5"`.
This property can also be set. void or an empty string clears it.

The value is normalized when set: tags are lowercased and sorted in ascending order, the last of duplicate tags wins,
and values are quantized (`wght` in steps of 1, other axes in steps of 0.5, so that axis animation does not
grow the cache without bound). An invalid format throws an exception.

Only axes of the same name that each face in the fallback chain actually has are applied.
You can find the available axes with [getVarAxes](#getvaraxes). The scope (glyphware
path only) is the same as for [weight](#weight).

---

### defaultUseVarStyle

Property \ Access: `r/w`

**Description**

Variable axis mapping for bold / italic (class property)

When true, for faces that can express `bold` / `italic` with variable axes (variable fonts with `wght` /
`slnt` / `ital` axes), the axes (wght=700 / slnt=-10 / ital=1) are used instead of synthetic bold / synthetic
italic, and the synthetic styles are disabled to avoid applying both. The default is false (so as not to change the existing appearance).

Whether the axes exist is determined from the first (primary) face in the fallback chain.
Effective only on the glyphware path.

---

### defaultEmojiMode

Property \ Access: `r/w`

**Type**: `Integer`

**Description**

Global default emoji drawing mode

Gets or sets the default emoji drawing mode applied to fonts whose `emojiMode` is -1.
The values are the same as for `emojiMode` (0 = not used / 1 = monochrome / 2 = color).
This property is static.

---

### emojiFaceName

Property \ Access: `r/w`

**Type**: `String`

**Description**

Face name used for monochrome emoji fallback

Gets or sets the face name of the emoji font used when `emojiMode` = 1 (monochrome).
The default is the embedded Noto Emoji ("Noto Emoji Regular").
You can specify the face name of any font registered with `addFont`.
This property is static.

---

### colorEmojiFaceName

Property \ Access: `r/w`

**Type**: `String`

**Description**

Face name used for color emoji fallback

Gets or sets the face name of the emoji font used when `emojiMode` = 2 (color).
The default is the embedded Noto Color Emoji ("Noto Color Emoji Regular").
Color emoji in COLRv0 / CBDT / sbix formats are supported (COLRv1 is not).
This property is static.

---

### defaultFaceName

Property \ Access: `r/w`

**Type**: `String`

**Description**

Default font face name

Gets or sets the face name of the default font used when no font is specified.
As a static class property, it is shared by all layers.

---

### faceIsFileName

Property \ Access: `r/w`

**Type**: `Boolean`

**Description**

Whether to treat the face name as a file name

When true, the name given in the `face` property is opened as a font file name
(effective only with FreeType).

Note: if you enable the IME on a layer with this flag set to true, the IME input field uses
`DEFAULT_GUI_FONT`.

---

### getTextWidth

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to measure. |

**Return value**

Width of the given string, in pixels

**Description**

Gets the width of a string

Gets the width needed to draw the given string
with the current font settings.

**See also:** [Font.getTextHeight](Font.md#gettextheight)

---

### getTextHeight

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String to measure. |

**Return value**

Height of the given string, in pixels

**Description**

Gets the height of a string

Gets the height needed to draw the given string with this font.

**See also:** [Font.getTextWidth](Font.md#gettextwidth)

---

### getEscWidthX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String whose horizontal X advance you want. |

**Return value**

X advance of the text in the horizontal direction, in pixels

**Description**

X advance of text in the horizontal direction

Gets how far the drawing position advances when the given text is drawn
with the current font settings.

This method returns the advance along the X axis when moving sideways (to the left) relative to the text drawing direction.

**See also:** [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscWidthY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String whose horizontal Y advance you want. |

**Return value**

Y advance of the text in the horizontal direction, in pixels

**Description**

Y advance of text in the horizontal direction

Gets how far the drawing position advances when the given text is drawn
with the current font settings.

This method returns the advance along the Y axis when moving sideways (to the left) relative to the text drawing direction.

**See also:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightX

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String whose vertical X advance you want. |

**Return value**

X advance of the text in the vertical direction, in pixels

**Description**

X advance of text in the vertical direction

Gets how far the drawing position advances when the given text is drawn
with the current font settings.

This method returns the advance along the X axis when moving vertically (downward) relative to the text drawing direction.

**See also:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightY

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String whose vertical Y advance you want. |

**Return value**

Y advance of the text in the vertical direction, in pixels

**Description**

Y advance of text in the vertical direction

Gets how far the drawing position advances when the given text is drawn
with the current font settings.

This method returns the advance along the Y axis when moving vertically (downward) relative to the text drawing direction.

**See also:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx)

---

### getGlyphDrawRect

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `text` | `&nbsp;` | String whose area you want. |

**Return value**

Actual drawing area of the string

**Description**

Actual drawing area of a string

Gets the area in which glyph images are drawn when the given text is drawn with the current font settings.

The result is a Rect object relative to coordinate 0,0.

Only horizontal text is supported.

**See also:** [Rect](Rect.md)

---

### getList

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `flags` | `&nbsp;` | How to enumerate fonts.<br>Specify a bitwise OR of the following values.<br>`**fsfFixedPitch**    ` : Enumerate only fixed-pitch fonts<br>`**fsfSameCharSet**   ` : Enumerate only fonts with the same character set<br>`**fsfNoVertical**    ` : Do not enumerate vertical-writing fonts<br>`**fsfTrueTypeOnly**  ` : Enumerate only TrueType fonts<br>`**fsfIgnoreSymbol**  ` : Exclude the symbol character set<br>With fsfSameCharSet, fonts with the same character set as the currently selected font<br>are enumerated. |

**Return value**

Array whose elements are font names (strings)

**Description**

Enumerates font names

Enumerates font names and returns them as an array.

---

### mapPrerenderedFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fontstorage` | `&nbsp;` | Prerendered font storage. |

**Description**

Maps a prerendered font

Maps a **prerendered font** to the currently selected font name.

From then on, the specified prerendered font is used instead for fonts with the same settings.

The setting applies to all layers.

**See also:** [Font.unmapPrerenderedFont](Font.md#unmapprerenderedfont)

---

### unmapPrerenderedFont

Method

**Description**

Unmaps a prerendered font

Removes the **prerendered font** mapping for the currently selected font name.

**See also:** [Font.mapPrerenderedFont](Font.md#mapprerenderedfont)

---

### addFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Font file name |

**Return value**

Array of the face names contained in the file.

**Description**

Adds a font to the font system.

---

### registerFontFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `storage` | `&nbsp;` | Font file name |
| `family` | `&nbsp;` | Font name to register (if omitted, the font is loaded immediately) |

**Return value**

Array of contained face names if family is omitted; void if it is given

**Description**

Registers a font (supports deferred registration).

If `family` is omitted, the font file is loaded immediately, like `addFont`,
and an array of the contained face names is returned.

If `family` is given, **only the name is registered, without opening the file**
(deferred registration, equivalent to one entry in `fonts.json`). The actual file
is loaded when the name is first used. Use this to register large fonts
without affecting startup time.

---

### queryFonts

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `query` | `&nbsp;` | Dictionary of search criteria (optional) |

**Return value**

Array of matching font information (dictionaries)

**Description**

Searches registered fonts with rich criteria.

From fonts declared in `fonts.json` and fonts registered at runtime with `addFont`/`registerFontFile`,
returns the faces matching the criteria in ranked order (best match first).
All criteria are optional; omitted items impose no constraint.
If the argument itself is omitted, all registered fonts are returned.

+ `name` : font name (family / alias / fullName / PostScript name)
+ `weight` : weight (100 to 900; 400 = Regular / 700 = Bold)
+ `slant` : 0 = normal, 1 = italic, 2 = oblique
+ `italic` : true for italic (shorthand for slant)
+ `script` : ISO 15924 script tag (e.g. "Jpan" "Hans" "Zsye")
+ `containsText` : must contain all code points of this string
+ `monospace` : whether it is monospaced
+ `color` : whether it is a color emoji font

Each element of the returned array is a dictionary in the same form as `getFontInfo` returns.

---

### getFontInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | Font name or storage path |

**Return value**

Metadata dictionary (void if it cannot be resolved)

**Description**

Gets font metadata.

Resolves a font name (declared name or actual SFNT name) or a storage path,
and returns a dictionary of SFNT metadata. Returns void if it cannot be resolved.

Dictionary members:
+ `key` : font key (storage path etc.)
+ `faceIndex` : face number within a TTC
+ `family` / `subfamily` / `fullName` / `postScriptName` : name information
+ `weight` : 100 to 900
+ `slant` : 0 = normal, 1 = italic, 2 = oblique
+ `bold` / `color` / `monospace` / `scalable` : attributes (0/1)

For variable fonts the following are also included (omitted for non-variable fonts):
+ `axes` : array of variable axes (same form as [getVarAxes](#getvaraxes))
+ `namedInstances` : array of fvar named instances
`%[ name : "SemiBold", coords : %[ wght : 600, ... ] ]`

(`queryFonts` does not return axis information, to keep its property of judging by declared values without opening fonts.
Get axes with this method or getVarAxes.)

---

### getVarAxes

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | Font name or storage path |

**Return value**

Array of variable axes (void if it cannot be resolved)

**Description**

Gets the list of variable axes of a variable font.

Resolves a font name (declared name or actual SFNT name) or a storage path, and returns the fvar
variable axes as an array. Each element is a dictionary like
`%[ tag : "wght", name : "Weight", min : 300, default : 400, max : 700 ]`.
Returns an empty array if the font is not a variable font, and void if it cannot be resolved.

```tjs
var axes = Font.getVarAxes("MyFont");
for (var i = 0; i < axes.count; i++)
Debug.message(axes[i].tag + ": " + axes[i].min + ".." + axes[i].max);
```

---

### setDefaultVariations

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | Font name or storage path (same notation as the face, without the suffix) |
| `axes` | `&nbsp;` | Default axes ("tag=val,..." form; void or an empty string removes the registration) |

**Description**

Registers default axes for a variable font (class method).

Registers default variable axes, per font name, that are filled in when no axes are specified explicitly.
`axes` is in the form `"wght=300,wdth=87.5"`. void or an empty string removes the registration.

When a variable font is referenced without wght, the default is equivalent to wght=400
(the same rule as the CSS font-weight default; fonts whose default fvar instance is not Regular
are also shown as Regular when nothing is specified). This registration takes precedence over that,
and the `#tag=val` suffix / [variations](#variations) /
[weight](#weight) / axes declared in fonts.json take precedence over this registration.

```tjs
Font.setDefaultVariations("Noto Sans JP", "wght=350");  // 無指定を少し細く
Font.setDefaultVariations("Noto Sans JP", void);        // 解除 (=400 に戻る)
```

---

### getDefaultVariations

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | Font name or storage path |

**Return value**

Registered default axes string (empty string if none)

**Description**

Gets the current value registered with setDefaultVariations (class method).

---
