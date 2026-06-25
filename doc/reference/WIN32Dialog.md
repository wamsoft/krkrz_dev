# WIN32Dialog

Windows ネイティブダイアログを操作するためのクラスです。
APIのラッパ程度の機能しかないので非常に使いにくいですが，
後述のtjsで記述された WIN32DialogEX を使うと幸せになれます。

## メンバー一覧

### コンストラクタ

- [WIN32Dialog](#win32dialog)

### プロパティ

- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [modeless](#modeless)
- [HWND](#hwnd)
- [icon](#icon)
- [isValid](#isvalid)
- [propsheet](#propsheet)
- [progress](#progress)
- [progressValue](#progressvalue)
- [progressCanceled](#progresscanceled)

### メソッド

- [loadResource](#loadresource)
- [makeTemplate](#maketemplate)
- [open](#open)
- [close](#close)
- [getItem](#getitem)
- [getItemID](#getitemid)
- [getItemClassName](#getitemclassname)
- [setItemInt](#setitemint)
- [getItemInt](#getitemint)
- [setItemText](#setitemtext)
- [getItemText](#getitemtext)
- [setItemEnabled](#setitemenabled)
- [getItemEnabled](#getitemenabled)
- [setItemFocus](#setitemfocus)
- [setItemPos](#setitempos)
- [setItemSize](#setitemsize)
- [getItemLeft](#getitemleft)
- [getItemTop](#getitemtop)
- [getItemWidth](#getitemwidth)
- [getItemHeight](#getitemheight)
- [setItemBitmap](#setitembitmap)
- [sendItemMessage](#senditemmessage)
- [getBaseUnits](#getbaseunits)
- [mapRect](#maprect)
- [invalidateRect](#invalidaterect)
- [setPos](#setpos)
- [setSize](#setsize)
- [setActive](#setactive)
- [onInit](#oninit)
- [onCommand](#oncommand)
- [onHScroll](#onhscroll)
- [onVScroll](#onvscroll)
- [onNotify](#onnotify)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [messageBox](#messagebox)
- [chooseColor](#choosecolor)
- [show](#show)
- [InitCommonControls](#initcommoncontrols)
- [InitCommonControlsEx](#initcommoncontrolsex)
- [openPropertySheet](#openpropertysheet)
- [propSheetMessage](#propsheetmessage)
- [setMessageResult](#setmessageresult)
- [openProgress](#openprogress)
- [closeProgress](#closeprogress)
- [insertTab](#inserttab)
- [deleteTab](#deletetab)
- [deleteAllTab](#deletealltab)
- [getCurSel](#getcursel)
- [selectTab](#selecttab)
- [setScrollInfo](#setscrollinfo)
- [getScrollInfo](#getscrollinfo)

---

### WIN32Dialog

コンストラクタ

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `owner` | `&nbsp;` | イベントコールバック用のオーナーを設定。nullかthisで自分自身へ送る。 |

**解説**

コンストラクタ

---

### left

プロパティ \ アクセス: `r`

**解説**

ダイアログサイズの取得

読み取り専用。サイズの変更はできないので注意

---

### top

プロパティ \ アクセス: `r`

---

### width

プロパティ \ アクセス: `r`

---

### height

プロパティ \ アクセス: `r`

---

### modeless

プロパティ \ アクセス: `r/w`

**解説**

モードレスダイアログ用のフラグ

trueならばモードレス状態でダイアログを開きます。
モードレスではダイアログのstyleにWS_VISIBLEを指定しない場合は
open()時に自動で表示されないので注意してください。

---

### HWND

プロパティ \ アクセス: `r`

**解説**

ダイアログのウィンドウハンドル

---

### icon

プロパティ \ アクセス: `r/w`

**解説**

ダイアログのアイコン画像

WIN32Dialog.Bitmapクラスのインスタンス:その画像
null:実行ファイルのアイコン
void:アイコンなし

---

### isValid

プロパティ \ アクセス: `r`

**解説**

ダイアログを open しているかどうか

---

### propsheet

プロパティ \ アクセス: `r`

**解説**

プロパティシートとして表示中かどうか

---

### progress

プロパティ \ アクセス: `r`

**解説**

プログレス状態かどうか

---

### progressValue

プロパティ \ アクセス: `r/w`

**解説**

プログレスバーを更新する（0-100の数値 or 負数の場合マーキー状態の速度）

---

### progressCanceled

プロパティ \ アクセス: `r/w`

**解説**

プログレスがキャンセルされたかどうか（※対象ボタンはIDCANCEL固定）

---

### loadResource

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | dllファイル（ローカルストレージ形式） |
| `resource` | `&nbsp;` | ダイアログリソース名 |

**解説**

ダイアログリソースを読み込む

---

### makeTemplate

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `header` | `&nbsp;` | ダイアログテンプレートヘッダ  （WIN32Dialog.Headerクラスのインスタンスであること） |
| `items*` | `&nbsp;` | ダイアログテンプレートアイテム（WIN32Dialog.Items クラスのインスタンスであること） |

**解説**

ダイアログテンプレートを生成する

---

### open

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 親ウィンドウ(吉里吉里の Window クラス)，省略時またはvoid時は親なし |

**解説**

ダイアログを開く

あらかじめ makeTemplate でダイアログテンプレートが生成されているか
または loadResource でダイアログリソースの読み込んでいること
makeTemplate より loadResource のデータ優先されるので注意

---

### close

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `result` | `&nbsp;` | EndDialog APIに渡す結果値 |

**解説**

ダイアログを閉じる

---

### getItem

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |

**戻り値**

ダイアログアイテムのHWND

**解説**

GetDlgItem のラッパー

---

### getItemID

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | ダイアログアイテムのHWND |

**戻り値**

ダイアログアイテムのID

**解説**

GetDlgCtrlID のラッパー

---

### getItemClassName

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |

**戻り値**

ダイアログアイテムのクラス名

**解説**

GetClassName のラッパー

---

### setItemInt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |
| `value` | `&nbsp;` | 設定する値（setの場合のみ） |

**戻り値**

取得結果（getの場合のみ）

**解説**

Get/SetDlgItemInt/Text のラッパー

---

### getItemInt

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getItemText

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemEnabled

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |
| `value` | `&nbsp;` | 有効・無効の設定（setの場合のみ） |

**戻り値**

取得結果（getの場合のみ）

**解説**

アイテムの有効・無効を設定・取得する

---

### getItemEnabled

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemFocus

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |

**解説**

アイテムにフォーカスを設定する

---

### setItemPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |
| `x` | `&nbsp;` | ダイアログアイテムのX座標 |
| `y` | `&nbsp;` | ダイアログアイテムのY座標 |

**解説**

アイテムの位置・大きさを変更・取得する

---

### setItemSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### getItemLeft

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemTop

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemWidth

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemHeight

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemBitmap

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |
| `bmp` | `&nbsp;` | ビットマップに設定するWIN32Dialog.Bitmapのインスタンス<br>WIN32DialogEXではLayerインスタンスが指定可能 |

**解説**

アイテムにBitmapを設定する

---

### sendItemMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | ダイアログアイテムのID |
| `msg` | `&nbsp;` | 送るメッセージ |
| `wparam` | `&nbsp;` | 送るwparam |
| `lparam` | `&nbsp;` | 送るlparam |

**戻り値**

LRESULT

**解説**

SendDlgItemMessage のラッパー

---

### getBaseUnits

メソッド

**戻り値**

結果辞書(%[ h:水平単位, v:垂直単位 ])

**解説**

GetDialogBaseUnit のラッパー

---

### mapRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 矩形領域辞書配列(%[ left, top, right, bottom ]) |

**戻り値**

結果辞書配列(%[ left, top, right, bottom ])

**解説**

MapDialogRect のラッパー

---

### invalidateRect

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 矩形領域辞書配列(%[ left, top, right, bottom ]) |
| `erase` | `&nbsp;` | 消去するかどうかフラグ |

**戻り値**

成功ならtrue

**解説**

InvalidateRect のラッパー

---

### setPos

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `x` | `&nbsp;` | x座標 |
| `y` | `&nbsp;` | y座標<br>ダイアログ表示中以外はエラーになるので注意。onInitなどにて座標を変更すること |

**解説**

ダイアログ座標を設定

---

### setSize

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `w` | `&nbsp;` | width |
| `h` | `&nbsp;` | height<br>ダイアログ表示中以外はエラーになるので注意。 |

**解説**

ダイアログの大きさを設定

---

### setActive

メソッド

**解説**

ダイアログをアクティブにする

このメソッドを追加する前のバージョンでは setPos/setSize でアクティブ化していた問題があったので留意のこと（現在はアクティブ化しない）

---

### onInit

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc のメッセージ == WM_INITDIALOG |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_INITDIALOG のコールバック

コールバックはownerに対して呼ばれるので注意してください
owner.onInitが未定義なら何もしません。

---

### onCommand

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc のメッセージ == WM_COMMAND |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_COMMAND のコールバック

コールバックはownerに対して呼ばれるので注意してください。
owner.onCommandが未定義なら何もしません。

---

### onHScroll

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc のメッセージ == WM_HSCROLL |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_HSCROLL のコールバック

---

### onVScroll

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc のメッセージ == WM_VSCROLL |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_VSCROLL のコールバック

---

### onNotify

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` |  |

**解説**

WM_NOTIFY のコールバック

---

### onKeyDown

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_KEYDOWN のコールバック

---

### onKeyUp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc のWPARAM |
| `lparam` | `&nbsp;` | DlgProc のLPARAM |

**解説**

WM_KEYUP のコールバック

---

### messageBox

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | オーナーwindow（指定しない場合はnullを渡すこと） |
| `text` | `&nbsp;` | メッセージテキスト |
| `caption` | `&nbsp;` | ダイアログボックスのキャプション |
| `type` | `&nbsp;` | 表示するボタンやアイコンのフラグの組み合わせ |

**戻り値**

押されたボタンのID
type に独自フラグ MB_OWNER_CENTER を設定するとオーナーウィンドウの中央に表示しようとする
（ただしダイアログが画面外になる場合はデスクトップの中央になる）

**解説**

MessageBox のラッパー

---

### chooseColor

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | オーナーwindow（指定しない場合はnullを渡すこと） |
| `elm` | `&nbsp;` | オプション（辞書または省略可能）<br>%[ color:初期選択色, palette:[ パレット色1, ... , パレット色16 ],<br>disableCustomColor:色の作成を無効にする, openCustomColor:色作成を最初から開いた状態にする ] |

**戻り値**

選択された色(0xRRGGBB) キャンセル時はvoid
elm.palette が渡された場合は，その内容も更新される

**解説**

ChooseColor のラッパー

---

### show

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `nCmdShow` | `&nbsp;` | SW_*フラグ |

**解説**

ShowWindow のラッパー

主にモードレスダイアログ用です。

---

### InitCommonControls

メソッド

**戻り値**

成功したか(〜Exのみ)

**解説**

InitCommonControls, InitCommonControlsEx のラッパー

---

### InitCommonControlsEx

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `icc` | `&nbsp;` |  |

---

### openPropertySheet

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `window` | `&nbsp;` | オーナーwindow（指定しない場合はnullを渡すこと） |
| `sheets` | `&nbsp;` | シート情報（WIN32Dialogインスタンスの配列） |
| `elm` | `&nbsp;` | オプション（辞書または省略可能）<br>%[ caption:プロパティシートタイトル, page:初期ページ番号, icon:アイコン ] |

**戻り値**

::PropertySheetの返り値

**解説**

プロパティシートを表示する（常にモーダル：モードレスは未実装）

---

### propSheetMessage

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` |  |
| `lparam` | `&nbsp;` |  |

**解説**

PSM_* メッセージをプロパティシートウィンドウに送信する

---

### setMessageResult

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**解説**

DWL_MSGRESULTの値を設定する

---

### openProgress

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | プログレスバーのダイアログアイテムID（progressValueプロパティで更新される対象） |
| `window` | `&nbsp;` | [optional] オーナーwindow (void=オーナーなし,null=Application) |
| `dsapp` | `(typeof window!="Object")` | [optional] プログレス表示中はアプリケーションウィンドウを無効にするか |
| `breathe` | `(typeof window=="Object")` | [optional] progressValueのsetterでbreatheするかどうか |
| `activate` | `true` |  |

**戻り値**

成功したらtrue

**解説**

プログレスダイアログを表示する

プログレスダイアログのstyleにはWS_VISIBLEを指定しないこと
閉じるときは必ず closeProgress() を使用すること
プログレス表示の場合，onInit以外のコールバックは来ないので注意

---

### closeProgress

メソッド

**解説**

プログレスダイアログを閉じる

---

### insertTab

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |
| `label` | `&nbsp;` |  |

**解説**

タブコントロールを利用する.

利用手順を検討中
insertTab(IDC_TAB, 0, "基本"); // タブを追加
// deleteTab(IDC_TAB, 0); // タブを削除
// deleteAllTab(IDC_TAB); // タブをすべて削除
var dlg = new WIN32Dialog(); dlg.loadResource("resource.dll", "INNER"); // Border=None, Style=Child にしたダイアログ
selectTab(IDC_TAB, dlg); // 表示
insertTab(IDC_TAB, 1, "拡張");
var dlg2 = new WIN32Dialog(); dlg2.loadResource("resource.dll", "INNER2");
dlg.show(SW_HIDE);
selectTab(IDC_TAB, dlg2); // 切り替え
// onNotify で notify->code == TCN_SELCHANGE かつ notify->idFrom == IDC_TAB の場合にユーザーによるタブの切り替え
// getCurSel(tab_id) でタブの番号を取得し、対応するダイアログを SW_SHOW、それ以外を SW_HIDE する
// タブ番号と対応するダイアログは自分で管理すること
※ dlg,dlg2 の open は selectTab されたときに行われるので、show(SW_HIDE) するときは isValid で open されているか確認のこと

---

### deleteTab

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |

---

### deleteAllTab

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### getCurSel

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### selectTab

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `dialog` | `&nbsp;` |  |

---

### setScrollInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | スクロールバーのダイアログアイテムID |
| `pos` | `&nbsp;` | スライダーの位置 |
| `min` | `&nbsp;` | 取りうる最小の値 |
| `max` | `&nbsp;` | 取りうる最大の値 |
| `page` | `&nbsp;` | ページの値 |

**解説**

ScrollInfo の設定

---

### getScrollInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `id` | `&nbsp;` | スクロールバーのダイアログアイテムID |

**戻り値**

%[pos, min, max, page]

**解説**

ScrollInfo の取得

---
