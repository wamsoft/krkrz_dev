# Threepp.OrthographicCamera

正射影カメラ

2Dシーンやアイソメトリックビューに適したカメラです。

## メンバー一覧

### コンストラクタ

- [OrthographicCamera](#orthographiccamera)

### プロパティ

- [type](#type)
- [left](#left)
- [right](#right)
- [top](#top)
- [bottom](#bottom)

### メソッド

- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)

---

### OrthographicCamera

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `-1` | 左端 |
| `right` | `1` | 右端 |
| `top` | `1` | 上端 |
| `bottom` | `-1` | 下端 |
| `near` | `0.1` | ニアクリップ面 |
| `far` | `2000` | ファークリップ面 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"OrthographicCamera"（読み取り専用）

---

### left

プロパティ \ アクセス: `r/w`

**解説**

左端

---

### right

プロパティ \ アクセス: `r/w`

**解説**

右端

---

### top

プロパティ \ アクセス: `r/w`

**解説**

上端

---

### bottom

プロパティ \ アクセス: `r/w`

**解説**

下端

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
