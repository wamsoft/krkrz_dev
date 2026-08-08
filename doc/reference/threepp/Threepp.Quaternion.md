# Threepp.Quaternion

クォータニオン（四元数）クラス

回転を表現するクォータニオンです。ジンバルロックが発生しません。

## メンバー一覧

### コンストラクタ

- [Quaternion](#quaternion)

### プロパティ

- [x](#x)
- [y](#y)
- [z](#z)
- [w](#w)

### メソッド

- [set](#set)
- [copy](#copy)
- [setFromEuler](#setfromeuler)
- [setFromAxisAngle](#setfromaxisangle)
- [setFromRotationMatrix](#setfromrotationmatrix)
- [setFromUnitVectors](#setfromunitvectors)
- [angleTo](#angleto)
- [rotateTowards](#rotatetowards)
- [identity](#identity)
- [invert](#invert)
- [conjugate](#conjugate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [normalize](#normalize)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyQuaternions](#multiplyquaternions)
- [slerp](#slerp)
- [slerpQuaternions](#slerpquaternions)
- [equals](#equals)

---

### Quaternion

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `0` | X成分 |
| `y` | `0` | Y成分 |
| `z` | `0` | Z成分 |
| `w` | `1` | W成分 |

**解説**

コンストラクタ

---

### x

プロパティ \ アクセス: `r/w`

**解説**

X成分（読み取り専用）

---

### y

プロパティ \ アクセス: `r/w`

**解説**

Y成分（読み取り専用）

---

### z

プロパティ \ アクセス: `r/w`

**解説**

Z成分（読み取り専用）

---

### w

プロパティ \ アクセス: `r/w`

**解説**

W成分（読み取り専用）

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**解説**

値を設定

---

### copy

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

コピー

---

### setFromEuler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**解説**

オイラー角から設定

---

### setFromAxisAngle

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**解説**

軸と角度から設定

---

### setFromRotationMatrix

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**解説**

回転行列から設定

---

### setFromUnitVectors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vFrom` | `&nbsp;` |  |
| `vTo` | `&nbsp;` |  |

**解説**

2つの単位ベクトルから設定

---

### angleTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

別のクォータニオンとの角度

---

### rotateTowards

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `step` | `&nbsp;` |  |

**解説**

別のクォータニオンへ回転

---

### identity

メソッド

**解説**

単位クォータニオンに設定

---

### invert

メソッド

**解説**

逆クォータニオン

---

### conjugate

メソッド

**解説**

共役

---

### dot

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

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

### normalize

メソッド

**解説**

正規化

---

### multiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

乗算

---

### premultiply

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

前置乗算

---

### multiplyQuaternions

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

2つのクォータニオンの積

---

### slerp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**解説**

球面線形補間

---

### slerpQuaternions

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `qa` | `&nbsp;` |  |
| `qb` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**解説**

2つのクォータニオン間の球面線形補間

---

### equals

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**解説**

等価判定

---
