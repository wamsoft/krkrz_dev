# RichText.Style

テキストスタイルクラス

テキストの論理的なスタイル（フォント、サイズ、ウェイト等）を定義します。
描画外観（色、縁取り等）は Appearance クラスで設定します。

## メンバー一覧

### コンストラクタ

- [Style](#style)

### プロパティ

- [fontSize](#fontsize)
- [fontWeight](#fontweight)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [wordSpacing](#wordspacing)
- [scaleX](#scalex)
- [skewX](#skewx)
- [fontWidth](#fontwidth)
- [bidi](#bidi)

### メソッド

- [setFonts](#setfonts)
- [setLocale](#setlocale)
- [clone](#clone)

---

### Style

コンストラクタ

**解説**

コンストラクタ

---

### fontSize

プロパティ \ アクセス: `r/w`

**解説**

フォントサイズ（ピクセル単位）

デフォルト: 16

---

### fontWeight

プロパティ \ アクセス: `r/w`

**解説**

フォントウェイト（太さ）

100〜900 の値。400 = 通常、700 = 太字
デフォルト: 400

---

### italic

プロパティ \ アクセス: `r/w`

**解説**

イタリック

デフォルト: false

---

### letterSpacing

プロパティ \ アクセス: `r/w`

**解説**

字間（em単位）

0.1 = フォントサイズの10%の追加スペース
デフォルト: 0

---

### wordSpacing

プロパティ \ アクセス: `r/w`

**解説**

語間（em単位）

デフォルト: 0

---

### scaleX

プロパティ \ アクセス: `r/w`

**解説**

水平スケール

1.0 = 通常、0.5 = 半分の幅
デフォルト: 1.0

---

### skewX

プロパティ \ アクセス: `r/w`

**解説**

斜体スキュー値

0 = 通常、負の値で右に傾斜
デフォルト: 0

---

### fontWidth

プロパティ \ アクセス: `r/w`

**解説**

フォント幅（バリアブルフォントの wdth 軸、パーセント）

100 = 通常幅。50 = 半分の幅、200 = 2倍の幅。
バリアブルフォントの wdth 軸に対応しているフォントでのみ有効。
デフォルト: 100

---

### bidi

プロパティ \ アクセス: `r/w`

**解説**

双方向テキスト制御

RichText.BIDI_LTR / BIDI_RTL / BIDI_DEFAULT_LTR / BIDI_DEFAULT_RTL
デフォルト: BIDI_DEFAULT_LTR

---

### setFonts

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `names` | `&nbsp;` | フォント名の配列（優先度順） |

**解説**

フォントコレクションの設定

配列の順序がフォールバック優先度になります。
最初のフォントで描画できない文字は次のフォントで描画されます。

配列の各要素は registerFont で指定した登録名のほか、
登録名で見つからなければフォントファイル内の family 名
（例: "Noto Sans JP"）や "family Style" 連結名
（例: "Noto Sans JP Bold"）でも参照できます。
使用例:
style.setFonts(["メインフォント", "絵文字フォント", "フォールバック"]);

---

### setLocale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `locale` | `&nbsp;` | ロケール文字列 |

**解説**

ロケールの設定

禁則処理などの行分割ルールに影響します。
使用例:
style.setLocale("ja_JP");

---

### clone

メソッド

**戻り値**

複製された Style オブジェクト

**解説**

スタイルの複製

---
