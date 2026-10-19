# GdiPlus.Appearance

This class is extended by several plugins.

## Plugin extension: layerExDraw

Drawing appearance

Think of it as Illustrator's Appearance.
You can specify multiple brushes (fills) and pens (strokes) for a drawing.
Items added earlier are placed underneath.

### Members

#### Constructors

- [Appearance](#appearance)

#### Methods

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

Constructor

**Description**

Constructor

---

### clear

Method

**Description**

Clears the information

---

### addBrush

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB color or brush definition (dictionary) |
| `ox` | `&nbsp;` | Display offset X |
| `oy` | `&nbsp;` | Display offset Y |

**Description**

Adds a brush

Brush definition
Basics: a point is an array [x,y] or a dictionary %[x:x, y:y]
A rectangle is an array [x,y,width,height] or a dictionary %[x:x, y:y, width:w, height:h]
A color is a 32-bit ARGB integer
For the parameters, study the GDI+ documentation.

type: brush type, specified with BrushType

For BrushTypeSolidColor (same as specifying an ARGB color directly)
color: color (white if omitted)

For BrushTypeHatchFill
hatchStyle: hatch style (HatchStyleHorizontal if omitted)
foreColor: foreground color (white if omitted)
backColor: background color (black if omitted)

For BrushTypeTextureFill
image: image
wrapMode: wrap pattern (WrapModeTile if omitted)
dstRect: texture area rectangle (whole image if omitted)

For BrushTypePathGradient
points: array of points
centerColor: center color
centerPoint: center point
focusScale: focus scales, [xScale,yScale] or %[xScale:, yScale:]
surroundColors: surround colors, an array of colors
---- The following also apply to BrushTypeLinearGradient
blend: blend factors, a numeric array [blendFactors, blendPositions] or a dictionary
blendBellShape: blend shape (bell-shaped) [focus, scale]
blendTriangularShape: blend shape (triangular) [focus, scale]
gammaCorrection: whether to enable gamma correction, true/false
interpolationColors: [presetColors (array of colors), blendPositions (numeric array)]

For BrushTypeLinearGradient
Common
color1: start color
color2: end color
wrapMode: wrap pattern (WrapModeTile if omitted)
Point form
point1: start point
point2: end point
Note: the angle appears to be determined automatically
Rectangle form
rect: rectangle; the top-left is the start and the bottom-right is the end
angle: angle (only valid in rectangle form)
isAngleScalable (whether the angle is scalable)
mode: mode (LinearGradientModeHorizontal if omitted); effective when angle is not specified

---

### addPen

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB color or brush definition (dictionary) |
| `widthOrOption` | `&nbsp;` | Pen width or pen definition (dictionary) |
| `ox` | `&nbsp;` | Display offset X |
| `oy` | `&nbsp;` | Display offset Y |

**Description**

Adds a pen

Pen definition: if widthOrOption is a dictionary, it is a detailed definition.
For the parameters, study the GDI+ documentation.

width: pen width
alignment: alignment; PenAlignmentCenter if omitted
compoundArray: compound array, a numeric array
dashCap: cap style of dashes; DashCapFlat if omitted
dashOffset: dash offset; 0 if omitted
dashStyle: dash style. An array (numeric) gives a user-defined pattern. The default is DasyStyleSolid
startCap: cap style at the start. LineCapFlat if omitted; AdjustableArrowCap if a dictionary
endCap: cap style at the end. LineCapFlat if omitted; AdjustableArrowCap if a dictionary
lineJoin: join style; LineJoinMiter if omitted
miterLimit: miter limit (number)

AdjustableArrowCap: for when LineCapArrowAnchor is not enough
width (arrow width), height (arrow height), and filled (true for a triangle, false for a three-pronged arrow) can be specified

---

## Plugin extension: layerExVector

Drawing appearance

Think of it as Illustrator's Appearance.
You can specify multiple brushes (fills) and pens (strokes) for a drawing.
Items added earlier are placed underneath.

### Members

#### Constructors

- [Appearance](#appearance)

#### Methods

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

Constructor

**Description**

Constructor

---

### clear

Method

**Description**

Clears the information

---

### addBrush

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB color or brush definition (dictionary) |
| `ox` | `0` | Display offset X |
| `oy` | `0` | Display offset Y |

**Description**

Adds a brush

Brush definition
Basics: a point is an array [x,y] or a dictionary %[x:x, y:y]
A color is a 32-bit ARGB integer

type: brush type, specified with BrushType

For BrushTypeSolidColor (same as specifying an ARGB color directly)
color: color (white if omitted)

For BrushTypePathGradient (approximated with a RadialGradient)
centerPoint: center point
centerColor: center color
radius: radius (100 if omitted)

For BrushTypeLinearGradient
point1: start point
point2: end point
color1: start color
color2: end color

---

### addPen

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB color or brush definition (dictionary) |
| `widthOrOption` | `1.0` | Pen width or pen definition (dictionary) |
| `ox` | `0` | Display offset X |
| `oy` | `0` | Display offset Y |

**Description**

Adds a pen

Pen definition: if widthOrOption is a dictionary, it is a detailed definition.

width: pen width
startCap / endCap: cap style, specified with a LineCap constant. LineCapFlat if omitted
lineJoin: join style, specified with a LineJoin constant. LineJoinBevel if omitted
miterLimit: miter limit (number)
dashStyle: dash pattern, specified as a numeric array
dashOffset: dash offset; 0 if omitted

---
