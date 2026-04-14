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

---

### Window

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `parent` | `&nbsp;` | 親ウィンドウを指定します。 親ウィンドウを指定すると、その子ウィンドウとして生成されます。 指定しない場合は省略します。 |

**解説**

Window クラスのオブジェクトを構築します。

ウィンドウは非表示の状態で作成され、位置やサイズは未定義 ( どこかにの位置に適当なサイズ ) です。

---

### onMouseEnter

イベント

**解説**

マウスがウィンドウのクライアント領域内に入ってきたときに発生します。

**関連:** [Window.onMouseLeave](Window.md#onmouseleave)

---

### onMouseLeave

イベント

**解説**

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
| `button` | `&nbsp;` | 押されたマウスボタンです。以下のいずれかの値になります。 `**mbLeft** : `マウスの左ボタンが押された `**mbMiddle** : `マウスの中ボタンが押された `**mbRight** : `マウスの右ボタンが押された `**mbX1** : `マウスのサイドキー第1ボタンが押された `**mbX2** : `マウスのサイドキー第2ボタンが押された |
| `shift` | `&nbsp;` | マウスボタンが押されたときに同時に押されていたシフト系のキーの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた |

**解説**

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
| `button` | `&nbsp;` | 離されたマウスボタンです。以下のいずれかの値になります。 `**mbLeft** : `マウスの左ボタンが離された `**mbMiddle** : `マウスの中ボタンが離された `**mbRight** : `マウスの右ボタンが離された `**mbX1** : `マウスのサイドキー第1ボタンが離された `**mbX2** : `マウスのサイドキー第2ボタンが離された |
| `shift` | `&nbsp;` | マウスボタンが離された時に同時に押されていたシフト系のキーの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた |

**解説**

マウスボタンが離された時に発生します。

---

### onMouseMove

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | マウスが移動した位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | マウスが移動した位置の y 座標 ( クライアント座標での ) の値です。 |
| `shift` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた `**ssLeft** : `マウスの左ボタンが押されていた `**ssMiddle** : `マウスの中ボタンが押されていた `**ssRight** : `マウスの右ボタンが押されていた |

**解説**

マウスが移動した時に発生します。

---

### onMouseWheel

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | マウスが移動していた時に同時に押されていたシフト系のキーやマウスのボタンの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた `**ssLeft** : `マウスの左ボタンが押されていた `**ssMiddle** : `マウスの中ボタンが押されていた `**ssRight** : `マウスの右ボタンが押されていた |
| `delta` | `&nbsp;` | ホイールの回転角です。上方向(ユーザの反対側の方向)に回された場合は正、 下方向(ユーザ側の方向)に回された場合は負の値になります。通常、最小量は 120 となります。 |
| `x` | `&nbsp;` | ホイールが回転した位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | ホイールが回転した位置の y 座標 ( クライアント座標での ) の値です。 |

**解説**

マウスホイールが回転した時に発生します。

---

### onTouchDown

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチされた位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | タッチされた位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。 マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

タッチパネルにタッチされた時に発生します。

---

### onTouchUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 離された位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | 離された位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。 マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

タッチパネルから指が離された時に発生します。

---

### onTouchMove

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | タッチ位置の x 座標 ( クライアント座標での ) の値です。 |
| `y` | `&nbsp;` | タッチ位置の y 座標 ( クライアント座標での ) の値です。 |
| `cx` | `&nbsp;` | 指が接触している横方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `cy` | `&nbsp;` | 指が接触している縦方向ピクセル数です。 デバイスが対応していない場合は常に1です。 |
| `id` | `&nbsp;` | タッチIDです。 マルチタッチ時、各位置ごとに固有の値が設定され、このIDによって位置を識別できます。 |

**解説**

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
| `flag` | `&nbsp;` | マルチタッチ状態フラグです。 `**0x01** : `マルチタッチが開始された最初のイベントに設定されています。 |

**解説**

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
| `flag` | `&nbsp;` | マルチタッチ状態フラグです。 `**0x01** : `マルチタッチが開始された最初のイベントに設定されています。 |

**解説**

タッチパネル上でマルチタッチによって回転操作した時に発生します。

---

### onMultiTouch

イベント

**解説**

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
| `shift` | `&nbsp;` | キーが押された時に同時に押されていたシフト系のキーやマウスのボタンの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた `**ssLeft** : `マウスの左ボタンが押されていた `**ssMiddle** : `マウスの中ボタンが押されていた `**ssRight** : `マウスの右ボタンが押されていた また、キーボードが長時間押され、キーリピートが発生している場合は 以下の値も組み合わされます。 `**ssRepeat** : `キーリピートが発生した |

**解説**

キーが押された時に発生します。

---

### onKeyUp

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 離されたキーの**仮想キーコード**の値です。 |
| `shift` | `&nbsp;` | キーが離された時に同時に押されていたシフト系のキーやマウスのボタンの状態です。 以下の値のビット OR による組み合わせになります。 `**ssAlt** : `ALT キーが押されていた `**ssShift** : `SHIFT キーが押されていた `**ssCtrl** : `CTRL キーが押されていた `**ssLeft** : `マウスの左ボタンが押されていた `**ssMiddle** : `マウスの中ボタンが押されていた `**ssRight** : `マウスの右ボタンが押されていた |

**解説**

キーが離された時に発生します。

---

### onKeyPress

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 入力された文字です。 |

**解説**

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

ファイルがエクスプローラなどからウィンドウにドロップされたときに発生します。

単一のファイルがドロップされた場合でも引数には配列オブジェクトが渡されます (最初の要素が
そのファイルになります )。

---

### onCloseQuery

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `canclose` | `&nbsp;` | ウィンドウを閉じることができるかどうかが渡されます。下位クラスから上位クラスのイベントハンドラが 呼ばれる課程で、下位クラスが決定した「ウィンドウを閉じることができるか」が渡されます。 |

**解説**

ウィンドウを閉じることができるかどうかを確認するためのイベントです。ウィンドウを閉じることが
できない場合、上位クラスの同メソッドに引数として false を渡してください。

---

### onPopupHide

イベント

**解説**

ポップアップウィンドウが閉じるべき時に発生するイベントです。このイベントは、[Window.stayOnTop](Window.md#stayontop) プロパティが真で、かつ、[Window.focusable](Window.md#focusable) プロパティが偽の場合、「他のウィンドウがクリックされた」あるいは「他のアプリケーションがアクティブになった」時に発生します。

通常は、ここでウィンドウを閉じたり、非表示にする処理を行ってください。

**関連:** [Window.focusable](Window.md#focusable) / [Window.stayOnTop](Window.md#stayontop)

---

### onActivate

イベント

**解説**

ウィンドウがアクティブになったときに呼び出されるイベント関数を表します。

このイベントは、ウィンドウが既にアクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [Window.onDeactivate](Window.md#ondeactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onDeactivate

イベント

**解説**

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
| `orientation` | `&nbsp;` | 画面の向き( orientation ) です。 以下のいずれかの値になります。 oriUnknown (取得失敗/不明), oriPortrait(縦向き), oriLandscape(横向き) |
| `angle` | `&nbsp;` | 角度です。 角度 ( angle ) は、0、90、180、270、-1 のいずれかで、取得できなかった時は-1となります。 角度は、そのデバイスデフォルトからの回転角なので、縦向きのデバイスでは縦向きで0となります。 通常のデバイスだと、横向きで0が多ようです。 縦向きが0になるのは最近の8インチタブレットなどで、縦向きが標準の向きとなっているものです。 |
| `bpp` | `&nbsp;` | bits per pixel です。 |
| `width` | `&nbsp;` | 画面の幅です。 |
| `height` | `&nbsp;` | 画面の高さです。 |

**解説**

画面が回転されたときに呼び出されるイベント関数を表します。

**関連:** [Window.displayOrientation](Window.md#displayorientation) / [Window.displayRotate](Window.md#displayrotate)

---

### close

メソッド

**解説**

[Window.showModal](Window.md#showmodal) メソッドで表示されたウィンドウを閉じます。ウィンドウを閉じる前に [Window.onCloseQuery](Window.md#onclosequery) イベントが発生し、ウィンドウを閉じることができるかどうかを確認することができます。

**関連:** [Window.showModal](Window.md#showmodal) / [Window.onCloseQuery](Window.md#onclosequery)

---

### bringToFront

メソッド

**解説**

ウィンドウを最前面に移動します。アプリケーションが非アクティブの場合はアプリケーション
自体もアクティブにします。

---

### update

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `tutNormal` | ウィンドウ描画のタイプを指定します。 `**tutNormal**` を指定すると通常の描画 ( 差分描画 )、 `**tutEntire**` を指定するとウィンドウ内容全体を描画します。 |

**解説**

引数は現バージョンでは無視されます。

tutNormal や tutEntire は実装されていません。

---

### showModal

メソッド

**解説**

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
| `threshold` | `1` | マスクのスレッショルド ( 敷居値 ) を指定します。 プライマリレイヤのマスク ( レイヤの不透明度の情報 ) のうち、この値よりも大きい部分の形に ウィンドウが切り取られて表示されます。 |

**解説**

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

ウィンドウの最大サイズを指定します。ウィンドウはこのメソッドで指定したサイズより大きくなることはできません。

**関連:** [Window.setMixSize](Window.md#setmixsize) / [Window.setSize](Window.md#setsize) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight)

---

### setPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` | ウィンドウの左端位置を指定します。 |
| `top` | `&nbsp;` | ウィンドウの上端位置を指定します。 |

**解説**

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
| `eventname` | `&nbsp;` | イベント名称を指定します。以下の文字列で指定します。 "**onKeyDown**" は [Window.onKeyDown](Window.md#onkeydown) イベントを生成します。 "**onKeyPress**" は [Window.onKeyPress](Window.md#onkeypress) イベントを生成します。 "**onKeyUp**" は [Window.onKeyUp](Window.md#onkeyup) イベントを生成します。onKeyDownとonKeyUpは対になるので、onKeyDownを生成したら対応するonKeyUpも生成することを推奨します。 |
| `params` | `null` | イベントのパラメータが格納された辞書配列を指定します。 "onKeyDown" イベントや "onKeyUp" イベントでは、"key" に仮想キーコード、"shift" にシフト状態を格納します。"shift" を省略すると 0 であると見なされます。 "onKeyPress" イベントでは "key" に文字を指定します。 |

**解説**

入力イベントを生成します。現バージョンではキー入力に関する３つのイベントを生成できます。

このメソッドは、イベントを非同期イベントとして生成します。つまり、このメソッドは、対応するイベントハンドラの終了を待たずに帰ります。実際にイベントハンドラが呼ばれて処理が行われるのは、いったん吉里吉里に制御が戻った後となります。

入力イベントは、Windowクラスのほか、通常の入力イベントと同じく、Layerクラスの該当するイベントとしても発生します。

```
postInputEvent('onKeyDown', %[key: VK_UP, shift: ssShift]);
postInputEvent('onKeyUp',   %[key: VK_UP, shift: ssShift]);
	// 左カーソルキーを押す
```

---

### hideMouseCursor

メソッド

**解説**

マウスカーソルを一時的に隠します。マウスを少しでも動かすと
マウスカーソルは再び表示されるようになります。

このメソッドは、[Window.mouseCursorState](Window.md#mousecursorstate)を`**mcsTempHidden**`に設定するのと同じ効果を持ちます。

---

### registerMessageReceiver

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `mode` | `&nbsp;` | 登録するか、登録削除するかどうかを指定します。 **wrmRegister** を指定すると登録になります。**wrmUnregister** を 指定すると登録削除になります。 wrm で始まる定数は tp_stub.h に定義されています。 |
| `func` | `&nbsp;` | メッセージ受信関数を指定します。 メッセージ受信関数は bool __stdcall func(void *userdata, tTVPWindowMessage *Message) の形式である必要があり、このメソッドに渡す際にその関数ポインタを整数型にキャストして渡す 必要があります。 構造体 tTVPWindowMessage は tp_stub.h に定義されています。 この関数が true を返すと吉里吉里本体側はそのウィンドウメッセージに関知しなくなります。 |
| `userdata` | `&nbsp;` | func 引数で指定された受信関数の userdata 引数に渡すためのデータポインタを指定します。 このメソッドに渡す際にはそのポインタを整数型にキャストして渡す必要があります。 この引数は mode 引数が wrmRegister でないときは無視されます。 |

**解説**

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

現在のタッチ移動速度を pixel / sec で取得します。

押下されてから離されるまでの間計測されています。

マルチタッチ対応のため ID ごとに速度計測されています。

[Window.onTouchUp](Window.md#ontouchup) イベントのメソッド呼び出しが終了すると計測している速度情報は消えてしまうので注意が必要です。

**関連:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### resetMouseVelocity

メソッド

**解説**

マウスの座標移動速度計測をリセットします。

リセットすることで任意のタイミングから速度計測を開始することが出来ます。

**関連:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### visible

プロパティ / アクセス: `r/w`

**解説**

ウィンドウが表示されているかどうかを表します。値を設定することもできます。

真ならばウィンドウが表示されていて、偽ならばウィンドウは非表示の状態です。

---

### caption

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの**キャプション** ( タイトルバーのタイトル ) を表します。
値を設定することもできます。

---

### width

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの横幅を表します。値を設定することもできます。

**関連:** [Window.height](Window.md#height) / [Window.setSize](Window.md#setsize)

---

### height

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの縦幅を表します。値を設定することもできます。

**関連:** [Window.width](Window.md#width) / [Window.setSize](Window.md#setsize)

---

### minWidth

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの最小の横幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.width](Window.md#width) / [Window.minHeight](Window.md#minheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### minHeight

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの最小の縦幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.height](Window.md#height) / [Window.minWidth](Window.md#minwidth) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxWidth

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの最大の横幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.width](Window.md#width) / [Window.maxHeight](Window.md#maxheight) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxHeight

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの最大の縦幅を表します。値を設定することもできます。0を指定すると制限は無くなります。

**関連:** [Window.height](Window.md#height) / [Window.maxWidth](Window.md#maxwidth) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### left

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの左端位置を表します。値を設定することもできます。

左端位置はスクリーンの原点 ( 左上隅 ) からの x 座標です。

**関連:** [Window.top](Window.md#top) / [Window.setPos](Window.md#setpos)

---

### top

プロパティ / アクセス: `r/w`

**解説**

ウィンドウの上端位置を表します。値を設定することもできます。

上端位置はスクリーンの原点 ( 左上隅 ) からの y 座標です。

**関連:** [Window.left](Window.md#left) / [Window.setPos](Window.md#setpos)

---

### focusable

プロパティ / アクセス: `r/w`

**解説**

フォーカスを取得可能かどうかを表します。値を設定することもできます。

偽に設定すると、フォーカスを取得できなくなる、つまり、ウィンドウがアクティブにならなくなります。副作用として、タイトルバーをつかんでのウィンドウの移動やウィンドウのリサイズ、「×」ボタンを押してウィンドウを閉じる操作もできなくなります。

キーボード入力を得たいときは [Window.trapKey](Window.md#trapkey) プロパティを使用することができます。

通常、これは、ポップアップメニューのように、もっとも手前に表示されるが、それ自身はフォーカスを得ないウィンドウの実装に用います。

現バージョンでは、ウィンドウがフルスクリーン化するとき、あるいはフルスクリーンから復帰するときに、このプロパティの設定内容が失われる可能性があります。

**関連:** [Window.trapKey](Window.md#trapkey) / [Window.onPopupHide](Window.md#onpopuphide)

---

### trapKey

プロパティ / アクセス: `r/w`

**解説**

キー入力をトラップするかどうかを表します。値を設定することもできます。

真に設定すると、他のウィンドウで発生したキー入力イベントを横取りし、このウィンドウ上で発生させることができます。

複数のウィンドウのこのプロパティが真に設定されている場合は、もっとも最後に作成したウィンドウに対してキー入力イベントが発生します。

**関連:** [Window.focusable](Window.md#focusable)

---

### innerWidth

プロパティ / アクセス: `r/w`

**解説**

クライアント領域の横幅を表します。
値を設定することもできます。

**関連:** [Window.innerHeight](Window.md#innerheight) / [Window.setInnerSize](Window.md#setinnersize)

---

### innerHeight

プロパティ / アクセス: `r/w`

**解説**

クライアント領域の縦幅を表します。
値を設定することもできます。

**関連:** [Window.innerWidth](Window.md#innerwidth) / [Window.setInnerSize](Window.md#setinnersize)

---

### zoomNumer

プロパティ / アクセス: `r/w`

**解説**

レイヤの拡大倍率の分子を表します。
一応、値を設定することもできますが、値を設定する場合は [Window.setZoom](Window.md#setzoom) メソッドを使用してください。

分母は [Window.zoomDenom](Window.md#zoomdenom) プロパティが表します。

詳しくは [Window.setZoom](Window.md#setzoom) メソッドを参照してください。

**関連:** [Window.setZoom](Window.md#setzoom) / [Window.zoomDenom](Window.md#zoomdenom)

---

### zoomDenom

プロパティ / アクセス: `r/w`

**解説**

レイヤの拡大倍率の分母を表します。
一応、値を設定することもできますが、値を設定する場合は [Window.setZoom](Window.md#setzoom) メソッドを使用してください。

分子は [Window.zoomNumer](Window.md#zoomnumer) プロパティが表します。

詳しくは [Window.setZoom](Window.md#setzoom) メソッドを参照してください。

**関連:** [Window.setZoom](Window.md#setzoom) / [Window.zoomNumer](Window.md#zoomnumer)

---

### drawDevice

プロパティ / アクセス: `r/w`

**解説**

描画デバイスオブジェクトを表します。

値を設定することもできます。値を設定すると、以前このウィンドウに指定されていた描画デバイスは自動的に
無効になります (invalidateされます)。

デフォルトでは、Window.BasicDrawDevice というクラスのインスタンスが指定されています。

Window.BasicDrawDevice の詳細については、吉里吉里ソースの core/visual/win32/BasicDrawDevice.cpp 内の説明も参照してください。

独自の描画デバイス (プラグインで提供される物) を指定する場合は、そのプラグインのドキュメントに
従ってください。

---

### borderStyle

プロパティ / アクセス: `r/w`

**解説**

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

プロパティ / アクセス: `r/w`

**解説**

ウィンドウを常に最上位 ( 一番手前 ) に表示するかどうかを表します。値を設定することもできます。

真ならばウィンドウは常に最上位に表示されます。

現バージョンでは、ウィンドウがフルスクリーン化するとき、あるいはフルスクリーンから復帰するときに、このプロパティの設定内容が失われる可能性があります。

---

### imeMode

プロパティ / アクセス: `r`

**解説**

デフォルトのIMEモードを表します。

ここで指定したモードは、どのレイヤにもフォーカスが無い状態に設定されるモードです。

未指定の場合は **imDisable**で、これはどのレイヤにもフォーカスが無い状態では IME は無効状態であるということになります。

指定可能な値については [Layer.imeMode](Layer.md#imemode) を参照してください。

---

### mouseCursorState

プロパティ / アクセス: `r/w`

**解説**

マウスカーソルの表示状態を表します。値を設定することもできます。

`**mcsVisible**`を指定すると、マウスカーソルは表示状態になります。これはデフォルトの状態です。

`**mcsTempHidden**`を指定すると、マウスカーソルは非表示状態になりますが、少しでもマウスを動かすと`mcsVisible`に変わり、表示状態になります。[Window.hideMouseCursor](Window.md#hidemousecursor)メソッドを呼び出すとこの状態になります。

`**mcsHidden**`を指定すると、マウスカーソルは非表示状態になります。マウスを動かしても表示状態にはなりません。

---

### useMouseKey

プロパティ / アクセス: `r/w`

**解説**

マウスキーを使用するかどうかを表します。値を設定することもできます。

真ならばマウスキーを使用することができます。

マウスキーが有効になると、カーソルキーを使ってマウスカーソルを移動させることが
できますが、キー入力系のイベントはいっさい発生しなくなります。

---

### fullScreen

プロパティ / アクセス: `r/w`

**解説**

**フルスクリーン**かどうかを表します。値を設定することもできます。

真を指定すると現在のウィンドウのクライアント領域がフルスクリーンになります。フルスクリーン
時の画面解像度はクライアント領域のサイズになります。

偽を指定するとウィンドウ表示になります。

---

### mainWindow

プロパティ / アクセス: `r`

**解説**

メインウィンドウ ( 最初に作成されたウィンドウ ) を表します。

---

### focusedLayer

プロパティ / アクセス: `r/w`

**解説**

現在 **フォーカス** を持っているレイヤオブジェクトを表します。
値を設定することもできます。

null の場合はどのレイヤもフォーカスを持っていません。レイヤオブジェクトを
設定するとそのレイヤにフォーカスが移ります。

---

### primaryLayer

プロパティ / アクセス: `r`

**解説**

**プライマリレイヤ**オブジェクトを表します。

---

### HWND

プロパティ / アクセス: `r`

**解説**

ウィンドウハンドルを表します。

ここで得られるのは整数ですが、プラグインなどでこの数値を使う場合は HWND 型に
キャストして使ってください。

**関連:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### touchScaleThreshold

プロパティ / アクセス: `r/w`

**解説**

マルチタッチで拡大を開始する閾値です。

2つのタッチ位置の距離がこの値以上変化した時に拡大イベントが発生します。

一度閾値を超えるといったん指が離されるまで拡大イベントは有効になります。

**関連:** [Window.onTouchScaling](Window.md#ontouchscaling)

---

### touchRotateThreshold

プロパティ / アクセス: `r/w`

**解説**

マルチタッチで回転を開始する閾値です。

各タッチ位置の移動距離がこの値以上変化した時に回転イベントが発生します。

一度閾値を超えるといったん指が離されるまで回転イベントは有効になります。

**関連:** [Window.onTouchRotate](Window.md#ontouchrotate)

---

### touchPointCount

プロパティ / アクセス: `r`

**解説**

タッチパネルにタッチされている数です。

**関連:** [Window.getTouchPoint](Window.md#gettouchpoint)

---

### enableTouch

プロパティ / アクセス: `r/w`

**解説**

**タッチイベント**が有効かどうかを表します。値を設定することもできます。

真を指定すると[Window.onTouchDown](Window.md#ontouchdown)等のイベントが有効になり、タッチ操作では[Window.onMouseDown](Window.md#onmousedown)などが発生しなくなります。

タッチデバイスがありマルチタッチが有効な環境では、デフォルトが true になります。

---

### waitVSync

プロパティ / アクセス: `r/w`

**解説**

トランジション(画面切り替え)などでディスプレイの垂直同期を待ってから描画するかどうかの設定です。

設定を変えると、画面のちらつきを抑えられる場合がありますが、描画のパフォーマンスが低下する場合もあります。

---

### hintDelay

プロパティ / アクセス: `r/w`

**解説**

ヒントの表示待ち時間をミリ秒単位で表します。値を設定することもできます。

デフォルトは500ミリ秒です。

0を設定すると即座に [Window.onHintChanged](Window.md#onhintchanged) が呼び出されます(常時表示状態)。

-1を設定するとヒントが表示されることはありません。

**関連:** [Window.onHintChanged](Window.md#onhintchanged)

---

### displayOrientation

プロパティ / アクセス: `r`

**解説**

ディスプレイの向きを表します。

oriUnknown (取得失敗/不明), oriPortrait(縦向き), oriLandscape(横向き)のいずれかの値です。

**関連:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayRotate](Window.md#displayrotate)

---

### displayRotate

プロパティ / アクセス: `r`

**解説**

ディスプレイの回転角度を表します。

0、90、180、270、-1 のいずれかで、取得できなかった時は-1です。

**関連:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayOrientation](Window.md#displayorientation)

---
