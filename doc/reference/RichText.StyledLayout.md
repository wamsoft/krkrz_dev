# RichText.StyledLayout

スタイルタグ付きテキストのレイアウトクラス

スタイルタグ付きテキストのレイアウト計算結果を保持します。
レイアウトと描画を分離することで、同一テキストの再描画や
文字送りアニメーションを効率的に実現できます。

使用例:
var sl = new RichText.StyledLayout();
sl.layout(
"<style:bold>太字</style>と通常テキスト",
400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]
);
layer.drawStyledLayout(sl, 10, 10);

## メンバー一覧

### コンストラクタ

- [StyledLayout](#styledlayout)

### プロパティ

- [lineCount](#linecount)
- [totalCharCount](#totalcharcount)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [isValid](#isvalid)
- [totalRenderDelay](#totalrenderdelay)

### メソッド

- [layout](#layout)
- [resolveAllTimings](#resolvealltimings)
- [calcShowCount](#calcshowcount)
- [getKeyWaits](#getkeywaits)
- [getResolvedTimings](#getresolvedtimings)

---

### StyledLayout

コンストラクタ

**解説**

コンストラクタ

---

### lineCount

プロパティ \ アクセス: `r/w`

**解説**

行数（読み取り専用）

---

### totalCharCount

プロパティ \ アクセス: `r/w`

**解説**

総文字数（読み取り専用）

文字送りアニメーションの上限値に使用

---

### maxWidth

プロパティ \ アクセス: `r/w`

**解説**

レイアウトの最大幅（読み取り専用）

---

### maxHeight

プロパティ \ アクセス: `r/w`

**解説**

レイアウトの最大高さ（読み取り専用）

---

### isValid

プロパティ \ アクセス: `r/w`

**解説**

レイアウトが有効かどうか（読み取り専用）

layout() 呼び出し後に true になります

---

### totalRenderDelay

プロパティ \ アクセス: `r/w`

**解説**

全体の最大表示遅延時間（ms）（読み取り専用）

全文字の表示が完了するまでの時間です。
文字送りアニメーションのタイマー上限に使用します。

---

### layout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | スタイルタグ付きテキスト |
| `maxWidth` | `&nbsp;` | 最大幅 |
| `maxHeight` | `&nbsp;` | 最大高さ |
| `hAlign` | `&nbsp;` | 水平アライン (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | 垂直アライン (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `styles` | `&nbsp;` | Style 単体、またはスタイル名→Style の辞書 |
| `appearances` | `&nbsp;` | Appearance 単体、またはスタイル名→Appearance の辞書 |
| `lineSpacing` | `0` | 行間（省略時: 0） |

**解説**

テキストのレイアウトを計算

styles / appearances に単体オブジェクトを渡すと "default" キーとして扱われます。

使用例:
// 単一スタイル
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, appearance);

// 複数スタイル
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]);

---

### resolveAllTimings

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `timeScale` | `1.0` | 時間スケール係数（省略時: 1.0） |
| `widthTimeScale` | `false` | 文字幅による時間補正を行うか（省略時: false） |

**解説**

タイミング情報を解決する

layout() で生成されたタイミング情報（<start>, <delay>, <wait>, <sync>, <keywait> タグ）
を解決し、各文字の表示開始時間を計算します。

明示的に呼ばなくても、getResolvedTimings / getKeyWaits / totalRenderDelay /
calcShowCount の初回アクセス時にデフォルト値（timeScale=1.0, widthTimeScale=false）
で自動的に解決されます。

使用例:
sl.resolveAllTimings(1.0, false);
// 倍速表示
sl.resolveAllTimings(0.5, false);

---

### calcShowCount

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `time` | `&nbsp;` | 経過時間（ms） |

**戻り値**

表示すべき文字数

**解説**

指定時間までに表示すべき文字数を計算

drawStyledLayout の maxChars 引数に渡すことで、
時間ベースの文字送りアニメーションを実現できます。

使用例:
var count = sl.calcShowCount(elapsed);
layer.drawStyledLayout(sl, x, y, count);

---

### getKeyWaits

メソッド

**戻り値**

キー待ち情報の配列

**解説**

キー入力待ち情報を取得

各要素は辞書 %[pos, time] です。
- pos: 文字位置（charIndex）
- time: その時点での経過時間（ms）

<keywait/> タグの位置と、そこまでの累積表示時間を返します。

---

### getResolvedTimings

メソッド

**戻り値**

タイミング情報の配列

**解説**

解決済みタイミング情報を取得

各要素は辞書 %[charIndex, delay] です。
- charIndex: 文字位置
- delay: 表示開始時間（ms）

各文字がいつ表示されるかの詳細情報です。

---
