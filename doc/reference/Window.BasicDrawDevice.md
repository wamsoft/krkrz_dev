# Window.BasicDrawDevice

Window.BasicDrawDevice クラスは、このインスタンスを [Window.drawDevice](Window.md#drawdevice) に登録して使用するための DrawDevice で、標準的な描画機能を提供します。

## メンバー一覧

### コンストラクタ

- [BasicDrawDevice](#basicdrawdevice)

### プロパティ

- [interface](#interface)
- [videoPresenterHost](#videopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)
- [d3d11Device](#d3d11device)

### メソッド

- [recreate](#recreate)

---

### BasicDrawDevice

コンストラクタ

**解説**

BasicDrawDevice オブジェクトの構築

Window.BasicDrawDevice クラスのオブジェクトを構築します。

初期状態で Window.drawDevice にはこのクラスのインスタンスが登録されているので、新たに登録する必要はありません。

---

### interface

プロパティ \ アクセス: `r`

**解説**

インターフェースオブジェクトを取得

プラグインなどで DrawDevice オブジェクトを利用するためにあります。

---

### videoPresenterHost

プロパティ \ アクセス: `r`

**解説**

オーバーレイ動画 presenter 登録口 (ポインタ値)

オーバーレイ動画側 (VideoOverlay) が、この DrawDevice の D3D11 バックバッファへ
pull 型で合成するために読み取る `iTVPVideoPresenterHost` へのポインタ値です。
非 0 なら presenter を登録して pull 合成に載り、0/未定義なら子ウィンドウ present に
フォールバックします。通常はエンジン内部/プラグインが使用します。

---

### dialogRendererHost

プロパティ \ アクセス: `r`

**解説**

Elements ダイアログ renderer host (ポインタ値)

Elements のオーバーレイ描画アダプタを取得するための `iTVPDialogRendererHost` への
ポインタ値です。通常はエンジン内部/プラグインが使用します。

---

### viewportBackgroundHost

プロパティ \ アクセス: `r`

**解説**

ビューポート余白塗り登録口 (ポインタ値)

ゲーム画面が描画領域全体を覆わないときの余白 ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) を受け取る
`iTVPViewportBackgroundHost` へのポインタ値です。 Window はこのプロパティが非 0 の
ときだけ余白設定を反映します ( プロパティを持たない描画デバイスでは余白の塗り分けは
効かず、そのデバイス既定の塗りつぶしのままになります )。 通常はエンジン内部/プラグインが
使用します。

---

### d3d11Device

プロパティ \ アクセス: `r`

**解説**

ID3D11Device ポインタ (ポインタ値)

HW 動画 (IMFMediaEngine) がエンジンの D3D11 デバイスへ束ねて HW デコードするために
公開している `ID3D11Device` へのポインタ値です (VIDEO_SUPPORT + マルチスレッド保護済み)。
WINVER (D3D11) ビルドのみ。通常はエンジン内部/プラグインが使用します。

---

### recreate

メソッド

**解説**

内部デバイス再生成

内部デバイスの再生成を行います。

通常使用することはありません。

---
