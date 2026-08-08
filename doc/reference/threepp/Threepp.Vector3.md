# Threepp.Vector3

3D ベクトルクラス

3次元ベクトルを表現します。配列 [x, y, z] や辞書 %[x:, y:, z:] からも変換可能です。

## メンバー一覧

### コンストラクタ

- [Vector3](#vector3)

### プロパティ

- [x](#x)
- [y](#y)
- [z](#z)

### メソッド

- [set](#set)
- [setScalar](#setscalar)
- [setX](#setx)
- [setY](#sety)
- [setZ](#setz)
- [copy](#copy)
- [add](#add)
- [addScalar](#addscalar)
- [addVectors](#addvectors)
- [addScaledVector](#addscaledvector)
- [sub](#sub)
- [subScalar](#subscalar)
- [subVectors](#subvectors)
- [multiply](#multiply)
- [multiplyScalar](#multiplyscalar)
- [multiplyVectors](#multiplyvectors)
- [applyAxisAngle](#applyaxisangle)
- [applyEuler](#applyeuler)
- [applyMatrix3](#applymatrix3)
- [applyMatrix4](#applymatrix4)
- [applyQuaternion](#applyquaternion)
- [project](#project)
- [unproject](#unproject)
- [transformDirection](#transformdirection)
- [divide](#divide)
- [divideScalar](#dividescalar)
- [min](#min)
- [max](#max)
- [clamp](#clamp)
- [clampScalar](#clampscalar)
- [clampLength](#clamplength)
- [floor](#floor)
- [ceil](#ceil)
- [round](#round)
- [negate](#negate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [manhattanLength](#manhattanlength)
- [normalize](#normalize)
- [setLength](#setlength)
- [lerp](#lerp)
- [lerpVectors](#lerpvectors)
- [cross](#cross)
- [crossVectors](#crossvectors)
- [reflect](#reflect)
- [angleTo](#angleto)
- [distanceTo](#distanceto)
- [distanceToSquared](#distancetosquared)
- [manhattanDistanceTo](#manhattandistanceto)
- [setFromMatrixPosition](#setfrommatrixposition)
- [setFromMatrixScale](#setfrommatrixscale)
- [equals](#equals)

---

### Vector3

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `0` | X成分 |
| `y` | `0` | Y成分 |
| `z` | `0` | Z成分 |

**解説**

コンストラクタ

---

### x

プロパティ \ アクセス: `r/w`

**解説**

X成分

---

### y

プロパティ \ アクセス: `r/w`

**解説**

Y成分

---

### z

プロパティ \ アクセス: `r/w`

**解説**

Z成分

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

値を設定

---

### setScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**解説**

すべての成分を同じ値に設定

---

### setX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**解説**

X成分を設定

---

### setY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**解説**

Y成分を設定

---

### setZ

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**解説**

Z成分を設定

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

別のベクトルからコピー

---

### add

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

ベクトルを加算

---

### addScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラーを加算

---

### addVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つのベクトルの和を設定

---

### addScaledVector

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `s` | `&nbsp;` |  |

**解説**

スケーリングして加算

---

### sub

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

ベクトルを減算

---

### subScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラーを減算

---

### subVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つのベクトルの差を設定

---

### multiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

ベクトル同士の成分ごとの乗算

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

### multiplyVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つのベクトルの成分ごとの積を設定

---

### applyAxisAngle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**解説**

軸と角度で回転

---

### applyEuler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**解説**

オイラー角で回転

---

### applyMatrix3

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

3x3行列を適用

---

### applyMatrix4

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

4x4行列を適用

---

### applyQuaternion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

クォータニオンで回転

---

### project

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**解説**

カメラに投影

---

### unproject

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**解説**

投影を解除

---

### transformDirection

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

方向ベクトルを変換

---

### divide

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

ベクトル同士の成分ごとの除算

---

### divideScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

スカラー除算

---

### min

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

各成分の最小値

---

### max

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

各成分の最大値

---

### clamp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**解説**

各成分をクランプ

---

### clampScalar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**解説**

スカラー範囲でクランプ

---

### clampLength

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**解説**

長さをクランプ

---

### floor

メソッド

**解説**

各成分を切り捨て

---

### ceil

メソッド

**解説**

各成分を切り上げ

---

### round

メソッド

**解説**

各成分を四捨五入

---

### negate

メソッド

**解説**

符号反転

---

### dot

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

内積

---

### lengthSq

メソッド

**解説**

長さの二乗

---

### length

メソッド

**解説**

長さ

---

### manhattanLength

メソッド

**解説**

マンハッタン距離

---

### normalize

メソッド

**解説**

正規化

---

### setLength

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `length` | `&nbsp;` |  |

**解説**

長さを設定

---

### lerp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**解説**

線形補間

---

### lerpVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**解説**

2つのベクトル間の線形補間

---

### cross

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

外積

---

### crossVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つのベクトルの外積

---

### reflect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |

**解説**

反射

---

### angleTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

別のベクトルとの角度

---

### distanceTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

別のベクトルとの距離

---

### distanceToSquared

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

距離の二乗

---

### manhattanDistanceTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

マンハッタン距離

---

### setFromMatrixPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

行列の位置成分を取得

---

### setFromMatrixScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

行列のスケール成分を取得

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**解説**

等価判定

---
