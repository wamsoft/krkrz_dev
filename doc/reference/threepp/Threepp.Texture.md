# Threepp.Texture

テクスチャ基底クラス

画像テクスチャを表現します。
============================================================ Texture クラス ============================================================

## メンバー一覧

### コンストラクタ

- [Texture](#texture)

### プロパティ

- [id](#id)
- [name](#name)
- [mapping](#mapping)
- [wrapS](#wraps)
- [wrapT](#wrapt)
- [magFilter](#magfilter)
- [minFilter](#minfilter)
- [anisotropy](#anisotropy)
- [format](#format)
- [offset](#offset)
- [repeat](#repeat)
- [center](#center)
- [rotation](#rotation)
- [matrixAutoUpdate](#matrixautoupdate)
- [generateMipmaps](#generatemipmaps)
- [premultiplyAlpha](#premultiplyalpha)
- [unpackAlignment](#unpackalignment)
- [encoding](#encoding)

### メソッド

- [updateMatrix](#updatematrix)
- [dispose](#dispose)
- [needsUpdate](#needsupdate)
- [version](#version)

---

### Texture

コンストラクタ

**解説**

コンストラクタ

---

### id

プロパティ \ アクセス: `r/w`

**解説**

ID（読み取り専用）

---

### name

プロパティ \ アクセス: `r/w`

**解説**

名前

---

### mapping

プロパティ \ アクセス: `r/w`

**解説**

マッピング種別

---

### wrapS

プロパティ \ アクセス: `r/w`

**解説**

S方向のラッピング

---

### wrapT

プロパティ \ アクセス: `r/w`

**解説**

T方向のラッピング

---

### magFilter

プロパティ \ アクセス: `r/w`

**解説**

拡大フィルタ

---

### minFilter

プロパティ \ アクセス: `r/w`

**解説**

縮小フィルタ

---

### anisotropy

プロパティ \ アクセス: `r/w`

**解説**

異方性フィルタリング

---

### format

プロパティ \ アクセス: `r/w`

**解説**

フォーマット

---

### offset

プロパティ \ アクセス: `r/w`

**解説**

オフセット (Vector2、読み取り専用)

---

### repeat

プロパティ \ アクセス: `r/w`

**解説**

繰り返し (Vector2、読み取り専用)

---

### center

プロパティ \ アクセス: `r/w`

**解説**

中心 (Vector2、読み取り専用)

---

### rotation

プロパティ \ アクセス: `r/w`

**解説**

回転

---

### matrixAutoUpdate

プロパティ \ アクセス: `r/w`

**解説**

行列の自動更新

---

### generateMipmaps

プロパティ \ アクセス: `r/w`

**解説**

ミップマップを生成するか

---

### premultiplyAlpha

プロパティ \ アクセス: `r/w`

**解説**

事前アルファ乗算

---

### unpackAlignment

プロパティ \ アクセス: `r/w`

**解説**

アンパックアラインメント

---

### encoding

プロパティ \ アクセス: `r/w`

**解説**

エンコーディング

---

### updateMatrix

メソッド

**解説**

行列を更新

---

### dispose

メソッド

**解説**

リソースを解放

---

### needsUpdate

メソッド

**解説**

更新フラグを立てる

---

### version

メソッド

**解説**

バージョンを取得

---
