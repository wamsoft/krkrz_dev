# 課題一覧 (索引)

krkrz_dev 全体の未対応課題をここに集約する。**詳細な SSOT が別にあるものはリンクのみ**に
留め、内容を二重管理しない。

| 領域 | 詳細 SSOT |
|---|---|
| バージョン番号の扱い | [src/core/doc/Versioning.md](src/core/doc/Versioning.md) |
| 画面転送コスト (計測・読み方) | [src/core/doc/ScreenTransfer.md](src/core/doc/ScreenTransfer.md) |
| Elements (レイアウト/ダイアログ) の要修正 | [TODO-elements.md](TODO-elements.md) |
| デモ整備 | [data/ROADMAP.md](data/ROADMAP.md) |
| Window のサイズ/位置/ズーム/ビューポート仕様 | [src/core/doc/WindowGeometry.md](src/core/doc/WindowGeometry.md) |
| Layer / Bitmap / ImageFunction の統合 | [src/core/doc/ImageBufferUnification.md](src/core/doc/ImageBufferUnification.md) |
| フォントエンジン (可変軸・glyphware 統合) | [src/core/doc/FontEngine.md](src/core/doc/FontEngine.md) |
| WINVER モダン化 | [src/core/doc/ModernizationRoadmap.md](src/core/doc/ModernizationRoadmap.md) |
| 動画 (Media Foundation 移行) | [src/core/doc/MovieMFMigration.md](src/core/doc/MovieMFMigration.md) |
| リファレンスとコードの差分 | [doc/_missing.md](doc/_missing.md) (生成物。現在 0 件) |
| ✅ Claude Code スキルの配布形 (install.sh) | [tools/skills/TODO-skills.md](tools/skills/TODO-skills.md) (切れリンク 0 件に解消済み) |

対応したら項目に ✅ と対応コミットを書き、**消さずに残す** (再発防止の記録)。
完了したものは末尾の「完了 (記録として残す)」へ移す。

## 現況 (2026-09-04 時点)

| 区分 | 件数 | 中身 |
|---|---|---|
| 予定・未着手 | 13 | Elements/UI 2 (高 1) / エンジン基盤 8 / ビルド・運用 3 |
| 将来課題 | 9 | 着手時期未定。優先は WaveSoundBuffer 3D 定位 (中〜高) |
| 未修正の既知バグ | 2 | いずれもレイヤ合成系。回避規約で運用中 |
| 低優先・保留 | 9 | 単発の小さいもの。着手順は問わない |
| デモ整備 | 10 + 1 | 未着手デモは多くが資材待ち |

**いま効いている焦点は Elements / UI の 1 件** (優先度 高、ホスト案件の
画面が実際に困っている):

1. **画面データ側で UI を完結させる (不足 4 点)** — 複数のホスト案件が
   それぞれ独自の UI フレームワークを書き始めているのを止めるための整備

> 「**overlay の出力先をホストのレイヤへ**」は 2026-09-01 に対応
> (`ElementsPanel`)。overlay が常に最前面でレイヤツリーの外にいるという制約を
> 外したので、テキストを出す画面 (メッセージ窓 / バックログ) も elements で
> 組める土台ができた。z 順・`[trans]`・`piledCopy`・入力の帰属はレイヤの
> 仕組みに従う。

> 「**ホストの描画中に文字だけ出ない**」は 2026-09-01 に解決 (`src/core`
> 3310a2d0)。条件は「ホストの描画中」ではなく **実行中にテーマの書体の並びを
> 入れ直すこと**で、theme が families を string_view で所有せずに持つのに
> engine 側が実体を static な 1 本で使い回していたのが原因だった。

> 同じホスト案件から出ていた `input_box` の 2 件 (フォーカス / 最大長) は
> 2026-09-02 に解決 (elements `de989d18`)。
>
> **2026-09-04: TJS クラス `Dialog` を `ElementsDialog` へ改名** (ゲーム側 TJS の
> クラス名と実際に衝突したため。互換エイリアスなし)。あわせて `ElementsPanel` と
> API 語彙を統一 (パネルの `open*`→`show*` / `focusById`→`focus` /
> `activateById`→`activate`、ElementsDialog に `activate(id)` 追加)。
> 利用側は次回更新時に追従する。

---

## 予定・未着手

### Elements / UI (ホスト案件に直結)

