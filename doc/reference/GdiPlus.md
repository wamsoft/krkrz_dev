# GdiPlus

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

### メンバー一覧

#### メソッド

- [addPrivateFont](#addprivatefont)
- [getFontList](#getfontlist)

#### 定数

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

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fontFileName` | `&nbsp;` |  |

---

### getFontList

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `privateOnly` | `&nbsp;` |  |

---

### Ok

定数

値: `0`

---

### GenericError

定数

値: `1`

---

### InvalidParameter

定数

値: `2`

---

### OutOfMemory

定数

値: `3`

---

### ObjectBusy

定数

値: `4`

---

### InsufficientBuffer

定数

値: `5`

---

### NotImplemented

定数

値: `6`

---

### Win32Error

定数

値: `7`

---

### WrongState

定数

値: `8`

---

### Aborted

定数

値: `9`

---

### FileNotFound

定数

値: `10`

---

### ValueOverflow

定数

値: `11`

---

### AccessDenied

定数

値: `12`

---

### UnknownImageFormat

定数

値: `13`

---

### FontFamilyNotFound

定数

値: `14`

---

### FontStyleNotFound

定数

値: `15`

---

### NotTrueTypeFont

定数

値: `16`

---

### UnsupportedGdiplusVersion

定数

値: `17`

---

### GdiplusNotInitialized

定数

値: `18`

---

### PropertyNotFound

定数

値: `19`

---

### PropertyNotSupported

定数

値: `20`

---

### ProfileNotFound

定数

値: `21`

---

### FontStyleRegular

定数

値: `0`

---

### FontStyleBold

定数

値: `1`

---

### FontStyleItalic

定数

値: `2`

---

### FontStyleBoldItalic

定数

値: `3`

---

### FontStyleUnderline

定数

値: `4`

---

### FontStyleStrikeout

定数

値: `8`

---

### BrushTypeSolidColor

定数

値: `0`

---

### BrushTypeHatchFill

定数

値: `1`

---

### BrushTypeTextureFill

定数

値: `2`

---

### BrushTypePathGradient

定数

値: `3`

---

### BrushTypeLinearGradient

定数

値: `4`

---

### DashCapFlat

定数

値: `0`

---

### DashCapRound

定数

値: `2`

---

### DashCapTriangle

定数

値: `3`

---

### DashStyleSolid

定数

値: `0`

---

### DashStyleDash

定数

値: `1`

---

### DashStyleDot

定数

値: `2`

---

### DashStyleDashDot

定数

値: `3`

---

### DashStyleDashDotDot

定数

値: `4`

---

### HatchStyleHorizontal

定数

値: `0`

---

### HatchStyleVertical

定数

値: `1`

---

### HatchStyleForwardDiagonal

定数

値: `2`

---

### HatchStyleBackwardDiagonal

定数

値: `3`

---

### HatchStyleCross

定数

値: `4`

---

### HatchStyleDiagonalCross

定数

値: `5`

---

### HatchStyle05Percent

定数

値: `6`

---

### HatchStyle10Percent

定数

値: `7`

---

### HatchStyle20Percent

定数

値: `8`

---

### HatchStyle25Percent

定数

値: `9`

---

### HatchStyle30Percent

定数

値: `10`

---

### HatchStyle40Percent

定数

値: `11`

---

### HatchStyle50Percent

定数

値: `12`

---

### HatchStyle60Percent

定数

値: `13`

---

### HatchStyle70Percent

定数

値: `14`

---

### HatchStyle75Percent

定数

値: `15`

---

### HatchStyle80Percent

定数

値: `16`

---

### HatchStyle90Percent

定数

値: `17`

---

### HatchStyleLightDownwardDiagonal

定数

値: `18`

---

### HatchStyleLightUpwardDiagonal

定数

値: `19`

---

### HatchStyleDarkDownwardDiagonal

定数

値: `20`

---

### HatchStyleDarkUpwardDiagonal

定数

値: `21`

---

### HatchStyleWideDownwardDiagonal

定数

値: `22`

---

### HatchStyleWideUpwardDiagonal

定数

値: `23`

---

### HatchStyleLightVertical

定数

値: `24`

---

### HatchStyleLightHorizontal

定数

値: `25`

---

### HatchStyleNarrowVertical

定数

値: `26`

---

### HatchStyleNarrowHorizontal

定数

値: `27`

---

### HatchStyleDarkVertical

定数

値: `28`

---

### HatchStyleDarkHorizontal

定数

値: `29`

---

### HatchStyleDashedDownwardDiagonal

定数

値: `30`

---

### HatchStyleDashedUpwardDiagonal

定数

値: `311`

---

### HatchStyleDashedHorizontal

定数

値: `32`

---

### HatchStyleDashedVertical

定数

値: `33`

---

### HatchStyleSmallConfetti

定数

値: `34`

---

### HatchStyleLargeConfetti

定数

値: `35`

---

### HatchStyleZigZag

定数

値: `36`

---

### HatchStyleWave

定数

値: `37`

---

### HatchStyleDiagonalBrick

定数

値: `38`

---

### HatchStyleHorizontalBrick

定数

値: `39`

---

### HatchStyleWeave

定数

値: `40`

---

### HatchStylePlaid

定数

値: `41`

---

### HatchStyleDivot

定数

値: `42`

---

### HatchStyleDottedGrid

定数

値: `43`

---

### HatchStyleDottedDiamond

定数

値: `44`

---

### HatchStyleShingle

定数

値: `45`

---

### HatchStyleTrellis

定数

値: `46`

---

### HatchStyleSphere

定数

値: `47`

---

### HatchStyleSmallGrid

定数

値: `48`

---

### HatchStyleSmallCheckerBoard

定数

値: `49`

---

### HatchStyleLargeCheckerBoard

定数

値: `50`

---

### HatchStyleOutlinedDiamond

定数

値: `51`

---

### HatchStyleSolidDiamond

定数

値: `52`

---

### HatchStyleTotal

定数

値: `53`

---

### HatchStyleLargeGrid

定数

値: `HatchStyleCross`

---

### HatchStyleMin

定数

値: `HatchStyleHorizontal`

---

### HatchStyleMax

定数

値: `HatchStyleTotal - 1`

---

### LinearGradientModeHorizontal

定数

値: `0`

---

### LinearGradientModeVertical

定数

値: `1`

---

### LinearGradientModeForwardDiagonal

定数

値: `2`

---

### LinearGradientModeBackwardDiagonal

定数

値: `3`

---

### LineCapFlat

定数

値: `0`

---

### LineCapSquare

定数

値: `1`

---

### LineCapRound

定数

値: `2`

---

### LineCapTriangle

定数

値: `3`

---

### LineCapNoAnchor

定数

値: `0x10`

---

### LineCapSquareAnchor

定数

値: `0x11`

---

### LineCapRoundAnchor

定数

値: `0x12`

---

### LineCapDiamondAnchor

定数

値: `0x13`

---

### LineCapArrowAnchor

定数

値: `0x14`

---

### LineJoinMiter

定数

値: `0`

---

### LineJoinBevel

定数

値: `1`

---

### LineJoinRound

定数

値: `2`

---

### LineJoinMiterClipped

定数

値: `3`

---

### PenAlignmentCenter

定数

値: `0`

---

### PenAlignmentInset

定数

値: `1`

---

### WrapModeTile

定数

値: `0`

---

### WrapModeTileFlipX

定数

値: `1`

---

### WrapModeTileFlipY

定数

値: `2`

---

### WrapModeTileFlipXY

定数

値: `3`

---

### WrapModeClamp

定数

値: `4`

---

### MatrixOrderPrepend

定数

値: `0`

---

### MatrixOrderAppend

定数

値: `1`

---

### ImageTypeUnknown

定数

値: `0`

---

### ImageTypeBitmap

定数

値: `1`

---

### ImageTypeMetafile

定数

値: `2`

---

### RotateNoneFlipNone

定数

値: `0`

---

### Rotate90FlipNone

定数

値: `1`

---

### Rotate180FlipNone

定数

値: `2`

---

### Rotate270FlipNone

定数

値: `3`

---

### RotateNoneFlipX

定数

値: `4`

---

### Rotate90FlipX

定数

値: `5`

---

### Rotate180FlipX

定数

値: `6`

---

### Rotate270FlipX

定数

値: `7`

---

### RotateNoneFlipY

定数

値: `Rotate180FlipX`

---

### Rotate90FlipY

定数

値: `Rotate270FlipX`

---

### Rotate180FlipY

定数

値: `RotateNoneFlipX`

---

### Rotate270FlipY

定数

値: `Rotate90FlipX`

---

### RotateNoneFlipXY

定数

値: `Rotate180FlipNone`

---

### Rotate90FlipXY

定数

値: `Rotate270FlipNone`

---

### Rotate180FlipXY

定数

値: `RotateNoneFlipNone`

---

### Rotate270FlipXY

定数

値: `Rotate90FlipNone`

---

### SmoothingModeInvalid

定数

値: `-1`

---

### SmoothingModeDefault

定数

値: `0`

---

### SmoothingModeHighSpeed

定数

値: `1`

---

### SmoothingModeHighQuality

定数

値: `2`

---

### SmoothingModeNone

定数

値: `0`

---

### SmoothingModeAntiAlias

定数

値: `1`

---

### TextRenderingHintSystemDefault

定数

値: `0`

---

### TextRenderingHintSingleBitPerPixelGridFit

定数

値: `1`

---

### TextRenderingHintSingleBitPerPixel

定数

値: `2`

---

### TextRenderingHintAntiAliasGridFit

定数

値: `3`

---

### TextRenderingHintAntiAlias

定数

値: `4`

---

### TextRenderingHintClearTypeGridFit

定数

値: `5`

---

## プラグイン拡張: layerExVector

### メンバー一覧

#### メソッド

- [loadFont](#loadfont)
- [unloadFont](#unloadfont)

#### 定数

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

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `void` |  |

---

### unloadFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### BrushTypeSolidColor

定数

値: `0`

---

### BrushTypePathGradient

定数

値: `3`

---

### BrushTypeLinearGradient

定数

値: `4`

---

### LineCapFlat

定数

値: `0`

---

### LineCapSquare

定数

値: `1`

---

### LineCapRound

定数

値: `2`

---

### LineCapTriangle

定数

値: `3`

---

### LineJoinMiter

定数

値: `0`

---

### LineJoinBevel

定数

値: `1`

---

### LineJoinRound

定数

値: `2`

---

### LineJoinMiterClipped

定数

値: `3`

---

### MatrixOrderPrepend

定数

値: `0`

---

### MatrixOrderAppend

定数

値: `1`

---
