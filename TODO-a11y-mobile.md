# 読み上げ (スクリーンリーダー) の iOS / Android 対応 計画

デスクトップ (Windows / macOS / Linux) で動いている読み上げ対応を、iOS (VoiceOver) と
Android (TalkBack) でも OS へ届くようにする計画。索引は [TODO.md](TODO.md)。
今の口と設計は [doc/specification/accessibility.md](doc/specification/accessibility.md)
(Elements 側は `src/core/external/elements/docs/accessibility.md`、以下「本体設計」)。

状態: **段階 0〜2 を実装 (2026-10-22)**。iOS は Simulator、Android は実機 2 台で確認 (フォーカス枠・announce の不具合も修正済み)。段階 3 (既定 ON) も実施 (2026-10-22、サイズの増分は下の表)。確認の記録は §7。

## 0. 結論

- **できる**。Elements が取ってくる accesskit-c 0.23.1 の prebuilt に、Android
  (`lib/android/arm64-v8a`・`x86_64`) と iOS (`lib/ios/arm64`、`lib/ios-simulator/arm64`・`x86_64`)
  の static / shared ライブラリと、C API (`accesskit.h` の `accesskit_android_*` / `accesskit_ios_*`)
  が入っている。Android の ABI は krkrz_android の `abiFilters` (arm64-v8a / x86_64) と一致する。
- 意味ツリー (L0〜L2)、`Agent.a11yTree` / `announce` / 読み上げログ、krkrz 側の slot 合成と
  「AT の操作をメインスレッドへ回す」仕組み (`OnA11yRequest` → `DrainA11yRequests`) はそのまま使える。
  足りないのは OS への接続 (L3 = `accesskit_host`) と、外枠リポジトリ側の配線だけ。
- iOS は C++ 側だけで閉じる (SDL の UIView に subclassing adapter を付ける)。
  Android は Java の小さな接着コードが要る (SDL の `SDLSurface` に
  `AccessibilityNodeProvider` を生やす)。どちらも accesskit-c 同梱の例
  (`examples/sdl/`、Android は `examples/sdl/android/`) と同じ形にできる。
- 規模は Elements ~200 行 + krkrz ~80 行 + 外枠 (Java ~120 行 / CMake 数行) の見込み。
  実機でしか確かめられない点 (座標の単位、live region、スレッド) が多いので、
  先に Phase 0 (試作) で確かめてから本実装に入る。

## 1. 今の状態 (2026-10-22 時点)

| 場所 | 内容 |
|---|---|
| `src/core/CMakeLists.txt` (`KRKRZ_USE_A11Y`) | 既定 ON は Windows / Darwin / Linux のみ。`ANDROID` / `IOS` / `EMSCRIPTEN` は既定 OFF。option なので `-DKRKRZ_USE_A11Y=ON` は渡せるが、渡すと下のとおりビルドが通らない |
| krkrz_ios `CMakeLists.txt` | `option(KRKRZ_USE_A11Y "" OFF)` を明示している |
| krkrz_android | 何も指定していない (core の既定 = OFF) |
| Elements `lib/src/a11y/accesskit_host.cpp` | `_WIN32` / `__APPLE__` (= macOS の NSWindow 前提) / `ELEMENTS_A11Y_UNIX` (AT-SPI、`__ANDROID__` は除外済み) の 3 系統。Android は `#else` に落ちて adapter が作られない (OS に出ないだけで動く)。**iOS は `__APPLE__` が立つので macOS 用の `accesskit_macos_*` 呼び出しがコンパイルされ、ビルドが通らない** |
| krkrz `common/visual/elements/ElementsDialogManager.cpp` (座標の換算 `to_os`) | `#if defined(__linux__)` → ウィンドウ座標、`#elif defined(__APPLE__)` → ポイント × `native_scale()`。**Android は `__linux__` が立つので AT-SPI 用の分岐に入ってしまう**。iOS は macOS 用の分岐に入る |
| accesskit-c の `accesskit-config.cmake` | OS 判定は `ANDROID` → `android` + `ANDROID_ABI`、`CMAKE_SYSTEM_NAME=iOS` → `CMAKE_OSX_SYSROOT` に `iphonesimulator` を含めば `ios-simulator`、それ以外 `ios`。arch は `CMAKE_OSX_ARCHITECTURES`。リンク依存は android = `android log`、ios = `UIKit Foundation CoreFoundation objc c++` を自分で付ける。どちらも外枠の今の configure (krkrz_ios の Makefile は `CMAKE_OSX_SYSROOT` / `CMAKE_OSX_ARCHITECTURES` を渡している) で正しく選ばれるはず |