| 優先 | 課題 | 内容 |
|---|---|---|
| 高 | Elements: 画面データ側で UI を完結させる | 複数のホスト案件がそれぞれ独自の UI フレームワークを書き始めているため、**UI の処理は画面データ側 (elements_modal + 画面 JSON) で完結させ、ホストは「呼ぶ / 値を供給する / アクションを実行する」だけ**にする方針へ。 実測した不足は 4 点 (画面をまたぐ変数 / 動的画像の実行時差替 / 画面契約 / 標準ロールの語彙) で、いずれも elements 側の作業。 詳細 = [TODO-elements.md](TODO-elements.md) §7 |
| 低 | Elements の観測・操作 API を TJS へ公開 (残り) | **変数系は 2026-08-29 に公開済み** (`ElementsDialog.getVar` / `listVars` / `onVar` / `watchVars` = elements_modal の `get_var` / `list_vars` / `set_var_watcher` に対応。src/core `fcae740b`)。 残りは **navigator の `push` / `pop` / `replace` / `stack`** と `languages`。 要素を名指しで動かす instance 版は公開済み (`ElementsDialog.focus(id)` = 2026-09-02 / `activate(id)` = 2026-09-04。検証用の `Agent.dialogFocus` / `dialogClick` は従来どおり)。 用途は検証ツールから「この画面へ飛ぶ」を実装すること。 当たり判定やフォーカスナビの確認は実入力を流す API でないと意味が無い点に注意 |
| ✅ | Elements: `input_box` にプログラム的フォーカスが効かない | **2026-09-02 に解決** (elements `de989d18`: `descend_focus_first` — composite 包みの内側へフォーカス連鎖を用意)。`initial_focus` / `focus_by_id` / `ElementsDialog.focus(id)` で編集フォーカス (キャレット + text 受理) になる。詳細 = [TODO-elements.md](TODO-elements.md) §3 |
| ✅ | Elements: `input_box` の最大長と値の差し替え口が無い | **2026-09-02 に解決** (elements `de989d18`): `"max_chars"` (別名 `"maxlength"`、codepoint 単位、0/省略=無制限) を追加。既定値 (`"text"`/`"value"`) 入りは build 時全選択なので initial_focus からそのまま打つと置き換わる (差し替え口の代替)。詳細 = [TODO-elements.md](TODO-elements.md) §5-8 |

### エンジン基盤

| 優先 | 課題 | 内容 |
|---|---|---|
| 中 | Layer / Bitmap / ImageFunction の統合 | ImageFunction の API 二重化と、プラグインが Bitmap を扱えない問題 (Layer 参照 26 ファイル) の再整理。**方針決定済 = P1 (tp_stub 共通アクセス口) → P2 (Bitmap へメソッド追加・ImageFunction は shim 化) → P3 (プラグイン対応) → P4 で共通基底 `ImageBuffer` の要否を判断**。B案はプロトタイプ実測済み (パッチ同梱)。着手は後日。SSOT = [ImageBufferUnification.md](src/core/doc/ImageBufferUnification.md) |
| 中 | DrawDevice overlay 描画口の汎用開放 | `PostRenderCallback` の tp_stub 公開 + WINVER 対応 (小) / dialog renderer の painter リスト化 (大) |
| 中 | Emote/Motion リソースマネージャの共有 (再読込の削減) | `data/system/AffineSourceMotion.tjs` の `SimpleEmotePlayer` はプレイヤー生成のたびに `MotionResourceManager` を new しており、リソースキャッシュ (`Motion.ResourceManager`、既定 20MB、`motionCacheSize` で可変) が効かず、立ち絵 psb (数十 MB) を表示/アクションのたびにフル再読込している。**アクション毎のカクつきと、メモリ枯渇 (特に 32-bit) を招く**。ウィンドウ単位で 1 つの ResourceManager を共有すれば解消するが、単純な共有化 (window に持たせて addRef/共有) を試すと **emoteplayer プラグイン内部 (`V2Unlink`) が AV で即死**した — 複数 `EmotePlayer` が同一 ResourceManager を参照する構成をプラグインが想定していない疑い。**要調査**: (1) `Motion.ResourceManager` / `EmotePlayer` の参照所有モデル (unload が他プレイヤーの参照中リソースを解放していないか)、(2) 共有可能にするためのプラグイン側 IF、(3) 併せて `SwitchEmotePlayer` の base 別プレイヤーも同一 psb を二重ロードしていないか。回避として `motionCacheSize` 拡大 + 32-bit の pool 縮小 + LAA で当座の枯渇は解消済み (別項)。実機再現は E-mote 立ち絵のアクションが連続する場面 |
| 中 | 固定長パスバッファ (`MAX_PATH`) の全体点検 | `common/utils/DebugIntf.cpp:533` に `tjs_char filename[MAX_PATH]` へ `Application->ExePath()` を長さ検査なしで `TJS_strcpy` している箇所がある (`TVPTJS2StartDump`)。Windows のパスは `MAX_PATH` を超えうるので、**同種の固定長バッファ + 無検査コピーが他にどれだけあるかを全体で洗い出し**、`tjs_string` / `ttstr` 化するか長さチェックを入れる。2026-08-19 の設定ファイル調査中に発見 (この件自体は今回の変更とは無関係の既存コード) |
| 低 | プラグイン横断のリソース消費収集 IF | 命名規約 `getResourceUsage()` の策定から。ライセンス収集 IF と同じ枠組み |
| 低 | 縦組みの組版拡張 (ルビ / 縦中横 / 圏点 / 割注 / 字取り・段組・傍線) | `Layer.drawVerticalTextArea` の対応範囲は本文の組版のみ。ルビ等は行の中へ**入れ子の組版ボックス**を埋める話で、`LineItem` の拡張と入力マークアップ (本文文字列 1 本では表現できない) の設計がセットになる。段組は「入りきらない列を次へ渡す継続位置」、傍線は縦組み固有の位置決めが要る。必要になった時点で層から決める。SSOT = [FontEngine.md](src/core/doc/FontEngine.md) 「縦組み (drawVerticalTextArea) の未対応」 |
| 低 | プラグイン向けログレベル個別 IF | `TVPLogMsg` を tp_stub に収録するだけ。important = WARNING は維持 |
| 低 | フォントエンジンの未対応 (計画) 4 件 | ①収録範囲を使った**言語別フォールバックの自動選択** (Elements は宣言式の `font_languages` で対応済みだが `Layer.drawText` / `Font.face` 側は未対応) ②圧縮 cmap/bitset による包含判定の最適化 ③`TVPGetAllFontList` へメタデータ名を合流 (設定 UI のフォント一覧反映) ④システムフォント全列挙 (`allowSystem`) の検索統合。SSOT = [FontEngine.md](src/core/doc/FontEngine.md) 「未対応 (計画)」 |

