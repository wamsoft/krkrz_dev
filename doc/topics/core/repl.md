# REPL (Read-Eval-Print Loop)

`KRKRZ_REPL=ON` でビルドされたバイナリにコマンドライン引数 `-repl`
( または `-repl=yes` ) を付けて起動すると、対話型 TJS シェルが有効に
なります。Windows / macOS / Linux 対応。行編集は
[icline](https://github.com/deths74r/icline) ( isocline フォーク ) を
利用しています。

詳細な仕様 ( コマンド一覧・編集機能・トラブルシューティング ) は
src/core 側のガイドを参照:

- [doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)

---

## 起動

```bash
krkrz -repl data/      # SDL 版
krkrz64 -repl data/    # Win32 版 (親コンソールに AttachConsole)
```

`-repl` が無ければ REPL は起動しません ( TTY 自動判定はありません )。
`-repl=no` / `-repl=off` / `-repl=false` / `-repl=0` で明示的に無効化も可能。

`KRKRZ_REPL_LINE_EDIT=OFF` でビルドすれば icline 依存なしの最小モードで
ビルドできます ( 矢印キー等の行編集機能は無効 )。

---

## 主な特殊コマンド

プロンプトは `krkrz>`、継続行は `...`。TJS の式や文をそのまま入力でき、
履歴は `.krkrz_history` に保存されます。

| コマンド | 説明 |
|---|---|
| `exit` / `quit` / `Ctrl+D` | REPL を抜けてアプリを終了 |
| `.help` | ヘルプ表示 |
| `.mem` | アロケータ + プロセスメモリの 1 行サマリ |
| `.memdump` | 詳細メモリ統計をログへダンプ |
| `.memoverlay [on\|off]` | 画面オーバレイの切替 ( SDL3 ビルド ) |
| `.mempeakclear` | peak 計測値を current_used に揃え直す |
| `.sysalloc` | システムアロケータ情報 ( 空き / 確保可能 / RSS ) を 1 行表示 |
| `.padoverlay [on\|off]` | パッドオーバレイの切替 ( SDL3 ビルド ) |
| `.filecache` | StorageCache ( file 層 ) 全エントリをログへダンプ |
| `.imagecache` | TVPGraphicCache ( decode 層 ) 全エントリをログへダンプ |
| `.cap [path]` | 次フレームの実画面 ( overlay 込み ) を PNG 保存 |
| `.dlg` | アクティブダイアログ一覧 |
| `.dlgclose` | 最前面ダイアログを閉じる |
| `.click <index> <id>` | id 指定の widget を起動 ( Enter 相当 ) |

メモリ系コマンドの詳細は [メモリ観測ガイド](memory_observation.md)、パッド
オーバレイの詳細は [PadOverlay](pad_overlay.md) を参照してください。

---

## REPL 起動中のエラーハンドラ動作

`-repl` または `-replfile` で REPL が有効なときは、未捕捉例外で吉里吉里
が即終了しなくなります。例外発生時はネイティブダイアログを表示せず、
スタックトレース付きでログ出力するだけに留まり、修正して再 eval できる
ようになります。同様に `System.inform` や `Application::MessageDlg` の
出力先は REPL コンソールへ振り替えられ ( 既定応答だけ返してダイアログは
出さない )、ヘッドレスな自動テストでも止まりません。

`-nostartup` を併用すると startup.tjs の自動実行も抑止できるので、
ウィンドウ無しで静止起動 → REPL から明示的に処理を起動、という流れが
組めます ( 詳細は [コマンドラインオプション](../../guide/CommandLine.md)
の `-nostartup` を参照 )。

---

## ファイルチャネル ( -replfile )

`-replfile=<dir>` を指定すると、コンソールを介さずファイルベースの
REPL チャネルが起動します。外部エージェントは指定ディレクトリ内の
コマンドファイルを書き込んで TJS 式を投げ、応答ファイルから結果 JSON
を読み取ります ( lockstep )。`-repl` と独立に有効化でき、両方同時に
利用しても構いません。

```bash
krkrz -replfile=./replbus data/
```

ヘッドレスな自動テストや、別プロセスのエージェントから krkrz を制御
する用途を想定しています。プロトコル詳細は src/core 側のドキュメントを
参照してください。

---

## エージェント駆動用 Agent クラス ( SDL3 ビルド )

`KRKRZ_REPL` ビルドの SDL3 版には、外部エージェント / 自動テストから
krkrz を駆動するための [Agent](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)
TJS クラスが組み込まれています。`System` クラスと同じくクラスメソッド
として呼び出します ( インスタンス化不要 )。

| 機能 | API ( 主要メソッド ) |
|---|---|
| 入力注入 | `Agent.mouseMove / mouseDown / mouseUp / click / wheel`、`Agent.keyDown / keyUp / keyPress`、`Agent.text` |
| ダイアログ観察 / 制御 | `Agent.dialogs()` / `Agent.dialogTree(index)` / `Agent.dialogClick(index, id)` / `Agent.dialogFocus(index, id)` / `Agent.closeDialog()` / `Agent.closeAllDialogs()` |
| 画面キャプチャ | `Agent.captureScreen(path[, x, y, w, h])` / `Agent.lastCapture()` |

`Agent` 経由の入力は実入力と同じ `TTVPWindowForm::Send*` 経路を通るので、
ゲームにも [Dialog](../../reference/Dialog.md) にも届きます。
`captureScreen` は overlay 込みの実画面を次フレームの present 直前に
読み戻して PNG 保存します ( 要求した時点でアイドルでも 1 フレーム後に
保存される )。

クラスは `KRKRZ_REPL=ON` の SDL3 ビルドでのみ登録されます。仕様の詳細
( ボタン定数、shift マスク、ファイルチャネルのプロトコル等 ) は
[doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)
を参照してください。