## 2. OS ごとにホストがすること

### 2.1 iOS (VoiceOver)

C API: `accesskit_ios_subclassing_adapter_new(UIView*, activation, action, deactivation)`
(または `..._for_window(UIWindow*)` = root view controller の view に付ける)、
`..._update_if_active(factory)` → `accesskit_ios_queued_events_raise`、`..._free`。
非 subclassing 版 (`accesskit_ios_adapter_*`) は UIView の `accessibilityElements` 等を
ホストが override する前提なので使わない (SDL の view クラスを書き換えずに済む subclassing 版にする)。

- **付ける view**: `SDL_PROP_WINDOW_UIKIT_WINDOW_POINTER` の UIWindow →
  `rootViewController.view`。SDL3 の UIKit では、GL / Metal の view を作った時点で
  `SDL_uikitview -setSDLWindow:` が view controller の `view` を**差し替える**
  (`src/video/uikit/SDL_uikitview.m`)。そのため、DrawDevice (= GL view) ができた後に付け、
  view が差し替わったら付け直す (DrawDevice 切替 `ogl` ↔ `sdl` で起こりうる)。
  `for_window` は「root view controller に view が無いと panic」と書かれているので、
  view の有無を確かめてから呼ぶ。
- **スレッド**: 全ハンドラはメインスレッドで呼ばれる (C API の記載)。krkrz の SDL3 は
  `SDL_MAIN_USE_CALLBACKS` で iOS でもメインスレッドで回るので、Windows / macOS と同じく
  `ui_thread_activation = true` (activation の場で snapshot を取る) でよい。
  アクションも同じスレッドで来るので、krkrz の `OnA11yRequest` はその場で流す。
- **フォーカス / 外接矩形**: macOS の `update_view_focus_state` / Linux の
  `set_root_window_bounds` に当たる関数は iOS には無い (アプリは常に全画面)。
  `window_focus` / `window_bounds` は何もしない。
- **座標**: 要確認 (Phase 0)。macOS と同じく「物理ピクセルを渡すと AccessKit がポイントに直す」
  なら、`native_scale()` を `UIView.contentScaleFactor` (または `UIScreen.scale`) にすれば
  krkrz 側の `to_os` は macOS と同じ式で済む。ポイントのまま渡す仕様なら `native_scale()` = 1。
- **タッチ**: VoiceOver が有効な間、画面のタッチは VoiceOver のジェスチャになり、
  ゲームには直接届かない (OS の仕様。ダブルタップ = click アクションで届く)。
  AccessKit には `UIAccessibilityTraitAllowsDirectInteraction` を付ける口が無いので、
  タッチで遊ぶ部分は `setGameA11y` / `a11yLayers` で操作できるようにしておく必要がある
  (ガイドに書く)。
- **アプリ側の Objective-C**: subclassing 版なら不要 (`objc_msgSend` で UIWindow →
  rootViewController → view を引けば済む。macOS の `backingScaleFactor` と同じやり方)。

### 2.2 Android (TalkBack)

C API は 2 系統ある。

