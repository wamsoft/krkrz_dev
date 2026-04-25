# Debug

Debug クラスは 吉里吉里のデバッグに関する機能を提供するクラスです。このクラスからオブジェクトを作成することはできません。

吉里吉里のコンソールのログの名前は krkr.console.log になります。また、ハードウェア例外が発生したときに作成されるファイルは hwexcept.log となります。

これらのログファイルは、デフォルトではプロジェクトディレクトリになります。ただし、プロジェクトディレクトリがアーカイブなど、書き込みができないディレクトリの場合は出力されません。

ログファイルの出力先は logLocation プロパティで変更することができます (KAGの場合は栞データの保存先に設定されます)。

## メンバー一覧

### プロパティ

- [logLocation](#loglocation)
- [logToFileOnError](#logtofileonerror)
- [clearLogFileOnError](#clearlogfileonerror)

### メソッド

- [message](#message)
- [notice](#notice)
- [startLogToFile](#startlogtofile)
- [logAsError](#logaserror)
- [addLoggingHandler](#addlogginghandler)
- [removeLoggingHandler](#removelogginghandler)
- [getLastLog](#getlastlog)
- [prettyPrint](#prettyprint)

---

### logLocation

プロパティ \ アクセス: `r/w`

**解説**

ログファイルの出力先

ログファイルの出力先ディレクトリを表します。値を書き込むこともできます。

デフォルトではデータ保存場所 (コマンドラインオプションの -datapath) に設定されています。

この値を変更すると、以降のログはそのディレクトリ下の *.console.log として出力されるようになります。

---

### logToFileOnError

プロパティ \ アクセス: `r/w`

**解説**

エラー発生時にコンソールのログをファイルに出力するか

真の場合、エラーが発生したときにコンソールのログのファイルへの出力を開始するように
なります。

偽の場合はエラーが発生してもログのファイルへの出力は開始されません。

**関連:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### clearLogFileOnError

プロパティ \ アクセス: `r/w`

**解説**

エラー発生時にコンソールのログファイルをクリアするかどうか

真の場合、エラーが発生したときにコンソールのログを自動的にクリアするようになります。

偽の場合はクリアはされず、既存のログファイルに追加されます。

**関連:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror)

---

### message

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `message` | `&nbsp;` | 出力するメッセージを指定します。 |

**解説**

コンソールへメッセージを出力

**コンソール**へメッセージを出力します。

---

### notice

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `message` | `&nbsp;` | 出力するメッセージを指定します。 |

**解説**

コンソールへ重要なメッセージを出力

**コンソール**へメッセージを出力します。

[Debug.message](Debug.md#message) と違い、ここで出力したメッセージは ログファイルへの書き出しを途中から開始したとしても、
必ずログファイルに書き出されます ( Debug.message で出力したメッセージは、ある程度さかのぼってまでしか
書き込まれません )。ログファイルを回収したときに有用になるような重要な情報を出力するために使います。

---

### startLogToFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `clear` | `false` | 真を指定するとログファイルはクリアされます。<br>偽を指定すると既存のファイルに追加されます。 |

**解説**

コンソールのログの出力開始

コンソールのログのファイルへの出力を開始します。

**関連:** [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### logAsError

メソッド

**解説**

エラー時と同じようにログをファイルに出力開始する

エラーログファイルに関し、吉里吉里がエラーが発生したときと同じ動作をさせます。
つまり、
[Debug.logToFileOnError](Debug.md#logtofileonerror) が真ならばファイルにコンソールのログの出力を
開始します。その際、[Debug.clearLogFileOnError](Debug.md#clearlogfileonerror) が真ならばファイルを
クリアします。

これに対し、[Debug.startLogToFile](Debug.md#startlogtofile) は無条件でコンソールのログの
ファイルへの出力を開始します。

**関連:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### addLoggingHandler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ログハンドラを指定します。 |

**解説**

ログハンドラを追加します

エラーログが出力されるごとに呼び出されるハンドラを登録します。

ハンドラはログメッセージを引数に与えられて呼び出されます。

登録メソッド内でログを出力しても、再帰的な呼び出しは行われず無視されます。

---

### removeLoggingHandler

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | ログハンドラを指定します。 |

**解説**

ログハンドラを削除します

登録したログハンドラを削除します。

---

### getLastLog

メソッド

**解説**

未出力のログを取得します

出力していないログを取得します。

---

### prettyPrint

メソッド

**解説**

TODO: prettyPrint の説明

---
