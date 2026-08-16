# Threepp.AnimationAction

再生中の1アニメーション (ModelAnimator.clipAction/play が返す)

mixer が内部所有する。ModelAnimator が生きている間有効。
チェーンメソッドは戻り値なし(void)として公開。

## メンバー一覧

### メソッド

- [play](#play)
- [stop](#stop)
- [reset](#reset)
- [isRunning](#isrunning)
- [setLoop](#setloop)
- [setEffectiveWeight](#seteffectiveweight)
- [setEffectiveTimeScale](#seteffectivetimescale)
- [fadeIn](#fadein)
- [fadeOut](#fadeout)
- [crossFadeTo](#crossfadeto)
- [setDuration](#setduration)

---

### play

メソッド

**解説**

再生開始

---

### stop

メソッド

**解説**

停止

---

### reset

メソッド

**解説**

先頭へ巻き戻し

---

### isRunning

メソッド

**解説**

-> bool

---

### setLoop

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |
| `reps` | `&nbsp;` |  |

**解説**

mode: Loop_* 定数, reps: 繰り返し回数(-1で無限)

---

### setEffectiveWeight

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |

**解説**

ブレンド重み (0..1)。複数アニメ合成時に使用

---

### setEffectiveTimeScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

このアクションの再生速度

---

### fadeIn

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**解説**

sec 秒でフェードイン

---

### fadeOut

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**解説**

sec 秒でフェードアウト

---

### crossFadeTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `other` | `&nbsp;` |  |
| `dur` | `&nbsp;` |  |
| `warp` | `&nbsp;` |  |

**解説**

別 AnimationAction へ dur 秒でクロスフェード

---

### setDuration

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**解説**

クリップの実効長を上書き

---
