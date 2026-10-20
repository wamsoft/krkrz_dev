# Claude Code 用スキル (インストールと更新)

krkrz_dev に同梱している [Claude Code](https://claude.com/claude-code) 用スキル (`krkrz` / `tjs2` /
`elements` / `krkrz-repl` / `krkrz-webui`) を、krkrz_dev の外でも使えるようにする方法です。
スキルの一覧はリポジトリ直下の README を参照してください。

正本は `.claude/skills/` にあります。**krkrz_dev で作業している間は追加のセットアップなしで有効**です
(Claude Code がプロジェクトのスキルとして読み込みます)。

## 他の場所でも使う (インストール)

`krkrz` / `tjs2` の SKILL.md は、詳しいリファレンスを `doc/reference/`・`doc/tjs2/` のような
**このリポジトリからの相対パス**で参照しています。そのため他のリポジトリへそのままコピーしても参照が
解決しません。

`tools/skills/install.sh` は、参照しているドキュメントをスキルの中の `references/` に同梱し、SKILL.md の
パスを書き換えて、**どこに置いても壊れない形**に組み立てます。実行には bash が要ります (msys2 / Git Bash)。

**自分用に入れる** — 以後どのリポジトリで作業していても有効になります。

```
bash tools/skills/install.sh --user
```

`~/.claude/skills/` に置かれます。同じ名前のスキルがあるときは確認を求めます (`--force` で確認なし)。
**このスクリプトが触るのは上の 5 つのスキルだけ**で、そこにある他のスキルには手を出しません。

**別のリポジトリに入れる** — そのリポジトリで作業する人全員に配りたい場合です。

```
bash tools/skills/install.sh --project /path/to/project
```

`<project>/.claude/skills/` に置かれます。そのリポジトリにコミットすれば、clone した人はセットアップ
なしで使えます。`.gitignore` で `.claude` を無視している場合は、krkrz_dev と同じように

```
.claude/*
!.claude/skills/
```

としてください。

**配布用に書き出す** — krkrz_dev を持っていない人へ配る場合です。

```
bash tools/skills/install.sh --dist /path/to/dist-repo
```

プラグインの構造 (`.claude-plugin/marketplace.json` + `plugins/krkrz-skills/`) で書き出します。これを git
リポジトリとして push すると、受け取る側は次で入れられます。

```
/plugin marketplace add <owner>/<repo>
/plugin install krkrz-skills@krkrz-skills
```

`--dry-run` を付けると、何をどこへ書くかだけを表示して終わります。

## 更新

スキルやリファレンスを更新したら、入れた先では `install.sh` を同じオプションで実行し直してください
(`--force` を推奨)。同梱されるリファレンスは、実行した時点のリポジトリの内容です。

## スキルを編集するとき

- 編集するのは `.claude/skills/` の**正本**です。入れた先を直接直しても、次の `install.sh` で上書きされます
- リファレンスはリポジトリからの相対パス (`doc/reference/<Name>.md` など) で参照します。同梱するときの
  パスの書き換えは `install.sh` の `BUNDLE` テーブルが受け持つので、参照先のフォルダを増やしたときは
  そこに 1 行足してください
- **特定のタイトルや取引先の情報 (名前・リポジトリのパス・設定値) は書かない**でください。スキルは
  リポジトリをまたいで配られます
- 今後の予定は [TODO-skills.md](TODO-skills.md) にあります
