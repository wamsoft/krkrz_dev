#!/usr/bin/env bash
#
# krkrz_dev の Claude Code スキルを「自己完結形」へ組み立てて配置する。
#
# 正本は <repo>/.claude/skills/ にあり、リファレンスは krkrz_dev のリポジトリ相対パス
# (doc/reference/ 等) を参照している。この形は krkrz_dev の中でしか解決できないため、
# 配布時は参照ドキュメントをスキル内 references/ へ同梱し、SKILL.md 内のパスを
# 書き換えて、どこに置いても壊れない形にする (Claude Code スキルの標準構成)。
#
#   bash tools/skills/install.sh --user            # → ~/.claude/skills/  (全リポジトリで有効)
#   bash tools/skills/install.sh --project <path>  # → <path>/.claude/skills/
#   bash tools/skills/install.sh --dist <path>     # → プラグイン構造で出力 (配布リポジトリ用)
#
# オプション:
#   --force   既存の同名スキルを確認なしで置き換える
#   --dry-run 何をするかだけ表示する
#
set -euo pipefail

REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
SRC="$REPO_ROOT/.claude/skills"

# 対象スキル。ここに列挙したものだけを扱う (配置先の他スキルには触れない)
SKILLS=(krkrz tjs2 elements krkrz-repl krkrz-webui)

PLUGIN_NAME="krkrz-skills"
MARKETPLACE_NAME="krkrz-skills"

MODE=""
DEST=""
FORCE=0
DRYRUN=0

die() { echo "error: $*" >&2; exit 1; }
say() { echo "$*"; }
run() { if [ "$DRYRUN" = 1 ]; then echo "  [dry-run] $*"; else "$@"; fi; }

usage() {
  sed -n '3,20p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'
  exit 1
}

while [ $# -gt 0 ]; do
  case "$1" in
    --user)    MODE=user; shift ;;
    --project) MODE=project; DEST="${2:-}"; [ -n "$DEST" ] || die "--project にパスが必要"; shift 2 ;;
    --dist)    MODE=dist;    DEST="${2:-}"; [ -n "$DEST" ] || die "--dist にパスが必要";    shift 2 ;;
    --force)   FORCE=1; shift ;;
    --dry-run) DRYRUN=1; shift ;;
    -h|--help) usage ;;
    *) die "不明な引数: $1" ;;
  esac
done
[ -n "$MODE" ] || usage
[ -d "$SRC" ] || die "スキルの正本が見つからない: $SRC"

# ---------------------------------------------------------------------------
# 同梱テーブル:  <skill>|<repo からの元パス>|<references 配下の宛先>|<書き換え前>|<書き換え後>
# 元パスがディレクトリなら中身を、ファイルならそれ自体をコピーする。
# ---------------------------------------------------------------------------
BUNDLE=(
  "krkrz|doc/reference|.|doc/reference/|references/"
  "tjs2|doc/tjs2|.|doc/tjs2/|references/"
  "tjs2|doc/topics/tjs2|topics|doc/topics/tjs2/|references/topics/"
  "elements|src/core/doc/ElementsDialog.md|.|doc/ElementsDialog.md|references/ElementsDialog.md"
  "krkrz-webui|src/core/doc/REPL.md|.|doc/REPL.md|references/REPL.md"
)

# 組み立て後のスキルに差し込む注記 (同梱できなかった engine ソースツリー参照の説明)
read -r -d '' NOTE <<'NOTE_EOF' || true

> **配布版メモ** — このスキルは krkrz_dev から組み立てられた自己完結版です。
> 深掘り用のリファレンスは `references/` に同梱済みで、そのまま Read できます。
> 本文に残る engine ソースツリー相対パス (`data/...`, `common/...`, `external/...`,
> `src/core/...`) は krkrz_dev のチェックアウトを指します。手元に無い場合は
> 「エンジン側のどこにあるか」の記述として読んでください。
NOTE_EOF

# 出力先を決める
case "$MODE" in
  user)    OUT="$HOME/.claude/skills" ;;
  project) OUT="$DEST/.claude/skills" ;;
  dist)    OUT="$DEST/plugins/$PLUGIN_NAME/skills" ;;
esac

say "krkrz_dev skills installer"
say "  正本  : $SRC"
say "  出力先: $OUT"
say "  対象  : ${SKILLS[*]}"

# 所要サイズを先に出す (references の同梱で数 MB になるため)
total=0
for row in "${BUNDLE[@]}"; do
  IFS='|' read -r _sk from _to _a _b <<<"$row"
  if [ -e "$REPO_ROOT/$from" ]; then
    kb=$(du -sk "$REPO_ROOT/$from" | cut -f1)
    total=$((total + kb))
  fi
done
say "  同梱リファレンス: 約 $((total / 1024)) MB"
say ""