### ビルド・運用

| 優先 | 課題 | 内容 |
|---|---|---|
| 中 | krkrlive2d のドライバソースを版固定取得へ | ドライバ側 CMake がローカルパス (`LIVE2DLIB_FOLDER` / `CUBISM_SDK` 等) を直接参照する作りで、そのフォルダの版がずれると **umbrella の configure ごと失敗する** (実例: ドライバが `find_package(minizip)` を要求する版になり、本体 vcpkg マニフェストに minizip が無くて configure 不能)。 版を固定して fetch する形へ直すまで、`CMakeLists.txt` の `CUBISM_SDK` ブロックをコメントアウトしてビルド対象から外してある (2edc380)。 直したら除外を戻す |
| 中 | リリースのバージョン運用を確定する | 番号の供給元は一本化済み ([Versioning.md](src/core/doc/Versioning.md))。`v2.0.0` は core (krkrz.git) / umbrella (master) 双方に打鍵済み。残りは **再パッケージ時のタグ規則の確定**: core 無変更でプラグインだけ更新する場合に `v2.0.0-2` 等のサフィックスを使うか。既存タグは `1.4.0` (v 無し) と `v1.0.0` (v 有り) が混在しているので、以後は `v` 付きで統一する |
| 中 | 全生成器の Perl 撤去 → Python 統一 | 残 = syntax 後処理 5 本 と `gengl.pl` (7519 行 = 最大の山)。バイト一致の差分ゲート方式。他作業と独立に実施可 |

## 将来課題

| 優先 | 課題 | 内容 |
|---|---|---|
| 中〜高 | WaveSoundBuffer 3D 定位 API (F-1) | miniaudio の spatializer で全バリアント横断の 3D 定位 API を新設 |
| 中 | Elements を WINVER のネイティブ経路へ | 中立イベント型の導入 / manager のテキスト入力・ウィンドウ取得の seam 化 / WndProc → manager 転送 + IME / OGLDrawDevice への renderer 配線 / elements_gallery の実機確認。[data/ROADMAP.md](data/ROADMAP.md) 参照 |
| 中 | フォントラスタライザを glyphware へ一本化 | 現状の既定は WINVER=GDI / 非 WINVER=旧 FreeType で、glyphware (`rasterizer=2`) はどちらでも既定ではない。可変軸・シェイピング・BiDi・カラー絵文字・フォールバックが既定で効くようにするには一本化が本筋だが、**全案件の文字描画の見た目が変わりうる**ためパリティ検証が前提。→ [FontEngine.md](src/core/doc/FontEngine.md) |
| 中 | SDL 版に `-about` のダイアログが無い | バージョン情報ダイアログは WINVER だけの実装 (`TVPCheckAbout()` → `TVPShowVersionForm()` = Win32 `DialogBox`)。SDL3 は `-about` を処理しておらず、`System.showVersion()` も WINVER のみ。**表示する文字列は全バリアント共通で用意済み** (`TVPGetAboutString()` = バージョン行 + LICENSE + 収録一覧 + 環境情報。SSOT = [LicenseSystem.md](src/core/doc/LicenseSystem.md)) なので、残るのは表示手段だけ。素直には `-userconf` と同じくゲームウィンドウ生成前の独立 SDL_Window + Elements overlay だが、**gamescope (Steam Deck) はセカンダリウィンドウを出せない**ので、その環境での代替 (標準出力へ落とす等) も併せて決める必要がある。現状の代替手段 = `-license` (標準出力) と `System.licenseText` |
| 中 | SDL ビルドの SEH 捕捉 | ゼロ除算・アクセス違反でログを残さず即死する。WINVER は translator + minidump あり |
| 低 | WINVER モダン化の残 | F-3 (入力)、HW mixer の直描画 |
| 低 | WINVER に繁体字のメッセージ文字列が無い | `messages.csv` の `cht` 列は SDL3/LIB へ `resource/messages-cht.json` として届くが、WINVER の PE 文字列テーブル (`win32/vcproj/string_table_*.rc`) は jp / en / chs の 3 種のみ。zh-Hant UI では PE リソースの言語解決でフォールバックする。`gen_messages.py` に `string_table_cht.rc` の出力を足し、`tvpwin32.rc` の Chinese (Traditional) ブロックへ `#include` すれば埋まる (設定ダイアログの文字列は既に繁体字あり)。→ `src/core/common/msg/text/README.md` |
| 低 | macOS (Retina) の point / pixel の使い分け | `SDL3WindowForm::GetSurfaceSize` が `SDL_GetWindowSize` (macOS では **point**) を使っているため、Retina では描画解像度が半分になる可能性がある。`SDL_GetWindowSizeInPixels` との使い分けを整理する必要あり。**未検証 (macOS 実機確認が前提)**。サイズ API の単位定義とあわせて判断する → [WindowGeometry.md](src/core/doc/WindowGeometry.md) §8 |
| 低 | generic フラグの 3 種区別 | `kirikiriz_generic` が導入当時「CS (コンシューマ) 版」の意味だったため、案件スクリプトは generic = プラグイン静的リンク前提で分岐している。PC の SDL ビルドは CS でも WINVER でもない第 3 の形態なのに区別する手段が無い。案件側スクリプトにも影響するため改定は慎重に |

