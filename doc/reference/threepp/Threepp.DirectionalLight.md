# Threepp.DirectionalLight

平行光源（太陽光のような光）

無限遠から平行に照射される光源です。影を落とすことができます。

## メンバー一覧

### コンストラクタ

- [DirectionalLight](#directionallight)

### プロパティ

- [type](#type)

### メソッド

- [setShadowMapSize](#setshadowmapsize)
- [setShadowBias](#setshadowbias)
- [setShadowNormalBias](#setshadownormalbias)
- [setShadowRadius](#setshadowradius)
- [setShadowNearFar](#setshadownearfar)
- [setShadowOrthoBounds](#setshadoworthobounds)
- [dispose](#dispose)

---

### DirectionalLight

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光の色 (0xRRGGBB) |
| `intensity` | `void` | 光の強度 |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

"DirectionalLight"（読み取り専用）

---

### setShadowMapSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

--- 影(ShadowMap) --- このライトで影を落とすには castShadow=true にし、 renderer.setShadowMapEnabled(true) と、影を受ける側の receiveShadow=true が必要。 平行光源の影は正投影カメラで焼くので、シーンを覆う範囲を setShadowOrthoBounds で指定する。

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

### setShadowOrthoBounds

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |

**解説**

平行光源の影範囲(正投影)

---

### dispose

メソッド

**解説**

リソースを解放

---
