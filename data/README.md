# data — プラグイン/機能サンプル集

吉里吉里Z (umbrella) の**サンプル置き場**です。各プラグインや機能の
使い方を、実際に動く最小構成で示します。今後プラグインごとにサンプルを
追加していく前提で、以下の規約で構成します。

## 構成規約

- **1 サンプル = 1 サブフォルダ**。サブフォルダ自体が「実行可能な data
  ディレクトリ」になります (エンジンは data dir 直下の `startup.tjs` を
  起動スクリプトとして評価する)。
- 各サンプルフォルダの構成:
  ```
  data/<sample_name>/
    startup.tjs      … エントリポイント (必須)
    readme.txt       … そのサンプルの説明・実行方法・操作 (推奨)
    image/ 等        … そのサンプル専用の資材 (必要なら)
  ```
  資材はサンプルフォルダ内に閉じて持たせ、`Storages.addAutoPath("image/")`
  等でサブディレクトリを検索パスに登録して参照します (他サンプルや
  src/core/data と共有しない = 自己完結)。
- 依存プラグインは `startup.tjs` の中で `Plugins.canLink` → `Plugins.link`
  し、**無い場合はその機能をスキップ**して落ちないようにします
  (サンプルは環境依存で欠けても最低限動くのが望ましい)。

## 実行方法

`make install` 済みの実行ファイルに、サンプルフォルダのパスを渡します。

```
bin/<preset>/<config>/krkrz64.exe  data/<sample_name>
```

例 (umbrella ルートから):
```
bin/x64-windows/Release/krkrz64.exe  data/transition_demo
```

- プラグイン DLL は実行ファイルと同じフォルダ、または実行ファイル配下の
  `plugin64/` (32bit は `plugin/`) にあれば読まれます。`make install` した
  `bin/` 以下には各プラグインが揃います。
- Elements UI (`Dialog` クラス) を使うサンプルは **SDL3 ビルド +
  KRKRZ_USE_ELEMENTS=ON** (既定 ON) が必要です (WINVER ビルドでは Dialog
  クラスが登録されません)。→ プリセット `x64-windows` (SDL) を使用。

## サンプル一覧

| サンプル | 概要 | 主な対象 | 要 SDL/Elements |
|---|---|---|---|
| [transition_demo](transition_demo/) | 標準 + extrans + extNagano のトランジションを Elements UI パネルで選択・パラメータ設定・実行 | トランジション全般 / extrans / extNagano / Dialog | ○ |

*(今後、プラグインごとにサンプルを追加予定)*

## 新しいサンプルの追加手順

1. `data/<new_sample>/` を作成し、`startup.tjs` を置く。
2. 専用資材は同フォルダ内 (`image/` 等) に置き、`addAutoPath` で登録。
3. 依存プラグインは `canLink` ガード付きで `link`。
4. `readme.txt` に概要・実行方法・操作を記述。
5. この `README.md` の「サンプル一覧」に 1 行追加。

---

※ `data/` 直下の `startup.tjs` / `bg_*.png` は旧来の動作確認用スクラッチで、
サンプル集とは独立です (サンプルは各サブフォルダを data dir として起動します)。
