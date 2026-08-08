# Threepp.GLTFLoader

汎用 glTF/GLB ローダ

VRM 拡張は解釈しない素の glTF として読む。GLB(自己完結) が確実。
スキンメッシュはバインドポーズ(T ポーズ)で読まれる。ボーンアニメの再生には
別途アニメ機構が要る(現状はモデル自身のアニメ再生は未対応。姿勢固定の小物/
地形/建物や、TJS 側でトランスフォームを動かす用途向け)。

## メンバー一覧

### コンストラクタ

- [GLTFLoader](#gltfloader)

### メソッド

- [load](#load)
- [loadStorage](#loadstorage)

---

### GLTFLoader

コンストラクタ

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**解説**

OS パスから (.gltf+外部リソースも解決可) -> GLTFModel

---

### loadStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**解説**

吉里吉里ストレージ名から (GLB 推奨) -> GLTFModel

---
