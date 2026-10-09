# 標準ツールの改定 (計画と進捗)

吉里吉里2 時代の標準ツール (krdevui.dll + krkrrel / krkrsign / krkrtpc / krkrlt / krkrfont
ほか、C++Builder 製・Windows 専用) を置き換える計画。索引は [TODO.md](TODO.md)。
完了した項目は消さずに ✅ と対応コミットを書いて残す。

## 方針

- **デスクトップ一式 (Windows / macOS / Linux) で動き、全ツールがコマンドラインでも動く**こと。
  GUI はブラウザを画面に使う (ローカル HTTP + ブラウザのアプリモード窓)。
- GUI と CLI は**同じ処理を呼ぶ** (GUI 専用の処理を作らない)。CI やビルドスクリプトから
  そのまま使えること。
- 旧ツールのファイル形式 (`.sli` / `.sig` / 公開鍵 PEM / xp3 / tlg / `.cf`) は**互換を保つ**。
  旧ツールで作ったものを新ツールで読める・逆も通ること。
- ドキュメントは `doc/guide/` の旧ツールのページを新ツールの説明で置き換える
  (旧ページは吉里吉里2 の exe の説明のまま残っている)。

## 廃止するもの

| 状態 | 対象 | 内容 |
|---|---|---|
| ✅ | 旧デバッガ (`src/tools/win32/debugger`) | 2026-10-08 にサブモジュールごと削除。本体の DAP + VSCode のデバッガで代替 ([Debug.md](doc/guide/Debug.md))。他からの参照は無かった |
| ✅ | レンダリング済みフォント作成ツール | 吉里吉里2 の krkrfont.exe は新しく作らない。**`.tft` の描画 (`Font.mapPrerenderedFont`) は残す**。作成手段はプラグイン `tftSave` (WIN 専用) とその同梱スクリプトのツールを残し、ガイド [FontMaker.md](doc/guide/FontMaker.md) を tftSave の説明に書き換えた (2026-10-08) |

## 構成 (A 案 / B 案)

| | A 案: 吉里吉里Z 本体 + プラグイン + ブラウザ UI | B 案: appserve で各ツールをネイティブに作る |
|---|---|---|
| 土台 | 本体の `WebServer` (`-replweb` 系) で UI を出し、処理は TJS + プラグイン | appserve (C++17、外部依存なし、localhost HTTP + SSE + ブラウザのアプリ窓。MIT) |
| 流用 | TLG5/6 保存・音声デコーダ・`getVowel` 等・psdfile / clipfile・sigcheck・XP3 読み込みを**そのまま使える** | 必要な部分をライブラリとして切り出してリンクする (下の「共通ライブラリ」) |
| CLI | `-nostartup` + スクリプト + `System.exit`。「スクリプトを実行して終了する」専用オプションが無いので足す必要あり | 同じ exe のサブコマンドとして素直に書ける (`App::addOption`、`run()` を呼ばずに処理を直接呼ぶ) |
| 重さ | 本体一式 + プラグイン DLL。起動時に描画系も初期化される (`-drawdevice=null` で回避) | ツールごとに exe 1 本 (UI は exe に埋め込める) |
| 対応 OS | SDL 版で Windows / Linux / macOS の実績あり | Windows / Linux は CI あり。macOS は分岐があるだけで未検証 |
| 足りないもの | 長時間処理の進捗 (`System.breathe` 中は TJS イベントが止まる) | ネイティブのファイル選択ダイアログが無い (fs モジュールのファイルブラウザで代用)。長時間ジョブ・進捗の仕組みが無い (ワーカー + SSE で自作)。v0.1 |

**B 案 + 共通ライブラリで進める (2026-10-08 決定)**。理由:

- 要件の «全部コマンドラインで動く» と «ツールごとに配れる» に素直に合う。本体を起動しないので
  CI・ビルドサーバで軽い。
- 流用したい処理 (TLG 保存、XP3、`.sli`、署名、PSD / CLIP、Vorbis / Opus) は、どれも本体の
  他の部分にほとんど依存しないか、もともと独立したライブラリ (psdparse / clipparse /
  libogg / libvorbis / libopus / libtomcrypt) なので、切り出すコストは低い。
