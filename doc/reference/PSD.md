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

### clearStorageCache

メソッド

**解説**

static method

ストレージとして保持されてるキャッシュをクリアする

---
