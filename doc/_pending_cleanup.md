# ドキュメント整理 残作業メモ

2026-04-26 時点の未完了タスク一覧。`mkdocs build --strict` は通り、
`diff_docs.py` は 0/0 のため必須作業ではないが、品質向上のために
順次潰したいもの。

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

## 3. GitHub Pages 展開

`.github/workflows/docs-pages.yml` で **設定済み**。`develop` / `master`
への push (doc/, mkdocs.yml, requirements.txt 変更時) で
`mkdocs build --strict` → `gh-pages` に自動デプロイ。
URL: <https://wamsoft.github.io/krkrz_dev/>

未 push の 11 コミットを push すれば最新版が反映される。

**残作業候補**:
- リポジトリ Settings → Pages で source = GitHub Actions が選択済か確認
  (環境 `github-pages` が必要)
- 現状サイトに繋がっているか初回ビルド後に動作確認
- 必要なら custom domain / robots.txt / 検索インデックス可否の調整

---

## 4. 旧ドキュメント (`document/` ディレクトリ) の削除

過去の HTML/XML ベースのドキュメント原本。`doc/` (mkdocs SSOT) への
変換が完了しているので、参照されていなければ削除可能。

| パス | 内容 | 状況 |
|---|---|---|
| `document/kirikiriz/j_in/*.xml` | 旧 XML リファレンス (TJS クラス + ガイド) | `xml2manual.py` `xml2md.py` の入力。初回変換後は不要のはずだが、TODO スタブ埋め (上記 1) で原稿引用元として再利用可能なので **当面残す** のが安全 |
| `document/kirikiriz/j/` | 上記 XML から perl で生成された HTML | 既に doc/ に取り込み済み。**削除可** |
| `document/misc_markdown/` | 周辺情報 markdown 群 | commit `894151a` で `doc/topics/` に取込済み。**削除可** |

`tools/docgen/xml2manual.py` `xml2md.py` `xml2tjs2.py` `html2spec.py`
は変換済みなので、原本を削除するならこれらのツールも撤去候補。
ただし、TODO 埋めで XML を grep する用途が残っていれば併存。

**判断ポイント**:
- (a) 即削除 (`document/` 全体 + `tools/docgen/xml2*.py` `html2spec.py`)
- (b) `document/kirikiriz/j/` と `misc_markdown/` のみ削除 (XML は残す)
- (c) 当面全保持 (TODO 埋め完了後に再検討)

---

## 5. Wiki 同期 (`docs-wiki.yml`) の撤去

`.github/workflows/docs-wiki.yml` + `tools/docgen/sync_wiki.py` は、
`doc/` を GitHub Wiki にフラット展開する仕組み。
(`doc/reference/Layer.md` → `Class.Layer.md` など)

経緯:
- `189c7cd` (doc: 旧XMLリファレンスをMarkdown化し doc/ へ移行) で導入
- `0a0372d` `4b8bd8e` で workflow 微調整

Pages を canonical な配信先にするなら Wiki は重複。判断:
- **撤去する場合**:
  1. `.github/workflows/docs-wiki.yml` 削除
  2. `tools/docgen/sync_wiki.py` 削除
  3. (任意) Wiki 上の生成済みページ (`Class.*` / `Guide.*` / `Home.md`
     / `_Docs-Diff-Report.md`) を一掃
  4. リポジトリ Settings → Wiki を無効化するかは別判断
- **残す場合**: Pages との二重配信を許容、検索動線を 2 系統用意

---

## 6. 未 push コミット (11 件)

`origin/develop` から 11 コミット先行:

```
e5c5d98 docs: SDLDrawDevice / OGLDrawDevice の manual.tjs を追加
dc7f819 docgen: scan_tjs.py がランタイム登録メンバを検出するよう改善
7f5d529 docs: Android 関連と C++ コードに無い記述を削除
b728a16 docs: multi_platform_design からクラス・メンバを取込
3cfb4d4 docgen: multi_platform_design 取込ツール追加 + event 構文対応
894151a docs: misc_markdown を doc/topics/ に取込 + nav 微修正
7c6bc1e docs: クラスリファレンスを独立タブに分離 + nav 整理
1ab3387 docs: TJS2 言語リファレンスと仕様書 HTML を取込
efdb856 docs: 残作業の優先タスクを片付け
05fc2e9 update submodules: httprequest / layerExDraw / psdfile
d2f3f6c docs: manual.tjs を SSOT 化、mkdocs Pages 対応
```

push すると Pages 自動ビルド + Wiki 同期 (現状残っていれば) が走る。
Wiki を先に撤去するならこの順で:
1. `docs-wiki.yml` 削除コミット → push (Wiki 同期はこの時点で停止)
2. 残りまとめて push

---

## 優先度感

1. **5 (Wiki 同期撤去)** — Pages を canonical にするなら早めに方針確定。push 前に決めると history が綺麗
2. **2 (リンク警告)** — 機械的作業で潰せる、サイト品質に直結
3. **4 (旧ドキュメント削除)** — 1 完了後の再判断が無難
4. **1 (TODO 埋め)** — 労力大、ユーザ可視の影響が一番大きい
5. **3 (Pages 設定確認)** — push 後に動作確認するだけ
6. **6 (push)** — 上記方針が固まってから
