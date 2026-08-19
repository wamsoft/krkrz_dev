---
name: krkrz-webui
description: 吉里吉里Z (krkrz) の -replweb HTTP+SSE サーバ (WebServer クラス) にブラウザ UI を載せて、本体アプリの操作/編集/観測パネルをブラウザ側に組み込む方法論。ゲーム本体は 3D 表示やゲーム内 UI に専念させ、編集ツール・インスペクター・ダッシュボード・REPL コンソールをブラウザ (別ウィンドウ/別PC) から使う構成を作るときに読む。プラグインや TJS がサーバへエンドポイントを追加公開する手順 (WebServer.register / serveStatic / broadcast)、ハンドラ呼び出し規約 (req %[method,path,query,body,bytes] → 文字列/octet/整数/辞書)、状態同期パターン (fetch POST + SSE /sub push + throttle + 差分/tick 配信)、既存 REPL コンソール (/events + /cmd) の UI 埋め込み、ブラウザのアプリモード起動 (Chromium --app / -webui)、json.dll 連携、TJS2 由来のハマりどころ (ローカル関数クロージャ不在→クラス化 / ブロックコメントのネスト誤爆 / startup 例外の致命性 / ハンドラは必ずメインスレッド実行) を網羅。エンジン側 WebServer クラスそのものの仕様は krkrz core doc/REPL.md、REPL/Agent 駆動は skill krkrz-repl、Elements ネイティブ UI は skill elements、TJS2 言語は skill tjs2、本体 API は skill krkrz を参照。
---

# krkrz replweb ベース ブラウザ UI 組み込み方法論

krkrz エンジンの `-replweb` HTTP+SSE サーバ (`KRKRZ_REPL_WEB` ビルド) に乗せて、
本体アプリの**操作・編集・観測 UI をブラウザ側に組み込む**ための方法論。
「ゲーム本体 = 表示 + ゲーム内 UI、ブラウザ = 編集ツール + インスペクター + REPL」
という分離を作れる。Elements ネイティブ UI (skill `elements`) の制約 (レイアウト/
入力/コピペ/フォント) から解放され、UI 反復にエンジン再ビルドが要らないのが利点。

エンジン側 `WebServer` クラスそのものの仕様は krkrz core `doc/REPL.md` の
「ブラウザ REPL / Web サーバ」節が SSOT。本スキルは**その上に UI を構築する側**の
設計パターンをまとめる。

本文のエンジンパスは engine ルート相対 (`doc/...`, `common/...`, `data/...`)。
本スキルが置かれている umbrella (`krkrz_dev`) では **`src/core/` を前置**して読む
(例: `src/core/doc/REPL.md`)。engine 単独チェックアウトならそのまま。

## いつ使うか / 使わないか

- **使う**: VRM/3D エディタ、ステージ/シーン編集、パラメータ調整パネル、ライブ
  インスペクター/ダッシュボード、リモート (別PC) 編集、REPL を UI に同居させたい。
- **使わない**: ゲーム内で完結する常駐 UI・モーダルダイアログ (→ skill `elements`)。
  ゲームの一部として配布する対話 UI は Elements、開発/編集ツールはブラウザ、が目安。

## 前提

- engine が `KRKRZ_REPL_WEB` ビルドであること (`WebServer` クラスが登録される)。
- **サーバ起動は `WebServer.start([port])` をスクリプトから呼ぶのが基本** (既定 8899)。
  `-replweb` オプションは不要 = 利用者に毎回付けさせなくてよい (アプリの startup で
  `if (!WebServer.active) WebServer.start(8899);`)。`-replweb[=port]` を明示した場合は
  本体が先に起動するので、`WebServer.start` は二重起動を避けて no-op になる。
  `0.0.0.0:<port>` で LAN 越し可 (`WebServer.startAt("0.0.0.0", port)`。信頼ネットワーク
  限定・起動ログに警告)。待受 URL は `WebServer.url` / `System.replWebURL`。
