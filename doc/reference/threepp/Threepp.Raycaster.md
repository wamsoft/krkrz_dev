# Threepp.Raycaster

レイキャスター

レイを使ってオブジェクトとの交差判定を行います。

## メンバー一覧

### コンストラクタ

- [Raycaster](#raycaster)

### プロパティ

- [nearPlane](#nearplane)
- [farPlane](#farplane)

### メソッド

- [set](#set)
- [setFromCameraNDC](#setfromcamerandc)
- [setFromCameraPixel](#setfromcamerapixel)
- [intersectObjects](#intersectobjects)

---

### Raycaster

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `origin` | `&nbsp;` | 原点 |
| `direction` | `&nbsp;` | 方向 |
| `near` | `0` | ニアクリップ |
| `far` | `Infinity` | ファークリップ |

**解説**

コンストラクタ

---

### nearPlane

プロパティ \ アクセス: `r/w`

**解説**

ニアクリップ

---

### farPlane

プロパティ \ アクセス: `r/w`

**解説**

ファークリップ

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

**解説**

原点と方向を設定 (direction は正規化前提)

---

### setFromCameraNDC

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `ndcX` | `&nbsp;` | 正規化デバイス座標 X [-1,1] (画面左端 -1, 右端 +1) |
| `ndcY` | `&nbsp;` | 正規化デバイス座標 Y [-1,1] (画面下端 -1, 上端 +1) |
| `camera` | `&nbsp;` | PerspectiveCamera または OrthographicCamera |

**解説**

カメラと正規化デバイス座標からレイを設定する (three.js の setFromCamera 相当)

---

### setFromCameraPixel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `px` | `&nbsp;` | ピクセル X (左上原点。吉里吉里レイヤ座標) |
| `py` | `&nbsp;` | ピクセル Y (左上原点。下方向が +) |
| `viewW` | `&nbsp;` | ビューポート幅 (描画レイヤの幅) |
| `viewH` | `&nbsp;` | ビューポート高さ (描画レイヤの高さ) |
| `camera` | `&nbsp;` | カメラ |

**解説**

ピクセル座標(左上原点)+ビューポートサイズからレイを設定する利便版

マウス座標をそのまま渡せる。内部で NDC に変換する。

---

### intersectObjects

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `objects` | `&nbsp;` | 判定対象の Object3D 配列 (例: [vrm.getScene(), boxMesh]) |
| `recursive` | `true` | 子孫まで再帰的に判定するか (省略時 true) |

**戻り値**

ヒット配列。各要素は辞書:
object   … 引数配列で渡した「ヒットしたルートオブジェクト」(同一インスタンス)。
recursive で子孫にヒットしても、対応する引数配列内の祖先を返す。
distance … レイ原点からの距離
x, y, z  … ワールド座標のヒット点
配列は距離の昇順 (result[0] が最も手前)。ヒット無しは count=0。

**解説**

オブジェクト群との交差判定を行い、ヒットを距離の近い順の配列で返す

---