| | `accesskit_android_adapter` (通常) | `accesskit_android_injecting_adapter` |
|---|---|---|
| 仕組み | ホストの View が `getAccessibilityNodeProvider()` / `onHoverEvent()` を override し、JNI で `create_accessibility_node_info` / `find_focus` / `perform_action` / `on_hover_event` を呼ぶ | 既存の View に `setAccessibilityDelegate` / `setOnHoverListener` を後付けする (C だけで完結しそうに見える) |
| Java | 要る (SDLSurface のサブクラス + native メソッド数個) | Java クラス `dev.accesskit.android.Delegate` を JNI で探す。prebuilt にはこのクラス (dex) が入っていないので、結局アプリ側に Java を足す必要がある。さらに `FindClass` を SDL のスレッドから呼ぶとアプリのクラスが見えない、という JNI の定番の罠もある |
| 判断 | **こちらを使う**。accesskit-c の SDL 例 (`examples/sdl/android/`) がこの形で、手順が確立している | 使わない |

- **付ける View**: `SDLActivity.mSurface` (`SDLSurface`、SurfaceView)。krkrz_android の
  `KrkrzActivity` は `SDLActivity` を継承しているので、`createSDLSurface()` を override して
  サブクラス (`setImportantForAccessibility(YES)` + `getAccessibilityNodeProvider()` +
  `onHoverEvent()`) を返す。`SDLSurface` 自身は touch / generic motion の listener だけを使い、
  hover は触っていない (SDL 3.4 で確認) ので衝突しない。
- **スレッド**: Android のアクセシビリティ呼び出しは **UI スレッド**、krkrz (SDL) は
  **SDL のスレッド**で動く。そのため:
  - adapter (`accesskit_android_adapter*`) は UI スレッドでだけ触る (例と同じ)。
  - activation (ツリーの初回要求) は UI スレッドから来る → Linux と同じく
    `ui_thread_activation = false` にして、SDL スレッドが最後に push した snapshot を返す。
  - アクション (`perform_action`) も UI スレッドから来る → krkrz の `OnA11yRequest` が
    既にキューに積んでメインスレッドで流す (Linux で使っている経路)。追加の仕事は無い。
  - 更新 (`push()`) は SDL スレッドから起きる → `update_if_active` を UI スレッドで呼ぶ必要が
    あるので、「UI スレッドで更新して」と Java 側へ頼む (`runOnUiThread` → native →
    `accesskit_android_adapter_update_if_active` → `accesskit_android_queued_events_raise(env, host)`)。
    `push()` の「factory が呼ばれなかったら full に戻す」判定は同期で取れなくなるので、
    UI スレッド側のコールバックで行う。
- **active の判定**: Android の adapter には deactivation が無い。TalkBack を切っても
  `a11yActive` が偽に戻らない。Java の `AccessibilityManager.isEnabled()` /
  `addAccessibilityStateChangeListener` で状態を拾って native へ伝える (C++ 側に
  `set_active(bool)` 相当を足す)。
- **座標**: View 内のピクセル (AccessKit が `getLocationOnScreen` を足す)。SurfaceView の
  サイズ = `SDL_GetWindowSizeInPixels` なので、Windows と同じ「ピクセル」系でよい。
  krkrz 側の `to_os` の `__linux__` 分岐から Android を外す。
- **Activity の作り直し**: `mSurface` は `onCreate` で作られ `onDestroy` で null になる。
  adapter は Activity と同じ寿命にし (例と同じ)、host の View は毎回渡される引数を使う
  (グローバル参照を握りっぱなしにしない)。
- **JNI の受け口**: Java のパッケージ名 (`jp.wamsoft.krkrz…`) は外枠のものなので、
  `JNIEXPORT` の関数は外枠に置く (virtualpad / license など既存の静的プラグインと同じ形)。
  krkrz core は JNI 型を受ける素の C 関数 (`TVPA11yAndroid*`) を出し、外枠の JNI 関数が
  それへ転送する。core に Java のクラス名を持ち込まない。

## 3. 変更箇所

### 3.1 Elements (`src/core/external/elements`、別リポジトリ)

