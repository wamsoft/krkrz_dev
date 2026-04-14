# System

System クラスは 吉里吉里本体や、吉里吉里が実行されている環境に関する情報を取得したり、設定したりするためのクラスです。このクラスからオブジェクトを作成することはできません。

## メンバー一覧

### プロパティ
- [versionString](#versionstring)
- [versionInformation](#versioninformation)
- [eventDisabled](#eventdisabled)
- [graphicCacheLimit](#graphiccachelimit)
- [platformName](#platformname)
- [osName](#osname)
- [exePath](#exepath)
- [personalPath](#personalpath)
- [appDataPath](#appdatapath)
- [dataPath](#datapath)
- [exeName](#exename)
- [title](#title)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [desktopLeft](#desktopleft)
- [desktopTop](#desktoptop)
- [desktopWidth](#desktopwidth)
- [desktopHeight](#desktopheight)
- [exitOnWindowClose](#exitonwindowclose)
- [exceptionHandler](#exceptionhandler)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [drawThreadNum](#drawthreadnum)
- [savedGamesPath](#savedgamespath)
- [exeBits](#exebits)
- [osBits](#osbits)

### メソッド
- [terminate](#terminate)
- [exit](#exit)
- [addContinuousHandler](#addcontinuoushandler)
- [removeContinuousHandler](#removecontinuoushandler)
- [inform](#inform)
- [getTickCount](#gettickcount)
- [getKeyState](#getkeystate)
- [shellExecute](#shellexecute)
- [readRegValue](#readregvalue)
- [getArgument](#getargument)
- [setArgument](#setargument)
- [toActualColor](#toactualcolor)
- [createAppLock](#createapplock)
- [createUUID](#createuuid)
- [assignMessage](#assignmessage)
- [doCompact](#docompact)
- [touchImages](#touchimages)
- [showVersion](#showversion)
- [dumpHeap](#dumpheap)

---

### terminate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `0` | プロセスの終了コードを指定します |

**解説**

吉里吉里を**終了**させます。

このメソッドを呼び出してもすぐには吉里吉里は終了しません。

すべてのイベントハンドラから吉里吉里に制御が戻った際に終了します。

---

### exit

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `0` | プロセスの終了コードを指定します |

**解説**

吉里吉里を**終了**させます。

このメソッドは [System.terminate](System.md#terminate) と異なり、呼び出した時点で終了します。そのため、
このメソッドは戻ることはありません。

---

### addContinuousHandler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | ハンドラとなる関数を指定します。 |

**解説**

**Continuous ハンドラ**を登録します。

Continuous ハンドラは、「できる限り頻繁に」呼び出されるイベントハンドラです。

他にする処理がない場合、吉里吉里は Continuous ハンドラを呼び出し続けます。
他にイベントなどが起きた場合はそちらが優先されます。

ただし、コマンドラインオプションの -contfreq で呼び出しの頻度が指定されている
場合はそれに従います。

---

### removeContinuousHandler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | ハンド関数を指定します。 |

**解説**

**Continuous ハンドラ**を削除します。

---

### inform

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 表示するメッセージを指定します。 |
| `caption` | `""` | ウィンドウのキャプションとなる文字列を指定します。 |

**解説**

ユーザにメッセージを示すためのウィンドウを表示します。

ウィンドウはモーダルで表示されます ( つまり、表示中は他のウィンドウは操作できない )。

---

### getTickCount

メソッド

**戻り値**

ティックカウント(64bitの整数)が戻ります。

**解説**

**ティックカウント**は 1/1000 秒ごとにカウントアップする数値です。二つの時点でこのメソッドを
用いてティックカウントを取得し、その差をとれば、二つの時点の時間差を知ることができます。

---

### getKeyState

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 状態を取得する**仮想キーコード** ( → [vkeys](../guide/vkeys.md) ) を指定します。 |

**戻り値**

キーが押されていれば真、押されていなければ偽になります。

**解説**

code で指定したキーコードに対応するキーが、このメソッドを呼んだ時点で押されているかどうかを
取得します。

---

### shellExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 実行するファイルやソフトウェアを指定します。 ファイルを指定された場合は、それに関連づけられたプログラムが起動します。 |
| `param` | `""` | 実行するソフトウェアに渡すパラメータを指定します。 target 引数にファイルを指定した場合はこの引数を省略するか、あるいは空文字列を 指定してください。 |

**戻り値**

実行に成功すれば真、失敗すれば偽が返ります。

**解説**

target で指定したファイルやソフトウェアを**実行**します。

---

### readRegValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 読み込むレジストリキーを指定します。 |

**戻り値**

実行に成功すればレジストリの値、失敗すれば void が返ります。

**解説**

key で指定した Windows レジストリを読み込みます。

レジストリキーは、以下のルートキー名で始めることができます。

`HKEY_CLASSES_ROOT
HKEY_CURRENT_CONFIG
HKEY_CURRENT_USER

HKEY_LOCAL_MACHINE
HKEY_USERS
HKEY_PERFORMANCE_DATA

HKEY_DYN_DATA
`
たとえば、以下のような文字列を key に指定することができます。

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\hoeg\installdir`



数値、単一文字列のみを読み込むことができます。数値の場合は整数型、文字列の場合は文字列型
の結果が返ります。

---

### getArgument

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 取得するコマンドラインオプション名を指定します。最初に '-' ( ハイフン ) をつけてください ( 例 : `'-nosplash'` )。 |

**戻り値**

コマンドラインオプションが指定されていればその値、指定されていなければ
void が返ります。

**解説**

**コマンドラインオプション**は、

`-name=value`

または

`-name`

の形式で吉里吉里に渡されている必要があります。前者の場合は値として `value` が
返り、前者の場合は値として `'yes'` が返ります。

**関連:** [System.setArgument](System.md#setargument)

---

### setArgument

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 設定するコマンドラインオプション名を指定します。最初に '-' ( ハイフン ) をつけてください ( 例 : `'-contfreq'` )。 |
| `value` | `&nbsp;` | 設定する値を指定します。 ( 例 : `'60'` )。 |

**解説**

動的に**コマンドラインオプション**を設定します。すべてのコマンドラインオプションが設定可能な訳ではありません。

設定可能なコマンドラインオプションについては

を参照してください。ここで動的に変更可能という表記のないオプションについては変更を行わないでください。

このメソッドは、そのオプションが動的に変更可能かどうかやオプションの存在、値の有効性などをチェックしません。値の設定には十分気をつけてください。

**関連:** [System.getArgument](System.md#getargument)

---

### toActualColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 色定数を指定します ( を参照 )。 通常の 0xRRGGBB 形式の色を指定した場合はそのままの値が返ります。 |

**戻り値**

指定された色定数が表す実際の色が 0xRRGGBB 形式で返ります。

**解説**

色定数を実際の色に変換し、0xRRGGBB 形式で返します。

---

### createAppLock

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | チェックを行うためのキー文字列を指定します。同じキー文字列をほかの 実行中の吉里吉里がこのメソッドに指定していた場合、false が戻ります。 キー文字列には基本的には TJS の変数の命名規則と同じ文字のみが使えると 考えてください。 キー文字列は十分にユニークな物である必要があります。 |

**戻り値**

すでに同じキー文字列が指定された吉里吉里が実行中の場合は false、そうでなければ true が戻ります。

**解説**

他に同じキー文字列を指定された吉里吉里が実行中ならば false、そうでなければ true が戻ります。

二重起動の防止に用います。

---

### createUUID

メソッド

**戻り値**

生成された UUID 文字列が "e8b2a2b5-5ceb-4f75-a08b-1f1bdfdca4f1" の形式
(ハイフンを除く各英数字は16進数の数字) で戻ります。

**解説**

UUID 文字列を生成して返します。このメソッドはランダムビット列を元に生成された
128bitの UUID (universal unique identifier) を生成します。

吉里吉里に実装されている UUID 生成アルゴリズムは、
ある程度、環境ノイズを拾ってランダムビット列を生成しますが、
高度なセキュリティが要求されるような用途に使用することはおすすめしません。しかし、
他の UUID とは「非常に非常に高い確率で重ならない」と考えられます。

---

### assignMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 割り当てるメッセージ ID を指定します。 |
| `msg` | `&nbsp;` | id で指定された ID に割り当てるメッセージを指定します。 |

**戻り値**

ID が存在し、メッセージの割り当てが成功すれば真、そうでなければ偽が戻ります。

**解説**

メッセージ割り当てを変更します。

吉里吉里が内蔵しているメッセージをこのメソッドで別のメッセージに変更することができます。

通常、メッセージマップファイル内に記述します (

参照 )。

設定可能な ID と、それに現在割り当てられているメッセージの一覧を取得するには

から
「メッセージマップファイルの作成」を実行してください。

---

### doCompact

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `level` | `clAll` | レベルを指定します。 **clIdle** を指定すると、システムがアイドル状態 (システムが比較的動作をしていない状態) に実行されるコンパクト化と同じ処理が行われます。現バージョンでは TJS2 のガベージコレクションが行われます。 **clDeactivate** を指定すると、吉里吉里が非アクティブになったとき (他のアプリケーションがアクティブになったとき) に実行されるコンパクト化と同じ処理が行われます。現バージョンではレイヤの演算用の一時画像バッファ、レイヤキャッシュ、XP3 アーカイブのセグメント(ストレージの断片) キャッシュ、自動検索パスのキャッシュがクリアされます。 **clMinimize** を指定すると、吉里吉里が最小化されたときに実行されるコンパクト化と同じ処理が行われます。現バージョンでは、描画文字のキャッシュ、画像キャッシュがクリアされます。 **clAll** を指定すると、上記のコンパクト化の全てが実行されます。 コンパクト化のレベルは、clIdle < clDeactivate < clMinimize < clAll の順に強くなります。より上位のレベルを指定すると、下位のレベルで行われるコンパクト化も行われます。たとえば、clDeactivate を実行すると、clIdle での処理も実行されます。 引数を省略すると clAll が指定された物と見なされます。 |

**解説**

メモリのコンパクト化を行います。コンパクト化とは、使用していないメモリや各種キャッシュ用メモリを解放して、メモリ使用量を減らす処理です。

吉里吉里は自動でこれを行うので通常はあまり気にする必要はありませんが、強制的にプログラム側の処理で行いたい場合にこのメソッドを使用することができます。

---

### touchImages

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storages` | `&nbsp;` | キャッシュに入れたい画像ストレージ名を配列(Arrayクラスのオブジェクト)で渡します。 先に書いた物ほど優先されます。 吉里吉里は、[Layer.loadImages](Layer.md#loadimages) の第１引数に指定された 文字列をそのままキーにしてキャッシュを管理するため、 キャッシュを意味のある物にするには、 ここで指定する画像ストレージ名は Layer.loadImages の第１引数に指定するものと 同一である必要があります。 |
| `limitbytes` | `0` | このメソッドの呼び出しで使用するキャッシュ容量の制限値をバイト単位で指定します。 0 を指定すると、キャッシュをすべて使用します。 正の数を指定すると、そのバイト数までキャッシュを使用しようとします。 負の数を指定すると、現在のキャッシュの 制限値 ( [System.graphicCacheLimit](System.md#graphiccachelimit) ) からその数値が加算された数 ( ただし 「負の数」を加算するので実際は減算 ) が制限値として使用されます。その結果制限値が 0 または負になってしまった場合は、このメソッドは何もせずに終了します。たとえば、 -2*1024*1024 を指定すれば、現在のキャッシュ制限値から 2MB が引かれた数値が指定さ れたとみなされます。これは、キャッシュの残り容量に余裕を残したい場合に便利です。 |
| `timeout` | `0` | タイムアウト ( 時間制限 ) を ms 単位で指定します。0 を指定すると無制限と なります。 このメソッドはこの引数で指定された時間が経過すると、以降の画像の読み込みを中止し、 戻ります。ただし、ある画像の読み込み中にタイムアウトになっても、その画像の読み 込みが終了するまでは戻りません。 |

**解説**

このメソッドは、指定された画像をキャッシュに入れようと試行します。ただし、このメソッドは
キャッシュに画像を入れようと努力はしますが、実際に画像がキャッシュにはいる保証
はありません。画像キャッシュの制限値をすぎたり、タイムアウトすると画像読み込みを中断します。
画像は、storages引数に指定した物のうち、最初に書いた物ほどキャッシュに入る可能性が大きくなり
ます ( 優先されます )。すでに指定された画像がキャッシュに入っていた場合は、キャッシュ中での
生存の順位を引き上げるだけの動作をします。

このメソッドは、画像読み込み中のエラーはすべて無視します。

現バージョンでは、このメソッドでキャッシュに入れることのできる画像は、通常
[Layer.loadImages](Layer.md#loadimages) で読み込み可能な画像で、かつカラーキーを指定しない画像
です ( アルファチャンネル付き画像は問題ありません )。ユニバーサルトランジションのルール画像や、
領域画像は読み込む動作はしますが、キャッシュとして有効なデータにはなりません ( 読み込んだ
データは無駄になります ) ので、指定しないようにしてください。

画像がキャッシュで使用するバイト数については [System.graphicCacheLimit](System.md#graphiccachelimit) を参照
してください。

---

### showVersion

メソッド

**解説**

aboutダイアログを表示します。

---

### dumpHeap

メソッド

**解説**

ヒープの情報をコンソールに出力します。

---

### versionString

プロパティ / アクセス: `r`

**解説**

吉里吉里本体のバージョン文字列を得ることができます。

バージョン文字列は以下のような形式です。

`1.0.0.1`

---

### versionInformation

プロパティ / アクセス: `r`

**解説**

吉里吉里本体のバージョン情報文字列を得ることができます。

バージョン情報文字列は [System.versionString](System.md#versionstring) よりも長い形式で、

以下のようになります。

`吉里吉里[きりきり] Z 実行コア/1.0.0.0 (Compiled on Dec 16 2013 23:15:27) TJS2/2.4.28 Copyright (C) 1997-2013 W.Dee and contributors All rights reserved.`

---

### eventDisabled

プロパティ / アクセス: `r/w`

**解説**

吉里吉里の**イベント配信**が停止されている場合に true になります。値を設定することもで
きます。

イベント配信が停止されると、吉里吉里上のイベントは発生しなくなるか、発生が延期されま
す ( イベントの種類によって挙動は異なります )。

---

### graphicCacheLimit

プロパティ / アクセス: `r/w`

**解説**

吉里吉里の**画像キャッシュ制限**をバイト単位で表します。値を設定することもできます。

`**gcsAuto**` を指定すると、マシンに搭載されているメモリ量に応じて自動的に
値が設定されます。

ルール画像や領域画像は、幅×高さ で表されるバイト数を消費します。それ以外の画像は
幅×高さ×４ で表されるバイト数を消費します。

---

### platformName

プロパティ / アクセス: `r`

**解説**

吉里吉里が動作しているプラットフォーム名を表します。Windows の場合は OS が 32bit 版の時 'Win32' 、64bit 版の時  'Win64' となります。

1.3.0 以前の場合は、常に 'Win32' となります。

---

### osName

プロパティ / アクセス: `r`

**解説**

吉里吉里が動作している OS の名前を表します。

---

### exePath

プロパティ / アクセス: `r`

**解説**

吉里吉里本体が設置してあるパスを表します。パス名は統一ストレージ名で表現されます。

**関連:** [System.appDataPath](System.md#appdatapath) / [System.personalPath](System.md#personalpath)

---

### personalPath

プロパティ / アクセス: `r`

**解説**

ユーザのマイドキュメントのパスを表します。Windows の場合、レジストリの
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders の
Personal で表されるフォルダが返されます。通常これは「マイドキュメント」フォルダを指します。

このフォルダがない場合は [System.exePath](System.md#exepath) と同じフォルダを返します。

**関連:** [System.appDataPath](System.md#appdatapath) / [System.exePath](System.md#exepath)

---

### appDataPath

プロパティ / アクセス: `r`

**解説**

ユーザのホームディレクトリのパスを表します。Windows の場合、レジストリの
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders の
AppData で表されるフォルダが返されます。このフォルダがない場合は [System.exePath](System.md#exepath) と同じ
フォルダを返します。



これは、通常、以下の通りになります。

- **XP の場合**  
  `C:\Documents and Settings\<ユーザ名>\Application Data\` ( C: の部分は環境によって異なります )
- **Vista, 7, 8 の場合**  
  `C:\Users\<ユーザ名>\AppData\Roaming` ( C: の部分は環境によって異なります )
- **何らかの理由で レジストリキー ( 上記参照 ) を読み出せなかった場合**  
  吉里吉里の実行可能ファイルのあるフォルダ ([System.exePath](System.md#exepath))になります

**関連:** [System.exePath](System.md#exepath) / [System.personalPath](System.md#personalpath)

---

### dataPath

プロパティ / アクセス: `r`

**解説**

コマンドラインオプションの -datapath で指定したディレクトリを表します。

標準では、ログなどがすべてここに出力されます。

ユーザスクリプトがデータを保存する場合は、ここに保存することを推奨します。

---

### exeName

プロパティ / アクセス: `r`

**解説**

吉里吉里本体へのパス名を表します。パス名は統一ストレージ名で表現されます。

---

### title

プロパティ / アクセス: `r/w`

**解説**

メインウィンドウのタイトルを文字列で表します。値を設定することもできます。

**関連:** [Window.caption](Window.md#caption)

---

### screenWidth

プロパティ / アクセス: `r`

**解説**

画面サイズ ( 画面解像度 ) の横サイズをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### screenHeight

プロパティ / アクセス: `r`

**解説**

画面サイズ ( 画面解像度 ) の縦サイズをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopLeft

プロパティ / アクセス: `r`

**解説**

デスクトップ ( ウィンドウを表示可能な領域 ) の左端位置をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopTop

プロパティ / アクセス: `r`

**解説**

デスクトップ ( ウィンドウを表示可能な領域 ) の上端位置をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopWidth

プロパティ / アクセス: `r`

**解説**

デスクトップ ( ウィンドウを表示可能な領域 ) の幅をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopHeight](System.md#desktopheight)

---

### desktopHeight

プロパティ / アクセス: `r`

**解説**

デスクトップ ( ウィンドウを表示可能な領域 ) の高さをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth)

---

### exitOnWindowClose

プロパティ / アクセス: `r/w`

**解説**

メインウィンドウ(一番最初に作成したWindowクラスのインスタンス)が閉じたときに終了するかどうかを表します。値を設定することもできます。デフォルトは真です。

メインウィンドウが閉じ、ほかのデバッグ関連ウィンドウも表示していない場合は吉里吉里は終了すること無くシステムに残り、制御不能に陥る可能性がありますので注意してください(タスクマネージャからプロセスを終了させるしか無くなる可能性があります)。

---

### exceptionHandler

プロパティ / アクセス: `r/w`

**解説**

捕捉されなかった例外 (どこにも捕捉されずに吉里吉里本体に渡された例外) を処理する関数を表します。

null を指定すると、デフォルトの動作になります。

デフォルトの動作とは、

1. 非同期イベントの配信を停止する ([System.eventDisabled](System.md#eventdisabled) を 真 に設定)
2. ログをファイルに出力開始する ([Debug.logAsError](Debug.md#logaserror) を呼ぶ)
3. エラーを通知するダイアログボックスを表示し、スクリプトエディタでその箇所を示す

です。

ハンドラ関数は引数を一つ取り、それが例外オブジェクトになります。

ハンドラ関数が指定されないか、あるいはハンドラ関数が null であるか、あるいはハンドラ関数が偽を返すと、デフォルトの動作が行われます。

ハンドラ関数が真を返すと上記のデフォルトの動作は行われません。

ハンドラ関数を実行中に非同期イベントが発生する可能性を考慮してください。吉里吉里本体が非同期イベントを処理できてしまうと、例外ハンドラを実行中に再び予期せぬ例外が発生する可能性があります。これを避けるため、通常、ハンドラ関数内でなにかを待つような処理をする場合 (吉里吉里が非同期イベントを処理する機会がある場合 )、非同期イベントの発生を停止させます。

```
System.exceptionHandler = function (e)
{
	// どこにも捕捉されない例外がシステム側で捕捉された場合、この関数が
	// 呼ばれる。e は例外オブジェクト。
	if(e instanceof "ConductorException")
	{
		// コンダクタの投げた例外の場合
		Debug.logAsError(); // ログのファイルへの書き出し動作の開始など
		var event_disabled = System.eventDisabled;
		System.eventDisabled = true;
			// エラーの理由を表示させている間にイベントが発生すると
			// やっかいなのでいったんイベント発生を停止させる
		System.inform(e.message);
		System.eventDisabled = event_disabled;
			// イベントを発生するかどうかを元の状態に
		return true; // true を返すと本体側で例外の処理は行わなくなる
	}
	else
	{
		return false; // false を返すと通常の例外処理
	}
};
```

**関連:** [System.eventDisabled](System.md#eventdisabled) / [Debug.logAsError](Debug.md#logaserror)

---

### onActivate

プロパティ / アクセス: `r/w`

**解説**

アプリケーションがアクティブになったときに呼び出されるイベント関数を表します。

null を指定すると関数は呼び出されません。

通常のイベントハンドラと異なり、このイベントを受け取りたい場合は、呼び出したい関数をこのプロパティに設定してください。

[Window.onActivate](Window.md#onactivate) は、同じアプリケーション内のそれぞれのウィンドウがアクティブになったときに発生しますが、このイベントは、メインウィンドウがアクティブになった場合に発生します。

このイベントは、メインウィンドウが既にアクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [System.onDeactivate](System.md#ondeactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onDeactivate

プロパティ / アクセス: `r/w`

**解説**

アプリケーションが非アクティブになったときに呼び出されるイベント関数を表します。

null を指定すると関数は呼び出されません。

通常のイベントハンドラと異なり、このイベントを受け取りたい場合は、呼び出したい関数をこのプロパティに設定してください。

[Window.onDeactivate](Window.md#ondeactivate) は、同じアプリケーション内のそれぞれのウィンドウが非アクティブになったときに発生しますが、このイベントは、メインウィンドウが非アクティブになった場合に発生します。

このイベントは、メインウィンドウが既に非アクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [System.onActivate](System.md#onactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### drawThreadNum

プロパティ / アクセス: `r/w`

**解説**

吉里吉里のレイヤシステムが描画時に使用する**スレッド数**を表します。値を設定することもできます。

`**dtnAuto**` を指定すると、OSの認識するプロセッサ数と同数のスレッドが自動的に割り当てられます。

描画スレッドを複数設定することで、マルチコア環境での描画パフォーマンスを向上させられる可能性がありますが、逆にパフォーマンスが低下する場合もあります。

描画面積が大きい処理、Affine系の高負荷な処理、演算の重いレイヤ合成処理などに適用することで、良好な結果を得られる可能性があります。

マルチスレッドを使用するように設定しても、描画処理の負荷が軽くマルチスレッド化の効果が得られないとシステムが判断した場合は、マルチスレッドで実行されない場合があります。

---

### savedGamesPath

プロパティ / アクセス: `r`

**解説**

保存したゲームのパスを表します。



これは、通常、以下の通りになります。

C:\Users\<ユーザ名>\Saved Games

---

### exeBits

プロパティ / アクセス: `r`

**解説**

実行バイナリが 32bit 版か 64bit 版かを整数の 32 か 64 で表します。

**関連:** [System.osBits](System.md#osbits) / [System.platformName](System.md#platformname)

---

### osBits

プロパティ / アクセス: `r`

**解説**

OS が 32bit 版か 64bit 版かを整数の 32 か 64 で表します。

**関連:** [System.exeBits](System.md#exebits) / [System.platformName](System.md#platformname)

---
