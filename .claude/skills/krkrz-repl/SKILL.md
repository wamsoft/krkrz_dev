---
name: krkrz-repl
description: 吉里吉里Z (krkrz) の SDL3 / WINVER ビルドを REPL 経由でエージェントから駆動するためのリファレンス。krkrz を起動して TJS スクリプトを評価・検証・デバッグする、startup.tjs を介さず明示的に処理を開始する、入力イベント (キー/マウス) を注入する、画面をキャプチャして目視確認する、Elements ダイアログを観測・操作する、例外やダイアログ表示をコンソールで観測する、といった場面で使う。**外部エージェントは console(CONIN$) に打てないので -replfile ファイルチャネルが本命**。起動フラグ (-repl / -replfile / -nostartup / -loglevel / -display)、ファイルチャネルのプロトコル、Agent API (入力注入 / captureScreen / dialogs / dialogClick)、ドットコマンド (.cap/.dlg/.click/.mem 等)、REPL 駆動時の挙動変更 (例外で即終了しない / inform と例外ダイアログがコンソールに出る) を網羅。TJS2 言語仕様そのものは skill `tjs2`、本体クラス API は skill `krkrz` を参照。
---

# krkrz REPL 駆動リファレンス

krkrz SDL3 ビルドには対話型 TJS シェル (REPL) が組み込まれている
(engine の `common/utils/REPL.cpp`)。エージェントが krkrz を立ち上げて
スクリプトを評価・検証するための仕組み。

## リポジトリ構成による読み替え (最初に確認)

このスキルは engine repo (krkrz.git / krkrz_develop.git) を対象にするが、
チェックアウト形態が 2 通りあり、**engine ソースのパス表記だけが異なる**。
REPL / Agent のプロトコルや TJS 側の使い方は同一。

| 形態 | engine ルート | 例: REPL 実装 | data 既定 | ビルド |
|---|---|---|---|---|
| engine 単独 (`krkrz` 等) | リポ直下 | `common/utils/REPL.cpp` | `data/` | `cmake --preset x64-windows` |
| umbrella (`krkrz_dev`) | `src/core/` | `src/core/common/utils/REPL.cpp` | `src/core/data/` | `make`(プリセットは `src/core/CMakePresets.json`) |

以降の本文は engine ルート相対 (`common/...`, `sdl3/...`, `doc/...`) で書く。
**umbrella で作業しているなら `src/core/` を前置して読む**。

**REPL 本体 + `-replfile` チャネルは全デスクトップ変種で有効** (`KRKRZ_REPL`
は `KRKRZ_DESKTOP` 既定。WIN32 = ON なので **WINVER (`x64-windows-win`) でも
TJS eval / 状態確認が `-replfile` でできる**)。REPL/実行キュー/ファイルチャネルは
`common/` にあり SDL 非依存。**Agent API・captureScreen も WINVER 対応済**
(2026-07-31):
- **Agent API** は `common/environ/AgentControlIntf.cpp` に共通化済。入力注入だけ
  `AgentInput` seam (`generic/environ/AgentInput.cpp` = SendMouseMessage/SendMessage、
  `win32/environ/AgentInput.cpp` = OnMouse*/OnKey*) でプラットフォーム分離。SDL3 /
  WINVER 両方で `Agent.click` / `keyPress` / `dialogs` / `dialogClick` / `text` が動く。
- **screencapture** も `BasicDrawDevice::FulfillScreenCapture[FromBackBuffer]` 実装済で
  WINVER で `System.captureScreen` / `Agent.captureScreen` が overlay 込み PNG を保存できる。

したがって **WINVER でも SDL3 と同様に GUI 検証 (入力注入 + captureScreen 目視) が可能**。
SDL3 専用として残るのは起動時 UserConfig UI (`-userconf`、ゲーム窓生成前の独立 OS
ウィンドウが必須) のみ。

## 重要: 作業に入る前に

1. **外部エージェント (Claude) が GUI の krkrz を駆動するなら `-replfile=<dir>`
   ファイルチャネルを使う**。`-repl` の console REPL は Windows で `CONIN$`
   (実コンソール) を読むため、ツールからは打ち込めない。ファイルチャネルなら
   `cmd`/`resp` ファイルの Write/Read だけで逐次駆動でき、`captureScreen` の
   PNG を Read で目視確認できる。→ 下の「ファイルチャネル駆動」。
2. REPL 駆動時は **例外で即終了しない / inform・例外ダイアログがネイティブ
   message box でなくコンソールに出る**。この差分を前提にログを読む。
