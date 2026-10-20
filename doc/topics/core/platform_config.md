# 外枠リポジトリの共通設定 (cmake / assetPack)

ブラウザ / Android / iOS / Linux / Microsoft GDK 向けのビルドは、それぞれ別の「外枠」リポジトリで
行います (krkrz_web / krkrz_android / krkrz_ios / krkrz_linux / krkrz_gdk)。どの外枠も
タイトルごとの設定ファイル (`app-config.json` など) を 1 本持ち、そのうち

- **`cmake`** — どのプラグインを組み込むか
- **`assetPack`** — ゲームのデータや資材をどこから集めて、配布物のどこへ置くか
- パス文字列の **`${...}` 展開**と相対パスの解決

は全ての外枠で同じ書式・同じ動作です。このページはその共通部分の説明です。機種ごとの項目
(アプリ ID・署名・アイコンなど) は各外枠の README を参照してください。

書式が同じなので、1 つのプロジェクトフォルダに各機種の設定ファイルを並べて、同じ `data/` を使い回せます。

```
mygame/                     ← PROJECT_DIR
├── data/                   ← ゲームデータ (全機種で共通)
├── archive/                ← 自分で作った xp3 (任意)
├── app-config.json         ← krkrz_android
├── ios-config.json         ← krkrz_ios
├── linux-config.json       ← krkrz_linux
├── gdk-config.json         ← krkrz_gdk
└── web-config.json         ← krkrz_web
```

## 外枠ごとの対応

