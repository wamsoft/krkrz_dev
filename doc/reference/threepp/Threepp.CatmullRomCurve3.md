# Threepp.CatmullRomCurve3

CatmullRom スプライン曲線

制御点を通過する滑らかな曲線を生成します。

## メンバー一覧

### コンストラクタ

- [CatmullRomCurve3](#catmullromcurve3)

### プロパティ

- [closed](#closed)
- [tension](#tension)

### メソッド

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### CatmullRomCurve3

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 制御点の配列 (Vector3の配列または [x,y,z] の配列) |
| `closed` | `false` | 閉曲線かどうか |
| `curveType` | `0` | 曲線タイプ (centripetal, chordal, catmullrom) |
| `tension` | `0.5` | テンション値 (catmullrom タイプ用) |

**解説**

コンストラクタ

---

### closed

プロパティ \ アクセス: `r/w`

**解説**

閉曲線フラグ

---

### tension

プロパティ \ アクセス: `r/w`

**解説**

テンション

---

### getLength

メソッド

**解説**

曲線の長さを取得

---

### getPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**解説**

パラメータ t (0-1) の点を取得

---
