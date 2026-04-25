# PreRenderedFontImage

フォントイメージ（※このクラスは実際には存在しません！）

callbackで返すレイヤオブジェクトに付加する追加情報を定義します。
普通のレイヤオブジェクトに対して，値を代入して渡してください。
レイヤの画像は(0,0)-(blackbox_x-1,blackbox_y-1)の領域のα情報のみ参照され，65段階（0〜64）にリサンプルされます。

callbackの返り値として同じインスタンスを何度も使いまわしても問題ありません。

継承元: [Layer](Layer.md)

## メンバー一覧

### プロパティ

- [blackbox_x](#blackbox_x)
- [blackbox_y](#blackbox_y)
- [origin_x](#origin_x)
- [origin_y](#origin_y)
- [inc_x](#inc_x)
- [inc_y](#inc_y)
- [inc](#inc)

---

### blackbox_x

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmBlackBoxX

---

### blackbox_y

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmBlackBoxY

---

### origin_x

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmptGlyphOrigin.x

---

### origin_y

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmptGlyphOrigin.y

---

### inc_x

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmCellIncX

---

### inc_y

プロパティ \ アクセス: `r/w`

**解説**

GLYPHMETRICS.gmCellIncY

---

### inc

プロパティ \ アクセス: `r/w`

**解説**

GetTextExtentPoint32 の返すサイズの SIZE.cx

---