3. `-replfile` と `-repl` は独立に起動できる (両方同時も可)。メイン実行は
   共有キュー `ReplMainQueue` で直列化される。

## 起動フラグ

| フラグ | 意味 |
|---|---|
| `-repl` | console REPL (CONIN$ 直読み) を起動。人間の対話向け。`-repl=no/off/false/0` で抑止。 |
| `-replfile=<dir>` | **ファイルチャネルを起動 (外部エージェント向け、本命)**。`<dir>` の `cmd`/`resp` ファイルで駆動。`-repl` と独立。 |
| `-replweb[=port]` | HTTP+SSE サーバ (既定 127.0.0.1:8899)。`GET /`=ブラウザ REPL ページ / `GET /events`=ログ SSE / `POST /cmd`=TJS 評価 / `GET /sub/<ch>`=汎用 SSE。**curl でも駆動できる** (`curl -X POST -d 'expr' http://127.0.0.1:8899/cmd`)。 |
| `-nostartup` | startup.tjs の自動実行を抑止。window 無し起動でも即終了しない。明示的にスクリプトを呼んで初めて処理が始まる。`-nostartup=no/off/false/0` で無効。 |
| `-loglevel=info` | ログレベル。コンソールに出る量を制御。`MASTER` ビルドだと既定 WARNING。 |
| `-display=<番号\|名前>` | 起動するディスプレイ (モニタ) の指定。**マルチディスプレイ環境でメインディスプレイを占有せずに検証したいときに使う**。番号は 1 origin (Windows の `\\.\DISPLAYn` の n)、名前はモニタ名の部分一致、`primary` も可。`-display=list` で一覧をログ出力。WINVER / SDL3 両対応。 |

### WebServer クラス (`-replweb` の拡張登録口)

`KRKRZ_REPL_WEB` ビルドではスクリプト/プラグインが web サーバへ機能を追加公開できる
(常時登録可、サーバ稼働時のみ配信)。**ハンドラは常にメインスレッド実行**。

- `WebServer.register(prefix, handler)` — 動的ハンドラ (最長一致)。
  `handler(%[method,path,query,body,bytes])` → 文字列=200 JSON / octet /
  整数=status / void=204 / `%[status,mime,body]`
- `WebServer.serveStatic(prefix, storageDir)` — Storages 経由の静的配信 (".." 拒否)
- `WebServer.broadcast(channel, text)` — `/sub/<channel>` 購読者へ SSE 配信
- `WebServer.active` / `WebServer.url` (= `System.replWebURL`)

詳細は engine `doc/REPL.md` の「ブラウザ REPL / Web サーバ」節。threepp の
ブラウザ編集 UI (threepp/docs/webui.md, `/ui/` + `/app/` + `/api/three/`) が実利用例。
検証は curl で足りる: ハンドラ登録は `-replfile` チャネルか `/cmd` から eval →
`curl http://127.0.0.1:8899/<path>` で応答確認。

代表的なエージェント起動 (ファイルチャネル + ゲーム画面あり):

```
krkrz64.exe <ABS_DATA_DIR> -replfile=<ABS_CHANNEL_DIR>
```

`-nostartup` を付けると startup.tjs を実行しない静止起動 (window も無い)。
描画やダイアログ検証には window が要るので、その場合はチャネルから明示的に
Window を作るか、startup.tjs を実行させる。

exe は krkrz_dev のビルド出力を使う (リポジトリルート相対):

- SDL3 版:   `build/x64-windows/core/Release/krkrz64.exe`
- WINVER 版: `build/x64-windows-win/core/Release/krkrz64.exe`

プロセスの起動・停止は skill `appctl` の規約に従うこと (PID を記録し、停止は
その PID のみ・exe パス照合付き。`taskkill /IM krkrz64.exe` のようなイメージ名
一括 kill は並行セッションを巻き添えにするため禁止)。`appctl` は別配布の
スキルなので、同梱ヘルパ `scripts/appctl.sh` の位置はそちらの SKILL.md を見る
(`$APPCTL` に入れてある想定で以下は書く)。

```bash
export APPCTL_DIR="$SCRATCHPAD/appctl"
S="$APPCTL"                    # appctl スキルの scripts/appctl.sh
CH="$SCRATCHPAD/replchan"

bash "$S" start krkr \
  "$REPO/build/x64-windows-win/core/Release/krkrz64.exe" \
  "$REPO/src/core/data" -readencoding=UTF-8 -replfile="$CH" -loglevel=info
# ... チャネル経由で評価・検証 ...
bash "$S" stop krkr
```

