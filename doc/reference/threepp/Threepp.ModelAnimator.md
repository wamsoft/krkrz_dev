# Threepp.ModelAnimator

モデルアニメーション再生機 (three.js の AnimationMixer 相当)

対象 root (通常 model.getScene()) を内部で生かし続けるので、
ModelAnimator を保持している間はモデルも解放されない。
============================================================ アニメーション再生 (glTF/GLB 内蔵アニメ) three.js の AnimationMixer 相当。GLTFModel が保持するアニメクリップを ModelAnimator で再生する。root には通常 model.getScene() を渡す。 毎フレーム update(dt秒) を呼ぶこと。 ※ VRM のアニメ(.vrma)は別系統。VRM は VRMLoader/VRMAnimation を使う。 ModelAnimator は「VRM 以外の glTF/GLB モデル自身のアニメ」用。 ============================================================

## メンバー一覧

### コンストラクタ

- [ModelAnimator](#modelanimator)

### メソッド

- [clipAction](#clipaction)
- [play](#play)
- [update](#update)
- [stopAll](#stopall)
- [setTimeScale](#settimescale)
- [getTimeScale](#gettimescale)

---

### ModelAnimator

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `root` | `&nbsp;` | アニメ対象の Object3D (通常 model.getScene()) |

---

### clipAction

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**解説**

(GLTFModel, クリップindex) -> AnimationAction (未再生)

---

### play

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**解説**

(GLTFModel, index) -> AnimationAction (ループ設定+reset+play 一括。定番)

---

### update

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dt` | `&nbsp;` |  |

**解説**

(経過秒) 毎フレーム呼んでアニメを進める

---

### stopAll

メソッド

**解説**

全アクション停止

---

### setTimeScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**解説**

全体の再生速度 (1.0=等速)

---

### getTimeScale

メソッド

**解説**

-> float

---
