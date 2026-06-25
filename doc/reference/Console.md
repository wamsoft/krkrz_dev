# Console

Console クラスは、**コンソール**に関する管理を行うクラスです。このクラスからオブジェクトを作成することはできません ( このクラスにはアクセスできません )。このクラスのオブジェクトには `Debug.console` でアクセスできます。

## メンバー一覧

### プロパティ

- [visible](#visible)

---

### visible

プロパティ \ アクセス: `r/w`

**解説**

表示されているかどうか

コンソールが表示されているかどうかを表します。値を設定することもできます。

真を指定すると表示されます。

---

## プラグイン拡張: windowEx

Debug.console拡張

### メンバー一覧

#### メソッド

- [restoreMaxmimize](#restoremaxmimize)
- [maxmimize](#maxmimize)
- [getRect](#getrect)
- [setPos](#setpos)
- [getPlacement](#getplacement)
- [setPlacement](#setplacement)
- [bringAfter](#bringafter)

---

### restoreMaxmimize

メソッド

**解説**

ウィンドウ最大化の復帰（最大化のまま終了すると次回サイズが狂う問題解決用）

---

### maxmimize

メソッド

**解説**

ウィンドウを最大化

---

### getRect

メソッド

**解説**

座標・サイズの取得

---

### setPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

座標・サイズの設定

---

### getPlacement

メソッド

**解説**

WindowPlacementの取得

---

### setPlacement

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dict` | `&nbsp;` |  |

**解説**

WindowPlacementの設定

---

### bringAfter

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `win` | `&nbsp;` |  |

**解説**

※ 起動後１度はvisible=trueしてウィンドウを生成しないと失敗する 優先順位の変更

---
