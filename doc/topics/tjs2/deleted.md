# 吉里吉里Zで削除された機能
吉里吉里Z本体からは削除された機能でもプラグインなどを入れると使用できる。

## KagParser クラス
吉里吉里Zリポジトリに同梱されている KAGParser.dll をリンクすると利用可能。

## Menu クラス
吉里吉里Zリポジトリに同梱されている menu.dll をリンクすると利用可能。

## Pad クラス
吉里吉里Zリポジトリに同梱されている Krkr2Compat を読み込むと利用可能。

## コンソールウィンドウ(Debug.console)
吉里吉里Zリポジトリに同梱されている Krkr2Compat を読み込むと利用可能。

## スクリプトエディタ
吉里吉里Zリポジトリに同梱されている Krkr2Compat を読み込むと利用可能。

## フォント選択ダイアログ(Font.doUserSelect)
吉里吉里Zリポジトリに同梱されている Krkr2Compat を読み込むと利用可能。

## 1行入力ダイアログ(System.inputString)
吉里吉里Zリポジトリに同梱されている Krkr2Compat を読み込むと利用可能。

## Layer.hint
TJS で実装可能。詳しくは[ツールチップの表示方法](./tooltip.md)を参照。

## Layer クラスの obsolete メソッド
affineBlend/affinePile/blendRect/pileRect/stretchBlend/stretchPileメソッドは以下のようなTJS で実装可能。

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
