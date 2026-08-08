# EffekseerEffect

エフェクト素材

読み込み済みのエフェクトを保持する。複数の EffekseerPlayer から共有できるので、
同じエフェクトを多数同時再生する場合はこちらを使い回すとよい。

## メンバー一覧

### コンストラクタ

- [EffekseerEffect](#effekseereffect)

### プロパティ

- [device](#device)
- [meta](#meta)
- [loaded](#loaded)
- [filename](#filename)
- [magnification](#magnification)
- [termMin](#termmin)
- [termMax](#termmax)

### メソッド

- [load](#load)
- [clear](#clear)
- [unloadResources](#unloadresources)
- [reloadResources](#reloadresources)
- [readMeta](#readmeta)
- [setDynamicInputNames](#setdynamicinputnames)
- [findDynamicInput](#finddynamicinput)

---

### EffekseerEffect

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

### meta

プロパティ \ アクセス: `r/w`

**解説**

.efkzip に同梱された付属情報 (effect.json)。無ければ void

エフェクトのバイナリには「動的パラメータの名前」が残らない。入るのは
既定値とコンパイル済みのコードだけで、本来は番号でしか触れない。そこで
名前と番号の対応などを JSON で持たせておく約束にしてある。
.efkzip を読んだ時点で自動的に解釈されるので、読み込み側の手続きは要らない。

意味づけが決まっているのは次の 2 つだけで、残りはそのまま渡される:
dynamicInputs … [ %[ name:"emitter.x", index:0 ], ... ]
setDynamicInputByName() の対応表として自動で取り込まれる
motions       … [ %[ name:"...", file:"motion/....json", ... ], ... ]

var meta = effect.meta;
if (meta !== void && meta.motions !== void)
var path = effect.readMeta(meta.motions[0].file);

---

### loaded

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 読み込み済みか

---

### filename

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 正規化済みストレージ名

---

### magnification

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 読み込み時拡大率

---

### termMin

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 想定再生長の最小(フレーム)

---

### termMax

プロパティ \ アクセス: `r/w`

**解説**

読み出し専用: 想定再生長の最大(フレーム)

---

### load

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ストレージ名 (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | 読み込み時の拡大率 (省略時 1.0) |
| `entry` | `&nbsp;` | .efkzip 内のエフェクトファイル名 (省略可)<br>・.efkzip … エフェクト本体とテクスチャ/モデル一式を固めた ZIP。<br>Effekseer のエフェクトは資材が複数ファイルに分かれるため、通常はこの形式を使う<br>(Live2D の .l2d と同じ考え方)。資材は ZIP 内の相対パスで解決される。<br>entry 省略時は ZIP 内の最初の .efkefc (無ければ .efk) を使う。<br>・.efkefc / .efk … 単体ファイル指定。資材は filename と同じディレクトリを基準に<br>解決され、見つからない場合はファイル名だけで自動検索パスも探す<br>(XP3 へパックしてディレクトリ構造が畳まれた場合の対策)。<br>失敗した場合は例外が発生する。 |

**解説**

エフェクトファイルを読み込む

---

### clear

メソッド

**解説**

内容消去

---

### unloadResources

メソッド

**解説**

資材(テクスチャ/モデル等)の破棄・再読込

---

### reloadResources

メソッド

---

### readMeta

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ZIP 内のパス |

**戻り値**

解釈できなければ void

**解説**

.efkzip 内の JSON ファイルを辞書 / 配列として読む

---

### setDynamicInputNames

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `names` | `&nbsp;` |  |

**解説**

動的パラメータの名前と入力番号の対応を差し替える

.efkzip なら effect.json から自動で入るので普通は呼ばなくてよい。
.efk / .efkefc を直接読んだ場合や、名前を付け替えたい場合に使う。

effect.setDynamicInputNames(%[ "emitter.x" => 0, "emitter.y" => 1 ]);
effect.setDynamicInputNames(["emitter.x", "emitter.y"]);  // 並び順が番号
effect.setDynamicInputNames([ %[ name:"emitter.x", index:0 ] ]);

void を渡すと登録を消す。

---

### findDynamicInput

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**戻り値**

見つからなければ -1

**解説**

登録した対応から入力番号を引く

---