## 未修正の既知バグ (回避策で運用中)

いずれもレイヤ合成系。回避規約を敷いて運用しているので実害は出ていないが、
**エンジン側のバグの可能性が高く未調査**。直したら回避規約を外せる。

| 課題 | 症状と回避 |
|---|---|
| primary レイヤ直描き / primary 直下の非全画面レイヤ | primary へ直接 `drawText` するとグリフが崩れ、primary 直下の半透明 `ltAlpha` レイヤが白帯化する。`Layer.type` を明示設定した後の `drawText` も崩れる。CPU フラグ (`-cpuavx2=no` / `-cpusimd=no`) で症状が変わるが SIMD パリティテストは全合格なので、レイヤ種別ごとの関数選択・dispatch 経路が疑わしい。DrawDevice 非依存。**回避**: 描画は必ず「primary の全画面 opaque 子レイヤ (demolib の `base`/`stage`)」以下で行う。デモ全体に適用済み (`data/demolib/readme.txt` / `data/README.md` に注意書き) |
| 非全画面の入れ子レイヤの `Layer.type` ブレンド | primary→stage→bg→sp のような**非全画面の孫レイヤ**に `Layer.type` でブレンドを設定すると、多くの型 (`ltOpaque` / `ltAlpha` / `ltMultiplicative` / `ltDodge` / `ltDarken` / `ltLighten`) でそのセルが真っ黒になる (`ltAdditive` / `ltSubtractive` / `ltScreen` は正常)。上と同じ合成器系統の別 facet の可能性。**回避**: ブレンド比較はレイヤツリー合成ではなく `Layer.operateRect` (CPU 合成) を使う。`layer_basic` デモはこの方式 |

## 低優先・保留

- MF SourceReader の WINVER YUV 対応
- web REPL の modal 転送 / 重複プラグインの削除
- Elements WINVER 展開のクリーンアップ
- ゲームパッド実機での最終確認
- glyphware: ThorVG 系のバイト共有最適化 / `fonts.json` スキーマ拡張 (✅ richtext 統合は完了 — 本体 `FontServiceIntf` をバックエンド注入し、richtext から thorvg 依存も除去)
- krkreffekseer の macOS (GLES3) 実機確認 (⏸ ビルド対応済)
- tjsDataPack のライセンス収集 IF 対応 (保留)
- リップシンクの母音判定精度向上とデモ
- Elements 遷移エフェクト Phase C (GPU present 拡張・optional)

## デモ整備

[data/ROADMAP.md](data/ROADMAP.md) 参照。未着手デモは
`sound` / `sound_3d` / `video` / `storage` / `ui_flow` /
`data_parse` / `net_demo` / `movie_alpha` / `archive_demo` / `richtext_demo` の 10 本
(多くは資材待ち。資材一覧は [data/DEMO-ASSETS.md](data/DEMO-ASSETS.md))。
資材不要のデモは全て実装済み (残りは資材待ち)。
ほかに krkrz_web のランチャ起動トークン (スラッシュ入り) 対応が残っている。
doc のデモ一覧ページ ([doc/demos.md](doc/demos.md)) と wasm 再ビルド・再ステージングは
✅ 2026-08-16 に完了 (デモを増やしたら krkrz_web を再ビルドして
`tools/stage_docs.py` で `doc/_assets/demo` を差し替えること)。

---

## 完了 (記録として残す)

