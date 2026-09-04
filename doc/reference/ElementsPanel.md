# ElementsPanel

Elements の画面をホストのレイヤへ描くパネル

[ElementsDialog](ElementsDialog.md) と同じ画面 JSON を、overlay ( 常に最前面 )
ではなく **指定した [Layer](Layer.md) のビットマップへ描画**するクラスです。
z 順・トランジション ( `[trans]` )・スクリーンショット ( piledCopy )・入力の
帰属がすべて吉里吉里のレイヤの仕組みに従うため、本文の上に UI が被らない
HUD、ゲーム画面の一部としての UI、トランジションに乗せたい画面などに
使います。

```tjs
var lay = new Layer(win, win.primaryLayer);
lay.setImageSize(400, 300);
lay.setSizeToImageSize();
lay.type = ltAlpha;      // ltAddAlpha なら変換なしでさらに軽い
lay.hitThreshold = 0;    // すべてのマウスメッセージを受ける
lay.visible = true;

var panel = new ElementsPanel(lay);
panel.onAction = function(id, payload) { ... };
panel.showFile("ui/hud.jsonc");

// レイヤの入力をパネルへ流す ( Layer 派生で 1 回書けばよい )
lay.onMouseDown = function(x, y, b, f) { panel.mouseDown(x, y, b, f); };
lay.onMouseUp   = function(x, y, b, f) { panel.mouseUp  (x, y, b, f); };
lay.onMouseMove = function(x, y, f)    { panel.mouseMove(x, y, f); };
```

