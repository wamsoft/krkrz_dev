---
source_hash: fb9a590b20a1
---

# Features Removed in Kirikiri Z
Features removed from the Kirikiri Z engine can still be used by adding plugins and the like.

## KagParser class
Available by linking KAGParser.dll, which ships with the Kirikiri Z repository.

## Menu class
Available by linking menu.dll, which ships with the Kirikiri Z repository.

## Pad class
Available by loading Krkr2Compat, which ships with the Kirikiri Z repository.

## Console window (Debug.console)
Available by loading Krkr2Compat, which ships with the Kirikiri Z repository.

## Script editor
Available by loading Krkr2Compat, which ships with the Kirikiri Z repository.

## Font selection dialog (Font.doUserSelect)
Available by loading Krkr2Compat, which ships with the Kirikiri Z repository.

## Single-line input dialog (System.inputString)
Available by loading Krkr2Compat, which ships with the Kirikiri Z repository.

## Layer.hint
Can be implemented in TJS. See [Showing Tooltips](./tooltip.md) for details.

## Obsolete methods of the Layer class
The affineBlend/affinePile/blendRect/pileRect/stretchBlend/stretchPile methods can be implemented in TJS as follows.

```
Layer.affineBlend = function(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, opa=255, type=stNearest) {
    this.operateAffine(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, omOpaque, opa, type);
};
Layer.affinePile = function(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, opa=255, type=stNearest) {
    this.operateAffine(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, omAuto, opa, type);
};
Layer.blendRect = function(dleft, dtop, src, sleft, stop, swidth, sheight, opa=255) {
    this.operateRect(dleft, dtop, src, sleft, stop, swidth, sheight, omOpaque, opa);
};
Layer.pileRect = function(dleft, dtop, src, sleft, stop, swidth, sheight, opa=255) {
    this.operateRect(dleft, dtop, src, sleft, stop, swidth, sheight, omAuto, opa);
};
Layer.stretchBlend = function(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, opa=255, type=stNearest) {
    this.operateStretch(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, omOpaque, opa, type);
};
Layer.stretchPile = function(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, opa=255, type=stNearest) {
    this.operateStretch(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, omAuto, opa, type);
};
```
