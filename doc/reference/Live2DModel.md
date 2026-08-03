# Live2DModel

情報参照・操作用モデル

デバイス(OpenGLコンテキスト)なしで生成できる
モデルの情報参照・パラメータ操作・モーション制御が可能
描画するには Live2DPlayer を使用する

## メンバー一覧

### コンストラクタ

- [Live2DModel](#live2dmodel)

### メソッド

- [clear](#clear)
- [load](#load)
- [clone](#clone)
- [getExpressionCount](#getexpressioncount)
- [getExpressionName](#getexpressionname)
- [setExpression](#setexpression)
- [getExpression](#getexpression)
- [fixExpression](#fixexpression)
- [getMotionGroupCount](#getmotiongroupcount)
- [getMotionGroupName](#getmotiongroupname)
- [getMotionCount](#getmotioncount)
- [getMotionName](#getmotionname)
- [getMotionType](#getmotiontype)
- [setMotionType](#setmotiontype)
- [startMotion](#startmotion)
- [stopMotion](#stopmotion)
- [getCurrentMotions](#getcurrentmotions)
- [getParameterCount](#getparametercount)
- [getParameterInfo](#getparameterinfo)
- [getParameterValue](#getparametervalue)
- [setParameterValue](#setparametervalue)
- [setParameterType](#setparametertype)
- [setDiffParameterValue](#setdiffparametervalue)
- [progress](#progress)
- [canSync](#cansync)
- [sync](#sync)
- [addLipSyncId](#addlipsyncid)
- [addEyeBlinkId](#addeyeblinkid)
- [isPlaying](#isplaying)
- [getPartCount](#getpartcount)
- [getPartInfo](#getpartinfo)
- [getPartValue](#getpartvalue)
- [setPartValue](#setpartvalue)
- [setPartFadeTime](#setpartfadetime)
- [getEventCount](#geteventcount)
- [getEventName](#geteventname)
- [addVriableMotion](#addvriablemotion)
- [delVariableMotion](#delvariablemotion)
- [getVariableMotionCount](#getvariablemotioncount)
- [getVariableMotionName](#getvariablemotionname)
- [getVariableMotionInfo](#getvariablemotioninfo)
- [setVariable](#setvariable)
- [getVariable](#getvariable)
- [isMosaicModel](#ismosaicmodel)

---

### Live2DModel

コンストラクタ

**解説**

コンストラクタ

デバイス指定は不要

---

### clear

メソッド

**解説**

内容消去

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### clone

メソッド

**解説**

複製

---

### getExpressionCount

メソッド

---

### getExpressionName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### setExpression

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getExpression

メソッド

---

### fixExpression

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getMotionGroupCount

メソッド

---

### getMotionGroupName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getMotionCount

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getMotionName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no` | `&nbsp;` |  |

---

### getMotionType

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### setMotionType

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### startMotion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `loop` | `&nbsp;` |  |
| `fadeIn` | `&nbsp;` |  |
| `fadeOut` | `&nbsp;` |  |

---

### stopMotion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getCurrentMotions

メソッド

---

### getParameterCount

メソッド

---

### getParameterInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getParameterValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setParameterValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setParameterType

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### setDiffParameterValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### progress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tick` | `&nbsp;` |  |

---

### canSync

メソッド

---

### sync

メソッド

---

### addLipSyncId

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### addEyeBlinkId

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### isPlaying

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getPartCount

メソッド

---

### getPartInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getPartValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setPartValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setPartFadeTime

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fadeTime` | `&nbsp;` |  |

---

### getEventCount

メソッド

---

### getEventName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### addVriableMotion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |
| `descrete` | `&nbsp;` |  |

---

### delVariableMotion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### getVariableMotionCount

メソッド

---

### getVariableMotionName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### getVariableMotionInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### setVariable

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getVariable

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### isMosaicModel

メソッド

---
