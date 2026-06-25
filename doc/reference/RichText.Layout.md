# RichText.Layout

1行テキストレイアウトクラス

1行テキストのレイアウト計算結果を保持します。
レイアウトと描画を分離することで、計測結果の再利用や
事前レイアウト済みテキストの描画が可能です。

使用例:
var tl = new RichText.Layout();
tl.layout("Hello World", style);
Debug.message("幅: " + tl.width + ", 高さ: " + tl.height);
layer.drawTextLayout(tl, 10, 50, appearance);

## メンバー一覧

### コンストラクタ

- [Layout](#layout)

### プロパティ

- [width](#width)
- [height](#height)
- [ascent](#ascent)
- [descent](#descent)
- [charCount](#charcount)

### メソッド

- [layout](#layout)
- [clone](#clone)

---

### Layout

コンストラクタ

**解説**

コンストラクタ

---

### width

プロパティ \ アクセス: `r/w`

**解説**

テキスト幅（読み取り専用）

---

### height

プロパティ \ アクセス: `r/w`

**解説**

テキスト高さ（ascent + descent）（読み取り専用）

---

### ascent

プロパティ \ アクセス: `r/w`

**解説**

アセント（ベースラインから上端まで、負の値）（読み取り専用）

---

### descent

プロパティ \ アクセス: `r/w`

**解説**

ディセント（ベースラインから下端まで、正の値）（読み取り専用）

---

### charCount

プロパティ \ アクセス: `r/w`

**解説**

文字数（読み取り専用）

---

### layout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト |
| `style` | `&nbsp;` | RichText.Style オブジェクト |

**解説**

テキストのレイアウト（計測）を実行

---

### clone

メソッド

**戻り値**

複製された Layout オブジェクト

**解説**

複製

---