対応済みの項目は再発防止の記録として残す。新しいものが上。

| 優先 | 課題 | 内容 |
|---|---|---|
| 中 | ✅ バリアブルフォント (可変軸) の TJS 露出 (P0〜P5) | **全実装済** (P0〜P4 = src/core b48ba3bc 2026-08-23、P5 = src/core 83482f08 2026-08-24)。`Font.weight` / `Font.variations` / `Font.defaultUseVarStyle` / `Font.getVarAxes` / `getFontInfo` の axes・namedInstances / `fonts.json` の `axes`・`instance` 宣言 / `#tag=val` サフィックス表記 (Font.face トークン・Elements JSON "font"・gw ブリッジキーで一様)。glyphware 経路 (`rasterizer=2` の drawText + drawShapedText 系 + Elements) のみ。SSOT = [FontEngine.md](src/core/doc/FontEngine.md) 「バリアブルフォント (可変軸) の全体展開」 |
| ✅ | Window ジオメトリ仕様の統一 **P1** | DestRect 算出を `TVPCalcViewportDestRect` 共通計算へ + viewport の配置 API を全バリアント公開 + WINVER 入力座標の DestRect オフセット対応。等価変換で**挙動不変を実測確認済**。SSOT = [WindowGeometry.md](src/core/doc/WindowGeometry.md) |
| ✅ | 同 **P2** | WINVER `setZoom` が `SetInnerSize(layer×zoom)` を行うようになり (旧 WIN / SDL と同じ意味論)、既定 align も両バリアント中央に統一。倍率・入力座標・フルスクリーン往復・KAG3 相当の呼び方を実測確認済 |
| ✅ | 同 **P3** (基準面を inner へ統一) | SDL の `innerWidth` 実値化 (+ min/max getter が 0 固定だったのを修正) / WINVER の min/max を inner 基準へ / WINVER `borderStyle` 変更を inner 維持へ / SDL `displayDensity` を実 DPI へ / WINVER `SetClientSize` を `AdjustWindowRectExForDpi` へ / `frameWidth`・`frameHeight` 追加。**サイズ挙動マトリクスは生成直後を除き全項目で両バリアント一致**。残る差 = キャプション付きウィンドウの Windows 由来の最小幅 (内側 ~116 論理px 未満) のみ、既知の差として記載 |
| ✅ | 同 **P4** (DPI ポリシー = inner の物理ピクセルサイズ維持) | WINVER の `WM_DPICHANGED` を「client 物理サイズ維持 + 位置だけ提案矩形へ」に変更 / SDL は `TVPSDLSetWindowPositionKeepingSize()` を新設してプログラム移動を全て経由させた。200%⇔100% 往復で inner 320x240 維持・枠だけ 26x71⇔16x39 を両バリアントで実測確認 |
| ✅ | 同 **P5** (余白塗りを全バリアントへ) | `viewportBgColor` / `setViewportWallpaper` / `clearViewportWallpaper` を全バリアントで有効化。**`iTVPDrawDevice` には載せず `iTVPViewportBackgroundHost` を新設し、対応デバイスが TJS プロパティ `viewportBackgroundHost` でポインタを公開する実行時検出方式** (動画の `videoPresenterHost` と同じ規約) にしたので、**`iTVPDrawDevice` の vtable は不変 = プラグインの再ビルド不要**。`BasicDrawDevice` に D3D11 実装 (背景色クリア + 壁紙クアッド) を追加、`OGLDrawDevice` の既存実装も開放 |
| ✅ | Steam Deck でオンスクリーンキーボードが意図せず表示される | 原因確定 (2026-08-24 実機計測): Deck (gamescope/Xwayland) では `driver=x11 / screenKB=1 / hasKB=1`。①SDL の `AutoShowingScreenKeyboard()` は環境変数 `SteamDeck=1` のとき物理キーボードの有無に関係なく無条件 true で、`SDL_StartTextInput` が即 `steam://open/keyboard` deeplink で Steam OSK を出す。②Xwayland は常にコアキーボードを提供するため `SDL_HasKeyboard()` は物理キーボード検出に使えず、旧来の「hasKB=true ならベースライン有効化して SDL が抑止してくれる」前提が崩れていた。修正 = Deck を `SDL_GetHintBoolean("SteamDeck")` で検出し、(a) `TVPUpdateBaselineTextInput` はベースライン無効化 + **focus レイヤの `imeMode != imDisable` の間だけ StartTextInput** (`SetImeMode`/`ResetImeMode` を virtual 化して SDL3WindowForm へ配線。ゲーム側入力欄は `Layer.imeMode` で OSK を呼べる)、(b) Elements は `HostHasPhysicalKeyboard()`=false で focus 駆動へ載せ、`HostScreenKeyboardIsFloating()` 新設で内蔵仮想キーボードではなく **OS 側 (Steam OSK) を使う** (NX/PS5 のブロッキングアプレット環境のみ内蔵 VK)。実機確認済み: 起動時 OSK 無し / ベース入力欄 focus で start / Elements 欄で内蔵 VK 非表示。既知の割り切り = Deck に物理キーボードを繋いでも「無し」扱い (SDL 自身と同じ)。 |
| ✅ | System.inform / confirm / inputString の SDL overlay 化 | gamescope (Steam Deck) がセカンダリウィンドウを表示できないため、SDL 版の 3 API をゲームウィンドウ上の Elements overlay モーダルへ切替 (2026-08-24)。`DialogIntf.cpp` に `TVPInformElements` / `TVPConfirmElements` を新設、`TVPInputStringElements` は独立窓→overlay へ変更。本文は label 行の縦積み (`SplitBodyLines`。text_box / text_area は vtile との高さ折衝で末尾行が切れるため不採用)。window/DrawDevice 未初期化や overlay 起動失敗時は従来の `SDL_ShowMessageBox` へフォールバック。WINVER はネイティブ維持。**REPL 駆動中は 3 API とも従来どおり抑止/チャネル迂回される** (エージェント検証は ElementsDialog.showModalJson で同一スケルトンを確認済み。最終挙動の目視は REPL 無し起動で行う) |
| ✅ | onTextInput イベント系の新設 (onKeyPress は WINVER 互換のみ) | 文字入力を文字列単位の `Window.onTextInput(text)` へ一斉移行 (2026-08-24)。SDL は TEXT_INPUT 1 イベント = 1 コール (IME 確定文字列はまとまる)、WINVER は WM_CHAR をサロゲート合成して併発 (制御文字は SDL パリティのため除外)。SDL では `Window.onKeyPress` は発火しない (WINVER のみ互換発火)。Layer 系へは UTF-16 分解して従来 `FireKeyPress` (`Layer.onKeyPress`) で互換配送 = **iTVPDrawDevice / LayerTreeOwner / iTVPLayerManager の vtable 不変・プラグイン再ビルド不要**。`Layer.onTextInput` の新設は DrawDevice ABI 拡張時の課題として保留。`Agent.text` は実入力と同じ経路への注入に変更 (Elements 消費→ゲーム素通しまで一致、SDL/WINVER 両実装)。demolib + softkey_ime デモを onTextInput ベースへ再構築、doc/reference/Window.md に onTextInput 追記。実測: SDL/WINVER 両方で日本語・絵文字 (サロゲートペア)・BS/Enter (onKeyDown 受け) を確認 |
| ✅ | ブロッキング overlay モーダルのクラッシュ 2 種 (再入 + handler UAF) | System.inputString overlay の実機テストで発覚・修正 (2026-08-24、ElementsDialogManager.cpp)。①**PaintOverlay 再入**: OnAction コールバック (session->update() 中に発火) からネストモーダルの pump が回ると PaintOverlay が再帰し、 ネスト側の teardown (instances erase) が外側 range-for のイテレータを無効化して AV → 全フェーズを index ベース + 生存確認化し、`Instance::in_update` ガードで update 再入とスタック上インスタンスの teardown を抑止。②**handler use-after-free**: finish → teardown は次フレームへ遅延されるが pump は先に脱出するため、 スタック上の短命 handler 解放後に `OnClosed` が飛んで AV → `FlushPendingTeardowns()` 新設、 pump 脱出直後 (SDL/WINVER 両ランナー) に同期破棄。 ③付随修正: WINVER の WM_CHAR 由来制御文字 (BS=0x08 等) を `ForwardKeyPress` がテキストとして input_box に挿入し「BS で消えない」症状 → 制御文字はテキスト転送しない (キーイベント側で処理済み)。 ④**paint 中 OnAction からのブロッキングモーダルが描画不能で固まる**: PaintOverlay → session->update() 内から発火した button click (Deck の touch 経由等) のコールバックで System.inputString を呼ぶと、 nested pump が window update の再入禁止 (`TVPDeliverWindowUpdateEvents` のグローバルフラグ) に阻まれ一切描画されないまま入力だけブロック (Deck 実機で再現、pump 診断ログで確定) → **bridge の OnAction 配送を manager の `DispatchAction` に一本化し、 paint 深度 > 0 のときはキューに積んで continuous イベントフック (window update の外) から配送** (`QueueOrDispatchAction` / `DrainPendingActions`。 入力経路発火の action は従来どおり即時)。 ⑤付随: REPL 中の System.inform/confirm/inputString は「モーダル応答チャネル (-replfile) があるときだけ非ブロッキング迂回、 無い REPL (-replweb / console) は実 UI へフォールスルー」に変更 (generic + win32 の SystemImpl。 Deck の replweb 運用でダイアログが出るように)。 いずれも実機 (SDL Windows/WINVER/Deck) で修正確認済み |