- JSON I/O を使うなら `json.dll` (`Scripts.toJSONString` / `evalJSON`)。下記参照。
- 検証には `krkrz-repl` (`-replfile` チャネル / `/cmd`) と curl が便利。

## 4 層アーキテクチャ

| 層 | 実体 | 役割 |
|---|---|---|
| ① サーバ | engine `common/utils/ReplWebServer.cpp` + TJS クラス `WebServer` (`ReplWebIntf.cpp`) | HTTP+SSE。ルーティング・静的配信・SSE チャネル。**ハンドラは常にメインスレッド実行** |
| ② ハンドラ | ネイティブ (プラグイン) or TJS | `/api/…` や `/app/…` を処理。重い/型変換が要る処理はネイティブ、細かい操作は TJS |
| ③ アプリブリッジ | TJS (アプリ側スクリプト) | アプリのモデル層 (状態取得/操作関数) を HTTP ルートへ橋渡し + 静的配信登録 + SSE 配信 |
| ④ ブラウザ UI | `data/ui/**` の静的 HTML/JS | 単一ページ (ビルドレス vanilla JS で十分)。fetch POST + SSE 購読 |

## 最小手順

### 1. 静的 UI を配信する
```tjs
// アプリ起動後 (startup.tjs 等) に一度
if (typeof global.WebServer != "undefined") {
    WebServer.serveStatic("/ui/", "ui/");   // data/ui/** を /ui/** で配信 (json.dll 不要)
}
```
`data/ui/index.html` を置けば `http://127.0.0.1:8899/ui/` で開ける。
静的配信は Storages 経由 (xp3 内でも可)。`..` はトラバーサル拒否 (403)。

### 2. 操作エンドポイントを登録する
```tjs
// TJS2 はローカル関数のレキシカルクロージャを持たない (下記ハマりどころ)。
// ハンドラはクラスのメンバにして objthis 経由で相互参照させる。
class AppBridge {
    function AppBridge() {}
    function handler(req) {
        // req = %[ method, path, query, body(文字列), bytes(octet: body 非空時) ]
        if (req.path == "/app/state") return Scripts.toJSONString(buildState());
        var arg = (req.body != "") ? Scripts.evalJSON(req.body) : %[];
        if (req.path == "/app/do") { app.doSomething(arg.x); push(); return "{\"ok\":true}"; }
        return %[ "status" => 404, "body" => "{}" ];
    }
    function buildState() { return %[ /* アプリ状態 */ ]; }
    function push() { WebServer.broadcast("state", Scripts.toJSONString(buildState())); }
}
global.bridge = new AppBridge();
WebServer.register("/app/", bridge.handler);   // プレフィックス最長一致
```

### 3. ブラウザから叩く (index.html 内)
```js
// 取得
const st = await (await fetch('/app/state')).json();
// 操作
await fetch('/app/do', {method:'POST', body: JSON.stringify({x:1})});
// 変更購読 (サーバ push)
const es = new EventSource('/sub/state');
es.onmessage = e => render(JSON.parse(e.data));
```

## WebServer API 早見表

| メンバ | 用途 |
|---|---|
| `WebServer.register(prefix, handler)` | 動的ハンドラ登録 (最長一致・上書き)。サーバ未起動でも保持され起動時から有効 |
| `WebServer.unregister(prefix)` | 解除 |
| `WebServer.serveStatic(prefix, storageDir)` | Storages 経由の静的配信。例 `("/ui/","ui/")` |
| `WebServer.unserveStatic(prefix)` | 静的マウント解除 |
| `WebServer.broadcast(channel, text)` | `/sub/<channel>` 購読者へ SSE 配信 (改行可) |
| `WebServer.start([port])` / `startAt(host, port)` | サーバをスクリプトから起動 (`-replweb` 不要)。既に稼働中なら no-op。戻り値=稼働中か |
| `WebServer.stop()` | サーバ停止 |
| `WebServer.openBrowser([url [, appMode=true]])` | url をブラウザで開く。appMode 時 Edge/Chrome を `--app` で試し不可なら既定ブラウザへ。url 省略で稼働中 URL。**SDL 版でもアプリモード可** |
| `WebServer.active` / `WebServer.url` | 稼働中か / 待受 URL |

