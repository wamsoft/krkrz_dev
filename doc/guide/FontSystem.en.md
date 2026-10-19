---
source_hash: 99c457dfb9a2
---

# Font System

This is a comprehensive guide to fonts in Kirikiri Z (registration, name resolution, drawing, and search).
It covers everything from preparing fonts and registering them to choosing between the various APIs.

## Overview

```
  Font files (.ttf/.otf/.ttc)
    │  (1) Embedded in exe (resource/)   (2) External in data + fonts.json (declared, lazy)
    │  (3) Runtime registration          (4) System fonts (Windows GDI)
    │      (Font.addFont, etc.)
    ▼
  ┌──────────────────────────────────────────────────┐
  │ FontSystem (name → storage mapping, lazy loading) │←─ fonts.json
  │ FontStream (shared in-memory buffer / 1 per font) │
  └───────────────┬──────────────────────────────────┘
                  ▼
  ┌──────────────────────────────────────────────────┐
  │ glyphware (unified font engine:                   │
  │  FreeType + HarfBuzz + BiDi / registry, search)   │
  └───┬───────────────┬───────────────┬──────────────┘
      ▼               ▼               ▼
  Layer.drawText   Layer.draw     ThorVG text
  (3 switchable    GlyphwareText  (Elements UI /
   rasterizers)    (shaping)       layerExVector)
```

- Font byte data is loaded **only once per font into a shared `FontStream`
  buffer**, and drawText, the Elements UI, layerExVector, and plugins all share
  the same buffer (fonts inside XP3 are supported; kept in memory).
- Glyph generation, shaping, and metadata search are consolidated in the unified
  font engine **glyphware**. The traditional GDI / FreeType rasterizers also
  remain as is for compatibility.

## Rasterizers

