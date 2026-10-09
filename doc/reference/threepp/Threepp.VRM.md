# Threepp.VRM

VRM モデル 1 体

getScene() の Group を Scene に add。毎フレーム update(dt) を呼ぶ。

## メンバー一覧

### メソッド

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

メソッド

**解説**

描画用ルート -> Threepp.Group (Scene に add する)

---

### getBoneCount

メソッド

**解説**

raw ボーン数 -> int

---

### getBoneNode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

VRM human bone 名 -> Threepp.Bone (無ければ void)

---

### getNormalizedBoneNode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

正規化リグのノード -> Threepp.Object3D

---

### resetNormalizedPose

メソッド

**解説**

正規化ポーズを rest に戻す

---

### update

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dt` | `&nbsp;` | 前フレームからの経過秒 (揺れ物の物理積分に使う。0 だと揺れは止まる) |

**解説**

毎フレーム更新。humanoid リグ転写 + 制約(node_constraint) + 表情 + 視線 +

揺れ物(springBone) をまとめて反映する。

---

### setExpression

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**解説**

--- 表情 (Expression) ---

---

### getExpression

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

-> float

---

### getExpressionCount

メソッド

**解説**

-> int

---

### getExpressionName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**解説**

i 番目の表情名 -> string (範囲外は "")

---

### expressionListJson

メソッド

**解説**

全表情の一括 JSON '[{"name":…,"weight":…},…]' (Web UI 用)

---

### setMorph

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**解説**

--- 生モーフ (ブレンドシェイプ直接指定。表情の後に override 適用) ---

---

### clearMorphs

メソッド

**解説**

生モーフ全解除

---

### getMorphCount

メソッド

**解説**

-> int

---

### getMorphName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**解説**

i 番目のモーフ名 -> string

---

### morphListJson

メソッド

**解説**

全モーフ名の一括 JSON '["Fcl_ALL_Neutral",…]' (Web UI 用)

---

### setLookAtTarget

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

--- 視線 (LookAt) ---

---

### clearLookAtTarget

メソッド

**解説**

注視を解除

---

### hasLookAt

メソッド

**解説**

視線機能を持つか -> bool

---

### applyAnimation

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` | Threepp.VRMAnimation |
| `time` | `&nbsp;` | 秒 |

**解説**

VRM アニメーションを時刻 time(秒) で適用する。適用後 update(dt) で raw ボーンへ転写。

--- アニメーション ---

---

### applyAnimationBlend

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` |  |
| `time` | `&nbsp;` |  |
| `blend` | `&nbsp;` |  |

**解説**

クロスフェード用 (blend 0..1)

---

### applyPose

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `arr` | `&nbsp;` |  |
| `blend` | `&nbsp;` | 0..1 (省略時 1 = 即時) |

**解説**

ポーズを適用。arr は [ボーン名, qx, qy, qz, qw, …] の平坦配列。

--- ポーズ (正規化リグのローカル回転) ---

---

### applyHipsOffset

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `dz` | `&nbsp;` |  |

**解説**

hips を rest からのオフセットへ (ルートモーション)

---

### getHipsOffset

メソッド

**解説**

-> Vector3

---

### captureRestPose

メソッド

**解説**

rest 正規化姿勢を記録

---

### blendToRest

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

rest へ slerp (素立ち復帰)

---

### setOffset

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

キャラ全体を平行移動

---

### setColliderScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**解説**

springBone コライダー半径の一律スケール (既定 1.0=忠実)。

VRoid 系はコライダーが体にタイトで胴体側面が手薄なため、髪が服に埋まる場合は
1.2〜1.4 程度にすると改善する (opt-in・標準外)。

--- 揺れ物 (SpringBone) ---

---

### getColliderScale

メソッド

**解説**

-> float

---

### resetSpringBones

メソッド

**解説**

揺れものを現在の姿勢で静止させる (慣性を 0 にする)。

ロード直後・服装替え・大きな姿勢変更・セーブ復元の後に呼ぶと髪が暴れない。

---

### getMaterialCount

メソッド

**解説**

--- マテリアル (glTF の material 単位) --- name は完全一致を優先し、無ければ部分一致した全 material に適用する。戻り値は適用数。 VRoid の服の部品 (上着/リボン等) の出し入れや色替え、全体の暗さに使う。 実効色 = 元の色 × setMaterialColor の色 × setTint の色 (MToon の lit/shade/emissive/rim/ matcap と輪郭線の色に掛かる)。

---

### getMaterialName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**解説**

-> string (glTF material.name)

---

### materialListJson

メソッド

**解説**

-> [{name,visible,meshes},…] の JSON 文字列

---

### setMaterialVisible

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `visible` | `&nbsp;` |  |

**解説**

-> 適用数

---

### getMaterialVisible

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

-> bool

---

### setMaterialColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

乗算色 (1,1,1 = 元の色) -> 適用数

---

### setTint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**解説**

全 material への乗算色 (1,1,1 = 元の色)

---

### getMetaName

メソッド

**解説**

--- メタ情報 ---

---

### getMetaVersion

メソッド

**解説**

-> string

---

### getMetaLicenseUrl

メソッド

**解説**

-> string

---