- 本体と同じ挙動を保証したい箇所 (`.sli` の解釈、TLG の書式、XP3 の読み込み、署名の検証範囲)
  は**本体のソースを共通ライブラリから参照して同じコードを使う** (コピーしない)。

⇒ **フェーズ 0 で最小のツール 1 本 (ファイル破損チェック) を作り、共通の枠 (GUI + CLI) を固める**。
A 案の利点 (本体の挙動そのものでの試聴など) が必要な場面は、ツールから本体を起動する
形で補う (例: ループチューナの «本体で鳴らして確認» ボタン)。

### 共通ライブラリ (B 案の場合)

| 部品 | 中身 | 出どころ |
|---|---|---|
| xp3 | 読み込み (インデックス / セグメント / 展開フィルタ) + **書き込み (新規)** | 読み込み = `src/core/common/base/XP3Archive.cpp`。書き込みは旧リリーサの仕様 (zlib セグメント、重複排除、インデックス圧縮、展開プロテクト) に合わせて新規 |
| sig | 鍵生成 (RSA 1024bit / e=65537) / 署名 (SHA256 + RSA-PSS) / 検証、exe の埋め込み領域 (`XOPT_EMBED_AREA_` / `XRELEASE_SIG____`) の扱い | 検証 = `src/plugins/sigcheck`。生成・署名は libtomcrypt で新規 (旧 krkrsign と同じ書式) |
| exe | 本体 exe へのオプション埋め込み・xp3 結合・アイコン差し替え | 旧 `KrkrExecutableUnit.cpp` 相当を新規 |
| image | TLG5 / TLG6 保存・読み込み、PNG / JPEG、PSD / CLIP の読み込み | `SaveTLG5.cpp` / `SaveTLG6.cpp` ほか本体、psdparse (psdfile)、clipparse (clipfile) |
| audio | Vorbis / Opus のデコード・**エンコード (新規)**、WAV、ゲイン | 本体の `VorbisCodecDecoder` / `OpusCodecDecoder`、libvorbisenc (本体でリンク済みだが未使用)、libopus のエンコーダ |
| loop | `.sli` の読み書き、リンク / ラベル / フラグの評価 | `WaveLoopManager.cpp` (`TVP_IN_LOOP_TUNER` の名残あり) |
| analysis | 音量 / スペクトル / 母音の解析 (リップシンク用) | 本体の `getSoundLevel` / `getSoundSpectrum` / `getVowel` の処理 |
| cf | `.cf` / `.cfu` / 埋め込みオプションの読み書き | 本体の `ConfigLine.h` と旧 krkrconf の仕様 |

## ツール別の内容

### 1. ファイル破損チェックツール

- 旧 sigchk 互換: フォルダ以下を再帰的に走査し、`.sig` のあるファイルと吉里吉里の exe の署名を
  公開鍵で検証。結果は 正常 / 破損 / 未チェック。設定 (お知らせ文・公開鍵) は旧形式の ini も読む。
- 追加: 結果の JSON / TSV 出力 (CLI)、xp3 の中身の整合 (セグメントの adler32) チェック、
  「あるはずのファイルが無い」検出 (ファイル一覧 = マニフェストを署名して同梱する方式。旧ツールは
  欠落を検出できなかった)。
- エンドユーザ配布物なので、画面は単純に保つ。

### 2. ループチューナ

- `.sli` (旧形式 `LoopStart` / `LoopLength`、v2 `#2.00` の `Link { }` / `Label { }`) の完全互換。
- 既存の試作 (吉里吉里2 リポジトリの `src/tools/win32/krdevui/looptuner_new`、webui + Svelte +
  libsndfile。リンク / ラベル編集・波形・Undo・`.sli` 読み書きまで実装済み、2026-02 時点。
  未コミットの手直しあり) を土台に移植する。
- 残課題 (試作の README より): **サンプル精度のループ再生** (いまは `<audio>` 再生でループ点を
  試聴できない。Web Audio で組み直すか、ネイティブ側で鳴らす)、Smooth (約 50ms クロスフェード)
  の試聴、フラグ値パネルとラベル式 (`:[0]=1` 等) の評価、ゼロクロス検索、D&D で開く。
- CLI: `.sli` の検証 (範囲外のリンク等)・旧形式から v2 への変換・一覧出力。

### 3. xp3 ツールとリリーサ

