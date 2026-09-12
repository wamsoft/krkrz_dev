# Agent

!!! warning "実験中 ( 安定保証の対象外 )"
    この API はまだ形が固まっていません。**予告なく変更・削除される
    ことがあります** ( 非互換変更でもメジャー番号は上がりません )。
    版の上げ方は [バージョン運用](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)
    を参照してください。

    開発・検証用の API です。REPL / デバッグ窓の整備にあわせて変わります。

Agent クラスはエージェント駆動 (テスト/自動化) のための API を提供するクラスです。このクラスからオブジェクトを作成することはできません。System と同様に `Agent.click(...)` のように直接呼び出して使用します。

このクラスは、入力イベント ( マウス / キー / ホイール ) の注入、実画面のキャプチャ、Elements ダイアログの観測・操作を行うための機能を提供します。外部エージェントから吉里吉里を駆動して動作を検証する用途を想定しています。

このクラスは REPL 機能が有効なとき ( コマンドラインオプションの `-repl` / `-replfile` / `-replweb` のいずれか ) かつ Elements を有効にしたビルドでのみ利用できます ( REPL 駆動については REPL.md を参照 )。

座標はすべて論理座標で指定します。`shift` 引数はシフト状態のビットフラグで、既定値は 0 です。`button` 引数は 0 = 左ボタン / 1 = 右ボタン / 2 = 中ボタンです。`vk` 引数は仮想キーコードの数値です。ダイアログ系のメソッド ( `dialogs` / `dialogTree` / `closeDialog` / `closeAllDialogs` / `dialogClick` / `dialogFocus` / `text` ) は Elements を有効にしたビルドでのみ動作します。

## メンバー一覧

### プロパティ

