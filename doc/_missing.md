# ドキュメント差分レポート

`tools/docgen/scan_tjs.py` が `src/core` から抽出したメンバー一覧と、
`doc/reference/*.md` の見出しを突き合わせた結果です。

- **未記載メンバー**: C++ 側には存在するが Markdown リファレンスに見出しが無いもの。
  対応する `.md` に `### <name>` 節を追加してください。
- **コードに無いメンバー**: 旧 XML には存在したがバインドからは消えているもの。
  リネーム/廃止を確認し、不要なら `.md` から節を削除してください。

更新手順:

1. `.venv/Scripts/python.exe tools/docgen/scan_tjs.py`
2. `.venv/Scripts/python.exe tools/docgen/diff_docs.py`
3. `doc/_missing.md` を見ながら `doc/reference/<Class>.md` を手編集
4. 再度 `diff_docs.py` を走らせ、レポートが空になるまで繰り返す
5. コミットすると GitHub Actions が Wiki に反映

## サマリー

- クラス未作成: 1
- 未記載メンバー合計: 116
- コードに無いメンバー合計: 5

## BasicDrawDevice

- file: `doc/reference/Window.BasicDrawDevice.md`
- code: `src/core/win32/visual/BasicDrawDevice.cpp`

### コードに存在しないメンバー（要確認）
- [ ] `onDisplayRotate`

## BitmapLayerTreeOwner

- file: `doc/reference/BitmapLayerTreeOwner.md`
- code: `src/core/common/visual/BitmapLayerTreeOwner.cpp`

### 未記載メンバー
- [ ] `bitmap` (property)
- [ ] `clearDirtyRect` (method)
- [ ] `dirtyRect` (property)
- [ ] `fireClick` (method)
- [ ] `fireDisplayRotate` (method)
- [ ] `fireDoubleClick` (method)
- [ ] `fireKeyDown` (method)
- [ ] `fireKeyPress` (method)
- [ ] `fireKeyUp` (method)
- [ ] `fireMouseDown` (method)
- [ ] `fireMouseMove` (method)
- [ ] `fireMouseOutOfWindow` (method)
- [ ] `fireMouseUp` (method)
- [ ] `fireMouseWheel` (method)
- [ ] `fireMultiTouch` (method)
- [ ] `fireRecheckInputState` (method)
- [ ] `fireReleaseCapture` (method)
- [ ] `fireTouchDown` (method)
- [ ] `fireTouchMove` (method)
- [ ] `fireTouchRotate` (method)
- [ ] `fireTouchScaling` (method)
- [ ] `fireTouchUp` (method)
- [ ] `focusedLayer` (property)
- [ ] `height` (property)
- [ ] `isUpdated` (property)
- [ ] `layerEventTargetInterface` (property)
- [ ] `layerTreeOwnerInterface` (property)
- [ ] `onChangeLayerImage` (method)
- [ ] `onDisableAttentionPoint` (method)
- [ ] `onGetCursorPos` (method)
- [ ] `onReleaseMouseCapture` (method)
- [ ] `onResetImeMode` (method)
- [ ] `onResizeLayer` (method)
- [ ] `onSetAttentionPoint` (method)
- [ ] `onSetCursorPos` (method)
- [ ] `onSetHintText` (method)
- [ ] `onSetImeMode` (method)
- [ ] `onSetMouseCursor` (method)
- [ ] `primaryLayer` (property)
- [ ] `update` (method)
- [ ] `width` (property)

## Font

- file: `doc/reference/Font.md`
- code: `src/core/common/visual/LayerIntf.cpp`

### 未記載メンバー
- [ ] `addFont` (method)
- [ ] `defaultFaceName` (property)
- [ ] `faceIsFileName` (property)

## ImageFunction

- file: `doc/reference/ImageFunction.md`
- code: `src/core/common/visual/ImageFunction.cpp`

### 未記載メンバー
- [ ] `copy9Patch` (method)

## Layer

- file: `doc/reference/Layer.md`
- code: `src/core/common/visual/LayerIntf.cpp`

### 未記載メンバー
- [ ] `dump` (method)
- [ ] `nodeFocusable` (property)
- [ ] `releaseTouchCapture` (method)

