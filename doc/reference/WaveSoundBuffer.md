# WaveSoundBuffer

WaveSoundBuffer クラスは、PCMの再生を管理するクラスです。

WaveSoundBuffer クラスでは、[](LoopTuner) で作成した .sli ファイルを読み込み、処理することができます。詳しくはループチューナの説明をご覧ください。

## メンバー一覧

### コンストラクタ

- [WaveSoundBuffer](#wavesoundbuffer)

### プロパティ

- [position](#position)
- [paused](#paused)
- [totalTime](#totaltime)
- [looping](#looping)
- [volume](#volume)
- [volume2](#volume2)
- [status](#status)
- [bits](#bits)
- [channels](#channels)
- [currentDevice](#currentdevice)
- [filters](#filters)
- [flags](#flags)
- [frequency](#frequency)
- [globalFocusMode](#globalfocusmode)
- [globalVolume](#globalvolume)
- [labels](#labels)
- [pan](#pan)
- [posX](#posx)
- [posY](#posy)
- [posZ](#posz)
- [samplePosition](#sampleposition)
- [useVisBuffer](#usevisbuffer)

### メソッド

- [open](#open)
- [play](#play)
- [stop](#stop)
- [fade](#fade)
- [stopFade](#stopfade)
- [freeDirectSound](#freedirectsound)
- [getDeviceList](#getdevicelist)
- [getVisBuffer](#getvisbuffer)
- [setPos](#setpos)

### イベント

- [onStatusChanged](#onstatuschanged)
- [onFadeCompleted](#onfadecompleted)
- [onLabel](#onlabel)

---

### WaveSoundBuffer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `owner` | `&nbsp;` | イベントの発生先を指定します。 |

**解説**

WaveSoundBuffer オブジェクトの構築

WaveSoundBuffer クラスのオブジェクトを構築します。

イベントが発生すると owner で指定したオブジェクトの action メソッドを呼び出します。owner に null を指定すると action メソッドは呼ばれません。通常は [Window](Window.md) クラスのオブジェクトを owner に指定します。

---

### position

プロパティ \ アクセス: `r/w`

**解説**

再生位置

再生位置を ms 単位で表します。値を設定するとその位置に移動します。

---

### paused

プロパティ \ アクセス: `r/w`

**解説**

一時停止状態かどうか

一時停止状態かどうかを表します。値を設定することもできます。

真の場合は一時停止状態です。

---

### totalTime

プロパティ \ アクセス: `r`

**解説**

メディアの再生時間

メディアの総再生時間を ms 単位で表します。

---

### looping

プロパティ \ アクセス: `r/w`

**解説**

ループ再生を行うかどうか

ループ再生を行うかどうかを表します。値を設定することもできます。

真を指定するとループ再生がされます。

偽を指定しても、再生しているメディアにループ情報があれば、ループ情報が利用されます。

---

### volume

プロパティ \ アクセス: `r/w`

**解説**

音量

再生する音量を表します。値を設定することもできます。

0 ～ 100000 の数値で指定し、 0 が完全ミュート、100000 が 100% の音量となります。

---

### volume2

プロパティ \ アクセス: `r/w`

**解説**

第２音量

再生する音量を表します。値を設定することができます。

[WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) プロパティと違うのは、このプロパティは
[WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) メソッドでも変化しないということです。

最終的な音量は、volume プロパティとこのプロパティの積で決定されます。volume プロパティが
100000 ( 100% ) で volume2 プロパティも 100000 ( 100% ) ならば 100% × 100% = 100% で
100% の音量で再生されます。volume プロパティが 50000 ( 50% ) で volume2 プロパティが 75000 ( 75% ) ならば
50% × 75% = 37.5% で 37.5 % の音量で再生されます。

---

### status

プロパティ \ アクセス: `r`

**解説**

ステータス

現在の状態を表します。

状態は文字列で表され、以下の値をとります。

`"**unload**"   : ` メディアが開かれてない

`"**play**"     : ` メディアは再生中である

`"**stop**"     : ` メディアは停止中である

---

### bits

プロパティ \ アクセス: `r`

**解説**

量子化ビット数

現在再生中のサウンドの量子化ビット数を表します。
CD と同じ量子化ビット数の場合は 16 になります。
メディアが開かれていない状態では正常な値を返さない可能性があります。

---

### channels

プロパティ \ アクセス: `r`

**解説**

チャンネル数

現在再生中のサウンドのチャンネル数を表します。
モノラルの場合は 1、ステレオの場合は 2 になります。
メディアが開かれていない状態では正常な値を返さない可能性があります。

---

### currentDevice

プロパティ \ アクセス: `r/w`

**解説**

TODO: currentDevice の説明

---

### filters

プロパティ \ アクセス: `r`

**解説**

フィルタ配列

インサーションフィルタオブジェクトを保持している配列(Arrayクラスのインスタンス)です。
この配列にフィルタオブジェクトを登録することにより、再生中にリアルタイムで音声に対して様々な効果をかけることができます。
フィルタ配列への変更が反映されるのは、WaveSoundBuffer.openメソッドが実行された時だけです。
それまでは、この配列への変更を行っても反映はされません。
例:
```
var buf = new WaveSoundBuffer(window);
(略)
buf.filters.clear();
// フィルタ配列をクリア
buf.filters.add(new WaveSoundBuffer.PhaseVocoder());
// PhaseVocoderフィルタを追加
buf.filters[0].time = 0.5;
// 倍速再生
```

---

### flags

プロパティ \ アクセス: `r`

**解説**

フラグ

フラグを表すオブジェクトを得ることができます。
このオブジェクトには 0 ～ 15 のプロパティがあり、それぞれ各フラグの値を表しています。
プロパティには間接メンバ選択演算子 ('[ ]' 演算子) を用いてアクセスすることができます。
これらのプロパティには値を設定することもできます。
値は 0 ～ 9999 の範囲であり、これを下回ったり、上回ることはできません。
このオブジェクトの count プロパティは常に 16 を返します。
このオブジェクトには reset メソッドがあり、このメソッドを実行すると、全てのフラグが 0 にリセットされます。
メディアを開いていない場合は、このオブジェクトのプロパティに値を設定しても無視されます。
このオブジェクトは一見配列オブジェクトにも見えますが、いわゆるTJSの配列オブジェクト('Array' クラスのオブジェクト) ではありません。
フラグは WaveSoundBuffer.open メソッドで全て 0 にリセットされます。
例:

```
var buf = new WaveSoundBuffer(window);
(略)
buf.flags.reset();
// 全てのフラグを 0 にリセット
var cnt = buf.flags.count;
// cnt には 16 が入る
buf.flags[4] = 34;
// 4番のフラグに34を代入
```

---

### frequency

プロパティ \ アクセス: `r/w`

**解説**

サンプリング周波数

現在再生中のサウンドのサンプリング周波数を表します。
値を設定することもできます。
CD と同じサンプリング周波数の場合は 44100 になります。
メディアが開かれていない状態では正常な値を返さない可能性があります。
値を設定すると、その周波数で再生します。

---

### globalFocusMode

プロパティ \ アクセス: `r/w`

**解説**

フォーカスモード

フォーカスモードを表します。
値を設定することもできます。
フォーカスモードは、アプリケーションが最小化したときや非アクティブになったときにミュートするモードです。

+ sgfmNeverMuteを指定すると、アプリケーションがどのような状態でもミュートはしません。
+ sgfmMuteOnMinimizeを指定すると、アプリケーションが最小化時にミュートします。
+ sgfmMuteOnDeactivateを指定すると、アプリケーションが非アクティブ化したときにミュートします。

このプロパティは WaveSoundBuffer クラス上にしか存在しません (WaveSoundBufferから作られたオブジェクト上にこのプロパティはありません)。
使用する際は WaveSoundBuffer.globalFocusMode としてください。
このプロパティの設定よりも、コマンドラインオプションで指定した '-wsmute' (DirectSound ミュート) の設定が優先されます。
Androidでは、非アクティブになった時ミュートされます。
バックグラウンドでは処理速度が低下し、正常に再生できなくなります。

---

### globalVolume

プロパティ \ アクセス: `r/w`

**解説**

大域音量

大域音量 (マスターボリューム)を表します。
値を設定することもできます。
この音量は、すべての WaveSoundBuffer に影響します。
0 ～ 100000 の数値で指定し、 0 が完全ミュート、100000 が 100% の音量となります。
デフォルトの値は 100000 です。
このプロパティは WaveSoundBuffer クラス上にしか存在しません (WaveSoundBufferから作られたオブジェクト上にこのプロパティはありません)。
使用する際は WaveSoundBuffer.globalVolume としてください。

---

### labels

プロパティ \ アクセス: `r`

**解説**

ラベル

ラベルを表すオブジェクトを得ることができます。
このオブジェクトは辞書配列で、それぞれ、ループ情報中のラベルの名前をメンバ名とした要素が入っています。
それぞれの要素も辞書配列で、name メンバはラベルの名前を表し、position メンバはミリ秒単位でのラベルの位置を表し、samplePosition はサンプル数単位でのラベルの位置を表しています。
この辞書配列は読み出し専用であると考えてください。
値を代入したり、新しいメンバを作成しても反映されることはありません。
例:

```
var buf = new WaveSoundBuffer(window);
(略)
debug.message(buf.labels['start'].position);
// 'start' というラベル名の位置をミリ秒単位で
debug.message(buf.labels['start'].samplePosition);
// 'start' というラベル名の位置をサンプル数単位で
```

---

### pan

プロパティ \ アクセス: `r/w`

**解説**

パン

パン (音像位置) を表します。
値を設定することもできます。
音の聞こえる左右の位置を指定することができます。
-100000 ～ 0 ～ 100000 の数値で指定し、 -100000 が 完全に左、0 が中央、100000 が完全に右になります。

---

### posX

プロパティ \ アクセス: `r/w`

**解説**

TODO: posX の説明

---

### posY

プロパティ \ アクセス: `r/w`

**解説**

TODO: posY の説明

---

### posZ

プロパティ \ アクセス: `r/w`

**解説**

TODO: posZ の説明

---

### samplePosition

プロパティ \ アクセス: `r/w`

**解説**

再生位置

再生位置をサンプル数単位で表します。
値を設定するとその位置に移動します。

---

### useVisBuffer

プロパティ \ アクセス: `r/w`

**解説**

視覚化用バッファを使用するかどうか

視覚化用バッファを使用するかどうか表します。
値を設定することもできます。
真を指定すると視覚化用バッファが利用可能になり、WaveSoundBuffer.getVisBuffer メソッドが利用可能になります。
デフォルトでは偽になっています。
真を指定すると偽を指定したときよりも多くのメモリと CPU 時間を消費するようになるので注意してください。

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 再生したいストレージを指定します。 |

**解説**

メディアを開く

指定されたメディアを開きます。このメソッドは再生を開始しません。

指定されたストレージ名に .sli を付加したファイル名があれば、サウンドループ情報として読み込みます。

---

### play

メソッド

**解説**

メディアを再生する

メディアの再生を開始します。

---

### stop

メソッド

**解説**

メディアを停止する

メディアを停止します。

---

### fade

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `to` | `&nbsp;` | 到達させる音量を指定します。<br>音量の指定については [WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) プロパティを参照して<br>ください。 |
| `time` | `&nbsp;` | フェードにかける時間を ms 単位で指定します。 |
| `delay` | `0` | フェード開始までの待ち時間を ms 単位で指定します。 |

**解説**

フェードを開始する

フェード ( 連続的な音量の変化 ) を開始します。

---

### stopFade

メソッド

**解説**

フェードを停止する

[WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) メソッドで開始したフェードを強制的に停止します。

音量は停止させた時点のままになります。

---

### freeDirectSound

メソッド

**解説**

DirectSound の解放

DirectSound を解放します。
すべての WaveSoundBuffer クラスのオブジェクトは停止状態になります。
DirectSound と WaveMapper ( MCI 等 ) による再生を同時に行えない環境などで DirectSound を 解放するためにこのメソッドを使います。
このメソッドは WaveSoundBuffer クラス上にしか存在しません (WaveSoundBufferから作られたオブジェクト上にこのメソッドはありません)。
使用する際は WaveSoundBuffer.freeDirectSound(); としてください。

---

### getDeviceList

メソッド

**解説**

TODO: getDeviceList の説明

---

### getVisBuffer

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `buffer` | `&nbsp;` | 出力データを書き込むバッファを指定します。<br>バッファは 16bit 符号付き整数の配列で、numsamples 引数および channels 引数で指定したサンプルが書き込まれるのに十分な個数 ( numsamples * channels 以上 )である必要があります。<br>channels に 1 以外を指定した場合は、各チャネルのサンプルはインターリーブされて( ステレオならば 右 左 右 左 ・・・・の順に ) 格納されます。<br>配列の先頭要素へのポインタを指定する必要がありますが、整数型にキャストして渡してください。 |
| `numsamples` | `&nbsp;` | 取得するサンプル数を指定します。 |
| `channel` | `&nbsp;` | 取得するチャンネル数を指定します。<br>1 を指定すると、モノラルの場合はそのまま、そうでない場合は 1チャンネルにダウンミックスされたデータを得ることができます。<br>1 以外の数値を指定する場合は、再生中のサウンドと同じチャンネル数を指定する必要があります。<br>このばあいは、そのままのデータを得ることができます。 |
| `ahead` | `0` | 先読みするサンプル数を指定します。<br>現在の再生位置から、この引数で指定したサンプル数だけ先にあるサンプルから取得することができます。<br>0 を指定するか、この引数を省略すると、現在の再生位置からの取得になります。 |

**戻り値**

取得できたサンプル数が戻ります。

**解説**

視覚化用データの取得

視覚化用に PCM データを取得します。
現在の再生位置から PCM データを読み込み、buffer 引数で指定した配列に書き込みます。
ただし、バッファの状態や再生形式によっては正常にデータを読み込めない可能性もあります。
このメソッドは C や C++ 等で書かれたプラグインから利用されることを想定してますので、たとえばbuffer 引数に TJS の配列を指定する、などのようなことはできません。
このメソッドを使用するには  WaveSoundBuffer.useVisBuffer プロパティを真に指定する必要があります。

---

### setPos

メソッド

**解説**

TODO: setPos の説明

---

### onStatusChanged

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `status` | `&nbsp;` | 新しいステータスです。<br>[WaveSoundBuffer.status](WaveSoundBuffer.md#status) プロパティを参照してください。 |

**解説**

ステータスが変更された

再生のステータス ( 状態 ) が変わった時に発生します。

---

### onFadeCompleted

イベント

**解説**

フェードが終了した

[WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) メソッドで開始したフェードが終了したときに発生します。

---

### onLabel

イベント

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 通過したラベル名です。 |

**解説**

ラベルを通過した

再生位置がラベルを通過した際に発生します。

---

## プラグイン拡張: getSample

擬似コードによるマニュアル

### メンバー一覧

#### プロパティ

- [sampleValue](#samplevalue)
- [sampleCount](#samplecount)
- [sampleAhead](#sampleahead)

#### メソッド

- [getSample](#getsample)

---

### sampleValue

プロパティ \ アクセス: `r`

**解説**

サンプル値の取得（新方式）

getVisBuffer(buf, sampleCount, 1, sampleAhead)でサンプルを取得し，
(value/32768)^2の最大値を取得します。(0～1の実数で返ります)
※このプロパティを読み出すと暗黙でuseVisBuffer=trueに設定されます

---

### sampleCount

プロパティ \ アクセス: `r/w`

**解説**

新方式のバッファ取得用パラメータプロパティ（sampleValueを参照）

デフォルトはsetDefaultCounts/setDefaultAheadsで決定されます
※このプロパティを読み書きする暗黙でuseVisBuffer=trueに設定されます

---

### sampleAhead

プロパティ \ アクセス: `r/w`

---

### getSample

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n` | `&nbsp;` | 取得するサンプルの数。省略すると 100 |

**戻り値**

平均値
※ 予めuseVisBuffer=trueにしておくこと

**解説**

サンプル値の取得（旧方式）

現在の再生位置から指定数のサンプルを取得してその平均値を返します。
値が負のサンプル値は無視されます。

---
