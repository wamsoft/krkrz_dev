# GdiPlus.Font

このクラスは複数のプラグインから拡張されています。

## プラグイン拡張: layerExDraw

フォント情報

### メンバー一覧

#### コンストラクタ

- [Font](#font)

#### プロパティ

- [familyName](#familyname)
- [emSize](#emsize)
- [style](#style)
- [forceSelfPathDraw](#forceselfpathdraw)
- [ascent](#ascent)
- [descent](#descent)
- [lineSpacing](#linespacing)
- [ascentLeading](#ascentleading)
- [descentLeading](#descentleading)

---

### Font

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `familyName` | `&nbsp;` | フォントファミリー |
| `emSize` | `&nbsp;` | フォントのサイズ |
| `style` | `&nbsp;` | フォントスタイル |

**解説**

コンストラクタ

---

### familyName

プロパティ \ アクセス: `r/w`

**解説**

フォントファミリー

---

### emSize

プロパティ \ アクセス: `r/w`

**解説**

フォントのサイズ

---

### style

プロパティ \ アクセス: `r/w`

**解説**

フォントのスタイル

---

### forceSelfPathDraw

プロパティ \ アクセス: `r/w`

**解説**

GDI+ のフォント描画機構を使わずに、自前でパスを取得してのフォント描画を行うかどうかを設定する。

---

### ascent

プロパティ \ アクセス: `r`

**解説**

ascent (読み出し専用)

---

### descent

プロパティ \ アクセス: `r`

**解説**

descent (読み出し専用)

---

### lineSpacing

プロパティ \ アクセス: `r`

**解説**

行間の長さ (読み出し専用)。

---

### ascentLeading

プロパティ \ アクセス: `r`

**解説**

ascent側のinternalLeading(読み出し専用)

---

### descentLeading

プロパティ \ アクセス: `r`

**解説**

descent側のinternalLeading(読み出し専用)

---

## プラグイン拡張: layerExVector

フォント情報

loadFont() で登録したフォントを使用してテキストを描画するための設定を保持します

### メンバー一覧

#### コンストラクタ

- [Font](#font)

#### プロパティ

- [fontFamily](#fontfamily)
- [fontSize](#fontsize)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [lineSpacing](#linespacing)

---

### Font

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fontFamily` | `&nbsp;` | フォントファミリー名（loadFont()で登録した名前） |
| `fontSize` | `&nbsp;` | フォントのサイズ |

**解説**

コンストラクタ

---

### fontFamily

プロパティ \ アクセス: `r/w`

**解説**

フォントファミリー名（loadFont()で登録した名前）

---

### fontSize

プロパティ \ アクセス: `r/w`

**解説**

フォントのサイズ

---

### italic

プロパティ \ アクセス: `r/w`

**解説**

イタリック傾斜 (0=なし, 0.18=標準)

---

### letterSpacing

プロパティ \ アクセス: `r/w`

**解説**

文字間隔スケール (1.0=標準, 値が大きいほど広い)

---

### lineSpacing

プロパティ \ アクセス: `r/w`

**解説**

行間隔スケール (1.0=標準, 値が大きいほど広い)

---
