# RichText.TextureAtlas

Texture atlas class

Pre-renders glyphs into a layer (texture) and transfers them in display order
using an array of copy rectangles.
Identical glyphs are deduplicated, making efficient use of the texture.

The layer passed to the constructor is used as the texture.

Workflow:
1. Create the atlas with a layer
2. Add glyphs with addLayout / addParagraphLayout / addStyledLayout
3. Write them to the texture with commit()
4. Get the array of copy rectangles with getCopyRects()
5. Copy from the atlas layer to the destination according to the copy rectangles

Example:
var atlasLayer = new Layer(window, window.primaryLayer);
atlasLayer.setImageSize(1024, 1024);
var atlas = new RichText.TextureAtlas(atlasLayer);

var sl = new RichText.StyledLayout();
sl.layout(text, 400, 300, RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);
atlas.addStyledLayout(sl);
atlas.commit();

var rects = atlas.getCopyRects(sl, 10, 10);
for (var i = 0; i < rects.count; i++) {
var r = rects[i];
// r.srcX, r.srcY, r.srcWidth, r.srcHeight: アトラスレイヤー内のソース矩形
// r.dstX, r.dstY: 表示先の座標
// r.displayIndex: 表示順序
targetLayer.copyRect(r.dstX, r.dstY, atlasLayer,
r.srcX, r.srcY, r.srcWidth, r.srcHeight);
}

## Members

### Constructors

- [TextureAtlas](#textureatlas)

### Methods

- [clear](#clear)
- [addLayout](#addlayout)
- [addParagraphLayout](#addparagraphlayout)
- [addStyledLayout](#addstyledlayout)
- [commit](#commit)
- [getCopyRects](#getcopyrects)

---

### TextureAtlas

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Layer to use as the texture |

**Description**

Constructor

---

### clear

Method

**Description**

Clears the atlas (removes all glyphs)

---

### addLayout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layout` | `&nbsp;` | RichText.Layout object |
| `appearance` | `&nbsp;` | RichText.Appearance object |

**Return value**

true on success

**Description**

Adds the glyphs of a TextLayout to the atlas

---

### addParagraphLayout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `paraLayout` | `&nbsp;` | RichText.ParagraphLayout object |
| `style` | `&nbsp;` | RichText.Style object |
| `appearance` | `&nbsp;` | RichText.Appearance object |

**Return value**

true on success

**Description**

Adds the glyphs of a ParagraphLayout to the atlas

---

### addStyledLayout

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `styledLayout` | `&nbsp;` | RichText.StyledLayout object |

**Return value**

true on success

**Description**

Adds the glyphs of a StyledLayout to the atlas

---

### commit

Method

**Description**

Writes the atlas to the texture (layer)

Renders the glyphs added with addLayout / addParagraphLayout / addStyledLayout
into the layer.

---

### getCopyRects

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `/* overloaded */` | `&nbsp;` |  |

**Return value**

Array of copy rectangles. Each element is a dictionary:
%[srcX, srcY, srcWidth, srcHeight, dstX, dstY, displayIndex, charIndex, delay, linkIndex]
charIndex: character position in the source text
delay: display timing (ms; omitted if not set)
linkIndex: link number (omitted if not set)

**Description**

Gets the array of copy rectangles for display

There are three overloads:

1) getCopyRects(layout, x, y, appearance, maxChars=-1)
- layout: RichText.Layout
- x, y: drawing position
- appearance: RichText.Appearance
- maxChars: maximum number of characters (-1 for all)

2) getCopyRects(paraLayout, x, y, width, height, hAlign, vAlign, style, appearance, maxChars=-1)
- paraLayout: RichText.ParagraphLayout
- x, y, width, height: drawing area
- hAlign, vAlign: alignment
- style: RichText.Style
- appearance: RichText.Appearance
- maxChars: maximum number of characters (-1 for all)

3) getCopyRects(styledLayout, x, y, maxChars=-1)
- styledLayout: RichText.StyledLayout
- x, y: drawing position
- maxChars: maximum number of characters (-1 for all)

---
