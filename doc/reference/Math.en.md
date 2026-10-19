# Math

Special arithmetic

## Members

### Methods

- [octetVectorSum](#octetvectorsum)

---

### octetVectorSum

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `a` | `&nbsp;` | octet |
| `b` | `void` | octet (optional) |

**Return value**

[ Σ(ai*bi), Σ(ai-bi)^2, Σai^2, Σbi^2, Σai, Σbi, Σ(ai!=bi) ], or when bi===void, [ 0, Σai^2, Σai^2, 0, Σai, 0, Σ(ai!=0) ]

**Description**

Treats octets as vectors and computes sums

The dot product is r[0], the Euclidean distance is Math.sqrt(r[1]), and the cosine similarity is r[0]/(sqrt(r[2])*sqrt(r[3])).

---
