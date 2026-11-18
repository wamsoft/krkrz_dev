#!/usr/bin/env bash
#
# krkrz_dev のスキル一式を ChatGPT (カスタム GPT / プロジェクト) 用のパックにまとめる。
#
#   bash tools/skills/pack_chatgpt.sh                 # → build/chatgpt-pack/
#   bash tools/skills/pack_chatgpt.sh --out <dir>     # 出力先を指定
#   bash tools/skills/pack_chatgpt.sh --zip           # <出力先>.zip も作る
#
# install.sh で自己完結形のスキルを一時フォルダへ組み立ててから、
# pack_chatgpt.py でナレッジファイルへ束ね直す。
#
set -euo pipefail

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "$HERE/../.." && pwd)
OUT="$REPO_ROOT/build/chatgpt-pack"
ZIP=()

while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT="${2:-}"; [ -n "$OUT" ] || { echo "error: --out にパスが必要" >&2; exit 1; }; shift 2 ;;
    --zip) ZIP=(--zip); shift ;;
    -h|--help) sed -n '3,10p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'; exit 0 ;;
    *) echo "error: 不明な引数: $1" >&2; exit 1 ;;
  esac
done

PY=python3
command -v "$PY" >/dev/null 2>&1 || PY=python
command -v "$PY" >/dev/null 2>&1 || { echo "error: python が見つからない" >&2; exit 1; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

bash "$HERE/install.sh" --project "$TMP" --force >/dev/null
"$PY" "$HERE/pack_chatgpt.py" "$TMP/.claude/skills" "$OUT" "${ZIP[@]}"
