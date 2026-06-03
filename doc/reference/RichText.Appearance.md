# RichText.Appearance

描画外観クラス

Illustrator のアピアランスに相当します。
塗り（Fill）とストローク（縁取り）を複数重ねて装飾効果を実現します。
先に追加したものが下（奥）に描画されます。

典型的な使用順序:
1. 影 (addShadow または addFill でオフセット付き)
2. 縁取り (addStroke)
3. 本体の塗り (addFill)

## メンバー一覧

### コンストラクタ

- [Appearance](#appearance)

### プロパティ

- [isEmpty](#isempty)
- [count](#count)

### メソッド

- [addFill](#addfill)
- [addStroke](#addstroke)
- [addShadow](#addshadow)
- [setColor](#setcolor)
- [addColor](#addcolor)
- [setOutline](#setoutline)
- [addOutline](#addoutline)
- [setShadow](#setshadow)
- [clear](#clear)
- [clone](#clone)

---

### Appearance

コンストラクタ

**解説**

コンストラクタ

---

### isEmpty

プロパティ \ アクセス: `r/w`

**解説**

スタイルが空かどうか（読み取り専用）

---

### count

プロパティ \ アクセス: `r/w`

**解説**

スタイル数（読み取り専用）

---

### addFill

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 (例: 0xFFFFFFFF = 白, 0xFF000000 = 黒) |
| `offsetX` | `0` | X方向オフセット（省略時: 0） |
| `offsetY` | `0` | Y方向オフセット（省略時: 0） |

**解説**

塗りの追加

使用例:
app.addFill(0xFFFFFFFF);  // 白で塗り
app.addFill(0x80000000, 2, 2);  // 半透明黒で影効果

---

### addStroke

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 |
| `width` | `&nbsp;` | 線幅 |
| `offsetX` | `0` | X方向オフセット（省略時: 0） |
| `offsetY` | `0` | Y方向オフセット（省略時: 0） |

**解説**

ストローク（縁取り）の追加

使用例:
app.addStroke(0xFF000000, 2);  // 黒2pxの縁取り

---

### addShadow

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 影色（ARGB） |
| `offsetX` | `&nbsp;` | X方向オフセット |
| `offsetY` | `&nbsp;` | Y方向オフセット |

**解説**

影の追加

影は自動的に一番下（奥）に追加されます。
使用例:
app.addShadow(0x80000000, 2, 2);  // 半透明黒の影

---

### setColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 |

**解説**

テキスト色の設定（既存の通常 Fill を置換）

既存の通常 Fill（オフセット 0,0 の Fill）を指定色に置き換えます。
通常 Fill が無い場合は新規追加します。
使用例:
app.setColor(0xFFFF0000);  // テキスト色を赤に変更

---

### addColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 |
| `offsetX` | `0` | X方向オフセット（省略時: 0） |
| `offsetY` | `0` | Y方向オフセット（省略時: 0） |

**解説**

テキスト色の追加（最前面に追加）

addFill と同様だが最前面に追加されます。

---

### setOutline

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 |
| `width` | `&nbsp;` | 線幅 |
| `offsetX` | `0` | X方向オフセット（省略時: 0） |
| `offsetY` | `0` | Y方向オフセット（省略時: 0） |

**解説**

縁取りの設定（既存の Stroke を置換）

既存の Stroke を指定のものに置き換えます。
Stroke が無い場合は新規追加します。

---

### addOutline

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB色値 |
| `width` | `&nbsp;` | 線幅 |
| `offsetX` | `0` | X方向オフセット（省略時: 0） |
| `offsetY` | `0` | Y方向オフセット（省略時: 0） |

**解説**

縁取りの追加（最背面 Stroke として追加）

---

### setShadow

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 影色（ARGB） |
| `offsetX` | `&nbsp;` | X方向オフセット |
| `offsetY` | `&nbsp;` | Y方向オフセット |

**解説**

影の設定（既存の影 Fill を置換）

既存の影（オフセット付き Fill）を指定のものに置き換えます。

---

### clear

メソッド

**解説**

全スタイルのクリア

---

### clone

メソッド

**戻り値**

複製された Appearance オブジェクト

**解説**

外観の複製

---
