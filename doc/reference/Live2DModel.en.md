# Live2DModel

Model for inspecting and manipulating

Can be created without a device (OpenGL context).
Supports inspecting model information, manipulating parameters, and controlling motions.
Use Live2DPlayer to draw it.

## Members

### Constructors

- [Live2DModel](#live2dmodel)

### Methods

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

Constructor

**Description**

Constructor

No device needs to be specified.

---

### clear

Method

**Description**

Clears the contents

---

### load

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### clone

Method

**Description**

Duplicates the model

---

### getExpressionCount

Method

---

### getExpressionName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### setExpression

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getExpression

Method

---

### fixExpression

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getMotionGroupCount

Method

---

### getMotionGroupName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getMotionCount

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getMotionName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no` | `&nbsp;` |  |

---

### getMotionType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### setMotionType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### startMotion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `loop` | `&nbsp;` |  |
| `fadeIn` | `&nbsp;` |  |
| `fadeOut` | `&nbsp;` |  |

---

### stopMotion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getCurrentMotions

Method

---

### getParameterCount

Method

---

### getParameterInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getParameterValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setParameterValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setParameterType

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### setDiffParameterValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### progress

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `tick` | `&nbsp;` |  |

---

### canSync

Method

---

### sync

Method

---

### addLipSyncId

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### addEyeBlinkId

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### isPlaying

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getPartCount

Method

---

### getPartInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getPartValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setPartValue

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setPartFadeTime

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `fadeTime` | `&nbsp;` |  |

---

### getEventCount

Method

---

### getEventName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### addVriableMotion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |
| `descrete` | `&nbsp;` |  |

---

### delVariableMotion

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### getVariableMotionCount

Method

---

### getVariableMotionName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### getVariableMotionInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### setVariable

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getVariable

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### isMosaicModel

Method

---
