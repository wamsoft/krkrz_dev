# WIN32DialogEX

WIN32Dialog を吉里吉里向けにもう少し使いやすくしたクラス
Scripts.execStorage("win32dialog.tjs")として使います。
詳細は当該ソースやサンプルなどを参照してください。

継承元: [WIN32Dialog](WIN32Dialog.md)

## メンバー一覧

### メソッド

- [store](#store)
- [setInitParams](#setinitparams)
- [open](#open)
- [setCenterPosition](#setcenterposition)
- [loadResource](#loadresource)
- [DefPushButton](#defpushbutton)
- [PushButton](#pushbutton)
- [AutoCheckBox](#autocheckbox)
- [CheckBox](#checkbox)
- [AutoRadioButton](#autoradiobutton)
- [RadioButton](#radiobutton)
- [GroupBox](#groupbox)
- [LText](#ltext)
- [CText](#ctext)
- [RText](#rtext)
- [Icon](#icon)
- [EditText](#edittext)
- [ListBox](#listbox)
- [ComboBox](#combobox)

---

### store

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | テンプレート用辞書配列<br>elm = %[ helpID, exStyle, style, x, y, cx, cy, menu, windowClass, title, pointSize, weight, italic, charset, typeFace,<br>items: [ コントロール1, コントロール2, ... ] ]; |

**解説**

テンプレートを流し込む

コントロールは，コントロール生成用の関数を呼びます。

---

### setInitParams

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | パラメータ辞書 |

**解説**

アイテムの初期化パラメータを設定する

必ず store() の後で呼ぶこと。パラメータ詳細は win32dialog.tjs や testscript.tjs を参照

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `parent` | `&nbsp;` |  |

**戻り値**

%[ result:EndDialogのnResult値, items:アイテムの状態辞書 ];

**解説**

ダイアログを表示する

WIN32Dialog.open と返り値が異なるので注意のこと

---

### setCenterPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `win` | `parent` | ウィンドウ（省略時はopen時の引数ウィンドウに対して）<br>nullを渡すと画面に対して中央になる |

**解説**

指定ウィンドウの中央位置にダイアログを移動

---

### loadResource

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | dllファイル（自動的にStorages.getPlacedPath/getLocalName処理される） |
| `resource` | `&nbsp;` | ダイアログリソース名 |

**解説**

ダイアログリソースを読み込む（オーバーライド）

---

### DefPushButton

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | テキスト |
| `id` | `&nbsp;` | コントロールID |
| `x` | `&nbsp;` | x座標（ダイアログ座標単位） |
| `y` | `&nbsp;` | y座標（ダイアログ座標単位） |
| `w` | `&nbsp;` | 横幅 （ダイアログ座標単位） |
| `h` | `&nbsp;` | 高さ （ダイアログ座標単位） |
| `style` | `&nbsp;` | スタイル |
| `ex` | `&nbsp;` | 拡張スタイル |

**解説**

各種コントロールを生成するための関数

---

### PushButton

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoCheckBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CheckBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoRadioButton

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RadioButton

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### GroupBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### LText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### Icon

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### EditText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ListBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ComboBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---
