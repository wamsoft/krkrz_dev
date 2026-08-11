# Threepp.PointLight

点光源

一点から全方向に照射される光源です。

## メンバー一覧

### コンストラクタ

- [PointLight](#pointlight)

### プロパティ

- [type](#type)
- [distance](#distance)
- [decay](#decay)

### メソッド

- [getPower](#getpower)
- [setPower](#setpower)
- [setShadowMapSize](#setshadowmapsize)
- [setShadowBias](#setshadowbias)
- [setShadowNormalBias](#setshadownormalbias)
- [setShadowRadius](#setshadowradius)
- [setShadowNearFar](#setshadownearfar)
- [dispose](#dispose)

---

### PointLight

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光の色 (0xRRGGBB) |
| `intensity` | `void` | 光の強度 |
| `distance` | `0` | 光が届く距離（0で無限） |
| `decay` | `1` | 減衰率 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"PointLight"（読み取り専用）

---

### distance

プロパティ \ アクセス: `r/w`

**解説**

光が届く距離

---

### decay

プロパティ \ アクセス: `r/w`

**解説**

減衰率

---

### getPower

メソッド

**解説**

光のパワーを取得

---

### setPower

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `power` | `&nbsp;` |  |

**解説**

光のパワーを設定

---

### setShadowMapSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

--- 影(ShadowMap) --- ※ setShadowOrthoBounds は平行光源専用(点光源では無効)

---

### setShadowBias

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

---

### setShadowNormalBias

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

---

### setShadowRadius

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |

---

### setShadowNearFar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

---

### dispose

メソッド

**解説**

リソースを解放

---
