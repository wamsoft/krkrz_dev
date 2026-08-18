# PSD

擬似コードによるマニュアル

PSDファイルストレージ機能
以下のパス名でPSDファイルのレイヤ画像を直接ファイルとしてロードできます

psd://PSDファイル名/root/フォルダ名/.../レイヤ名.bmp
psd://PSDファイル名/id/レイヤID.bmp

・PSDファイル名はベース名のみで小文字で正規化されます
・フォルダ名、レイヤ名は全て小文字で正規化されて含まれる"/" は "_" に置換されます
・名前が重複する場合は後にあるものが優先になります

## メンバー一覧

### プロパティ

- [width](#width)
- [height](#height)
- [channels](#channels)
- [depth](#depth)
- [color_mode](#color_mode)
- [layer_count](#layer_count)
- [hresolution](#hresolution)
- [vresolution](#vresolution)
- [merged_alpha](#merged_alpha)

### メソッド

- [load](#load)
- [loadOctet](#loadoctet)
- [clear](#clear)
- [assignAutoIds](#assignautoids)
- [getLayerType](#getlayertype)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getSlices](#getslices)
- [getGuides](#getguides)
- [getBlend](#getblend)
- [getLayerComp](#getlayercomp)
- [getLayerMask](#getlayermask)
- [getLayerBlendingRanges](#getlayerblendingranges)
- [getLayerSheetColor](#getlayersheetcolor)
- [getLayerInfoKeys](#getlayerinfokeys)
- [getLayerDescriptor](#getlayerdescriptor)
- [getLayerDescriptorBytes](#getlayerdescriptorbytes)
- [getLayerEffects](#getlayereffects)
- [getLayerFill](#getlayerfill)
- [getColorTable](#getcolortable)
- [getGlobalLayerMask](#getgloballayermask)
- [getImageResourceIds](#getimageresourceids)
- [getImageResource](#getimageresource)
- [getICCProfile](#geticcprofile)
- [getEXIF](#getexif)
- [getXMP](#getxmp)
- [getThumbnail](#getthumbnail)
- [save](#save)
- [createBlank](#createblank)
- [deleteLayer](#deletelayer)
- [moveLayer](#movelayer)
- [groupSpan](#groupspan)
- [moveLayerSibling](#movelayersibling)
- [moveLayerRange](#movelayerrange)
- [duplicateLayer](#duplicatelayer)
- [copyLayerFrom](#copylayerfrom)
- [setLayerName](#setlayername)
- [setFillOpacity](#setfillopacity)
- [setLayerOpacity](#setlayeropacity)
- [setLayerClipping](#setlayerclipping)
- [setLayerVisible](#setlayervisible)
- [setLayerBlendMode](#setlayerblendmode)
- [setLayerEffects](#setlayereffects)
- [setLayerDescriptor](#setlayerdescriptor)
- [setMaskDisabled](#setmaskdisabled)
- [setMaskDensity](#setmaskdensity)
- [setMaskFeather](#setmaskfeather)
- [setMaskDefaultColor](#setmaskdefaultcolor)
- [setLayerPixels](#setlayerpixels)
- [setLayerMaskPixels](#setlayermaskpixels)
- [addLayer](#addlayer)
- [setMergedImage](#setmergedimage)
- [setLayerText](#setlayertext)
- [setLayerRunStyle](#setlayerrunstyle)
- [setLayerRichText](#setlayerrichtext)
- [setLayerJustification](#setlayerjustification)
- [getLayerFonts](#getlayerfonts)
- [getLayerTextTransform](#getlayertexttransform)
- [setLayerTextTransform](#setlayertexttransform)
- [moveTextLayer](#movetextlayer)
- [getLayerTextBounds](#getlayertextbounds)
- [setLayerTextBounds](#setlayertextbounds)
- [clearStorageCache](#clearstoragecache)

---

### width

プロパティ \ アクセス: `r`

**解説**

画像横幅

---

### height

プロパティ \ アクセス: `r`

**解説**

画像縦幅

---

### channels

プロパティ \ アクセス: `r`

**解説**

チャンネル数

---

### depth

プロパティ \ アクセス: `r`

**解説**

1チャンネルあたりのビット数(1/8/16/32)

---

### color_mode

プロパティ \ アクセス: `r`

**解説**

カラーモード

---

### layer_count

プロパティ \ アクセス: `r`

**解説**

レイヤ数

---

### hresolution

プロパティ \ アクセス: `r`

**解説**

水平解像度(dpi, 既定72, image resource 1005)

---

### vresolution

プロパティ \ アクセス: `r`

**解説**

垂直解像度(dpi, 既定72)

---

### merged_alpha

プロパティ \ アクセス: `r`

**解説**

合成済み画像にアルファチャンネルが含まれるか

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名 |

**戻り値**

ロードに成功したら true

**解説**

PSD画像のロード

---

### loadOctet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `data` | `&nbsp;` | PSD ファイル全体を格納した octet |

**戻り値**

ロードに成功したら true

**解説**

octet に入った PSD データをロードする。

バイト列は内部バッファへコピーされるので、呼び出し後に octet を破棄しても
かまわない。ファイル名を持たないため psd:// ストレージへは登録されない。

---

### clear

メソッド

**解説**

保持しているデータを明示的に破棄する。

吉里吉里のオブジェクト寿命は GC 依存なので、大きな PSD を掴んだままに
したくないときに呼ぶ。以後の参照系は "no data" 例外になる。

---

### assignAutoIds

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `base_id` | `0` | 割り付けID最小番号-1(※既存のいずれかのレイヤIDがこれより大きかったらその値が利用される) |

**戻り値**

IDを設定したレイヤの枚数

**解説**

LayerIDが未設定のレイヤに対してID番号を自動割り付け(base_id+1からlayer_no順に)

Photoshop互換系のpsd保存ツールではレイヤIDが割り付けられないケースがあるため，psd://~/id/ が正しくロードできない問題がある
基本的にはload直後に呼ぶことを推奨

---

### getLayerType

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

レイヤ種別

**解説**

レイヤ種別の取得

---

### getLayerName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

レイヤ名称

**解説**

レイヤの名前の取得

---

### getLayerInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

レイヤ情報がはいった辞書
辞書の内容
layer_type   レイヤ種別
top          上座標
left         左座標
bottom       底座標
right        右座標
width        横幅
height       縦幅
blend_mode   合成モード(blend_mode_*。未知のモードは blend_mode_invalid)
blend_mode_key PSD 上の生の合成モードキー(4文字。3文字キーは末尾に空白が付く
ことに注意 "mul " 等)。未知モードもそのまま得られるので、
読んだ値をそのまま書き戻すなら setLayerBlendMode にこれを渡す
opacity      不透明度
fill_opacity 塗りの不透明度
visible      表示状態
name         レイヤ名
layer_id     レイヤID
group_layer_id 親レイヤID
parent_index 親フォルダのレイヤ番号(トップレベルは -1)。layer_id は PSD に
よっては未設定(-1)なので、階層を組むならこちらが確実。
構造編集(deleteLayer/moveLayer/duplicateLayer/addLayer 等)の
あとも再計算される
type         合成モード（吉里吉里の対応モード)
clipping	クリッピングマスクの対象か？
mask		レイヤマスクを持っているかどうか？
mask_params  マスクパラメータ(density/feather)。マスクを持ちパラメータ
ブロックが実在するレイヤのみ存在。指定された項目だけ持つ
%[ user_density:   // ユーザーマスク濃度 0..255
user_feather:   // ユーザーマスクぼかし(px)
vector_density: // ベクタマスク濃度 0..255
vector_feather: // ベクタマスクぼかし(px)
]
layer_comp    レイヤーカンプ情報(カンプIDをキーとした辞書)
%[ <id>: [ id,       // カンプID(getLayerComp() を参照してください)
offset_x, // レイヤのXオフセット
offset_y, // レイヤのYオフセット
enable,   // 表示状態フラグ
],... ]
text         テキストレイヤ情報(テキストレイヤ layer_type==layer_type_text のときのみ存在。
それ以外のレイヤではキー自体が存在しない)
%[ text:          // 本文全体(改行は復帰文字 CR)
orientation:   // "horizontal" または "vertical"(縦書き)
justification: // 先頭段落の行揃え 0=左 1=右 2=中央
transform:     // アフィン変換 `[ xx, xy, yx, yy, tx, ty ]` (tx,ty=平行移動)
runs: [        // 文字スタイルのラン配列(本文の並び順)
%[ length:       // 適用文字数(UTF-16 コードユニット。絵文字等サロゲートは2)
font:         // 解決済みフォント名
size_px:      // フォントサイズ(pt)
color:        // RGBA 各 0..1 の配列 `[ r, g, b, a ]` (未指定なら存在しない)
tracking:     // トラッキング(字送り, 1/1000 em)
kerning:      // 手動カーニング
auto_kerning: // 自動カーニング(メトリクス/オプティカル)有効か
bold:         // 疑似ボールド(FauxBold)
italic:       // 疑似イタリック(FauxItalic)
underline:    // 下線(Underline)
],... ]
paragraphs: [   // 段落別の行揃え(box text で段落ごとに揃えが変わる用)
%[ length:        // 段落の文字数(UTF-16 コードユニット)
justification: // 行揃え 0=左 1=右 2=中央
],... ]
]
以下 additional information （※詳細はPSD仕様書を参照のこと）
obsolete
transparency_protected
pixel_data_irrelevant

**解説**

レイヤの情報の取得

---

### getLayerData

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号<br>layer_type が layer_type_normal の場合のみ読み込みできます<br>イメージとマスクを合成した状態で読み出します。<br>データ内容のほか以下のプロパティが自動的にレイヤに設定されます<br>left          左座標<br>top           上座標<br>width         横幅<br>height        縦幅<br>type          合成モード<br>opacity       不透明度<br>fill_opacity	 塗りの不透明度<br>visible       表示状態<br>imageLeft     0になります<br>imageTop      0になります<br>imageWidth    width になります<br>imageHeight   height になります<br>name          name が設定されます |

**解説**

レイヤデータの読み出し

---

### getLayerDataRaw

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号<br>layer_type が layer_type_normal の場合のみ読み込みできます<br>イメージのみを読み出します。<br>データ内容のほか以下のプロパティが自動的にレイヤに設定されます<br>left          左座標<br>top           上座標<br>width         横幅<br>height        縦幅<br>type          合成モード<br>opacity       不透明度<br>fill_opacity	 塗りの不透明度<br>visible       表示状態<br>imageLeft     0になります<br>imageTop      0になります<br>imageWidth    width になります<br>imageHeight   height になります<br>name          name が設定されます |

**解説**

レイヤデータの読み出し

---

### getLayerDataMask

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号<br>layer_type が layer_type_normal の場合のみ読み込みできます<br>マスクのみを読み出します。<br>マスクのイメージサイズが0でdefualtMaskColorのみが設定されているケースでは、<br>「レイヤサイズを0には設定できない」と言う吉里吉里の制限を回避するため、<br>(0,0)-(1,1)の最小サイズのレイヤをダミーで作り、defaultMaskColorでfillして返します。<br>データ内容のほか以下のプロパティが自動的にレイヤに設定されます<br>left          左座標<br>top           上座標<br>width         横幅<br>height        縦幅<br>type          合成モード<br>opacity       不透明度<br>fill_opacity	 塗りの不透明度<br>visible       表示状態<br>imageLeft     0になります<br>imageTop      0になります<br>imageWidth    width になります<br>imageHeight   height になります<br>name          name が設定されます<br>defaultMaskColor  取得領域外のマスクカラー(常に0か255のどちらか) |

**解説**

レイヤデータの読み出し

---

### getSlices

メソッド

**戻り値**

スライス情報辞書 %[ top, left, bottom, right, slices:[ %[ id, group_id, left, top, bottom, right ], ... ] ]
スライス情報がない場合は void を返す
スライスの一番最後は全スライスを含むサイズのスライスのようです

**解説**

スライスデータの読み出し

---

### getGuides

メソッド

**戻り値**

ガイド情報辞書 %[ vertical:[ x1, x2, ... ], horizontal:[ y1, y2, ... ] ]
ガイド情報がない場合は void を返す

**解説**

ガイドデータの読み出し

---

### getBlend

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 格納先レイヤ |

**戻り値**

取得に成功したら true

**解説**

合成結果の取得。

ライブラリ中で合成を行うわけではなく、PSDに保存された合成結果を読み出します。
保存方法によってはこの画像は存在しない可能性があります。
また、レイヤが存在しないカラーモード(2値、インデックスカラー)の場合には
画像データはこのメソッドで取得する必要があります。

---

### getLayerComp

メソッド

**戻り値**

ガイド情報辞書 %[ last_applied_id,  // Photoshp上で最後に適用状態だったid
comps:[id,                // カンプID
record_visibility, // 表示/非表示を記録しているか
record_position,   // 位置を記録しているか
record_appearance, // 外観(レイヤーエフェクト)を記録しているか
name,              // カンプ名
comment,           // コメント
],... ]
カンプ情報がない場合は void を返す

・record_xxx フラグが立っていな場合は最後に適用したカンプ(last_applied_id ではなく
プログラムで最後に適用したカンプ)の状態を引き継ぎます
・カンプIDに対応した各レイヤーごとの表示状態情報は、レイヤー情報の layer_comp
プロパティにカンプIDをキーとした辞書に格納してあります。

**解説**

レイヤーカンプデータの読み出し

---

### getLayerMask

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ top:, left:, bottom:, right:, // マスク矩形
width:, height:,
default_color:  // マスク領域外の値 0..255
flags:          // 生のフラグバイト
relative:       // 位置がレイヤ相対か(bit0)
disabled:       // マスクが無効か(bit1)
inverted:       // 反転(bit2、廃止仕様)
from_render:    // 他データのレンダリング由来か(bit3)
has_parameters: // density/feather ブロックを持つか(bit4)
user_density:   // ユーザーマスク濃度 0..255(無ければキー自体なし)
user_feather:   // ユーザーマスクぼかし(px、同上)
vector_density: // ベクタマスク濃度(同上)
vector_feather: // ベクタマスクぼかし(同上)
real: %[        // real/user mask (無ければキー自体なし)
flags:, background:,
top:, left:, bottom:, right:, // enclosing 矩形
]
]  マスクを持たない場合は void

**解説**

レイヤマスクの詳細を取得する

---

### getLayerBlendingRanges

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ gray:     %[ source:, dest: ],
channels: [ %[ source:, dest: ],... ]
]  ブレンド範囲ブロックが無い場合は void

**解説**

レイヤのブレンド範囲を取得する。source/dest は 32bit の生値で、

上下 16bit に黒側/白側の範囲が詰まっている(詳細は PSD 仕様書を参照)。

---

### getLayerSheetColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ index: // 0..11
name:  // "none" "red" "orange" "yellow" "green" "blue"
// "violet" "gray" "seafoam" "indigo" "magenta" "fuschia"
]  lclr ブロックが無い場合は void
(index 0/"none" は「明示的にラベル無し」なので void とは区別される)

**解説**

レイヤパネルの色ラベル('lclr')を取得する

---

### getLayerInfoKeys

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

キー文字列(4文字)の配列

**解説**

レイヤが持つ追加レイヤ情報ブロックの 4CC キー一覧を取得する。

getLayerDescriptor / getLayerDescriptorBytes に渡せるキーの調査用。

---

### getLayerDescriptor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |
| `key` | `&nbsp;` | 4文字のキー("lfx2" 等) |
| `skip` | `-1` | ディスクリプタ本体前のバージョン接頭バイト数。<br>-1 で既知キー(lfx2/SoCo/GdFl/PtFl/SoLd/SoLE/vstk/CgEd/vscg/vogk)<br>は自動判定、それ以外は 0。既定 -1 |

**戻り値**

辞書。キーが無い・解析できない場合は void

**解説**

追加レイヤ情報ブロックを Photoshop ディスクリプタとして辞書化する。

型に応じて以下へ変換される:
整数/実数     → 数値
真偽         → 1/0
文字列       → 文字列
UnitFloat    → %[ value:, unit: ]  unit は "points" "millimeters" "angle"
"density" "distance" "none" "percent"
"pixels" のいずれか
Enumerated   → %[ type:, value: ]
List         → 配列
Descriptor   → 辞書(入れ子)
RawData      → octet
Class/Alias  → 文字列
Reference    → void

---

### getLayerDescriptorBytes

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |
| `key` | `&nbsp;` | 4文字のキー |

**戻り値**

octet。キーが無い場合は void

**解説**

追加レイヤ情報ブロックの生バイトを取得する

---

### getLayerEffects

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

辞書。効果が無い場合は void

**解説**

レイヤ効果('lfx2')のディスクリプタ辞書を取得する。

ドロップシャドウ/光彩/オーバーレイ/境界線/ベベル等が入れ子の辞書で入る。
getLayerDescriptor(no, "lfx2") と同じ。

---

### getLayerFill

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ type: // "solid" / "gradient" / "pattern"
data: // ディスクリプタ辞書
]  塗りつぶしレイヤでない場合は void

**解説**

塗りつぶしレイヤの内容('SoCo'単色/'GdFl'グラデーション/'PtFl'パターン)を

取得する

---

### getColorTable

メソッド

**戻り値**

%[ valid_count:        // 有効なエントリ数
transparency_index: // 透明色インデックス(-1 で無し)
colors: [ 0xAARRGGBB, ... ] // 常に 256 エントリ
]  カラーテーブルが無い場合は void

**解説**

カラーテーブル(インデックスカラー文書のパレット)を取得する

---

### getGlobalLayerMask

メソッド

**戻り値**

%[ overlay_color_space:,
color: [ c1, c2, c3, c4 ],
opacity: // 0..100
kind:    // 0=反転 / 1=全マスク / 128=レイヤ毎
]  ブロックが空/不在の場合は void

**解説**

global layer mask info(マスク表示用のオーバーレイ色)を取得する

---

### getImageResourceIds

メソッド

**戻り値**

ID(整数)の配列

**解説**

文書が持つイメージリソースの ID 一覧を取得する

---

### getImageResource

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | リソースID(1039=ICCプロファイル, 1058=EXIF, 1060=XMP,<br>1036/1033=サムネイル, 1005=解像度, 1032=グリッド/ガイド 等) |

**戻り値**

octet。該当リソースが無い場合は void

**解説**

イメージリソースの生バイトを取得する。デコードは呼び出し側の責任。

---

### getICCProfile

メソッド

**解説**

ICC プロファイル(リソース 1039)の生バイト。無ければ void

---

### getEXIF

メソッド

**解説**

EXIF(リソース 1058)の生バイト。無ければ void

---

### getXMP

メソッド

**戻り値**

文字列。無ければ void

**解説**

XMP パケット(リソース 1060)を文字列で取得する。中身は UTF-8 の XML。

不正な UTF-8 が入っている可能性を考えるなら getImageResource(1060) で
生バイトを取ること。

---

### getThumbnail

メソッド

**戻り値**

%[ format:      // "jpeg"(JFIF JPEG) または "raw"
width:, height:,
bits:        // 1ピクセルあたりのビット数
resource_id: // 1036 または 1033
data:        // ペイロードの octet(28バイトのヘッダを除いたもの)
]  サムネイルが無い場合は void

**解説**

埋め込みサムネイルを取得する(リソース 1036=RGB順 / 旧 1033=BGR順)

---

### save

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 保存先ファイル名(ローカルパス) |

**戻り値**

成功したら true

**解説**

現在の内容を PSD ファイルとして書き出す

---

### createBlank

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 幅 |
| `height` | `&nbsp;` | 高さ |
| `mode` | `color_mode_rgb` | カラーモード(color_mode_*、既定 color_mode_rgb)。<br>**現状 color_mode_rgb 以外は false を返します**<br>(新規作成に対応しているのは 8bit RGB のみ)。<br>画素編集系(addLayer/setLayerPixels/setMergedImage)も同様に<br>8bit RGB 文書のみ対応です |

**戻り値**

成功したら true

**解説**

この PSD を空の 8bit 文書(白の合成画像)として初期化する。

以後 addLayer(...) でレイヤを足して save() できる。

---

### deleteLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

成功したら true(範囲外で false)

**解説**

レイヤを 1 枚削除する

---

### moveLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 移動元レイヤ番号 |
| `to` | `&nbsp;` | 移動先(削除後リストでの挿入位置) |

**戻り値**

成功したら true

**解説**

レイヤを from から to へ移動する

---

### groupSpan

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ start: // 塊の先頭レイヤ番号
count: // 塊の枚数
]  範囲外なら void

**解説**

レイヤがレイヤ一覧上で占める「塊」を返す。

フォルダ(layer_type_folder)の場合は対応する区切り(layer_type_hidden)から
自分自身までの範囲(入れ子も内側に含む)、それ以外は自分自身 1 枚だけ。
moveLayerRange と組み合わせてフォルダごと動かすのに使う。

---

### moveLayerSibling

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `up` | `true` | true でレイヤパネル表示上ひとつ上(レイヤ一覧では後ろ)へ。<br>既定 true |

**戻り値**

移動後のレイヤ番号。端まで来ていて動かせない場合や範囲外は -1

**解説**

レイヤを同じ階層の隣の兄弟と入れ替える。

フォルダは区切り+中身をまとめた塊として動き、隣がフォルダならその塊ごと
飛び越える。階層をまたぐ移動はしない。

---

### moveLayerRange

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 移動元先頭レイヤ番号 |
| `count` | `&nbsp;` | 移動する枚数 |
| `to` | `&nbsp;` | 移動先(「取り除く前」のレイヤ一覧でのインデックス) |

**戻り値**

成功したら true(引数が不正なら false)

**解説**

レイヤ一覧上の [from, from+count) の範囲をまとめて to の位置へ動かす

(低水準。フォルダごと動かすなら groupSpan の戻り値を渡す)。

---

### duplicateLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

複製の新レイヤ番号(失敗で -1)

**解説**

レイヤを複製する(元の直後に挿入)

---

### copyLayerFrom

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `src` | `&nbsp;` | コピー元 PSD インスタンス |
| `srcIndex` | `&nbsp;` | コピー元レイヤ番号 |
| `destIndex` | `&nbsp;` | 挿入位置(負値で末尾) |

**戻り値**

新レイヤ番号(失敗で -1)

**解説**

別の PSD インスタンスからレイヤをコピー挿入する。

カラーモード/ビット深度が一致している必要がある。コピー元 PSD は
この PSD の save() が終わるまで生存している必要がある。

---

### setLayerName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `name` | `&nbsp;` | 新しい名前 |

**戻り値**

成功したら true

**解説**

レイヤを改名する(pascal 名 + luni 名の両方を更新)

---

### setFillOpacity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `opacity` | `&nbsp;` | 0..255 |

**戻り値**

成功したら true

**解説**

塗り不透明度(fill opacity)を編集する

---

### setLayerOpacity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `opacity` | `&nbsp;` | 0..255(範囲外はクランプされる) |

**戻り値**

成功したら true(範囲外のレイヤ番号で false)

**解説**

不透明度を編集する

---

### setLayerClipping

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `clipping` | `&nbsp;` | 0=base / 1=non-base(クリッピング対象) |

**戻り値**

成功したら true

**解説**

クリッピングマスクの対象かどうかを編集する

---

### setLayerVisible

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `visible` | `&nbsp;` | 表示するか |

**戻り値**

成功したら true

**解説**

表示状態を編集する

---

### setLayerBlendMode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `mode` | `&nbsp;` | blend_mode_* 定数、または PSD 上の生のキー文字列(4文字。<br>"norm" "mul " "scrn" など。3文字キーは末尾の空白が必須)。<br>getLayerInfo().blend_mode_key の値をそのまま渡せる |

**戻り値**

成功したら true

**解説**

合成モードを編集する

---

### setLayerEffects

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `changes` | `&nbsp;` | 部分辞書 |

**解説**

レイヤ効果('lfx2')の値を編集する。

changes は getLayerEffects() と同じ形の「部分辞書」で、指定した葉の値だけが
上書きされる。構造/クラスID/型/キー順はそのまま保たれ、指定しなかった項目や
ディスクリプタ側に存在しないキーは無視される(そのためバイト一致が保たれる)。
値の与え方:
数値/文字列/真偽 → そのまま
UnitFloat        → %[ value: ] か生の数値(単位は変更しない)
Enumerated       → %[ type:, value: ] か値だけの文字列
List             → 配列(先頭から既存要素数までを順に上書き)
Descriptor       → 辞書(入れ子でマージ)
lfx2 ブロックを持たないレイヤの場合は例外。

---

### setLayerDescriptor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `key` | `&nbsp;` | 4文字のキー |
| `changes` | `&nbsp;` | 部分辞書 |
| `skip` | `-1` | ディスクリプタ本体前のバージョン接頭バイト数<br>(-1 で既知キーは自動判定。既定 -1) |

**解説**

任意の追加レイヤ情報キーに対する setLayerEffects の一般版

(塗りつぶしレイヤの 'SoCo'/'GdFl'/'PtFl' 等)。
該当キーを持たないレイヤの場合は例外。

---

### setMaskDisabled

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `disabled` | `&nbsp;` | マスクを無効にするか |

**戻り値**

成功したら true

**解説**

マスク無効フラグを編集する(マスクを持つレイヤのみ)

---

### setMaskDensity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `density` | `&nbsp;` | 0..255 |

**戻り値**

成功したら true

**解説**

ユーザーマスク濃度を編集する(マスクを持つレイヤのみ)

---

### setMaskFeather

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `feather` | `&nbsp;` | ぼかし半径(px) |

**戻り値**

成功したら true

**解説**

ユーザーマスクぼかしを編集する(マスクを持つレイヤのみ)

---

### setMaskDefaultColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `color` | `&nbsp;` | 0..255 |

**戻り値**

成功したら true

**解説**

マスク既定色を編集する(マスクを持つレイヤのみ)

---

### setLayerPixels

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `layer` | `&nbsp;` | 画素供給元 Layer |

**戻り値**

成功したら true

**解説**

既存レイヤの画素を Layer オブジェクトの内容で差し替える。

Layer の imageWidth×imageHeight・BGRA を取り込む。left/top は保持し
width/height は更新される。8bit RGB 文書のみ。

---

### setLayerMaskPixels

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `layer` | `&nbsp;` | マスク供給元 Layer |
| `top` | `&nbsp;` | マスク上端 |
| `left` | `&nbsp;` | マスク左端 |

**戻り値**

成功したら true

**解説**

レイヤのマスク画素を Layer オブジェクトの内容(B 成分をグレーとして使用)で

差し替える。マスク矩形も (top,left,imageWidth,imageHeight) に設定する。
マスクが無ければ新規作成する。8bit 文書のみ。

---

### addLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | レイヤ名 |
| `left` | `&nbsp;` | 左座標 |
| `top` | `&nbsp;` | 上座標 |
| `layer` | `&nbsp;` | 画素供給元 Layer |
| `blendMode` | `blend_mode_normal` | 合成モード(blend_mode_*、既定 blend_mode_normal) |
| `opacity` | `255` | 不透明度 0..255(既定 255) |
| `destIndex` | `-1` | 挿入位置(負値で末尾) |

**戻り値**

新レイヤ番号(失敗で -1)

**解説**

新規画像レイヤを追加する。Layer の imageWidth×imageHeight・BGRA を取り込む。

8bit RGB 文書のみ。

---

### setMergedImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 画素供給元 Layer |

**戻り値**

成功したら true

**解説**

合成済み画像(プレビュー/getBlend の元)を Layer の内容で差し替える。

Layer のサイズは canvas サイズ(width×height)と一致している必要がある。
8bit RGB 文書のみ。

---

### setLayerText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `text` | `&nbsp;` | 新しい本文(改行は \\r) |

**解説**

テキストレイヤの本文を差し替える(スタイルは先頭ランに畳まれる)。

テキストレイヤ以外や TySh ブロックが無い場合は例外。

---

### setLayerRunStyle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `runIndex` | `&nbsp;` | ラン番号 |
| `style` | `&nbsp;` | スタイル辞書 |

**解説**

テキストレイヤの runIndex 番目のラン(getLayerInfo().text.runs に対応)の

スタイルを編集する。style 辞書のうち指定されたキーだけ上書きする。
%[ font:      // フォント名。文書のフォントセットに無ければ追加される
// (getLayerFonts() が返す PostScript 風の名前。表示名では
//  ないことに注意。手元に無い名前は Photoshop 側で代替される)
size_px:   // フォントサイズ(px)
color:     // RGBA 各 0..1 の配列 `[ r, g, b, a ]` (a 省略で `[ r, g, b ]` も可)
tracking:  // トラッキング(1/1000 em)
kerning:   // 手動カーニング
bold:      // 疑似ボールド(FauxBold) true/false
italic:    // 疑似イタリック(FauxItalic) true/false
underline: // 下線(Underline) true/false
]
本文とランの長さは変わらない。継承でキーを持たないランには追加される。
テキストレイヤ以外や runIndex 範囲外の場合は例外。

---

### setLayerRichText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `text` | `&nbsp;` | 新しい本文(改行は \\r) |
| `runs` | `void` | [ %[ length: // 適用文字数<br>…setLayerRunStyle の style と同じキー<br>],... ]   省略可 |
| `paragraphs` | `void` | [ %[ length:        // 段落の文字数<br>justification: // 行揃え 0=左 1=右 2=中央<br>],... ]   省略可 |

**解説**

テキストレイヤの本文とラン構成/段落構成をまとめて差し替える。

setLayerText はスタイルを先頭ランに畳んでしまうので、本文を変えつつ
部分ごとに書式を変えたい場合はこちらを使う。

runs / paragraphs の length は UTF-16 コードユニット数(絵文字等サロゲート
ペアは 2)。length の合計が本文長と合わない場合は末尾要素が過不足を吸収する
(伸ばす/切り詰める)。長さ 0 の要素は捨てられる。void や空配列を渡すと
単一ラン/単一段落に畳まれる。末尾に改行(\r)が無ければ補われる。
各ランのスタイルは「元の先頭ランを雛形にして指定キーだけ上書き」なので、
指定しなかった書式は元の見た目のまま残る。

テキストレイヤ以外の場合は例外。

---

### setLayerJustification

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `justification` | `&nbsp;` | 行揃え 0=左 1=右 2=中央 |
| `paraIndex` | `-1` | 対象段落番号(getLayerInfo().text.paragraphs に対応)。<br>負値で全段落。既定 -1 |

**解説**

テキストレイヤの段落の行揃えだけを変更する(本文もラン構成も変えない)。

テキストレイヤ以外や paraIndex 範囲外の場合は例外。

---

### getLayerFonts

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

フォント名の配列

**解説**

テキストレイヤが持つフォント名の一覧を返す(フォント選択 UI の候補用)。

setLayerRunStyle / setLayerRichText の font に渡せる名前。
テキストレイヤ以外の場合は例外。

---

### getLayerTextTransform

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

`[ xx, xy, yx, yy, tx, ty ]` (tx,ty=平行移動)

**解説**

テキストレイヤの配置(アフィン変換)を取得する。

getLayerInfo().text.transform と同じ値。テキストレイヤ以外は例外。

---

### setLayerTextTransform

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `matrix` | `&nbsp;` | [ xx, xy, yx, yy, tx, ty ] の 6 要素配列 |

**解説**

テキストレイヤの配置(アフィン変換)を差し替える。

書き換わるのはテキスト情報だけで、レイヤ矩形(焼き込み済みラスタ)は
動かない。単純な平行移動には moveTextLayer を使うこと。
テキストレイヤ以外や要素数不足の場合は例外。

---

### moveTextLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `dx` | `&nbsp;` | X 移動量(px) |
| `dy` | `&nbsp;` | Y 移動量(px) |

**解説**

テキストレイヤを平行移動する。アフィン変換の tx/ty とレイヤ矩形

(マスク矩形があればそれも)を同じだけずらすので、PSD 内蔵のラスタも
一緒に動く。テキストレイヤ以外の場合は例外。

---

### getLayerTextBounds

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |

**戻り値**

%[ left:, top:, right:, bottom: ]

**解説**

テキストレイヤの流し込み枠を取得する(アフィン変換のローカル座標。

文書上の位置は transform の tx/ty を足したもの)。
テキストレイヤ以外の場合は例外。

---

### setLayerTextBounds

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | レイヤ番号 |
| `left` | `&nbsp;` | 左 |
| `top` | `&nbsp;` | 上 |
| `right` | `&nbsp;` | 右 |
| `bottom` | `&nbsp;` | 下 |

**解説**

テキストレイヤの流し込み枠を差し替える(アフィン変換のローカル座標)。

実際に流し込みが変わるのは段落テキスト(ボックステキスト)のみで、
ポイントテキストでは Photoshop 側が字形から枠を作り直す。
テキストレイヤ以外の場合は例外。

---

### clearStorageCache

メソッド

**解説**

static method

ストレージとして保持されてるキャッシュをクリアする

---