## Scripts

- file: `doc/reference/Scripts.md`
- code: `src/core/common/base/ScriptMgnIntf.cpp`

### 未記載メンバー
- [ ] `dumpStringHeap` (method)

## Storages

- file: `doc/reference/Storages.md`
- code: `src/core/common/base/StorageIntf.cpp`

### 未記載メンバー
- [ ] `addCacheTargetExtension` (method)
- [ ] `clearArchiveCache` (method)
- [ ] `clearCache` (method)
- [ ] `clearFastCache` (method)
- [ ] `clearOldCache` (method)
- [ ] `commitSavedata` (method)
- [ ] `deleteFile` (method)
- [ ] `dirlist` (method)
- [ ] `dirtree` (method)
- [ ] `getFileProperty` (method)
- [ ] `isCacheLoading` (method)
- [ ] `isExistentDirectory` (method)
- [ ] `isFastCacheLoading` (method)
- [ ] `moveFile` (method)
- [ ] `requestCache` (method)
- [ ] `requestFastCache` (method)
- [ ] `rollbackSavedata` (method)
- [ ] `setCacheMaxSize` (method)

## System

- file: `doc/reference/System.md`
- code: `src/core/common/base/SystemIntf.cpp`

### 未記載メンバー
- [ ] `addFont` (method)
- [ ] `clearGraphicCache` (method)
- [ ] `exitOnNoWindowStartup` (property)
- [ ] `getJoypadType` (method)
- [ ] `isAndroid` (property)
- [ ] `isGeneric` (property)
- [ ] `isWindows` (property)
- [ ] `licenseText` (property)
- [ ] `nullpo` (method)
- [ ] `openGLESVersion` (property)
- [ ] `processorNum` (property)
- [ ] `system` (method)
- [ ] `touchDevice` (property)

### コードに存在しないメンバー（要確認）
- [ ] `exceptionHandler`
- [ ] `onActivate`
- [ ] `onDeactivate`

## VideoOverlay

- file: `doc/reference/VideoOverlay.md`
- code: `src/core/common/visual/VideoOvlIntf.cpp`

### 未記載メンバー
- [ ] `enabledVideoStream` (property)
- [ ] `numberOfVideoStream` (property)
- [ ] `onCallbackCommand` (method)

## WaveSoundBuffer

- file: `doc/reference/WaveSoundBuffer.md`
- code: `src/core/common/sound/WaveIntf.cpp`

### 未記載メンバー
- [ ] `bits` (property)
- [ ] `channels` (property)
- [ ] `currentDevice` (property)
- [ ] `filters` (property)
- [ ] `flags` (property)
- [ ] `freeDirectSound` (method)
- [ ] `frequency` (property)
- [ ] `getDeviceList` (method)
- [ ] `getVisBuffer` (method)
- [ ] `globalFocusMode` (property)
- [ ] `globalVolume` (property)
- [ ] `labels` (property)
- [ ] `onLabel` (method)
- [ ] `pan` (property)
- [ ] `posX` (property)
- [ ] `posY` (property)
- [ ] `posZ` (property)
- [ ] `samplePosition` (property)
- [ ] `setPos` (method)
- [ ] `useVisBuffer` (property)

## Window

- file: `doc/reference/Window.md`
- code: `src/core/common/visual/WindowIntf.cpp`

### 未記載メンバー
- [ ] `beginMove` (method)
- [ ] `displayDensity` (property)
- [ ] `enableTouchMouse` (property)
- [ ] `findFullScreenCandidates` (method)
- [ ] `innerSunken` (property)
- [ ] `layerEventTarget` (property)
- [ ] `layerLeft` (property)
- [ ] `layerTop` (property)
- [ ] `layerTreeOwnerInterface` (property)
- [ ] `mouseCursor` (property)
- [ ] `requestUpdate` (method)
- [ ] `setLayerPos` (method)
- [ ] `showScrollBars` (property)

### コードに存在しないメンバー（要確認）
- [ ] `onHintChanged`

## ドキュメント未作成クラス

- [ ] `NullDrawDevice` — `doc/reference/NullDrawDevice.md` を新規作成

