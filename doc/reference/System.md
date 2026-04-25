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
- [exitOnNoWindowStartup](#exitonnowindowstartup)
- [isAndroid](#isandroid)
- [isGeneric](#isgeneric)
- [isWindows](#iswindows)
- [licenseText](#licensetext)
- [openGLESVersion](#openglesversion)
- [processorNum](#processornum)
- [touchDevice](#touchdevice)

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
- [addFont](#addfont)
- [clearGraphicCache](#cleargraphiccache)
- [getJoypadType](#getjoypadtype)
- [nullpo](#nullpo)
- [system](#system)

---

### versionString

プロパティ \ アクセス: `r`

**解説**

バージョン文字列

吉里吉里本体のバージョン文字列を得ることができます。

バージョン文字列は以下のような形式です。

`1.0.0.1`

---

### versionInformation

プロパティ \ アクセス: `r`

**解説**

バージョン情報文字列

吉里吉里本体のバージョン情報文字列を得ることができます。

バージョン情報文字列は [System.versionString](System.md#versionstring) よりも長い形式で、

以下のようになります。

`吉里吉里[きりきり] Z 実行コア/1.0.0.0 (Compiled on Dec 16 2013 23:15:27) TJS2/2.4.28 Copyright (C) 1997-2013 W.Dee and contributors All rights reserved.`

---

### eventDisabled

プロパティ \ アクセス: `r/w`

**解説**

イベント配信が停止されているかどうか

吉里吉里の**イベント配信**が停止されている場合に true になります。値を設定することもで
きます。

イベント配信が停止されると、吉里吉里上のイベントは発生しなくなるか、発生が延期されま
す ( イベントの種類によって挙動は異なります )。

---

### graphicCacheLimit

プロパティ \ アクセス: `r/w`

**解説**

画像キャッシュ制限

吉里吉里の**画像キャッシュ制限**をバイト単位で表します。値を設定することもできます。

`**gcsAuto**` を指定すると、マシンに搭載されているメモリ量に応じて自動的に
値が設定されます。

ルール画像や領域画像は、幅×高さ で表されるバイト数を消費します。それ以外の画像は
幅×高さ×４ で表されるバイト数を消費します。

---

### platformName

プロパティ \ アクセス: `r`

**解説**

プラットフォーム名

吉里吉里が動作しているプラットフォーム名を表します。Windows の場合は OS が 32bit 版の時 'Win32' 、64bit 版の時  'Win64' となります。

1.3.0 以前の場合は、常に 'Win32' となります。

---

### osName

プロパティ \ アクセス: `r`

**解説**

OS 名

吉里吉里が動作している OS の名前を表します。

---

### exePath

プロパティ \ アクセス: `r`

**解説**

吉里吉里本体のあるフォルダのパス

吉里吉里本体が設置してあるパスを表します。パス名は統一ストレージ名で表現されます。

**関連:** [System.appDataPath](System.md#appdatapath) / [System.personalPath](System.md#personalpath)

---

### personalPath

プロパティ \ アクセス: `r`

**解説**

マイドキュメントのパス

ユーザのマイドキュメントのパスを表します。Windows の場合、レジストリの
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders の
Personal で表されるフォルダが返されます。通常これは「マイドキュメント」フォルダを指します。

このフォルダがない場合は [System.exePath](System.md#exepath) と同じフォルダを返します。

**関連:** [System.appDataPath](System.md#appdatapath) / [System.exePath](System.md#exepath)

---

### appDataPath

プロパティ \ アクセス: `r`

**解説**

ユーザのホームディレクトリのパス

ユーザのホームディレクトリのパスを表します。Windows の場合、レジストリの
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders の
AppData で表されるフォルダが返されます。このフォルダがない場合は [System.exePath](System.md#exepath) と同じ
フォルダを返します。

これは、通常、以下の通りになります。

XP の場合
`C:\Documents and Settings\<ユーザ名>\Application Data\` ( C: の部分は環境によって異なります )
Vista, 7, 8 の場合
`C:\Users\<ユーザ名>\AppData\Roaming` ( C: の部分は環境によって異なります )
何らかの理由で レジストリキー ( 上記参照 ) を読み出せなかった場合
吉里吉里の実行可能ファイルのあるフォルダ ([System.exePath](System.md#exepath))になります

**関連:** [System.exePath](System.md#exepath) / [System.personalPath](System.md#personalpath)

---

### dataPath

プロパティ \ アクセス: `r`

**解説**

データ保存場所のパス

コマンドラインオプションの -datapath で指定したディレクトリを表します。

標準では、ログなどがすべてここに出力されます。

ユーザスクリプトがデータを保存する場合は、ここに保存することを推奨します。

---

### exeName

プロパティ \ アクセス: `r`

**解説**

吉里吉里本体のパス

吉里吉里本体へのパス名を表します。パス名は統一ストレージ名で表現されます。

---

### title

プロパティ \ アクセス: `r/w`

**解説**

タイトル

メインウィンドウのタイトルを文字列で表します。値を設定することもできます。

**関連:** [Window.caption](Window.md#caption)

---

### screenWidth

プロパティ \ アクセス: `r`

**解説**

画面幅

画面サイズ ( 画面解像度 ) の横サイズをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### screenHeight

プロパティ \ アクセス: `r`

**解説**

画面高さ

画面サイズ ( 画面解像度 ) の縦サイズをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopLeft

プロパティ \ アクセス: `r`

**解説**

デスクトップ左端位置

デスクトップ ( ウィンドウを表示可能な領域 ) の左端位置をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopTop

プロパティ \ アクセス: `r`

**解説**

デスクトップ上端位置

デスクトップ ( ウィンドウを表示可能な領域 ) の上端位置をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopWidth

プロパティ \ アクセス: `r`

**解説**

デスクトップ幅

デスクトップ ( ウィンドウを表示可能な領域 ) の幅をピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopHeight](System.md#desktopheight)

---

### desktopHeight

プロパティ \ アクセス: `r`

**解説**

デスクトップ高さ

デスクトップ ( ウィンドウを表示可能な領域 ) の高さをピクセル単位で表します。

値はメインウィンドウのあるディスプレイを対象としたものです。

メインウィンドウがない場合はプライマリーディスプレイが対象となります。

**関連:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth)

---

### exitOnWindowClose

プロパティ \ アクセス: `r/w`

**解説**

メインウィンドウが閉じたときに終了するかどうか

メインウィンドウ(一番最初に作成したWindowクラスのインスタンス)が閉じたときに終了するかどうかを表します。値を設定することもできます。デフォルトは真です。

メインウィンドウが閉じ、ほかのデバッグ関連ウィンドウも表示していない場合は吉里吉里は終了すること無くシステムに残り、制御不能に陥る可能性がありますので注意してください(タスクマネージャからプロセスを終了させるしか無くなる可能性があります)。

---

### exceptionHandler

プロパティ \ アクセス: `r/w`

**解説**

捕捉されなかった例外のためのハンドラ関数

捕捉されなかった例外 (どこにも捕捉されずに吉里吉里本体に渡された例外) を処理する関数を表します。

null を指定すると、デフォルトの動作になります。

デフォルトの動作とは、

- 非同期イベントの配信を停止する ([System.eventDisabled](System.md#eventdisabled) を 真 に設定)
- ログをファイルに出力開始する ([Debug.logAsError](Debug.md#logaserror) を呼ぶ)
- エラーを通知するダイアログボックスを表示し、スクリプトエディタでその箇所を示す

です。

ハンドラ関数は引数を一つ取り、それが例外オブジェクトになります。

ハンドラ関数が指定されないか、あるいはハンドラ関数が null であるか、あるいはハンドラ関数が偽を返すと、デフォルトの動作が行われます。

ハンドラ関数が真を返すと上記のデフォルトの動作は行われません。

ハンドラ関数を実行中に非同期イベントが発生する可能性を考慮してください。吉里吉里本体が非同期イベントを処理できてしまうと、例外ハンドラを実行中に再び予期せぬ例外が発生する可能性があります。これを避けるため、通常、ハンドラ関数内でなにかを待つような処理をする場合 (吉里吉里が非同期イベントを処理する機会がある場合 )、非同期イベントの発生を停止させます。

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

**関連:** [System.eventDisabled](System.md#eventdisabled) / [Debug.logAsError](Debug.md#logaserror)

---

### onActivate

プロパティ \ アクセス: `r/w`

**解説**

アプリケーションがアクティブになったとき

アプリケーションがアクティブになったときに呼び出されるイベント関数を表します。

null を指定すると関数は呼び出されません。

通常のイベントハンドラと異なり、このイベントを受け取りたい場合は、呼び出したい関数をこのプロパティに設定してください。

[Window.onActivate](Window.md#onactivate) は、同じアプリケーション内のそれぞれのウィンドウがアクティブになったときに発生しますが、このイベントは、メインウィンドウがアクティブになった場合に発生します。

このイベントは、メインウィンドウが既にアクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [System.onDeactivate](System.md#ondeactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onDeactivate

プロパティ \ アクセス: `r/w`

**解説**

アプリケーションが非アクティブになったとき

アプリケーションが非アクティブになったときに呼び出されるイベント関数を表します。

null を指定すると関数は呼び出されません。

通常のイベントハンドラと異なり、このイベントを受け取りたい場合は、呼び出したい関数をこのプロパティに設定してください。

[Window.onDeactivate](Window.md#ondeactivate) は、同じアプリケーション内のそれぞれのウィンドウが非アクティブになったときに発生しますが、このイベントは、メインウィンドウが非アクティブになった場合に発生します。

このイベントは、メインウィンドウが既に非アクティブの場合にも発生する可能性があるので注意してください (完全に onActivate → onDeactivate → onActivate → …… の順に発生する保証がない )。

**関連:** [System.onActivate](System.md#onactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### drawThreadNum

プロパティ \ アクセス: `r/w`

**解説**

描画に使用するスレッドの数

吉里吉里のレイヤシステムが描画時に使用する**スレッド数**を表します。値を設定することもできます。

`**dtnAuto**` を指定すると、OSの認識するプロセッサ数と同数のスレッドが自動的に割り当てられます。

描画スレッドを複数設定することで、マルチコア環境での描画パフォーマンスを向上させられる可能性がありますが、逆にパフォーマンスが低下する場合もあります。

描画面積が大きい処理、Affine系の高負荷な処理、演算の重いレイヤ合成処理などに適用することで、良好な結果を得られる可能性があります。

マルチスレッドを使用するように設定しても、描画処理の負荷が軽くマルチスレッド化の効果が得られないとシステムが判断した場合は、マルチスレッドで実行されない場合があります。

---

### savedGamesPath

プロパティ \ アクセス: `r`

**解説**

保存したゲームのパス(1.1.0以降)

保存したゲームのパスを表します。

これは、通常、以下の通りになります。

C:\Users\<ユーザ名>\Saved Games

---

### exeBits

プロパティ \ アクセス: `r`

**解説**

吉里吉里本体が 32bit 版か 64bit 版か(1.3.0以降)

実行バイナリが 32bit 版か 64bit 版かを整数の 32 か 64 で表します。

**関連:** [System.osBits](System.md#osbits) / [System.platformName](System.md#platformname)

---

### osBits

プロパティ \ アクセス: `r`

**解説**

OS が 32bit 版か 64bit 版か(1.3.0以降)

OS が 32bit 版か 64bit 版かを整数の 32 か 64 で表します。

**関連:** [System.exeBits](System.md#exebits) / [System.platformName](System.md#platformname)

---

### exitOnNoWindowStartup

プロパティ \ アクセス: `r/w`

**解説**

TODO: exitOnNoWindowStartup の説明

---

### isAndroid

プロパティ \ アクセス: `r/w`

**解説**

システムがAndroidかどうか判定[r]

---

### isGeneric

プロパティ \ アクセス: `r/w`

**解説**

TODO: isGeneric の説明

---

### isWindows

プロパティ \ アクセス: `r/w`

**解説**

システムがWindowsかどうか判定[r]

---

### licenseText

プロパティ \ アクセス: `r/w`

**解説**

TODO: licenseText の説明

---

### openGLESVersion

プロパティ \ アクセス: `r/w`

**解説**

OpenGL ES のバージョン

実際の値を100倍した数、つまり2.0なら200、3.0なら300が返ります。

---

### processorNum

プロパティ \ アクセス: `r/w`

**解説**

TODO: processorNum の説明

---

### touchDevice

プロパティ \ アクセス: `r/w`

**解説**

TODO: touchDevice の説明

---

### terminate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `0` | プロセスの終了コードを指定します |

**解説**

吉里吉里の非同期終了

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

吉里吉里の同期終了

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

Continuous ハンドラの追加

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

Continuous ハンドラの削除

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

メッセージの表示

ユーザにメッセージを示すためのウィンドウを表示します。

ウィンドウはモーダルで表示されます ( つまり、表示中は他のウィンドウは操作できない )。

---

### getTickCount

メソッド

**戻り値**

ティックカウント(64bitの整数)が戻ります。

**解説**

ティックカウントの取得

**ティックカウント**は 1/1000 秒ごとにカウントアップする数値です。二つの時点でこのメソッドを
用いてティックカウントを取得し、その差をとれば、二つの時点の時間差を知ることができます。

---

### getKeyState

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 状態を取得する**仮想キーコード**  を指定します。 |

**戻り値**

キーが押されていれば真、押されていなければ偽になります。

**解説**

キー状態の取得

code で指定したキーコードに対応するキーが、このメソッドを呼んだ時点で押されているかどうかを
取得します。

---

### shellExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 実行するファイルやソフトウェアを指定します。<br>ファイルを指定された場合は、それに関連づけられたプログラムが起動します。 |
| `param` | `""` | 実行するソフトウェアに渡すパラメータを指定します。<br>target 引数にファイルを指定した場合はこの引数を省略するか、あるいは空文字列を<br>指定してください。 |

**戻り値**

実行に成功すれば真、失敗すれば偽が返ります。

**解説**

ファイル/プログラムの実行

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

レジストリの読み込み

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
| `name` | `&nbsp;` | 取得するコマンドラインオプション名を指定します。最初に '-'<br>( ハイフン ) をつけてください ( 例 : `'-nosplash'` )。 |

**戻り値**

コマンドラインオプションが指定されていればその値、指定されていなければ
void が返ります。

**解説**

コマンドラインオプションの取得

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
| `name` | `&nbsp;` | 設定するコマンドラインオプション名を指定します。最初に '-'<br>( ハイフン ) をつけてください ( 例 : `'-contfreq'` )。 |
| `value` | `&nbsp;` | 設定する値を指定します。 ( 例 : `'60'` )。 |

**解説**

コマンドラインオプションの設定

動的に**コマンドラインオプション**を設定します。すべてのコマンドラインオプションが設定可能な訳ではありません。

設定可能なコマンドラインオプションについては [](CommandLine) を参照してください。ここで動的に変更可能という表記のないオプションについては変更を行わないでください。

このメソッドは、そのオプションが動的に変更可能かどうかやオプションの存在、値の有効性などをチェックしません。値の設定には十分気をつけてください。

**関連:** [System.getArgument](System.md#getargument)

---

### toActualColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 色定数を指定します ( [](ColorCodes) を参照 )。<br>通常の 0xRRGGBB 形式の色を指定した場合はそのままの値が返ります。 |

**戻り値**

指定された色定数が表す実際の色が 0xRRGGBB 形式で返ります。

**解説**

色定数の実際の色の取得

色定数を実際の色に変換し、0xRRGGBB 形式で返します。

---

### createAppLock

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | チェックを行うためのキー文字列を指定します。同じキー文字列をほかの<br>実行中の吉里吉里がこのメソッドに指定していた場合、false が戻ります。<br>キー文字列には基本的には TJS の変数の命名規則と同じ文字のみが使えると<br>考えてください。<br>キー文字列は十分にユニークな物である必要があります。 |

**戻り値**

すでに同じキー文字列が指定された吉里吉里が実行中の場合は false、そうでなければ true が戻ります。

**解説**

二重起動のチェック

他に同じキー文字列を指定された吉里吉里が実行中ならば false、そうでなければ true が戻ります。

二重起動の防止に用います。

---

### createUUID

メソッド

**戻り値**

生成された UUID 文字列が "e8b2a2b5-5ceb-4f75-a08b-1f1bdfdca4f1" の形式
(ハイフンを除く各英数字は16進数の数字) で戻ります。

**解説**

UUID 文字列の生成

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

メッセージ割り当ての変更

メッセージ割り当てを変更します。

吉里吉里が内蔵しているメッセージをこのメソッドで別のメッセージに変更することができます。

通常、メッセージマップファイル内に記述します ( [](Startup) 参照 )。

設定可能な ID と、それに現在割り当てられているメッセージの一覧を取得するには [](Controller) から
「メッセージマップファイルの作成」を実行してください。

---

### doCompact

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `level` | `clAll` | レベルを指定します。<br>**clIdle** を指定すると、システムがアイドル状態 (システムが比較的動作をしていない状態) に実行されるコンパクト化と同じ処理が行われます。現バージョンでは TJS2 のガベージコレクションが行われます。<br>**clDeactivate** を指定すると、吉里吉里が非アクティブになったとき (他のアプリケーションがアクティブになったとき) に実行されるコンパクト化と同じ処理が行われます。現バージョンではレイヤの演算用の一時画像バッファ、レイヤキャッシュ、XP3 アーカイブのセグメント(ストレージの断片) キャッシュ、自動検索パスのキャッシュがクリアされます。<br>**clMinimize** を指定すると、吉里吉里が最小化されたときに実行されるコンパクト化と同じ処理が行われます。現バージョンでは、描画文字のキャッシュ、画像キャッシュがクリアされます。<br>**clAll** を指定すると、上記のコンパクト化の全てが実行されます。<br>コンパクト化のレベルは、clIdle < clDeactivate < clMinimize < clAll の順に強くなります。より上位のレベルを指定すると、下位のレベルで行われるコンパクト化も行われます。たとえば、clDeactivate を実行すると、clIdle での処理も実行されます。<br>引数を省略すると clAll が指定された物と見なされます。 |

**解説**

メモリのコンパクト化

メモリのコンパクト化を行います。コンパクト化とは、使用していないメモリや各種キャッシュ用メモリを解放して、メモリ使用量を減らす処理です。

吉里吉里は自動でこれを行うので通常はあまり気にする必要はありませんが、強制的にプログラム側の処理で行いたい場合にこのメソッドを使用することができます。

---

### touchImages

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storages` | `&nbsp;` | キャッシュに入れたい画像ストレージ名を配列(Arrayクラスのオブジェクト)で渡します。<br>先に書いた物ほど優先されます。<br>吉里吉里は、[Layer.loadImages](Layer.md#loadimages) の第１引数に指定された<br>文字列をそのままキーにしてキャッシュを管理するため、<br>キャッシュを意味のある物にするには、<br>ここで指定する画像ストレージ名は Layer.loadImages の第１引数に指定するものと<br>同一である必要があります。 |
| `limitbytes` | `0` | このメソッドの呼び出しで使用するキャッシュ容量の制限値をバイト単位で指定します。<br>0 を指定すると、キャッシュをすべて使用します。<br>正の数を指定すると、そのバイト数までキャッシュを使用しようとします。<br>負の数を指定すると、現在のキャッシュの<br>制限値 ( [System.graphicCacheLimit](System.md#graphiccachelimit) ) からその数値が加算された数 ( ただし<br>「負の数」を加算するので実際は減算 ) が制限値として使用されます。その結果制限値が<br>0 または負になってしまった場合は、このメソッドは何もせずに終了します。たとえば、<br>-2*1024*1024 を指定すれば、現在のキャッシュ制限値から 2MB が引かれた数値が指定さ<br>れたとみなされます。これは、キャッシュの残り容量に余裕を残したい場合に便利です。 |
| `timeout` | `0` | タイムアウト ( 時間制限 ) を ms 単位で指定します。0 を指定すると無制限と<br>なります。<br>このメソッドはこの引数で指定された時間が経過すると、以降の画像の読み込みを中止し、<br>戻ります。ただし、ある画像の読み込み中にタイムアウトになっても、その画像の読み<br>込みが終了するまでは戻りません。 |

**解説**

画像のキャッシュへの読み込み

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

aboutダイアログの表示(1.1.0以降)

aboutダイアログを表示します。

---

### dumpHeap

メソッド

**解説**

ヒープ情報ダンプ(1.1.0以降)

ヒープの情報をコンソールに出力します。

---

### addFont

メソッド

**解説**

TODO: addFont の説明

---

### clearGraphicCache

メソッド

**解説**

TODO: clearGraphicCache の説明

---

### getJoypadType

メソッド

**解説**

TODO: getJoypadType の説明

---

### nullpo

メソッド

**解説**

nullポインターアクセスを発生させます

呼ばないでください。

---

### system

メソッド

**解説**

TODO: system の説明

---

## プラグイン拡張: process

### メンバー一覧

#### メソッド

- [commandExecute](#commandexecute)

---

### commandExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` |  |
| `param` | `&nbsp;` |  |
| `timeout` | `0` |  |

---

## プラグイン拡張: shellExecute

### メンバー一覧

#### メソッド

- [commandExecute](#commandexecute)

---

### commandExecute

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `target` | `&nbsp;` | プログラム |
| `param` | `&nbsp;` | 引数 |
| `timeout` | `0` | タイムアウト時間(ms) |

**戻り値**

%[
status:   ok/error/timeoutのいずれかの文字列,
stdout:   コンソール出力文字列配列(改行で分離)
exitcode: 終了コード(status=="ok"時のみ),
message:  エラーメッセージ(status!="ok"時のみ)
];

**解説**

コンソール出力取得つきコマンドラインプログラムの実行

バックグラウンド処理はありません。実行対象のプログラムが終了するまで吉里吉里が停止します。

---

## プラグイン拡張: stdio

System クラスへの標準入出力拡張

### メンバー一覧

#### プロパティ

- [stdioState](#stdiostate)

#### メソッド

- [attachConsole](#attachconsole)
- [allocConsole](#allocconsole)
- [freeConsole](#freeconsole)
- [stdin](#stdin)
- [stdout](#stdout)
- [stderr](#stderr)
- [flush](#flush)

---

### stdioState

プロパティ \ アクセス: `r/w`

**解説**

標準入出力との接続状態を返す

---

### attachConsole

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bind` | `0` | 0:未接続の部分だけ接続 それ以外:指定した部分を強制接続<br>標準入力:0x01 標準出力:0x02 標準エラー出力:0x04 の論理和 |

**戻り値**

成功したかどうか

**解説**

標準入出力を既存のコンソールと接続する

---

### allocConsole

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `bind` | `0` | 0:未接続の部分だけ接続 それ以外:指定した部分を強制接続<br>標準入力:0x01 標準出力:0x02 標準エラー出力:0x04 の論理和 |

**戻り値**

成功したかどうか

**解説**

標準入出力をコンソールを作成して接続する

---

### freeConsole

メソッド

**戻り値**

成功したかどうか

**解説**

コンソールから切り離す

---

### stdin

メソッド

**戻り値**

入力されたテキスト

**解説**

標準入力からテキストを入力する。入力はブロッキングします。

---

### stdout

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `string` | `&nbsp;` | 出力するメッセージ |

**解説**

標準出力に文字列を出力

---

### stderr

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `string` | `&nbsp;` | 出力するメッセージ |

**解説**

標準エラー出力に文字列を出力

---

### flush

メソッド

**解説**

標準出力をフラッシュする

---

## プラグイン拡張: systemEx

擬似コードによるマニュアル

### メンバー一覧

#### メソッド

- [writeRegValue](#writeregvalue)
- [readEnvValue](#readenvvalue)
- [writeEnvValue](#writeenvvalue)
- [expandEnvString](#expandenvstring)
- [urlencode](#urlencode)
- [urldecode](#urldecode)
- [getAboutString](#getaboutstring)
- [confirm](#confirm)
- [waitForAppLock](#waitforapplock)
- [setDpiAwareness](#setdpiawareness)
- [getOSVersion](#getosversion)
- [getKnownFolderPath](#getknownfolderpath)
- [processApplicationMessages](#processapplicationmessages)
- [handleApplicationMessage](#handleapplicationmessage)
- [setDefaultDllDirectories](#setdefaultdlldirectories)
- [addDllDirectory](#adddlldirectory)
- [removeDllDirectory](#removedlldirectory)

---

### writeRegValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 書き込み先のキー(readRegValue と同様に HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\hoeg\\installdir と指定する) |
| `value` | `&nbsp;` | 書き込む値(文字列又は整数値) |

**解説**

レジストリにデータを書き込みます

---

### readEnvValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 環境変数名 |

**戻り値**

環境変数値（未定義の場合はvoid）

**解説**

環境変数を取得

---

### writeEnvValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 環境変数名 |
| `value` | `&nbsp;` | 設定する値 |

**戻り値**

元の環境変数値（未定義の場合はvoid）

**解説**

環境変数を設定

---

### expandEnvString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 展開する文字列 |

**戻り値**

展開後文字列

**解説**

文字列内の「%～%」を環境変数で展開

---

### urlencode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 元文字列 |
| `utf8` | `true` | UTF8で出力する場合はtrue |

**戻り値**

URLEncodeされた文字列

**解説**

URLEncode処理を行う

---

### urldecode

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 元文字列 |
| `utf8` | `true` | UTF8として処理する場合はtrue |

**戻り値**

URLDecodeされた文字列

**解説**

URLDecode処理を行う

---

### getAboutString

メソッド

**戻り値**

テキスト(TVPGetAboutString)

**解説**

Ctrl+F12で表示される環境情報テキストを取得する

---

### confirm

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 表示するメッセージ |
| `caption` | `""` | ウインドウのキャプション文字列 |
| `window` | `void` | 指定があった場合はそのウインドウを親として表示します |

**戻り値**

YESがおされたら true

**解説**

確認用メッセージ窓を表示します。ウインドウはモーダルで表示されます。

---

### waitForAppLock

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `key` | `&nbsp;` | AppLockのキー文字列 |
| `timeout` | `0` | タイムアウト待ち時間(ms) |

**戻り値**

true:正常終了(AppLockは存在しないもしくはタイムアウト時間内に消えた),  false:タイムアウトした, (void:エラー)

※この関数の後に再度同じキーでcreateAppLockを呼ぶ必要はありません（すでに所有権があるため失敗する）

**解説**

他プロセスのSystem.createAppLockで作成されたMutexがリリースされるのを待ち所有権を取得する

---

### setDpiAwareness

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `context` | `&nbsp;` | : コンテキスト値（-1～-5）<br>DPI_AWARENESS_CONTEXT_UNAWARE              : -1<br>DPI_AWARENESS_CONTEXT_SYSTEM_AWARE         : -2<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE    : -3<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 : -4 (Creators Update or later)<br>DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED    : -5 (October 2018 update or later) |

**戻り値**

前の値(※設定できなかった場合は0)

**解説**

DPI Awarenessを設定する

Windows10 Redstone1 (ver 1607) 以降にて有効

---

### getOSVersion

メソッド

**戻り値**

void or %[ major, minor, build, platform, spmajor, spminor, servevicepack, suite, type ];

**解説**

OSのバージョン情報詳細を取得

RtlGetVersion API および RTL_OSVERSIONINFOW 構造体を参照のこと

---

### getKnownFolderPath

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `folderid` | `&nbsp;` | 取得したいFOLDERID (String or GUID-octet) |
| `flags` | `0` | KF_FLAG_* 値（KF_FLAG_CREATE = 0x00008000 等） |

**戻り値**

結果のローカルパス文字 or ""(不明) or void(失敗)

**解説**

SHGetKnownFolderPath ラッパー

FOLDERIDが文字列の場合は FOLDERID_{} の {} 部分の文字列を指定。GUIDは <% 00000000 0000 0000 0000 0000000000000 %> の 16byte octet を指定
この関数独自の特殊指定として folderid に "Captures" が指定可能（GameBarのキャプチャフォルダ[Video\Captures] : GUID {EDC0FE71-98D8-4F4A-B920-C8DC133CB165} 指定と同等の動作）

---

### processApplicationMessages

メソッド

**解説**

TVPProcessApplicationMessages(), TVPHandleApplicationMessage() 呼び出し

メッセージの処理（※System.breathe()と違い吉里吉里のイベントも処理される）
基本的にprocessApplicationMessagesはアプリが終了するまで返らないので注意
[TODO] イベントでの例外発生時はどうなるか確認

---

### handleApplicationMessage

メソッド

---

### setDefaultDllDirectories

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `flags` | `&nbsp;` | lls*フラグ組み合わせ |

**戻り値**

成功したらtrue

**解説**

::SetDefaultDllDirectoriesラッパー

---

### addDllDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 追加するローカルパス（※Storages.getLocalNameしておくこと） |

**戻り値**

removeDllDirectoryに渡す用の固有値（0だった場合は失敗）
setDefaultDllDirectoriesでllsUserDirsフラグを立てておくこと

**解説**

::AddDllDirectoryラッパー

---

### removeDllDirectory

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `cookie` | `&nbsp;` | 削除するaddDllPath固有値 |

**戻り値**

成功したらtrue

**解説**

::RemoveDllDirectoryラッパー

---

## プラグイン拡張: tftSave

システム拡張

### メンバー一覧

#### メソッド

- [savePreRenderedFont](#saveprerenderedfont)
- [loadPreRenderedFont](#loadprerenderedfont)
- [modifyPreRenderedFont](#modifyprerenderedfont)

---

### savePreRenderedFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 保存するファイル名 |
| `characters` | `&nbsp;` | 保存する文字（キャラクタコード）の入った配列 |
| `callback` | `&nbsp;` | 情報とイメージを取得するコールバック<br>キャラクタコードを引数に取り，レイヤ(PreRenderedFontImage)を返す関数であること<br>function(ch) { return layer; } |

**解説**

レンダリング済みフォントデータをファイルに保存する

---

### loadPreRenderedFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 読み込みファイル名 |
| `characters` | `&nbsp;` | 一覧の文字を受け取るための配列 |
| `callback` | `&nbsp;` | 将来的に画像イメージを受け取るコールバックが実装される予定(現状では必ずvoidを渡すこと） |

**解説**

レンダリング済みフォントデータをファイルから読み込む

---

### modifyPreRenderedFont

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 読み込みファイル名 |
| `callback` | `&nbsp;` | 情報取得・更新用コールバック<br>function(ch, info = %[ blackbox_x\|y, origin_x\|y, inc_x\|y, inc ]) { return true_if_modofied; } |

**解説**

レンダリング済みフォントデータのグリフ情報を更新する(変更できるのはorigin_x|y, inc_x|y, incのみ/blackboxは固定)

---

## プラグイン拡張: windowEx

System拡張

### メンバー一覧

#### メソッド

- [getDisplayMonitors](#getdisplaymonitors)
- [getDisplayMonitors](#getdisplaymonitors)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [setDpiAwareness](#setdpiawareness)
- [setCursorPos](#setcursorpos)
- [getCursorPos](#getcursorpos)
- [setClipCursor](#setclipcursor)
- [getSystemMetrics](#getsystemmetrics)
- [getDoubleClickTime](#getdoubleclicktime)
- [readEnvValue](#readenvvalue)
- [expandEnvString](#expandenvstring)
- [setApplicationIcon](#setapplicationicon)
- [setIconicPreview](#seticonicpreview)
- [breathe](#breathe)
- [isBreathing](#isbreathing)
- [findWindowEx](#findwindowex)
- [classLongPtr](#classlongptr)
- [loadCursor](#loadcursor)
- [mapVirtualKey](#mapvirtualkey)

---

### getDisplayMonitors

メソッド

**戻り値**

[ %[ name, primary, monitor:%[ x, y, w, h ], work:%[ x,y,w,h ], intersect:%[ x,y,w,h ] ], ... ];
name:      モニタの名前('\\.\DISPLAY?' 等)
primary:   プライマリモニタかどうか
monitor:   モニタの範囲辞書
work:      モニタのワークエリア範囲(ウィンドウを最大化したときなどの表示範囲)
intersect: 指定範囲と交わる領域(指定しなかった場合は monitor と同じ)

**解説**

モニタの情報一覧を取得

全てのモニタを列挙する

---

### getDisplayMonitors

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

指定範囲に交わるモニタのみ列挙する

---

### getMonitorInfo

メソッド

**戻り値**

%[ name, primary, monitor:%[ x, y, w, h ], work:%[ x, y, w, h ] ];
モニタの情報。辞書内容は getDisplayMonitors と同じ (ただし intersect 情報は無い)。
near=false 時でモニタが無い場合は void を返す。

**解説**

モニタ情報を取得

プライマリモニタを返す

---

### getMonitorInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**解説**

指定座標の位置のモニタを返す

---

### getMonitorInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**解説**

指定座標の範囲にもっとも多く交わるモニタを返す

---

### getMonitorInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `window` | `&nbsp;` |  |

**解説**

指定ウィンドウの範囲にもっとも多く交わるモニタを返す

---

### setDpiAwareness

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `context` | `&nbsp;` |  |

**解説**

SetThreadDpiAwarenessContext を呼び出す

---

### setCursorPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**戻り値**

get時：%[ x, y ] または void(取得失敗時)

**解説**

マウスカーソルのスクリーン座標を設定・取得

---

### getCursorPos

メソッド

---

### setClipCursor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `win_or_rect` | `&nbsp;` |  |

**解説**

カーソル位置クリップ処理

---

### getSystemMetrics

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `index` | `&nbsp;` | SM_* の「*」部分の文字列（ただし大文字小文字は無関係） |

**戻り値**

メトリクス値（indexにより内容が異なる）

**解説**

システムメトリクス情報を取得

詳細は GetSystemMetrics() API のマニュアルを参照
SW_ARRANGE は ARW_* の定義がないので直接数値指定で比較すること

---

### getDoubleClickTime

メソッド

**戻り値**

時間(ms) 既定値は500ms

**解説**

システムのダブルクリック許容時間を取得

詳細は GetDoubleClickTime() API のマニュアルを参照
ダブルクリックの許容移動範囲はgetSystemMetricsのCXDOUBLECLK/CYDOUBLECLKで取得可能
Layer.onDoubleClickを使わずにソフトウェアで擬似的にダブルクリック判定を行う場合に使用（時間決め打ちでも問題ないけど一応…）

---

### readEnvValue

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 環境変数名 |

**戻り値**

環境変数値（未定義の場合はvoid）

**解説**

環境変数を取得

---

### expandEnvString

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 展開する文字列 |

**戻り値**

展開後文字列

**解説**

文字列内の「%～%」を環境変数で展開

---

### setApplicationIcon

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `file` | `&nbsp;` | アイコンファイルまたはvoid (voidか""で初期状態にリセット） |

**解説**

タスクバーやALT+TABなどで表示されるアプリケーションアイコンを変更する

※ アーカイブ内のファイル指定は不可，exeやDLLを指定した場合は一番最初のアイコンが設定される

---

### setIconicPreview

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `iconic` | `&nbsp;` | trueならサムネイルの代わりにアイコンを表示する／falseなら設定解除 |

**戻り値**

成功したかどうか（XP以前では常に失敗）

**解説**

Vista以降のタスクバーやAlt+TABでのサムネイル表示を強制的にアプリケーションアイコン表示にする

※ アプリケーションウィンドウに DWMWA_FORCE_ICONIC_REPRESENTATION が設定される

---

### breathe

メソッド

**解説**

TVPBreathe, TVPGetBreathing のラッパ

---

### isBreathing

メソッド

---

### findWindowEx

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `winname` | `void` | ウインドウ名 |
| `clsname` | `void` | クラス名 |
| `parwin` | `void` | 親ウインドウ（Windowクラス指定かHWND数値） |
| `childafter` | `void` | 検索開始位置ウインドウ（〃） |

**戻り値**

成功した場合はHWND数値

**解説**

findWindoeEx のラッパ

---

### classLongPtr

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `win` | `&nbsp;` | 対象ウインドウ（Windowクラス指定かHWND数値） |
| `key` | `&nbsp;` | 対象インデックス 現状の実装では {cursor,icon,iconsm,brbackground} の文字列いずれか |
| `setvalue_or_getasvoid` | `void` | 取得する場合はvoid, 数値指定の場合はset （ただし key=brbackground の場合は {black,white,gray,ltgray,dkgray} のStockブラシを指定可） |

**戻り値**

成功した場合は現在（もしくは直前）のLONG_PTR数値／失敗時はvoid

**解説**

{Get,Set}ClassLongPtr のラッパ

---

### loadCursor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `idc_or_res` | `&nbsp;` | 数値>=0の場合はMAKEINTRESOURCE, 数値<0の場合はcrXXXX，文字列の場合はリソース名 |
| `hmodule` | `void` | リソース対象のHMODULE値 |

**戻り値**

HCURSOR数値

**解説**

LoadCursorのラッパ

---

### mapVirtualKey

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 仮想キーコードもしくはスキャンコード |
| `maptype` | `&nbsp;` | MAPVK_*値 |

**戻り値**

keycode

**解説**

MapVirtualKeyのラッパ

---
