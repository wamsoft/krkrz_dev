# Threepp.PointLight

点光源

一点から全方向に照射される光源です。

影の設定は DirectionalLight と同様です。ただし setShadowOrthoBounds は平行光源専用で、点光源では効果がありません。

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

シャドウマップ解像度 (既定 2048x2048)

---

### setShadowBias

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**解説**

影のアクネ対策バイアス (例 -0.0005)

---

### setShadowNormalBias

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**解説**

法線方向バイアス

---

### setShadowRadius

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |

**解説**

ソフトシャドウ半径 (PCF)

---

### setShadowNearFar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**解説**

影用カメラの near/far

---

### dispose

メソッド

**解説**

リソースを解放

---
