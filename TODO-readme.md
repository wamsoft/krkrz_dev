# README の整理と英語版

krkrz_dev と外枠リポジトリ、標準ツール、公開エンジンの README を同じ構成に揃え、
英語版 (`README_en.md`) を用意する。既定の `README.md` は日本語のまま。

## 対象 (公開リポジトリ 8 本)

| リポジトリ | 現状の行数 | 主な問題 |
|---|---|---|
| krkrz_dev | 343 | 公開サイトへのリンクが無い / master・develop の説明が無い / vcpkg マニフェストの仕組みや Makefile の変数表など開発者向けの詳細が混ざっている / ライセンス節が無い / 文体が混在 |
| krkrz_android | 1007 | 長すぎる。ios / linux / gdk が「android と同じ書式」と参照する `cmake` / `assetPack` の仕様が README の途中にある / ライセンス節が無い |
| krkrz_web | 440 | 常体 / ライセンス節が 1 行 |
| krkrz_ios | 165 | 常体 / ライセンス節が無い |
| krkrz_linux | 142 | ライセンス節が無い |
| krkrz_gdk | 238 | (ほぼ型どおり。ライセンス節あり) |
| krkrz_tools | 234 | 常体 |
| krkrz (src/core) | 523 | (構成は整っている。英語版と言語切り替えの追加が主) |

krkrz_nx ほか非公開のリポジトリは対象外。

## 決めたこと (2026-10-20)

- 文体は**ですます調**に揃える
- 外枠共通の `cmake` / `assetPack` の書式は **公開サイト (krkrz_dev の docs) に 1 ページ**置いて正本にし、
  各 README からリンクする (日英は既存の翻訳の仕組みで管理できる)
- 長い README は詳細を各リポジトリの `docs/` へ移し、README は概要と索引に絞る (目安 200 行前後)
- 英語版は `README_en.md`。両方の先頭に言語の切り替えリンクを置く

## 共通の構成 (外枠リポジトリ)

1. タイトル `# krkrz_xxx — 吉里吉里Z <機種> 版` と、言語の切り替え行 (`日本語 | [English](README_en.md)`)
2. 概要 (何をするリポジトリか 2〜4 行。krkrz_dev を `KRKRZ_BASE` で参照する外枠であること。
   ターゲットと状況の表があればここ)
3. 必要なもの
4. セットアップ
5. ビルドと実行 (サンプル → 案件 `PROJECT_DIR`)
6. `<x>-config.json` (その機種だけの項目。共通の `cmake` / `assetPack` は公開サイトのページへリンク)
7. 機種固有の項目 (署名・ストア提出・セーブ先・devkit など)
8. 機能の対応状況 (あれば)
9. ドキュメント (`docs/` の索引表)
10. ライセンス (共通の雛形。リポジトリ自体のライセンス + 参照・取得するもの)

krkrz_dev: 概要 (中身・公開サイト・ブランチ) / リポジトリの構成 (submodule) / 外枠リポジトリの一覧 (表で短く) /
必要なもの / ビルド (Windows / Linux / macOS) / 標準ツール / プラグインの選び方 / Claude Code 用スキル / ライセンス。
vcpkg マニフェストの統合の仕組みなど開発者向けの詳細は開発用ドキュメントへ移す。

## 英語版の管理

- `README_en.md` の先頭に `<!-- source_hash: ... -->` を置き、日本語版から計算した値と比べて古さを判定する
  (公開サイトの `check_translations.py` と同じ考え方)。複数リポジトリを横断して見る小さな確認スクリプトを
  krkrz_dev の `tools/docgen/` に置く
- 用語は `doc/i18n/glossary.md` に揃える

## 進め方

1. 公開サイトに外枠共通の書式のページ (`cmake` / `assetPack` / `${...}` 展開) を作る (日英)
2. krkrz_android の詳細を `docs/` へ分け、README を共通構成に
3. 残りの外枠 (web / ios / linux / gdk) を共通構成に
4. krkrz_dev / krkrz_tools / krkrz (src/core) を整理
5. 各 `README_en.md` を作る + 確認スクリプト

## 状況

- 2026-10-20: 現状確認と方針決定まで
- 2026-10-20: 1 を完了。公開サイトに [外枠リポジトリの共通設定](doc/topics/core/platform_config.md) (日英)。
  公開文書の用語の決まり (「案件」は書かない) に合わせ、プロジェクトフォルダ / タイトルと書いた
- 2026-10-20: 2〜5 を完了 (全 8 本を共通構成 + ですます + README_en.md。push 前)。
  - krkrz_android 1007→139 行 (docs/ に android-build / config / signing / customize を新設)、krkrz_web 440→188 行
    (docs/ に web-build / config / hosting / save-data / loading / shell / video / tools)、krkrz_tools 234→133 行
    (docs/ にツールごとのページ)。krkrz_ios は docs/ios-config.md を新設。krkrz_linux / krkrz_gdk / src/core は構成をそろえた
  - krkrz_dev: 公開サイト・ブランチ・リポジトリの構成を追加。vcpkg マニフェストの仕組みは MergeVcpkgManifest.cmake の
    先頭の説明へのリンクに、スキルのインストール手順は tools/skills/README.md へ
  - 英語版の鮮度は `tools/docgen/check_readme_en.py` (全 8 本 訳済み)
  - README 以外でも直したもの: 利用者向け docs・サンプル設定の「案件」、krkrz_web の CMakeLists.txt と src/core の
    CMakeLists.txt のコメントにあった非公開リポジトリ名 / 機種名を一般的な書き方に
  - 残り (README の外・未着手): 外枠の Makefile / スクリプト / CLAUDE.md のコメントの「案件」、krkrz_web の
    既定リソースフォルダ名 `setup/nxresource` (コードの既定値)
- 2026-10-20: 外枠リポジトリのライセンスを MIT に統一 (ユーザ決定)。android / ios / linux / web に LICENSE
  (krkrz_gdk と同じ MIT、Copyright WAMSOFT) を追加し、README (日英) のライセンス節を gdk と同じ書き方に
