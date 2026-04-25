# ドキュメント整理 残作業メモ

2026-04-26 時点の未完了タスク一覧。`mkdocs build --strict` は通り、
`diff_docs.py` は 0/0 のため必須作業ではないが、品質向上のために
順次潰したいもの。

> **更新 (2026-04-26)**: カテゴリ 3/4/5 (Pages 確認、旧 document/ 削除、
> Wiki 同期撤去) は実施済み。残るのは 1 (TODO スタブ) と 2 (リンク警告)、
> および 6 (push) のみ。

---

## 1. TODO スタブ埋め (61 件 / 10 ファイル)

C++ にバインドはあるが `manual.tjs` の本文が `TODO: xxx の説明` のみの
プレースホルダ。SSOT 上は宣言だけある状態なので `diff_docs` には出ない。

| ファイル | 件数 | メンバ |
|---|---|---|
| `Storages.manual.tjs` | 18 | addCacheTargetExtension, clearArchiveCache, clearCache, clearFastCache, clearOldCache, commitSavedata, deleteFile, dirlist, dirtree, isCacheLoading, isExistentDirectory, isFastCacheLoading, lastModifiedFileTime, moveFile, requestCache, requestFastCache, rollbackSavedata, setCacheMaxSize |
| `Window.manual.tjs` | 12 | enableTouchMouse, innerSunken, layerEventTarget, layerLeft, layerTop, layerTreeOwnerInterface, mouseCursor, showScrollBars, beginMove, findFullScreenCandidates, requestUpdate, setLayerPos |
| `System.manual.tjs` | 9 | exitOnNoWindowStartup, isGeneric, licenseText, processorNum, touchDevice, addFont, clearGraphicCache, getJoypadType, system |
| `WaveSoundBuffer.manual.tjs` | 6 | enabledVideoStream, numberOfVideoStream, onCallbackCommand, currentDevice, getDeviceList, setPos |
| `BitmapLayerTreeOwner.manual.tjs` | 6 | bitmap, dirtyRect, focusedLayer, isUpdated, layerEventTargetInterface, update |
| `VideoOverlay.manual.tjs` | 3 | posX, posY, posZ |
| `Layer.manual.tjs` | 3 | nodeFocusable, dump, releaseTouchCapture |
| `Font.manual.tjs` | 2 | defaultFaceName, faceIsFileName |
| `Scripts.manual.tjs` | 1 | dumpStringHeap |
| `Debug.manual.tjs` | 1 | prettyPrint |

埋め方の選択肢:
- A. 旧 `document/kirikiriz/j_in/classes/f_*.xml` から該当 description を grep して引いてくる
- B. C++ 実装を読んで書き起こす (実装が SSOT に最も近い)
- C. 当面 TODO 維持

---

## 2. mkdocs build の INFO リンク警告 (18 件)

`mkdocs build --strict` は通るが、内部リンクが解決していない箇所:

### 未解決の相対リンク (10 件)

旧スタイルの ".md なし" 相対リンク。`guide/<name>.md` に書き換える。

| 出元 | 壊れているリンク | 正しい先 |
|---|---|---|
| `reference/Bitmap.md` | `TPC` | `guide/TPC.md` |
| `reference/Layer.md` | `GraphicSystem`, `TPC` | `guide/GraphicSystem.md`, `guide/TPC.md` |
| `reference/SoundBuffer.md` | `LoopTuner` | `guide/LoopTuner.md` |
| `reference/WaveSoundBuffer.md` | `LoopTuner` | `guide/LoopTuner.md` |
| `reference/System.md` | `CommandLine`, `ColorCodes`, `Startup`, `Controller` | `guide/CommandLine.md` ほか |
| `specification/fileformat.md` | `../../src/plugins/win32/addFont/` | リポ内ソースへの相対リンク; mkdocs では解決不可。GitHub URL に書き換えるか除去 |

直す場所は **manual.tjs / spec md の本文**。生成された `doc/reference/*.md`
を直接編集しても次の `tjsdoc.py` 実行で上書きされるので注意。

### 存在しないアンカーへのリンク (8 件)

| 出元 | リンク先 | 状況 |
|---|---|---|
| `reference/Console.md` | `Debug.md#console` | Debug.md を分割した名残 |
| `reference/Controller.md` | `Debug.md#controller` | 同上 |
| `reference/Rect.md` | `Rect.md#topt` | 廃止 API へのリンク |
| `reference/Window.md` | `Window.md#setmixsize` | 廃止 API へのリンク |
| `specification/index.md` | `#tjs2spec` | アンカー再定義漏れ |
| `specification/graphics.md` | `#affine`, `#gamma`, `#glayscale` | アンカー再定義漏れ |

manual.tjs / spec md から該当 `@see` / リンクを除去するか、参照先に
アンカーを追加する。

---

## 3. GitHub Pages 展開 [DONE]

`.github/workflows/docs-pages.yml` で **設定済み**。`develop` / `master`
への push (doc/, mkdocs.yml, requirements.txt 変更時) で
`mkdocs build --strict` → `gh-pages` に自動デプロイ。
URL: <https://wamsoft.github.io/krkrz_dev/>

push 後に動作確認。リポジトリ Settings → Pages で source = GitHub Actions
が選択されている必要あり (環境 `github-pages`)。

---

## 4. 旧ドキュメント (`document/` ディレクトリ) の削除 [DONE]

両 submodule (`document/kirikiriz`, `document/misc_markdown`) を
deinit + git rm で撤去 (commit に含まれる)。同時に入力源を失った
コンバータツール `tools/docgen/xml2manual.py` `xml2md.py`
`xml2tjs2.py` `html2spec.py` と Makefile の `docs-convert` ターゲット
も削除。CLAUDE.md / tools/docgen/README.md の document/ 言及も更新。

XML リファレンスを再度参照したくなった場合は
`https://github.com/krkrz/krkrz-documents.git` を別ロケーションに clone
して使用 (リポ本体には組み込まない)。

---

## 5. Wiki 同期 (`docs-wiki.yml`) の撤去 [DONE]

`.github/workflows/docs-wiki.yml` と `tools/docgen/sync_wiki.py` を
削除 (Pages を canonical な配信先とするため)。Makefile の
`docs-wiki-test` ターゲット + `DST` 変数も撤去。

Wiki 上に残っている生成済みページ (`Class.*` / `Guide.*` / `Home.md`
/ `_Docs-Diff-Report.md`) は次回 push 後も自動更新されないため、必要なら
Wiki 側で個別削除する。リポジトリ Settings → Wiki 機能の有効/無効は
別判断。

---

## 6. 未 push コミット

`origin/develop` 先行コミットを `git push` する。push すると
`docs-pages.yml` が自動ビルドして Pages を更新する。
(`docs-wiki.yml` は撤去済みなので Wiki への影響はない)

---

## 残優先度感

1. **2 (リンク警告 18 件)** — 機械的作業で潰せる、サイト品質に直結
2. **1 (TODO スタブ 61 件)** — 労力大、ユーザ可視の影響が一番大きい

3/4/5/6 は完了 or 進行中。
