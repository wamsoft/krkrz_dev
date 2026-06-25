# ログ出力

吉里吉里Z は実行中の動作ログをコンソール / ファイルに出力します。
出力レベルとフォーマットは複数の経路から制御できます。

詳細な仕様と設計は src/core 側のガイドを参照:

- [doc/Logging.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Logging.md)

---

## ログレベル

吉里吉里Z は次の 5 段階のログレベルを持ちます ( 上ほど重要度が高い )。

- `error` — エラー
- `warning` — 警告 ( `TVPAddImportantLog` )
- `info` — 通常ログ ( `TVPAddLog` )
- `debug` — デバッグ情報
- `off` — 全て抑止

ビルド時の既定値は次のとおり:

| ビルド | デフォルトレベル |
|---|---|
| `MASTER` | `warning` |
| Release ( 非 MASTER ) | `info` |
| Debug | `debug` |

実行時に上書きしたい場合は起動オプション
[`-loglevel=<level>`](../../guide/CommandLine.md) を使います。
配布バイナリで一時的に詳細ログを採取したいときに便利です。

```
krkrz64 -loglevel=debug data/
```

---

## 関連オプション

| オプション | 機能 |
|---|---|
| `-loglevel=<level>` | ログレベルの動的指定 |
| `-debug=yes` | デバッグモード ( デバッグ支援機能を有効 ) |
| `-forcelog=yes` | コンソールログを常時ファイルへ |
| `-logerror=yes` | エラー時のログをファイルへ |
| `-memstatinterval=N` | 周期メモリ統計ログ出力 |
| `-memstatonexit=1` | 終了時の統計ログ出力 |
| `-cachelistonexit=<mode>` | 終了時の cache 一覧ログ出力 |
