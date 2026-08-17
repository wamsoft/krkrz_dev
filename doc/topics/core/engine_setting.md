# エンジン設定の追加/編集
## 従来の方法
吉里吉里2 では、本体は TVPGetCommandDesc で得られる "|" 区切り(他の区切り文字もあり)の文字列を得て、それを元にエンジン設定の項目を表示していた。  
また、プラグインでは、コメント部に --has-option-- を入れて、GetOptionDesc 関数を公開し、その中で本体と同じ文字列フォーマットで設定の詳細を入れていた。  
リンカに /COMMENT: で --has-option-- を追加していたが、最近の Visual Studio では無視されるので、通常の方法ではこれを DLL バイナリに入れることは出来なくなっていた。

## 吉里吉里Zからの方法
吉里吉里Z では、設定項目のリストは JSON にし、ソースに埋め込むのではなくリソースに入れる方法に変更した。  
JSON の具体的なフォーマットは、ファイルを見ればだいたい分かるはず。  
本体の方はリソースの option_desc_ja.json を編集してもらえば反映されるのでいいとして、プラグイン側は少し注意が必要。  
リソースの種類は、TEXT で、ID は文字列 IDR_OPTION_DESC_JSON で DLL に格納する。  

具体的には *.rc ファイルに、以下のように記述してリソースに追加する。  
IDR_OPTION_DESC_JSON TEXT "option_desc_ja.json"

resource.h では、IDR_OPTION_DESC_JSON を定義しない。  
IDR_OPTION_DESC_JSON を定義するとリソース ID が数値で追加される。

### JSON のフォーマット

トップレベルは**カテゴリの配列**で、各カテゴリが `options` にオプション定義の配列を持つ。
本体の実物は `src/core/resource/optiondesc.json` ( 7 カテゴリ / 56 オプション ) を参照。

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