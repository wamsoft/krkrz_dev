# ドキュメント差分レポート

`tools/docgen/scan_tjs.py` が `src/core` から抽出したメンバー一覧と、
`doc/manual/*.manual.tjs` （SSOT）の宣言を突き合わせた結果です。

- **未記載メンバー**: C++ 側には存在するが manual.tjs に宣言が無いもの。
  対応する `manual.tjs` に `function`/`property` 宣言を追加してください。
- **コードに無いメンバー**: manual.tjs にはあるが C++ バインドには存在しないもの。
  リネーム/廃止を確認し、不要なら `manual.tjs` から削除してください。

更新手順:

1. `python tools/docgen/scan_tjs.py`
2. `python tools/docgen/diff_docs.py`
3. `doc/_missing.md` を見ながら `doc/manual/<Class>.manual.tjs` を編集
4. `python tools/docgen/tjsdoc.py --in doc/manual --in src/plugins` で md 再生成
5. 再度 `diff_docs.py` を走らせ、レポートが空になるまで繰り返す

## サマリー

- クラス未作成: 1
- 未記載メンバー合計: 118
- コードに無いメンバー合計: 5

## BasicDrawDevice

- manual: `doc/manual/Window.BasicDrawDevice.manual.tjs`
- code: `src/core/win32/visual/BasicDrawDevice.cpp`

### コードに存在しないメンバー（要確認）
- [ ] `onDisplayRotate`

## BitmapLayerTreeOwner

- manual: `doc/manual/BitmapLayerTreeOwner.manual.tjs`
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

## Debug

- manual: `doc/manual/Debug.manual.tjs`
- code: `src/core/common/utils/DebugIntf.cpp`

### 未記載メンバー
- [ ] `prettyPrint` (method)

## Font

- manual: `doc/manual/Font.manual.tjs`
- code: `src/core/common/visual/LayerIntf.cpp`

### 未記載メンバー
- [ ] `addFont` (method)
- [ ] `defaultFaceName` (property)
- [ ] `faceIsFileName` (property)

## ImageFunction

- manual: `doc/manual/ImageFunction.manual.tjs`
- code: `src/core/common/visual/ImageFunction.cpp`

### 未記載メンバー
- [ ] `copy9Patch` (method)

## Layer

- manual: `doc/manual/Layer.manual.tjs`
- code: `src/core/common/visual/LayerIntf.cpp`

### 未記載メンバー
- [ ] `dump` (method)
- [ ] `nodeFocusable` (property)
- [ ] `releaseTouchCapture` (method)

## Scripts

- manual: `doc/manual/Scripts.manual.tjs`
- code: `src/core/common/base/ScriptMgnIntf.cpp`

### 未記載メンバー
- [ ] `dumpStringHeap` (method)

## Storages

- manual: `doc/manual/Storages.manual.tjs`
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
- [ ] `lastModifiedFileTime` (method)
- [ ] `moveFile` (method)
- [ ] `requestCache` (method)
- [ ] `requestFastCache` (method)
- [ ] `rollbackSavedata` (method)
- [ ] `setCacheMaxSize` (method)

## System

- manual: `doc/manual/System.manual.tjs`
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

- manual: `doc/manual/VideoOverlay.manual.tjs`
- code: `src/core/common/visual/VideoOvlIntf.cpp`

### 未記載メンバー
- [ ] `enabledVideoStream` (property)
- [ ] `numberOfVideoStream` (property)
- [ ] `onCallbackCommand` (method)

## WaveSoundBuffer

- manual: `doc/manual/WaveSoundBuffer.manual.tjs`
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

- manual: `doc/manual/Window.manual.tjs`
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

## manual.tjs 未作成クラス

- [ ] `NullDrawDevice` — `doc/manual/NullDrawDevice.manual.tjs` を新規作成

