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
| `path` | `&nbsp;` | 自動検索パスに追加するパスを指定します。<br>パスの最後は、アーカイブ内のルートフォルダを指定するときは '>'、通常のフォルダを<br>指定するときは '/' で終わる必要があります<br>( 例 : `"Archive/arc.xp3>"` や `"System/"` ) 。<br>2.19 beta 14 よりアーカイブの区切り文字が '#' から '>' に変わりました。 |

**解説**

自動検索パスへの追加

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

自動検索パスの削除

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

完全な統一ストレージ名の取得

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

ストレージの検索

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

ストレージの存在確認

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

ストレージ名の拡張子の抽出

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

ストレージ名の抽出

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

ストレージ名のパスの抽出

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

ストレージ名の拡張子の切り落とし

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

CD の検索

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

ローカルファイル名の取得

指定された統一ストレージ名を、OS ネイティブの形式 ( ローカルファイル名 ) に変換して返します。

---

### selectFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `params` | `&nbsp;` | データの受け渡しに用いる辞書配列を指定します。<br>このメソッドに渡すとき、以下のメンバを指定することができます。また、<br>いくつかのメンバはこのメソッドが終わると値が変更されます。<br>**filter**<br>フィルタ文字列を配列で渡します。<br>フィルタ文字列は、フィルタの説明と フィルタを \| (半角縦棒) で区切って指定<br>するもので、フィルタにはワイルドカードを指定します。一つのフィルタに複数の<br>拡張子が対応する場合は ; (半角セミコロン) で区切ります。<br>複数のフィルタを指定するには配列で指定します。<br>省略するとフィルタは用いません。<br>例 :<br>`["画像ファイル(*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg)\|*.bmp;*.png;*.jpg;*.jpeg;*.eri;*.tlg", `<br>` "スクリプトファイル(*.tjs;*.ks)\|*.tjs;*.ks"]`<br>**filterIndex**<br>選択されているフィルタの番号 ( filter で指定したもの ) を指定します。<br>1 を指定すると、filter で指定された最初のフィルタが初期状態において<br>選択されています。2 を指定すると2番目のフィルタが選択さている状態に<br>なります ( 0 から始まるインデックス番号ではないことに注意してください;<br>先頭は 1 です )。<br>省略すると先頭のフィルタが選択されます。<br>また、ユーザが OK ボタンを押した場合、最後にダイアログボックス上で<br>選ばれていたフィルタのインデックスがこのメンバに設定されます。<br>**name**<br>ファイル名を指定します。省略したり、空文字列を指定すると初期状態ではなにもファイルを選択<br>されていない状態にすることができます。<br>また、ユーザが OK ボタンを押した場合、選択されたファイルがこのメンバに<br>設定されます。<br>**initialDir**<br>初期状態で表示するフォルダを指定します。<br>省略するとカレントディレクトリが使用されます。<br>**title**<br>ダイアログボックスのタイトルを表示します。<br>省略されるとデフォルトの「開く」や「名前を付けて保存」になります<br>( save メンバの設定によります )。<br>**save**<br>ダイアログボックスの種類を指定します。<br>false(デフォルト) の場合、「開く」のダイアログボックスが使われます。<br>true の場合、「名前を付けて保存」のダイアログボックスが使われます。<br>**defaultExt**<br>デフォルトの拡張子を指定します。ユーザが拡張子を指定しなかった場合に<br>自動的にこの拡張子を付加します。ここで指定する拡張子には . (ピリオド)を<br>指定しないでください。<br>省略すると、拡張子が付加されることはありません。 |

**戻り値**

ユーザがファイルを選択して OK ボタンを押せば真、キャンセルボタンを押せば偽が戻ります。

**解説**

ファイル選択ダイアログボックスを表示

ファイル選択ダイアログボックスを開きます。

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

---

## プラグイン拡張: fstat

擬似コードによるマニュアル

Copyright 2007 GoWatanabe