### 他項目へ統合したもの

| 優先 | 課題 | 内容 |
|---|---|---|
| — | ~~レイヤ系プラグインの Bitmap 両対応~~ | 上の **Layer / Bitmap / ImageFunction の統合** に統合。同じ作業の別名で、統合ロードマップの **P3 (プラグイン対応)** がこれにあたる。事前調査の内容 (Layer 参照 26 ファイル、詰まりは `hasImage` の有無 / class dispatch 経路 / Layer 専用メンバの使用の 3 種類) は [ImageBufferUnification.md](src/core/doc/ImageBufferUnification.md) 「課題 B」に取り込み済み。プラグイン単体で先に直すより、P1 (tp_stub 共通アクセス口) を入れてからの方が 26 本の分岐がほぼ解ける |
| — | ~~WINVER の `Window.setZoom` が事実上効かない~~ | 上の **P2** に統合。調査の結果、旧来の契約は「`setZoom` は倍率を覚えるだけで `inner == layer×zoom` はスクリプトが維持する」(KAG3 `YesNoDialog.tjs:51-59` が実例) であり、この不変条件が守られていれば現 WINVER も 1:1 で正しく出る。差が出るのは `setInnerSize` を伴わず `setZoom` だけ呼んだ場合。詳細 = [WindowGeometry.md](src/core/doc/WindowGeometry.md) §3 |

