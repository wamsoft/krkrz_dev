# CLIPWriter

CLIP ファイルの編集 / 書き出しクラス。

読み側(CLIP)とは別クラスです。編集元をメモリへ全部読む(mmap しない)ので
同じパスへ書き戻せます。

**書いたファイルは validate() を通してから CSP で開いてください。**
「こちらのリーダでは読めるのに CSP が受け付けない」種類の間違い(格納型・
ミップ段数・チェックサム・サムネイルの世代番号・CanvasPreview)は
clipparse 側が面倒を見ていますが、参照整合性の崩れは validate() でしか
検出できません。引っかかる状態のファイルは CSP で落ちたり全面透明になります。

使用例:
var w = new CLIPWriter();
w.load("in.clip");
w.setLayerAttr(5, %[ opacity: 128, composite: CLIPWriter.composite_multiply ]);
w.save("out.clip");
var problems = CLIPWriter.validate("out.clip");
if (problems.count) Debug.message(problems.join("\n"));

## メンバー一覧

### プロパティ

- [error](#error)
- [external_count](#external_count)

### メソッド

- [load](#load)
- [save](#save)
- [clearData](#cleardata)
- [setLayerAttr](#setlayerattr)
- [setPixels](#setpixels)
- [addLayer](#addlayer)
- [deleteLayer](#deletelayer)
- [dropThumbnail](#dropthumbnail)
- [setCanvasPreview](#setcanvaspreview)
- [resizeCanvas](#resizecanvas)
- [setSeed](#setseed)
- [validate](#validate)

---

### error

プロパティ \ アクセス: `r`

**解説**

直近の失敗理由。無ければ空文字列。

**成功時にクリアされないので、戻り値が false のときだけ読むこと。**

---

### external_count

プロパティ \ アクセス: `r`

**解説**

外部チャンク(CHNKExta)の数

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名(ローカルパスに落ちる必要があります。<br>アーカイブ内のファイルは編集元にできず例外になります) |

**戻り値**

成功したら true(失敗理由は error プロパティ)

**解説**

編集元の CLIP ファイルを読む

---

### save

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 保存先ファイル名(ローカルパス) |

**戻り値**

書いたバイト数。失敗で 0

**解説**

現在の状態でファイルを組み立てて書き出す。

無変更で書き戻した場合は元ファイルと sha256 が一致します。

---

### clearData

メソッド

**解説**

保持しているデータを明示的に破棄する

---

### setLayerAttr

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId (CLIP.getLayerInfo().layer_id の値) |
| `attr` | `&nbsp;` | 属性辞書 |

**戻り値**

成功したら true

**解説**

レイヤ属性を編集する。attr 辞書のうち指定されたキーだけ変更します

%[ name:       // レイヤ名
opacity:    // 不透明度 0..**256** (CLIP は 256 段。0..255 ではない)
visibility: // 表示状態 0/1
composite:  // 合成モード(composite_* 定数)
clipping:   // 下のレイヤでクリッピングするか
folder:     // フォルダ属性 (bit0=フォルダ / bit4=折り畳み)
]

---

### setPixels

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |
| `layer` | `&nbsp;` | 画素供給元 Layer |

**戻り値**

成功したら true

**解説**

レイヤの画素を Layer オブジェクトの内容で差し替える。

**Layer のサイズはそのレイヤの 100% ミップの寸法と一致していなければ
なりません。これはキャンバスサイズとは限りません** — CSP はレイヤによって
256x256 ブロック境界に切り上げた大きさ(300x400 のキャンバスでも 512x512 等)
で持つことがあります。必要な寸法は読み側の
`CLIP.getLayerAttribute(レイヤ番号)` の width / height で調べられます:

var a = clip.getLayerAttribute(3);
lay.setImageSize(a.width, a.height);
lay.setSizeToImageSize();
// ... lay に描く ...
w.setPixels(clip.getLayerInfo(3).layer_id, lay);

寸法が合わないと false が返り、error に
"pixel size does not match the 100% mipmap" が入ります。
RGBA プレーンのレイヤのみ対応 (getLayerAttribute().num_channels == 4)。

---

### addLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 新しいレイヤ名 |
| `copyFrom` | `&nbsp;` | 雛形にする既存レイヤの LayerId |
| `layer` | `void` | 画素供給元 Layer(省略/void で全面透明) |
| `after` | `-1` | この LayerId の直上に挿す。負値で最上段。既定 -1 |
| `parent` | `0` | 親フォルダの LayerId。0 でルート直下。既定 0 |

**戻り値**

新しいレイヤの LayerId。失敗で 0

**解説**

既存レイヤを雛形にレイヤを追加する。

雛形から表現色などの属性を引き継ぐので、追加元のレイヤを選ぶことが必要です。

---

### deleteLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |

**戻り値**

成功したら true

**解説**

レイヤを削除する

---

### dropThumbnail

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |

**戻り値**

成功したら true

**解説**

サムネイルの実体だけ落として世代番号を立てる(CSP が開いたときに作り直す)。

画素を差し替えたのに古いサムネイルが残るのを避けたいとき用ですが、
setPixels / addLayer が内部で面倒を見るので通常は呼ぶ必要はありません。

---

### setCanvasPreview

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 画素供給元 Layer |

**戻り値**

成功したら true

**解説**

開いた直後に表示される画像(CanvasPreview)を差し替える

---

### resizeCanvas

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 新しい幅 |
| `height` | `&nbsp;` | 新しい高さ |
| `dpi` | `0` | 解像度(0 で据え置き)。既定 0 |

**戻り値**

成功したら true

**解説**

キャンバスの寸法ごと作り替える(ミップ連鎖を伸縮させる)。

**画素の実体は全部落ちるので、呼んだあと setPixels で入れ直してください。**

---

### setSeed

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `seed` | `&nbsp;` | 乱数種 |

**解説**

外部 ID の乱数種を固定する(テストで出力の再現性が要るとき)

---

### validate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 検査するファイル(ローカルパス) |

**戻り値**

問題点の文字列配列。空配列なら問題なし

**解説**

static method

参照整合性を検査する。**CSP で開く前に必ず通すこと。**
ミップ段数 / 閉路 / 孤児行 / 格納型 / 消えたレイヤへの参照を見ます。

---
