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

- クラス未作成: 0
- 未記載メンバー合計: 1
- コードに無いメンバー合計: 5

## BasicDrawDevice

- manual: `doc/manual/Window.BasicDrawDevice.manual.tjs`
- code: `src/core/win32/visual/BasicDrawDevice.cpp`

### コードに存在しないメンバー（要確認）
- [ ] `onDisplayRotate`

## System

- manual: `doc/manual/System.manual.tjs`
- code: `src/core/common/base/SystemIntf.cpp`

### 未記載メンバー
- [ ] `isAndroid` (property)

### コードに存在しないメンバー（要確認）
- [ ] `exceptionHandler`
- [ ] `onActivate`
- [ ] `onDeactivate`

## Window

- manual: `doc/manual/Window.manual.tjs`
- code: `src/core/common/visual/WindowIntf.cpp`

### コードに存在しないメンバー（要確認）
- [ ] `onHintChanged`

