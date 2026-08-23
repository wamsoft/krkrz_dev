# エンジン設定の追加/編集
## 従来の方法
吉里吉里2 では、本体は TVPGetCommandDesc で得られる "|" 区切り(他の区切り文字もあり)の文字列を得て、それを元にエンジン設定の項目を表示していた。  
また、プラグインでは、コメント部に --has-option-- を入れて、GetOptionDesc 関数を公開し、その中で本体と同じ文字列フォーマットで設定の詳細を入れていた。  
リンカに /COMMENT: で --has-option-- を追加していたが、最近の Visual Studio では無視されるので、通常の方法ではこれを DLL バイナリに入れることは出来なくなっていた。

## 吉里吉里Zからの方法
吉里吉里Z では、設定項目のリストは JSON にし、ソースに埋め込むのではなくリソースに入れる方法に変更した。  
JSON の具体的なフォーマットは、ファイルを見ればだいたい分かるはず。

### 本体側の定義ファイル (SSOT) と言語選択

本体の定義は `src/core/resource/optiondesc.json` ( 日本語 = 基底 ) と、その言語別
ファイル `optiondesc-en.json` / `optiondesc-chs.json` / `optiondesc-cht.json` の
4 ファイルが SSOT ( 以前 WINVER 用に別管理だった `win32/vcproj/option_desc_*.json`
は 2026-08 に廃止し、こちらへ一本化した )。編集時は 4 言語の構成 ( カテゴリと
オプションの並び ) を揃えておくこと。

読み込みは実行時に言語を選択する ( OS 言語 = `System.systemLanguage`、または
起動オプション `-language`。対応言語が無ければ en → 基底へフォールバック ):

- SDL3 ビルド … `resource/optiondesc<言語suffix>.json` を直接読む
- WINVER ビルド … `resource/*` はファイル名そのままの **BINARY** リソースとして
  exe へ埋め込まれており、それを同じ規則で選択する。見つからない場合は従来の
  TEXT リソース ( `IDR_OPTION_DESC_JSON`、実体は `resource/optiondesc.json` ) へ
  フォールバックする ( `KRKRZ_RESOURCE_DIR` を案件リソースへ差し替えた場合の保険 )

### プラグイン側

プラグイン側は少し注意が必要。  
リソースの種類は、TEXT で、ID は文字列 IDR_OPTION_DESC_JSON で DLL に格納する。  

具体的には *.rc ファイルに、以下のように記述してリソースに追加する。  
IDR_OPTION_DESC_JSON TEXT "option_desc_ja.json"

resource.h では、IDR_OPTION_DESC_JSON を定義しない。  
IDR_OPTION_DESC_JSON を定義するとリソース ID が数値で追加される。

SDL3 / 汎用ビルドのプラグイン ( .so 等、Win32 リソースを持てない形式 ) では、
DLL に隣接する `<basename>.options.json` ( 例: `myplugin.options.json` ) を
置くと読み込まれる。無ければ単に設定項目なしとして扱われる。

### JSON のフォーマット

トップレベルは**カテゴリの配列**で、各カテゴリが `options` にオプション定義の配列を持つ。
本体の実物は `src/core/resource/optiondesc.json` ( 7 カテゴリ / 65 オプション ) を参照。

```json
[
  {
    "category": "システム全般",
    "options": [
      {
        "caption":     "データ保存場所",
        "description": "吉里吉里が様々なデータを保存する場所を指定します。

...",
        "name":        "datapath",
        "type":        "string",
        "length":      255,
        "user":        false,
        "value":       "$(exepath)\savedata"
      },
      {
        "caption":     "処理ウェイト",
        "description": "...",
        "name":        "contfreq",
        "type":        "select",
        "user":        true,
        "values": [
          { "value": "0",  "desc": "ウェイトをかけない", "default": true },
          { "value": "60", "desc": "60Hz" }
        ]
      }
    ]
  }
]
```

#### カテゴリ

| キー | 内容 |
|---|---|
| `category` | 設定ツールのタブ / 見出しに出るカテゴリ名 |
| `options`  | このカテゴリに属するオプション定義の配列 |

#### オプション定義

| キー | 必須 | 内容 |
|---|---|---|
| `caption`     | ○ | 設定ツールに表示する項目名 |
| `description` | ○ | 説明文。`
` で改行できる |
| `name`        | ○ | コマンドラインオプション名 ( 先頭の `-` は書かない。`datapath` なら `-datapath=` ) |
| `type`        | ○ | `"select"` ( 選択肢から選ぶ ) または `"string"` ( 自由入力 ) |
| `user`        | ○ | エンドユーザ向け設定ツール ( `-userconf` ) に出すかどうか。`false` なら Releaser の制作者向け設定にのみ出る |
| `values`      | `select` のみ | 選択肢の配列 |
| `value`       | `string` のみ | 初期値 |
| `length`      | `string` のみ | 入力欄の最大文字数 |

#### 選択肢 (`values` の要素)

| キー | 必須 | 内容 |
|---|---|---|
| `value`   | ○ | 実際にオプションへ渡る値 ( 例 `"60"` ) |
| `desc`    | ○ | 選択肢として表示する文字列 |
| `default` | | `true` ならこれが既定値。カテゴリ内で 1 つだけ指定する |

!!! note "コマンドラインオプションの説明との関係"
    ここに書く `description` は**設定ツールに出る説明**で、
    [コマンドラインオプション](../../guide/CommandLine.md) のドキュメントとは別管理になっている。
    オプションを追加/変更したときは両方の更新が要る。