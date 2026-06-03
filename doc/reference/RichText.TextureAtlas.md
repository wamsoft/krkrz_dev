# RichText.TextureAtlas

テクスチャアトラスクラス

グリフを事前レンダリングしてレイヤー（テクスチャ）に格納し、
コピー矩形配列で表示順に転送するためのクラスです。
同一グリフは重複排除され、効率的なテクスチャ利用が可能です。

コンストラクタにレイヤーを渡すと、そのレイヤーをテクスチャとして使用します。

使用フロー:
1. レイヤーを渡してアトラスを作成
2. addLayout / addParagraphLayout / addStyledLayout でグリフを追加
3. commit() でテクスチャに書き込み
4. getCopyRects() でコピー矩形配列を取得
5. コピー矩形に基づいてアトラスレイヤーから表示先にコピー

使用例:
var atlasLayer = new Layer(window, window.primaryLayer);
atlasLayer.setImageSize(1024, 1024);
var atlas = new RichText.TextureAtlas(atlasLayer);

var sl = new RichText.StyledLayout();
sl.layout(text, 400, 300, RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);
atlas.addStyledLayout(sl);
atlas.commit();

var rects = atlas.getCopyRects(sl, 10, 10);
for (var i = 0; i < rects.count; i++) {
var r = rects[i];
// r.srcX, r.srcY, r.srcWidth, r.srcHeight: アトラスレイヤー内のソース矩形
// r.dstX, r.dstY: 表示先の座標
// r.displayIndex: 表示順序
targetLayer.copyRect(r.dstX, r.dstY, atlasLayer,
r.srcX, r.srcY, r.srcWidth, r.srcHeight);
}

## メンバー一覧

### コンストラクタ

- [TextureAtlas](#textureatlas)

### メソッド

- [clear](#clear)
- [addLayout](#addlayout)
- [addParagraphLayout](#addparagraphlayout)
- [addStyledLayout](#addstyledlayout)
- [commit](#commit)
- [getCopyRects](#getcopyrects)

---

### TextureAtlas

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | テクスチャとして使用するレイヤー |

**解説**

コンストラクタ

---

### clear

メソッド

**解説**

アトラスをクリア（全グリフを削除）

---

### addLayout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layout` | `&nbsp;` | RichText.Layout オブジェクト |
| `appearance` | `&nbsp;` | RichText.Appearance オブジェクト |

**戻り値**

成功時 true

**解説**

TextLayout のグリフをアトラスに追加

---

### addParagraphLayout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `paraLayout` | `&nbsp;` | RichText.ParagraphLayout オブジェクト |
| `style` | `&nbsp;` | RichText.Style オブジェクト |
| `appearance` | `&nbsp;` | RichText.Appearance オブジェクト |

**戻り値**

成功時 true

**解説**

ParagraphLayout のグリフをアトラスに追加

---

### addStyledLayout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `styledLayout` | `&nbsp;` | RichText.StyledLayout オブジェクト |

**戻り値**

成功時 true

**解説**

StyledLayout のグリフをアトラスに追加

---

### commit

メソッド

**解説**

アトラスをテクスチャ（レイヤー）に書き込み

addLayout / addParagraphLayout / addStyledLayout で追加した
グリフをレイヤーにレンダリングします。

---

### getCopyRects

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `/* overloaded */` | `&nbsp;` |  |

**戻り値**

コピー矩形の配列。各要素は辞書:
%[srcX, srcY, srcWidth, srcHeight, dstX, dstY, displayIndex, charIndex, delay, linkIndex]
charIndex: 元テキストでの文字位置
delay: 表示タイミング（ms、未設定時は含まれない）
linkIndex: リンク番号（未設定時は含まれない）

**解説**

表示用コピー矩形配列を取得

3つのオーバーロードがあります:

1) getCopyRects(layout, x, y, appearance, maxChars=-1)
- layout: RichText.Layout
- x, y: 描画位置
- appearance: RichText.Appearance
- maxChars: 最大文字数（-1で全て）

2) getCopyRects(paraLayout, x, y, width, height, hAlign, vAlign, style, appearance, maxChars=-1)
- paraLayout: RichText.ParagraphLayout
- x, y, width, height: 描画領域
- hAlign, vAlign: アライン
- style: RichText.Style
- appearance: RichText.Appearance
- maxChars: 最大文字数（-1で全て）

3) getCopyRects(styledLayout, x, y, maxChars=-1)
- styledLayout: RichText.StyledLayout
- x, y: 描画位置
- maxChars: 最大文字数（-1で全て）

---