### メンバー一覧

#### メソッド

- [fstat](#fstat)
- [exportFile](#exportfile)
- [deleteFile](#deletefile)
- [truncateFile](#truncatefile)
- [moveFile](#movefile)
- [dirlist](#dirlist)
- [dirlistEx](#dirlistex)
- [dirtree](#dirtree)
- [removeDirectory](#removedirectory)
- [createDirectory](#createdirectory)
- [createDirectoryNoNormalize](#createdirectorynonormalize)
- [changeDirectory](#changedirectory)
- [setFileAttributes](#setfileattributes)
- [resetFileAttributes](#resetfileattributes)
- [getFileAttributes](#getfileattributes)
- [selectDirectory](#selectdirectory)
- [isExistentDirectory](#isexistentdirectory)
- [getTime](#gettime)
- [setTime](#settime)
- [getLastModifiedFileTime](#getlastmodifiedfiletime)
- [setLastModifiedFileTime](#setlastmodifiedfiletime)
- [copyFile](#copyfile)
- [copyFileNoNormalize](#copyfilenonormalize)
- [isExistentStorageNoSearchNoNormalize](#isexistentstoragenosearchnonormalize)
- [getDisplayName](#getdisplayname)
- [getMD5HashString](#getmd5hashstring)
- [searchPath](#searchpath)
- [getTemporaryName](#gettemporaryname)

---

### fstat

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**戻り値**

属性情報の入った辞書
size: ファイルサイズ
mtime: 更新日時 (Date オブジェクト)
atime: アクセス日時 (Date オブジェクト)
ctime: 作成日時 (Date オブジェクト)

**解説**

ファイル属性の取得

---

### exportFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 保存元ファイル |
| `dest` | `&nbsp;` | 保存先ファイル |

**解説**

吉里吉里のストレージ空間中のファイルを抽出する

---

### deleteFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 削除対象ファイル |

**戻り値**

実際に削除されたら true
実ファイルがある場合のみ削除されます

**解説**

吉里吉里のストレージ空間中の指定ファイルを削除する。

---

### truncateFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | ファイル |
| `size` | `&nbsp;` | 指定サイズ |

**戻り値**

サイズ変更できたら true
実ファイルがある場合のみ処理されます

**解説**

吉里吉里のストレージ空間中の指定ファイルのサイズを変更する(切り捨てる)

---

### moveFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `fromFile` | `&nbsp;` | 移動対象ファイル |
| `toFile` | `&nbsp;` | 移動先パス |

**戻り値**

実際に移動されたら true
移動対象ファイルが実在し、移動先パスにファイルが無い場合のみ移動されます
※パスはNormalize/Placedチェックされないのでフルパスで記入のこと

**解説**

指定ファイルを移動する。

---

### dirlist

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

ファイル名一覧が格納された配列

**解説**

指定ディレクトリのファイル一覧を取得する

---

### dirlistEx

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

ファイル情報一覧が格納された配列
[ %[ name:ファイル名, size, attrib, mtime, atime, ctime ], ... ]
dirlistと違いnameにおいてフォルダの場合の末尾"/"追加がないので注意(attribで判定のこと)

**解説**

指定ディレクトリのファイル一覧と詳細情報を取得する

---

### dirtree

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |
| `dironly` | `false` | フォルダ名のみでファイルは除外する |

**戻り値**

一覧が格納された配列（木構造ではなくサブフォルダ含む全列挙）
一覧には ./ ../ 系の自身や親の参照は含まれません

**解説**

指定ディレクトリ以下のファイル・フォルダ一覧（サブフォルダ含む）を取得する

---

### removeDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

実際に削除されたら true
中にファイルが無い場合のみ削除されます

**解説**

指定ディレクトリを削除する

---

### createDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

実際に作成できたら true

**解説**

ディレクトリを作成する

---

### createDirectoryNoNormalize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

実際に作成できたら true

**解説**

パスの正規化を行なわずディレクトリを作成する

(ディレクトリ名が小文字に変換されない)

---

### changeDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

実際に変更できたら true

**解説**

カレントディレクトリを変更する

---

### setFileAttributes

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |
| `attr` | `&nbsp;` | 設定する属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...) |

**解説**

ファイルの属性を設定する

---

### resetFileAttributes

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |
| `attr` | `&nbsp;` | 解除する属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...) |

**解説**

ファイルの属性を解除する

---

### getFileAttributes

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル/ディレクトリ名 |

**戻り値**

取得した属性(FILE_ATTRIBUTE_READONLY,FILE_ATTRIBUTE_HIDDEN,...)

**解説**

ファイルの属性を取得する

---

### selectDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `params` | `%[name:"", title:"", window:void, rootDir:""]` | selectFile と同様のパラメータを設定する |

**戻り値**

フォルダを選択してOKボタンを押せば真、キャンセルボタンを押せば偽
params.name フォルダ名を指定します。OKボタンを押した場合、選択されたフォルダがこのメンバに設定されます
params.title ダイアログボックスのタイトルを表示します
params.window ダイアログを開くWindowオブジェクトを指定します(void なら mainWindow が、未指定ならデスクトップがオーナーウィンドウとなります。デスクトップがオーナーの場合は、モードレス)
params.rootDir フォルダ選択のルートを指定します(このフォルダ以下のみ表示されます)

**解説**

フォルダ選択ダイアログを開く

---

### isExistentDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | ディレクトリ名 |

**戻り値**

ディレクトリが存在すれば true/存在しなければ -1/ディレクトリでなければ false

**解説**

ディレクトリの存在チェック

---

### getTime

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 対象ファイルまたはディレクトリ |

**戻り値**

タイムスタンプ情報の入った辞書
mtime: 更新日時 (Date オブジェクト)
atime: アクセス日時 (Date オブジェクト)
ctime: 作成日時 (Date オブジェクト)
⇒fstatとの違いは非アーカイブファイル限定で，sizeを返さないこと

**解説**

タイムスタンプ取得

---

### setTime

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 対象ファイルまたはディレクトリ |
| `times` | `&nbsp;` | タイムスタンプ情報の入った辞書<br>mtime: 更新日時 (Date オブジェクト)<br>atime: アクセス日時 (Date オブジェクト)<br>ctime: 作成日時 (Date オブジェクト) |

**戻り値**

成功したかどうか

**解説**

タイムスタンプ設定

---

### getLastModifiedFileTime

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 対象ファイルまたはディレクトリ |

**戻り値**

時間（WINDOWSのFILETIME 64bit値）

**解説**

更新日取得（高速版）

---

### setLastModifiedFileTime

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 対象ファイルまたはディレクトリ |
| `time` | `&nbsp;` | 時間（WINDOWSのFILETIME 64bit値） |

**戻り値**

成功したかどうか

**解説**

更新日設定（高速版）

---

### copyFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `from` | `&nbsp;` | コピー元ファイル |
| `to` | `&nbsp;` | コピー先ファイル |
| `failIfExist` | `&nbsp;` | ファイルが存在するときに失敗するなら ture、上書きするなら false |

**戻り値**

実際にコピーできたら true

**解説**

吉里吉里のストレージ空間中の指定ファイルをコピーする

---

### copyFileNoNormalize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `from` | `&nbsp;` | コピー元ファイル |
| `to` | `&nbsp;` | コピー先ファイル |
| `failIfExist` | `&nbsp;` | ファイルが存在するときに失敗するなら ture、上書きするなら false |

**戻り値**

実際にコピーできたら true
※toには「file://./c/～」のようにフルパスで記述しないと例外が発生します

**解説**

パスの正規化を行なわず吉里吉里のストレージ空間中の指定ファイルをコピーする

(コピー先ファイルのファイル名が小文字に変換されない)

---

### isExistentStorageNoSearchNoNormalize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名 |

**戻り値**

ファイルが存在したらtrue

**解説**

パスの正規化を行なわず、autoPathからの検索も行なわずに

ファイルの存在確認を行う

---

### getDisplayName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | ファイル名（親ディレクトリ以上のパスは落とされるので注意)。 |

**戻り値**

表示名

**解説**

表示名の取得

実際にエクスプローラで表示されるファイル名を返す (SHGetFileInfoによる)

---

### getMD5HashString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ファイル名 |

**戻り値**

ハッシュ値（32文字の16進数ハッシュ文字列（小文字））

**解説**

MD5ハッシュ値の取得

---

### searchPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 検索対象ファイル名 |
| `searchpath` | `&nbsp;` | 検索対象パス（ローカル表記(c:\\～等)で";"区切り，省略時はシステムのデフォルト検索パス） |

**戻り値**

見つからなかった場合はvoid，見つかった場合はファイルのフルパス(file://./～)

**解説**

パスの検索

---

### getTemporaryName

メソッド

**戻り値**

テンポラリファイル名（TVPGetTemporaryName()の文字列）

**解説**

テンポラリファイル名の取得

---

## プラグイン拡張: memfile

擬似コードによるマニュアル

mem://./ファイル名 でオンメモリ確保されたファイルとしてアクセス可能になります。

### メンバー一覧

#### メソッド

- [isExistMemoryFile](#isexistmemoryfile)
- [isExistMemoryDirectory](#isexistmemorydirectory)
- [deleteMemoryFile](#deletememoryfile)
- [deleteMemoryDirectory](#deletememorydirectory)
- [getMemoryFileInfo](#getmemoryfileinfo)
- [getMemoryFileData](#getmemoryfiledata)
- [getMemoryDirectory](#getmemorydirectory)

---

### isExistMemoryFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ファイル名 (mem:///はつけない) |

**戻り値**

存在したら true

**解説**

メモリファイルの存在確認

---

### isExistMemoryDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

**戻り値**

存在したら true

**解説**

メモリディレクトリの存在確認

---

### deleteMemoryFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ファイル名 (mem:///はつけない) |

**戻り値**

ファイルが削除されたら true

**解説**

メモリファイルを削除する

---

### deleteMemoryDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dirname` | `&nbsp;` | 対象ディレクトリ名 (mem:///はつけない) |

**戻り値**

ディレクトリが削除されたら true

**解説**

メモリディレクトリを削除する

---

### getMemoryFileInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ファイル名 (mem:///はつけない) |

**戻り値**

ファイル情報 %[name:名前, size:サイズ, isDirectory:ディレクトリならtrue]

**解説**

メモリファイル情報を取得する

---

### getMemoryFileData

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 対象ファイル名 (mem:///はつけない) |

**戻り値**

ファイルが存在したら内容を octet で返す。なければ void

**解説**

メモリファイル情報を取得する

---

### getMemoryDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dirname` | `&nbsp;` | 対象ディレクトリ名 (mem:///はつけない) |

**戻り値**

ファイル情報の配列 %[name:名前, size:サイズ, isDirectory:ディレクトリならtrue]

**解説**

メモリディレクトリ情報を取得する

---

## プラグイン拡張: minizip

Storages クラス機能拡張

### メンバー一覧

#### メソッド

- [mountZip](#mountzip)
- [unmountZip](#unmountzip)

---

### mountZip

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ドメイン名 |
| `zipfile` | `&nbsp;` | マウントするZIPファイル名 |

**戻り値**

マウントに成功したら true

**解説**

zipファイルをファイルシステムとして mount します

zip://ドメイン名/ファイル名 でアクセス可能になります。読み込み専用になります。

---

### unmountZip

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ドメイン名 |

**戻り値**

アンマウントに成功したら true

**解説**

zipファイルを unmount します

---
