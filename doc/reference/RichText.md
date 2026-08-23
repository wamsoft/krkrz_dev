# RichText

擬似コードによるマニュアル

richtext - 吉里吉里用リッチテキストレンダリングプラグイン

minikin (Android テキストレイアウトエンジン) による組版と、吉里吉里Z 本体の
統一フォントエンジン (glyphware) によるグリフ描画で、高品質なテキスト
レンダリングを提供します。フォントの実体・グリフのラスタライズを本体と共有
するため、Layer.drawText や Elements ダイアログと見た目が揃います。

特徴:
- 複数フォントのフォールバック対応
- 多言語対応（RTL含む）
- 絵文字対応
- HTMLライクなタグによるスタイル指定
- 縁取り・影などの装飾効果
- パラグラフレイアウト（自動改行）
- 逐次表示対応（ParagraphLayout / StyledLayout 使用）

## メンバー一覧

### メソッド

- [registerFont](#registerfont)
- [registerVariableFont](#registervariablefont)
- [unregisterFont](#unregisterfont)
- [registerCollection](#registercollection)
- [unregisterCollection](#unregistercollection)
- [registerLocale](#registerlocale)

### 定数

- [HALIGN_LEFT](#halign_left)
- [HALIGN_CENTER](#halign_center)
- [HALIGN_RIGHT](#halign_right)
- [HALIGN_JUSTIFY](#halign_justify)
- [VALIGN_TOP](#valign_top)
- [VALIGN_MIDDLE](#valign_middle)
- [VALIGN_BOTTOM](#valign_bottom)
- [BREAK_GREEDY](#break_greedy)
- [BREAK_HIGH_QUALITY](#break_high_quality)
- [BREAK_BALANCED](#break_balanced)
- [BIDI_LTR](#bidi_ltr)
- [BIDI_RTL](#bidi_rtl)
- [BIDI_DEFAULT_LTR](#bidi_default_ltr)
- [BIDI_DEFAULT_RTL](#bidi_default_rtl)

---

### registerFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `index` | `0` |  |

---

### registerVariableFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |
| `italic` | `false` |  |
| `index` | `0` |  |

---

### unregisterFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### registerCollection

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |
| `fontNames` | `&nbsp;` |  |

---

### unregisterCollection

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |

---

### registerLocale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `locale` | `&nbsp;` |  |

---

### HALIGN_LEFT

定数

値: `0`

---

### HALIGN_CENTER

定数

値: `1`

**解説**

左揃え

---

### HALIGN_RIGHT

定数

値: `2`

**解説**

中央揃え

---

### HALIGN_JUSTIFY

定数

値: `3`

**解説**

右揃え

---

### VALIGN_TOP

定数

値: `0`

---

### VALIGN_MIDDLE

定数

値: `1`

**解説**

上揃え

---

### VALIGN_BOTTOM

定数

値: `2`

**解説**

中央揃え

---

### BREAK_GREEDY

定数

値: `0`

---

### BREAK_HIGH_QUALITY

定数

値: `1`

**解説**

高速（各改行候補で即座に判断）

---

### BREAK_BALANCED

定数

値: `2`

**解説**

高品質（Knuth-Plassアルゴリズム）

---

### BIDI_LTR

定数

値: `0`

---

### BIDI_RTL

定数

値: `1`

**解説**

左から右

---

### BIDI_DEFAULT_LTR

定数

値: `2`

**解説**

右から左

---

### BIDI_DEFAULT_RTL

定数

値: `3`

**解説**

デフォルト左から右

---