- `lib/src/a11y/accesskit_host.cpp`
  - `__APPLE__` の分岐を `ELEMENTS_A11Y_MACOS` (`TARGET_OS_OSX`) と `ELEMENTS_A11Y_IOS`
    (`TARGET_OS_IOS`) に分ける (`accesskit.h` が `ACCESSKIT_MACOS` / `ACCESSKIT_IOS` を
    同じ条件で立てるので、それに合わせる)。`attach_sdl` の `"SDL3Window"` focus forwarder は
    macOS だけにする。
  - iOS: `impl` に `accesskit_ios_subclassing_adapter*`。`attach` (UIView*)、`push`
    (`update_if_active` + `raise`)、`detach`、`native_scale` (contentScaleFactor)。
    `attach_sdl` は `SDL_PROP_WINDOW_UIKIT_WINDOW_POINTER` から view を引く。
    view の差し替えに追従する `reattach()` (または `attach_sdl` をもう一度呼べる作り)。
  - Android: `impl` に `accesskit_android_adapter*`。UI スレッドから呼ぶ入口を
    公開する (`android_create_node_info(env, host, id)` / `android_find_focus` /
    `android_perform_action(env, host, id, action, bundle)` / `android_on_hover(env, host, action, x, y)` /
    `android_update(env, host)`)。`push()` は「UI スレッドで `android_update` を呼んで」と
    ホストへ頼むコールバック (`set_request_update(std::function<void()>)`) を呼ぶ。
    `ui_thread_activation = false`、`set_active(bool)` を足す。
  - ヘッダ `include/elements/a11y/accesskit_host.hpp` に上の宣言 (JNI 型は
    `#if defined(__ANDROID__)` の中だけ、他 OS の利用者に `jni.h` を見せない)。
- `lib/CMakeLists.txt`: 変更は不要の見込み (`accesskit-config.cmake` がリンク依存を付ける)。
  `BUILD_SHARED_LIBS` が ON の外枠だと shared 版 (`libaccesskit.so` / `.dylib`) を選び
  同梱が要るので、static を強制する (`accesskit-static` を直接リンク) かを決める。
- `docs/accessibility.md`: §3.2 の宣言、§3.4 の SDL3 ホストに iOS / Android の行、
  Phase 0 の結果 (§3.2.x に iOS / Android の節)、§7「モバイルは範囲外」の行を書き換え。

### 3.2 krkrz core (`src/core`)

- `CMakeLists.txt`: `KRKRZ_USE_A11Y` の既定判定に `IOS` / `ANDROID` を (実機確認が済んだ段階で)
  入れる。それまでは外枠が `-DKRKRZ_USE_A11Y=ON` を渡したときだけ有効。
- `common/visual/elements/ElementsDialogManager.cpp` の `to_os`: `__linux__` → `__linux__ && !__ANDROID__`、
  `__APPLE__` の分岐が iOS でも正しいか (Phase 0 の結果次第)。iOS の view 差し替え
  (DrawDevice 切替) で `accesskit_host` を付け直す (`UpdateA11yHost` を view の変化でも回す)。
- 新規 `sdl3/environ/android/A11yAndroid.cpp` (仮、`ANDROID && KRKRZ_HAS_A11Y` のときだけ
  `sources.cmake` に入れる): `extern "C"` の `TVPA11yAndroid{CreateNodeInfo,FindFocus,PerformAction,OnHover,Update,SetEnabled}`。
  ElementsDialogManager の `a11y_host` を引いて Elements の入口へ渡す。更新の依頼は
  `SDL_GetAndroidJNIEnv()` + 外枠が登録した Java の static メソッドを呼ぶ
  (メソッドの `jclass` は UI スレッドから最初に呼ばれたときにグローバル参照で覚える。
  SDL スレッドで `FindClass` しない)。
- `doc/specification/accessibility.md` (+ `.en.md`): 「使い方」のビルド行と §7 の段階を更新。
  `doc/guide/Accessibility.md` (+ en): 対応 OS と、VoiceOver 中はタッチがゲームに届かない注意。

### 3.3 外枠

