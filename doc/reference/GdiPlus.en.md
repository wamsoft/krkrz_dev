# GdiPlus

This class is extended by several plugins.

## Plugin extension: layerExDraw

Manual in pseudo-code

### Members

#### Methods

- [addPrivateFont](#addprivatefont)
- [getFontList](#getfontlist)

#### Constants

- [Ok](#ok)
- [GenericError](#genericerror)
- [InvalidParameter](#invalidparameter)
- [OutOfMemory](#outofmemory)
- [ObjectBusy](#objectbusy)
- [InsufficientBuffer](#insufficientbuffer)
- [NotImplemented](#notimplemented)
- [Win32Error](#win32error)
- [WrongState](#wrongstate)
- [Aborted](#aborted)
- [FileNotFound](#filenotfound)
- [ValueOverflow](#valueoverflow)
- [AccessDenied](#accessdenied)
- [UnknownImageFormat](#unknownimageformat)
- [FontFamilyNotFound](#fontfamilynotfound)
- [FontStyleNotFound](#fontstylenotfound)
- [NotTrueTypeFont](#nottruetypefont)
- [UnsupportedGdiplusVersion](#unsupportedgdiplusversion)
- [GdiplusNotInitialized](#gdiplusnotinitialized)
- [PropertyNotFound](#propertynotfound)
- [PropertyNotSupported](#propertynotsupported)
- [ProfileNotFound](#profilenotfound)
- [FontStyleRegular](#fontstyleregular)
- [FontStyleBold](#fontstylebold)
- [FontStyleItalic](#fontstyleitalic)
- [FontStyleBoldItalic](#fontstylebolditalic)
- [FontStyleUnderline](#fontstyleunderline)
- [FontStyleStrikeout](#fontstylestrikeout)
- [BrushTypeSolidColor](#brushtypesolidcolor)
- [BrushTypeHatchFill](#brushtypehatchfill)
- [BrushTypeTextureFill](#brushtypetexturefill)
- [BrushTypePathGradient](#brushtypepathgradient)
- [BrushTypeLinearGradient](#brushtypelineargradient)
- [DashCapFlat](#dashcapflat)
- [DashCapRound](#dashcapround)
- [DashCapTriangle](#dashcaptriangle)
- [DashStyleSolid](#dashstylesolid)
- [DashStyleDash](#dashstyledash)
- [DashStyleDot](#dashstyledot)
- [DashStyleDashDot](#dashstyledashdot)
- [DashStyleDashDotDot](#dashstyledashdotdot)
- [HatchStyleHorizontal](#hatchstylehorizontal)
- [HatchStyleVertical](#hatchstylevertical)
- [HatchStyleForwardDiagonal](#hatchstyleforwarddiagonal)
- [HatchStyleBackwardDiagonal](#hatchstylebackwarddiagonal)
- [HatchStyleCross](#hatchstylecross)
- [HatchStyleDiagonalCross](#hatchstylediagonalcross)
- [HatchStyle05Percent](#hatchstyle05percent)
- [HatchStyle10Percent](#hatchstyle10percent)
- [HatchStyle20Percent](#hatchstyle20percent)
- [HatchStyle25Percent](#hatchstyle25percent)
- [HatchStyle30Percent](#hatchstyle30percent)
- [HatchStyle40Percent](#hatchstyle40percent)
- [HatchStyle50Percent](#hatchstyle50percent)
- [HatchStyle60Percent](#hatchstyle60percent)
- [HatchStyle70Percent](#hatchstyle70percent)
- [HatchStyle75Percent](#hatchstyle75percent)
- [HatchStyle80Percent](#hatchstyle80percent)
- [HatchStyle90Percent](#hatchstyle90percent)
- [HatchStyleLightDownwardDiagonal](#hatchstylelightdownwarddiagonal)
- [HatchStyleLightUpwardDiagonal](#hatchstylelightupwarddiagonal)
- [HatchStyleDarkDownwardDiagonal](#hatchstyledarkdownwarddiagonal)
- [HatchStyleDarkUpwardDiagonal](#hatchstyledarkupwarddiagonal)
- [HatchStyleWideDownwardDiagonal](#hatchstylewidedownwarddiagonal)
- [HatchStyleWideUpwardDiagonal](#hatchstylewideupwarddiagonal)
- [HatchStyleLightVertical](#hatchstylelightvertical)
- [HatchStyleLightHorizontal](#hatchstylelighthorizontal)
- [HatchStyleNarrowVertical](#hatchstylenarrowvertical)
- [HatchStyleNarrowHorizontal](#hatchstylenarrowhorizontal)
- [HatchStyleDarkVertical](#hatchstyledarkvertical)
- [HatchStyleDarkHorizontal](#hatchstyledarkhorizontal)
- [HatchStyleDashedDownwardDiagonal](#hatchstyledasheddownwarddiagonal)
- [HatchStyleDashedUpwardDiagonal](#hatchstyledashedupwarddiagonal)
- [HatchStyleDashedHorizontal](#hatchstyledashedhorizontal)
- [HatchStyleDashedVertical](#hatchstyledashedvertical)
- [HatchStyleSmallConfetti](#hatchstylesmallconfetti)
- [HatchStyleLargeConfetti](#hatchstylelargeconfetti)
- [HatchStyleZigZag](#hatchstylezigzag)
- [HatchStyleWave](#hatchstylewave)
- [HatchStyleDiagonalBrick](#hatchstylediagonalbrick)
- [HatchStyleHorizontalBrick](#hatchstylehorizontalbrick)
- [HatchStyleWeave](#hatchstyleweave)
- [HatchStylePlaid](#hatchstyleplaid)
- [HatchStyleDivot](#hatchstyledivot)
- [HatchStyleDottedGrid](#hatchstyledottedgrid)
- [HatchStyleDottedDiamond](#hatchstyledotteddiamond)
- [HatchStyleShingle](#hatchstyleshingle)
- [HatchStyleTrellis](#hatchstyletrellis)
- [HatchStyleSphere](#hatchstylesphere)
- [HatchStyleSmallGrid](#hatchstylesmallgrid)
- [HatchStyleSmallCheckerBoard](#hatchstylesmallcheckerboard)
- [HatchStyleLargeCheckerBoard](#hatchstylelargecheckerboard)
- [HatchStyleOutlinedDiamond](#hatchstyleoutlineddiamond)
- [HatchStyleSolidDiamond](#hatchstylesoliddiamond)
- [HatchStyleTotal](#hatchstyletotal)
- [HatchStyleLargeGrid](#hatchstylelargegrid)
- [HatchStyleMin](#hatchstylemin)
- [HatchStyleMax](#hatchstylemax)
- [LinearGradientModeHorizontal](#lineargradientmodehorizontal)
- [LinearGradientModeVertical](#lineargradientmodevertical)
- [LinearGradientModeForwardDiagonal](#lineargradientmodeforwarddiagonal)
- [LinearGradientModeBackwardDiagonal](#lineargradientmodebackwarddiagonal)
- [LineCapFlat](#linecapflat)
- [LineCapSquare](#linecapsquare)
- [LineCapRound](#linecapround)
- [LineCapTriangle](#linecaptriangle)
- [LineCapNoAnchor](#linecapnoanchor)
- [LineCapSquareAnchor](#linecapsquareanchor)
- [LineCapRoundAnchor](#linecaproundanchor)
- [LineCapDiamondAnchor](#linecapdiamondanchor)
- [LineCapArrowAnchor](#linecaparrowanchor)
- [LineJoinMiter](#linejoinmiter)
- [LineJoinBevel](#linejoinbevel)
- [LineJoinRound](#linejoinround)
- [LineJoinMiterClipped](#linejoinmiterclipped)
- [PenAlignmentCenter](#penalignmentcenter)
- [PenAlignmentInset](#penalignmentinset)
- [WrapModeTile](#wrapmodetile)
- [WrapModeTileFlipX](#wrapmodetileflipx)
- [WrapModeTileFlipY](#wrapmodetileflipy)
- [WrapModeTileFlipXY](#wrapmodetileflipxy)
- [WrapModeClamp](#wrapmodeclamp)
- [MatrixOrderPrepend](#matrixorderprepend)
- [MatrixOrderAppend](#matrixorderappend)
- [ImageTypeUnknown](#imagetypeunknown)
- [ImageTypeBitmap](#imagetypebitmap)
- [ImageTypeMetafile](#imagetypemetafile)
- [RotateNoneFlipNone](#rotatenoneflipnone)
- [Rotate90FlipNone](#rotate90flipnone)
- [Rotate180FlipNone](#rotate180flipnone)
- [Rotate270FlipNone](#rotate270flipnone)
- [RotateNoneFlipX](#rotatenoneflipx)
- [Rotate90FlipX](#rotate90flipx)
- [Rotate180FlipX](#rotate180flipx)
- [Rotate270FlipX](#rotate270flipx)
- [RotateNoneFlipY](#rotatenoneflipy)
- [Rotate90FlipY](#rotate90flipy)
- [Rotate180FlipY](#rotate180flipy)
- [Rotate270FlipY](#rotate270flipy)
- [RotateNoneFlipXY](#rotatenoneflipxy)
- [Rotate90FlipXY](#rotate90flipxy)
- [Rotate180FlipXY](#rotate180flipxy)
- [Rotate270FlipXY](#rotate270flipxy)
- [SmoothingModeInvalid](#smoothingmodeinvalid)
- [SmoothingModeDefault](#smoothingmodedefault)
- [SmoothingModeHighSpeed](#smoothingmodehighspeed)
- [SmoothingModeHighQuality](#smoothingmodehighquality)
- [SmoothingModeNone](#smoothingmodenone)
- [SmoothingModeAntiAlias](#smoothingmodeantialias)
- [TextRenderingHintSystemDefault](#textrenderinghintsystemdefault)
- [TextRenderingHintSingleBitPerPixelGridFit](#textrenderinghintsinglebitperpixelgridfit)
- [TextRenderingHintSingleBitPerPixel](#textrenderinghintsinglebitperpixel)
- [TextRenderingHintAntiAliasGridFit](#textrenderinghintantialiasgridfit)
- [TextRenderingHintAntiAlias](#textrenderinghintantialias)
- [TextRenderingHintClearTypeGridFit](#textrenderinghintcleartypegridfit)

---

### addPrivateFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fontFileName` | `&nbsp;` | Font file name |

**Description**

Adds a private font (static)

Adds an application-specific font.
Fonts inside Kirikiri archives can also be registered.

---

### getFontList

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `privateOnly` | `&nbsp;` | If true, only private fonts are returned |

**Description**

Gets the list of fonts

---

### Ok

Constant

Value: `0`

---

### GenericError

Constant

Value: `1`

---

### InvalidParameter

Constant

Value: `2`

---

### OutOfMemory

Constant

Value: `3`

---

### ObjectBusy

Constant

Value: `4`

---

### InsufficientBuffer

Constant

Value: `5`

---

### NotImplemented

Constant

Value: `6`

---

### Win32Error

Constant

Value: `7`

---

### WrongState

Constant

Value: `8`

---

### Aborted

Constant

Value: `9`

---

### FileNotFound

Constant

Value: `10`

---

### ValueOverflow

Constant

Value: `11`

---

### AccessDenied

Constant

Value: `12`

---

### UnknownImageFormat

Constant

Value: `13`

---

### FontFamilyNotFound

Constant

Value: `14`

---

### FontStyleNotFound

Constant

Value: `15`

---

### NotTrueTypeFont

Constant

Value: `16`

---

### UnsupportedGdiplusVersion

Constant

Value: `17`

---

### GdiplusNotInitialized

Constant

Value: `18`

---

### PropertyNotFound

Constant

Value: `19`

---

### PropertyNotSupported

Constant

Value: `20`

---

### ProfileNotFound

Constant

Value: `21`

---

### FontStyleRegular

Constant

Value: `0`

---

### FontStyleBold

Constant

Value: `1`

---

### FontStyleItalic

Constant

Value: `2`

---

### FontStyleBoldItalic

Constant

Value: `3`

---

### FontStyleUnderline

Constant

Value: `4`

---

### FontStyleStrikeout

Constant

Value: `8`

---

### BrushTypeSolidColor

Constant

Value: `0`

---

### BrushTypeHatchFill

Constant

Value: `1`

---

### BrushTypeTextureFill

Constant

Value: `2`

---

### BrushTypePathGradient

Constant

Value: `3`

---

### BrushTypeLinearGradient

Constant

Value: `4`

---

### DashCapFlat

Constant

Value: `0`

---

### DashCapRound

Constant

Value: `2`

---

### DashCapTriangle

Constant

Value: `3`

---

### DashStyleSolid

Constant

Value: `0`

---

### DashStyleDash

Constant

Value: `1`

---

### DashStyleDot

Constant

Value: `2`

---

### DashStyleDashDot

Constant

Value: `3`

---

### DashStyleDashDotDot

Constant

Value: `4`

---

### HatchStyleHorizontal

Constant

Value: `0`

---

### HatchStyleVertical

Constant

Value: `1`

---

### HatchStyleForwardDiagonal

Constant

Value: `2`

---

### HatchStyleBackwardDiagonal

Constant

Value: `3`

---

### HatchStyleCross

Constant

Value: `4`

---

### HatchStyleDiagonalCross

Constant

Value: `5`

---

### HatchStyle05Percent

Constant

Value: `6`

---

### HatchStyle10Percent

Constant

Value: `7`

---

### HatchStyle20Percent

Constant

Value: `8`

---

### HatchStyle25Percent

Constant

Value: `9`

---

### HatchStyle30Percent

Constant

Value: `10`

---

### HatchStyle40Percent

Constant

Value: `11`

---

### HatchStyle50Percent

Constant

Value: `12`

---

### HatchStyle60Percent

Constant

Value: `13`

---

### HatchStyle70Percent

Constant

Value: `14`

---

### HatchStyle75Percent

Constant

Value: `15`

---

### HatchStyle80Percent

Constant

Value: `16`

---

### HatchStyle90Percent

Constant

Value: `17`

---

### HatchStyleLightDownwardDiagonal

Constant

Value: `18`

---

### HatchStyleLightUpwardDiagonal

Constant

Value: `19`

---

### HatchStyleDarkDownwardDiagonal

Constant

Value: `20`

---

### HatchStyleDarkUpwardDiagonal

Constant

Value: `21`

---

### HatchStyleWideDownwardDiagonal

Constant

Value: `22`

---

### HatchStyleWideUpwardDiagonal

Constant

Value: `23`

---

### HatchStyleLightVertical

Constant

Value: `24`

---

### HatchStyleLightHorizontal

Constant

Value: `25`

---

### HatchStyleNarrowVertical

Constant

Value: `26`

---

### HatchStyleNarrowHorizontal

Constant

Value: `27`

---

### HatchStyleDarkVertical

Constant

Value: `28`

---

### HatchStyleDarkHorizontal

Constant

Value: `29`

---

### HatchStyleDashedDownwardDiagonal

Constant

Value: `30`

---

### HatchStyleDashedUpwardDiagonal

Constant

Value: `311`

---

### HatchStyleDashedHorizontal

Constant

Value: `32`

---

### HatchStyleDashedVertical

Constant

Value: `33`

---

### HatchStyleSmallConfetti

Constant

Value: `34`

---

### HatchStyleLargeConfetti

Constant

Value: `35`

---

### HatchStyleZigZag

Constant

Value: `36`

---

### HatchStyleWave

Constant

Value: `37`

---

### HatchStyleDiagonalBrick

Constant

Value: `38`

---

### HatchStyleHorizontalBrick

Constant

Value: `39`

---

### HatchStyleWeave

Constant

Value: `40`

---

### HatchStylePlaid

Constant

Value: `41`

---

### HatchStyleDivot

Constant

Value: `42`

---

### HatchStyleDottedGrid

Constant

Value: `43`

---

### HatchStyleDottedDiamond

Constant

Value: `44`

---

### HatchStyleShingle

Constant

Value: `45`

---

### HatchStyleTrellis

Constant

Value: `46`

---

### HatchStyleSphere

Constant

Value: `47`

---

### HatchStyleSmallGrid

Constant

Value: `48`

---

### HatchStyleSmallCheckerBoard

Constant

Value: `49`

---

### HatchStyleLargeCheckerBoard

Constant

Value: `50`

---

### HatchStyleOutlinedDiamond

Constant

Value: `51`

---

### HatchStyleSolidDiamond

Constant

Value: `52`

---

### HatchStyleTotal

Constant

Value: `53`

---

### HatchStyleLargeGrid

Constant

Value: `HatchStyleCross`

---

### HatchStyleMin

Constant

Value: `HatchStyleHorizontal`

---

### HatchStyleMax

Constant

Value: `HatchStyleTotal - 1`

---

### LinearGradientModeHorizontal

Constant

Value: `0`

**Description**

LinearGradientMode definitions

---

### LinearGradientModeVertical

Constant

Value: `1`

---

### LinearGradientModeForwardDiagonal

Constant

Value: `2`

---

### LinearGradientModeBackwardDiagonal

Constant

Value: `3`

---

### LineCapFlat

Constant

Value: `0`

---

### LineCapSquare

Constant

Value: `1`

---

### LineCapRound

Constant

Value: `2`

---

### LineCapTriangle

Constant

Value: `3`

---

### LineCapNoAnchor

Constant

Value: `0x10`

---

### LineCapSquareAnchor

Constant

Value: `0x11`

---

### LineCapRoundAnchor

Constant

Value: `0x12`

---

### LineCapDiamondAnchor

Constant

Value: `0x13`

---

### LineCapArrowAnchor

Constant

Value: `0x14`

---

### LineJoinMiter

Constant

Value: `0`

---

### LineJoinBevel

Constant

Value: `1`

---

### LineJoinRound

Constant

Value: `2`

---

### LineJoinMiterClipped

Constant

Value: `3`

---

### PenAlignmentCenter

Constant

Value: `0`

---

### PenAlignmentInset

Constant

Value: `1`

---

### WrapModeTile

Constant

Value: `0`

---

### WrapModeTileFlipX

Constant

Value: `1`

---

### WrapModeTileFlipY

Constant

Value: `2`

---

### WrapModeTileFlipXY

Constant

Value: `3`

---

### WrapModeClamp

Constant

Value: `4`

---

### MatrixOrderPrepend

Constant

Value: `0`

---

### MatrixOrderAppend

Constant

Value: `1`

---

### ImageTypeUnknown

Constant

Value: `0`

---

### ImageTypeBitmap

Constant

Value: `1`

---

### ImageTypeMetafile

Constant

Value: `2`

---

### RotateNoneFlipNone

Constant

Value: `0`

---

### Rotate90FlipNone

Constant

Value: `1`

---

### Rotate180FlipNone

Constant

Value: `2`

---

### Rotate270FlipNone

Constant

Value: `3`

---

### RotateNoneFlipX

Constant

Value: `4`

---

### Rotate90FlipX

Constant

Value: `5`

---

### Rotate180FlipX

Constant

Value: `6`

---

### Rotate270FlipX

Constant

Value: `7`

---

### RotateNoneFlipY

Constant

Value: `Rotate180FlipX`

---

### Rotate90FlipY

Constant

Value: `Rotate270FlipX`

---

### Rotate180FlipY

Constant

Value: `RotateNoneFlipX`

---

### Rotate270FlipY

Constant

Value: `Rotate90FlipX`

---

### RotateNoneFlipXY

Constant

Value: `Rotate180FlipNone`

---

### Rotate90FlipXY

Constant

Value: `Rotate270FlipNone`

---

### Rotate180FlipXY

Constant

Value: `RotateNoneFlipNone`

---

### Rotate270FlipXY

Constant

Value: `Rotate90FlipNone`

---

### SmoothingModeInvalid

Constant

Value: `-1`

**Description**

SmoothingMode values

---

### SmoothingModeDefault

Constant

Value: `0`

---

### SmoothingModeHighSpeed

Constant

Value: `1`

---

### SmoothingModeHighQuality

Constant

Value: `2`

---

### SmoothingModeNone

Constant

Value: `0`

---

### SmoothingModeAntiAlias

Constant

Value: `1`

---

### TextRenderingHintSystemDefault

Constant

Value: `0`

**Description**

TextRenderingHint values

---

### TextRenderingHintSingleBitPerPixelGridFit

Constant

Value: `1`

---

### TextRenderingHintSingleBitPerPixel

Constant

Value: `2`

---

### TextRenderingHintAntiAliasGridFit

Constant

Value: `3`

---

### TextRenderingHintAntiAlias

Constant

Value: `4`

---

### TextRenderingHintClearTypeGridFit

Constant

Value: `5`

---

## Plugin extension: layerExVector

Manual in pseudo-code

A vector drawing plugin based on ThorVG.
It reimplements the GDI+-based LayerExDraw with ThorVG.
Some GDI+-specific features have been removed.

### Members

#### Methods

- [loadFont](#loadfont)
- [unloadFont](#unloadfont)

#### Constants

- [BrushTypeSolidColor](#brushtypesolidcolor)
- [BrushTypePathGradient](#brushtypepathgradient)
- [BrushTypeLinearGradient](#brushtypelineargradient)
- [LineCapFlat](#linecapflat)
- [LineCapSquare](#linecapsquare)
- [LineCapRound](#linecapround)
- [LineCapTriangle](#linecaptriangle)
- [LineJoinMiter](#linejoinmiter)
- [LineJoinBevel](#linejoinbevel)
- [LineJoinRound](#linejoinround)
- [LineJoinMiterClipped](#linejoinmiterclipped)
- [MatrixOrderPrepend](#matrixorderprepend)
- [MatrixOrderAppend](#matrixorderappend)

---

### loadFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `void` |  |

---

### unloadFont

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### BrushTypeSolidColor

Constant

Value: `0`

---

### BrushTypePathGradient

Constant

Value: `3`

---

### BrushTypeLinearGradient

Constant

Value: `4`

---

### LineCapFlat

Constant

Value: `0`

---

### LineCapSquare

Constant

Value: `1`

---

### LineCapRound

Constant

Value: `2`

---

### LineCapTriangle

Constant

Value: `3`

---

### LineJoinMiter

Constant

Value: `0`

---

### LineJoinBevel

Constant

Value: `1`

---

### LineJoinRound

Constant

Value: `2`

---

### LineJoinMiterClipped

Constant

Value: `3`

---

### MatrixOrderPrepend

Constant

Value: `0`

---

### MatrixOrderAppend

Constant

Value: `1`

---
