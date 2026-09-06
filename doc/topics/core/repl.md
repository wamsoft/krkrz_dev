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

### オプション一覧

REPL 関連のオプションはここに集約します ( 詳細は各節、書式は
[コマンドラインオプション](../../guide/CommandLine.md) )。いずれも独立で、
同時指定できます。

| オプション | 既定 | 内容 |
|---|---|---|
| `-repl[=yes\|no\|new]` | 無効 | コンソール REPL。`new` は新規コンソールを強制 |
| `-replfile=<dir>` | 無効 | ファイルチャネル ( **エージェント駆動の本命** ) |
| `-replsocket=<name>` | 無効 | abstract unix socket チャネル ( Linux 系 ) |
| `-replweb[=[host:]port]` | 無効 | HTTP + SSE サーバ + ブラウザ UI ( 既定 127.0.0.1:8899 ) |
| `-replwebopen=app\|tab\|no` | 条件付き自動 | ブラウザの自動オープン。**端末起動では既定で開かない** |
| `-replwebidle=<秒>\|no` | **5 秒** | ブラウザが居なくなってから終了するまで |
| `-replwebpad=<dir>` | 書込禁止 | Pad タブの [保存] を許すストレージ接頭辞 |
| `-replwatchfile=<path>\|no` | `.krkrz_watch` | 監視式リストの保存先 |
| `-replmodaltimeout=<秒>` | 30 | モーダル応答待ちのタイムアウト ( 0 = 無限 ) |

`-nostartup` ( startup.tjs を実行しない ) と `-loglevel=` は REPL 専用では
ありませんが、エージェント駆動でよく併用します。

---

## 主な特殊コマンド

プロンプトは `krkrz>`、継続行は `...`。TJS の式や文をそのまま入力でき、
履歴は `.krkrz_history` に保存されます。

| コマンド | 説明 |
|---|---|
| `exit` / `quit` / `Ctrl+D` | REPL を抜けてアプリを終了 |
| `.help` | ヘルプ表示 |
| `.clear` | 継続入力中のバッファをクリア |
| `.depth [N]` | 結果表示の展開深さを表示 / 設定 |
| `.compact [on\|off]` | 結果表示のコンパクトモードを切替 |
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
| `.click X Y` | (X,Y) にマウスクリックを注入 ( `Agent.click` ) |
| `.watch` | 監視式の一覧を `id: 式 = 値` で表示 ( 表示前に全件評価 ) |
| `.watch add EXPR` | 監視式を追加して即評価 |
| `.watch rm ID` / `.watch rm all` | 監視式の削除 / 全消し |
| `.watch edit ID EXPR` | 監視式の差し替え |
| `.watch auto [ms\|on\|off]` | 自動更新の間隔を表示 / 設定 ( `on` = 500ms、`0` = 毎フレーム、下限 100ms ) |
| `.event [on\|off\|toggle]` | `System.eventDisabled` の表示 / 切替 |

メモリ系コマンドの詳細は [メモリ観測ガイド](memory_observation.md)、パッド
オーバレイの詳細は [PadOverlay](pad_overlay.md) を参照してください。

`.watch` は吉里吉里2 が本体に持っていたデバッグ窓「監視式」に相当します。
式を登録しておくと、`.watch` を打つたび ( または自動更新の間隔ごとに ) まとめて
評価して式と値を並べます。評価コンテキストは global 固定で、式が例外を投げても
`(error) <メッセージ>` を**値として**表示するだけなので、監視式が 1 本壊れても
REPL もアプリも死にません。

式の一覧と自動更新間隔は**カレントディレクトリの `.krkrz_watch` に保存**され、
次回起動で読み戻ります ( `-replwatchfile=<path>` で変更、`=no` で無効 )。

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

先頭が `.` の行は**特殊コマンド**として扱われ、コンソール REPL と同じ出力が
応答 JSON の `result` に入ります ( `.watch` / `.mem` / `.cap` などをそのまま
エージェントから叩けます )。

---

## ブラウザ UI ( -replweb )

`GET /` が返す埋め込みページは **Console / Watch のタブ構成**です。

| タブ | 中身 |
|---|---|
| Console | 上=ログ / 下=入力 ( 従来のページ ) |
| Watch | 監視式の表 ( 式 / 値 ) + 追加・削除・インライン編集 ( ダブルクリック ) + 自動更新間隔 |
| Pad | スクリプトエディタ。複数行を Ctrl+Enter で実行、ストレージへの読込 / 保存 |

本体埋め込みなので `-replweb` だけで完結します ( プラグインもスクリプトも不要 )。
自前 UI に差し替えたい場合は `WebServer.serveStatic` を使ってください。

### ブラウザ UI とアプリの寿命をそろえる

ブラウザを UI にした構成では、**片方だけ残る**のがいちばん困ります
( ウィンドウを閉じたのに本体が残る / 本体が終わったのに «disconnected» の
ページが残る )。両方向を閉じます。

