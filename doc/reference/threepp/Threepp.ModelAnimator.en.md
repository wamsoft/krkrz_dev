# Threepp.ModelAnimator

Model animation player (equivalent to three.js's AnimationMixer)

It keeps the target root (usually model.getScene()) alive internally, so the model is not released while you hold the ModelAnimator.

## Members

### Constructors

- [ModelAnimator](#modelanimator)

### Methods

- [clipAction](#clipaction)
- [play](#play)
- [update](#update)
- [stopAll](#stopall)
- [setTimeScale](#settimescale)
- [getTimeScale](#gettimescale)

---

### ModelAnimator

Constructor

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `root` | `&nbsp;` | Object3D to animate (usually model.getScene()). |

---

### clipAction

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**Description**

(GLTFModel, clip index) -> AnimationAction (not yet playing)

---

### play

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**Description**

(GLTFModel, index) -> AnimationAction (sets looping, resets and plays in one call; the usual way)

---

### update

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dt` | `&nbsp;` |  |

**Description**

(elapsed seconds) Call every frame to advance the animation

---

### stopAll

Method

**Description**

Stops all actions

---

### setTimeScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**Description**

Overall playback speed (1.0 = normal speed)

---

### getTimeScale

Method

**Description**

-> float

---