- **krkrz_ios**: `option(KRKRZ_USE_A11Y "" OFF)` を `ios-config.json` のキー (例 `"a11y": true`) で
  切り替えられるようにし、実機確認後に既定 ON。Objective-C の追加は無い見込み。
- **krkrz_android**:
  - `app-config.json` の `cmake` 節に任意の CMake 変数を書ける口を足す (例
    `"options": {"KRKRZ_USE_A11Y": "ON"}` → `generateMyappCmake` が `set(... CACHE ...)` を書く)。
    または `build.gradle` の `arguments` に直接足す。
  - Java: `KrkrzActivity.createSDLSurface()` の override と、SDLSurface のサブクラス
    (`getAccessibilityNodeProvider` / `onHoverEvent`)、`requestAccessibilityUpdate()`
    (`runOnUiThread` → native)、`AccessibilityManager` の状態リスナー。
    `KRKRZ_USE_A11Y` が OFF のビルドでは native が無いので、native 側から
    「使える」と登録されたときだけ provider を返す (UnsatisfiedLinkError を避ける)。
  - JNI: 静的プラグイン (例 `app/src/main/cpp/a11y/JniBridge.cpp`) で `JNIEXPORT` →
    `TVPA11yAndroid*` へ転送。`app-config.json` の `plugins` / `staticPlugins` に足す。
  - ProGuard / R8: native メソッドを持つクラスと provider を keep する。
- **krkrz_web / krkrz_linux**: 変更なし (web は別系統、linux は既存の AT-SPI)。

## 4. 段階

| 段階 | 内容 | 完了条件 |
|---|---|---|
| 0. 試作 | accesskit-c の `examples/sdl` を SDL3 に直したもの (Elements なし) を両 OS で動かす。確かめること: iOS の座標単位 (ポイントかピクセルか)、iOS で view を差し替えたときの振る舞い、Android の live region が TalkBack で読まれるか、iOS の live region (announce) が VoiceOver で読まれるか、slider の increment / decrement の操作 (Android = スクロール系アクション、iOS = 上下スワイプ)、文字入力欄の TextRun がどこまで効くか | 結果を Elements 本体設計 §3.2.x に追記 |
| 1. iOS | Elements の iOS 分岐 + krkrz の `to_os` / 付け直し + krkrz_ios の切替 | §5 の確認が iOS で通る |
| 2. Android | Elements の Android 入口 + krkrz の `A11yAndroid.cpp` + krkrz_android の Java / JNI / 設定 | §5 の確認が Android で通る |
| 3. 既定 ON | core の既定判定と外枠の既定を ON に。exe / so のサイズ増を記録 (Android arm64 の `libaccesskit.a` は約 16MB、リンク後の増分は未計測) | ドキュメント・ガイド・スキル更新 |

1 と 2 は互いに依存しない (Elements の同じファイルを触るので、同時に進めるなら順に取り込む)。

### 段階 3 の判断材料: サイズの増分 (2026-10-22 計測)

`KRKRZ_USE_A11Y` の ON / OFF で同じ版を 2 回ビルドして比べた (計測用の一時設定はコミットしていない)。

| 対象 | OFF | ON | 増分 |
|---|---|---|---|
| Android `libkrkrz.so` arm64-v8a (Release、strip 後) | 14,858,680 B (14.17 MB) | 15,495,336 B (14.78 MB) | +636,656 B (+0.61 MB / +4.3%) |
| Android `libkrkrz.so` x86_64 (Release、strip 後) | 16,291,024 B (15.54 MB) | 16,998,864 B (16.21 MB) | +707,840 B (+0.68 MB / +4.3%) |
| Android APK (arm64-v8a + x86_64、圧縮後) | 76,656,485 B (73.11 MB) | 77,999,973 B (74.39 MB) | +1,343,488 B (+1.28 MB / +1.8%) |
| Windows `krkrz64.exe` (SDL 版 x64、Release) | 15,248,384 B (14.54 MB) | 15,546,880 B (14.83 MB) | +298,496 B (+0.28 MB / +2.0%) |
| iOS (実機 arm64、Release) | | | Mac で計測中 |

