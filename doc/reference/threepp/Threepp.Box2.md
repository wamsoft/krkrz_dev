# Threepp.Box2

2D 軸平行境界ボックスクラス

============================================================ 追加 Math クラス ============================================================

## メンバー一覧

### コンストラクタ

- [Box2](#box2)

### プロパティ

- [min](#min)
- [max](#max)

### メソッド

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeEmpty](#makeempty)
- [isEmpty](#isempty)
- [expandByPoint](#expandbypoint)
- [expandByVector](#expandbyvector)
- [expandByScalar](#expandbyscalar)
- [containsPoint](#containspoint)
- [containsBox](#containsbox)
- [intersectsBox](#intersectsbox)
- [distanceToPoint](#distancetopoint)
- [intersect](#intersect)
- [union_](#union_)
- [translate](#translate)
- [equals](#equals)

---

### Box2

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` | 最小座標 (Vector2) |
| `max` | `&nbsp;` | 最大座標 (Vector2) |

**解説**

コンストラクタ

---

### min

プロパティ \ アクセス: `r/w`

**解説**

最小座標（読み取り専用）

---

### max

プロパティ \ アクセス: `r/w`

**解説**

最大座標（読み取り専用）

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**解説**

値を設定

---

### clone

メソッド

**解説**

クローン

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

コピー

---

### makeEmpty

メソッド

**解説**

空にする

---

### isEmpty

メソッド

**解説**

空かどうか

---

### expandByPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点で拡張

---

### expandByVector

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

ベクトルで拡張

---

### expandByScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラーで拡張

---

### containsPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点を含むか

---

### containsBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

ボックスを含むか

---

### intersectsBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

ボックスと交差するか

---

### distanceToPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**解説**

点との距離

---

### intersect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

交差部分を取得

---

### union_

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

和集合

---

### translate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `offset` | `&nbsp;` |  |

**解説**

平行移動

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**解説**

等価判定

---
