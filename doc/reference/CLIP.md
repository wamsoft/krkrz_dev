# CLIP

擬似コードによるマニュアル

CLIP STUDIO PAINT (.clip) 読み込み / 編集プラグイン clipfile.dll

CLIPファイルストレージ機能
以下のパス名で CLIP ファイルのレイヤ画像を直接ファイルとしてロードできます

clip://CLIPファイル名/root/フォルダ名/.../レイヤ名.bmp
clip://CLIPファイル名/id/LayerId.bmp

・CLIPファイル名はベース名のみで小文字で正規化されます
・フォルダ名、レイヤ名は全て小文字で正規化されて含まれる"/" は "_" に置換されます
・名前が重複する場合は後にあるものが優先になります
・画像を持たないレイヤ(フォルダ・調整レイヤ・空レイヤ)は列挙されません

psdfile プラグインの psd:// と同じ規則です。

## メンバー一覧

### プロパティ

- [width](#width)
- [height](#height)
- [resolution](#resolution)
- [layer_count](#layer_count)
- [root_layer](#root_layer)
- [is_loaded](#is_loaded)
- [error](#error)

### メソッド

- [load](#load)
- [loadOctet](#loadoctet)
- [clearData](#cleardata)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getRoots](#getroots)
- [getChildren](#getchildren)
- [getLayerIndexById](#getlayerindexbyid)
- [getLayerAttribute](#getlayerattribute)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getLayerRegion](#getlayerregion)
- [getBlend](#getblend)
- [getPreviewPNG](#getpreviewpng)
- [check](#check)
- [clearStorageCache](#clearstoragecache)

---

### width

プロパティ \ アクセス: `r`

**解説**

キャンバスの横幅(実ピクセル)。

CLIP の Canvas.CanvasWidth は CanvasUnit 依存で mm 単位のファイルが実在する
ため、100% ミップの属性から求めた実ピクセル値を返します。未ロードは -1

---

### height

プロパティ \ アクセス: `r`

**解説**

キャンバスの縦幅(実ピクセル)。未ロードは -1

---

### resolution

プロパティ \ アクセス: `r`

**解説**

解像度(dpi)。未ロードは 0

---

### layer_count

プロパティ \ アクセス: `r`

**解説**

レイヤ数。未ロードは -1

---

### root_layer

プロパティ \ アクセス: `r`

**解説**

ルートフォルダの LayerId。未ロードは -1

---

### is_loaded

プロパティ \ アクセス: `r`

**解説**

ロード済みかどうか

---

### error

プロパティ \ アクセス: `r`

**解説**

直近の失敗理由。無ければ空文字列

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名 |

**戻り値**

ロードに成功したら true(失敗理由は error プロパティ)

**解説**

CLIP ファイルのロード。

ローカルに実体があるファイルは mmap で開き、画素は 256x256 ブロック単位で
必要になったときだけ読みます(大きなファイルでも load 自体は軽い)。
アーカイブ内などローカルパスに落ちない場合はストリームから全体をメモリへ
読み込んでから解析します。

---

### loadOctet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `data` | `&nbsp;` | ファイル全体を格納した octet |

**戻り値**

ロードに成功したら true

**解説**

octet に入った CLIP データをロードする。

バイト列はこのオブジェクトが保持します。ファイル名を持たないため
clip:// ストレージへは登録されません。

---

### clearData

メソッド

**解説**

保持しているデータを明示的に破棄する。

吉里吉里のオブジェクト寿命は GC 依存なので、大きなファイルを掴んだままに
したくないときに呼びます。

---

### getLayerName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

レイヤ名

**解説**

レイヤ名の取得

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
left         左座標(キャンバス座標)
top          上座標
right        右座標
bottom       底座標
width        横幅
height       縦幅
name         レイヤ名
layer_id     LayerId (CLIP の Layer.MainId)。CLIPWriter の各メソッドや
clip://~/id/ で使うのはこの値
visible      表示状態
opacity      不透明度 0..255 (PSD / 吉里吉里 と揃えた値)
opacity_raw  不透明度の生値 0..**256** (CLIP は 256 段)
clipping     下のレイヤでクリッピングするか (0/1)
composite    合成モードの生値 (CLIP の LayerComposite。CLIPWriter の
composite_* 定数と同じ値)
type         合成モード(吉里吉里の対応モード)。対応が無いモードは
ltPsNormal に落ちるので、正確に見たいときは composite を使う
blend_mode_key 合成モードを PSD の 4 文字コードで表したもの。psdfile の
getLayerInfo().blend_mode_key と見比べるとき用
is_group     フォルダレイヤか
is_filter    調整レイヤか(自分の画素を持たない)
is_text      テキストレイヤか
has_mask     レイヤマスクを持つか
folder       フォルダ属性の生値 (bit0=フォルダ / bit4=折り畳み)
collapsed    フォルダが折り畳まれているか
layer_type_raw LayerType の生値 (bit12(4096)=調整レイヤ / bit1(2)=マスク有)
parent_index 親フォルダのレイヤ番号(最上位は -1)
children     直接の子のレイヤ番号配列(下から上)。フォルダ以外は空配列

**解説**

レイヤ情報の取得

レイヤ番号 no は 0 から layer_count-1 までで、並び順は psdfile と同じ
「中身が先、フォルダが後、下から上」の平坦順です。

---

### getRoots

メソッド

**戻り値**

レイヤ番号の配列

**解説**

最上位(ルート直下)のレイヤ番号配列を取得する。下から上の順

---

### getChildren

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |

**戻り値**

レイヤ番号の配列(フォルダ以外は空配列)

**解説**

フォルダの直接の子のレイヤ番号配列を取得する。下から上の順

---

### getLayerIndexById

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | getLayerInfo().layer_id の値 |

**戻り値**

レイヤ番号。見つからなければ -1

**解説**

LayerId からレイヤ番号を引く

---

### getLayerAttribute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | レイヤ番号 |
| `mask` | `false` | true でマスク側のミップ連鎖を見る。既定 false |

**戻り値**

%[ width:, height:,        // 論理サイズ
cols:, rows:,           // ブロックグリッド
color_mode:             // 33=RGBA / 17=グレー・モノクロ / 1=マスク
num_channels:           // 4 / 1 / 0
bit_depth:              // 5=8bpp RGBA / 2=8bpp / 1=1bpp
plane_bytes:,
block_width:, block_height:,
has_init_color:,
init_color:             // RGBA をパックした値
block_count:            // ブロック数
]  実体が無ければ void

**ここで返る width / height はキャンバスサイズとは限りません** — CSP は
レイヤによって 256x256 ブロック境界に切り上げた大きさ(300x400 のキャンバスでも
512x512 等)で画素を持ちます。`CLIPWriter.setPixels` に渡す Layer のサイズは
この値に合わせる必要があるので、書き換えるときはここで調べてください。

**解説**

100% ミップの Offscreen 属性を取得する(ブロックグリッドや表現色の確認用)

---

### getLayerData

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号<br>フォルダ・調整レイヤ・空レイヤは画像を持たないので何もしません<br>(吉里吉里の Layer は 0 サイズにできないため)。<br>データ内容のほか以下のプロパティが自動的にレイヤに設定されます<br>left          左座標<br>top           上座標<br>width         横幅<br>height        縦幅<br>type          合成モード<br>opacity       不透明度(0..255 に正規化した値)<br>visible       表示状態<br>imageLeft     0になります<br>imageTop      0になります<br>imageWidth    width になります<br>imageHeight   height になります<br>name          name が設定されます |

**解説**

レイヤ画像の読み出し(マスクをアルファに繰り込んだもの)

---

### getLayerDataRaw

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号 |

**解説**

レイヤ画像の読み出し(マスクを繰り込まない生画像)。

設定されるプロパティは getLayerData と同じ

---

### getLayerDataMask

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号 |

**解説**

レイヤのマスクのみ(グレー)の読み出し。

マスクを持たないレイヤでは何もしません。
opacity は 255、type は ltPsNormal になります

---

### getLayerRegion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 読み出し先レイヤ |
| `no` | `&nbsp;` | レイヤ番号 |
| `x` | `&nbsp;` | 矩形の左(キャンバス座標) |
| `y` | `&nbsp;` | 矩形の上 |
| `w` | `&nbsp;` | 矩形の幅 |
| `h` | `&nbsp;` | 矩形の高さ |
| `mode` | `image_mode_masked` | image_mode_*(既定 image_mode_masked) |

**解説**

レイヤ画像のうち指定矩形(キャンバス座標)だけを読み出す。

CLIP は画素を 256x256 タイルで持っているので、**重なるタイルしか
展開されません**。大きなレイヤの一部だけ欲しいときはこちらが安いです
(PSD は行 RLE なので同じことができない = clipparse 固有の口)。
読み出し先 Layer の left/top には x/y が設定されます。

---

### getBlend

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 格納先レイヤ(キャンバスサイズに調整される) |

**戻り値**

取得に成功したら true

**解説**

全レイヤを下から合成した画像の取得。

psdfile の getBlend が「PSD に保存済みの合成結果を読むだけ」なのとは違い、
こちらは clipparse 側で実際に合成します(CSP の CanvasPreview と一致するのが
正しい状態)。合成モード 27 種・表現色 4 種・マスク・クリッピング・
通過フォルダ・調整レイヤ 5 種に対応しています。
保存済みの完成画をそのまま使いたいだけなら getPreviewPNG() の方が安いです。

---

### getPreviewPNG

メソッド

**戻り値**

PNG データの octet。無ければ void

**解説**

ファイルに埋まっている完成画(CanvasPreview)を PNG の octet で返す。

CSP が保存した画そのものなので合成の計算が不要ですが、**等倍とは限りません**。

---

### check

メソッド

**戻り値**

問題があればレポート文字列、問題が無ければ void

**解説**

全ブロックの構造アサーションを回す(診断用)

---

### clearStorageCache

メソッド

**解説**

static method

ストレージとして保持されてるキャッシュをクリアする

---