組み込みルート: `GET /` = 素の REPL ページ / `GET /events` = ログ SSE /
`POST /cmd` = TJS 評価 / `GET /sub/<ch>` = 汎用 SSE。

## ハンドラ呼び出し規約

- 引数 `req` = `%[ method, path, query, body, bytes ]` (bytes は body 非空時のみ octet)。
- 戻り値の解釈:
  - 文字列 → 200 `application/json`
  - octet → 200 `application/octet-stream`
  - 整数 → そのステータスで空ボディ
  - void → 204
  - 辞書 `%[status, mime, body(文字列 or octet)]` → 明示指定
- ハンドラ内の TJS 例外 → 500 (本文=メッセージ) + `WebServer: handler error:` ログ。
- **ハンドラは必ずメインスレッドで呼ばれる** (`ReplMainQueue` タスク)。GL/TJS/エンジン
  API を自由に触ってよい。長い処理はフレームを止めるので注意 (Elements 版と同じ制約)。

## 状態同期パターン (実践)

- **client → server**: `fetch POST` (body=JSON)。スライダ等の連続入力は
  **throttle** (例 50ms、キー単位で最新値のみ送る)。連続反映系は `push()` しない
  (操作元が真実。SSE 逆流で入力が上書きされるのを防ぐ)。
- **server → client**: SSE `/sub/state`。
  - 各操作ルートの直後に `push()` (辞書一発)。
  - フレームループから ~4Hz で**差分検知 push** (前回 JSON と一致なら送らない)。
    これで REPL 等 UI 外からの変更もブラウザに自動反映される。
- **エディタ DOM の再構築を壊さない**: 高頻度で変わる観測データ (fps/ログ等) と
  編集状態を分け、編集状態が変わったときだけ DOM を作り直す (観測は別 DOM を差分更新)。
  スライダ操作中フラグを持ち、操作中は SSE 由来の再描画を抑止する。

## REPL コンソールを UI に同居させる

エンジン組み込みの `/events` (ログ SSE、バックログ2000行・レベル別 cls 付き) と
`/cmd` (POST body=1行を TJS 評価、応答 body は継続入力中なら "1") を**そのまま**
ブラウザ UI 側で購読・POST するだけ。エンジン改変なしで編集 UI に REPL を統合できる。
履歴 (↑↓) と継続プロンプト切替はブラウザ側で実装する。

## ブラウザをアプリモードで開く

Chromium 系の `--app=<URL>` でタブ/アドレスバー無しウィンドウになる。
**本体の `WebServer.openBrowser(url)` を使う**のが基本 (Edge → Chrome を `--app` で試し、
不可なら既定ブラウザへフォールバック)。エンジンが「URL を開く」(`TVPShellExecute`=
SDL は `SDL_OpenURL`) と「プログラムを引数付きで実行」(`TVPExecuteProgram`= デスクトップ
Windows は Win32 `ShellExecute`) を分けて実装しているので、**SDL 版でもアプリモードで
開ける** (`System.shellExecute` 直呼びは SDL で `--app` 引数が捨てられるため不可だった)。
```tjs
WebServer.openBrowser(("" + WebServer.url) + "ui/");   // url 省略で稼働中サーバ URL
```
`WebServer.start()` を先に呼んでいればサーバは同期的に稼働 (`WebServer.active`=true) なので、
**開くのを Timer で待つ必要はない** (起動直後にそのまま `openBrowser` してよい)。
旧エンジン (`openBrowser` 未実装) 向けにフォールバックを書くなら
`typeof WebServer.openBrowser != "undefined"` で分岐し、無い場合のみ従来の
`System.shellExecute("msedge.exe", "--app=" + url)` 列を使う。

