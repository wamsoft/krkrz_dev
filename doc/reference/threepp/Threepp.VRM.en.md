# Threepp.VRM

A single VRM model

Add the Group from getScene() to a Scene, and call update(dt) every frame.

## Members

### Methods

- [getScene](#getscene)
- [getBoneCount](#getbonecount)
- [getBoneNode](#getbonenode)
- [getNormalizedBoneNode](#getnormalizedbonenode)
- [resetNormalizedPose](#resetnormalizedpose)
- [update](#update)
- [setExpression](#setexpression)
- [getExpression](#getexpression)
- [getExpressionCount](#getexpressioncount)
- [getExpressionName](#getexpressionname)
- [expressionListJson](#expressionlistjson)
- [setMorph](#setmorph)
- [clearMorphs](#clearmorphs)
- [getMorphCount](#getmorphcount)
- [getMorphName](#getmorphname)
- [morphListJson](#morphlistjson)
- [setLookAtTarget](#setlookattarget)
- [clearLookAtTarget](#clearlookattarget)
- [hasLookAt](#haslookat)
- [applyAnimation](#applyanimation)
- [applyAnimationBlend](#applyanimationblend)
- [applyPose](#applypose)
- [applyHipsOffset](#applyhipsoffset)
- [getHipsOffset](#gethipsoffset)
- [captureRestPose](#capturerestpose)
- [blendToRest](#blendtorest)
- [setOffset](#setoffset)
- [setColliderScale](#setcolliderscale)
- [getColliderScale](#getcolliderscale)
- [resetSpringBones](#resetspringbones)
- [getMaterialCount](#getmaterialcount)
- [getMaterialName](#getmaterialname)
- [materialListJson](#materiallistjson)
- [setMaterialVisible](#setmaterialvisible)
- [getMaterialVisible](#getmaterialvisible)
- [setMaterialColor](#setmaterialcolor)
- [setTint](#settint)
- [getMetaName](#getmetaname)
- [getMetaVersion](#getmetaversion)
- [getMetaLicenseUrl](#getmetalicenseurl)

---

### getScene

Method

**Description**

Root for rendering -> Threepp.Group (add it to a Scene)

---

### getBoneCount

Method

**Description**

Number of raw bones -> int

---

### getBoneNode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

VRM human bone name -> Threepp.Bone (void if not found)

---

### getNormalizedBoneNode

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

Node of the normalized rig -> Threepp.Object3D

---

### resetNormalizedPose

Method

**Description**

Returns the normalized pose to rest

---

### update

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dt` | `&nbsp;` | Seconds elapsed since the previous frame (used for physics integration of spring bones; 0 stops the motion). |

**Description**

Per-frame update

Applies humanoid rig transfer + constraints (node_constraint) + expressions + look-at + spring bones (springBone) all together.

---

### setExpression

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**Description**

Sets an expression weight (name: "happy"/"blink"/"aa", etc.; weight 0..1)

---

### getExpression

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

-> float

---

### getExpressionCount

Method

**Description**

-> int

---

### getExpressionName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**Description**

Name of the i-th expression -> string ("" if out of range)

---

### expressionListJson

Method

**Description**

JSON of all expressions at once '[{"name":…,"weight":…},…]' (for web UIs)

---

### setMorph

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**Description**

Sets an individual morph by name (VRoid: "Fcl_*", etc.)

Specifies a blend shape directly. Applied as an override after expressions.

---

### clearMorphs

Method

**Description**

Clears all raw morphs

---

### getMorphCount

Method

**Description**

-> int

---

### getMorphName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**Description**

Name of the i-th morph -> string

---

### morphListJson

Method

**Description**

JSON of all morph names at once '["Fcl_ALL_Neutral",…]' (for web UIs)

---

### setLookAtTarget

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Sets the look-at target (world coordinates)

---

### clearLookAtTarget

Method

**Description**

Clears the look-at target

---

### hasLookAt

Method

**Description**

Whether the model has look-at support -> bool

---

### applyAnimation

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` | Threepp.VRMAnimation |
| `time` | `&nbsp;` | Seconds. |

**Description**

Applies a VRM animation at time (seconds). After applying, update(dt) transfers it to the raw bones.

---

### applyAnimationBlend

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` |  |
| `time` | `&nbsp;` |  |
| `blend` | `&nbsp;` |  |

**Description**

For cross-fading (blend 0..1)

---

### applyPose

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `arr` | `&nbsp;` |  |
| `blend` | `&nbsp;` | 0..1 (default 1 = immediate). |

**Description**

Applies a pose. arr is a flat array of [bone name, qx, qy, qz, qw, …].

The rotations are local rotations of the normalized rig.

---

### applyHipsOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `dz` | `&nbsp;` |  |

**Description**

Moves the hips to an offset from rest (root motion)

---

### getHipsOffset

Method

**Description**

-> Vector3

---

### captureRestPose

Method

**Description**

Records the rest normalized pose

---

### blendToRest

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**Description**

Slerps toward rest (back to a neutral standing pose)

---

### setOffset

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**Description**

Translates the whole character

---

### setColliderScale

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**Description**

Uniform scale for springBone collider radii (default 1.0 = faithful).

VRoid models have colliders that fit the body tightly and cover the sides of the torso poorly, so if hair sinks into clothing,
a value around 1.2 to 1.4 helps (opt-in; non-standard).

---

### getColliderScale

Method

**Description**

-> float

---

### resetSpringBones

Method

**Description**

Settles the spring bones at the current pose (zeroes their inertia).

Call it right after loading, after changing outfits, after a large pose change, or after restoring a save, to keep the hair from flailing.

---

### getMaterialCount

Method

**Description**

-> int

---

### getMaterialName

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**Description**

-> string (glTF material.name)

---

### materialListJson

Method

**Description**

-> JSON string of [{name,visible,meshes},…]

---

### setMaterialVisible

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `visible` | `&nbsp;` |  |

**Description**

Shows or hides materials -> number of materials affected

name prefers an exact match; if there is none, the operation applies to every material that partially matches. The return value is the number of materials affected.
Use it to show or hide VRoid clothing parts (jackets, ribbons, etc.).

---

### getMaterialVisible

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Description**

-> bool

---

### setMaterialColor

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Multiply color (1,1,1 = original color) -> number of materials affected

name prefers an exact match; if there is none, the operation applies to every material that partially matches. The return value is the number of materials affected.
Effective color = original color × setMaterialColor color × setTint color (applied to MToon's lit/shade/emissive/rim/
matcap and outline colors). Use it to recolor VRoid clothing parts.

---

### setTint

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**Description**

Multiply color for all materials (1,1,1 = original color)

Multiplied on top of the setMaterialColor color. Use it to adjust the overall darkness.

---

### getMetaName

Method

**Description**

-> string

---

### getMetaVersion

Method

**Description**

-> string

---

### getMetaLicenseUrl

Method

**Description**

-> string

---