イベント ( [onAction](#onaction) / [onDrag](#ondrag) / [onVar](#onvar) /
[onClose](#onclose) ) と変数 store の API ( [setVar](#setvar) /
[getVar](#getvar) / [listVars](#listvars) / [watchVars](#watchvars) ) は
ElementsDialog と同じ形なので、既存の画面ドライバをほぼそのまま載せられます。

ElementsDialog ( overlay ) との違い:

- 入力インターセプトやウィンドウクローズ抑止に影響しません
- `Agent.dialogs()` / `closeAllDialogs()` には現れません
- モーダル結果・navigator フロー・仮想キーボード・ホストホットキー表は
持ちません ( 1 パネル = 1 画面。画面切替は showJson を呼び直すか、
レイヤを 2 枚にして `[trans]` に任せます )
- キー / パッド入力は既定では受けません。効かせたい画面だけ
[keyDown](#keydown) / [keyUp](#keyup) / [text](#text) をスクリプトから
流します

テーマ・表示言語・[ElementsDialog.registerImage](ElementsDialog.md#registerimage)
の実行時画像ストアはプロセス全体で共有され、パネルにも反映されます。

## メンバー一覧

### コンストラクタ

- [ElementsPanel](#elementspanel)

### プロパティ

- [active](#active)
- [focused](#focused)
- [watchVars](#watchvars)

### メソッド

- [showFile](#showfile)
- [showJson](#showjson)
- [showDict](#showdict)
- [close](#close)
- [notifyResized](#notifyresized)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [mouseMove](#mousemove)
- [mouseWheel](#mousewheel)
- [mouseLeave](#mouseleave)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [text](#text)
- [setVar](#setvar)
- [getVar](#getvar)
- [listVars](#listvars)
- [invalidate](#invalidate)
- [focus](#focus)
- [activate](#activate)

### イベント

- [onAction](#onaction)
- [onDrag](#ondrag)
- [onVar](#onvar)
- [onClose](#onclose)

---

### ElementsPanel

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 描画先の [Layer](Layer.md)。 |

**解説**

ElementsPanel オブジェクトの構築

描画先のレイヤを指定してパネルを構築します。描画はレイヤの画像サイズ
いっぱいに行われます。

---

### active

プロパティ \ アクセス: `r`

**解説**

画面を開いているか

---

### focused

プロパティ \ アクセス: `r`

**解説**

現在フォーカス中の widget id

フォーカスが無ければ空文字列です。

---

### watchVars

プロパティ \ アクセス: `r/w`

**解説**

どの変数の変化を onVar で受けるか

[ElementsDialog.watchVars](ElementsDialog.md#watchvars) と同じです。
void ( 既定 ) = onVar を実装しているときだけ全変数 / `"*"` = 全変数 /
`[]` = 観測しない / `[名前, ...]` = その変数だけ。

---

### showFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 画面 JSON の統一ストレージパス。 |

**戻り値**

開けたかどうか。

**解説**

画面 JSON をファイルから開く

画面 JSON ( jsonc 可 ) をファイルから読み込み、レイヤへの描画を開始します。
画面内の相対資材パスはその JSON があるディレクトリ起点で解決されます。

---

### showJson

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `json` | `&nbsp;` | 画面 JSON 文字列。 |

**戻り値**

開けたかどうか。

**解説**

画面 JSON を文字列から開く

---

### showDict

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | レイアウトの Dictionary。 |

**戻り値**

開けたかどうか。

**解説**

Dictionary で書いたレイアウトを開く

TJS の Dictionary / Array で書いたレイアウトを開きます (
[ElementsDialog.showDict](ElementsDialog.md#showdict) と同じ形式 )。

---

### close

メソッド

**解説**

パネルを閉じる

画面を破棄して描画を止めます。レイヤ自体は残る ( 最後の描画内容も
消えない ) ので、必要ならホスト側でクリアしてください。

---

### notifyResized

メソッド

**解説**

レイヤのサイズ変更をパネルへ通知する

描画先レイヤの画像サイズを変えた後に呼びます。次フレームから新しい
サイズで描画されます。

---

### mouseDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | レイヤ local X 座標。 |
| `y` | `&nbsp;` | レイヤ local Y 座標。 |
| `button` | `0` | = 0 マウスボタン ( 0 = 左 / 1 = 右 / 2 = 中 )。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**解説**

マウス押下をパネルへ流す

座標はレイヤ local ( Layer.onMouseDown の引数そのまま ) です。

---

### mouseUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | レイヤ local X 座標。 |
| `y` | `&nbsp;` | レイヤ local Y 座標。 |
| `button` | `0` | = 0 マウスボタン。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**解説**

マウス解放をパネルへ流す

---

### mouseMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | レイヤ local X 座標。 |
| `y` | `&nbsp;` | レイヤ local Y 座標。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**解説**

マウス移動をパネルへ流す

---

### mouseWheel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `delta` | `&nbsp;` | 回転量 ( 120 単位 )。 |
| `x` | `&nbsp;` | レイヤ local X 座標。 |
| `y` | `&nbsp;` | レイヤ local Y 座標。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**解説**

ホイール回転をパネルへ流す

---

### mouseLeave

メソッド

**解説**

マウスがレイヤから出たことをパネルへ流す

---

### keyDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 仮想キーコード。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**戻り値**

パネルが消費したかどうか。

**解説**

キー押下をパネルへ流す

パネルは既定でキーボードフォーカスを取らないので、キーを効かせたい
画面だけスクリプトから流します。

---

### keyUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 仮想キーコード。 |
| `shift` | `0` | = 0 シフト状態ビットフラグ。 |

**戻り値**

パネルが消費したかどうか。

**解説**

キー解放をパネルへ流す

---

### text

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 入力する文字列。 |

**解説**

テキスト入力をパネルへ流す

input_box へのテキスト入力 ( IME / 貼り付け相当 ) です。

---

### setVar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 変数名。 |
| `value` | `&nbsp;` | 設定する値 ( 文字列 )。 |

**戻り値**

書き込めたかどうか。

**解説**

表示中画面の変数を書き換える

[ElementsDialog.setVar](ElementsDialog.md#setvar) と同じです。

---

### getVar

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 変数名。 |

**戻り値**

変数の値 ( 文字列 )。未知の変数 / 未オープンなら void。

**解説**

表示中画面の変数を読み出す

[ElementsDialog.getVar](ElementsDialog.md#getvar) と同じです。

---

### listVars

メソッド

**戻り値**

変数記述 Dictionary の配列。未オープンなら空配列。

**解説**

表示中画面の変数一覧を取得する

[ElementsDialog.listVars](ElementsDialog.md#listvars) と同じです。

---

### invalidate

メソッド

**解説**

明示的な再描画を要求する

次フレームで画面全体を描き直します。通常は不要です ( 画面の変化は
自動で反映されます )。

---

### focus

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | フォーカスを移す widget の id。 |

**戻り値**

依頼できたかどうか。未オープンなら false。

**解説**

指定 id の widget へフォーカスを移す

[ElementsDialog.focus](ElementsDialog.md#focus) と同じです。input_box は
編集フォーカス ( キャレット表示 + テキスト受理 ) になります。

---

### activate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 実行する widget の id。 |

**戻り値**

実行できたかどうか。id 不明 / 未オープンなら false。

**解説**

指定 id の widget を実行する

フォーカスを移して実行 ( Enter 相当 ) します。
[ElementsDialog.activate](ElementsDialog.md#activate) と同じです。

---

### onAction

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 操作された widget の id。 |
| `payload` | `&nbsp;` | 値 ( button クリックは void、state widget は実値 )。 |

**解説**

widget 操作の通知

[ElementsDialog.onAction](ElementsDialog.md#onaction) と同じです。

---

### onDrag

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `payload` | `&nbsp;` | ドラッグ情報の Dictionary。 |

**解説**

ドラッグ通知

[ElementsDialog.onDrag](ElementsDialog.md#ondrag) と同じです。

---

### onVar

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 変数名。 |
| `value` | `&nbsp;` | 新しい値 ( 文字列 )。 |

**解説**

変数変化の通知

[ElementsDialog.onVar](ElementsDialog.md#onvar) と同じです。

---

### onClose

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `action` | `&nbsp;` | 閉じる契機になった action。 |

**解説**

画面が閉じたときの通知

[ElementsDialog.onClose](ElementsDialog.md#onclose) と同じです。

---
