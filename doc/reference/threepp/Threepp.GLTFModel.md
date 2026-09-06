# Threepp.GLTFModel

ロード済み glTF モデル (GLTFLoader の戻り値)

モデルのシーングラフとアニメ情報を保持する。

## メンバー一覧

### メソッド

- [getScene](#getscene)
- [getAnimationCount](#getanimationcount)
- [getAnimationName](#getanimationname)
- [getAnimationDuration](#getanimationduration)
- [getPartCount](#getpartcount)
- [getPartGeometry](#getpartgeometry)
- [getPartMaterial](#getpartmaterial)
- [getPartName](#getpartname)

---

### getScene

メソッド

**解説**

-> Threepp.Group (Scene に add して描画)

---

### getAnimationCount

メソッド

**解説**

-> int (内蔵アニメクリップ数)

---

### getAnimationName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**解説**

(i) -> string (クリップ名)

---

### getAnimationDuration

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**解説**

(i) -> float (秒)

---

### getPartCount

メソッド

**解説**

--- パーツ (メッシュ) の取り出し --- 同じモデルを何百個も並べたいとき、GLB を個数ぶん読んで Mesh を並べると draw call がそのまま個数になる。ここから取り出して InstancedMesh へ まとめると 1 個で済む。

---

### getPartGeometry

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**解説**

(i) -> BufferGeometry

---

### getPartMaterial

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**解説**

(i) -> Material (元を共有。テクスチャを持つため)

---

### getPartName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**解説**

(i) -> string (どのパーツか見分ける用)

---
