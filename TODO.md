# 課題一覧 (索引)

krkrz_dev 全体の未対応課題をここに集約する。**詳細な SSOT が別にあるものはリンクのみ**に
留め、内容を二重管理しない。

| 領域 | 詳細 SSOT |
|---|---|
| Elements (レイアウト/ダイアログ) の要修正 | [TODO-elements.md](TODO-elements.md) |
| デモ整備 | [data/ROADMAP.md](data/ROADMAP.md) |
| WINVER モダン化 | [src/core/doc/ModernizationRoadmap.md](src/core/doc/ModernizationRoadmap.md) |
| 動画 (Media Foundation 移行) | [src/core/doc/MovieMFMigration.md](src/core/doc/MovieMFMigration.md) |
| リファレンスとコードの差分 | [doc/_missing.md](doc/_missing.md) (生成物。現在 0 件) |

対応したら項目に ✅ と対応コミットを書き、**消さずに残す** (再発防止の記録)。

---

## 予定・未着手

| 優先 | 課題 | 内容 |
|---|---|---|
| 中 | 全生成器の Perl 撤去 → Python 統一 | 残 = syntax 後処理 5 本 と `gengl.pl` (7519 行 = 最大の山)。バイト一致の差分ゲート方式。他作業と独立に実施可 |
| 中 | DrawDevice overlay 描画口の汎用開放 | `PostRenderCallback` の tp_stub 公開 + WINVER 対応 (小) / dialog renderer の painter リスト化 (大) |
| 低 | プラグイン横断のリソース消費収集 IF | 命名規約 `getResourceUsage()` の策定から。ライセンス収集 IF と同じ枠組み |
| 低 | プラグイン向けログレベル個別 IF | `TVPLogMsg` を tp_stub に収録するだけ。important = WARNING は維持 |
| 低 | WINVER の `Window.setZoom` が事実上効かない | WINVER は zoom を DestRect 計算にしか使わず、レイヤ×zoom をクライアントへアスペクト維持でフィットさせるため、windowed では倍率を変えても見た目が変わらない (旧 kirikiri2 はウィンドウ自体がリサイズされた)。SDL/generic 側は「レイヤ×zoom をウィンドウの内側サイズにする」実装 (`window_multi` デモで確認可)。KAG3 の画面サイズ切替に影響するため、揃えるかどうかは要判断 |
| 低 | 「SDL3 ビルド限定」表記の全体精査 | WINVER 対応済みの機能が「SDL3 限定」と書かれたままの箇所がある。Dialog は修正済、CommandLine / System overlay 系が要確認 |

## 将来課題

| 優先 | 課題 | 内容 |
|---|---|---|
| 中〜高 | WaveSoundBuffer 3D 定位 API (F-1) | miniaudio の spatializer で全バリアント横断の 3D 定位 API を新設 |
| 中 | Elements を WINVER のネイティブ経路へ | 中立イベント型の導入 / manager のテキスト入力・ウィンドウ取得の seam 化 / WndProc → manager 転送 + IME / OGLDrawDevice への renderer 配線 / elements_gallery の実機確認。[data/ROADMAP.md](data/ROADMAP.md) 参照 |
| 中 | SDL ビルドの SEH 捕捉 | ゼロ除算・アクセス違反でログを残さず即死する。WINVER は translator + minidump あり |
| 低 | WINVER モダン化の残 | F-3 (入力)、HW mixer の直描画 |
| 低 | generic フラグの 3 種区別 | `kirikiriz_generic` が導入当時「CS (コンシューマ) 版」の意味だったため、案件スクリプトは generic = プラグイン静的リンク前提で分岐している。PC の SDL ビルドは CS でも WINVER でもない第 3 の形態なのに区別する手段が無い。案件側スクリプトにも影響するため改定は慎重に |

## 低優先・保留

- MF SourceReader の WINVER YUV 対応
- web REPL の modal 転送 / 重複プラグインの削除
- Elements WINVER 展開のクリーンアップ
- ゲームパッド実機での最終確認
- glyphware: richtext 統合 (保留) / ThorVG 系のバイト共有最適化 / `fonts.json` スキーマ拡張
- krkreffekseer の macOS (GLES3) 実機確認 (⏸ ビルド対応済)
- tjsDataPack のライセンス収集 IF 対応 (保留)
- リップシンクの母音判定精度向上とデモ
- Elements 遷移エフェクト Phase C (GPU present 拡張・optional)

## デモ整備

[data/ROADMAP.md](data/ROADMAP.md) に未完 24 項目。未着手デモは
`sound` / `sound_3d` / `video` / `storage` / `ui_flow` / `system_debug` /
`data_parse` / `net_demo` / `movie_alpha` / `archive_demo` / `richtext_demo` の 11 本。
ほかに doc へのデモ一覧ページ新設、krkrz_web のランチャ起動トークン (スラッシュ入り)
対応、wasm 再ビルド (別リポ作業・未実施)。

---

## 最近クローズしたもの

- ✅ WINVER のモーダルウィンドウがマウス操作を受け付けない (src/core `49fdd011`)
  D3D9 → D3D11 移行の回帰。vblank 待ちをメインスレッドから VSync タイミング
  スレッドへ移動。詳細 = [src/core/doc/D3D11Migration.md](src/core/doc/D3D11Migration.md) 追補節
- ✅ SDL / generic の `Window.showModal` 実装 + generic で `onClick` が発火しない欠落
  (src/core `f6aa5900`) 詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ モーダル表示中にタイマーが完全停止する / wake 投函失敗でタイマーが永久停止する
  / WINVER の Agent 入力がモーダルへ届かない (src/core `90698ee1`)
  詳細 = [src/core/doc/ModalWindow.md](src/core/doc/ModalWindow.md)
- ✅ Elements の複数行テキストがレイアウトで壊れる (elements `c98276e1` / src/core `c5e156fa`)
  `default_label_styler` の limits / draw を改行対応に。`text_area` の高さ (1-b) は
  報告後の修正で解決済みだったことを実機確認、dialog の `size` (1-c) は仕様どおりで
  README 記載済み、DSL の lint (1-d) は不要になった。詳細 = [TODO-elements.md](TODO-elements.md)
