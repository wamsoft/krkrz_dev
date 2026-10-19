# Threepp

Pseudo-code manual for the threepp plugin

threepp is a C++ port of three.js.
It provides 3D graphics rendering.

## Members

### Constants

- [Side_Front](#side_front)
- [Side_Back](#side_back)
- [Side_Double](#side_double)
- [Blending_None](#blending_none)
- [Blending_Normal](#blending_normal)
- [Blending_Additive](#blending_additive)
- [Blending_Subtractive](#blending_subtractive)
- [Blending_Multiply](#blending_multiply)
- [Blending_Custom](#blending_custom)
- [CullFace_None](#cullface_none)
- [CullFace_Back](#cullface_back)
- [CullFace_Front](#cullface_front)
- [CullFace_FrontBack](#cullface_frontback)
- [ShadowMap_Basic](#shadowmap_basic)
- [ShadowMap_PFC](#shadowmap_pfc)
- [ShadowMap_PFCSoft](#shadowmap_pfcsoft)
- [ShadowMap_VSM](#shadowmap_vsm)
- [ToneMapping_None](#tonemapping_none)
- [ToneMapping_Linear](#tonemapping_linear)
- [ToneMapping_Reinhard](#tonemapping_reinhard)
- [ToneMapping_Cineon](#tonemapping_cineon)
- [ToneMapping_ACESFilmic](#tonemapping_acesfilmic)
- [ToneMapping_Custom](#tonemapping_custom)
- [Encoding_Linear](#encoding_linear)
- [Encoding_sRGB](#encoding_srgb)
- [Encoding_Gamma](#encoding_gamma)
- [TextureWrapping_Repeat](#texturewrapping_repeat)
- [TextureWrapping_ClampToEdge](#texturewrapping_clamptoedge)
- [TextureWrapping_MirroredRepeat](#texturewrapping_mirroredrepeat)
- [Filter_Nearest](#filter_nearest)
- [Filter_Linear](#filter_linear)
- [Filter_NearestMipmapNearest](#filter_nearestmipmapnearest)
- [Filter_NearestMipmapLinear](#filter_nearestmipmaplinear)
- [Filter_LinearMipmapNearest](#filter_linearmipmapnearest)
- [Filter_LinearMipmapLinear](#filter_linearmipmaplinear)
- [Loop_Once](#loop_once)
- [Loop_Repeat](#loop_repeat)
- [Loop_PingPong](#loop_pingpong)
- [CatmullRomCurve3_CurveType_centripetal](#catmullromcurve3_curvetype_centripetal)
- [CatmullRomCurve3_CurveType_chordal](#catmullromcurve3_curvetype_chordal)
- [CatmullRomCurve3_CurveType_catmullrom](#catmullromcurve3_curvetype_catmullrom)

---

### Side_Front

Constant

Value: `0`

**Description**

Render front faces only

---

### Side_Back

Constant

Value: `1`

**Description**

Render back faces only

---

### Side_Double

Constant

Value: `2`

**Description**

Render both faces

---

### Blending_None

Constant

Value: `0`

---

### Blending_Normal

Constant

Value: `1`

---

### Blending_Additive

Constant

Value: `2`

---

### Blending_Subtractive

Constant

Value: `3`

---

### Blending_Multiply

Constant

Value: `4`

---

### Blending_Custom

Constant

Value: `5`

---

### CullFace_None

Constant

Value: `0`

---

### CullFace_Back

Constant

Value: `1`

---

### CullFace_Front

Constant

Value: `2`

---

### CullFace_FrontBack

Constant

Value: `3`

---

### ShadowMap_Basic

Constant

Value: `0`

---

### ShadowMap_PFC

Constant

Value: `1`

---

### ShadowMap_PFCSoft

Constant

Value: `2`

---

### ShadowMap_VSM

Constant

Value: `3`

---

### ToneMapping_None

Constant

Value: `0`

---

### ToneMapping_Linear

Constant

Value: `1`

---

### ToneMapping_Reinhard

Constant

Value: `2`

---

### ToneMapping_Cineon

Constant

Value: `3`

---

### ToneMapping_ACESFilmic

Constant

Value: `4`

---

### ToneMapping_Custom

Constant

Value: `5`

---

### Encoding_Linear

Constant

Value: `3000`

---

### Encoding_sRGB

Constant

Value: `3001`

---

### Encoding_Gamma

Constant

Value: `3007`

---

### TextureWrapping_Repeat

Constant

Value: `1000`

---

### TextureWrapping_ClampToEdge

Constant

Value: `1001`

---

### TextureWrapping_MirroredRepeat

Constant

Value: `1002`

---

### Filter_Nearest

Constant

Value: `1003`

---

### Filter_Linear

Constant

Value: `1006`

---

### Filter_NearestMipmapNearest

Constant

Value: `1004`

---

### Filter_NearestMipmapLinear

Constant

Value: `1005`

---

### Filter_LinearMipmapNearest

Constant

Value: `1007`

---

### Filter_LinearMipmapLinear

Constant

Value: `1008`

---

### Loop_Once

Constant

Value: `2200`

**Description**

Stop after one pass

---

### Loop_Repeat

Constant

Value: `2201`

**Description**

Loop (the default of ModelAnimator.play)

---

### Loop_PingPong

Constant

Value: `2202`

**Description**

Back and forth

---

### CatmullRomCurve3_CurveType_centripetal

Constant

Value: `0`

---

### CatmullRomCurve3_CurveType_chordal

Constant

Value: `1`

---

### CatmullRomCurve3_CurveType_catmullrom

Constant

Value: `2`

---
