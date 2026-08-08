# EffekseerPlayer

再生用プレイヤー

エフェクト 1 インスタンスの再生・配置・描画を担当する。

## メンバー一覧

### コンストラクタ

- [EffekseerPlayer](#effekseerplayer)

### プロパティ

- [device](#device)
- [effect](#effect)
- [loaded](#loaded)
- [playing](#playing)
- [instanceCount](#instancecount)
- [renderScale](#renderscale)
- [left](#left)
- [top](#top)
- [z](#z)
- [zoomX](#zoomx)
- [zoomY](#zoomy)
- [angle](#angle)
- [speed](#speed)
- [color](#color)
- [paused](#paused)
- [shown](#shown)
- [spawnDisabled](#spawndisabled)
- [layer](#layer)
- [meta](#meta)

### メソッド

- [load](#load)
- [loadEffect](#loadeffect)
- [clear](#clear)
- [play](#play)
- [stop](#stop)
- [stopRoot](#stoproot)
- [progress](#progress)
- [moveToFrame](#movetoframe)
- [render](#render)
- [setRenderMatrix](#setrendermatrix)
- [getRenderMatrix](#getrendermatrix)
- [setRenderScale](#setrenderscale)
- [getRenderScale](#getrenderscale)
- [setCoord](#setcoord)
- [getCoord](#getcoord)
- [setZoom](#setzoom)
- [getZoom](#getzoom)
- [setAngleDeg](#setangledeg)
- [getAngleDeg](#getangledeg)
- [setAngleRad](#setanglerad)
- [getAngleRad](#getanglerad)
- [setRotate](#setrotate)
- [getRotate](#getrotate)
- [setSpeed](#setspeed)
- [getSpeed](#getspeed)
- [setTargetLocation](#settargetlocation)
- [setRandomSeed](#setrandomseed)
- [setDynamicInput](#setdynamicinput)
- [setDynamicInputByName](#setdynamicinputbyname)
- [getDynamicInputByName](#getdynamicinputbyname)
- [findDynamicInput](#finddynamicinput)
- [readMeta](#readmeta)
- [getDynamicInput](#getdynamicinput)
- [sendTrigger](#sendtrigger)

---

### EffekseerPlayer

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `device` | `&nbsp;` | EffekseerDevice インスタンス |

**解説**

コンストラクタ

---

### device

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用

---

### effect

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: loadEffect() で割り当てた EffekseerEffect

---

### loaded

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用

---

### playing

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 再生中か

---

### instanceCount

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: このエフェクトのパーティクル数

---

### renderScale

プロパティ \ アクセス: `r/w`

---

### left

プロパティ \ アクセス: `r/w`

---

### top

プロパティ \ アクセス: `r/w`

---

### z

プロパティ \ アクセス: `r/w`

---

### zoomX

プロパティ \ アクセス: `r/w`

---

### zoomY

プロパティ \ アクセス: `r/w`

---

### angle

プロパティ \ アクセス: `r/w`

**解説**

度

---

### speed

プロパティ \ アクセス: `r/w`

---

### color

プロパティ \ アクセス: `r/w`

**解説**

全体色 0xAARRGGBB (既定 0xFFFFFFFF)。エフェクト全体に乗算される。

---

### paused

プロパティ \ アクセス: `r/w`

**解説**

一時停止

---

### shown

プロパティ \ アクセス: `r/w`

**解説**

表示/非表示

---

### spawnDisabled

プロパティ \ アクセス: `r/w`

**解説**

新規パーティクル生成の停止

---

### layer

プロパティ \ アクセス: `r/w`

**解説**

所属レイヤー (0〜31)

---

### meta

プロパティ \ アクセス: `r/w`

**解説**

再生している素材の付属情報 (EffekseerEffect.meta と同じもの)

player.load() で読んだ場合も触れるよう橋渡ししてある。

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ストレージ名 (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | 読み込み時の拡大率 (省略時 1.0) |
| `entry` | `&nbsp;` | .efkzip 内のエフェクトファイル名 (省略可) |

**解説**

エフェクトファイルを読み込む (このプレイヤー専用)

引数は EffekseerEffect.load と同じ (.efkzip 対応)

---

### loadEffect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `effect` | `&nbsp;` | EffekseerEffect インスタンス |

**解説**

読み込み済みの EffekseerEffect を割り当てる

---

### clear

メソッド

**解説**

割り当て解除 (再生中なら停止する)

---

### play

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `startFrame` | `&nbsp;` | 開始フレーム (省略時 0) |

**解説**

再生開始。再生中の場合はいったん停止してから再スタートする。

---

### stop

メソッド

**解説**

即時停止 (パーティクルも消える)

---

### stopRoot

メソッド

**解説**

ルートのみ停止。新規パーティクルの生成を止め、残りは自然消滅させる。

「エフェクトを綺麗に終わらせる」場合はこちら。

---

### progress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tick` | `&nbsp;` | 経過時間(ミリ秒)<br>配置系の設定は progress() より前に行うこと。 |

**解説**

進行

---

### moveToFrame

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `frame` | `&nbsp;` | フレーム数 (60fps基準) |

**解説**

指定フレームへ移動 (先頭から再計算するため低速)

---

### render

メソッド

**解説**

描画。OpenGL コンテキスト上で、device.onBeginScene()〜onEndScene() の間で呼ぶ。

---

### setRenderMatrix

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**解説**

描画行列 (外側のアフィン変換) を設定する

X' = m11*x + m12*y + m13
Y' = m21*x + m22*y + m23

---

### getRenderMatrix

メソッド

**解説**

%[ m11:, m12:, m13:, m21:, m22:, m23: ]

---

### setRenderScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**解説**

描画行列の線形部にかかる倍率 (既定 1.0)

---

### getRenderScale

メソッド

---

### setCoord

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

表示位置 (画面中央からのピクセルオフセット)

---

### getCoord

メソッド

**解説**

%[ x:, y:, z: ]

---

### setZoom

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**解説**

拡縮 (既定 1.0)

---

### getZoom

メソッド

**解説**

%[ x:, y: ]

---

### setAngleDeg

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `degree` | `&nbsp;` |  |

**解説**

画面内回転。角度が正のとき画面上では時計回り。

---

### getAngleDeg

メソッド

---

### setAngleRad

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `radian` | `&nbsp;` |  |

---

### getAngleRad

メソッド

---

### setRotate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

3軸回転(度)。z は setAngleDeg と同じ画面内回転。

x / y は奥行き方向の傾きで、透視投影と組み合わせると効果が分かりやすい。

---

### getRotate

メソッド

**解説**

%[ x:, y:, z: ]

---

### setSpeed

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `speed` | `&nbsp;` |  |

**解説**

再生速度 (1.0 が等速)

---

### getSpeed

メソッド

---

### setTargetLocation

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

ターゲット位置 (エフェクト側で「ターゲット依存」を使っている場合)

座標は配置と同じ画面中央原点のピクセル座標。

---

### setRandomSeed

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `seed` | `&nbsp;` |  |

**解説**

乱数シードを固定する

---

### setDynamicInput

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | エフェクト側で定義された動的入力の番号 (0 始まり)<br>範囲外の index は無視される (取得は 0 を返す)。 |
| `value` | `&nbsp;` |  |

**解説**

動的パラメータ (Effekseer エディタの Dynamic Input)

---

### setDynamicInputByName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

**解説**

動的パラメータを名前で差し込む / 読む

対応は .efkzip の effect.json から自動で入る
(EffekseerEffect.setDynamicInputNames() で差し替えもできる)。
知らない名前を渡すと例外。

player.setDynamicInputByName("emitter.x", 120);

---

### getDynamicInputByName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### findDynamicInput

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**解説**

差し込める名前かどうかの確認。知らなければ -1

---

### readMeta

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### getDynamicInput

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### sendTrigger

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | エフェクト側で定義されたトリガーの番号 (0 始まり) |

**解説**

トリガー送出 (Effekseer エディタの Trigger)

---