- Android: Play のダウンロード (AAB の ABI 分割) では、端末に届くのはその ABI 分だけなので、増分は APK の半分程度の見込み (AAB は作っていない)。armeabi-v7a は外枠が作っておらず、AccessKit も Android の 32bit ARM 版を同梱していない。
- Windows: ON 側は少し前の同じ系列のビルド (読み上げ以外の差は無い範囲)。Linux / macOS は手元に比べられるビルドが無く未計測。
- 参考: AccessKit の prebuilt の static ライブラリ自体は Android 15.9 MB / iOS 8.9 MB / Windows (MSVC x64) 8.8 MB / macOS 9.6 MB / Linux x86_64 44.4 MB だが、リンク後に残るのは上の増分だけ。


## 5. 実機での確かめ方

共通の題材はコアデモ `data/a11y` と `data/elements_gallery`。`Agent.a11yTree()` の
出力 (REPL web が使えるビルドなら `.a11y`) と、OS 側に見えるツリーを突き合わせる。

| 項目 | iOS | Android |
|---|---|---|
| ツリーの機械的な確認 | シミュレータ + Xcode の Accessibility Inspector (名前・ロール・値・矩形、Activate / Increment の実行)。XCUITest の `app.debugDescription` でも階層が取れる | `adb shell uiautomator dump` (provider の仮想ノードも出る) / Accessibility Scanner |
| 読み上げ | 実機の VoiceOver (シミュレータに VoiceOver は無い) | エミュレータ (Play 入りイメージ) または実機の TalkBack。`adb shell settings put secure enabled_accessibility_services ...` で有効化できる |
| 見ること | ダイアログのボタン・チェック・スライダーの名前とロール、フォーカスの追従、ダブルタップで click (`onGameA11yAction` / ダイアログのアクション)、スライダーの増減、モーダル表示中に下が隠れること、`announce` が読まれること、`a11yActive` / `onA11yActiveChanged` (Android は TalkBack の on / off で戻ること)、回転・リサイズ後の矩形、`setGameA11y` / `a11yLayers` のノード | 同左 + バックグラウンド → 復帰、Activity の作り直し |
| 退行 | Windows / macOS / Linux で既存の確認 (accessibility.md 冒頭の「確認」) をやり直す。Elements の `test/a11y_tree_test.cpp` / `test/modal_a11y_test.cpp` | 同左 |

## 6. リスク

- **iOS の view 差し替え**: SDL が view controller の view を替えると subclassing が外れる。
  付け直しの漏れはツリーが消える形で出るので、DrawDevice 切替を確認項目に入れる。
  SDL を上げたとき (`SDL_uikitview` の実装変更) にも壊れうる。
- **スレッド (Android)**: UI スレッドと SDL スレッドの間で、adapter を UI スレッド専用にする
  規律を崩すとクラッシュする。Elements の `mtx` を UI スレッドで長く握らない
  (activation は snapshot を返すだけにする)。
- **AccessKit の C API の変更**: 0.x 系。モバイル部分は特に新しい (accesskit-c の CHANGELOG では
  Android が 0.21.0 = 2026-02、iOS が 0.22.0 = 2026-05 に追加)。prebuilt のバージョン固定は今のまま。
- **サイズ**: Rust の static ライブラリは大きい。Android / iOS ともリンク後の増分を
  段階 3 で計測し、許容できなければ「外枠の設定で OFF」を残す。
- **タッチ操作のゲーム**: VoiceOver / TalkBack 中は直接タッチが届かない。読み上げ対応を
  謳うタイトルは、操作をツリーに載せる作業がスクリプト側に要る (デスクトップより重い)。
- **外枠の Gradle 設定**: `app-config.json` に CMake 変数の口が無い。足す場合は
  スキーマを共有している krkrz_ios / krkrz_linux の `cmake` 節と揃える。