# 既存の確認
existing=()
for s in "${SKILLS[@]}"; do [ -e "$OUT/$s" ] && existing+=("$s"); done
if [ ${#existing[@]} -gt 0 ] && [ "$FORCE" = 0 ] && [ "$DRYRUN" = 0 ]; then
  say "既に存在するスキル: ${existing[*]}"
  say "(これら以外のスキルには触れません)"
  if [ -t 0 ]; then
    printf "置き換えますか? [y/N] "
    read -r ans
    case "$ans" in y|Y|yes|YES) ;; *) die "中止しました" ;; esac
  else
    die "非対話実行です。置き換えるなら --force を付けてください"
  fi
fi

run mkdir -p "$OUT"

for s in "${SKILLS[@]}"; do
  [ -d "$SRC/$s" ] || die "正本が無い: $SRC/$s"
  say "[$s]"

  # 1. 正本をまるごとコピー (SKILL.md と既存の references/ など)
  run rm -rf "$OUT/$s"
  run cp -r "$SRC/$s" "$OUT/$s"

  # 2. リファレンスを同梱
  for row in "${BUNDLE[@]}"; do
    IFS='|' read -r sk from to _a _b <<<"$row"
    [ "$sk" = "$s" ] || continue
    src_path="$REPO_ROOT/$from"
    if [ ! -e "$src_path" ]; then
      say "  ! 同梱元が見つからない (スキップ): $from"
      continue
    fi
    if [ "$to" = "." ]; then dst="$OUT/$s/references"; else dst="$OUT/$s/references/$to"; fi
    run mkdir -p "$dst"
    if [ -d "$src_path" ]; then
      run cp -r "$src_path"/. "$dst/"
      n=$(find "$src_path" -type f | wc -l)
      say "  + $from → references/${to#.}  ($n files)"
    else
      run cp "$src_path" "$dst/"
      say "  + $from → references/${to#.}"
    fi
  done

  # 3. SKILL.md 内のパスを references/ 起点へ書き換え
  if [ "$DRYRUN" = 0 ]; then
    for row in "${BUNDLE[@]}"; do
      IFS='|' read -r sk _f _t before after <<<"$row"
      [ "$sk" = "$s" ] || continue
      # | は BUNDLE の区切りなので sed の区切りには # を使う
      sed -i "s#${before}#${after}#g" "$OUT/$s/SKILL.md"
    done
    # 同梱後は「krkrz_dev リポジトリルート相対」ではなくスキル内相対になる
    sed -i 's#krkrz_dev リポジトリルート相対#このスキルディレクトリ相対#g' "$OUT/$s/SKILL.md"
    # 4. 配布版メモを frontmatter 直後 (2 つ目の --- の後) へ挿入
    awk -v note="$NOTE" '
      BEGIN { n = 0; done = 0 }
      /^---$/ { n++; print; if (n == 2 && !done) { print note; done = 1 }; next }
      { print }
    ' "$OUT/$s/SKILL.md" > "$OUT/$s/SKILL.md.tmp" && mv "$OUT/$s/SKILL.md.tmp" "$OUT/$s/SKILL.md"
  fi
  say "  ✓ $OUT/$s"
done

# --dist のときはプラグインとして成立させるマニフェストも出す
if [ "$MODE" = dist ] && [ "$DRYRUN" = 0 ]; then
  mkdir -p "$DEST/.claude-plugin" "$DEST/plugins/$PLUGIN_NAME/.claude-plugin"
  cat > "$DEST/plugins/$PLUGIN_NAME/.claude-plugin/plugin.json" <<JSON
{
  "name": "$PLUGIN_NAME",
  "version": "0.1.0",
  "description": "吉里吉里Z (krkrz) 開発用スキル集 — 本体クラス API / TJS2 言語 / Elements UI / REPL 駆動 / ブラウザ UI",
  "author": { "name": "Go Watanabe" },
  "repository": "https://github.com/wamsoft/krkrz_dev",
  "keywords": ["kirikiri", "krkrz", "tjs2", "game-engine"]
}
JSON
  cat > "$DEST/.claude-plugin/marketplace.json" <<JSON
{
  "name": "$MARKETPLACE_NAME",
  "description": "吉里吉里Z (krkrz) 開発用スキルの配布元",
  "owner": { "name": "Go Watanabe" },
  "plugins": [
    {
      "name": "$PLUGIN_NAME",
      "description": "吉里吉里Z (krkrz) 開発用スキル集",
      "source": "./plugins/$PLUGIN_NAME"
    }
  ]
}
JSON
  say ""
  say "プラグインマニフェストを生成しました:"
  say "  $DEST/.claude-plugin/marketplace.json"
  say "  $DEST/plugins/$PLUGIN_NAME/.claude-plugin/plugin.json"
  say ""
  say "この内容を git リポジトリとして push すると、受け取る側は次で導入できます:"
  say "  /plugin marketplace add <owner>/<repo>"
  say "  /plugin install $PLUGIN_NAME@$MARKETPLACE_NAME"
fi

say ""
say "完了。${#SKILLS[@]} スキルを $OUT へ配置しました。"
[ "$MODE" = user ] && say "以降どのリポジトリで作業していてもこれらのスキルが使えます。"
exit 0