### パスの落とし穴

プロジェクトディレクトリ引数は **exe からの相対**で解決される。リポジトリの
data ディレクトリを使うなら **絶対パス**で渡す。相対 `data/` だと
`build/.../Release/data/` を探して "startup.tjs が見つかりません" になる。

リポジトリルート相対では `src/core/data/` ( umbrella の場合 )。engine 単独チェックアウト
なら `data/`。いずれも **絶対パスに展開して**渡すこと。

## REPL 駆動時の挙動変更 (このビルドで実装済み)

`TVPReplActive` (REPL 起動中 true、`SysInitIntf.h`) を見て、`Application->MessageDlg`
を呼ぶ各ラッパ側で分岐している (override 実装の `SDL3Application::MessageDlg`
本体は無改造)。

- **例外で即終了しない**: `TVPShowScriptException` は REPL 中、ネイティブ
  ダイアログ表示も `TVPTerminateSync` も行わず、例外メッセージ + trace を
  `TVPAddImportantLog` でコンソールに出すだけ。修正して再 eval できる。
- **System.inform → コンソール**: `TVPShowSimpleMessageBox` が REPL 中は
  `[dialog] caption: text` をログに出すだけで、ブロッキングな message box を
  出さない (既定応答で進む。応答取得は将来拡張)。
- **致命エラー (ShowException)**: `TVPLOG_CRITICAL` で出力済みなので REPL 中は
  message box を抑止。
- **System.confirm / Storages.selectFile / Storages.selectDirectory → エージェント応答**:
  REPL 中はネイティブモーダルを出さず、下記「モーダル応答チャネル」でエージェントが
  実際に応答を返せる (応答口が無ければ confirm は既定 Yes、選択はネイティブへ)。
  `inputString` は本体未実装 (将来対応予定)。

## モーダル応答チャネル (confirm / ファイル選択)

`-replfile=<dir>` 駆動中、本体が `System.confirm` / `Storages.selectFile` /
`Storages.selectDirectory` を実行すると、**cmd/resp とは別の専用ファイル対**で
応答を求めてくる。メイン実行はブロックするが、応答は別プロセス (エージェント) が
直接書くのでデッドロックしない。

プロトコル (`<dir>` 配下、cmd を投げた後):
1. 本体が要求 JSON を `<dir>/modal` に書く。例:
   - `{"type":"confirm","caption":"確認","text":"続行?"}`
   - `{"type":"selectFile","name":"","title":"開く","save":false}`
   - `{"type":"selectDirectory","name":"","title":"フォルダ","save":false}`
2. エージェントは `modal` の出現を検知し、応答を **`<dir>/modalresp`** に書く
   (プレーン文字列):
   - confirm         : `yes` / `no`
   - selectFile/Dir  : 返すパス (直接入力でよい) / 空文字列 = キャンセル
3. 本体が `modalresp` を読み、`modal`/`modalresp` を削除して処理続行 → 通常どおり
   `resp` に最終結果が出る。

つまり **selectFile/selectDirectory はダイアログを出さず、エージェントが返したい
パスを `modalresp` に直接書けばそれが選択結果になる** (`name` に正規化されて書き戻る)。

手順のキモ: `cmd` を投げたら `resp` を待つ前に **`modal` の出現をポーリング**し、
出たら `modalresp` を書く。その後 `resp` が出る。PowerShell 例:
```powershell
# cmd 送信後
while (-not (Test-Path "$chan/modal")) { Start-Sleep -Milliseconds 30 }
[IO.File]::WriteAllText("$chan/modalresp", "yes")   # or パス / "no" / ""
# この後 $chan/resp が出るので通常どおり読む
```

## ファイルチャネル駆動 (エージェント推奨)

`-replfile=<dir>` で起動すると、`<dir>` 配下のファイルで REPL を駆動できる。
console を介さないので Claude のツール (Write/Read) でそのまま操作できる。

プロトコル (lockstep):

1. コマンド (UTF-8 TJS) を `<dir>/cmd.tmp` に書き、`<dir>/cmd` に rename。
2. チャネルが実行し、結果 JSON を `<dir>/resp` に書く
   (`{"ok":bool,"result":"<pretty>","error":"<msg>"}`)。
3. `resp` の出現を待って読み、**削除してから**次の `cmd` を出す。
   (未読 `resp` が残る間は次コマンドを処理しない)

