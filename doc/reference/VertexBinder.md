# VertexBinder

VertexBinderはVertexBufferとシェーダーに入力する頂点情報を関連付けるためのクラスです。
ShaderProgramのプロパティにはこのクラスのインスタンスを設定します。
ShaderProgramに設定されたVertexBinderは、Canvs.drawMeshで呼び出された時シェーダーへ頂点情報として渡されます。

## メンバー一覧

### コンストラクタ

- [VertexBinder](#vertexbinder)

### プロパティ

- [vertexBuffer](#vertexbuffer)
- [stride](#stride)
- [componentCount](#componentcount)
- [offset](#offset)
- [normalize](#normalize)

---

### VertexBinder

コンストラクタ

**引数**

| 引数 | 型 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `vertex` | `VertexBuffer` | `&nbsp;` | 関連付けるVertexBuffer |
| `stride` | `int` | `0` | 頂点ごとのストライドをバイト数で指定します。XY座標をfloat型で渡すのであればsizeof(float)*2なので、8を指定します。 |
| `componentCount` | `int` | `4` | 頂点要素数を渡します。XY座標を渡すのであれば2を指定します。RGBAカラーなら4です。 |
| `offset` | `int` | `0` | VertexBufferの先頭からのオフセットをバイト数で指定します。一つのVertexBufferで複数の頂点情報を格納している場合に使用します。 |
| `normalize` | `bool` | `false` | 正規化するかどうかを指定します。trueの場合、非float型の時[-1.0～0.0～1.0]の間に正規化されシェーダーに送られます。 |

**解説**

コンストラクタ

---

### vertexBuffer

プロパティ \ アクセス: `r/w`

**解説**

頂点バッファ(VertexBufferクラス readonly)

---

### stride

プロパティ \ アクセス: `r/w`

**解説**

頂点ごとのストライド(バイト数)

デフォルトは0。

---

### componentCount

プロパティ \ アクセス: `r/w`

**解説**

頂点要素数 (1～4)

デフォルトは4
XY座標の時は、2を指定する。

---

### offset

プロパティ \ アクセス: `r/w`

**解説**

頂点バッファオフセット(バイト数)

デフォルトは0。
VertexBufferの先頭からのバイトオフセットを指定する。
一つのVertexBufferで複数の頂点情報を格納している場合に使用します。

---

### normalize

プロパティ \ アクセス: `r/w`

**解説**

正規化するかどうか

デフォルトはfalse。
trueの場合、非float型の時[-1.0～0.0～1.0]の間に正規化されシェーダーに送られます。
色情報などubyte形で0～255で色を指定し、その色を0.0～1.0に正規化してシェーダーで使う等するときに指定します。

---
