# Math

特殊演算

## メンバー一覧

### メソッド

- [octetVectorSum](#octetvectorsum)

---

### octetVectorSum

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `void` |  |

**戻り値**

[ Σ(ai*bi), Σ(ai-bi)^2, Σai^2, Σbi^2, Σai, Σbi, Σ(ai!=bi) ] or bi===voidの場合 [ 0, Σai^2, Σai^2, 0, Σai, 0, Σ(ai!=0) ]

**解説**

octetをベクトルとみなして演算

内積はr[0], ユークリッド距離は Math.sqrt(r[1])，コサイン類似度は r[0]/(sqrt(r[2])*sqrt(r[3]))

---