## 7. 実施の記録 (2026-10-22)

### 段階 0 (試作の代わりにソースで確認)

Elements なしの試作アプリは作らず、AccessKit の `adapters/ios` / `adapters/android` のソースを読んで未確認点を詰めた。計画の変更は無し。

- iOS の座標: view 内のピクセル (ポイント × `contentScaleFactor`) を受け、AccessKit が割ってポイントに戻す (`util.rs` の `to_cg_rect`)。`native_scale()` = `contentScaleFactor` で、krkrz の `to_os` は macOS と同じ式。
- iOS: live region → `UIAccessibilityAnnouncementNotification`、増減あり、VoiceOver の on / off で activation / deactivation が来る。入力欄のキャレットはアダプタ未対応。
- Android: View 内ピクセル (+ `getLocationOnScreen`)、live region は `setLiveRegion`、スライダーは `SCROLL_FORWARD` / `BACKWARD`、テキスト選択あり。injecting adapter は prebuilt に dex が無いので使えない (計画どおり)。

### 段階 1 (iOS)

- 確認: Simulator (iPhone 17 / iOS 26.3 / x86_64 / 横向き)、要素は AXe CLI の `axe describe-ui`、操作は macOS 側のアクセシビリティ経由の AXPress / AXIncrement。
- 通ったこと: ビルドとリンク (`lib/ios-simulator/x86_64/static/libaccesskit.a`)。読み上げデモ・elements_gallery の要素の名前 / ロール / 値 / 枠。Activate (セーブ・オートモード・あいさつ) と Increment / Decrement (音量 50% → 60%)。`a11yActive` が接続で 1。DrawDevice を切り替えても要素が消えない (付け直しが効く)。
- 未確認: 実機の VoiceOver の読み上げ、announce の通知そのもの (Simulator では取る手段が無い)、選択肢の list item の操作。
- krkrz_ios: ブランチ `ios-a11y` (origin/main から) にコミット。未 push。

### 段階 2 (Android)

- 確認: 実機 (Android 14)、`uiautomator dump`、REPL (`make repl` と同じ socket)、TalkBack (ユーザーが操作)、Java 側の一時的な記録。
- 通ったこと: ビルドとリンク (`libkrkrz.so` に JNI の口と AccessKit)。読み上げデモのダイアログ・ゲーム側のノードが名前 / ロール / 値 / 枠付きで出る。TalkBack が繋がると `a11yActive` が 1。タッチで項目が読まれ、TalkBack のフォーカスがその項目へ移る (ACTION_ACCESSIBILITY_FOCUS が届く)。node provider へ直接送った ACTION_CLICK (選択肢の決定 → `onGameA11yAction` の click、ボタン)、SCROLL_FORWARD / BACKWARD (音量 50% → 70% → 60%)、パネルのボタンからの announce が動く。
- 直したこと: AccessKit のイベントをロックを握ったまま出していたため、TalkBack のタッチで固まった (ANR)。イベントを送ると Android が同じ UI スレッドで node provider を呼び返すため。イベントはロックを放してから出し、krkrz 側のロックは再帰可にした。AccessKit は ACTION_CLICK を付けるが setClickable しないので、Java 側で clickable を立てる。
- 未解決 (→ 後述の別の実機で解決): TalkBack のフォーカス枠が描かれない (フォーカス自体は移る。ウィンドウごと描き直させても出なかった)。TalkBack のダブルタップはこの端末ではホーム画面でもほとんど効かず、アプリ内のダブルタップ → ACTION_CLICK の経路は実操作では確かめきれていない (ACTION_CLICK を直接送る経路は確認済み)。TalkBack を切ったときに `a11yActive` が 0 へ戻るかは未確認。
- 調べるときの注意: この端末は `log.tag=I` で `Log.d` を捨てる (記録は `Log.w` 以上で出す)。socket の REPL はドットコマンド (`.a11y` 等) を受け付けないので `Agent.a11yTree()` 等の式で見る。