旧 krkrrel は **xp3 の作成** (拡張子ごとの 圧縮 / 格納 / 除外、重複排除、圧縮サイズ上限、
インデックス圧縮、展開プロテクト、Ogg Vorbis のコードブック共有、`.rpf` プロファイル) と
**本体 exe への結合** (オプション埋め込み + xp3 追記 + アイコン差し替え) を 1 本で持っていた。
新しくは 2 本に分ける:

- **xp3 ツール** (全 OS) — 作成 / 一覧 / 展開 / 検証。CLI が主で、GUI は簡単なもの。
  外枠 (krkrz_android / krkrz_linux / krkrz_ios) や CI からも使う。**TODO.md の「共通の xp3 作成 CLI」は
  これ**。旧 krkrrel と同じ書式で出力し、`.rpf` も読める。展開は展開プロテクト付きのものはしない。
- **リリーサ** — xp3 の作成は上のライブラリを呼び、**本体 exe への結合**を受け持つ。
  ⚠ **吉里吉里Z の本体 exe にはオプション領域・署名領域の目印 (`XOPT_EMBED_AREA_` 等) が無く、exe の末尾に付けた xp3 も読まない** (2026-10-09 確認)。結合には本体側の対応 (目印の埋め込みと、起動時に自分の末尾の xp3 / 埋め込みオプションを読む処理) が先に要る。それまでは吉里吉里2 の exe だけが結合・埋め込み署名の対象:
  オプション埋め込み (`XOPT_EMBED_AREA_`)、`.cf` の設定、**アイコンの差し替え**、署名 (sig ライブラリ)。
  - 結合先は **Windows の exe** (PE)。アイコン差し替えも PE のリソースの書き換え。ただし処理は
    自前で PE を書き換えるので、**ツール自体は Windows 以外でも動かせる** (旧版も PE を直接書き換えていた)。
    Linux / macOS / モバイルの配布物は外枠 (krkrz_linux 等) が作るので、リリーサの結合機能は対象外。
  - 暗号化: 旧 `xp3enc.dll` (`XP3ArchiveAttractFilter_v2`) 互換の口を残す (外部の共有ライブラリを
    読み込むプラグイン方式)。DLL を読むこの部分は Windows 前提になりうる。暗号の中身は標準ツールでは持たない。

### 4. キー生成・署名ツール

- 旧 krkrsign 互換: 鍵生成 (RSA 1024bit・PEM・パスフレーズなし)、`.sig` の作成、exe への署名埋め込み。
- 追加: 鍵長の選択 (互換のため既定は 1024)、複数ファイルの一括署名、検証 (CLI)。
- ファイル破損チェックツール・リリーサと同じ sig ライブラリを使う。

### 5. 画像フォーマットコンバータ (大改造)

- 旧 krkrtpc の機能 (BMP / PNG / JPEG / PSD 入力、不透明 / 透過で別形式、TLG5 / TLG6 / PNG /
  JPEG / 分離形式出力、ltAddAlpha、完全透明部分の色の処理、mode / offs / vpag / reso タグ) を引き継ぐ。
- **PSD / CLIP 対応の強化**: 1 枚へ合成 (psdparse の `getComposite` = 調整レイヤ・レイヤー効果込み)、
  レイヤ単位の書き出し (名前・位置の情報付き)、CLIP のキャンバス合成とレイヤ書き出し。
- TLG の読み込み (旧ツールは不可)、一括変換・フォルダ監視は CLI 側で。

### 6. 音声フォーマットコンバータ (新規)

- Ogg Vorbis / Opus のエンコード・デコード (WAV ⇔ ogg / opus、ogg ⇔ opus)。品質 / ビットレート指定。
- ゲイン: Opus のヘッダ `output_gain` の設定、ReplayGain タグ (`replaygain_*_gain`) の書き込み
  (本体の `-ogg_rg` / `-opus_gain` / `setGainQueryCallback` と対応)、ラウドネス測定。
- `.sli` が付いた素材は、変換後にループ位置がずれないこと (エンコーダの先頭パディング分を補正)。
- **簡易口パク**: 音量ベースの口の開き (フレームごとの値) を出力。将来の拡張として母音
  (a/i/u/e/o) の推定 (本体の `getVowel` と同じ処理) と、Live2D 向けのパラメータ出力。
  出力形式 (JSON / CSV / 本体で読める形) は着手時に決める。

