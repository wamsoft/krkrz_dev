# 音声再生機能

吉里吉里Z がサポートする音声再生機能について記載します。

### 目次

[概要](#overview)

[諸元](#spec)

[対応形式](#format)

[シームレスループ (.sli)](#loop)

[3D 定位 (spatializer)](#spatializer)

[リップシンク/解析 API](#analysis)

[時間伸縮/ピッチシフト](#phasevocoder)

## 概要 { #overview }

現行の吉里吉里Z は、全ビルドで **miniaudio** を単一の音声エンジンとして使用します (旧 DirectSound 実装は撤去されています)。

- **WINVER** — miniaudio が出力デバイスを所有し、直接デバイスへ出力します。
- **SDL(GENERIC)** — miniaudio をデバイス I/O 無効 (no-device) モードで回して PCM を生成し、出力デバイスは SDL3 が所有します。

いずれの系統でもデコード・ミキシング・エフェクト・3D 定位といった音声処理の中核は共通です。

## 諸元 { #spec }

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| 値 | 量子化ビット数 | 整数 : 8bit ～ 32bit<br>浮動小数点 : 32bit |
| 値 | チャンネル数 | 1ch, 2ch, 4ch, 6ch(5.1ch) |
| 値 | サンプリング周波数 | ソースに依存 (44.1kHz / 48kHz 等) |
| 設定可能値 | 音量 | 0 ～ 100000<br>0 : 完全ミュート<br>100000 : 100% |
| 設定可能値 | 音声バランス<br>(パニング) | -100000 ～ 0 ～ 100000<br>-100000 : 完全に左<br>0 : 中央<br>100000 : 完全に右 |
| 設定可能値 | 再生位置 | ミリ秒、サンプル番号 |

## 対応形式 { #format }

WaveSoundBuffer で標準対応する形式は以下の通りです。

| 形式 | 拡張子 | 備考 |
| --- | --- | --- |
| WAV (RIFF PCM) | .wav | WAVE_FORMAT_PCM (8～32bit 整数)、WAVE_FORMAT_IEEE_FLOAT (32bit float)、WAVE_FORMAT_EXTENSIBLE (PCM / IEEE_FLOAT サブタイプ) に対応。 |
| Ogg Vorbis | .ogg | Vorbis デコード。 |
| Opus | .opus | Opus デコード。 |

デコーダ側のアロケーションは **SoundAllocator** の TLSF プールを経由します。プールサイズは `-soundpoolsize` で指定でき、既定は 128MB です。

対応形式はプラグインによって拡張することができます。

## シームレスループ (.sli) { #loop }

サウンドループ情報ファイル (`.sli` ファイル) を用いることで、つなぎめを感じさせないシームレスなループ再生が可能です。ループ位置の指定を含む `.sli` ファイルは、ループチューナで作成します。

## 3D 定位 (spatializer) { #spatializer }

miniaudio ベースの 3D 定位機能を備えています。

- `WaveSoundBuffer.use3D` を有効にすると、そのバッファは 3D 音源として扱われます。
- 音源側は `set3DPosition` / `set3DVelocity` / `set3DCone` などで位置・速度・指向性を設定します。
- リスナー側は `SoundListener` で位置・向き・速度などを制御します。

距離減衰モデルは次の 4 種から選択できます。

| モデル | 説明 |
| --- | --- |
| amNone | 距離減衰なし |
| amInverse | 逆数減衰 |
| amLinear | 線形減衰 |
| amExponential | 指数減衰 |

なお HRTF には対応していないため、前後の区別はつきません。

## リップシンク/解析 API { #analysis }

再生中の音声を解析するための API を備えています。リップシンクや音声可視化に利用できます。

| API | 内容 |
| --- | --- |
| getSoundLevel | RMS / ピークの音量レベルを取得します。 |
| getSoundSpectrum | 帯域ごとのスペクトルを取得します。 |
| getVowel | 日本語 5 母音の推定重みを取得します。 |
| getVisBuffer | 再生位置周辺の生 PCM を取得します。 |

## 時間伸縮/ピッチシフト { #phasevocoder }

Phase Vocoder による時間伸縮 (テンポ変更) およびピッチシフトに対応します。`WaveSoundBuffer.filters` を通じて適用します。
