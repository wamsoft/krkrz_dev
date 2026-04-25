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
- [onLabel](#onlabel)
- [setPos](#setpos)

### イベント

- [onStatusChanged](#onstatuschanged)
- [onFadeCompleted](#onfadecompleted)

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

プロパティ \ アクセス: `r/w`

**解説**

TODO: bits の説明

---

### channels

プロパティ \ アクセス: `r/w`

**解説**

TODO: channels の説明

---

### currentDevice

プロパティ \ アクセス: `r/w`

**解説**

TODO: currentDevice の説明

---

### filters

プロパティ \ アクセス: `r/w`

**解説**

TODO: filters の説明

---

### flags

プロパティ \ アクセス: `r/w`

**解説**

TODO: flags の説明

---

### frequency

プロパティ \ アクセス: `r/w`

**解説**

TODO: frequency の説明

---

### globalFocusMode

プロパティ \ アクセス: `r/w`

**解説**

TODO: globalFocusMode の説明

---

### globalVolume

プロパティ \ アクセス: `r/w`

**解説**

TODO: globalVolume の説明

---

### labels

プロパティ \ アクセス: `r/w`

**解説**

TODO: labels の説明

---

### pan

プロパティ \ アクセス: `r/w`

**解説**

TODO: pan の説明

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

TODO: samplePosition の説明

---

### useVisBuffer

プロパティ \ アクセス: `r/w`

**解説**

TODO: useVisBuffer の説明

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

TODO: freeDirectSound の説明

---

### getDeviceList

メソッド

**解説**

TODO: getDeviceList の説明

---

### getVisBuffer

メソッド

**解説**

TODO: getVisBuffer の説明

---

### onLabel

メソッド

**解説**

TODO: onLabel の説明

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
