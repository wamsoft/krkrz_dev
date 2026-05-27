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

---

## 主な特殊コマンド

プロンプトは `krkrz>`、継続行は `...`。TJS の式や文をそのまま入力でき、
履歴は `.krkrz_history` に保存されます。

| コマンド | 説明 |
|---|---|
| `exit` / `quit` / `Ctrl+D` | REPL を抜けてアプリを終了 |
| `.help` | ヘルプ表示 |
| `.mem` | アロケータ + プロセスメモリの 1 行サマリ |
| `.memdump` | 詳細メモリ統計をログへダンプ |
| `.memoverlay [on\|off]` | 画面オーバレイの切替 ( SDL3 ビルド ) |
| `.mempeakclear` | peak 計測値を current_used に揃え直す |
| `.sysalloc` | システムアロケータ情報 ( 空き / 確保可能 / RSS ) を 1 行表示 |
| `.padoverlay [on\|off]` | パッドオーバレイの切替 ( SDL3 ビルド ) |
| `.filecache` | StorageCache ( file 層 ) 全エントリをログへダンプ |
| `.imagecache` | TVPGraphicCache ( decode 層 ) 全エントリをログへダンプ |

メモリ系コマンドの詳細は [メモリ観測ガイド](memory_observation.md)、パッド
オーバレイの詳細は [PadOverlay](pad_overlay.md) を参照してください。