### 段階 2 の続き (別の実機、2026-10-22)

最初の端末 (Android 14) はホーム画面でも TalkBack のダブルタップがほとんど効かず、アプリの問題と切り分けられなかったので、別の Android 14 端末 (TalkBack 17) で確かめ直した。

- 通ったこと: タップで読み上げ、ダブルタップで選択肢の決定・ボタン (押されるのは常にフォーカス中の項目。セーブ / ロードの取り違えは無い)、スライダーは 1 本指の上下スワイプで増減 (TalkBack 中の音量キーは端末の音量)、TalkBack のフォーカス枠、ボタンからの announce が最後まで読まれる (1 回確認)。
- 直したこと:
  - **フォーカス枠が描かれない**: 枠は Android がウィンドウに描くが、SDL の描画面はウィンドウの背面の SurfaceView で、その範囲はウィンドウ側では透明扱いになり、View でない枠は表示されない。外枠に枠を描く透明な View (A11yFocusOverlay) を足した。起動時に足すと描画面のレイアウトが SDL のウィンドウ生成と重なって固まる / GL の初期化で落ちることがあったので、TalkBack が初めてフォーカスを置いたときに足す。
  - **announce が読まれない**: 矩形の無い live region は TalkBack が読まない。Android では 1 ピクセルの矩形を与える (Elements)。
  - **announce が冒頭で切れる**: 押した結果のフォーカス移動と live region の変化が同じ更新で届き、TalkBack はフォーカス移動で読み上げを打ち切る。live region を次の更新に回す (Elements)。最後まで読まれたのは 1 回の確認で、修正後の最初の試行では切れていた (タイミング次第の可能性あり。再現の確認を続ける)。
- 未確認: TalkBack を切ったときに `a11yActive` が 0 に戻るか (切る操作でアプリが背面に回るため、確認の途中でアプリを再起動して状態が消えた)。
- 調べるときの注意: 実行中のアプリを外から `am start` / ランチャーで起動し直すと、SDL は既存のインスタンスを終了させる (状態が消える)。画面が消えているときに起動すると、起動時に固まることがある (SDL の起動タイミングの問題。読み上げとは別)。

### 両 OS で見つかった不具合 (修正済み)

- ゲーム本体の slot (`setGameA11y` / `a11yLayers`) の座標が、ウィンドウの論理面 (inner) と描画面の大きさが違うときにずれていた (iOS 全般、Android のナビゲーションバー分、`-dpiscaling=yes`)。`GetDestRect` が論理面の値なのに描画面のピクセルとして使っていた。ダイアログの配置 (`in_scale` / `in_off`) と同じ換算を入れた。

### 別件 (今回は直さない)

- krkrz_android の左端スワイプのサイドメニュー: TalkBack 中は 1 本指のスワイプが届かない (2 本指なら開く)。TalkBack 利用者向けに別の入口 (例: TalkBack が有効なときだけ出すメニューボタン) があるとよい。

- elements_gallery: ページ切り替えのタブ列が名前の無い slider として、slide_switch が名前の無い switch として出る。Elements のロールと名前の対応の問題で、デスクトップでも同じはず。
- コアデモのギャラリー (メニュー) の項目が読み上げツリーに載っていない。TalkBack 中はメニューからデモを開けない (デモのスクリプト側で setGameA11y / a11yLayers に載せる必要がある)。
- PC (SDL) の読み上げデモ: 音量のスライダーは値が文字列 ("50%") だけで数値が無く、UIA では RangeValue にならない (Value パターンのみ)。Android はスクロールの操作で増減できる。
- WINVER で Tab を押すとゲーム側とパネルの両方のフォーカスが動いたように見えた、という報告: 実キー入力で確かめた範囲では動くのはパネルだけで、ゲーム側の focusedLayer は変わらない。ただしパネルにフォーカスがある間もゲーム側の選択肢は青い強調のままで、パネルのフォーカス表示は見えにくい (見た目の問題の可能性)。

