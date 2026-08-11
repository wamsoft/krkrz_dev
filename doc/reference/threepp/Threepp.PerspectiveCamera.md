# Threepp.PerspectiveCamera

透視投影カメラ

人間の目のような透視投影を行うカメラです。

## メンバー一覧

### コンストラクタ

- [PerspectiveCamera](#perspectivecamera)

### プロパティ

- [type](#type)
- [fov](#fov)
- [aspect](#aspect)
- [focus](#focus)
- [filmGauge](#filmgauge)
- [filmOffset](#filmoffset)

### メソッド

- [setFocalLength](#setfocallength)
- [getFocalLength](#getfocallength)
- [getEffectiveFOV](#geteffectivefov)
- [getFilmWidth](#getfilmwidth)
- [getFilmHeight](#getfilmheight)
- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)

---

### PerspectiveCamera

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fov` | `60` | 視野角（度） |
| `aspect` | `1` | アスペクト比 |
| `near` | `0.1` | ニアクリップ面 |
| `far` | `2000` | ファークリップ面 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"PerspectiveCamera"（読み取り専用）

---

### fov

プロパティ \ アクセス: `r/w`

**解説**

視野角（度）

---

### aspect

プロパティ \ アクセス: `r/w`

**解説**

アスペクト比

---

### focus

プロパティ \ アクセス: `r/w`

**解説**

フォーカス距離

---

### filmGauge

プロパティ \ アクセス: `r/w`

**解説**

フィルムゲージ（mm）

---

### filmOffset

プロパティ \ アクセス: `r/w`

**解説**

フィルムオフセット

---

### setFocalLength

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `focalLength` | `&nbsp;` |  |

**解説**

焦点距離を設定

---

### getFocalLength

メソッド

**解説**

焦点距離を取得

---

### getEffectiveFOV

メソッド

**解説**

実効視野角を取得

---

### getFilmWidth

メソッド

**解説**

フィルム幅を取得

---

### getFilmHeight

メソッド

**解説**

フィルム高さを取得

---

### setViewOffset

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fullWidth` | `&nbsp;` |  |
| `fullHeight` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**解説**

ビューオフセットを設定

---

### clearViewOffset

メソッド

**解説**

ビューオフセットをクリア

---

### updateProjectionMatrix

メソッド

**解説**

投影行列を更新

---