PowerShell ヘルパ例 (Move-Item で atomic rename → resp 待ち):

```powershell
function Send-Cmd($script, $timeoutMs = 5000) {
    $cmdTmp = "$chan/cmd.tmp"; $cmd = "$chan/cmd"; $resp = "$chan/resp"
    [IO.File]::WriteAllText($cmdTmp, $script, [Text.UTF8Encoding]::new($false))
    Move-Item -Force $cmdTmp $cmd
    $sw = [Diagnostics.Stopwatch]::StartNew()
    while ($sw.ElapsedMilliseconds -lt $timeoutMs) {
        if (Test-Path $resp) { Start-Sleep -Milliseconds 30
            $c = [IO.File]::ReadAllText($resp); Remove-Item -Force $resp; return $c }
        Start-Sleep -Milliseconds 30
    }
    "<TIMEOUT>"
}
```

起動 → 数秒待って window/DrawDevice 初期化 → `Send-Cmd` でコマンドを送る。
`win` 等 startup.tjs のグローバルもそのまま参照できる。

- 1 コマンド = 1 式/1 文。**複数文を `;` で繋ぐと syntax error** になることが
  あるので、分割送信するか `(function(){ ...; return x; })()` で包む。

## Agent API (入力注入 / キャプチャ / ダイアログ制御)

`Agent` は `System` 同様インスタンス不要でクラスメソッドを呼ぶ (SDL3 / WINVER +
`KRKRZ_USE_ELEMENTS` + `KRKRZ_USE_REPL` で登録。`KRKRZ_REPL=OFF` で消える)。入力は
実入力と同じ経路を通るのでゲームにも Elements ダイアログにも届く。

| メソッド | 用途 |
|---|---|
| `Agent.mouseMove/mouseDown/mouseUp(x,y[,btn[,shift]])` | マウス (論理座標、btn: 0=左1=右2=中) |
| `Agent.click(x,y[,btn[,shift]])` / `Agent.wheel(delta,x,y)` | クリック (move+down+up) / ホイール(120単位) |
| `Agent.keyDown/keyUp/keyPress(vk[,shift])` | キー (vk は `VK_*` 数値、例 `VK_RETURN`) |
| `Agent.text(str)` | アクティブダイアログへテキスト入力 (input_box 等) |
| `Agent.dialogs()` | アクティブダイアログ配列 `%[index,modal,active,screen,focused,x,y,w,h]` |
| `Agent.closeDialog()` / `Agent.closeAllDialogs()` | 最前面 / 全ダイアログを閉じる |
| `Agent.dialogClick(i,id)` / `Agent.dialogFocus(i,id)` | id 指定で起動 / フォーカス (座標不要) |
| `Agent.captureScreen(path[,x,y,w,h])` | overlay 込み実画面を**次フレーム**で PNG 保存 (戻り値=path) |
| `Agent.lastCapture()` | 直近キャプチャ結果 `%[path,width,height,ok]` |

検証フロー例 (ファイルチャネル)。`$CAP_DIR` はセッションの scratchpad など
書き込み可能な作業ディレクトリの絶対パス:

```
Send-Cmd "win.openMenu()"
Send-Cmd "Agent.dialogs()"                       # 状態確認 (screen/rect)
Send-Cmd "Agent.click(255,80)"                   # 座標クリックで遷移
Send-Cmd "Agent.dialogClick(0,'sound')"          # or id 指定で操作
Send-Cmd "Agent.captureScreen('$CAP_DIR/cap.png')" # 即 return、~1 フレーム後に保存
# (少し待って) Read tool で cap.png を開いて目視確認
```

`captureScreen` は内部で `RequestUpdate` を呼ぶのでアイドルでも保存される。
既定 DrawDevice は `SDLOGLDrawDevice` (GL) で、`glReadPixels` 経由で読み戻す。
**PrintWindow/BitBlt では GL クライアント領域が黒くなる問題を回避**できるのが
利点 (走らせて数百 ms 待って captureScreen→Read で目視、が定番)。

## stdin への TJS 送り込み (console REPL / 人間向け)

REPL worker は `ic_readline` (icline) または fgets shim で 1 行ずつ読む。
worker からのリクエストは main スレッドの `TVPDrainREPL()` が毎フレーム
1 件 drain して `TVPExecuteExpression` で実行する。

### バッチ実行 (推奨: 検証・スモーク用)

複数行を流して結果を拾う (data パスは絶対パスで、自分の構成に読み替え):

