# RichText.ParagraphLayout

パラグラフ（複数行）テキストレイアウトクラス

複数行テキストのレイアウト計算結果を保持します。
レイアウトと描画を分離することで、計測結果の再利用や
逐次表示（maxChars 指定）に利用できます。

使用例:
var pl = new RichText.ParagraphLayout();
pl.layout("長いテキスト...", 300, style);
Debug.message("行数: " + pl.lineCount);
layer.drawParagraphLayout(pl, 10, 10, 300, 200,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);

## メンバー一覧

### コンストラクタ

- [ParagraphLayout](#paragraphlayout)

### プロパティ

- [lineCount](#linecount)
- [totalHeight](#totalheight)
- [maxWidth](#maxwidth)
- [totalCharCount](#totalcharcount)
- [lineSpacing](#linespacing)
- [breakStrategy](#breakstrategy)

### メソッド

- [layout](#layout)
- [getLineInfo](#getlineinfo)
- [clone](#clone)

---

### ParagraphLayout

コンストラクタ

**解説**

コンストラクタ

---

### lineCount

プロパティ \ アクセス: `r/w`

**解説**

行数（読み取り専用）

---

### totalHeight

プロパティ \ アクセス: `r/w`

**解説**

全行の高さ合計（読み取り専用）

---

### maxWidth

プロパティ \ アクセス: `r/w`

**解説**

最大行幅（読み取り専用）

---

### totalCharCount

プロパティ \ アクセス: `r/w`

**解説**

全行の文字数合計（読み取り専用）

---

### lineSpacing

プロパティ \ アクセス: `r/w`

**解説**

行間

デフォルト: 0

---

### breakStrategy

プロパティ \ アクセス: `r/w`

**解説**

行分割戦略

RichText.BREAK_GREEDY / BREAK_HIGH_QUALITY / BREAK_BALANCED
デフォルト: BREAK_HIGH_QUALITY

---

### layout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト |
| `maxWidth` | `&nbsp;` | 最大幅 |
| `style` | `&nbsp;` | RichText.Style オブジェクト |

**解説**

パラグラフのレイアウト（計測）を実行

---

### getLineInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 行インデックス（0〜lineCount-1） |

**戻り値**

行情報の辞書 %[startIndex, endIndex, width, height]

**解説**

行情報を取得

---

### clone

メソッド

**戻り値**

複製された ParagraphLayout オブジェクト

**解説**

複製

---
