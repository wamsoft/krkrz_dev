# 吉里吉里Z / TJS2 開発ナレッジパック (Codex / ChatGPT 用)

krkrz_dev の Claude Code 用スキル (`tjs2` / `krkrz` / `elements` / `krkrz-repl` / `krkrz-webui`) と、
それが参照するリファレンス一式を、Codex と ChatGPT で使える形にまとめたものです。

| ファイル | 中身 |
|---|---|
| `skills/` | スキル本体 (SKILL.md 形式、リファレンス同梱)。**Codex はこれを使う** |
| `instructions.md` | ChatGPT の GPT / プロジェクトの「指示」欄に貼る文面 (8,000 文字以内) |
| `knowledge/` | ChatGPT にナレッジとしてアップロードするファイル (20 個以内) |
| `knowledge/00_INDEX.md` | 元のスキル内のパス → どのナレッジファイルに入っているかの対応表 |
| `VERSION.md` | このパックの生成日と元にしたコミット (各 SKILL.md の先頭にも同じ情報があります) |

## Codex で使う

`skills/` の下の 5 つのフォルダ (`tjs2/` `krkrz/` `elements/` `krkrz-repl/` `krkrz-webui/`) を、
フォルダごと次のどちらかへコピーします。

- 自分の全作業で使う: `~/.agents/skills/` (Windows では `%USERPROFILE%\.agents\skills\`)
- 特定のリポジトリで使う: `<リポジトリ>/.agents/skills/` (コミットすればそのリポジトリの全員に効きます)

```
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

Codex は新しいスキルを自動で見つけます。出てこなければ Codex を再起動してください。
TJS2 のコードを書く・`.tjs` を直す・Layer や Window の使い方を聞く、といった依頼で自動的に使われます。
明示するなら `$tjs2` `$krkrz` のようにスキル名で呼べます。

更新するときは、古い 5 フォルダを消してから新しいものをコピーしてください
(ファイルが減った場合に古いものが残らないように)。

## ChatGPT で使う

**カスタム GPT にする**

1. ChatGPT の「GPT を探す」→「作成する」→「構成」を開く
2. 「指示」に `instructions.md` の全文を貼る
3. 「知識」に `knowledge/` の中のファイルを全部アップロードする
4. 「機能」はコードインタープリターをオンにしておくと、ナレッジの全文検索がしやすくなります

**プロジェクトで使う**

1. ChatGPT でプロジェクトを作り、「指示」に `instructions.md` の全文を貼る
2. 「ファイル」に `knowledge/` の中のファイルを追加する
3. そのプロジェクトの中でチャットを始める

## 注意

- 中身は生成した時点の krkrz_dev のドキュメントです。版は `VERSION.md` で確認できます
- スキル本文には「Claude」「Read で開く」など Claude Code 向けの言い回しが残っています。
  ファイルを読めるエージェントなら同じ意味に読み替えて使えます
- `krkrz-repl` / `krkrz-webui` は、手元で krkrz を起動してエージェントから操作する手順です。
  Codex ならそのまま実行できます。ChatGPT (ブラウザ) では実行できないので、示された手順を
  手元で実行して結果を貼り付ける使い方になります