```bash
printf '%s\n' \
  'var w = new Window(); w.setSize(320,240); w.visible = true;' \
  'Debug.message("hello from repl");' \
  '1 + 2 * 3' \
  'exit' \
  | krkrz64.exe <ABS_DATA_DIR> -repl -nostartup -loglevel=info
```

`=>` 行が評価結果。`exit` / `quit` で REPL を閉じてプロセス終了。

### icline と TTY の注意

既定ビルドは icline (行編集・履歴・色) を使い、raw TTY を期待する。
パイプ stdin だと挙動が乱れる場合があるため、**エージェント/ヘッドレスで
パイプ駆動するなら `KRKRZ_REPL_LINE_EDIT=OFF` でビルド**すると fgets ベースの
shim (`KRKRZ_REPL_NO_ICLINE`) になり、パイプ stdin をそのまま素直に処理できる。

- engine 単独: `cmake --preset x64-windows -DKRKRZ_REPL_LINE_EDIT=OFF`
- umbrella: `PRESET=x64-windows CMAKEOPT='-DKRKRZ_REPL_LINE_EDIT=OFF' make prebuild build`

### 長いスクリプトは Storages 経由

複数行スクリプトは stdin で送るより、ファイルに置いて REPL から呼ぶ方が確実:

```tjs
Scripts.execStorage("mytest.tjs");      // data/ 配下 (autopath)
```

`-nostartup` で立ち上げてから上記でテストを開始する、が基本フロー。

## ドットコマンド (REPL 専用)

`.help` で一覧。主なもの:

| コマンド | 用途 |
|---|---|
| `.help` | コマンド一覧 |
| `.clear` | multiline 入力を破棄 |
| `.depth [N]` / `.compact [on/off]` | 結果の pretty-print 設定 |
| `.mem` | メモリ要約 1 行 (File/Bitmap/Sound/Global/Process/SysAlloc) |
| `.memdump` | 全メモリ統計をログへ (`TVPHeapDump`) |
| `.sysalloc` | システムアロケータ情報 |
| `.filecache` / `.imagecache` | ファイル/画像キャッシュ一覧をログへ |
| `.memoverlay [on/off]` / `.padoverlay [on/off]` | 画面オーバレイ表示トグル |
| `.mempeakclear` | peak_used リセット |
| `.cap [path]` | 画面キャプチャ (`Agent.captureScreen`、省略時 agent_cap.png) |
| `.dlg` / `.dlgclose` | ダイアログ一覧 / 全クローズ (`Agent.dialogs`/`closeAllDialogs`) |
| `.click X Y` | (X,Y) にクリック注入 (`Agent.click`) |

TJS の評価は dot で始まらない行をそのまま入力する (式・文どちらも可、
括弧/クォートが閉じるまで複数行継続)。

## 典型ワークフロー (エージェント)

1. `-repl -nostartup` で起動 (window も startup も無い静止状態)。
2. REPL から最小 Window を作って `visible=true` → SDL イベントループに入る
   (window が無いと描画ループに入らない種類の検証はこれが要る)。
3. 検証スクリプトを `Scripts.execStorage` か stdin で評価。
4. 例外が出てもプロセスは生きているので、コンソールの例外/trace を読んで
   スクリプトを直し、再度評価。
5. `.mem` 等で状態を観測。`exit` で終了。

## 関連 (パスは engine ルート相対 / umbrella では `src/core/` 前置)

- 言語仕様: skill `tjs2` / 本体 API: skill `krkrz`
- ビルド: engine 単独は `cmake --preset x64-windows`、umbrella は `make`
  (プリセット `src/core/CMakePresets.json`)。詳細は各 `CLAUDE.md`
- REPL 実装: `common/utils/REPL.cpp` / 共有実行キュー:
  `common/utils/ReplMainQueue.cpp` / ファイルチャネル:
  `common/utils/ReplFileChannel.cpp` / 有効化: CMake `KRKRZ_REPL`
  (= `KRKRZ_USE_REPL`)
- Agent API: `common/environ/AgentControlIntf.cpp` (共通) + 入力 seam
  `generic/environ/AgentInput.cpp` (SDL3/LIB) / `win32/environ/AgentInput.cpp` (WINVER) /
  キャプチャ: `common/visual/ScreenCapture.cpp`
- 詳細ドキュメント: `doc/REPL.md` の「エージェント駆動」節
- 複数ダイアログ同時表示の仕様: `doc/ElementsDialog.md`
