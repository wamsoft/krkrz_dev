# Threepp.Matrix4

4x4 行列クラス

変換行列を表現します。

## メンバー一覧

### コンストラクタ

- [Matrix4](#matrix4)

### メソッド

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [copyPosition](#copyposition)
- [extractBasis](#extractbasis)
- [makeBasis](#makebasis)
- [extractRotation](#extractrotation)
- [makeRotationFromEuler](#makerotationfromeuler)
- [makeRotationFromQuaternion](#makerotationfromquaternion)
- [lookAt](#lookat)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [transpose](#transpose)
- [setPosition](#setposition)
- [invert](#invert)
- [scale](#scale)
- [getMaxScaleOnAxis](#getmaxscaleonaxis)
- [makeTranslation](#maketranslation)
- [makeRotationX](#makerotationx)
- [makeRotationY](#makerotationy)
- [makeRotationZ](#makerotationz)
- [makeRotationAxis](#makerotationaxis)
- [makeScale](#makescale)
- [makeShear](#makeshear)
- [compose](#compose)
- [decompose](#decompose)
- [makePerspective](#makeperspective)
- [makeOrthographic](#makeorthographic)
- [equals](#equals)

---

### Matrix4

コンストラクタ

**解説**

コンストラクタ

単位行列を生成します

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n14` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n24` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |
| `n34` | `&nbsp;` |  |
| `n41` | `&nbsp;` |  |
| `n42` | `&nbsp;` |  |
| `n43` | `&nbsp;` |  |
| `n44` | `&nbsp;` |  |

**解説**

要素を設定

---

### identity

メソッド

**解説**

単位行列に設定

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

コピー

---

### copyPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

位置成分のみコピー

---

### extractBasis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**解説**

基底ベクトルを抽出

---

### makeBasis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**解説**

基底ベクトルから行列を生成

---

### extractRotation

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

回転成分を抽出

---

### makeRotationFromEuler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**解説**

オイラー角から回転行列を生成

---

### makeRotationFromQuaternion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

クォータニオンから回転行列を生成

---

### lookAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `eye` | `&nbsp;` |  |
| `target` | `&nbsp;` |  |
| `up` | `&nbsp;` |  |

**解説**

視線行列を生成

---

### multiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

乗算

---

### premultiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

前置乗算

---

### multiplyMatrices

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つの行列の積

---

### multiplyScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラー乗算

---

### determinant

メソッド

**解説**

行列式

---

### transpose

メソッド

**解説**

転置

---

### setPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

位置を設定

---

### invert

メソッド

**解説**

逆行列

---

### scale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

スケーリング

---

### getMaxScaleOnAxis

メソッド

**解説**

軸の最大スケール値

---

### makeTranslation

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

平行移動行列を生成

---

### makeRotationX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**解説**

X軸回転行列を生成

---

### makeRotationY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**解説**

Y軸回転行列を生成

---

### makeRotationZ

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**解説**

Z軸回転行列を生成

---

### makeRotationAxis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**解説**

任意軸回転行列を生成

---

### makeScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

スケーリング行列を生成

---

### makeShear

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `xy` | `&nbsp;` |  |
| `xz` | `&nbsp;` |  |
| `yx` | `&nbsp;` |  |
| `yz` | `&nbsp;` |  |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**解説**

せん断行列を生成

---

### compose

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**解説**

位置・回転・スケールから合成

---

### decompose

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**解説**

位置・回転・スケールに分解

---

### makePerspective

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**解説**

透視投影行列を生成

---

### makeOrthographic

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**解説**

正射影行列を生成

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

等価判定

---
