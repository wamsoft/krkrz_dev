# Threepp.LatheGeometry

旋盤ジオメトリ

2D輪郭を回転軸周りに回転させて3D形状を生成します。

## メンバー一覧

### コンストラクタ

- [LatheGeometry](#lathegeometry)

### プロパティ

- [type](#type)

---

### LatheGeometry

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 輪郭点の配列 (Vector2の配列または [x,y] の配列) |
| `segments` | `12` | セグメント数 |
| `phiStart` | `0` | 開始角度 (ラジアン) |
| `phiLength` | `Math.PI*2` | 回転角度 (ラジアン) |

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

型名（読み取り専用）

---
