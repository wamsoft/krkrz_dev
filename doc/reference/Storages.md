# Storages

Storages クラスは 吉里吉里本体の**ストレージシステム**に関するメソッドやプロパティを持ったクラスです。このクラスからオブジェクトを作成することはできません。

## メンバー一覧

### メソッド
- [addAutoPath](#addautopath)
- [removeAutoPath](#removeautopath)
- [getFullPath](#getfullpath)
- [getPlacedPath](#getplacedpath)
- [isExistentStorage](#isexistentstorage)
- [extractStorageExt](#extractstorageext)
- [extractStorageName](#extractstoragename)
- [extractStoragePath](#extractstoragepath)
- [chopStorageExt](#chopstorageext)
- [searchCD](#searchcd)
- [getLocalName](#getlocalname)
- [selectFile](#selectfile)

---

### addAutoPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 自動検索パスに追加するパスを指定します。 パスの最後は、アーカイブ内のルートフォルダを指定するときは '>'、通常のフォルダを 指定するときは '/' で終わる必要があります ( 例 : `"Archive/arc.xp3>"` や `"System/"` ) 。 2.19 beta 14 よりアーカイブの区切り文字が '#' から '>' に変わりました。 |

**解説**

**自動検索パス**に、指定したパスを追加します。吉里吉里は、利用可能なストレージを
検索するとき、この自動検索パスに登録されたパスを探します。

自動検索パスは、後に指定したものがより優先されて検索されます。

また、プロジェクトフォルダはもっとも優先されて検索されます。

**関連:** [Storages.removeAutoPath](Storages.md#removeautopath)

---

### removeAutoPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 自動検索から削除するパスを指定します。 |

**解説**

自動検索パスから、指定したパスを削除します。

**関連:** [Storages.addAutoPath](Storages.md#addautopath)

---

### getFullPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 完全な統一ストレージ名にしたいストレージ名を指定します。 |

**戻り値**

完全な統一ストレージ名

**解説**

path で指定されたストレージ名を完全な**統一ストレージ名**に変換します。

冗長なパスアクセス ( たとえば `system/flags/../data/` など ) はすべて圧縮されます。

カレントメディア、カレントフォルダが指定されていなければ、補完します。

**関連:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### getPlacedPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 検索したいストレージ名を指定します。 |

**戻り値**

発見された場所が統一ストレージ名で返ります。見つからなかった場合は空文字列が返ります。

**解説**

storage で指定されたストレージを**自動検索パス**から検索します。

**関連:** [Storages.getFullPath](Storages.md#getfullpath) / [Storages.isExistentStorage](Storages.md#isexistentstorage)

---

### isExistentStorage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 存在を確認したいストレージ名を指定します。 |

**戻り値**

存在を確認できれば真、なければ偽が返ります。

**解説**

storage で指定したストレージが存在するかどうかを確認します。getPlacedPath を用いるよりは高速
です。

**関連:** [Storages.getPlacedPath](Storages.md#getplacedpath)

---

### extractStorageExt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 拡張子部分を抽出したいストレージ名を指定します。 |

**戻り値**

拡張子部分が返ります。拡張子部分は `.` (ドット)も含みます。拡張子が
なかった場合は空文字列が返ります。

**解説**

指定されたストレージ名から拡張子の部分を抽出して返します。

**関連:** [Storages.extractStorageName](Storages.md#extractstoragename) / [Storages.extractStoragePath](Storages.md#extractstoragepath) / [Storages.chopStorageExt](Storages.md#chopstorageext)

---

### extractStorageName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | ストレージ名を抽出したいストレージ名を指定します。 |

**戻り値**

ストレージ名が返ります。ストレージ名がなかった場合は空文字列が返ります。

**解説**

指定されたストレージ名から、ストレージ名の部分 ( パスを除く ) を抽出して返します。

たとえば `"System/hoge.txt"` を渡した場合、`"hoge.txt"` が返ります。

**関連:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStoragePath](Storages.md#extractstoragepath)

---

### extractStoragePath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | パスを抽出したいストレージ名を指定します。 |

**戻り値**

パスが返ります。パスがなかった場合は空文字列が返ります。

**解説**

指定されたストレージ名から、パスの部分を抽出して返します。

たとえば `"file://home/dee/hoge.txt"` を渡した場合、`"file://home/dee/"` が
返ります。

**関連:** [Storages.extractStorageExt](Storages.md#extractstorageext) / [Storages.extractStorageName](Storages.md#extractstoragename)

---

### chopStorageExt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 拡張子部分を切り落としたいストレージ名を指定します。 |

**戻り値**

拡張子部分が切り落とされたストレージ名が返ります。

**解説**

指定されたストレージ名から拡張子の部分を切り落として返します。

たとえば `"file://home/dee/hoge.txt"` を渡した場合、`"file://home/dee/hoge"` が返
ります。

**関連:** [Storages.extractStorageExt](Storages.md#extractstorageext)

---

### searchCD

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `volume` | `&nbsp;` | 検索するCDのボリュームラベルを指定します。 |

**戻り値**

見つかった CD-ROM ドライブのドライブ文字が返ります。

**解説**

指定されたボリュームラベルを持つ CD ドライブを探して、そのドライブ文字 ( 'H' など ) を返し
ます。

もちろん、ドライブには該当する CD-ROM が挿入されていなければなりません。

---

### getLocalName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | **ローカルファイル名** に変換したい統一ストレージ名を指定します。 |

**戻り値**

ローカルファイル名が返ります。ローカルファイル名に変換できなかった場合は空文字が返るか、
例外が発生します。

**解説**

指定された統一ストレージ名を、OS ネイティブの形式 ( ローカルファイル名 ) に変換して返します。

---

### selectFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `params` | `&nbsp;` | データの受け渡しに用いる辞書配列を指定します。 このメソッドに渡すとき、以下のメンバを指定することができます。また、 いくつかのメンバはこのメソッドが終わると値が変更されます。 **filter** フィルタ文字列を配列で渡します。 フィルタ文字列は、フィルタの説明と フィルタを \| (半角縦棒) で区切って指定 するもので、フィルタにはワイルドカードを指定します。一つのフィルタに複数の 拡張子が対応する場合は ; (半角セミコロン) で区切ります。 複数のフィルタを指定するには配列で指定します。 省略するとフィルタは用いません。 例 : `["画像ファイル(*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg)\|*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg", ` ` "スクリプトファイル(*.tjs;*.ks)\|*.tjs;*.ks"]` **filterIndex** 選択されているフィルタの番号 ( filter で指定したもの ) を指定します。 1 を指定すると、filter で指定された最初のフィルタが初期状態において 選択されています。2 を指定すると2番目のフィルタが選択さている状態に なります ( 0 から始まるインデックス番号ではないことに注意してください; 先頭は 1 です )。 省略すると先頭のフィルタが選択されます。 また、ユーザが OK ボタンを押した場合、最後にダイアログボックス上で 選ばれていたフィルタのインデックスがこのメンバに設定されます。 **name** ファイル名を指定します。省略したり、空文字列を指定すると初期状態ではなにもファイルを選択 されていない状態にすることができます。 また、ユーザが OK ボタンを押した場合、選択されたファイルがこのメンバに 設定されます。 **initialDir** 初期状態で表示するフォルダを指定します。 省略するとカレントディレクトリが使用されます。 **title** ダイアログボックスのタイトルを表示します。 省略されるとデフォルトの「開く」や「名前を付けて保存」になります ( save メンバの設定によります )。 **save** ダイアログボックスの種類を指定します。 false(デフォルト) の場合、「開く」のダイアログボックスが使われます。 true の場合、「名前を付けて保存」のダイアログボックスが使われます。 **defaultExt** デフォルトの拡張子を指定します。ユーザが拡張子を指定しなかった場合に 自動的にこの拡張子を付加します。ここで指定する拡張子には . (ピリオド)を 指定しないでください。 省略すると、拡張子が付加されることはありません。 |

**戻り値**

ユーザがファイルを選択して OK ボタンを押せば真、キャンセルボタンを押せば偽が戻ります。

**解説**

ファイル選択ダイアログボックスを開きます。

```
var params = %[
filter : [ "テキストファイル(*.txt)|*.txt", "バイナリファイル(*.bin)|*.bin" ],
filterIndex : 1,
name : "",
initialDir : System.exePath,
title : "ファイルを開く",
save : false,
];
if(Storages.selectFile(params))
System.inform("選択したファイルは : " + params.name);
```

---
