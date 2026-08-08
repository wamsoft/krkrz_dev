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
- [color_mode](#color_mode)
- [layer_count](#layer_count)
- [hresolution](#hresolution)
- [vresolution](#vresolution)

### メソッド

- [load](#load)
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
- [save](#save)
- [createBlank](#createblank)
- [deleteLayer](#deletelayer)
- [moveLayer](#movelayer)
- [duplicateLayer](#duplicatelayer)
- [copyLayerFrom](#copylayerfrom)
- [setLayerName](#setlayername)
- [setFillOpacity](#setfillopacity)
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
blend_mode   合成モード
opacity      不透明度
fill_opacity 塗りの不透明度
visible      表示状態
name         レイヤ名
layer_id     レイヤID
group_layer_id 親レイヤID
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
transform:     // アフィン変換 [ xx, xy, yx, yy, tx, ty ](tx,ty=平行移動)
runs: [        // 文字スタイルのラン配列(本文の並び順)
%[ length:       // 適用文字数(UTF-16 コードユニット。絵文字等サロゲートは2)
font:         // 解決済みフォント名
size_px:      // フォントサイズ(pt)
color:        // RGBA 各 0..1 の配列 [ r, g, b, a ](未指定なら存在しない)
tracking:     // トラッキング(字送り, 1/1000 em)
kerning:      // 手動カーニング
auto_kerning: // 自動カーニング(メトリクス/オプティカル)有効か
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

**戻り値**

成功したら true

**解説**

この PSD を空の 8bit RGB 文書(白の合成画像)として初期化する。

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
%[ size_px:   // フォントサイズ(px)
color:     // RGBA 各 0..1 の配列 [ r, g, b, a ]
tracking:  // トラッキング(1/1000 em)
kerning:   // 手動カーニング
bold:      // 疑似ボールド(FauxBold) true/false
italic:    // 疑似イタリック(FauxItalic) true/false
underline: // 下線(Underline) true/false
]
テキストレイヤ以外や runIndex 範囲外の場合は例外。

---

### clearStorageCache

メソッド

**解説**

static method

ストレージとして保持されてるキャッシュをクリアする

---
