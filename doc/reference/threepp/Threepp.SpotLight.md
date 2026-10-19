# Threepp.SpotLight

スポットライト

一点から円錐状に照射される光源です。

影の設定は DirectionalLight と同様です。スポットライトの影は透視カメラで焼きます (角度は angle に依存)。

## メンバー一覧

### コンストラクタ

- [SpotLight](#spotlight)

### プロパティ

- [type](#type)
- [distance](#distance)
- [angle](#angle)
- [penumbra](#penumbra)
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

### SpotLight

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光の色 (0xRRGGBB) |
| `intensity` | `void` | 光の強度 |
| `distance` | `0` | 光が届く距離 |
| `angle` | `PI/3` | 照射角度（ラジアン） |
| `penumbra` | `0` | ペナンブラ（ぼかし） |
| `decay` | `1` | 減衰率 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"SpotLight"（読み取り専用）

---

### distance

プロパティ \ アクセス: `r/w`

**解説**

光が届く距離

---

### angle

プロパティ \ アクセス: `r/w`

**解説**

照射角度

---

### penumbra

プロパティ \ アクセス: `r/w`

**解説**

ペナンブラ

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
