# メモリ観測・リーク調査

吉里吉里Z のエンジンには、メモリ使用量とアロケータの内訳をリアルタイム
に観察するための一連の仕組みが組み込まれています。本ページは、その
**入口** をまとめたガイドです。設計上の詳細や根拠は src/core 側の
開発者ドキュメントを参照してください。

- 詳細ガイド: [doc/MemoryGuide.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryGuide.md)
- 設計・実装根拠: [doc/MemoryDesign.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryDesign.md)
- リーク監査の運用: [doc/LeakAudit.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LeakAudit.md)

---

## アロケータの構成

エンジン内のメモリは、用途別に 4 系統 + 外部に分かれて計測されます。

| アロケータ | 主な用途 |
|---|---|
| **FileAllocator** | StorageCache (file 層キャッシュ) のバイナリ |
| **BitmapAllocator** | `Bitmap` の bits 領域 |
| **SoundAllocator** | PCM / リングバッファ / DSP の作業領域 |
| **GlobalAlloc[Krkrz]** | `operator new` / `TJS_malloc` 経由の確保 (TLSF プール) |
| **GlobalAlloc[SDL]** | SDL3 内部の確保 (`KRKRZ_SDLMEMORY_STAT=ON` ビルド時のみ) |
| 外部 | ANGLE / miniaudio / opus / libpng 等の C ライブラリ内部 malloc、GL texture、直 HeapAlloc |

`GlobalAlloc[Krkrz]` はさらにスレッドローカルな **タグ** ごとに内訳
集計されます ( `TJS2` / `GraphicsLoader` / `User` / `Unknown` )。

---

## TJS2 から見る

[System](../../reference/System.md) クラスに観測 API があります。

- [System.getSystemAllocatorInfo](../../reference/System.md#getsystemallocatorinfo) — プロセス RSS / VSize、システム空きメモリを含む辞書を取得。
- [System.resetMemoryPeak](../../reference/System.md#resetmemorypeak) — peak 計測を現在値に揃え直す。
- [System.beginAllocTag](../../reference/System.md#beginalloctag) / [System.endAllocTag](../../reference/System.md#endalloctag) — スクリプト由来の確保をタグで分離計測。
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — 画面オーバレイの動的切替。

ファイルキャッシュ ( file 層 ) と画像デコードキャッシュ ( decode 層 )
は [Storages](../../reference/Storages.md) 側に観測 API があります。

- [Storages.getFileCacheList](../../reference/Storages.md#getfilecachelist) / [Storages.getImageCacheList](../../reference/Storages.md#getimagecachelist) — エントリ一覧を辞書配列で取得
- [Storages.dumpFileCacheList](../../reference/Storages.md#dumpfilecachelist) / [Storages.dumpImageCacheList](../../reference/Storages.md#dumpimagecachelist) — ログに WARNING レベルでダンプ
- [Storages.pinCache](../../reference/Storages.md#pincache) / [Storages.unpinCache](../../reference/Storages.md#unpincache) / [Storages.isCachePinned](../../reference/Storages.md#iscachepinned) — エントリ単位の pin 管理
- [Storages.clearTransientCaches](../../reference/Storages.md#cleartransientcaches) / [Storages.clearAllCaches](../../reference/Storages.md#clearallcaches) — 一括クリア

---

## 起動オプション

メモリ調査用の起動オプションが追加されています ( 詳細: [コマンドラインオプション](../../guide/CommandLine.md) )。

| オプション | 機能 |
|---|---|
| `-memoverlay=1` | 起動時から画面右上にメモリ状態をオーバレイ表示 ( 描画は OGL 系 / SDL の DrawDevice。WINVER 既定の D3D11 では表示されない ) |
| `-memstatinterval=N` | N 秒ごとにメモリ統計をログ出力 |
| `-memstatonexit=1` | 終了時にメモリ統計を 1 回ログ出力 |
| `-cachelistonexit=<mode>` | 終了時に Storages cache 一覧をダンプ ( `1`/`all`/`file`/`image`/`0`/`none` ) |

`KRKRZ_ENABLE_PERIODIC_DUMP=OFF` ビルドでは周期ダンプ系 (`memstat*`/`cachelistonexit`) は無視されます。

---

## REPL からの観察

[REPL](repl.md) を有効にしたビルドでは、対話シェルから直接メモリ状態を
覗き見ることができます ( `.mem` / `.memdump` / `.memoverlay` /
`.mempeakclear` / `.sysalloc` / `.filecache` / `.imagecache` 等 )。

---

## 何がメモリを持っているかを調べる ( 診断ビルド )

`GlobalAlloc[Krkrz]` の live が TJS オブジェクトの数では説明できないほど
大きいときは、`KRKRZ_ENABLE_MEMSTAT_DETAIL=ON` の診断ビルドで内訳を調べます。
製品ビルドには入りません ( Windows のみ )。

`.memdump` の出力に次の項目が加わります。

| 項目 | 内容 |
|---|---|
| `live by size` | 生存している確保の大きさ別の件数とバイト数 ( 半オクターブ刻み ) |
| `member tables` / `per-class member table bytes` | TJS オブジェクトのメンバ表 ( ハッシュ表のスロット配列と連鎖ノード ) の合計とクラス別の大きさ |
| `string heap` | TJS 文字列ヒープのブロック数・充填率・同じ内容の文字列の重複 |

さらに起動オプション `-memstatsite=<段数>` ( `yes` で 16 段 ) を付けると、
確保ごとにスタックを取って **呼び出し元別** に生存バイト数と件数を数えます。
`.memdump` の末尾と REPL の `.memsites [件数] [関数名の一部]` で、
アロケータ内部を飛ばした最初の関数ごと・呼び出し連鎖ごとに多い順で出ます。
PDB のあるモジュールは関数名とソース行、PDB の無いプラグイン DLL は
モジュール名付きで表示されます。

- 確保ごとにスタックを取るため、起動や処理はかなり遅くなります。
- 診断ビルドは確保ヘッダを 16 byte から 32 byte に広げてサイト番号を持つので、プロセス全体のメモリ量は製品ビルドと比べられません ( `GlobalAlloc[Krkrz]` の live は要求サイズの合計なので比べられます )。
- ログはコンソールログ ( `-forcelog=yes` ) に出ます。