## json.dll

`/app/` の JSON I/O には `json.dll` (`Scripts.toJSONString(v,indent)` /
`evalJSON(str)` / `evalJSONStorage(path,utf8)` / `saveJSON(path,v,utf8,indent)`) が要る。
exe と同世代のものを plugin フォルダへ。ビューア/最小起動では未リンクのことがあるので、
ブリッジ側で自力 `try { Plugins.link("json.dll"); } catch(e){}` を試み、不可なら
静的配信 (`/ui/`) だけ登録して操作系を無効化するとフォールバックが綺麗。

## ★ハマりどころ (TJS2/krkrz 由来)

1. **TJS2 にローカル関数のレキシカルクロージャは無い**: IIFE 内の関数同士の相互参照は
   実行時「メンバが見つかりません」。→ ハンドラ/ヘルパは**クラスのメンバ**にして
   `objthis` (インスタンス) 経由で解決する。`WebServer.register("/x/", obj.method)`
   で渡すと呼び出し時 objthis がそのインスタンスになる。
2. **TJS2 のブロックコメントはネスト可能**: コメント文中の `/ui/` + `*` のような並びが
   `/*` と誤認され「コメントが終わらないまま終端に達した」。→ ブリッジ/ハンドラを書く
   .tjs は**行コメント (`//`) のみ**にすると安全。
3. **startup スクリプト中の例外は致命**: REPL 保護 (`TVPReplActive`) は
   `TVPCreateREPL()` 後に立つため、startup から呼ぶ登録スクリプトのロード失敗は
   プロセスごと落ちる。登録処理は例外を出さないよう防御的に書く/切り分ける。
4. **ハンドラはメインスレッド実行**だが、HTTP スレッドは複数接続を捌く。共有状態は
   ハンドラ内 (メインスレッド) でのみ触る前提で設計する (engine が SubmitTask で
   直列化してくれる)。
5. **静的配信は json.dll 非依存**。UI ページだけ先に出したいときは serveStatic を
   register より先に無条件で呼ぶ。

## 検証

- ハンドラ登録は `-replfile` チャネル (skill `krkrz-repl`) か `/cmd` から eval し、
  `curl http://127.0.0.1:<port>/<path>` で応答確認 (ブラウザ不要で往復テストできる)。
- SSE は `curl -N http://127.0.0.1:<port>/sub/<ch>` で購読しつつ別で操作を投げる。
- 画面反映は `Agent.captureScreen(path)` → 画像を目視 (skill `krkrz-repl`)。
- UI の JS 構文チェックは `<script>` 部を抜き出して `node --check`。

## リファレンス実装 (krkr_threepp)

VRM 立ち絵/箱庭エディタの完全な実例:
- engine: `common/utils/ReplWebServer.cpp` (サーバ) / `ReplWebIntf.cpp` (TJS クラス) /
  `doc/REPL.md` (仕様 SSOT)
- プラグイン: `main.cpp` の `ThreeWebApi` (`/api/three/` をネイティブ公開。
  リンク時に POST_REGIST から `WebServer.register`、unlink 時に解除)。UI 向け一括
  JSON ダンプ `Object3D.treeJson` / `VRM.expressionListJson` / `morphListJson`
  (UTF-8→ttstr 変換ヘルパで日本語対応。既定 std::string コンバータは ASCII 限定)
- アプリ+UI: `data/webui.tjs` (`WebUIBridge`, `/app/…` ブリッジ) + `data/ui/index.html`
  (5 モード編集 + サイドバー + REPL コンソール)。設計詳細は `threepp/docs/webui.md`

関連スキル: `krkrz-repl` (REPL/Agent 駆動・-replweb 起動) / `elements` (ネイティブ UI) /
`krkrz` (本体 API: Storages/System/Plugins) / `tjs2` (言語仕様) / `dev-toolkit:msys2` (シェル)。
