# ドキュメント整理 残作業メモ

`mkdocs build --strict` は警告ゼロで通り、`diff_docs.py` も 0/0。
品質向上のため順次潰したいもののみ残す。

---

## TODO スタブ埋め (61 件 / 10 ファイル)

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

- A. 旧 `krkrz-documents` (XML リファレンス) を別ロケーションに clone して
  該当 description を grep で引いてくる
  (`https://github.com/krkrz/krkrz-documents.git`)
- B. C++ 実装を読んで書き起こす (実装が SSOT に最も近い)
- C. 当面 TODO 維持
