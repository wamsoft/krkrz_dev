# Threepp.VRMLoader

VRM ローダ

.vrm を読み込み VRM を返す。VRM 0.x / 1.0 両対応。
============================================================ VRM (VRoid/VRM 0.x・1.0 アバター) ------------------------------------------------------------ VRMLoader で .vrm を読み、getScene() の Group を Scene に add して描画する。 毎フレーム update(dt) で humanoid リグ/表情/視線/揺れ物(springBone)を反映する。 アニメ(.vrma)は VRMAnimationLoader で読み、applyAnimation(anim, time) → update(dt)。 MToon(トゥーン)/輪郭線/matcap/normalMap/揺れ物/制約は内部で自動処理される。 ============================================================

## メンバー一覧

### コンストラクタ

- [VRMLoader](#vrmloader)

### メソッド

- [load](#load)
- [loadStorage](#loadstorage)

---

### VRMLoader

コンストラクタ

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` | ファイルシステム上の絶対/相対パス |

**戻り値**

VRM  (失敗時 void)

**解説**

OS パスから読み込む (デバッグ/スタンドアロン用)。

---

### loadStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` | ストレージ名 (例 Storages.getPlacedPath("model.vrm")) |

**戻り値**

VRM  (失敗時 void)

**解説**

吉里吉里ストレージ名から読み込む (本番用。アーカイブ対応)。

---