The engine that creates the character images for `Layer.drawText` can be switched
with [Font.rasterizer](../reference/Font.md#rasterizer) (a static property).

| Value | Native Windows build (WINVER) | SDL build and others |
|---|---|---|
| 0 | FreeType | FreeType **(default)** |
| 1 | GDI **(default)** | glyphware |
| 2 | glyphware | - |

- The defaults remain backward compatible (WINVER = GDI / others = FreeType).
- The **glyphware rasterizer** keeps layout compatibility with the classic ones
  (cell advance, shadow, outline, underline/strikethrough, VS15/16, etc.) while
  supporting fallback chains, color emoji, and synthetic bold/italic. Known
  difference: it always draws with anti-aliasing even when anti-aliasing is
  turned off (`font.hinting` / `font.antialiased` are ignored).

## Preparing and Registering Fonts

### (1) Embedded in the exe (resource/)

`.ttf/.otf` files placed in the engine's `resource/` folder are embedded into the
executable at build time and are available from startup. This is not something
the game adds to; it is where the engine's default fonts live. Embedded fonts can
also be accessed with the storage name `resource://./filename`.

**By default, only Roboto (Latin) and elements_basic (Elements icons) are
embedded.** Japanese (Noto Sans JP, 4.3 MB) and emoji (Noto Emoji, 1.9 MB) make up
most of the executable size, so they are not embedded by default. For Japanese,
either declare a font in `fonts.json` on the game side ((2)) or use OS fonts ((4)).
To embed them as before, pass `-DKRKRZ_EMBED_BUNDLED_FONTS=ON` at build time
(the executable grows by about 6.2 MB). To exclude arbitrary files, use
`-DKRKRZ_RESOURCE_EXCLUDE="filename;filename"`.

The demos bundled with the engine (`src/core/data`) put these two fonts in
`data/fonts/` and declare them in `fonts.json`. They serve as an example for using
the same fonts in a game.

### (2) External in data + fonts.json (recommended)

Put large fonts (color emoji, CJK variants, etc.) in the data folder and
**declare them in `fonts.json`**. Only the names are registered at startup, and
the actual files are **loaded lazily on first use**, so startup time and memory
are not affected.

```json
{
  "version": 1,
  "fonts": [
    { "file": "fonts/notocoloremoji.ttf",
      "family": "Noto Color Emoji",
      "subfamily": "Regular",
      "aliases": ["Noto Color Emoji Regular"],
      "weight": 400,
      "scripts": ["Zsye"],
      "flags": ["emoji", "color"],
      "ranges": [[9728, 9983], [126976, 129791]] }
  ]
}
```

- Put `fonts.json` **directly under the data folder (project root)**.
- Everything except `file` is optional. You can declare `subfamily` / `fullName` /
  `postScriptName` / `weight` (100-900) / `width` (1-9) / `italic` / `faceIndex` /
  `languages` / `aliases` / `flags` (`emoji` `color` `monospace`) / `ranges`
  (covered code point ranges).
- For **variable fonts**, you can declare "name = specific axis settings" with
  `instance` (an fvar named instance name) or `axes` (axis values written
  directly). The same file can be declared multiple times with different names
  and axes (see the "Variable Fonts" section below).

```json
{ "file": "myfont.ttf", "family": "MyFont SemiBold", "instance": "SemiBold" }
{ "file": "myfont.ttf", "family": "MyFont Narrow",   "axes": { "wdth": 75 } }
```
- The declared `scripts` / `ranges` / styles are used by [Font.queryFonts](../reference/Font.md#queryfonts)
  for searching **without opening the font files**.
- It can be generated automatically with the **generator tool** (requires `pip install fonttools`):

```
python tools/fontgen/gen_fonts_json.py \
    --fonts-dir <データ>/fonts --root <データ> --out <データ>/fonts.json
```

The generator sets family to the pure family name and outputs the classic
rasterizer's face name convention ("family subfamily" concatenated, e.g. "Noto
Color Emoji Regular") to `aliases`, so either name resolves.

Bundled example: in addition to Noto Color Emoji, the core demo's
`src/core/data/fonts` includes **Noto Sans Arabic / Noto Sans Hebrew** for RTL
(Arabic/Hebrew look the same on all platforms, including the SDL build). If you
get fonts for other scripts from the Noto family (https://notofonts.github.io/),
they will match the look of the embedded Noto Sans JP / Roboto
(candidates: Noto Sans Thai / Devanagari / KR / SC / TC, etc. For details, see
`src/core/data/fonts/README.md`).

### (3) Runtime Registration (Script)

- [Font.addFont](../reference/Font.md#addfont)`(storage)` — Loads and registers a
  font file immediately and returns an array of the face names it contains.
- [Font.registerFontFile](../reference/Font.md#registerfontfile)`(storage[, family])`
  — When `family` is specified, this is a **lazy registration that does not open
  the file** (equivalent to one fonts.json entry). If omitted, it loads
  immediately, like addFont.

```tjs
Font.addFont("mygame_font.ttf");                       // 即時ロード
Font.registerFontFile("fonts/big_cjk.ttf", "MyCJK");   // 遅延 (初回使用時に読む)
```

### (4) System Fonts (Fonts Installed in the OS)

You can use fonts installed in the OS **by font name alone**.

- **WINVER** uses GDI name resolution. On the glyphware paths (rasterizer=2 /
  drawShapedText / Elements) too, names such as `"メイリオ"` (Meiryo) and `"MS PGothic"`
  resolve as is, and the face index in TTC files is selected correctly. Embedded
  fonts registered with the `addFont` plugin can likewise be used by name.
- **The SDL build and others** register **only the name-to-file mapping** from the
  OS font list at startup, and read the actual file on first use (the same lazy
  loading as fonts.json). The list comes from DirectWrite on Windows and
  fontconfig on Linux (macOS / Android are not supported). If the same name exists
  in fonts.json or in a runtime registration, that one takes precedence. If you do
  not want the look of your distribution to depend on the runtime environment,
  disable this with the command-line option `-systemfont=no`.

## Font Name Conventions and Resolution Order

Names written in `Font.face` or `fontKey` (comma-separated to form a **fallback
chain**) are resolved in the following order:

1. **Names declared in fonts.json / registerFontFile** (family / aliases) → storage
2. **Storage paths** (ones that exist, such as `fonts/foo.ttf` or `resource://./…`)
3. **OS font names** (GDI on WINVER, including fonts registered with addFont; on
   the SDL build and others, the OS font list registered at startup)
4. Names that cannot be resolved fall back to the default face

### Default Font

When no font name is specified, the default font is the one given by the
command-line option `-deffont` if present; otherwise, **one that is actually
available** is chosen from candidates matching the runtime environment's language
(SDL build and others). In a Japanese environment, the candidates are Noto Sans JP
in `fonts.json`, followed by OS fonts such as Yu Gothic UI / Meiryo / MS Gothic /
Hiragino / IPA / Noto Sans CJK JP. If none were available at startup, the choice is
made again when a candidate name is later registered through `fonts.json` or
`Font.registerFontFile`. WINVER uses the GDI default font as before.

### Characters Missing from All Fonts

Characters that are not in any font of the fallback chain are drawn as
**U+FFFD (�)** from a font in the chain that has it. If no font has U+FFFD, `?` is
used (the bundled Roboto has U+FFFD). Invisible characters such as line breaks,
zero-width characters, and variation selectors draw nothing. This is common to
`Layer.drawText` (FreeType / glyphware rasterizers), the `drawShapedText` family,
vertical text, and Elements (the GDI rasterizer keeps GDI's own substitute display).

Note that classic (FreeType) face names are "family subfamily" concatenated (e.g.
"Noto Sans JP Regular"). The fonts.json generator outputs the concatenated name as
an alias, so usually either form works.

## Emoji

[Font.emojiMode](../reference/Font.md#emojimode) (0 = disabled / 1 = monochrome / 2 = color)
selects how emoji glyphs are handled.

- The color emoji font (default "Noto Color Emoji") is expected to be declared
  externally in fonts.json. If it is not present, it automatically falls back to
  the bundled monochrome emoji (Noto Emoji) (no tofu boxes).
- The default font names can be changed with `Font.emojiFaceName` / `Font.colorEmojiFaceName`.
- The default WINVER rasterizer (GDI) has no emoji glyphs, so use it with
  `Font.rasterizer = 0` (FreeType) or `= 2` (glyphware).
- The VS15 (text presentation) / VS16 (emoji presentation) variation selectors are supported.

## Font Search and Metadata

Registered fonts can be searched richly with [Font.queryFonts](../reference/Font.md#queryfonts)
(all conditions are optional; the result is an array of dictionaries in rank order):

```tjs
// カラー絵文字フォントを探す
var r = Font.queryFonts(%[ containsText : "😀", color : 1 ]);
// 日本語を収録した太字を探す
var r = Font.queryFonts(%[ containsText : "あ", weight : 700 ]);
```

The SFNT metadata of a single font can be obtained with [Font.getFontInfo](../reference/Font.md#getfontinfo)
(family / subfamily / weight / color, etc.). For information already declared in
fonts.json, it responds without opening the font.

## Variable Fonts (Variation Axes)

For fonts with variation axes (fvar), you can specify the axes from TJS font
parameters. They take effect **only on the glyphware path** — the
[Layer.drawShapedText](../reference/Layer.md#drawshapedtext) family (always) and
[Layer.drawText](../reference/Layer.md#drawtext) when
[Font.rasterizer](../reference/Font.md#rasterizer) = 2 — and are ignored by the old
FreeType / GDI rasterizers (a warning is shown once after startup).

```tjs
Font.rasterizer = 2;                     // drawText で使う場合
layer.font.weight = 700;                 // wght 軸 (100-900、void で解除)
layer.font.variations = "wdth=87.5";     // 汎用軸指定 (複数は "wght=700,wdth=75")
var axes = Font.getVarAxes("MyFont");    // 利用できる軸の一覧
Font.defaultUseVarStyle = true;          // bold/italic を軸で表現 (オプトイン)
```

- [Font.weight](../reference/Font.md#weight) acts as the `wght` axis; if `wght` is
  given explicitly in [Font.variations](../reference/Font.md#variations), that takes
  precedence. Only **axes with the same name that each face in the fallback chain
  actually has** are applied, so it is safe even with chains whose faces have
  different axes, such as a Japanese font + an emoji font.
- You can create "name = specific axis settings" with `instance` / `axes`
  declarations in `fonts.json` (see the fonts.json section above). Simply pointing
  to the name gives you the font with its axes applied, so scripts do not need to
  touch weight / variations.
- When [Font.defaultUseVarStyle](../reference/Font.md#defaultusevarstyle) is true,
  fonts that can express bold / italic with axes (wght=700 / slnt=-10 / ital=1) use
  the axes instead of synthetic bold / italic (default is false).
- Axes can be queried with [Font.getVarAxes](../reference/Font.md#getvaraxes) /
  [Font.getFontInfo](../reference/Font.md#getfontinfo) (`axes` /
  `namedInstances`).
- **`#tag=val` suffix notation**: appending `#tag=val[,tag=val...]` to a font name
  denotes an axis instance of the font that name refers to
  (e.g. `"MyFont#wght=700"`, `"MyFont#wght=700,wdth=75"`).
  It works uniformly in each element of the [Font.face](../reference/Font.md#face)
  fallback chain and in `"font"` of Elements screen JSON (both label and text_area;
  line wrapping is computed with the same instance). While `Font.variations`
  applies to the whole font (all faces in the chain), this applies **per element**
  of the chain.
- **The default when unspecified is equivalent to wght=400**: when a variable font
  is referenced without wght, it is displayed at wght=400, not at the fvar default
  instance (the same rule as the CSS font-weight default). Even VFs whose default
  is Thin (such as Noto VF) read as Regular when unspecified, with just one VF
  registered. To change the default, register it per name with
  [Font.setDefaultVariations](../reference/Font.md#setdefaultvariations) (explicit
  settings and fonts.json declarations always win).

## Multilingual Shaped Text Drawing (glyphware)

`Layer.drawText` still uses "per-character cell advance", but
[Layer.drawShapedText](../reference/Layer.md#drawshapedtext) performs full
multilingual single-line drawing with **HarfBuzz shaping + BiDi**:

- Arabic joining, ligatures, kerning, and right-to-left Hebrew/Arabic (BiDi)
- Per-code-point fallback chains (comma-separated Font.face)
- Color emoji, synthetic bold/italic, underline/strikethrough, rotation (angle)
- Drawing attributes are passed as a single [Font](../reference/Font.md) object
  (void = the layer's own font / a string = replace only the face)

[Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea) does
**simple wrapped drawing** into a rectangle. It supports explicit line breaks with
`\n`, word-based wrapping for English and similar languages, character-based
wrapping for Japanese (with simple line-start/line-end prohibition rules),
alignment (left/center/right), and line spacing adjustment.

Passing 0 or more to the `count` argument (common to drawShapedText /
drawShapedTextArea) draws only the first count "characters", which you can use for
typewriter display. These "characters" are **clusters** treated as one unit when
drawing (a ligature, combining sequence, or emoji ZWJ sequence counts as 1), and
the total is obtained with [Layer.shapedTextCount](../reference/Layer.md#shapedtextcount).
Because the whole text is shaped and wrapped before only the leading part is drawn,
glyphs and wrap positions do not change (reflow) partway through.

Measurement is done with [Layer.measureShapedText](../reference/Layer.md#measureshapedtext)
(it returns the ink bounds, ascent/descent, and the cluster count).

Working sample: in the core demo gallery (`src/core/data`), the
"Multilingual shaping (glyphware)" scene shows examples of Arabic/Hebrew (RTL),
mixed BiDi, mixed emoji, measurement, wrapping within a rectangle, and typewriter
display (automatic playback of a mixed RTL sentence — RTL runs appear one cluster
at a time in logical order).

## Vertical Text (Japanese Vertical Writing)

[Layer.drawVerticalTextArea](../reference/Layer.md#drawverticaltextarea) flows
body text into a rectangle as **vertical text**. It is a separate path from the
horizontal `drawShapedTextArea` and lays out text according to the spacing tables
of the Japanese layout requirements (JLReq):

- Japanese characters are set upright and Latin letters/digits are rotated sideways
  (`orientation` can change this to all upright / all sideways)
- It uses vertical glyphs (`vert` / `vrt2`) and vertical advances (`vmtx` / `VORG`),
  so brackets, the long vowel mark, and punctuation use vertical glyph forms
- Compression of punctuation (periods, commas, brackets) and spacing between
  Japanese and Latin text
- Line-start/line-end prohibition rules, pushing in / pushing out, justification
  at line end, and hanging punctuation (optional)

The column length is the rectangle's height, and the column advance is "font size
+ lineSpacing". The default is right to left (the first column is at the right edge
of the rectangle); `verticalLr` makes it left to right. Columns that do not fit in
the rectangle are not drawn. Font specification (the `font` argument) and color
handling are the same as `drawShapedText`, so the same Font object gives a
consistent look with horizontal text.

```tjs
var opt = %[ "hanging" => true, "letterSpacing" => 0.05 ];
// (x, y, width, height, text, color, font, count, lineSpacing, options)
var r = layer.drawVerticalTextArea(20, 20, 400, 560, text, 0x000000,
                                   font, -1, 6, opt);
// r.lines = 組んだ列数 / r.width = 使った幅 / r.count = 描いたクラスタ数
```

For all `options` keys and their defaults, see
[Layer.drawVerticalTextArea](../reference/Layer.md#drawverticaltextarea)
(`orientation` / `verticalLr` / `punctuation` / `latinGap` /
`hanging` / `justify` / `letterSpacing`).

`count` is for typewriter display. As with horizontal text, the limit is applied
**after line breaking has been finalized for the whole text**, so there is no
reflow partway through. However, the unit counted is "drawn characters", and spaces
between Latin words are not counted, so it may not match the value of
[Layer.shapedTextCount](../reference/Layer.md#shapedtextcount). Use `totalCount` in
the return value for the total.

To get only the number of columns or the required width without drawing, use
[Layer.measureVerticalTextArea](../reference/Layer.md#measureverticaltextarea)
(the same arguments minus x / y / color; the return value is the same).

**Not supported**: ruby, tate-chu-yoko (horizontal-in-vertical), emphasis dots,
warichu (inline notes), character-width fitting, multi-column layout, underline /
strikethrough, and [Font.angle](../reference/Font.md#angle). Currently only body
text layout is supported.

Working sample: in the core demo gallery (`src/core/data`), the
"Vertical text (drawVerticalTextArea)" scene shows examples of flowing body text,
toggling `options` keys (hanging / justification / punctuation compression /
column direction / letter spacing), mixed Japanese/Latin layout with `orientation`,
a side-by-side comparison with the same text set horizontally, and typewriter
display (count limit).

## Fonts in the UI (Elements) and layerExVector

- Text in **Elements dialogs** ([Dialogs](ElementsDialog.md)) is drawn with
  glyphware. The embedded font (Roboto by default) is automatically registered as
  the theme font, followed by **the engine's default font** (see "Default Font"
  above: a font declared in fonts.json, an OS Japanese font, or the GDI default on
  WINVER) as a last resort. This is why Japanese appears even in configurations
  that bundle no fonts.
  Register additional fonts with
  `ElementsDialog.registerFont(family, storage[, weight, slant, stretch])` /
  `ElementsDialog.registerFontDir(dir)`. You can pass storage paths (including
  inside XP3 and `resource://`) as is. `registerFontDir` returns **the number of
  fonts registered**, so `if (ElementsDialog.registerFontDir(dir) == 0) { ... }`
  catches the "no fonts at all after packaging" accident (the engine also logs a
  warning when the count is 0). When pointing to fonts packed in an XP3,
  **specify the archive explicitly**, as in `"data.xp3>font/"`
  (mounting with `addAutoPath` is for file lookup and cannot enumerate directories).
  Passing an OS path (`"D:/game/font/"`) as is yields 0 fonts. To switch fonts
  (JP/TC/SC, etc.) automatically per display language in a multilingual UI, use
  [ElementsDialog.fontLanguages](../reference/ElementsDialog.md#fontlanguages)
  (language-linked font substitution)
  (see the "言語連動フォント置換" (language-linked font substitution) section of [Dialogs](ElementsDialog.md)).
- Flowing text into a rectangle also **shares the wrapping logic**. The dialog's
  `text_area` widget goes through the same wrapping, line-start/line-end
  prohibition rules, and cluster-based character advance as `drawShapedTextArea`
  above, so for the same text and the same width, **line breaks match** between
  layer drawing and Elements
  (the older `text_box` keeps naive wrapping for compatibility).
- The **richtext plugin** ([RichText](../reference/RichText.md)) uses minikin for
  layout, but obtaining font data and rasterizing glyphs go through the engine's
  glyphware. Because it shares faces and font bytes with the engine, it gives
  **the same fonts and the same look** as `Layer.drawText` and Elements ( only when
  variable font axes are used is a dedicated face opened, so as not to disturb the
  state of the shared face ).
- The **layerExVector plugin** (`GdiPlus.loadFont(storage, name)`) also shares the
  same engine. You can specify fonts embedded in the engine, such as
  `resource://./roboto-regular.ttf`, or names declared in fonts.json.
- Every path uses a single shared FontStream buffer for the same font, so using
  the same font in several places does not increase memory.

## Use from Plugins (C++)

Font service APIs (`TVPCreateFontStream` / `TVPFontAcquireFace` /
`TVPFontShapeLine` / `TVPFontQueryFaces`, etc.) are exposed in tp_stub, so plugins
can also use the shared buffer, glyph supply, shaping, and search. For details,
see `src/core/doc/FontEngine.md` (internal implementation notes) in the engine
repository.

## Troubleshooting

- **Characters appear as � (U+FFFD)** — No font has that character. For Japanese,
  declare a Japanese font in fonts.json or use OS fonts (check that you have not
  passed `-systemfont=no`, and note that OS fonts are not available in the SDL
  build on macOS / Android).
- **A font name is specified but the default font is used** — The name is not
  registered. Check whether `Font.getFontInfo(name)` returns void, and use a name or
  alias declared in fonts.json, or a face name returned by `Font.addFont`.
- **Color emoji appear in black and white** — If the color emoji font is not
  present (not declared in fonts.json), it falls back to monochrome. You can check
  what is available with `Font.queryFonts(%[color:1])`.
- **Emoji do not appear on WINVER** — The default rasterizer (GDI) does not support
  emoji. Set `Font.rasterizer = 2` (or 0).
- **The width of "MS Gothic" differs between paths** — FreeType name resolution
  can turn an English name in a TTC into a different face (PGothic). Using the
  actual family name ("ＭＳ ゴシック", etc.) makes all paths match.

## Related Documents

- Reference: [Font](../reference/Font.md) / [Layer](../reference/Layer.md)
- [Dialogs (Elements)](ElementsDialog.md)
- Pre-rendered fonts: [FontMaker](FontMaker.md)
- Engine internals (for developers): `src/core/doc/FontEngine.md`
