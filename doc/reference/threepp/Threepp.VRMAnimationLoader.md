# Threepp.VRMAnimationLoader

VRM アニメーションローダ

## メンバー一覧

### コンストラクタ

- [VRMAnimationLoader](#vrmanimationloader)

### メソッド

- [load](#load)
- [loadStorage](#loadstorage)
- [exportPoseSeq](#exportposeseq)

---

### VRMAnimationLoader

コンストラクタ

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**解説**

OS パスから (デバッグ用) -> VRMAnimation

---

### loadStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**解説**

吉里吉里ストレージ名から (本番用) -> VRMAnimation

---

### exportPoseSeq

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `boneNames` | `&nbsp;` | [ボーン名,…] (nBones) |
| `times` | `&nbsp;` | [秒,…] (nKeys) |
| `quatsFlat` | `&nbsp;` | [(key,bone) 行優先の qx,qy,qz,qw,…] (nKeys*nBones*4) |
| `hipsFlat` | `&nbsp;` | hips オフセット [dx,dy,dz,…] (nKeys*3。空配列 = トラック無し) |
| `exprNames` | `&nbsp;` | 表情名 [] (省略/空 = 表情トラック無し) |
| `exprWeightsFlat` | `&nbsp;` | 表情 weight (expr-major 平坦, nExpr*nKeys) |
| `path` | `&nbsp;` | 出力ストレージ名 (bare 名で data/ 直下) |

**解説**

ポーズ列を 1 本の VRMA (.vrma = glTF-JSON + base64) へ書き出す。

入力は平坦な並列配列。書き出したファイルは loadStorage で読み戻せる。

---
