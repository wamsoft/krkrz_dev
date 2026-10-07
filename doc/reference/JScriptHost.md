# JScriptHost

JScript 実行用ホスト。IActiveScript を利用して JScript の式評価と結果取得ができます。
例:
var js = new JScriptHost();
var r = js.eval("1+2"); // -> 3
js.addGlobal("tvp", global); // TJS の global オブジェクトを JScript 側に追加
var v = js.eval("tvp.version");

## メンバー一覧

### コンストラクタ

- [JScriptHost](#jscripthost)

### メソッド

- [eval](#eval)
- [addGlobal](#addglobal)
- [reset](#reset)
- [invoke](#invoke)
- [set](#set)
- [get](#get)
- [missing](#missing)

---

### JScriptHost

コンストラクタ

**解説**

コンストラクタ

JScript エンジンを生成して接続します。

---

### eval

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 評価する JScript の式文字列 |

**戻り値**

評価結果 (数値/文字列/bool/IDispatch ラップ 等)

**解説**

式評価

---

### addGlobal

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | JScript 側で参照する名前 |
| `obj` | `&nbsp;` | 追加するオブジェクト (TJS オブジェクト; IDispatch として公開) |

**解説**

グローバルオブジェクト追加（JScript 内部の namedObject 一覧に登録）

---

### reset

メソッド

**解説**

エンジン再初期化

スクリプト状態を初期化し直します。

---

### invoke

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | メソッド名 |
| `...` | `&nbsp;` | 以下パラメータ |

**解説**

メソッドの実行

---

### set

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | プロパティ名 |
| `value` | `&nbsp;` |  |

**解説**

プロパティの設定

---

### get

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | プロパティ名 |

**戻り値**

設定値

**解説**

プロパティの取得

---

### missing

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `...` | `&nbsp;` |  |

**解説**

TJS missing処理。未登録の名前はそのまま set/get/invoke 処理が試みられます

---
