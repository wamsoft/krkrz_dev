# 画面全体の暗転・クロスフェード (スクリーンカバー)

ウィンドウ全体に単色や静止画を重ねて、画面の切り替えに暗転 (黒)・白への転換・クロスフェードをかける仕組みです。
API は [Window.screenCover](../../reference/Window.md#screencover) /
[Window.fadeScreenCover](../../reference/Window.md#fadescreencover) /
[Window.snapshotScreenCover](../../reference/Window.md#snapshotscreencover) /
[Window.onScreenCoverDone](../../reference/Window.md#onscreencoverdone) です。

## 何が良いか

- **Elements のダイアログ (overlay) より手前に重なります。** レイヤで作った覆い (KAG の `syscover` など) は
  Elements の overlay の奥になるので、Elements で作ったセーブ・ロード・環境設定などの画面は覆えません。
  スクリーンカバーはレイヤではないので、レイヤやダイアログの重なり順に関係なく画面全体を覆えます
- **フェードはエンジンの時計で進みます。** スクリプトの処理が重くても、描画のたびにその時点の不透明度で
  描かれるので、なめらかに変わります
- **どの DrawDevice でも同じに見えます** (WINVER の basic / ogl、SDL3 版の sdl / sdlogl / ogl)

重なる順番 (奥 → 手前):

```
レイヤ (primaryLayer の下) → Elements のダイアログ → スクリーンカバー → デバッグ用の表示 (メモリ・パッド)
```

## 暗転して明ける

```tjs
// 0.25 秒で黒へ → 終わったら画面を切り替えて → 0.25 秒で明ける
window.fadeScreenCover(255, 250);   // 終わると window.onScreenCoverDone(255)
// …onScreenCoverDone の中で画面を切り替えてから…
window.fadeScreenCover(0, 250);     // 終わると window.onScreenCoverDone(0)
```

- 白へ転換するときは色を渡します: `window.fadeScreenCover(255, 300, 0xFFFFFF);`
- すぐに覆う / 外すときは `screenCover` に書きます: `window.screenCover = %[ color: 0x000000, opacity: 255 ];`
- ロードの直後など、黒から明けたいときは「すぐに黒で覆う → フェードで 0」です

```tjs
window.screenCover = %[ color: 0x000000, opacity: 255 ];
window.fadeScreenCover(0, 500);
```

### KAG3 でフェードの終わりを待つ

完了イベント `onScreenCoverDone` でトリガを引けば、シナリオ側は `[waittrig]` で待てます。

```
[iscript]
kag.onScreenCoverDone = function(opacity) { trigger("screencover"); } incontextof kag;
[endscript]

[eval exp="kag.fadeScreenCover(255, 250)"]
[waittrig name="screencover"]
; …ここで画面を切り替える…
[eval exp="kag.fadeScreenCover(0, 250)"]
[waittrig name="screencover"]
```

## クロスフェード (今の画面の静止画で覆う)

`snapshotScreenCover()` は、呼んだ時点の画面 (レイヤと Elements のダイアログ) を静止画にして画面全体を覆います。
そのまま下で画面を切り替え、`fadeScreenCover(0, ms)` で消すと、新しい画面へのクロスフェードになります。
Elements の画面も含めてフェードします。

```tjs
window.snapshotScreenCover();      // 今の画面で覆う (不透明度 255)
// …下で画面を切り替える (レイヤを出す、Elements の画面を出す / 閉じる)…
window.fadeScreenCover(0, 500);    // 0.5 秒で新しい画面へクロスフェード
```

- 静止画は呼んだその場で撮るので、同じ処理の中で続けて画面を変えても、変える前の画面が写ります
- 静止画に入るのはレイヤと Elements のダイアログだけで、スクリーンカバー自身とデバッグ用の表示は入りません
- 不透明度が 0 になると静止画は捨てます (覆っている間だけメモリを使います。大きさはウィンドウの描画バッファと同じ)
- 色を書く・`fadeScreenCover` に色を渡すと、単色の覆いに戻ります
- 静止画を撮れない DrawDevice (プラグインの DrawDevice など) では何もせず false を返します

## 覆っている間の入力

`blockInput` を true にすると、覆っている間 (不透明度が 0 でないか、フェード中) はマウス・キー・タッチの入力を
レイヤ・Elements・Window のイベントのどれにも渡しません。暗転中にボタンが押されて画面が二重に開く、といった
事故を防げます。既定は false (入力を通す) です。

```tjs
window.screenCover = %[ blockInput: true ];          // 以後、覆っている間は入力を止める
window.fadeScreenCover(255, 250, void, true);        // フェードと同時に指定してもよい
```

ボタンやキーを離す入力 (onMouseUp / onKeyUp など) は、押したままにならないよう止めずに通します。

## キャプチャとサムネイル

- 画面のキャプチャ ([System.captureScreen](../../reference/System.md#capturescreen)) には見えているとおり
  (スクリーンカバー込みで) 入ります
- レイヤから取る画像 (セーブのサムネイルなど) には入りません。レイヤではないためです

## 今の状態を見る

`screenCover` を読むと `%[ color, opacity, blockInput, fading, snapshot ]` が返ります。`opacity` はその時点の
不透明度 (フェード中なら途中の値)、`fading` はフェード中なら 1、`snapshot` は静止画で覆っているなら 1 です。
