# GdiPlus.Image

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

画像情報を取り扱うクラス
※ベクトル画像データの領域は座標が負の領域にある場合もあります

### メンバー一覧

#### コンストラクタ

- [Image](#image)

#### メソッド

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)
- [GetHorizontalResolution](#gethorizontalresolution)
- [GetVerticalResolution](#getverticalresolution)
- [GetWidth](#getwidth)
- [GetHeight](#getheight)
- [GetFlags](#getflags)
- [GetLastStatus](#getlaststatus)
- [GetPixelFormat](#getpixelformat)
- [GetType](#gettype)
- [RotateFlip](#rotateflip)

---

### Image

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `void` | ファイル名。指定された場合は自動的にロードします |

**解説**

コンストラクタ

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 画像ファイル名 |

**解説**

画像をロードする

---

### Clone

メソッド

**戻り値**

このオブジェクトの複製(Image)

---

### GetBounds

メソッド

**戻り値**

Bounds情報(RectF) 単位 pixel

**解説**

Bounds情報の取得

---

### GetHorizontalResolution

メソッド

**戻り値**

水平方向解像度(dpi)

---

### GetVerticalResolution

メソッド

**戻り値**

垂直方向解像度(dpi)

---

### GetWidth

メソッド

**戻り値**

横幅 (pixel値：整数)

---

### GetHeight

メソッド

**戻り値**

縦幅 (pixel値:整数)

---

### GetFlags

メソッド

---

### GetLastStatus

メソッド

---

### GetPixelFormat

メソッド

---

### GetType

メソッド

---

### RotateFlip

メソッド

---

## プラグイン拡張: layerExVector

画像情報を取り扱うクラス
※ベクトル画像データの領域は座標が負の領域にある場合もあります

### メンバー一覧

#### コンストラクタ

- [Image](#image)

#### プロパティ

- [width](#width)
- [height](#height)
- [isLoaded](#isloaded)

#### メソッド

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)

---

### Image

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `void` | ファイル名。指定された場合は自動的にロードします |

**解説**

コンストラクタ

---

### width

プロパティ \ アクセス: `r`

**解説**

横幅 (read only)

---

### height

プロパティ \ アクセス: `r`

**解説**

縦幅 (read only)

---

### isLoaded

プロパティ \ アクセス: `r`

**解説**

ロード済みかどうか (read only)

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 画像ファイル名 |

**解説**

画像をロードする

---

### Clone

メソッド

**戻り値**

このオブジェクトの複製(Image)

---

### GetBounds

メソッド

**戻り値**

Bounds情報(RectF) 単位 pixel

**解説**

Bounds情報の取得

---
