# Threepp.AnimationAction

A single playing animation (returned by ModelAnimator.clipAction/play)

Owned internally by the mixer; valid while the ModelAnimator is alive.
Chainable methods are exposed as returning nothing (void).

## Members

### Methods

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

Method

**Description**

Starts playback

---

### stop

Method

**Description**

Stops playback

---

### reset

Method

**Description**

Rewinds to the beginning

---

### isRunning

Method

**Description**

-> bool

---

### setLoop

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |
| `reps` | `&nbsp;` |  |

**Description**

mode: a Loop_* constant, reps: number of repetitions (-1 for infinite)

---

### setEffectiveWeight

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `w` | `&nbsp;` |  |

**Description**

Blend weight (0..1), used when blending multiple animations

---

### setEffectiveTimeScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Playback speed of this action

---

### fadeIn

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**Description**

Fades in over sec seconds

---

### fadeOut

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**Description**

Fades out over sec seconds

---

### crossFadeTo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `other` | `&nbsp;` |  |
| `dur` | `&nbsp;` |  |
| `warp` | `&nbsp;` |  |

**Description**

Cross-fades to another AnimationAction over dur seconds

---

### setDuration

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**Description**

Overrides the effective duration of the clip

---
