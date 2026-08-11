# SoundListener

SoundListener クラスは 3D 音声定位における「リスナー」を制御するためのクラスです。このクラスからオブジェクトを作成することはできません。System と同様に `SoundListener.setPosition(...)` のように直接呼び出して使用します。

このクラスは miniaudio ベースの 3D 音声定位における、エンジンで共有されるリスナー ( listener 0 ) を制御します。音源側は WaveSoundBuffer の [use3D](WaveSoundBuffer.md#use3d) や set3DPosition 等で設定します。

座標系は miniaudio に準じます ( 右手系・Y up・任意単位、既定では forward = -Z, up = +Y、コーン角はラジアン )。

なお HRTF には対応していません。ステレオ環境では前後の区別はつかず、L / R のパンと距離による減衰のみが反映されます。

## メンバー一覧

### プロパティ

- [enabled](#enabled)

### メソッド

- [setPosition](#setposition)
- [setDirection](#setdirection)
- [setWorldUp](#setworldup)
- [setVelocity](#setvelocity)
- [setCone](#setcone)

---

### enabled

プロパティ \ アクセス: `r/w`

**解説**

リスナー ( 3D 定位 ) を有効にするか

リスナー ( 3D 定位 ) を有効にするかどうかを表します。値を設定することもできます。

**関連:** [WaveSoundBuffer.use3D](WaveSoundBuffer.md#use3d)

---

### setPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 位置の X 成分を指定します。 |
| `y` | `&nbsp;` | 位置の Y 成分を指定します。 |
| `z` | `&nbsp;` | 位置の Z 成分を指定します。 |

**解説**

リスナー位置の設定

リスナーの位置を設定します。

---

### setDirection

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | forward ベクトルの X 成分を指定します。 |
| `y` | `&nbsp;` | forward ベクトルの Y 成分を指定します。 |
| `z` | `&nbsp;` | forward ベクトルの Z 成分を指定します。 |

**解説**

リスナーの向きの設定

リスナーの向き ( forward ベクトル ) を設定します。

---

### setWorldUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | up ベクトルの X 成分を指定します。 |
| `y` | `&nbsp;` | up ベクトルの Y 成分を指定します。 |
| `z` | `&nbsp;` | up ベクトルの Z 成分を指定します。 |

**解説**

ワールドの上方向ベクトルの設定

ワールドの上方向 ( up ) ベクトルを設定します。

---

### setVelocity

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 速度の X 成分を指定します。 |
| `y` | `&nbsp;` | 速度の Y 成分を指定します。 |
| `z` | `&nbsp;` | 速度の Z 成分を指定します。 |

**解説**

リスナー速度の設定

ドップラー計算に用いるリスナーの速度を設定します。

---

### setCone

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `innerAngleRad` | `&nbsp;` | コーンの内側角度をラジアンで指定します。 |
| `outerAngleRad` | `&nbsp;` | コーンの外側角度をラジアンで指定します。 |
| `outerGain` | `&nbsp;` | コーンの外側でのゲインを指定します ( 0 〜 1 )。 |

**解説**

リスナーの指向性コーンの設定

リスナーの指向性コーンを設定します。角度はラジアンで指定します。

---
