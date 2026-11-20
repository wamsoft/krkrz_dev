# krkrz-skills

吉里吉里Z (kirikiri Z) の開発向けの [Claude Code](https://claude.com/claude-code) 用スキル集です。
Claude に「TJS2 の書き方」「Layer の API」「REPL での確かめ方」を毎回説明しなくて済むように、
言語仕様・本体 API・UI・REPL 駆動のリファレンスを、Claude が必要なときに自分で読みに行ける形に
まとめています。

このリポジトリは [krkrz_dev](https://github.com/wamsoft/krkrz_dev) から生成した配布用のものです。
直接は編集しないでください (次の生成で上書きされます)。

## インストール (Claude Code)

いちばん簡単なのは、Claude Code に次のように頼むことです。

> https://github.com/wamsoft/krkrz-skills のスキルを入れて

自分で入れる場合は、Claude Code の入力欄で次の 2 行を実行します。

```
/plugin marketplace add wamsoft/krkrz-skills
/plugin install krkrz-skills@krkrz-skills
```

インストールすると、どのリポジトリで作業していてもスキルが有効になります。
入れたあとは Claude Code を再起動するか、新しいセッションを始めてください。

更新は `/plugin marketplace update krkrz-skills` のあと `/plugin update krkrz-skills@krkrz-skills` です。

### Claude Code への導入手順 (このリポジトリを入れるよう頼まれたエージェント向け)

1. ターミナルで次を実行してプラグインとして入れる (ユーザースコープ = 全リポジトリで有効)

   ```
   claude plugin marketplace add wamsoft/krkrz-skills
   claude plugin install krkrz-skills@krkrz-skills
   ```

2. `claude plugin` コマンドが使えない、またはプラグインを使いたくないと言われた場合は、
   スキルのフォルダを直接コピーする

   ```
   git clone --depth 1 https://github.com/wamsoft/krkrz-skills.git
   mkdir -p ~/.claude/skills
   cp -r krkrz-skills/plugins/krkrz-skills/skills/* ~/.claude/skills/
   ```

   コピー先に同じ名前のフォルダ (`tjs2` `krkrz` `elements` `krkrz-repl` `krkrz-webui`) があれば、
   上書きしてよいかをユーザーに確認する。この 5 つ以外のフォルダには触らない。
   特定のリポジトリだけで使いたいと言われたら、コピー先を `<リポジトリ>/.claude/skills/` にする

3. ユーザーに、Claude Code を再起動するか新しいセッションを始めるとスキルが有効になることを伝える

## 収録スキル

| スキル | 内容 |
|---|---|
| `tjs2` | TJS2 の言語仕様と組み込みクラス (Array / Dictionary / String / RegExp など)。JavaScript との違いを中心に |
| `krkrz` | 本体のクラスの API (Layer / Window / Bitmap / Storages / DrawDevice / OpenGL の描画 / サウンド / 主なプラグイン) と解説 |
| `elements` | Elements を使ったダイアログ / 画面 UI の作り方 |
| `krkrz-repl` | `-repl` / `-replfile` でのエージェントからの操作、Agent API、画面のキャプチャ |
| `krkrz-webui` | `-replweb` の HTTP + SSE サーバにブラウザの UI を載せる方法 |

TJS2 のコードを書く・`.tjs` を直す・Layer や Window の使い方を聞く、といった依頼で自動的に使われます。
明示的に呼ぶなら `/tjs2` `/krkrz` のようにスキル名を打ちます。

各スキルは詳しいリファレンスを `references/` などに同梱した自己完結形です。

## ほかのツールで使う

スキル本体は `plugins/krkrz-skills/skills/` の下にある SKILL.md 形式のフォルダです。
SKILL.md を読めるツールなら、フォルダごとそのツールのスキル置き場へコピーすれば使えます。

- Claude Code (プラグインを使わない場合): `~/.claude/skills/`
- Codex: `~/.agents/skills/` または `<リポジトリ>/.agents/skills/`

## 版

生成日と元にした krkrz_dev のコミットは [VERSION.md](VERSION.md) にあります。

## ライセンス

収録しているドキュメントは吉里吉里Z のドキュメントから作ったもので、吉里吉里Z と同じ条件
([LICENSE](LICENSE)) で利用できます。