**本体側** — ブラウザが居なくなったら終了 ( `-replwebidle` )

| 状態 | 動作 |
|---|---|
| 起動〜**最初の接続が来るまで** | 待機 ( いつまでも終了しない ) |
| 接続が 1 本以上ある | 動き続ける |
| 接続が全部消えた | `<秒>` 後に終了 |

**既定は有効 ( 5 秒 )**。`-replwebidle=no` で無効、`=<秒>` で秒数指定。
**一度でも接続が来てから武装する**ので、ブラウザを開かないエージェント駆動や
API 面としての利用は影響を受けません。ページを閉じる際は合図 ( `POST /bye` )
が飛ぶので、通常は 2 秒ほどで終了します。

**ブラウザ側** — 本体が居なくなったら閉じる

| 状態 | 動作 |
|---|---|
| 本体が終了を通知 ( `/sub/state` の `exiting` ) | 即座にウィンドウを閉じる |
| SSE が切れて 5 秒復帰しない ( クラッシュ等 ) | ウィンドウを閉じる |
| `window.close()` が効かない ( 通常タブ ) | 「吉里吉里Z が終了しました」を全面表示 |

### Pad ( スクリプトエディタ )

複数行の TJS を書いて **Ctrl+Enter でまるごと実行**します ( `/cmd` の 1 行実行と
違い、関数定義やループをそのまま流せます )。本文はブラウザの `localStorage` に
自動保存されるので、リロードしても消えません。

パス欄 + [読込] / [保存] でストレージとやりとりできますが、**保存は既定で禁止**
です。`-replwebpad=<dir>` を指定したときだけ、その配下へ書けます
( 「UI の [保存] をうっかり押して資材を上書きしない」ための柵。
`-replweb` を開いた時点で任意の TJS が実行できるので、セキュリティ境界では
ありません )。

### ブラウザの自動オープン ( -replwebopen )

既定では「ループバック束縛 かつ コンソール無し ( GUI 起動 )」のときだけアプリ
モードで開きます。**端末から起動したときは開きません**。明示指定は
`-replwebopen=app` ( アプリモード ) / `tab` ( 通常ウィンドウ ) / `no` ( 開かない )。
端末から起動しつつブラウザも開きたいときは `-replwebopen=app` を使います。

---

## 監視式の HTTP API ( -replweb )

`-replweb` を併用すると、監視式をブラウザや curl からも扱えます。

| ルート | 説明 |
|---|---|
| `GET /watch` | 一覧 + 現在値 ( JSON )。**評価しない**のでポーリングしても安全。`?eval=1` で評価してから返す |
| `POST /watch` | 操作 ( form-urlencoded )。`op=add&expr=…` / `op=rm&id=…` / `op=edit&id=…&expr=…` / `op=clear` / `op=interval&ms=…` / `op=eval` |
| `GET /sub/watch` | 自動更新の push ( SSE )。値が変わったときと、評価を伴わない変更 ( 削除 / 全消し / 間隔変更 ) のとき |

```bash
curl -s -X POST -d 'op=add&expr=System.getTickCount()' localhost:8899/watch
curl -s -X POST -d 'op=interval&ms=500'                localhost:8899/watch
curl -N localhost:8899/sub/watch
```

応答と push は同じ形です。

```json
{"interval":500,"entries":[{"id":1,"expr":"System.getTickCount()","value":"32470","error":false}]}
```

---

## ソケットチャネル ( -replsocket / Linux 系限定 )

`-replsocket=<name>` ( または環境変数 `KRKRZ_REPL_SOCKET` ) を指定すると、
abstract namespace の Unix ドメインソケットを listen するコマンドチャネルが
起動します ( Linux 系ビルド限定。他 OS では無視されます )。ファイルチャネル
のソケット版で、1 行 = 1 コマンド ( TJS 式 ) を受け取り、メインスレッドで
実行して 1 行 JSON で応答します。`-repl` / `-replfile` とは独立に起動でき、
同時利用も可能です。

- 行末に `\` を置くと継続行として扱われ、改行を保ったまま複数行を
  1 コマンドとして実行できます ( `nc` などからも使えるワイヤ上の継続
  マーカーです )。
- 単一行の先頭が `.` のものはチャネル側の dot コマンドとして解釈されます
  ( `.help` / `.depth` / `.compact` )。

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
ゲームにも [Dialog](../../reference/ElementsDialog.md) にも届きます。
`captureScreen` は overlay 込みの実画面を次フレームの present 直前に
読み戻して PNG 保存します ( 要求した時点でアイドルでも 1 フレーム後に
保存される )。

クラスは `KRKRZ_REPL=ON` の SDL3 ビルドでのみ登録されます。仕様の詳細
( ボタン定数、shift マスク、ファイルチャネルのプロトコル等 ) は
[doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)
を参照してください。