### 7. 追加候補 (標準にあるとよいもの)

| 候補 | 理由 |
|---|---|
| 吉里吉里設定 (`.cf` / `.cfu` / 埋め込みオプションの編集) | 旧 krkrconf / userconf の後継。リリーサのコンフィグ設定と同じ部品で作れる |
| xp3 の閲覧・展開 | 中身の確認とデバッグ用。**展開プロテクト付きのアーカイブは展開しない** (本体の `TVPExtractArchive` と同じ扱い) |
| TJS のバイトコード化 | 旧 compiler_script の後継。本体の TJS をライブラリとして使う |
| 動画の変換補助 | 本体が再生できる形式 (webm / mpeg1 / mp4) への変換を外部の ffmpeg で行う薄いラッパ。需要次第 |

## 進め方 (フェーズ)

| 状態 | フェーズ | 内容 |
|---|---|---|
| ✅ (Windows) | 0. 基盤 | **2026-10-09 krkrz_tools (ローカル、`10d0c36`)**。appserve を submodule で取り込み、共通の枠 `libs/app` (ToolApp = `--cli` で CLI / 無ければ画面、JobRunner = 長い処理を別スレッド + SSE で進捗、Progress、UTF-8 ⇔ パス変換)、画面の共通部品 `web/common` (フォルダ / ファイル選択)、`krt_add_tool()` (exe + 画面の埋め込み)。リモート: https://github.com/wamsoft/krkrz_tools (public、2026-10-09)。krkrz_dev には `src/tools/krkrz_tools` (submodule) として入れ、ExternalProject でビルドして `make install` で `tools/` に置く (`cmake/KrkrzTools.cmake`、デスクトップで既定 ON)。Linux / macOS のビルド確認済み (2026-10-09: Linux = ホスト直接 + **sniper SDK コンテナで GLIBC 2.30 / GLIBCXX 依存なし**、macOS = Intel、どちらも 6 本の CLI と画面を確認)。**残り: 配布物の作り方 (CPack)、Apple Silicon での確認 (install 後の ad-hoc 再署名が要るか)** |
| ✅ (Windows) | 1. 署名系 | **2026-10-09**。`krkrcheck` (破損チェック: 旧 sigchk と同じ対象規則、旧形式の Shift_JIS の ini をそのまま読める、TSV / JSON 出力) と `krkrsign` (keygen / sign / verify、exe 埋め込み署名)。確認済み: 旧ツールの鍵での署名と旧ツールの署名の検証、exe 埋め込み署名の改変検出 (オプション領域は対象外)、**本体の sigcheck プラグインでの判定の一致**。差異 1 点: 別の鍵の署名・壊れた署名は、ツールは «破損»、sigcheck は «エラー (-2)»。**残り: 欠落ファイルの検出 (署名付きファイル一覧)** |
| 一部 ✅ (Windows) | 2. xp3 ツール / リリーサ | **xp3 ツール `krkrxp3` は 2026-10-09 済み** (krkrz_tools `3b020ff`): CLI (pack / list / extract / verify) + 画面 (拡張子ごとの扱いを選んで作成、一覧・検証・展開)。旧 krkrrel と同じ書式 (クッション形式のヘッダ・zlib セグメント・重複排除・展開プロテクトと警告エントリ・インデックス圧縮)、`.rpf` の読み書き。確認済み: **本体 (krkrz64) で全ファイルを読めて中身が一致**、旧 krkrrel.exe の xp3 と exe 結合 xp3 を読める。旧版との差: 圧縮しても小さくならないファイルは圧縮しない。**残り: 暗号化 (`xp3enc.dll` 互換)、Ogg Vorbis のコードブック共有、リリーサ (処理案は決定: リソース書き換え (オプション `TEXT`/139・SDL は `BINARY`/`CONFIG.CF`、アイコン、版情報) + セキュリティ設定の文字列 + data.xp3 別置き (結合は選択肢) + `.sig` 別置き。SSOT=`src/core/doc/ReleaseEmbedding.md`。本体側の結合 xp3 の探索高速化・SDL 対応は src/core `45cbe177` で済み)** |
| 一部 ✅ (Windows) | 3. ループチューナ | **`krkrloop` 2026-10-09** (krkrz_tools `bb16525`): 画面は素の JS で作り直し (試作の Svelte は使わない)。波形 (全体表示・拡大縮小・サンプル単位)、リンク / ラベルの追加・ドラッグ移動 (ゼロクロス吸着)・編集・削除、元に戻す / やり直し、フラグ 16 個。**再生は AudioWorklet に本体 `WaveLoopManager::Decode` を移植** (サンプル単位で正確。条件・同じ From の優先順・Smooth の 50ms クロスフェード・«:» ラベルのフラグ式も本体と同じ)、リンク試聴。保存時は本体と同じ規則で読み直して確認。CLI は info / check。確認済み: Node 上でのリンクのたどり方、画面の表示・再生・拡大、保存と読み直し。**残り: 実際の曲での聴感確認、旧 LoopTuner2 にあった WAV 書き出し** |
| 一部 ✅ (Windows) | 4. 画像コンバータ | **`krkrimg` 2026-10-09** (krkrz_tools `8e8fdc9`): 入力 BMP / PNG / JPEG / TLG5 / TLG6 / PSD / CLIP、旧 krkrtpc と同じ規則 (不透明 / 透過で別形式、メイン/マスク分離の読み書き、完全透明部分の色の除去・合成、ltAddAlpha、mode / offs / vpag / reso タグ)。PSD・CLIP は psdparse / clipparse でレイヤから合成 (ブレンド・効果・調整レイヤ込み)、`layers` でレイヤ単位の書き出し (位置・文書サイズのタグ + `layers.json`)。TLG は本体コードを単体ライブラリ `libs/tlg` へ移植。確認済み: **エンコード結果が本体と 114 件すべてバイト一致**、本体が出した TLG を読める、本体で変換結果を読めて画素とタグが一致、完全透明部分の合成が旧版の計算と一致。**残り: CLIP は中身のある実データで未確認 (空のサンプルのみ)、画面は API のみ確認 (ブラウザでの表示は未確認)、非 ASCII のタグ値の扱いは本体と未照合** |
| 一部 ✅ (Windows) | 5. 音声コンバータ | **`krkraudio` 2026-10-09** (krkrz_tools `f2375cf`): WAV / Ogg Vorbis / Ogg Opus の相互変換 (品質・ビットレート・ビット数)、`.sli` の引き継ぎ (Opus の 48kHz へは位置を換算)、音量 (`--gain` = Opus はヘッダゲイン / ほかは焼き込み、`--normalize=LUFS`、Vorbis の ReplayGain タグ)、EBU R128 ラウドネス測定、口パク用の音量 (RMS / ピーク、JSON / CSV、**形式は暫定**)。確認済み: 本体で変換結果と `.sli` を開ける、長さがサンプル単位で保たれる、**先頭位置もずれない** (0.5 秒の位置のクリックが Vorbis 22050 / Opus 24000 サンプル目に戻る)。**残り: 母音の推定 (本体 `getVowel` と同じ処理)、Live2D 向けパラメータ出力、口パク出力形式の確定** |
| | 6. 追加候補 | 吉里吉里設定 / xp3 閲覧 ほか |
| | 7. ドキュメント | `doc/guide/` の旧ツールのページを置き換え、`doc/topics/tools/releaser.md` (「吉里吉里2 のものを使う」) を更新 |

各フェーズの終わりに、そのツールのガイドを書き、旧ツールとの互換確認の結果をここへ残す。

Windows 向けの標準インストーラを作る環境 (krkrz_linux と同じ形式の外枠) は別計画。

## 決めること

- [x] 構成: **B 案 + 共通ライブラリ** (2026-10-08)
- [x] リポジトリの置き場所: **独立したリポジトリ** (外枠と同じく krkrz_dev を参照する形) (2026-10-08)
- [x] レンダリング済みフォント作成: **tftSave は残し、ガイドを書き換え** (2026-10-08 対応済み)
- [x] リリーサの差し替え対象: «フォント» ではなく **アイコン** だった。xp3 部分は別ツールに分ける (上の 3.)
- [x] 独立リポジトリ: **krkrz_tools** (ツールごとの exe + `libs/` の共通ライブラリ、本体ソースは `KRKRZ_BASE` から参照)。まずローカルで作成 (2026-10-09)
- [ ] 簡易口パクの出力形式
