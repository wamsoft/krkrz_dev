# Threepp

threepp プラグイン 擬似コードによるマニュアル

threepp は three.js の C++ ポートです。
3D グラフィックスのレンダリング機能を提供します。

## メンバー一覧

### 定数

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
- [Loop_Once](#loop_once)
- [Loop_Repeat](#loop_repeat)
- [Loop_PingPong](#loop_pingpong)
- [CatmullRomCurve3_CurveType_centripetal](#catmullromcurve3_curvetype_centripetal)
- [CatmullRomCurve3_CurveType_chordal](#catmullromcurve3_curvetype_chordal)
- [CatmullRomCurve3_CurveType_catmullrom](#catmullromcurve3_curvetype_catmullrom)

---

### Side_Front

定数

値: `0`

**解説**

============================================================ Side 定義 (マテリアルの描画面) ============================================================

---

### Side_Back

定数

値: `1`

**解説**

表面のみ描画

---

### Side_Double

定数

値: `2`

**解説**

裏面のみ描画

---

### Blending_None

定数

値: `0`

**解説**

両面描画 ============================================================ Blending 定義 (ブレンドモード) ============================================================

---

### Blending_Normal

定数

値: `1`

---

### Blending_Additive

定数

値: `2`

---

### Blending_Subtractive

定数

値: `3`

---

### Blending_Multiply

定数

値: `4`

---

### Blending_Custom

定数

値: `5`

---

### CullFace_None

定数

値: `0`

**解説**

============================================================ CullFace 定義 (カリング) ============================================================

---

### CullFace_Back

定数

値: `1`

---

### CullFace_Front

定数

値: `2`

---

### CullFace_FrontBack

定数

値: `3`

---

### ShadowMap_Basic

定数

値: `0`

**解説**

============================================================ ShadowMap 定義 (シャドウマップ種別) ============================================================

---

### ShadowMap_PFC

定数

値: `1`

---

### ShadowMap_PFCSoft

定数

値: `2`

---

### ShadowMap_VSM

定数

値: `3`

---

### ToneMapping_None

定数

値: `0`

**解説**

============================================================ ToneMapping 定義 (トーンマッピング) ============================================================

---

### ToneMapping_Linear

定数

値: `1`

---

### ToneMapping_Reinhard

定数

値: `2`

---

### ToneMapping_Cineon

定数

値: `3`

---

### ToneMapping_ACESFilmic

定数

値: `4`

---

### ToneMapping_Custom

定数

値: `5`

---

### Encoding_Linear

定数

値: `3000`

**解説**

============================================================ Encoding 定義 (出力エンコーディング) ============================================================

---

### Encoding_sRGB

定数

値: `3001`

---

### Encoding_Gamma

定数

値: `3007`

---

### TextureWrapping_Repeat

定数

値: `1000`

**解説**

============================================================ TextureWrapping 定義 (テクスチャラッピング) ============================================================

---

### TextureWrapping_ClampToEdge

定数

値: `1001`

---

### TextureWrapping_MirroredRepeat

定数

値: `1002`

---

### Filter_Nearest

定数

値: `1003`

**解説**

============================================================ Filter 定義 (テクスチャフィルタ) ============================================================

---

### Filter_Linear

定数

値: `1006`

---

### Filter_NearestMipmapNearest

定数

値: `1004`

---

### Filter_NearestMipmapLinear

定数

値: `1005`

---

### Filter_LinearMipmapNearest

定数

値: `1007`

---

### Filter_LinearMipmapLinear

定数

値: `1008`

---

### Loop_Once

定数

値: `2200`

**解説**

============================================================ Loop 定義 (アニメーションループ) ============================================================

---

### Loop_Repeat

定数

値: `2201`

---

### Loop_PingPong

定数

値: `2202`

---

### Loop_Once

定数

値: `2200`

**解説**

Loop モード定数 (AnimationAction.setLoop に渡す)

---

### Loop_Repeat

定数

値: `2201`

**解説**

1回で停止

---

### Loop_PingPong

定数

値: `2202`

**解説**

ループ (ModelAnimator.play の既定)

---

### CatmullRomCurve3_CurveType_centripetal

定数

値: `0`

**解説**

往復

---

### CatmullRomCurve3_CurveType_chordal

定数

値: `1`

---

### CatmullRomCurve3_CurveType_catmullrom

定数

値: `2`

---
