# VideoOverlay

VideoOverlay クラスは、MPEG I や WMV、H.264、theora などを表示するため表示領域を作成するクラスです。吉里吉里のレイヤに表示を行うこともできます。

1.3.0以前は WMV/MPEG I を再生するときは、吉里吉里実行可能ファイルと同じ場所に、krmovie.dll が必要になります。

1.3.0以降は krmovie.dll が本体に統合されたため、別途添付する必要はなくなりました。theora を再生するには krdstheora.dll が必要になります。

レイヤでの再生を除き、オーバーレイによる再生では、VideoOverlay クラスの表示領域は、すべてのレイヤよりも手前に表示され、透過することはできません。

レイヤでの再生は、オーバーレイでの再生に比べ、再生時のプロセッサの負荷は高くなる傾向にあります。

## メンバー一覧

### コンストラクタ

- [VideoOverlay](#videooverlay)

### プロパティ

- [position](#position)
- [frame](#frame)
- [loop](#loop)
- [width](#width)
- [height](#height)
- [left](#left)
- [top](#top)
- [visible](#visible)
- [fps](#fps)
- [numberOfFrame](#numberofframe)
- [totalTime](#totaltime)
- [layer1](#layer1)
- [layer2](#layer2)
- [mode](#mode)
- [playRate](#playrate)
- [segmentLoopStartFrame](#segmentloopstartframe)
- [segmentLoopEndFrame](#segmentloopendframe)
- [periodEventFrame](#periodeventframe)
- [audioBalance](#audiobalance)
- [audioVolume](#audiovolume)
- [numberOfAudioStream](#numberofaudiostream)
- [enabledAudioStream](#enabledaudiostream)
- [mixingMovieAlpha](#mixingmoviealpha)
- [mixingMovieBGColor](#mixingmoviebgcolor)
- [contrastRangeMin](#contrastrangemin)
- [contrastRangeMax](#contrastrangemax)
- [contrastDefaultValue](#contrastdefaultvalue)
- [contrastStepSize](#contraststepsize)
- [contrast](#contrast)
- [brightnessRangeMin](#brightnessrangemin)
- [brightnessRangeMax](#brightnessrangemax)
- [brightnessDefaultValue](#brightnessdefaultvalue)
- [brightnessStepSize](#brightnessstepsize)
- [brightness](#brightness)
- [hueRangeMin](#huerangemin)
- [hueRangeMax](#huerangemax)
- [hueDefaultValue](#huedefaultvalue)
- [hueStepSize](#huestepsize)
- [hue](#hue)
- [saturationRangeMin](#saturationrangemin)
- [saturationRangeMax](#saturationrangemax)
- [saturationDefaultValue](#saturationdefaultvalue)
- [saturationStepSize](#saturationstepsize)
- [saturation](#saturation)
- [originalWidth](#originalwidth)
- [originalHeight](#originalheight)

### メソッド

- [open](#open)
- [play](#play)
- [stop](#stop)
- [pause](#pause)
- [rewind](#rewind)
- [prepare](#prepare)
- [setSegmentLoop](#setsegmentloop)
- [cancelSegmentLoop](#cancelsegmentloop)
- [close](#close)
- [setPeriodEvent](#setperiodevent)
- [cancelPeriodEvent](#cancelperiodevent)
- [setPos](#setpos)
- [setSize](#setsize)
- [setBounds](#setbounds)
- [selectAudioStream](#selectaudiostream)
- [setMixingLayer](#setmixinglayer)
- [resetMixingLayer](#resetmixinglayer)

### イベント

- [onStatusChanged](#onstatuschanged)
- [onPeriod](#onperiod)
- [onFrameUpdate](#onframeupdate)

---

### VideoOverlay

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | このレイヤを保有することになるウィンドウ ( [Window](Window.md) クラスの<br>オブジェクト ) を指定します。 |

**解説**

VideoOverlay オブジェクトの構築

VideoOverlay クラスのオブジェクトを構築します。

---

### position

プロパティ \ アクセス: `r/w`

**解説**

再生位置

メディアの再生位置を ms 単位で表します。値を設定することもできます。

**関連:** [VideoOverlay.frame](VideoOverlay.md#frame) / [VideoOverlay.totalTime](VideoOverlay.md#totaltime)

---

### frame

プロパティ \ アクセス: `r/w`

**解説**

現在のフレーム

メディアの再生位置をフレーム単位で表します。値を設定することもできます。

**関連:** [VideoOverlay.position](VideoOverlay.md#position) / [VideoOverlay.numberOfFrame](VideoOverlay.md#numberofframe)

---

### loop

プロパティ \ アクセス: `r/w`

**解説**

ループ再生をするかどうか

ループ再生の有効無効を表します。値を設定することもできます。

真ならばループ、偽ならば非ループです。

---

### width

プロパティ \ アクセス: `r/w`

**解説**

再生矩形の横幅

再生矩形の横幅を表します。値を設定することもできます。

このプロパティは、現バージョンではレイヤ再生時は使用できません(常にサイズはビデオのサイズと同じになります)。

**関連:** [VideoOverlay.height](VideoOverlay.md#height) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### height

プロパティ \ アクセス: `r/w`

**解説**

再生矩形の縦幅

再生矩形の縦幅を表します。値を設定することもできます。

このプロパティは、現バージョンではレイヤ再生時は使用できません(常にサイズはビデオのサイズと同じになります)。

**関連:** [VideoOverlay.width](VideoOverlay.md#width) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### left

プロパティ \ アクセス: `r/w`

**解説**

再生矩形の左端位置

再生矩形の左端位置を表します。値を設定することもできます。

**関連:** [VideoOverlay.top](VideoOverlay.md#top) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### top

プロパティ \ アクセス: `r/w`

**解説**

再生矩形の上端位置

再生矩形の上端位置を表します。値を設定することもできます。

**関連:** [VideoOverlay.left](VideoOverlay.md#left) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### visible

プロパティ \ アクセス: `r/w`

**解説**

可視かどうか

再生領域が可視かどうかを指定します。値を設定することもできます。

真ならば可視、偽ならば不可視です。

---

### fps

プロパティ \ アクセス: `r`

**解説**

フレームレート

フレームレート(フレーム/秒)を表します。

---

### numberOfFrame

プロパティ \ アクセス: `r`

**解説**

全フレーム数

全フレーム数を表します。

---

### totalTime

プロパティ \ アクセス: `r`

**解説**

合計時間

合計時間をms単位で表します。

---

### layer1

プロパティ \ アクセス: `r/w`

**解説**

描画レイヤ指定1

レイヤ描画モード時、描画するレイヤを表します。値を設定することもできます。

layer1 プロパティと layer2 プロパティを異なるレイヤに設定することにより、同時に２つのレイヤに同じ動画を表示させることができます。

---

### layer2

プロパティ \ アクセス: `r/w`

**解説**

描画レイヤ指定2

レイヤ描画モード時、描画するレイヤを表します。値を設定することもできます。

---

### mode

プロパティ \ アクセス: `r/w`

**解説**

オーバーレイorレイヤ描画の指定

オーバーレイモードであるか、レイヤ描画モードであるか、ミキサーモードであるかを表します。値を設定することもできます。

オーバーレイモードの場合は **vomOverlay**、レイヤ描画モードの場合は **vomLayer** 、ミキサーモードの場合は **vomMixer**、Media Foundation モードの場合は **vomMFEVR** となります。

vomMFEVR モードは 1.2.0 以降でのみ使用できます。

---

### playRate

プロパティ \ アクセス: `r/w`

**解説**

再生速度

メディアの再生速度を設定します。

1.0 を指定すると通常の再生速度、0.5 では半分の再生速度、2では2倍の再生速度となります。

設定可能値はDirectShowのフィルタによって決まります。

参考 : 音声付のMPEGファイルの場合、0.0より大きい値から2.0までの値が設定可能です。音声なしのMPEGファイルの場合、0.0より大きい値からdoubleの範囲内(たぶん)で設定可能ですが、実際の再生速度は処理速度によって上限が決まります。

---

### segmentLoopStartFrame

プロパティ \ アクセス: `r`

**解説**

セグメントループの開始フレーム

セグメントループの始端フレームです。

**関連:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop) / [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop)

---

### segmentLoopEndFrame

プロパティ \ アクセス: `r`

**解説**

セグメントループの開始フレーム

セグメントループの始端フレームです。

**関連:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### periodEventFrame

プロパティ \ アクセス: `r/w`

**解説**

ピリオドイベントフレーム

periodイベントを発生させるフレームです。

未設定の場合は負の値となります。

---

### audioBalance

プロパティ \ アクセス: `r/w`

**解説**

音声バランス(パニング)

パン (音像位置) を表します。値を設定することもできます。

音の聞こえる左右の位置を指定することができます。

-100000 ～ 0 ～ 100000 の数値で指定し、 -100000 が 完全に左、0 が中央、100000 が完全に右になります。

ステレオのソースを再生する場合は、パンは、左右どちらかのチャンネルを減衰させることで実現されます(0を指定すると両チャンネルが出力され、-100000を指定すると左チャンネルのみが出力される)。

---

### audioVolume

プロパティ \ アクセス: `r/w`

**解説**

音声ボリューム

再生する音量を表します。値を設定することもできます。

0 ～ 100000 の数値で指定し、 0 が完全ミュート、100000 が 100% の音量となります。

---

### numberOfAudioStream

プロパティ \ アクセス: `r`

**解説**

音声ストリーム数

MPEGファイルのみで利用可能です。
オーディオストリーム数を取得できます。

**関連:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### enabledAudioStream

プロパティ \ アクセス: `r`

**解説**

再生対象音声ストリーム番号

MPEGファイルのみで利用可能です。
再生対象のオーディオストリーム番号を取得できます。
オーディオストリームが見付からない場合は-1を返します。

**関連:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream)

---

### mixingMovieAlpha

プロパティ \ アクセス: `r/w`

**解説**

ビデオの透明度

0.0(完全に透明)～1.0(完全に不透明)の範囲でビデオの透明度を表します。

ミキサーモードでのみ利用可能です。

---

### mixingMovieBGColor

プロパティ \ アクセス: `r/w`

**解説**

ビデオの背景色

ビデオの背景色を表します。

ミキサーモードでのみ利用可能です。

---

### contrastRangeMin

プロパティ \ アクセス: `r`

**解説**

ビデオのコントラストレンジ最小値

コントラストの幅の最小値を表します。

ミキサーモードでのみ利用可能です。

---

### contrastRangeMax

プロパティ \ アクセス: `r`

**解説**

ビデオのコントラストレンジ最大値

コントラストの幅の最大値を表します。

ミキサーモードでのみ利用可能です。

---

### contrastDefaultValue

プロパティ \ アクセス: `r`

**解説**

ビデオのコントラスト既定値

コントラストの既定値を表します。

ミキサーモードでのみ利用可能です。

---

### contrastStepSize

プロパティ \ アクセス: `r`

**解説**

ビデオのコントラスト増減ステップ値

contrastRangeMin から contrastRangeMax への有効な増分を表します。

この値の単位でコントラストを変更できます。

ミキサーモードでのみ利用可能です。

---

### contrast

プロパティ \ アクセス: `r/w`

**解説**

ビデオのコントラスト

ビデオのコントラストを表します。

ミキサーモードでのみ利用可能です。

---

### brightnessRangeMin

プロパティ \ アクセス: `r`

**解説**

ビデオの輝度レンジ最小値

輝度の幅の最小値を表します。

ミキサーモードでのみ利用可能です。

---

### brightnessRangeMax

プロパティ \ アクセス: `r`

**解説**

ビデオの輝度レンジ最大値

輝度の幅の最大値を表します。

ミキサーモードでのみ利用可能です。

---

### brightnessDefaultValue

プロパティ \ アクセス: `r`

**解説**

ビデオの輝度既定値

輝度の既定値を表します。

ミキサーモードでのみ利用可能です。

---

### brightnessStepSize

プロパティ \ アクセス: `r`

**解説**

ビデオの輝度増減ステップ値

brightnessRangeMin から brightnessRangeMax への有効な増分を表します。

この値の単位で輝度を変更できます。

ミキサーモードでのみ利用可能です。

---

### brightness

プロパティ \ アクセス: `r/w`

**解説**

ビデオの輝度

ビデオの輝度を表します。

ミキサーモードでのみ利用可能です。

---

### hueRangeMin

プロパティ \ アクセス: `r`

**解説**

ビデオの色相レンジ最小値

色相の幅の最小値を表します。

ミキサーモードでのみ利用可能です。

---

### hueRangeMax

プロパティ \ アクセス: `r`

**解説**

ビデオの色相レンジ最大値

色相の幅の最大値を表します。

ミキサーモードでのみ利用可能です。

---

### hueDefaultValue

プロパティ \ アクセス: `r`

**解説**

ビデオの色相既定値

色相の既定値を表します。

ミキサーモードでのみ利用可能です。

---

### hueStepSize

プロパティ \ アクセス: `r`

**解説**

ビデオの色相増減ステップ値

hueRangeMin から hueRangeMax への有効な増分を表します。

この値の単位で色相を変更できます。

ミキサーモードでのみ利用可能です。

---

### hue

プロパティ \ アクセス: `r/w`

**解説**

ビデオの色相

ビデオの色相を表します。

ミキサーモードでのみ利用可能です。

---

### saturationRangeMin

プロパティ \ アクセス: `r`

**解説**

ビデオの彩度レンジ最小値

彩度の幅の最小値を表します。

ミキサーモードでのみ利用可能です。

---

### saturationRangeMax

プロパティ \ アクセス: `r`

**解説**

ビデオの彩度レンジ最大値

彩度の幅の最大値を表します。

ミキサーモードでのみ利用可能です。

---

### saturationDefaultValue

プロパティ \ アクセス: `r`

**解説**

ビデオの彩度既定値

彩度の既定値を表します。

ミキサーモードでのみ利用可能です。

---

### saturationStepSize

プロパティ \ アクセス: `r`

**解説**

ビデオの彩度増減ステップ値

saturationRangeMin から saturationRangeMax への有効な増分を表します。

この値の単位で彩度を変更できます。

ミキサーモードでのみ利用可能です。

---

### saturation

プロパティ \ アクセス: `r/w`

**解説**

ビデオの彩度

ビデオの彩度を表します。

ミキサーモードでのみ利用可能です。

---

### originalWidth

プロパティ \ アクセス: `r`

**解説**

ビデオの実際の幅

格納されているビデオの幅です。

---

### originalHeight

プロパティ \ アクセス: `r`

**解説**

ビデオの実際の高さ

格納されているビデオの高さです。

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定されたメディアを開きます。 |

**解説**

メディアを開く

指定されたメディアを開きます。

現バージョンで再生可能なのは MPEG I (拡張子 .mpeg または .mpg または .mpv)、WMVです。

ビデオのみの (オーディオとマルチプレクシングされていない) MPEG I ストリームの拡張子は .mpv にしてください。

---

### play

メソッド

**解説**

再生開始

メディアの再生を開始します。

---

### stop

メソッド

**解説**

再生停止

メディアの再生を停止します。

---

### pause

メソッド

**解説**

一時停止

メディアの再生を一時停止します。

---

### rewind

メソッド

**解説**

巻き戻し

メディアの再生位置を先頭に移動します。

---

### prepare

メソッド

**解説**

再生準備

メディアの1フレーム目を指定されているレイヤーに描画し、描画終了時にonPeriodイベントを発生させます。
prepareメソッド コール後の再生は、onPeriodイベントを待機してから行ってください。

**関連:** [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### setSegmentLoop

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `comeFrame` | `&nbsp;` | ループ移動先フレーム(ループの始端フレーム)。再生がgoFrameに達したとき、再生ヘッドはこのフレームに移動します。 |
| `goFrame` | `&nbsp;` | ループ終点フレーム(ループの終端フレーム)。このフレームの1つ前のフレームの表示が終了した時、再生ヘッドはcomeFrameへ移動します。 |

**解説**

フレーム間ループの設定

指定されたフレーム間でループ処理を行います。

ループ終端(goFrame)では、onPeriodイベントが発生します。

comeFrameのフレームにはムービーファイルにキーフレームを設定しておく必要があります。

設定されていない場合は、
ループ終点から始点へ移動時に指定されたフレームに最も近いキーフレームへ再生位置が移動することになります。

**関連:** [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod) / [VideoOverlay.segmentLoopStartFrame](VideoOverlay.md#segmentloopstartframe) / [VideoOverlay.segmentLoopEndFrame](VideoOverlay.md#segmentloopendframe)

---

### cancelSegmentLoop

メソッド

**解説**

フレーム間ループの解除

setSegmentLoopメソッドで指定したセグメント間ループを解除します。

**関連:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### close

メソッド

**解説**

メディアを閉じる

メディアを閉じます。

メディアを再生するために確保されていたリソースなどもすべて解放します。

**関連:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### setPeriodEvent

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `eventFrame` | `&nbsp;` | onPeriodイベントを発生させるフレームを指定します。 |

**解説**

指定フレームでのイベント発生の指定

指定したフレームでonPeriodイベントを発生させます。

onPeriodイベントは、一度発生すると解除されます。再び発生させたい場合は再度このメソッドで設定してください。

**関連:** [VideoOverlay.cancelPeriodEvent](VideoOverlay.md#cancelperiodevent) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### cancelPeriodEvent

メソッド

**解説**

指定フレームでのイベント発生の解除

setPeriodEventメソッドで設定したイベント発生を解除します。

**関連:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent)

---

### setPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` | メディアを再生するための矩形領域の左端位置を指定します。 |
| `top` | `&nbsp;` | メディアを再生するための矩形領域の上端位置を指定します。 |

**解説**

再生矩形の左上位置を指定

メディアを再生するための矩形領域の左上位置を指定します。

座標は、ウィンドウのクライアント ( レイヤを表示可能な領域 ) 内での座標で、ピクセル単位で
指定します。

---

### setSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `width` | `&nbsp;` | メディアを再生するための矩形領域の横幅を指定します。 |
| `height` | `&nbsp;` | メディアを再生するための矩形領域の縦幅を指定します。 |

**解説**

再生矩形のサイズを指定

メディアを再生するための矩形領域のサイズをピクセル単位で指定します。

現バージョンでは、レイヤ再生時にはこのメソッドを使用することはできません。

---

### setBounds

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `left` | `&nbsp;` | メディアを再生するための矩形領域の左端位置を指定します。 |
| `top` | `&nbsp;` | メディアを再生するための矩形領域の上端位置を指定します。 |
| `width` | `&nbsp;` | メディアを再生するための矩形領域の横幅を指定します。 |
| `height` | `&nbsp;` | メディアを再生するための矩形領域の縦幅を指定します。 |

**解説**

再生矩形の位置とサイズを指定

メディアを再生するための矩形領域の位置とサイズを指定します。

座標は、ウィンドウのクライアント ( レイヤを表示可能な領域 ) 内での座標で、ピクセル単位で
指定します。

現バージョンでは、レイヤ再生時にはこのメソッドで指定できるのは位置だけで、サイズは無視されます。

---

### selectAudioStream

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `streamNumber` | `&nbsp;` | 音声ストリーム番号を指定します。 |

**解説**

音声ストリームの選択

指定した音声ストリーム番号を有効にします。

音声ストリームを複数含まないビデオでは使用できません。

**関連:** [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### setMixingLayer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | レイヤー |

**解説**

ミキシング対象レイヤの設定

指定したレイヤーとビデオのミキシングを行います。

ミキシングはこのメソッドが呼び出された時のレイヤー画像と行われます。

レイヤー画像の更新を反映するには、再度このメソッドを呼び出す必要があります。

VideOverlay.OnFrameUpdate を使用して、
レイヤー画像が更新されたことを調べてこのメソッドを呼び出すようにすれば、自動的に更新が反映されるようになります。
onFrameUpdateで毎フレームこのメソッドを呼び出した場合、かなり負荷がかかりますのでそれは避けた方が良いです。

ミキサーモードでのみ利用可能です。

---

### resetMixingLayer

メソッド

**解説**

ミキシング対象レイヤの設定解除

ビデオとレイヤーのミキシングを解除します。

ミキサーモードでのみ利用可能です。

---

### onStatusChanged

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `status` | `&nbsp;` | ステータス文字列を表します。<br>以下のいずれかです。<br>`"**unload**"   : ` メディアが開かれてない<br>`"**ready**"    : ` メディアの準備が完了している<br>`"**play**"     : ` メディアは再生中である<br>`"**stop**"     : ` メディアは停止中である<br>`"**pause**"    : ` メディアは一時停止中である |

**解説**

ステータスが変更された

このオブジェクトのステータスが変更されたときに発生します。

ready は、vomMFEVR モードの時のみ発生します。

---

### onPeriod

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `type` | `&nbsp;` | Periodイベントのタイプを表します。<br>以下のいずれかです。<br>`**perLoop**    : ` (通常の)ループの終端に達した<br>`**perSegLoop** : ` セグメントループの終端に達した<br>`**perPeriod**  : ` setPeriodEvent メソッドで指定されたフレームに達した<br>`**perPrepare** : ` prepare メソッドによる再生準備が完了した |

**解説**

Periodイベントが発生した

ループの終端や、 setPeriodEventによって指定されたフレームに達した場合、または prepare メソッドにより再生準備が完了した場合に呼び出されるメソッドです。

ループの終端や、 setPeriodEvent によって指定されたフレームに達した場合にこのイベントが呼ばれる時点では、再生状況によっては、すでに再生位置が指定された位置を超えている場合があります。現在の実際の再生位置を取得するには frame プロパティを参照してください。

**関連:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent) / [VideoOverlay.prepare](VideoOverlay.md#prepare) / [VideoOverlay.frame](VideoOverlay.md#frame)

---

### onFrameUpdate

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `frame` | `&nbsp;` | ビデオのフレーム番号 |

**解説**

ビデオフレームが更新された

ビデオフレームが更新された後に呼び出されるメソッドです。

引数であるframeは現在表示されているビデオフレームと完全に一致しているとは限りません。

レイヤ描画モード、ミキサーモード時のみ利用可能です。

---