| 外枠 | 設定ファイル | `cmake` | `assetPack` の置き先 | その外枠だけの主な項目 |
|---|---|---|---|---|
| [krkrz_android](https://github.com/wamsoft/krkrz_android) | `app-config.json` | ○ | APK の `assets/` | `resOverride` (res の上書き)、`padPacks` (Play Asset Delivery) |
| [krkrz_ios](https://github.com/wamsoft/krkrz_ios) | `ios-config.json` | ○ (全プラグインを静的リンク) | アプリバンドル直下 | `graphics` (gles / metal)、`icon`、`infoPlist` |
| [krkrz_linux](https://github.com/wamsoft/krkrz_linux) | `linux-config.json` | ○ (+ `buildType` / `options`) | 実行ファイルと同じフォルダ | `exeName`、`orgName` / `appName`、`desktop` |
| [krkrz_gdk](https://github.com/wamsoft/krkrz_gdk) | `gdk-config.json` | ○ (全プラグインを静的リンク、+ `options`) | 実行ファイルと同じフォルダ | `targets`、`identity`、`gpuShaderDir` |
| [krkrz_web](https://github.com/wamsoft/krkrz_web) | `web-config.json` | — (共有バイナリなのでタイトルごとに組まない) | `gamedata/` (`web://` で配信) | `sources[].delivery` (先読み)、`lowercase`、`args` |

## パス文字列の展開

設定ファイル内のパス文字列には `${...}` を書けます。

| 書き方 | 展開先 |
|---|---|
| `${PROJECT_DIR}` | プロジェクトフォルダ (設定ファイルのあるフォルダ) の絶対パス。指定が無いときは外枠リポジトリのルート (= 同梱のサンプルで動く) |
| `${BUILD_SYSTEM_DIR}` | 外枠リポジトリのルートの絶対パス。外枠に同梱したプラグインなどを指すときに使う |
| `${KRKRZ_BASE}` などの環境変数 | プロセスの環境変数の値。**未定義なら空文字**になる (`${KRKRZ_BASE}/foo` は `/foo` になる) |

- 展開したあとに相対パスが残った場合は **`${PROJECT_DIR}` 基準**で解決します
- 展開が効くのはパスを書く項目 (`assetPack.baseFolder`、`assetPack.sources[].from`、`cmake.pluginFolders[]` など)
  です。プラグイン名 (`cmake.plugins` など) は展開しません

## cmake — 組み込むプラグイン

```jsonc
"cmake": {
    "pluginFolders": [
        "${KRKRZ_BASE}/krkrz_dev/src/plugins",
        "${PROJECT_DIR}/plugins"
    ],
    "plugins": ["json", "csvParser", "saveStruct"],
    "staticPlugins": ["json"]
}
```

| キー | 内容 | CMake の変数 |
|---|---|---|
| `pluginFolders` | プラグインのフォルダを探す場所。相対パス (`${PROJECT_DIR}` 基準) / 絶対パス / `${...}` が使えます | `TVP_PLUGIN_FOLDERS` |
| `plugins` | 組み込むプラグイン (フォルダ名) | `TVP_PLUGINS` |
| `staticPlugins` | エンジンへ静的リンクするもの (`plugins` の一部) | `TVP_PLUGINS_STATIC` |

- iOS と GDK は全てのプラグインを静的リンクするので `staticPlugins` は要りません
- 外枠の中 (`${BUILD_SYSTEM_DIR}/...`) のプラグインを使う場合は `${BUILD_SYSTEM_DIR}` を明示してください。
  相対パスはプロジェクトフォルダ基準なので、そちらに無ければ見つかりません
- 設定から作られる CMake のファイルはビルドフォルダに生成されます。直接編集しても次のビルドで
  上書きされるので、変更は設定ファイル側で行います
- `cmake` を省略するとプラグインを組み込みません

プラグインの選び方 (フォルダ名と CMake のターゲット名の関係など) は krkrz_dev の
[プラグイン一覧](../../guide/Plugins.md) を参照してください。

## assetPack — 資材の取り込み

プロジェクトフォルダなど、外枠の外にあるデータをビルド時に集めて配布物へ置きます。

```jsonc
"assetPack": {
    "baseFolder": "${PROJECT_DIR}",
    "sources": [
        {
            "comment": "ゲームデータをそのままの構成で置く",
            "type": "mirror",
            "from": "data",
            "exclude": ["**/*.bak", "**/*.psd"]
        },
        {
            "comment": "自分で作った xp3 をルートへ並べる",
            "type": "flatten",
            "from": "archive",
            "include": ["*.xp3"]
        }
    ]
}
```

| キー | 必須 | 内容 |
|---|---|---|
| `baseFolder` | 相対の `from` を使うなら必須 | 相対の `from` の起点。相対パス (`${PROJECT_DIR}` 基準) / 絶対パス / `${...}` が使えます |
| `transfer` | | `"copy"` (既定) / `"hardlink"` (下記)。対応は外枠ごとに README を参照 |
| `sources` | ○ | 取り込みの定義の配列。**書いた順に処理します** |
| `sources[].type` | ○ | `"mirror"` / `"flatten"` |
| `sources[].from` | ○ | 取り込むフォルダ。相対なら `baseFolder` 起点、絶対ならそのまま |
| `sources[].include` | | 取り込むファイルのパターンの配列 (例: `"**/*.png"`)。既定は `["**/*"]` |
| `sources[].exclude` | | 除くファイルのパターンの配列。既定は `[]` |
| `sources[].to` | | 置き先のフォルダ (配布物の資材のルートからの相対)。省略時は下記 |

`comment` のような知らないキーは無視されるので、各項目の意図をメモしておけます。

### type

- **`mirror`** — `from` の下のファイルを、フォルダ構成を保ったまま `to` の下へ置きます
- **`flatten`** — フォルダ構成を捨てて、ファイル名だけで `to` の直下へ置きます

`to` を省略したときの置き先:

| 条件 | 置き先 |
|---|---|
| `mirror` + 相対の `from` | `from` と同じ名前 (`from: "data"` → `data/...`) |
| `mirror` + 絶対の `from` | `from` の末尾のフォルダ名 |
| `flatten` | ルート直下 |

ルート直下に展開したいときは `"to": ""` を明示します。

パターン (`include` / `exclude`) は Ant 風のグロブです。`*` はフォルダ区切りを含まない任意の文字列、
`**` は 0 個以上のフォルダに一致します (`**/*.psd` は全階層の .psd)。

### 同じ置き先の衝突 (先勝ち)

複数の `sources` (または `flatten` の別々のフォルダ) が同じ置き先に書こうとした場合は、
**先に現れたファイルが採用され**、後のものは警告を出して飛ばします。自分の側で上書きしたい
ファイルの source を前に書けば、後ろの source の同名ファイルより優先されます。

外枠が自分で置くファイル (エンジン一式・設定から作るファイルなど) との順番は外枠ごとに違います。

- **krkrz_linux / krkrz_gdk** — エンジン一式と生成物を先に置き、そのあとに `assetPack` を処理します。
  つまり同じ名前のファイルを `assetPack` で上書きすることはできません
- **krkrz_android** — エンジンの必須資材 (`src/core/resource`) も `sources` の 1 項目として書きます。
  プロジェクトフォルダの `resource/` をその前に書けば、個別のファイルを差し替えられます

### 差分更新

再実行したときは変わったものだけを更新します。元から消えたファイルは置き先からも消え、
内容の変わらないファイルはコピーし直しません (タイムスタンプも保つので、後段の処理を
無駄に走らせません)。

### transfer: hardlink

元と置き先が同じドライブ (同じファイルシステム) にある場合、`"transfer": "hardlink"` にすると
コピーの代わりにハードリンクを作ります。数 GB の資材でもディスクをほとんど使わず、時間もほぼ
かかりません。

- 元のファイルを書き換えると置き先にもすぐ反映されます (実体が同じため)。ビルド前に元を
  書き換える運用がある場合は既定の `copy` を使ってください
- ハードリンクを作れないファイル (別ドライブ・ネットワーク上・FAT など) は自動的にコピーに
  切り替えます
- Windows (NTFS) でも管理者権限は要りません。シンボリックリンクは使いません

## 関連

- 各外枠の README — 機種ごとの項目・ビルド手順
- [Linux 版の配布パッケージ](linux_package.md) — krkrz_linux の配布形式の考え方
