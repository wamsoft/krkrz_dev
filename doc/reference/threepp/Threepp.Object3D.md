# Threepp.Object3D

3Dオブジェクトの基底クラス

シーングラフ内のすべての3Dオブジェクトの基底となるクラスです。

## メンバー一覧

### コンストラクタ

- [Object3D](#object3d)

### プロパティ

- [type](#type)
- [id](#id)
- [name](#name)
- [visible](#visible)
- [castShadow](#castshadow)
- [receiveShadow](#receiveshadow)
- [frustumCulled](#frustumculled)
- [renderOrder](#renderorder)
- [position](#position)
- [rotation](#rotation)
- [quaternion](#quaternion)
- [scale](#scale)
- [up](#up)

### メソッド

- [setPosition](#setposition)
- [setRotation](#setrotation)
- [setScale](#setscale)
- [add](#add)
- [remove](#remove)
- [removeFromParent](#removefromparent)
- [clear](#clear)
- [lookAt](#lookat)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [rotateOnAxis](#rotateonaxis)
- [rotateOnWorldAxis](#rotateonworldaxis)
- [translateX](#translatex)
- [translateY](#translatey)
- [translateZ](#translatez)
- [translateOnAxis](#translateonaxis)
- [updateMatrix](#updatematrix)
- [updateMatrixWorld](#updatematrixworld)
- [treeJson](#treejson)
- [getWorldPosition](#getworldposition)
- [getWorldQuaternion](#getworldquaternion)
- [getWorldScale](#getworldscale)

---

### Object3D

コンストラクタ

**解説**

コンストラクタ

---

### type

プロパティ \ アクセス: `r/w`

**解説**

オブジェクトの種類（読み取り専用）

---

### id

プロパティ \ アクセス: `r/w`

**解説**

オブジェクトID（読み取り専用）

---

### name

プロパティ \ アクセス: `r/w`

**解説**

オブジェクト名

---

### visible

プロパティ \ アクセス: `r/w`

**解説**

表示/非表示

---

### castShadow

プロパティ \ アクセス: `r/w`

**解説**

影を落とすか

---

### receiveShadow

プロパティ \ アクセス: `r/w`

**解説**

影を受けるか

---

### frustumCulled

プロパティ \ アクセス: `r/w`

**解説**

視錐台カリングを行うか

---

### renderOrder

プロパティ \ アクセス: `r/w`

**解説**

描画順序

---

### position

プロパティ \ アクセス: `r/w`

**解説**

注意: position/rotation/scale/quaternion の getter は「値のコピー」を返すため、 obj.position.set(...) や obj.position.x = ... を書いても本体には反映されません。 位置・回転・スケールを変えるには下の setPosition/setRotation/setScale を使ってください。

---

### rotation

プロパティ \ アクセス: `r/w`

**解説**

回転 (Euler、値コピー = 実質読み取り専用)

---

### quaternion

プロパティ \ アクセス: `r/w`

**解説**

回転 (Quaternion、値コピー = 実質読み取り専用)

---

### scale

プロパティ \ アクセス: `r/w`

**解説**

スケール (Vector3、値コピー = 実質読み取り専用)

---

### up

プロパティ \ アクセス: `r/w`

**解説**

上方向ベクトル (Vector3、値コピー)

---

### setPosition

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

位置を設定 (position.set の代わりにこれを使う)

---

### setRotation

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

回転(オイラー角ラジアン)を設定

---

### setScale

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**解説**

スケールを設定

---

### add

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 追加するObject3D |

**解説**

子オブジェクトを追加

---

### remove

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 削除するObject3D |

**解説**

子オブジェクトを削除

---

### removeFromParent

メソッド

**解説**

親から自身を削除

---

### clear

メソッド

**解説**

すべての子オブジェクトを削除

---

### lookAt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X座標 |
| `y` | `&nbsp;` | Y座標 |
| `z` | `&nbsp;` | Z座標 |

**解説**

指定した点を向く

---

### rotateX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

X軸回転

---

### rotateY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

Y軸回転

---

### rotateZ

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**解説**

Z軸回転

---

### rotateOnAxis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**解説**

任意軸回転（ローカル）

---

### rotateOnWorldAxis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**解説**

任意軸回転（ワールド）

---

### translateX

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**解説**

X軸移動

---

### translateY

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**解説**

Y軸移動

---

### translateZ

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**解説**

Z軸移動

---

### translateOnAxis

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `distance` | `&nbsp;` |  |

**解説**

任意軸移動

---

### updateMatrix

メソッド

**解説**

ローカル行列を更新

---

### updateMatrixWorld

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `force` | `&nbsp;` |  |

**解説**

ワールド行列を更新

---

### treeJson

メソッド

**戻り値**

JSON 文字列

**解説**

サブツリーを JSON 文字列で一括ダンプ (外部インスペクタのシーンツリー表示用)。

1 ノード = {id,name,type,visible,pos:[x,y,z],children:[…]}

---

### getWorldPosition

メソッド

**解説**

--- ワールド変換の取得 (matrixWorld から算出) --- 返り値が最新であるには、直前に render するか updateMatrixWorld(true) を 呼んでおくこと(親をたどって world 行列を確定させる必要がある)。 立ち絵フレーミングで骨(head/hips 等)の world 座標を得るのに使う。

---

### getWorldQuaternion

メソッド

**解説**

-> Quaternion (ワールド回転)

---

### getWorldScale

メソッド

**解説**

-> Vector3 (ワールドスケール)

---