## 最近クローズしたもの

- ✅ Elements の言語連動フォント置換 `font_languages` (elements `56d1318d`〜 /
  src/core `c6444966`)
  多言語 UI で表示言語に応じて JP/TC/SC 等のフォントを自動で差し替える
  (共有コードポイントの漢字を正しい地域字形で描画)。宣言は画面 JSON /
  app.jsonc top-level / `ElementsDialog.fontLanguages` の 3 系統、widget 明示
  `"locale"` で個別固定可、`#tag=val` 軸サフィックス温存。実装は elements
  フォント層に一元化 (krkrz は submodule bump + TJS プロパティのみ)。
  設計 SSOT = [src/core/doc/FontEngine.md](src/core/doc/FontEngine.md)
  「言語連動フォント置換」節、ガイド = [doc/guide/ElementsDialog.md](doc/guide/ElementsDialog.md)。
  既知の制限 (text_area 非追従 / グローバル表) も同節に記載
- ✅ 設定ファイル (`.cf` / `.cfu`) の行正規化と、デスクトップ SDL の探索規約を
  WINVER へ統一 (src/core `43a0a827`)
  行末の改行が値に混入していた (win32 = `fgets` で LF が残る / generic =
  `getline` で CRLF の CR が残る)。素の値の比較が静かに失敗し、値省略行は
  参照不能だった。`common/base/ConfigLine.h` で解釈直前に改行・前後の空白・BOM を
  落とすようにした。あわせて generic のデスクトップを WINVER と同じ規約にし
  (`<exe名>.cfu` > `<exe名>.cf` > `config.cf` > 埋め込み)、無効化されていた `.cfu`
  読み込みを有効化 (sdl3 の `-userconf` は書いていたのに誰も読んでいなかった)。
  sdl3 の `ExePath` が固定文字列 `"krkrz.exe"` だったのも実パス解決に修正。
  非デスクトップ (Android/iOS/wasm/組込み機) は挙動を変えていない。
  仕様 = [doc/guide/CommandLine.md](doc/guide/CommandLine.md)
- ✅ `System.screenWidth` / `screenHeight` の仕様を WINVER / SDL で揃えた
  SDL/generic は常にプライマリディスプレイを返していて、リファレンスの記述
  「メインウィンドウのあるディスプレイを対象」と食い違っていた。
  **メインウィンドウのあるディスプレイ → `-display` 指定 → プライマリ** の順で
  解決する規則に統一 (SDL = `SDL3Application::BaseDisplayID()` /
  WINVER = `TVPGetBaseMonitorInfo()`。WINVER は `desktop*` 系も同じ経路)。
  リファレンスにも `-display` 時の扱いを追記
- ✅ 起動するディスプレイの指定 `-display` (src/core `94c67f6b` / umbrella `35a9353`)
  マルチディスプレイ環境で最初に表示するモニタを番号 (1 origin) / モニタ名の
  部分一致 / `primary` で指定できる (`-display=list` で一覧をログ出力)。
  WINVER / SDL3 両対応。テスト時にメインディスプレイを占有しないための口。
  仕様 = [doc/guide/CommandLine.md](doc/guide/CommandLine.md)。
  ※落とし穴: WINVER は `TTVPWindowForm` コンストラクタ**途中**で `SetWindowPos`
  すると WM_MOVE/WM_SIZE ハンドラが未初期化の `TJSNativeInstance` を触って即死する