- [ignoreRealMouse](#ignorerealmouse)

### メソッド

- [mouseMove](#mousemove)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [click](#click)
- [wheel](#wheel)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [keyPress](#keypress)
- [text](#text)
- [dialogs](#dialogs)
- [imeStatus](#imestatus)
- [dialogTree](#dialogtree)
- [closeDialog](#closedialog)
- [closeAllDialogs](#closealldialogs)
- [dialogClick](#dialogclick)
- [dialogFocus](#dialogfocus)
- [captureScreen](#capturescreen)
- [lastCapture](#lastcapture)

---

### ignoreRealMouse

プロパティ \ アクセス: `r/w`

**型**: `Integer`

**解説**

実マウス入力を捨てる ( 動作テスト用 )

真にすると**実マウスの入力をすべて捨て**、Agent から注入された入力だけを
通します。自動テストで「入力は全部 Agent が出す」前提を作るためのもので、
人がうっかりポインタを動かしても測定が汚れません。

起動オプション `-ignoremouse=yes` を付けると最初から有効です。

hover 判定やカーソル参照は**仮想カーソル位置**を見るようになっており、
Agent の注入でその位置が更新されるので、有効にしてもホバーやフォーカスは
従来どおり動きます。

⚠ 有効にすると**人の手ではマウス操作できなくなります**。検証用です。

---

### mouseMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 移動先の X 座標を論理座標で指定します。 |
| `y` | `&nbsp;` | 移動先の Y 座標を論理座標で指定します。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

マウス移動の注入

指定した論理座標へのマウス移動イベントを注入します。

---

### mouseDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 座標を論理座標で指定します。 |
| `y` | `&nbsp;` | Y 座標を論理座標で指定します。 |
| `button` | `0` | ボタン番号を指定します ( 0 = 左 / 1 = 右 / 2 = 中 )。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

マウスボタン押下の注入

指定した論理座標でのマウスボタン押下イベントを注入します。

---

### mouseUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 座標を論理座標で指定します。 |
| `y` | `&nbsp;` | Y 座標を論理座標で指定します。 |
| `button` | `0` | ボタン番号を指定します ( 0 = 左 / 1 = 右 / 2 = 中 )。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

マウスボタン解放の注入

指定した論理座標でのマウスボタン解放イベントを注入します。

---

### click

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 座標を論理座標で指定します。 |
| `y` | `&nbsp;` | Y 座標を論理座標で指定します。 |
| `button` | `0` | ボタン番号を指定します ( 0 = 左 / 1 = 右 / 2 = 中 )。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

クリックの注入

指定した論理座標に対して、hover ( 移動 ) → 押下 → 解放 を一括で注入し、
1 回のクリック操作を再現します。

---

### wheel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `delta` | `&nbsp;` | 回転量を指定します ( 1 ノッチ = 120 単位 )。 |
| `x` | `&nbsp;` | X 座標を論理座標で指定します。 |
| `y` | `&nbsp;` | Y 座標を論理座標で指定します。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

マウスホイールの注入

マウスホイールの回転イベントを注入します。

---

### keyDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 仮想キーコード ( VK_* ) の数値を指定します。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

キー押下の注入

キー押下イベントを注入します。

---

### keyUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 仮想キーコード ( VK_* ) の数値を指定します。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

キー解放の注入

キー解放イベントを注入します。

---

### keyPress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 仮想キーコード ( VK_* ) の数値を指定します。 |
| `shift` | `0` | シフト状態のビットフラグを指定します。 |

**解説**

キー押下＋解放の注入

キーの押下と解放を一括で注入し、1 回のキー入力を再現します。

注入されるのは**キーイベントだけ**です。文字入力イベント
( [Window.onKeyPress](Window.md#onkeypress) ) は OS のテキスト入力経路を
通って発生するため、このメソッドでは発生しません。自動テストで文字を
入力したい場合は Elements の入力欄と [Agent.text](Agent.md#text) を
使用してください。

---

### text

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 送出する UTF-8 テキストを指定します。 |

**解説**

テキストの送出

アクティブな Elements ダイアログの入力欄 ( input_box ) へ UTF-8 テキストを
送出します。対象となる入力欄が無い場合は無視されます。

---

### dialogs

メソッド

**戻り値**

ダイアログ記述子の配列が返ります。各要素は
`%[index, modal, active, screen, focused, textFocus, x, y, w, h]` 形式の辞書です。

`textFocus` は「テキスト入力ウィジェット ( input_box 等 ) が編集フォーカスを
持っているか」で、ソフトキーボードや IME を開くかどうかの判断に使われている値
そのものです。日本語入力が始まらない等の切り分けに使えます。

`screen` はフロー ( navigator ) の現画面名で、単発のダイアログでは空です。
`focused` はフォーカス中のウィジェット id ですが、**id を追跡する仕掛けを持つ
画面でのみ埋まります**。空だからフォーカスが無い、という意味ではありません
( フォーカスの有無を見たいときは `textFocus` か
[Agent.dialogTree](Agent.md#dialogtree) を使ってください )。

**解説**

アクティブなダイアログ一覧の取得

現在アクティブな Elements ダイアログの記述子の配列を返します。

**関連:** [Agent.dialogTree](Agent.md#dialogtree)

---

### imeStatus

メソッド

**戻り値**

各ウィンドウの状態を表す辞書の配列が返ります。主な項目は次のとおりです。

`contextAttached` … 入力コンテキストが結び付いているか。**偽なら IME は完全に
無効**で、[Window.imeMode](Window.md#imemode) も半角/全角キーも効きません
( `Window.resetImeContext(false)` 等で切られた状態 )。`conversion` も 0 になります。

`hasFocus` … このウィンドウがキーボードフォーカスを持つか。偽の間は IME モードの
適用そのものが行われません。

`keyTrapperIsSelf` … 偽の場合、`trapKey` が真の別ウィンドウのモードが適用されます。

`imeMode` … 実際に適用しているモード。`defaultImeMode` は
[Window.imeMode](Window.md#imemode) が返す既定値です。

`overrideActive` … ElementsDialog のテキスト欄が IME を握っているか。
`contextForced` はそのために入力コンテキストを結び直したか。

`areaX` / `areaY` / `areaW` / `areaH` / `areaCursor` … IME の変換 / 変換候補
ウィンドウを寄せるために最後にホストへ渡した矩形 ( ウィンドウクライアント
座標 px ) と、その左端からのキャレット相対 x です。`areaValid` が偽なら
テキスト欄に編集フォーカスがありません。

ほかに `visible` / `trapKeys` / `attentionPoint` / `controlImeState` /
`disabledBySelf` / `imeAvailable` / `open` / `savedImeMode` / `conversion` /
`sentence` / `index` / `isMain` があります。SDL3 ビルドでは
`textInputActive` と上記の area 系のみが入ります。

**解説**

IME 状態の取得

ウィンドウごとの IME 関連の状態を返します。「入力欄にキャレットは出ているのに
日本語が打てない」といった不具合の切り分け用です。

Windows ネイティブ ( WINVER ) ビルドでのみ中身が入ります。他のビルドでは
常に空の配列が返ります。

**関連:** [Agent.dialogs](Agent.md#dialogs)

---

### dialogTree

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 対象とするダイアログのインデックスを指定します。 |

**戻り値**

ウィジェットの配列が返ります。各要素は `%[id, type, value]`
形式の辞書です。

**解説**

ダイアログのウィジェット一覧の取得

指定したダイアログの、id を持つウィジェットの一覧を返します。

**関連:** [Agent.dialogs](Agent.md#dialogs)

---

### closeDialog

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `0` | 対象とするダイアログのインデックスを指定します ( 現状この<br>引数は無視され、常に最前面のダイアログが閉じられます )。 |

**解説**

ダイアログを閉じる

最前面の Elements ダイアログを閉じます。

**関連:** [Agent.closeAllDialogs](Agent.md#closealldialogs)

---

### closeAllDialogs

メソッド

**解説**

すべてのダイアログを閉じる

すべての Elements ダイアログを強制的に閉じます。

**関連:** [Agent.closeDialog](Agent.md#closedialog)

---

### dialogClick

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 対象とするダイアログのインデックスを指定します。 |
| `id` | `&nbsp;` | 実行するウィジェットの id を指定します。 |

**解説**

ダイアログのウィジェットを実行する

指定したダイアログの id を持つウィジェットへ focus を移動し、実行します
( Enter 相当 )。座標を指定する必要はありません。

**関連:** [Agent.dialogFocus](Agent.md#dialogfocus)

---

### dialogFocus

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 対象とするダイアログのインデックスを指定します。 |
| `id` | `&nbsp;` | focus を移動するウィジェットの id を指定します。 |

**解説**

ダイアログのウィジェットへ focus を移動する

指定したダイアログの id を持つウィジェットへ focus を移動します。

**関連:** [Agent.dialogClick](Agent.md#dialogclick)

---

### captureScreen

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 保存先の統一ストレージパス ( .png ) を指定します。 |
| `x` | `0` | 保存範囲の左端を指定します。 |
| `y` | `0` | 保存範囲の上端を指定します。 |
| `w` | `0` | 保存範囲の幅を指定します ( 0 で画面全体 )。 |
| `h` | `0` | 保存範囲の高さを指定します ( 0 で画面全体 )。 |

**戻り値**

保存先パスが返ります。

**解説**

実画面を PNG 保存する

次フレームの present 込みで実画面を読み戻し、path へ PNG 保存する要求を
立てます。x, y, w, h で保存範囲を指定でき、w / h を 0 にすると画面全体に
なります。

**関連:** [System.captureScreen](System.md#capturescreen) / [Agent.lastCapture](Agent.md#lastcapture)

---

### lastCapture

メソッド

**戻り値**

`%[path, width, height, ok]` 形式の辞書が返ります。

**解説**

直近のキャプチャ結果の取得

直近の [Agent.captureScreen](Agent.md#capturescreen) の結果を返します。

**関連:** [Agent.captureScreen](Agent.md#capturescreen)

---
