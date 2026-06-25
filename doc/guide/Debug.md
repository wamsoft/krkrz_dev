# デバッグ

## アプリケーションのデバッグについて

デバッグとは、アプリケーション内にあるバグ ( 機能不全や想定しない動作の原因 ) を特定し、修正する作業です。

吉里吉里はいくつかのデバッグ支援機能を持っていますので、その機能を用い、アプリケーションをデバッグします。その方法について説明します。

## デバッグメッセージ出力

吉里吉里はデバッグを支援するためのメッセージ出力先をいくつか提供しています。

- **[コンソール](Console.md)**
  コマンドラインから起動したときに、吉里吉里のシステムや、ユーザスクリプトが出力する様々なデバッグ用メッセージを端末上に表示することができます。

特にコンソールでは、[Debug.message](../reference/Debug.md#message) によってユーザプログラムがプログラム中で出力したメッセージが表示されます。プログラムの任意の場所でメソッドを呼び出し、変数の内容を表示させ、実行中の変数の内容を見ることができます。

メッセージ表示の方法やログをファイルに記述する方法については、[コマンドラインオプション](CommandLine.md) の「デバッグ関連のオプション」や [Debug クラス](../reference/Debug.md) を参照してください。

## デバッグモード

[コマンドラインオプション](CommandLine.md) で `-debug` を指定する (「デバッグモード」を ' 有効 ' にする) と、吉里吉里をデバッグモードで動作させることができます。

デバッグモードではTJS2の動作は低速になりますが、デバッグに便利ないくつかの機能が有効になります。

- **型情報追跡機能**  
  TJS2のオブジェクトに関する情報が強化されます。
  
  デバッグモードではない場合は、たとえば KAG で kag.saveSystemVariables の情報を得ようとしても
  
  ```
  コンソール : kag.saveSystemVariables = (object)(object 0x0279E130:0x01EB0BD4)
  ```
  
  が得られるだけですが、デバッグモードが有効の場合は
  
  ```
  コンソール : kag.saveSystemVariables = (object)(object 0x0279E130[(function) KAGWindow.saveSystemVariables]:0x01EB0BD4[instance of class KAGWindow])
  ```
  
  のように型の情報が得られます。(':' で区切られた２つの部分のうち、前の部分はオブジェクトの型、後ろの部分はそのオブジェクトが動作するコンテキストです )。
  
  デバッガで追う場合はほぼ必須のオプションです。
  
  この機能は、(現バージョンでは)オブジェクトが文字列に変換される過程すべてで有効になります。
- **オブジェクトリーク検出機能**  
  削除されていない(解放されていない)オブジェクトを終了時に警告する機能が有効になります。
  
  TJS2は本来、ガベージコレクション機能により、作成されたオブジェクトは自動的に削除され、明示的な削除の指示は必要ありません。しかし、プラグインや吉里吉里本体のバグ、循環参照が原因で、オブジェクトが削除されないままになる(リークする)可能性があります。
  
  デバッグモードでは、終了時になってもまだ解放されていないオブジェクトがコンソールのログファイルに書き出されます。
  
  たった一個のオブジェクトが解放されなかっただけでも、そのオブジェクトに関連するオブジェクトが全て検出されるため、ログファイルが巨大になる可能性がありますので注意してください。
  
  
  
  [System.exit](../reference/System.md#exit) メソッドは、アプリケーションを強制終了に近い形で終了させるもので、このメソッドでアプリケーションを終了させると多くのオブジェクトがリークし、大量のログが記録されますので注意してください。
  
  > **Note:**
  > 循環参照とは、A は B を参照している、B は A を参照しているという状況の事です。
  >
  > たとえば、以下のスクリプトは循環参照を生成します。
  >
  > ```
  > var a = %[], b = %[];
  > a.b = b; b.a = a;
  > ```
  >
  > このような状況では、オブジェクト a は b を必要とし、オブジェクト b は a を必要としています。TJS2が採用しているガベージコレクションの方法(参照カウンタ)はこのような状況を検出してオブジェクトを解放するのは困難であるため、TJS2ではこのような状況を検出しません。そのため、いつまで経ってもこれらのオブジェクトが削除されることはありません (明示的に invalidate 演算子でどちらかのオブジェクトを無効化すると循環参照を断ち切ることができます)。
  >
  >
  >
  > プラグインでは、参照カウンタの扱いを誤るとオブジェクトがリークする可能性があります。プラグインを作成して、その中でTJS2オブジェクトを扱う場合は、参照カウンタの扱いに十分注意してください。
- **削除中のオブジェクトでのスクリプト実行の警告**  
  オブジェクトは、削除あるいは無効化されるときに finalize メソッドが呼ばれます。
  
  オブジェクトが削除されるタイミングは、TJS2では「いつになるかわからない」ため、変なタイミングで finalize メソッドがよばれ、予期しない挙動を示す場合があります。デバッグモードでは、このような「不安定なタイミング」、つまり無効化されなかったオブジェクトがガベージコレクションによって削除され、finalizeメソッドが呼ばれたときに、警告がコンソールに表示されるようになります。
  
  警告は以下のような物です。
  
  ```
  警告: anonymous@0x016DFA7C(9)[(function) finalize]: 削除中のオブジェクト 0x0167DD44[instance of class A] 上でコードが実行されています。このオブジェクトの作成時の呼び出し履歴は以下の通りです:
                       anonymous@0x016DFA7C(13)[(top level script) global]
  ```
  
  このような状況を防ぐため、new で作成したオブジェクトは、使用し終わったら明示的に invalidate 演算子で無効化することを推奨します。
  
  ただし、Array や Dictionary、Date のように finalize メソッドがない、あるいは finalize メソッドでは特に問題を起こすような動作を起こさないクラスのオブジェクトについては、明示的な無効化は必要ない場合があります。
  
  上記の警告は、明示的な無効化が無いままオブジェクトが削除されようとし、そのコンテキスト上でTJS2スクリプトが実行されようとした場合に表示されます。
- **呼び出し履歴の取得機能**  
  TJS2 の関数/メソッド呼び出し履歴をスクリプトから取得できるようになります。
  
  これには [Scripts.getTraceString](../reference/Scripts.md#gettracestring) メソッドを用います。
  
  プログラムの途中に何か問題があり、そのメソッドがどこから呼ばれたのか分からない場合に、このメソッドを使って、呼び出し履歴をコンソールに出力したりができるようになります。

## VSCode による TJS2 デバッグ

吉里吉里Z は **Debug Adapter Protocol (DAP)** サーバを内蔵しており、
専用の VSCode 拡張 [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode)
と組み合わせると、通常のプログラミング言語と同じ感覚で TJS2 スクリプトを
デバッグできます。

### 必要なもの

- 吉里吉里Z 本体: ビルド時オプション `KRKRZ_ENABLE_DAP=ON` ( 既定で ON )
  でビルドされたバイナリ
- VSCode 1.75 以降
- [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode) 拡張

旧 `ENABLE_DEBUGGER` ( Win32 専用 `WM_COPYDATA` ベースの独自プロトコル ) は
2026-04-25 に廃止され、代わりに DAP に統一されました。

### 拡張のインストール

Marketplace 公開はまだのため、現状はリポジトリから直接ビルドして
インストールします。

```bash
git clone https://github.com/wamsoft/krkrz-vscode.git
cd krkrz-vscode
npm install
npm run package         # → krkrz-vscode-X.Y.Z.vsix を生成
code --install-extension krkrz-vscode-0.0.1.vsix
```

開発用に Extension Development Host で動かしたい場合は、`npm run compile`
の後に VSCode で本フォルダを開き **F5** を押します。

### 起動方法

吉里吉里Z を `-dap=<port>` 付きで起動します。`-dap=yes` を指定すると
既定ポート ( 6635 ) を使用します。

```
krkrz64.exe -dap=6635 path\to\data
```

VSCode 側で「実行とデバッグ」 → 「launch.json を作成」 → 「Kirikiri Z」
を選択するとスニペットが提供されます。`Attach` ( 起動済みの krkrz に接続 )
と `Launch` ( krkrz を spawn して接続 ) の 2 形式があります。

`launch.json` の主な設定項目:

| 項目 | 型 | 既定 | 説明 |
|---|---|---|---|
| `request` | string | — | `attach` または `launch` |
| `host` | string | `127.0.0.1` | DAP サーバのホスト |
| `port` | number | `6635` | TCP ポート |
| `stopOnEntry` | bool | `false` | 接続直後の最初の VM 行で停止 |
| `program` | string | — | `launch` 時に起動する krkrz 実行ファイル絶対パス |
| `data` | string | — | `launch` 時の data フォルダ |
| `args` | string[] | `[]` | 追加の krkrz オプション ( 例: `["-debug", "-loglevel=DEBUG"]` ) |
| `cwd` | string | program のあるディレクトリ | 作業ディレクトリ |
| `env` | object | `{}` | 環境変数の追加 |

### 対応機能

- ブレークポイント ( 条件付き / log point 対応 )
- ステップ実行 ( Over / In / Out )
- 一時停止 / 再開
- マルチフレーム コールスタック ( 各フレームの Locals / `this` / Globals 表示 )
- 変数 inspect ( Object / Array / Dictionary は子展開可 )
- Watch / Hover / Debug Console での式評価
- 例外停止 ( Uncaught Exceptions フィルタ )
- TJS の `debugger;` 文での停止
- TJS のログ出力を Debug Console に転送

### 既知の制限

- **KAG (`.ks`) 行への BP は不可** ( TJS VM の hook を踏まないため )。
  `[iscript]...[endscript]` 内の TJS なら BP 設置可能
- 例外 / BP 停止中は krkrz 全体 ( 描画・ContinuousHandler 等 ) が止まります。
  停止解除は VSCode の Continue / 停止ボタン、または吉里吉里Z 内蔵の
  [REPL](Console.md#repl) から ( 停止中も REPL 入力は処理されます )
- 条件付き BP / Watch / Hover の評価結果オブジェクトに対する mutation は
  フレームに反映されません ( snapshot 経由のため )
- `setBreakpoints` の verified は常に `true` を返すため、実在しない行に
  BP が置かれても無効化検出はされません
- TJS class 名は `exceptionInfo.typeName` に反映されません ( 現状 "Exception" 固定 )
- Hit count BP は未対応

詳細な使い方や拡張のビルド方法、最新の対応機能については
[krkrz-vscode の README](https://github.com/wamsoft/krkrz-vscode) を参照してください。
TJS2 / KAG のシンタックスハイライトも同拡張に同梱されています。