- ✅ 「SDL3 ビルド限定」表記の全体精査 (src/core `a9bf9de4` / umbrella 側 doc)
  memoverlay / padoverlay は「ビルド限定」ではなく**描画デバイス依存**だった
  (OGL 系 DrawDevice と SDLDrawDevice が描く / WINVER 既定の D3D11 は描かない。
  WINVER でも OGL へ切り替えれば出る)。 併せて PadOverlayGL の WINVER stub を
  撤去し、WINVER でも実パッドの名前・ボタン・軸が出るようにした。
  CommandLine.md / System リファレンス / MemoryGuide / DrawStats / PadOverlay /
  REPL ヘルプ文言 / 各 SystemImpl のコメントを修正。
  ※ `-drawdevice` `-renderer` は実装が sdl3/ のみなので「SDL3 限定」のまま、
  `-drawstatslog` は generic 実装なので「SDL3・LIB」に補正。
- ✅ WINVER 本画面転送の差分更新化 (src/core `5597496d`)
  `BasicDrawDevice` がダーティ矩形単位で `UpdateSubresource` するようになり、
  静止画面 421.9MB/秒 → 1.8MB/秒 (転送率 5.0% → 0.0%)、動きのある画面でも
  -87〜-98%。詳細 = [src/core/doc/D3D11Migration.md](src/core/doc/D3D11Migration.md) 追補節

- ✅ WINVER のモーダルウィンドウがマウス操作を受け付けない (src/core `49fdd011`)
  D3D9 → D3D11 移行の回帰。vblank 待ちをメインスレッドから VSync タイミング
  スレッドへ移動。詳細 = [src/core/doc/D3D11Migration.md](src/core/doc/D3D11Migration.md) 追補節
- ✅ SDL / generic の `Window.showModal` 実装 + generic で `onClick` が発火しない欠落
  (src/core `f6aa5900`) 詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ モーダル表示中にタイマーが完全停止する / wake 投函失敗でタイマーが永久停止する
  / WINVER の Agent 入力がモーダルへ届かない (src/core `90698ee1`)
  詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ Elements: overlay の出力先をホストのレイヤへ向けられるようにする
  (src/core `e2f05dbc` / `06085168` / `fbd51004` / `029c9413`)
  `ElementsPanel` を追加 (overlay とは別枠。manager のインスタンス列に入らない
  ので入力インターセプトのゲートもウィンドウクローズ抑止もダイアログ列挙にも
  影響しない)。`render_to_buffer` の書き込み先をレイヤのビットマップにするだけで
  z 順・トランジション・スクリーンショット・入力の帰属が一度に片付いた。
  入力の座標変換は不要 (surface を 0,0 にすると view local = レイヤ local)。
  **副産物として、overlay の提示が straight alpha でアルファを二重に掛けていた
  のを直した** (半透明の画素だけが薄く出ていた)。詳細 =
  [TODO-elements.md](TODO-elements.md) §8 / `src/core/doc/ElementsDialog.md`
- ✅ Elements: 同じチャンネルの `animate` が連ならない (elements `8f5f0145` /
  src/core `58cc0a81`) `delay` 中の束縛が自分の `from` を書き続けて先行の動きを
  打ち消していた。チャンネルごとに「いま支配している束縛 1 本」だけを反映する
  ようにして、`"delay"` 昇順に並べるだけで折れ線になるようにした。1 本しか無い
  チャンネルと別チャンネルの同時掛けは挙動不変。詳細 =
  [TODO-elements.md](TODO-elements.md) §9
- ✅ Elements: テーマの書体の並びを差し替えると以後のテキストが描かれなくなる
  (src/core `3310a2d0`) theme の `font_descr` は families を string_view で
  所有せずに持つ仕様なのに、engine 側が実体を static な `std::string` 1 本で
  使い回していたため、差し替えのたびに旧バッファが解放されて font_descr の
  コピーが宙を指していた。`clear()` はバッファを解放しないので「並びが長く
  なって再確保が起きた回でだけ壊れる」未定義動作で、ビルドによって出方が
  変わり不可解な症状に見えていた。**`font` を明示した widget だけ無事なら
  theme の書体の並びを疑う**。詳細 = [TODO-elements.md](TODO-elements.md) §6
- ✅ Elements 画面資材そのまま移植の拡張要望 7 件 (elements `365bc122` / `a2a36319`
  / `06c39b99` / `bd7b607d` / src/core `fcae740b` / `7352157f`)
  変数の読出と変化通知 (`ElementsDialog.getVar` / `listVars` / `onVar` / `watchVars`)、
  行テンプレート方式の一覧 `list`、スクロールバー `atlas_scrollbar`、つまみの
  9-slice と `at_var_offset`、named action の通知形をドキュメント化。OS フォントの
  family→ファイル解決 (5-7) は engine 側の課題として見送り。
  詳細 = [TODO-elements.md](TODO-elements.md)
- ✅ Elements の複数行テキストがレイアウトで壊れる (elements `c98276e1` / src/core `c5e156fa`)
  `default_label_styler` の limits / draw を改行対応に。`text_area` の高さ (1-b) は
  報告後の修正で解決済みだったことを実機確認、dialog の `size` (1-c) は仕様どおりで
  README 記載済み、DSL の lint (1-d) は不要になった。詳細 = [TODO-elements.md](TODO-elements.md)
