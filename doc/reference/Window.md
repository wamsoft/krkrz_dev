# Window

Window クラスは、**ウィンドウ**を管理するためのクラスです。

## メンバー一覧

### コンストラクタ

- [Window](#window)

### プロパティ

- [visible](#visible)
- [caption](#caption)
- [width](#width)
- [height](#height)
- [minWidth](#minwidth)
- [minHeight](#minheight)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [left](#left)
- [top](#top)
- [focusable](#focusable)
- [trapKey](#trapkey)
- [innerWidth](#innerwidth)
- [innerHeight](#innerheight)
- [zoomNumer](#zoomnumer)
- [zoomDenom](#zoomdenom)
- [drawDevice](#drawdevice)
- [borderStyle](#borderstyle)
- [stayOnTop](#stayontop)
- [imeMode](#imemode)
- [mouseCursorState](#mousecursorstate)
- [useMouseKey](#usemousekey)
- [fullScreen](#fullscreen)
- [mainWindow](#mainwindow)
- [focusedLayer](#focusedlayer)
- [primaryLayer](#primarylayer)
- [HWND](#hwnd)
- [touchScaleThreshold](#touchscalethreshold)
- [touchRotateThreshold](#touchrotatethreshold)
- [touchPointCount](#touchpointcount)
- [enableTouch](#enabletouch)
- [waitVSync](#waitvsync)
- [hintDelay](#hintdelay)
- [displayOrientation](#displayorientation)
- [displayRotate](#displayrotate)
- [displayDensity](#displaydensity)
- [enableTouchMouse](#enabletouchmouse)
- [innerSunken](#innersunken)
- [layerEventTarget](#layereventtarget)
- [layerLeft](#layerleft)
- [layerTop](#layertop)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [mouseCursor](#mousecursor)
- [showScrollBars](#showscrollbars)

### メソッド

- [close](#close)
- [bringToFront](#bringtofront)
- [update](#update)
- [showModal](#showmodal)
- [setMaskRegion](#setmaskregion)
- [removeMaskRegion](#removemaskregion)
- [add](#add)
- [remove](#remove)
- [setSize](#setsize)
- [setMinSize](#setminsize)
- [setMaxSize](#setmaxsize)
- [setPos](#setpos)
- [setInnerSize](#setinnersize)
- [setZoom](#setzoom)
- [postInputEvent](#postinputevent)
- [hideMouseCursor](#hidemousecursor)
- [registerMessageReceiver](#registermessagereceiver)
- [getTouchPoint](#gettouchpoint)
- [getMouseVelocity](#getmousevelocity)
- [getTouchVelocity](#gettouchvelocity)
- [resetMouseVelocity](#resetmousevelocity)
- [beginMove](#beginmove)
- [findFullScreenCandidates](#findfullscreencandidates)
- [requestUpdate](#requestupdate)
- [setLayerPos](#setlayerpos)

### イベント

- [onMouseEnter](#onmouseenter)
- [onMouseLeave](#onmouseleave)
- [onClick](#onclick)
- [onDoubleClick](#ondoubleclick)
- [onMouseDown](#onmousedown)
- [onMouseUp](#onmouseup)
- [onMouseMove](#onmousemove)
- [onMouseWheel](#onmousewheel)
- [onTouchDown](#ontouchdown)
- [onTouchUp](#ontouchup)
- [onTouchMove](#ontouchmove)
- [onTouchScaling](#ontouchscaling)
- [onTouchRotate](#ontouchrotate)
- [onMultiTouch](#onmultitouch)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [onKeyPress](#onkeypress)
- [onResize](#onresize)
- [onFileDrop](#onfiledrop)
- [onCloseQuery](#onclosequery)
- [onPopupHide](#onpopuphide)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [onHintChanged](#onhintchanged)
- [onDisplayRotate](#ondisplayrotate)
- [onPointerDown](#onpointerdown)
- [onPointerMove](#onpointermove)
- [onPointerUp](#onpointerup)

---

### Window

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `parent` | `&nbsp;` | 親ウィンドウを指定します。<br>親ウィンドウを指定すると、その子ウィンドウとして生成されます。<br>指定しない場合は省略します。 |

**解説**

Window オブジェクトの構築

Window クラスのオブジェクトを構築します。

ウィンドウは非表示の状態で作成され、位置やサイズは未定義 ( どこかにの位置に適当なサイズ ) です。

---

### visible

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウが表示されているかどうか

ウィンドウが表示されているかどうかを表します。値を設定することもできます。

真ならばウィンドウが表示されていて、偽ならばウィンドウは非表示の状態です。

---

### caption

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウのキャプション

ウィンドウの**キャプション** ( タイトルバーのタイトル ) を表します。
値を設定することもできます。

---

### width

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの横幅

ウィンドウの横幅を表します。値を設定することもできます。

**関連:** [Window.height](Window.md#height) / [Window.setSize](Window.md#setsize)

---

### height

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの縦幅

ウィンドウの縦幅を表します。値を設定することもできます。

**関連:** [Window.width](Window.md#width) / [Window.setSize](Window.md#setsize)

---

### minWidth

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの最小の横幅

ウィンドウの最小の横幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.width](Window.md#width) / [Window.minHeight](Window.md#minheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### minHeight

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの最小の縦幅

ウィンドウの最小の縦幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.height](Window.md#height) / [Window.minWidth](Window.md#minwidth) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxWidth

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの最大の横幅

ウィンドウの最大の横幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.width](Window.md#width) / [Window.maxHeight](Window.md#maxheight) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxHeight

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの最大の縦幅

ウィンドウの最大の縦幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.height](Window.md#height) / [Window.maxWidth](Window.md#maxwidth) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### left

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの左端位置

ウィンドウの左端位置を表します。値を設定することもできます。

左端位置はスクリーンの原点 ( 左上隅 ) からの x 座標です。

**関連:** [Window.top](Window.md#top) / [Window.setPos](Window.md#setpos)

---

### top

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウの上端位置

ウィンドウの上端位置を表します。値を設定することもできます。

上端位置はスクリーンの原点 ( 左上隅 ) からの y 座標です。

**関連:** [Window.left](Window.md#left) / [Window.setPos](Window.md#setpos)

---

### focusable

プロパティ \ アクセス: `r/w`

**解説**

フォーカスを取得可能か

フォーカスを取得可能かどうかを表します。値を設定することもできます。

偽に設定すると、フォーカスを取得できなくなる、つまり、ウィンドウがアクティブにならなくなります。副作用として、タイトルバーをつかんでのウィンドウの移動やウィンドウのリサイズ、「×」ボタンを押してウィンドウを閉じる操作もできなくなります。

キーボード入力を得たいときは [Window.trapKey](Window.md#trapkey) プロパティを使用することができます。

通常、これは、ポップアップメニューのように、もっとも手前に表示されるが、それ自身はフォーカスを得ないウィンドウの実装に用います。

現バージョンでは、ウィンドウがフルスクリーン化するとき、あるいはフルスクリーンから復帰するときに、このプロパティの設定内容が失われる可能性があります。

**関連:** [Window.trapKey](Window.md#trapkey) / [Window.onPopupHide](Window.md#onpopuphide)

---

### trapKey

プロパティ \ アクセス: `r/w`

**解説**

キー入力をトラップするか

キー入力をトラップするかどうかを表します。値を設定することもできます。

真に設定すると、他のウィンドウで発生したキー入力イベントを横取りし、このウィンドウ上で発生させることができます。

複数のウィンドウのこのプロパティが真に設定されている場合は、もっとも最後に作成したウィンドウに対してキー入力イベントが発生します。

**関連:** [Window.focusable](Window.md#focusable)

---

### innerWidth

プロパティ \ アクセス: `r/w`

**解説**

クライアント領域の横幅

クライアント領域の横幅を表します。
値を設定することもできます。

**関連:** [Window.innerHeight](Window.md#innerheight) / [Window.setInnerSize](Window.md#setinnersize)

---

### innerHeight

プロパティ \ アクセス: `r/w`

**解説**

クライアント領域の縦幅

クライアント領域の縦幅を表します。
値を設定することもできます。

**関連:** [Window.innerWidth](Window.md#innerwidth) / [Window.setInnerSize](Window.md#setinnersize)

---

### zoomNumer

プロパティ \ アクセス: `r/w`

**解説**

レイヤ拡大倍率(分子)

レイヤの拡大倍率の分子を表します。
一応、値を設定することもできますが、値を設定する場合は [Window.setZoom](Window.md#setzoom) メソッドを使用してください。

分母は [Window.zoomDenom](Window.md#zoomdenom) プロパティが表します。

詳しくは [Window.setZoom](Window.md#setzoom) メソッドを参照してください。

**関連:** [Window.setZoom](Window.md#setzoom) / [Window.zoomDenom](Window.md#zoomdenom)

---

### zoomDenom

プロパティ \ アクセス: `r/w`

**解説**

レイヤ拡大倍率(分母)

レイヤの拡大倍率の分母を表します。
一応、値を設定することもできますが、値を設定する場合は [Window.setZoom](Window.md#setzoom) メソッドを使用してください。

分子は [Window.zoomNumer](Window.md#zoomnumer) プロパティが表します。

詳しくは [Window.setZoom](Window.md#setzoom) メソッドを参照してください。

**関連:** [Window.setZoom](Window.md#setzoom) / [Window.zoomNumer](Window.md#zoomnumer)

---

### drawDevice

プロパティ \ アクセス: `r/w`

**解説**

描画デバイス

描画デバイスオブジェクトを表します。

値を設定することもできます。値を設定すると、以前このウィンドウに指定されていた描画デバイスは自動的に
無効になります (invalidateされます)。

デフォルトでは、Window.BasicDrawDevice というクラスのインスタンスが指定されています。

Window.BasicDrawDevice の詳細については、吉里吉里ソースの core/visual/win32/BasicDrawDevice.cpp 内の説明も参照してください。

独自の描画デバイス (プラグインで提供される物) を指定する場合は、そのプラグインのドキュメントに
従ってください。

---

### borderStyle

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウ外見

ウィンドウの外見を表します。値を設定することもできます。

以下の値を設定することができます。

`**bsDialog**      :` サイズ変更不可の、ダイアログボックスと同様の外見を持ちます。

`**bsSingle**      :` サイズ変更不可のウィンドウです。

`**bsNone**        :` ボーダーのないウィンドウです。

`**bsSizeable**    :` サイズ変更可の一般的なウィンドウです。デフォルトです。

`**bsToolWindow**  :` サイズ変更不可のツールウィンドウ(キャプションの小さいウィンドウ) です。

`**bsSizeToolWin** :` bsToolWindow と似ていますが、サイズ変更が可能です。

---

### stayOnTop

プロパティ \ アクセス: `r/w`

**解説**

常に最上位に表示するかどうか

ウィンドウを常に最上位 ( 一番手前 ) に表示するかどうかを表します。値を設定することもできます。

真ならばウィンドウは常に最上位に表示されます。

現バージョンでは、ウィンドウがフルスクリーン化するとき、あるいはフルスクリーンから復帰するときに、このプロパティの設定内容が失われる可能性があります。

---

### imeMode

プロパティ \ アクセス: `r`

**解説**

デフォルトのIMEモード

デフォルトのIMEモードを表します。

ここで指定したモードは、どのレイヤにもフォーカスが無い状態に設定されるモードです。

未指定の場合は **imDisable**で、これはどのレイヤにもフォーカスが無い状態では IME は無効状態であるということになります。

指定可能な値については [Layer.imeMode](Layer.md#imemode) を参照してください。

---

### mouseCursorState

プロパティ \ アクセス: `r/w`

**解説**

マウスカーソル表示状態

マウスカーソルの表示状態を表します。値を設定することもできます。

`**mcsVisible**`を指定すると、マウスカーソルは表示状態になります。これはデフォルトの状態です。

`**mcsTempHidden**`を指定すると、マウスカーソルは非表示状態になりますが、少しでもマウスを動かすと`mcsVisible`に変わり、表示状態になります。[Window.hideMouseCursor](Window.md#hidemousecursor)メソッドを呼び出すとこの状態になります。

`**mcsHidden**`を指定すると、マウスカーソルは非表示状態になります。マウスを動かしても表示状態にはなりません。

---

### useMouseKey

プロパティ \ アクセス: `r/w`

**解説**

マウスキーを使用するかどうか

マウスキーを使用するかどうかを表します。値を設定することもできます。

真ならばマウスキーを使用することができます。

マウスキーが有効になると、カーソルキーを使ってマウスカーソルを移動させることが
できますが、キー入力系のイベントはいっさい発生しなくなります。

---

### fullScreen

プロパティ \ アクセス: `r/w`

**解説**

フルスクリーンかどうか

**フルスクリーン**かどうかを表します。値を設定することもできます。

真を指定すると現在のウィンドウのクライアント領域がフルスクリーンになります。フルスクリーン
時の画面解像度はクライアント領域のサイズになります。

偽を指定するとウィンドウ表示になります。

---

### mainWindow

プロパティ \ アクセス: `r`

**解説**

メインウィンドウ

メインウィンドウ ( 最初に作成されたウィンドウ ) を表します。

---

### focusedLayer

プロパティ \ アクセス: `r/w`

**解説**

フォーカスを持っているレイヤオブジェクト

現在 **フォーカス** を持っているレイヤオブジェクトを表します。
値を設定することもできます。

null の場合はどのレイヤもフォーカスを持っていません。レイヤオブジェクトを
設定するとそのレイヤにフォーカスが移ります。

---

### primaryLayer

プロパティ \ アクセス: `r`

**解説**

プライマリレイヤオブジェクト

**プライマリレイヤ**オブジェクトを表します。

---

### HWND

プロパティ \ アクセス: `r`

**解説**

ウィンドウハンドル

ウィンドウハンドルを表します。

ここで得られるのは整数ですが、プラグインなどでこの数値を使う場合は HWND 型に
キャストして使ってください。

**関連:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### touchScaleThreshold

プロパティ \ アクセス: `r/w`

**解説**

マルチタッチ拡大閾値

マルチタッチで拡大を開始する閾値です。

2つのタッチ位置の距離がこの値以上変化した時に拡大イベントが発生します。

一度閾値を超えるといったん指が離されるまで拡大イベントは有効になります。

**関連:** [Window.onTouchScaling](Window.md#ontouchscaling)

---

### touchRotateThreshold

プロパティ \ アクセス: `r/w`

**解説**

マルチタッチ回転閾値

マルチタッチで回転を開始する閾値です。

各タッチ位置の移動距離がこの値以上変化した時に回転イベントが発生します。

一度閾値を超えるといったん指が離されるまで回転イベントは有効になります。

**関連:** [Window.onTouchRotate](Window.md#ontouchrotate)

---

### touchPointCount

プロパティ \ アクセス: `r`

**解説**

タッチ数

タッチパネルにタッチされている数です。

**関連:** [Window.getTouchPoint](Window.md#gettouchpoint)

---

### enableTouch

プロパティ \ アクセス: `r/w`

**解説**

タッチイベント有効/無効

**タッチイベント**が有効かどうかを表します。値を設定することもできます。

真を指定すると[Window.onTouchDown](Window.md#ontouchdown)等のイベントが有効になり、タッチ操作では[Window.onMouseDown](Window.md#onmousedown)などが発生しなくなります。

タッチデバイスがありマルチタッチが有効な環境では、デフォルトが true になります。

---

### waitVSync

プロパティ \ アクセス: `r/w`

**解説**

垂直同期待ち

トランジション(画面切り替え)などでディスプレイの垂直同期を待ってから描画するかどうかの設定です。

設定を変えると、画面のちらつきを抑えられる場合がありますが、描画のパフォーマンスが低下する場合もあります。

---

### hintDelay

プロパティ \ アクセス: `r/w`

**解説**

ヒント表示待ち時間

ヒントの表示待ち時間をミリ秒単位で表します。値を設定することもできます。

デフォルトは500ミリ秒です。

0を設定すると即座に [Window.onHintChanged](Window.md#onhintchanged) が呼び出されます(常時表示状態)。

-1を設定するとヒントが表示されることはありません。

**関連:** [Window.onHintChanged](Window.md#onhintchanged)

---

### displayOrientation

プロパティ \ アクセス: `r`

**解説**

ディスプレイの向き(1.1.0以降)

ディスプレイの向きを表します。

oriUnknown (取得失敗/不明), oriPortrait(縦向き), oriLandscape(横向き)のいずれかの値です。

**関連:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayRotate](Window.md#displayrotate)

---

### displayRotate

プロパティ \ アクセス: `r`

**解説**

ディスプレイの回転角度(1.1.0以降)

ディスプレイの回転角度を表します。

0、90、180、270、-1 のいずれかで、取得できなかった時は-1です。

**関連:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayOrientation](Window.md#displayorientation)

---

### displayDensity

プロパティ \ アクセス: `r/w`

**解説**

画面密度(dpi)

dpi値を返します。
読み取りのみ可能です。
GetDeviceCapsで得られる値です。

---

### enableTouchMouse

プロパティ \ アクセス: `r/w`

**解説**

TODO: enableTouchMouse の説明

---

### innerSunken

プロパティ \ アクセス: `r/w`

**解説**

TODO: innerSunken の説明

---

### layerEventTarget

プロパティ \ アクセス: `r/w`

**解説**

TODO: layerEventTarget の説明

---

### layerLeft

プロパティ \ アクセス: `r/w`

**解説**

TODO: layerLeft の説明

---

### layerTop

プロパティ \ アクセス: `r/w`

**解説**

TODO: layerTop の説明

---

### layerTreeOwnerInterface

プロパティ \ アクセス: `r/w`

**解説**

TODO: layerTreeOwnerInterface の説明

---

### mouseCursor

プロパティ \ アクセス: `r/w`

**解説**

TODO: mouseCursor の説明

---

### showScrollBars

プロパティ \ アクセス: `r/w`

**解説**

TODO: showScrollBars の説明

---

### close

メソッド

**解説**

ウィンドウを閉じる

[Window.showModal](Window.md#showmodal) メソッドで表示されたウィンドウを閉じます。ウィンドウを閉じる前に [Window.onCloseQuery](Window.md#onclosequery) イベントが発生し、ウィンドウを閉じることができるかどうかを確認することができます。

**関連:** [Window.showModal](Window.md#showmodal) / [Window.onCloseQuery](Window.md#onclosequery)

---

### bringToFront

メソッド

**解説**

ウィンドウを最前面に移動

ウィンドウを最前面に移動します。アプリケーションが非アクティブの場合はアプリケーション
自体もアクティブにします。

---

### update

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `tutNormal` | ウィンドウ描画のタイプを指定します。<br>`**tutNormal**` を指定すると通常の描画 ( 差分描画 )、<br>`**tutEntire**` を指定するとウィンドウ内容全体を描画します。 |

**解説**

ウィンドウ内容の強制的な描画

引数は現バージョンでは無視されます。

tutNormal や tutEntire は実装されていません。

---

### showModal

メソッド

**解説**

モーダルでウィンドウを表示

ウィンドウを**モーダル** ( **モード付き** ) で表示します。
このメソッドはウィンドウを表示状態に
し、かつ、他のウィンドウを一時的に無効にします。そのためユーザはこのウィンドウのみに
アクセスできる状態になります ( これをモード付きの状態と呼びます )。ウィンドウが閉じられると
モード付きの状態は解除されます。

このメソッドを呼び出す時点ではウィンドウは非表示でなくてはなりません。

---

### setMaskRegion

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `threshold` | `1` | マスクのスレッショルド ( 敷居値 ) を指定します。<br>プライマリレイヤのマスク ( レイヤの不透明度の情報 ) のうち、この値よりも大きい部分の形に<br>ウィンドウが切り取られて表示されます。 |

**解説**

ウィンドウリージョンをマスクに従って設定

ウィンドウリージョンをプライマリレイヤのマスク ( レイヤの不透明度の情報 ) に従って設定します。

ウィンドウを不定形にする事ができます。

表示されるプライマリレイヤと、ウィンドウの大きさ、位置がずれないようにするには
以下のことを行う必要があります。

- [Window.borderStyle](Window.md#borderstyle) は bsNone に設定します。
- [Layer.imageLeft](Layer.md#imageleft) および [Layer.imageTop](Layer.md#imagetop) は 0 に設定します。

**関連:** [Window.removeMaskRegion](Window.md#removemaskregion)

---

### removeMaskRegion

メソッド

**解説**

ウィンドウリージョンの解除

[Window.setMaskRegion](Window.md#setmaskregion)で設定したウィンドウリージョンを解除し、ウィンドウを矩形に戻します。

**関連:** [Window.setMaskRegion](Window.md#setmaskregion)

---

### add

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 管理されるオブジェクトを指定します。 |

**解説**

管理オブジェクトの追加

管理オブジェクトを追加します。ここで指定されたオブジェクトは、ウィンドウが無効化
されるときに自動的に無効化されるようになります。

**関連:** [Window.remove](Window.md#remove)

---

### remove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 管理オブジェクトのリストから削除するオブジェクトを指定します。 |

**解説**

管理オブジェクトの削除

管理オブジェクトのリストから指定されたオブジェクトを削除します。

**関連:** [Window.add](Window.md#add)

---

### setSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | ウィンドウの横幅を指定します。 |
| `height` | `&nbsp;` | ウィンドウの縦幅を指定します。 |

**解説**

ウィンドウサイズの設定

ウィンドウのサイズを指定します。

ウィンドウのサイズを指定するときには、[Window.width](Window.md#width) や
[Window.height](Window.md#height) プロパティを個々に設定するよりも
このメソッドで一気に指定した方が効率的です。

**関連:** [Window.width](Window.md#width) / [Window.height](Window.md#height) / [Window.setPos](Window.md#setpos) / [Window.setInnerSize](Window.md#setinnersize) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize)

---

### setMinSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | ウィンドウの最小の横幅を指定します。0を指定すると制限は無くなります。 |
| `height` | `&nbsp;` | ウィンドウの最小の縦幅を指定します。0を指定すると制限は無くなります。 |

**解説**

ウィンドウの最小サイズの設定

ウィンドウの最小サイズを指定します。ウィンドウはこのメソッドで指定したサイズより小さくなることはできません。

**関連:** [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight)

---

### setMaxSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | ウィンドウの最大の横幅を指定します。0を指定すると制限は無くなります。 |
| `height` | `&nbsp;` | ウィンドウの最大の縦幅を指定します。0を指定すると制限は無くなります。 |

**解説**

ウィンドウの最大サイズの設定

ウィンドウの最大サイズを指定します。ウィンドウはこのメソッドで指定したサイズより大きくなることはできません。

**関連:** [Window.setMinSize](Window.md#setminsize) / [Window.setSize](Window.md#setsize) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight)

---

### setPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` | ウィンドウの左端位置を指定します。 |
| `top` | `&nbsp;` | ウィンドウの上端位置を指定します。 |

**解説**

ウィンドウ位置の設定

ウィンドウの位置を指定します。

ウィンドウの位置を指定するときには、[Window.left](Window.md#left) や
[Window.top](Window.md#top) プロパティを個々に設定するよりも
このメソッドで一気に指定した方が効率的です。

**関連:** [Window.left](Window.md#left) / [Window.top](Window.md#top) / [Window.setSize](Window.md#setsize)

---

### setInnerSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | クライアントの横幅を指定します。 |
| `height` | `&nbsp;` | クライアントの縦幅を指定します。 |

**解説**

クライアントサイズの設定

ウィンドウのクライアントサイズを指定します。

クライアントは、レイヤを表示可能なウィンドウ内の領域です。

このサイズを設定するとウィンドウのサイズもそれに応じて変化します。

クライアントのサイズを指定するときには、[Window.innerWidth](Window.md#innerwidth) や
[Window.innerHeight](Window.md#innerheight) プロパティを個々に設定するよりも
このメソッドで一気に指定した方が効率的です。

**関連:** [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)

---

### setZoom

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `numer` | `&nbsp;` | 倍率の分子を整数で指定します。 |
| `denom` | `&nbsp;` | 倍率の分母を整数で指定します。 |

**解説**

レイヤ拡大倍率の設定

レイヤの拡大倍率を指定します。分子/分母で指定したサイズで画像が拡大、あるいは縮小されて表示されます。

分子・分母が公約数を持つ場合は自動的に約分されるため、[Window.zoomNumer](Window.md#zoomnumer) プロパティや [Window.zoomDenom](Window.md#zoomdenom) プロパティで読み出される値は、このメソッドで指定した値とは異なる場合があります。

現バージョンの吉里吉里では、拡大・縮小時に補間がかかるかどうかはグラフィックカードのハードウェアやドライバに影響されます。補間がかからないハードウェアやドライバの場合は、画質が荒くなります。

オプションによっては、吉里吉里は拡大・縮小に使用可能なハードウェアを、倍率が変更されるたびに調査するため、このメソッドは拡大率を連続的に変化させて演出を行うような用途には適していません。

**関連:** [Window.zoomNumer](Window.md#zoomnumer) / [Window.zoomDenom](Window.md#zoomdenom)

---

### postInputEvent

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `eventname` | `&nbsp;` | イベント名称を指定します。以下の文字列で指定します。<br>- "**onKeyDown**" は [Window.onKeyDown](Window.md#onkeydown) イベントを生成します。<br>- "**onKeyPress**" は [Window.onKeyPress](Window.md#onkeypress) イベントを生成します。<br>- "**onKeyUp**" は [Window.onKeyUp](Window.md#onkeyup) イベントを生成します。onKeyDownとonKeyUpは対になるので、onKeyDownを生成したら対応するonKeyUpも生成することを推奨します。 |
| `params` | `null` | イベントのパラメータが格納された辞書配列を指定します。<br>- "onKeyDown" イベントや "onKeyUp" イベントでは、"key" に仮想キーコード、"shift" にシフト状態を格納します。"shift" を省略すると 0 であると見なされます。<br>- "onKeyPress" イベントでは "key" に文字を指定します。 |

**解説**

入力イベントの生成

入力イベントを生成します。現バージョンではキー入力に関する３つのイベントを生成できます。

このメソッドは、イベントを非同期イベントとして生成します。つまり、このメソッドは、対応するイベントハンドラの終了を待たずに帰ります。実際にイベントハンドラが呼ばれて処理が行われるのは、いったん吉里吉里に制御が戻った後となります。

入力イベントは、Windowクラスのほか、通常の入力イベントと同じく、Layerクラスの該当するイベントとしても発生します。

postInputEvent('onKeyDown', %[key: VK_UP, shift: ssShift]);

postInputEvent('onKeyUp',   %[key: VK_UP, shift: ssShift]);

// 左カーソルキーを押す

---

### hideMouseCursor

メソッド

**解説**

マウスカーソルを一時的に隠す

マウスカーソルを一時的に隠します。マウスを少しでも動かすと
マウスカーソルは再び表示されるようになります。

このメソッドは、[Window.mouseCursorState](Window.md#mousecursorstate)を`**mcsTempHidden**`に設定するのと同じ効果を持ちます。

---

### registerMessageReceiver

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` | 登録するか、登録削除するかどうかを指定します。<br>**wrmRegister** を指定すると登録になります。**wrmUnregister** を<br>指定すると登録削除になります。<br>wrm で始まる定数は tp_stub.h に定義されています。 |
| `func` | `&nbsp;` | メッセージ受信関数を指定します。<br>メッセージ受信関数は bool __stdcall func(void *userdata, tTVPWindowMessage *Message)<br>の形式である必要があり、このメソッドに渡す際にその関数ポインタを整数型にキャストして渡す<br>必要があります。<br>構造体 tTVPWindowMessage は tp_stub.h に定義されています。<br>この関数が true を返すと吉里吉里本体側はそのウィンドウメッセージに関知しなくなります。 |
| `userdata` | `&nbsp;` | func 引数で指定された受信関数の userdata 引数に渡すためのデータポインタを指定します。<br>このメソッドに渡す際にはそのポインタを整数型にキャストして渡す必要があります。<br>この引数は mode 引数が wrmRegister でないときは無視されます。 |

**解説**

メッセージ受信関数の登録/登録削除

このメソッドは C++ 等で記述されたプラグインから利用されることを想定しているメソッドです。TJS2
からは正常に利用できません。

このメソッドでは、このウィンドウを通過するメッセージをトラップするためのメッセージ受信関数を
登録することができます。メッセージ受信関数では通常のウィンドウメッセージの他、
TVP_WM_DETACH と TVP_WM_ATTACH という２つの重要なメッセージもトラップすることができ、
ウィンドウが再構築や破棄されるタイミングにおいて、子ウィンドウを取り外すというような
用途に使用できます。

吉里吉里ソース配布パッケージ中の src/plugins/win32/wmrdump に簡単な使用法の説明があります。

**関連:** [Window.HWND](Window.md#hwnd)

---

### getTouchPoint

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | タッチ座標配列のインデックスを指定します。 |

**解説**

タッチ座標の取得

現在のタッチ座標配列から指定インデックスの座標情報を取得します。

座標数は [Window.touchPointCount](Window.md#touchpointcount) プロパティで取得できます。

座標情報は以下の要素を含む辞書で返されます。

`**startX**     : `このタッチの開始座標の x 座標値 ( クライアント座標系 ) です

`**startY**   : `このタッチの開始座標の y 座標値 ( クライアント座標系 ) です

`**x**    : `このタッチの現在座標の x 座標値 ( クライアント座標系 ) です

`**y**    : `このタッチの現在座標の y 座標値 ( クライアント座標系 ) です

`**ID**    : `このタッチの識別用 IDです

**関連:** [Window.touchPointCount](Window.md#touchpointcount)

---

### getMouseVelocity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X軸方向のマウス座標移動速度が返ります。 |
| `y` | `&nbsp;` | Y軸方向のマウス座標移動速度が返ります。 |
| `speed` | `&nbsp;` | マウス座標移動速度が返ります。 |

**戻り値**

取得が成功したか失敗したかが返ります

**解説**

マウス座標移動速度の取得(1.1.0以降)

現在のマウス移動速度を pixel / sec で取得します。

ウィンドウ内に入った瞬間から計測開始されています。

[Window.resetMouseVelocity](Window.md#resetmousevelocity) を使用して計測をリセットし、任意のタイミングか計測得できるように出来ます。

**関連:** [Window.getTouchVelocity](Window.md#gettouchvelocity) / [Window.resetMouseVelocity](Window.md#resetmousevelocity)

---

### getTouchVelocity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | タッチIDを指定します。 |
| `x` | `&nbsp;` | X軸方向のマウス座標移動速度が返ります。 |
| `y` | `&nbsp;` | Y軸方向のマウス座標移動速度が返ります。 |
| `speed` | `&nbsp;` | マウス座標移動速度が返ります。 |

**戻り値**

取得が成功したか失敗したかが返ります

**解説**

タッチ座標移動速度の取得(1.1.0以降)

現在のタッチ移動速度を pixel / sec で取得します。

押下されてから離されるまでの間計測されています。

マルチタッチ対応のため ID ごとに速度計測されています。

[Window.onTouchUp](Window.md#ontouchup) イベントのメソッド呼び出しが終了すると計測している速度情報は消えてしまうので注意が必要です。

**関連:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### resetMouseVelocity

メソッド

**解説**

マウス座標移動速度計測のリセット(1.1.0以降)

マウスの座標移動速度計測をリセットします。

リセットすることで任意のタイミングから速度計測を開始することが出来ます。

**関連:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### beginMove

メソッド

**解説**

TODO: beginMove の説明

---

### findFullScreenCandidates

メソッド

**解説**

TODO: findFullScreenCandidates の説明

---

### requestUpdate

メソッド

**解説**

TODO: requestUpdate の説明

---

### setLayerPos

メソッド

**解説**

TODO: setLayerPos の説明

---

### onMouseEnter

イベント

**解説**

マウスが入ってきた

マウスがウィンドウのクライアント領域内に入ってきたときに発生します。

**関連:** [Window.onMouseLeave](Window.md#onmouseleave)

---

### onMouseLeave

イベント

**解説**

マウスが出ていった

マウスがウィンドウのクライアント領域内から出ていったときに発生します。

**関連:** [Window.onMouseEnter](Window.md#onmouseenter)

---

### onClick

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | ウィンドウがクリックされた位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | ウィンドウがクリックされた位置の y 座標 ( クライアント座標での ) の値です。 |

**解説**

ウィンドウがクリックされた

ウィンドウがクリックされた時に発生します。

**関連:** [Window.onMouseDown](Window.md#onmousedown) / [Window.onDoubleClick](Window.md#ondoubleclick)

---

### onDoubleClick

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | ウィンドウがダブルクリックされた位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | ウィンドウがダブルクリックされた位置の y 座標 ( クライアント座標での ) の値です。 |

**解説**

ウィンドウがダブルクリックされた

ウィンドウがダブルクリックされた時に発生します。

**関連:** [Window.onClick](Window.md#onclick)

---

### onMouseDown

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスのボタンが押された位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | マウスのボタンが押された位置の y 座標 ( クライアント座標での ) の値です。 |
| `button` | `&nbsp;` | 押されたマウスボタンです。以下のいずれかの値になります。<br>`**mbLeft**    : `マウスの左ボタンが押された<br>`**mbMiddle**  : `マウスの中ボタンが押された<br>`**mbRight**   : `マウスの右ボタンが押された<br>`**mbX1**      : `マウスのサイドキー第1ボタンが押された<br>`**mbX2**      : `マウスのサイドキー第2ボタンが押された |
| `shift` | `&nbsp;` | マウスボタンが押されたときに同時に押されていたシフト系のキーの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた |

**解説**

マウスのボタンが押された

マウスボタンが押された時に発生します。

**関連:** [Window.onClick](Window.md#onclick)

---

### onMouseUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスのボタンが離された位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | マウスのボタンが離された位置の y 座標 ( クライアント座標での ) の値です。 |
| `button` | `&nbsp;` | 離されたマウスボタンです。以下のいずれかの値になります。<br>`**mbLeft**    : `マウスの左ボタンが離された<br>`**mbMiddle**  : `マウスの中ボタンが離された<br>`**mbRight**   : `マウスの右ボタンが離された<br>`**mbX1**      : `マウスのサイドキー第1ボタンが離された<br>`**mbX2**      : `マウスのサイドキー第2ボタンが離された |
| `shift` | `&nbsp;` | マウスボタンが離された時に同時に押されていたシフト系のキーの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた |

**解説**

マウスのボタンが離された

マウスボタンが離された時に発生します。

---

### onMouseMove

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスが移動した位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | マウスが移動した位置の y 座標 ( クライアント座標での ) の値です。 |
| `shift` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた<br>`**ssLeft**    : `マウスの左ボタンが押されていた<br>`**ssMiddle**  : `マウスの中ボタンが押されていた<br>`**ssRight**   : `マウスの右ボタンが押されていた |

**解説**

マウスが移動した

マウスが移動した時に発生します。

---

### onMouseWheel

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた<br>`**ssLeft**    : `マウスの左ボタンが押されていた<br>`**ssMiddle**  : `マウスの中ボタンが押されていた<br>`**ssRight**   : `マウスの右ボタンが押されていた |
| `delta` | `&nbsp;` | ホイールの回転角です。上方向(ユーザの反対側の方向)に回された場合は正、<br>下方向(ユーザ側の方向)に回された場合は負の値になります。通常、最小量は 120<br>となります。 |
| `x` | `&nbsp;` | ホイールが回転した位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | ホイールが回転した位置の y 座標 ( クライアント座標での ) の値です。 |

**解説**

マウスホイールが回転した

マウスホイールが回転した時に発生します。

---

### onTouchDown

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチされた位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | タッチされた位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。<br>マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

画面がタッチされた

タッチパネルにタッチされた時に発生します。

---

### onTouchUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 離された位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | 離された位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。<br>マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

画面から指が離された

タッチパネルから指が離された時に発生します。

---

### onTouchMove

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチ位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | タッチ位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。<br>デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。<br>マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

指が移動した

タッチパネル上で触れている指が移動した時に発生します。

---

### onTouchScaling

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `startdistance` | `&nbsp;` | マルチタッチが開始された時のピクセル距離です。 |
| `currentdistance` | `&nbsp;` | イベント発生時のタッチのピクセル距離です。 |
| `cx` | `&nbsp;` | 中心位置の x 座標 ( クライアント座標での ) の値です。 |
| `cy` | `&nbsp;` | 中心位置の y 座標 ( クライアント座標での ) の値です。 |
| `flag` | `&nbsp;` | マルチタッチ状態フラグです。<br>`**0x01**     : `マルチタッチが開始された最初のイベントに設定されています。 |

**解説**

拡大操作した

タッチパネル上でマルチタッチによって拡大操作した時に発生します。

---

### onTouchRotate

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `startangle` | `&nbsp;` | マルチタッチが開始された時のラジアン角度です。 |
| `currentangle` | `&nbsp;` | イベント発生時のタッチのラジアン角度です。 |
| `distance` | `&nbsp;` | イベント発生時のタッチのピクセル距離です。 |
| `cx` | `&nbsp;` | 中心位置の x 座標 ( クライアント座標での ) の値です。 |
| `cy` | `&nbsp;` | 中心位置の y 座標 ( クライアント座標での ) の値です。 |
| `flag` | `&nbsp;` | マルチタッチ状態フラグです。<br>`**0x01**     : `マルチタッチが開始された最初のイベントに設定されています。 |

**解説**

回転操作した

タッチパネル上でマルチタッチによって回転操作した時に発生します。

---

### onMultiTouch

イベント

**解説**

マルチタッチ状態が変化した

マルチタッチ状態が開始されたり、移動したり、離れた時に発生します。

座標情報は [Window.touchPointCount](Window.md#touchpointcount) プロパティと [Window.getTouchPoint](Window.md#gettouchpoint) メソッドで取得できます。

**関連:** [Window.getTouchPoint](Window.md#gettouchpoint) / [Window.touchPointCount](Window.md#touchpointcount)

---

### onKeyDown

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 押されたキーの**仮想キーコード**の値です。 |
| `shift` | `&nbsp;` | キーが押された時に同時に押されていたシフト系のキーやマウスのボタンの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた<br>`**ssLeft**    : `マウスの左ボタンが押されていた<br>`**ssMiddle**  : `マウスの中ボタンが押されていた<br>`**ssRight**   : `マウスの右ボタンが押されていた<br>また、キーボードが長時間押され、キーリピートが発生している場合は<br>以下の値も組み合わされます。<br>`**ssRepeat**  : `キーリピートが発生した |

**解説**

キーが押された

キーが押された時に発生します。

---

### onKeyUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 離されたキーの**仮想キーコード**の値です。 |
| `shift` | `&nbsp;` | キーが離された時に同時に押されていたシフト系のキーやマウスのボタンの状態です。<br>以下の値のビット OR による組み合わせになります。<br>`**ssAlt**     : `ALT キーが押されていた<br>`**ssShift**   : `SHIFT キーが押されていた<br>`**ssCtrl**    : `CTRL キーが押されていた<br>`**ssLeft**    : `マウスの左ボタンが押されていた<br>`**ssMiddle**  : `マウスの中ボタンが押されていた<br>`**ssRight**   : `マウスの右ボタンが押されていた |

**解説**

キーが離された

キーが離された時に発生します。

---

### onKeyPress

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 入力された文字です。 |

**解説**

文字が入力された

文字が入力されたときに発生します。[Window.onKeyDown](Window.md#onkeydown) と異なるのは、onKeyDown が
仮想キーコードを扱うのに対し、このイベントは文字そのものを扱います。押されたキーが
文字とは関係のないキー (ファンクションキーなど) の場合はこのイベントは発生しません。

Ctrlキーと同時に押された場合は、以下に示すようなコントロールコードが送られてきます。

`0x00 : `Ctrl+@

`0x01 : `Ctrl+A

`0x02 : `Ctrl+B

`0x03 : `Ctrl+C

`0x04 : `Ctrl+D

`0x05 : `Ctrl+E

`0x06 : `Ctrl+F

`0x07 : `Ctrl+G

`0x08 : `Ctrl+H

`0x09 : `Ctrl+I

`0x0A : `Ctrl+J

`0x0B : `Ctrl+K

`0x0C : `Ctrl+L

`0x0D : `Ctrl+M

`0x0E : `Ctrl+N

`0x0F : `Ctrl+O

`0x10 : `Ctrl+P

`0x11 : `Ctrl+Q

`0x12 : `Ctrl+R

`0x13 : `Ctrl+S

`0x14 : `Ctrl+T

`0x15 : `Ctrl+U

`0x16 : `Ctrl+V

`0x17 : `Ctrl+W

`0x18 : `Ctrl+X

`0x19 : `Ctrl+Y

`0x1A : `Ctrl+Z

`0x1B : `Ctrl+[

`0x1C : `Ctrl+\

`0x1D : `Ctrl+]

`0x1E : `Ctrl+^

`0x1F : `Ctrl+_

---

### onResize

イベント

**解説**

ウィンドウのサイズが変化した

ウィンドウのサイズが変化した時に発生します。

実際のサイズは [Window.width](Window.md#width) プロパティや [Window.height](Window.md#height) プロパティなどで取得してください。

---

### onFileDrop

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `files` | `&nbsp;` | ドロップされたファイル名が格納された配列(Array)オブジェクトです。 |

**解説**

ファイルがドロップされた

ファイルがエクスプローラなどからウィンドウにドロップされたときに発生します。

単一のファイルがドロップされた場合でも引数には配列オブジェクトが渡されます (最初の要素が
そのファイルになります )。

---

### onCloseQuery

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `canclose` | `&nbsp;` | ウィンドウを閉じることができるかどうかが渡されます。下位クラスから上位クラスのイベントハンドラが<br>呼ばれる課程で、下位クラスが決定した「ウィンドウを閉じることができるか」が渡されます。 |

**解説**

ウィンドウを閉じる確認

ウィンドウを閉じることができるかどうかを確認するためのイベントです。ウィンドウを閉じることが
できない場合、上位クラスの同メソッドに引数として false を渡してください。

---

### onPopupHide

イベント

**解説**

ポップアップウィンドウを閉じる

ポップアップウィンドウが閉じるべき時に発生するイベントです。このイベントは、[Window.stayOnTop](Window.md#stayontop) プロパティが真で、かつ、[Window.focusable](Window.md#focusable) プロパティが偽の場合、「他のウィンドウがクリックされた」あるいは「他のアプリケーションがアクティブになった」時に発生します。

通常は、ここでウィンドウを閉じたり、非表示にする処理を行ってください。

**関連:** [Window.focusable](Window.md#focusable) / [Window.stayOnTop](Window.md#stayontop)

---

### onActivate

イベント

**解説**

ウィンドウがアクティブになったとき

ウィンドウがアクティブになったときに呼び出されるイベント関数を表します。

このイベントは、ウィンドウが既にアクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [Window.onDeactivate](Window.md#ondeactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onDeactivate

イベント

**解説**

ウィンドウが非アクティブになったとき

ウィンドウが非アクティブになったときに呼び出されるイベント関数を表します。

このイベントは、ウィンドウが既に非アクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [Window.onActivate](Window.md#onactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onHintChanged

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | ヒントに表示する文字列が渡されます。 |
| `x` | `&nbsp;` | ヒント表示X軸座標値が渡されます。 |
| `y` | `&nbsp;` | ヒント表示Y軸座標値が渡されます。 |
| `isshow` | `&nbsp;` | ヒントを表示するか、非表示にするかが渡されます。 |

**解説**

ヒントの状態が変化したとき

ヒントの状態が変化したときに呼び出されるイベント関数を表します。

表示/非表示に従いヒントの表示を行います。

ヒントをレイヤで表示する場合は、そのレイヤのマウスメッセージが無視されるように [Layer.hitThreshold](Layer.md#hitthreshold) を256に設定します。

また、[Layer.ignoreHintSensing](Layer.md#ignorehintsensing) もtrueを指定します。

**関連:** [Window.hintDelay](Window.md#hintdelay) / [Layer.ignoreHintSensing](Layer.md#ignorehintsensing) / [Layer.hitThreshold](Layer.md#hitthreshold)

---

### onDisplayRotate

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `orientation` | `&nbsp;` | 画面の向き( orientation ) です。<br>以下のいずれかの値になります。<br>oriUnknown (取得失敗/不明), oriPortrait(縦向き), oriLandscape(横向き) |
| `angle` | `&nbsp;` | 角度です。<br>角度 ( angle ) は、0、90、180、270、-1 のいずれかで、取得できなかった時は-1となります。<br>角度は、そのデバイスデフォルトからの回転角なので、縦向きのデバイスでは縦向きで0となります。<br>通常のデバイスだと、横向きで0が多ようです。<br>縦向きが0になるのは最近の8インチタブレットなどで、縦向きが標準の向きとなっているものです。 |
| `bpp` | `&nbsp;` | bits per pixel です。 |
| `width` | `&nbsp;` | 画面の幅です。 |
| `height` | `&nbsp;` | 画面の高さです。 |

**解説**

画面が回転されたとき(1.1.0以降)

画面が回転されたときに呼び出されるイベント関数を表します。

**関連:** [Window.displayOrientation](Window.md#displayorientation) / [Window.displayRotate](Window.md#displayrotate)

---

### onPointerDown

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | タッチもしくはマウスボタンの種類 |
| `x` | `&nbsp;` | X位置 |
| `y` | `&nbsp;` | Y位置 |
| `cx` | `&nbsp;` | 接触幅(ピクセル数)、マウスの時は1 |
| `cy` | `&nbsp;` | 接触高さ(ピクセル数)、マウスの時は1 |
| `shift` | `&nbsp;` | 修飾キー状態、タッチの時は0 |
| `id` | `&nbsp;` | タッチID、マウスの時は常に0 |

**解説**

何らかのポインティングデバイスで押下された

---

### onPointerMove

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | タッチもしくはマウス。マウスボタンの種類ではなく、マウスとして通知。 |
| `x` | `&nbsp;` | X位置 |
| `y` | `&nbsp;` | Y位置 |
| `cx` | `&nbsp;` | 接触幅(ピクセル数)、マウスの時は1 |
| `cy` | `&nbsp;` | 接触高さ(ピクセル数)、マウスの時は1 |
| `shift` | `&nbsp;` | 修飾キー状態(マウス押下状態を含む)、タッチの時は0 |
| `id` | `&nbsp;` | タッチID、マウスの時は常に0 |

**解説**

何らかのポインティングデバイスが移動された

---

### onPointerUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | タッチもしくはマウスボタンの種類 |
| `x` | `&nbsp;` | X位置 |
| `y` | `&nbsp;` | Y位置 |
| `cx` | `&nbsp;` | 接触幅(ピクセル数)、マウスの時は1 |
| `cy` | `&nbsp;` | 接触高さ(ピクセル数)、マウスの時は1 |
| `shift` | `&nbsp;` | 修飾キー状態、タッチの時は0 |
| `id` | `&nbsp;` | タッチID、マウスの時は常に0 |

**解説**

何らかのポインティングデバイスが離された

---

## プラグイン拡張: layerExSave

ウインドウ拡張

### メンバー一覧

#### メソッド

- [startSaveLayerImage](#startsavelayerimage)
- [cancelSaveLayerImage](#cancelsavelayerimage)
- [stopSaveLayerImage](#stopsavelayerimage)
- [onSaveLayerImageProgress](#onsavelayerimageprogress)
- [onSaveLayerImageDone](#onsavelayerimagedone)

---

### startSaveLayerImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 保存対象レイヤ |
| `filename` | `&nbsp;` | ファイル名（拡張子が.pngの時のみPNG形式保存，それ以外はTLG5） |
| `tags` | `&nbsp;` | タグ情報 |

**戻り値**

ハンドラ

**解説**

TLG5/PNG 形式での画像の保存の開始

---

### cancelSaveLayerImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ハンドラ |

**解説**

画像保存キャンセル

---

### stopSaveLayerImage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ハンドラ |

**解説**

画像保存中止（中止した場合は終了イベントが来ません）

---

### onSaveLayerImageProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ハンドラ |
| `progress` | `&nbsp;` | 進行度合い(%表記) |
| `layer` | `&nbsp;` | レイヤ |
| `filename` | `&nbsp;` | ファイル名 |

**解説**

保存処理実行中イベント

---

### onSaveLayerImageDone

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ハンドラ |
| `canceled` | `&nbsp;` | キャンセルされたら1 |
| `layer` | `&nbsp;` |  |
| `filename` | `&nbsp;` | ファイル名 |

**解説**

保存処理実行完了イベント

---

## プラグイン拡張: menu

### メンバー一覧

#### プロパティ

- [menu](#menu)

---

### menu

プロパティ \ アクセス: `r`

**解説**

ルートメニューオブジェクト

ルートメニューオブジェクト ( Menu クラスのオブジェクト ) を表します。
このルートメニューオブジェクトの子として登録されたメニューはメニューバーに並ぶことになります。

---

## プラグイン拡張: messenger

擬似コードによるマニュアル

同一マシン上で起動している吉里吉里間での相互通信機能および
外部アプリからの通信機能を提供します。
やりとりされる データは WM_COPYDATA を用いて転送されます。

### メンバー一覧

#### プロパティ

- [messageEnable](#messageenable)
- [storeHWND](#storehwnd)

#### メソッド

- [registerUserMessageReceiver](#registerusermessagereceiver)
- [sendUserMessage](#sendusermessage)
- [sendUserMessageDirect](#sendusermessagedirect)
- [postUserMessage](#postusermessage)
- [postUserMessageDirect](#postusermessagedirect)
- [sendMessage](#sendmessage)
- [sendMessageDirect](#sendmessagedirect)
- [onMessageReceived](#onmessagereceived)

---

### messageEnable

プロパティ \ アクセス: `r/w`

**解説**

メッセージ受信機能が有効かどうかを指定します。

true にするとメッセージを受信するようになります。
メッセージ受信が有効なら true

---

### storeHWND

プロパティ \ アクセス: `r/w`

**解説**

HWND 情報を保存するかどうかを指定します。

これの値を指定すると、実行ファイル名.キーの値 という名前の
ファイルが作成され、その中に現在の HWND 情報が出力されるようになります。
外部アプリケーションからメッセージを送りたい場合は、このファイルに
記録された HWND を参照することができます。
フルスクリーン時など、HWND が変わった時には内容が自動的に更新されます。
このため、外部アプリケーションは送るときは毎回 HWND の値を参照しなおす必要があります。

---

### registerUserMessageReceiver

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` | wrmRegister=0:登録 wrmUnRegister=1:解除 |
| `msg` | `&nbsp;` | 数値:メッセージ番号 文字列:RegisterWindowMessage して値を決定 |
| `proc` | `&nbsp;` | 呼び出しファンクション |
| `userdata` | `&nbsp;` | ユーザデータパラメータ |

**戻り値**

登録されたメッセージ番号を返す

**解説**

ユーザ定義のメッセージハンドラを登録します。

※TJS2 から関数を登録した場合（typeof proc == Object の場合)
function receiver(userdata, wparam, lparam)
の形式のファンクションであるとみなされます。
この時、userdata は渡した値そのままを、
wparam, lparam は元メッセージのデータから整数にキャストした値を渡します。

※TJS2 から文字列を登録した場合 (typeof proc == String の場合)
該当オブジェクトの指定された文字列の関数を function name(userdata, wparam, lparam)
の引数で呼びだします

※プラグイン側から関数を登録する場合 (typeof proc == Integer の場合)
static bool __stdcall receiver(iTJSDispatch2 *winobj, void *userdata, tTVPWindowMessage *Message)
であるとみなされます。設定時は整数にキャストしてください。
winobj は該当するウインドウのオブジェクトです
userdata は整数にキャストした値でひきわたされます。

---

### sendUserMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | メッセージ番号 |
| `wparam` | `&nbsp;` | WPARAM (整数扱いで処理されます) |
| `lparam` | `&nbsp;` | LPARAM (整数扱いで処理されます) |

**解説**

低レベルメッセージ送信を実行します。

全吉里吉里に指定のメッセージが送信されます

---

### sendUserMessageDirect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND数値 |
| `msg` | `&nbsp;` | メッセージ番号 |
| `wparam` | `&nbsp;` | WPARAM (整数扱いで処理されます) |
| `lparam` | `&nbsp;` | LPARAM (整数扱いで処理されます) |

**解説**

HWNDを指定して低レベルメッセージ送信を実行します。

特定のウインドウに指定のメッセージが送信されます

---

### postUserMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | メッセージ番号 |
| `wparam` | `&nbsp;` | WPARAM (整数扱いで処理されます) |
| `lparam` | `&nbsp;` | LPARAM (整数扱いで処理されます) |

**解説**

低レベルメッセージをポストします。

全吉里吉里に指定のメッセージがポストされます

---

### postUserMessageDirect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND数値 |
| `msg` | `&nbsp;` | メッセージ番号 |
| `wparam` | `&nbsp;` | WPARAM (整数扱いで処理されます) |
| `lparam` | `&nbsp;` | LPARAM (整数扱いで処理されます) |

**解説**

HWNDを指定して低レベルメッセージをポストします。

特定のウインドウに指定のメッセージがポストされます

---

### sendMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 識別キー(文字列:256文字までなので注意) |
| `message` | `&nbsp;` | メッセージ(文字列) |

**解説**

メッセージの送信を行います。

起動している吉里吉里すべてに WM_COPYDATA メッセージを送信します。
識別キーとメッセージの意味はそれぞれのアプリで適当に定めてください。

---

### sendMessageDirect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND数値 |
| `key` | `&nbsp;` | 識別キー(文字列:256文字までなので注意) |
| `message` | `&nbsp;` | メッセージ(文字列) |

**解説**

HWNDを指定してメッセージの送信を行います。

指定したウインドウに WM_COPYDATA メッセージを送信します。
受け取る側はsendMessageと共通の処理のため識別キーは必ず指定してください

---

### onMessageReceived

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 識別キー(文字列:256文字までなので注意) |
| `message` | `&nbsp;` | メッセージ(文字列) |

**解説**

イベント：メッセージ受信。

ほかの吉里吉里、あるいは外部アプリから WM_COPYDATA メッセージを受信したときに呼び出されます
呼び出し元はこれの呼び出しが終了するまでロックされてしまうため、
速やかに処理を終了するようにしてください。

---

## プラグイン拡張: shellExecute

擬似コードによるマニュアル

外部アプリを機動してその終了を待つ機構を提供します。
ウインドウメッセージとして WM_APP + 1 を利用しています

### メンバー一覧

#### メソッド

- [shellExecute](#shellexecute)
- [terminateProcess](#terminateprocess)
- [onShellExecuted](#onshellexecuted)
- [commandExecute](#commandexecute)
- [commandSendSignal](#commandsendsignal)
- [onCommandLineOutput](#oncommandlineoutput)

---

### shellExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | プログラム |
| `param` | `&nbsp;` | 引数 |

**戻り値**

プロセスハンドル（失敗した場合は-1)。terminateProcess に渡すことができます。

**解説**

バックグラウンドでの外部プログラムの実行

処理がおわったら onShellExecuted イベントが発生します。

---

### terminateProcess

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `process` | `&nbsp;` | プロセスハンドル |
| `endCode` | `&nbsp;` | 終了コード |

**解説**

実行中の外部プログラムの強制終了

---

### onShellExecuted

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `process` | `&nbsp;` | プロセスハンドル |
| `endCode` | `&nbsp;` | 終了コード |

**解説**

イベント:シェル実行終了

---

### commandExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | プログラム |
| `param` | `&nbsp;` | 引数 |

**戻り値**

プロセスハンドル（失敗した場合は-1)。terminateProcess に渡すことができます。

**解説**

コンソール出力取得つきコマンドラインプログラムの実行

コンソールの行単位出力で onCommandLineOutput イベントが発生します。
処理がおわったら onShellExecuted イベントが発生します。

---

### commandSendSignal

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `process` | `&nbsp;` | プロセスハンドル（commandExecuteしたプロセスのみ） |
| `isBreak` | `&nbsp;` | Ctrl+CではなくCtrl+Breakを送る |

**戻り値**

成功したらtrue

**解説**

Ctrl+Cイベントの送信(experimental:すべての環境で動作するとは限りません)

---

### onCommandLineOutput

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `process` | `&nbsp;` | プロセスハンドル |
| `text` | `&nbsp;` | 出力テキスト（１行単位） |

**解説**

イベント:コンソール出力

---

## プラグイン拡張: sigcheck

擬似コードによるマニュアル

バックグラウンドで署名チェックを行います。
ウインドウメッセージとして WM_APP + 2 と WM_APP + 3 を利用しています

### メンバー一覧

#### メソッド

- [checkSignature](#checksignature)
- [cancelCheckSignature](#cancelchecksignature)
- [stopCheckSignature](#stopchecksignature)
- [onCheckSignatureProgress](#onchecksignatureprogress)
- [onCheckSignatureDone](#onchecksignaturedone)

---

### checkSignature

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 確認対象ファイル |
| `publickey` | `&nbsp;` | 公開鍵 |
| `info` | `&nbsp;` | ユーザ情報 |

**戻り値**

handler 識別ハンドラ

**解説**

署名チェックの開始

処理中に onCheckSignatureProgress、
終了時に onCheckSignatureDone イベントが発生します。
exe や dll の場合は署名はファイルに内臓されます。xp3 などの場合は、
元のファイルに .sig をつけた外部ファイルを署名として処理されます。

---

### cancelCheckSignature

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 識別ハンドラ |

**解説**

署名チェックのキャンセル

実行中の署名チェックを速やかに停止させます。キャンセル終了になります。

---

### stopCheckSignature

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 識別ハンドラ |

**解説**

署名チェックの中止

実行中の署名チェックを速やかに停止させます。終了イベントは来ません。

---

### onCheckSignatureProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 識別ハンドラ |
| `info` | `&nbsp;` | ユーザ情報 |
| `percent` | `&nbsp;` | 進捗度合い 0〜100% |

**解説**

イベント:署名チェック進捗

---

### onCheckSignatureDone

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 識別ハンドラ |
| `info` | `&nbsp;` | ユーザ情報 |
| `result` | `&nbsp;` | 結果 -2:エラー -1:キャンセル 0:チェック失敗 1:チェック成功 |
| `errormsg` | `&nbsp;` | 結果がエラーの場合のエラーメッセージ |

**解説**

イベント:署名チェック終了

---

## プラグイン拡張: windowEx

Window拡張

### メンバー一覧

#### プロパティ

- [maximized](#maximized)
- [minimized](#minimized)
- [disableResize](#disableresize)
- [exSystemMenu](#exsystemmenu)
- [enableNCMouseEvent](#enablencmouseevent)

#### メソッド

- [maximize](#maximize)
- [minimize](#minimize)
- [showRestore](#showrestore)
- [resetWindowIcon](#resetwindowicon)
- [setWindowIcon](#setwindowicon)
- [setWindowCornerPreference](#setwindowcornerpreference)
- [getClientRect](#getclientrect)
- [getWindowRect](#getwindowrect)
- [getNormalRect](#getnormalrect)
- [setClientRect](#setclientrect)
- [bringTo](#bringto)
- [sendToBack](#sendtoback)
- [acquireImeControl](#acquireimecontrol)
- [resetImeContext](#resetimecontext)
- [registerExEvent](#registerexevent)
- [onMaximizeQuery](#onmaximizequery)
- [onMaximize](#onmaximize)
- [onMinimize](#onminimize)
- [onShow](#onshow)
- [onHide](#onhide)
- [onMoveSizeBegin](#onmovesizebegin)
- [onMoveSizeEnd](#onmovesizeend)
- [onMoving](#onmoving)
- [onMove](#onmove)
- [onResizing](#onresizing)
- [forceResizeRect](#forceresizerect)
- [onDisplayChanged](#ondisplaychanged)
- [onDPIChanged](#ondpichanged)
- [onEnterMenuLoop](#onentermenuloop)
- [onExitMenuLoop](#onexitmenuloop)
- [onScreenSave](#onscreensave)
- [onMonitorPower](#onmonitorpower)
- [onDeviceChanged](#ondevicechanged)
- [registerDeviceChange](#registerdevicechange)
- [onHotKeyPressed](#onhotkeypressed)
- [registerHotKey](#registerhotkey)
- [onActivateChanged](#onactivatechanged)
- [setOverlayBitmap](#setoverlaybitmap)
- [onNcMouseMove](#onncmousemove)
- [onNcMouseUp](#onncmouseup)
- [onNcMouseDown](#onncmousedown)
- [onNcMouseLeave](#onncmouseleave)
- [ncHitTest](#nchittest)
- [onNonCapMouseEvent](#onnoncapmouseevent)
- [focusMenuByKey](#focusmenubykey)
- [onStartKeyMenu](#onstartkeymenu)
- [onAccelKeyMenu](#onaccelkeymenu)
- [setMessageHook](#setmessagehook)
- [onWindowsMessageHook](#onwindowsmessagehook)
- [getNotificationNum](#getnotificationnum)
- [getNotificationName](#getnotificationname)

#### 定数

- [nchtError](#nchterror)
- [nchtTransparent](#nchttransparent)
- [nchtNoWhere](#nchtnowhere)
- [nchtClient](#nchtclient)
- [nchtCaption](#nchtcaption)
- [nchtSysMenu](#nchtsysmenu)
- [nchtSize](#nchtsize)
- [nchtGrowBox](#nchtgrowbox)
- [nchtMenu](#nchtmenu)
- [nchtHScroll](#nchthscroll)
- [nchtVScroll](#nchtvscroll)
- [nchtMinButton](#nchtminbutton)
- [nchtReduce](#nchtreduce)
- [nchtMaxButton](#nchtmaxbutton)
- [nchtZoom](#nchtzoom)
- [nchtLeft](#nchtleft)
- [nchtRight](#nchtright)
- [nchtTop](#nchttop)
- [nchtTopLeft](#nchttopleft)
- [nchtTopRight](#nchttopright)
- [nchtBottom](#nchtbottom)
- [nchtBottomLeft](#nchtbottomleft)
- [nchtBottomRight](#nchtbottomright)
- [nchtBorder](#nchtborder)

---

### maximized

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウが最大化かどうか取得

setterも一応あるが使わないことを推奨

---

### minimized

プロパティ \ アクセス: `r/w`

**解説**

ウィンドウが最小化かどうか取得

---

### disableResize

プロパティ \ アクセス: `r/w`

**解説**

リサイズの抑制

setter は registerExEvent() で拡張イベントを登録していないと例外が発生する
true に設定すると，borderStyle == bsSizeable の場合でも
・ウィンドウ淵のサイズ変更カーソルが出なくなりサイズが変更できなくなる
・システムメニュー(Alt+Space)のサイズ変更がグレーになり選択できなくなる
最大化など他の方法でのサイズ変更は有効(onResizeも飛ぶ)

---

### exSystemMenu

プロパティ \ アクセス: `r/w`

**解説**

システムメニューに追加

setter は registerExEvent() で拡張イベントを登録していないと例外が発生する
MenuItemまたは辞書の配列を指定する
このメニューが選択されると onExSystemMenuSelected(選択されたオブジェクト) コールバックが発生

---

### enableNCMouseEvent

プロパティ \ アクセス: `r/w`

**解説**

以下特殊用途 WM_SETCURSORのコールバックonNonCapMouseEventを有効にする（デフォルト：false）

---

### maximize

メソッド

**解説**

ウィンドウの最大化

最大化ボタンを押した動作と同等
サイズ固定ウィンドウでは機能しない

---

### minimize

メソッド

**解説**

ウィンドウの最小化（mainWindowではタスクバー収納，それ以外は画面左下に最小化）

最小化ボタンを押した動作と同等

---

### showRestore

メソッド

**解説**

ウィンドウ最大化・最小化の復帰

---

### resetWindowIcon

メソッド

**解説**

ウィンドウのタイトルバーアイコンを再設定する

※ Vista でフルスクリーンから復帰するとアイコンが消える問題（吉里吉里v2.30で確認）の消極的対処メソッド

---

### setWindowIcon

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | アイコンファイルまたはvoid (voidか""で初期状態にリセット） |
| `withapp` | `&nbsp;` | アプリケーションウィンドウのアイコンも一緒に変更するかどうか |

**解説**

ウィンドウのタイトルバーアイコンを変更する

※ アーカイブ内のファイル指定は不可，exeやDLLを指定した場合は一番最初のアイコンが設定される

---

### setWindowCornerPreference

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `0` | DWMWCP_* の値 (0=DEFAULT, 1=DONOTROUND, 2=ROUND, 3=ROUNDSMALL) |

**戻り値**

成功したらtrue

**解説**

ウィンドウの角の形状を変更する

※ Windows 11 Build 22000 以降で使用可能

---

### getClientRect

メソッド

**戻り値**

%[ x, y, w, h ] または void(取得失敗時)

**解説**

クライアント・ウィンドウ領域，非最大化通常表示の領域の取得

※ innerSunken枠分はクライアント領域に含まれるので注意
クライアント領域

---

### getWindowRect

メソッド

**解説**

ウィンドウ領域

---

### getNormalRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `nofix` | `false` |  |

**解説**

非最大化通常表示領域(@param nofix true:ワークエリア補正を行わない)

---

### setClientRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x,y,w,h ] |

**解説**

クライアント領域の設定

---

### bringTo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `win` | `"top"` | Windowオブジェクトまたは規定文字列または数値<br>Windowオブジェクトなら，そのウィンドウの後ろに置かれる<br>文字列の場合，"bottom" "notopmost" "top" "topmost" のいずれか（HWND_*相当）cf. SetWindowPos API<br>数値の場合，ウィンドウハンドルと見なすか，HWND_* マクロの値を直指定する<br>#define HWND_TOP        ((HWND)0)<br>#define HWND_BOTTOM     ((HWND)1)<br>#define HWND_TOPMOST    ((HWND)-1)<br>#define HWND_NOTOPMOST  ((HWND)-2) |
| `activate` | `false` | アクティブ状態にするかどうかのフラグ<br>trueにしてもアプリケーション自体はアクティブになりません（タスクバーの点滅などおこりません） |

**解説**

ウィンドウの Zオーダーを変更する

---

### sendToBack

メソッド

**解説**

/ alias method

---

### acquireImeControl

メソッド

**戻り値**

成功した場合はtrue

**解説**

IMEを再設定する(吉里吉里Z専用)

実行環境が 吉里吉里Z の場合にTVP_WM_ACQUIREIMECONTROLをポストする

---

### resetImeContext

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `defval` | `true` | true:IACE_DEFAULT, false:NULL |

**戻り値**

成功した場合はtrue

**解説**

IMEコンテキストを再設定する

imDisableが再実装された場合や複数ウインドウでテキスト入力を使う場合に吉里吉里Z本体側(ImeControl.h)の設定と競合する可能性あり

---

### registerExEvent

メソッド

**解説**

拡張イベントを有効にする

このウィンドウのインスタンスについて
説明に「■拡張イベント：」と記述されているコールバックが有効になる

ただし、下記のコールバックについては
この関数を実行した時点でインスタンスに存在しない場合には発生しないので注意
（ない場合は後からインスタンスに関数を追加しても呼ばれない）
onMoving      移動中
onMove        移動
onResizing    リサイズ中
onNcMouseMove NonClient領域でのマウス移動

---

### onMaximizeQuery

メソッド

**戻り値**

true を返すと最大化を許可しない

**解説**

■拡張イベント：最大化を許可するかどうか確認

---

### onMaximize

メソッド

**解説**

■拡張イベント：ウィンドウ最大化

呼ばれた時点でウィンドウサイズは既に最大化されている

---

### onMinimize

メソッド

**解説**

■拡張イベント：ウィンドウ最小化

フルスクリーン中にAlt+Tabなどで別のアプリを選んだ場合や，mainWindow以外が最小化されたときに呼ばれる
タスクバーに収納された場合は onHide イベントが呼ばれるので注意

---

### onShow

メソッド

**解説**

■拡張イベント：ウィンドウ表示

タスクバーから復帰したときなどに呼ばれる

---

### onHide

メソッド

**解説**

■拡張イベント：ウィンドウ非表示

タスクバーに収納された時などに呼ばれる

---

### onMoveSizeBegin

メソッド

**解説**

■拡張イベント：リサイズ・移動開始通知/終了

フレームやタイトルバーをドラッグ開始した時やAlt+SpaceでSやMを選んだ時（開始通知），
および移動やリサイズが終了した時（終了通知）にそれぞれ呼ばれる
onMovingやonResizing中に元のウィンドウ位置やサイズを参照したい時はここで保存しておくとよい
リサイズか移動かは WM_ENTERSIZEMOVE/WM_EXITSIZEMOVE の都合で判定不可

---

### onMoveSizeEnd

メソッド

**解説**

終了通知

---

### onMoving

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h ] ウィンドウ座標 |

**解説**

■拡張イベント：ウィンドウ移動中

※Windowsでウィンドウ内容を表示したまま移動する設定（移動枠表示なし）の場合，すぐにonMoveが呼ばれる

---

### onMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

■拡張イベント：ウィンドウ移動（完了）

---

### onResizing

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h, type ] 変更中サイズ（ウィンドウ座標） |

**戻り値**

true を返すと rect の変更を反映（位置・サイズを強制指定）
この場合，つかんだ位置(rect.type)に応じてうまく書き換え内容を調整しないと
サイズ変更中にウィンドウが動いてしまうことがあるので注意（⇒forceResizeRect()参照）

**解説**

■拡張イベント：サイズ変更中

※Windowsでウィンドウ内容を表示したままリサイズする設定（サイズ枠表示なし）の場合，すぐにonResizeが呼ばれる

---

### forceResizeRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### onDisplayChanged

メソッド

**解説**

■拡張イベント：ディスプレイ構成の変更通知

解像度や色数、マルチモニタの構成（位置変更も含む）が変更されたときに呼ばれる

---

### onDPIChanged

メソッド

**解説**

■拡張イベント：ウィンドウのDPI変更通知

DPIの設定を変えたりDPI値の異なるモニタ間を移動した場合に通知

---

### onEnterMenuLoop

メソッド

**解説**

■拡張イベント：メニュー処理の開始・終了通知

ウィンドウのメニュー処理（クリックやF10を押した場合など）の開始と終了の通知イベント
WM_ENTERMENULOOP / WM_EXITMENULOOP 通知のコールバック

※フルスクリーンにした場合のメニューではこのイベントは発生しないので注意！

---

### onExitMenuLoop

メソッド

**解説**

メニュー処理終了

---

### onScreenSave

メソッド

**戻り値**

true を返すと制御抑制

**解説**

■拡張イベント：スクリーンセーバー開始通知，モニタパワー変更通知

---

### onMonitorPower

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### onDeviceChanged

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `arrival` | `&nbsp;` | trueならデバイスが追加された, falseなら外された<br>※registerExEvent()が呼んでいてかつregisterDeviceChange()を呼んでおく必要があるので注意 |

**解説**

■拡張イベント：デバイス追加・リムーブ通知

---

### registerDeviceChange

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `guid` | `GUID_DEVINTERFACE_HID` | GUIDを示したoctet値（省略時HIDデバイスクラス）<br>※登録できるGUIDはウィンドウにつき1つまでなので注意 |

**解説**

onDeviceChanged拡張イベントを有効にする

---

### onHotKeyPressed

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | registerHotKeyで登録したID |
| `mod` | `&nbsp;` | モディファイアキー(ssShift, ssAlt, ssCtrl 等の組み合わせ） |

**解説**

■拡張イベント：ホットキーの入力

---

### registerHotKey

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 登録するID (※0x0000～0xBFFFまで） |
| `key` | `&nbsp;` |  |
| `mod` | `&nbsp;` | モディファイアキー(ssShift, ssAlt, ssCtrl 等の組み合わせ） |

**戻り値**

登録出来たらtrue

**解説**

ホットキーを登録する

---

### onActivateChanged

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `active` | `&nbsp;` | 0:非アクティブ化 1:マウスクリック以外でアクティブ化 2:マウスクリックでアクティブ化 |
| `minimize` | `&nbsp;` | 0:ウィンドウは最小化されていない それ以外:最小化されている |

**解説**

■拡張イベント：アクティブ状態変更通知

※Window.onActivate や Window.onDeactivate と違うのは、（これは拡張イベント全般に言えることだが）
System.eventDisabled == true でもイベントコールバックが飛んでくるという点

例えば System.onDeactivate 時に System.eventDisabled=true（こうすると System.onActivateは
飛んでこない）にして，このイベント通知で復帰させると「非アクティブ時に動作停止」といった機能を
追加できるかもしれない（ただしこれはイベントを配信停止するだけなので，前との時間差を見るような
タイマーを使ったアプリではあまり意味が無い）
なお，System.eventDisabled=true 時は画面更新すら走らないので，他のウィンドウを上にするなどして
WM_PAINT が発生すると画面が崩れる問題がある（後述の OverlayBitmap を使うなどする）

---

### setOverlayBitmap

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | ビットマップ画像にコピーするレイヤ（void or省略時はオーバーレイ消去） |

**解説**

オーバーレイビットマップを表示・消去する

指定画像でクライアント領域に子ウィンドウ（吉里吉里のではなくWindowsのそれ）をかぶせる
・拡張イベントが有効でないと例外が発生する
・オーバーレイ表示中は吉里吉里のレイヤ側にマウス系のメッセージが一切行かない
・実質的に System.eventDisabled=true の時専用
・TVP_WM_DETACH で自動消去される

---

### onNcMouseMove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `ht` | `&nbsp;` | 領域の種類（NCHITTEST定数） |

**解説**

■拡張イベント：非クライアントエリアマウスイベント

---

### onNcMouseUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseLeave

メソッド

---

### ncHitTest

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

非クライアントエリア調査

---

### onNonCapMouseEvent

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `ht` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**解説**

WM_SETCURSORコールバック：ht=LOWORD(LParam), ev=HIWORD(LParam)

---

### focusMenuByKey

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**解説**

SC_KEYMENUを送る

---

### onStartKeyMenu

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**解説**

SC_KEYMENU通知コールバック

---

### onAccelKeyMenu

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |
| `st` | `&nbsp;` |  |

**解説**

WM_MENUCHAR通知コールバック

---

### setMessageHook

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `on` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**解説**

メッセージフックを設定(on:有効, ev:イベント番号またはイベント名文字：省略時全部）

---

### onWindowsMessageHook

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wp` | `&nbsp;` |  |
| `lp` | `&nbsp;` |  |

**解説**

setMessageHookで指定したイベント発生時のコールバック

---

### getNotificationNum

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

WM_XXXイベント番号を取得（WM_は除いて渡す）

---

### getNotificationName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**解説**

イベント番号からWM_XXXを取得（WM_を除いて返る）

---

### nchtError

定数

**解説**

HTERROR

---

### nchtTransparent

定数

**解説**

HTTRANSPARENT

---

### nchtNoWhere

定数

**解説**

HTNOWHERE

---

### nchtClient

定数

**解説**

HTCLIENT

---

### nchtCaption

定数

**解説**

HTCAPTION

---

### nchtSysMenu

定数

**解説**

HTSYSMENU

---

### nchtSize

定数

**解説**

HTSIZE

---

### nchtGrowBox

定数

**解説**

HTGROWBOX

---

### nchtMenu

定数

**解説**

HTMENU

---

### nchtHScroll

定数

**解説**

HTHSCROLL

---

### nchtVScroll

定数

**解説**

HTVSCROLL

---

### nchtMinButton

定数

**解説**

HTMINBUTTON

---

### nchtReduce

定数

**解説**

HTREDUCE

---

### nchtMaxButton

定数

**解説**

HTMAXBUTTON

---

### nchtZoom

定数

**解説**

HTZOOM

---

### nchtLeft

定数

**解説**

HTLEFT

---

### nchtRight

定数

**解説**

HTRIGHT

---

### nchtTop

定数

**解説**

HTTOP

---

### nchtTopLeft

定数

**解説**

HTTOPLEFT

---

### nchtTopRight

定数

**解説**

HTTOPRIGHT

---

### nchtBottom

定数

**解説**

HTBOTTOM

---

### nchtBottomLeft

定数

**解説**

HTBOTTOMLEFT

---

### nchtBottomRight

定数

**解説**

HTBOTTOMRIGHT

---

### nchtBorder

定数

**解説**

HTBORDER

---

## プラグイン拡張: windowExProgress

ウインドウ拡張

### メンバー一覧

#### メソッド

- [startProgress](#startprogress)
- [doProgress](#doprogress)
- [setProgressMessage](#setprogressmessage)
- [endProgress](#endprogress)

#### 定数

- [PBS_SMOOTH](#pbs_smooth)
- [PBS_VERTICAL](#pbs_vertical)

---

### startProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `init` | `&nbsp;` | 初期化データ(辞書) |

**解説**

プログレス処理を開始する。

吉里吉里が実行ブロック中でも正常に表示継続します。
プログレスバー初期化パラメータ
progressBarEnable: プログレスバーを表示するかどうか(デフォルト:true)
progressBarStyle: プログレスバーのスタイル (デフォルト:なし)
progressBarLeft: プログレスバー表示位置X (デフォルト:自動センタリング)
progressBarTop: プログレスバー表示位置Y (デフォルト:自動センタリング)
progressBarWidth: プログレスバー横幅 (デフォルト:ウインドウ横幅の 1/3)
progressBarHeight: プログレスバー縦幅 (デフォルト:ウインドウ縦幅の 1/10)
progressBarColor: プログレスバー色 0xRRGGBB (デフォルト:デフォルト色)
progressBarBackColor: プログレスバー背景色 0xRRGGBB (デフォルト:デフォルト色)

キャンセルボタン初期化パラメータ
cancelButtonEnable: キャンセルボタンを表示するかどうか(デフォルト:true)
cancelButtonCaption: キャンセルボタンに表示するテキスト(デフォルト:Cancel)
cancelButtonLeft: キャンセルボタン表示位置X (デフォルト:自動センタリング)
cancelButtonTop: キャンセルボタン表示位置Y (デフォルト:下から heightの３倍の位置)
cancelButtonWidth: キャンセルボタン横幅 (デフォルト:テキスト文字数*12+8)
cancelButtonHeight: キャンセルボタン縦幅 (デフォルト:20)

背景画像初期化パラメータ(未実装)
backGround: 背景指定 レイヤ：レイヤの画像を直接参照 数値:該当色で塗りつぶし デフォルト:なし

メッセージ初期化パラメータ(未実装)
messages: メッセージ情報またはその配列
left: 表示座標X
top: 表示座標Y
text: 初期表示テキスト
size: 表示サイズ
color: 表示カラー
shadowColor: 影色
shadowDistanceX: 影のずれ指定
shadowDistanceY: 影のずれ指定
font: フォント指定
fontStyle: フォントスタイル

---

### doProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `percent` | `&nbsp;` | 経過状態をパーセント指定 |

**戻り値**

キャンセル要求があれば true

**解説**

プログレス処理の経過状態を通知する。

---

### setProgressMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | テキストID(登録順) |
| `text` | `&nbsp;` | 表示テキスト |

**解説**

プログレス処理のテキストを差し替える

---

### endProgress

メソッド

**解説**

プログレス処理を終了する。

---

### PBS_SMOOTH

定数

値: `1`

**解説**

プログレスバースタイル指定 プログレスバースムーズ指定

---

### PBS_VERTICAL

定数

値: `4`

**解説**

プログレスバー垂直配置指定

---
