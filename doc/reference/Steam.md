# Steam

Steam クラス(static)

## メンバー一覧

### プロパティ

- [initialized](#initialized)
- [achievementsCount](#achievementscount)
- [steamID](#steamid)
- [accountID](#accountid)
- [loggedOn](#loggedon)
- [personaName](#personaname)
- [appID](#appid)
- [cloudEnabled](#cloudenabled)
- [coundFileCount](#coundfilecount)

### メソッド

- [requestInitialize](#requestinitialize)
- [getAchievement](#getachievement)
- [setAchievement](#setachievement)
- [clearAchievment](#clearachievment)
- [getLanguage](#getlanguage)
- [RestartAppIfNecessary](#restartappifnecessary)
- [getCloudQuota](#getcloudquota)
- [getCloudFileInfo](#getcloudfileinfo)
- [deleteCloudFile](#deletecloudfile)
- [copyCloudFile](#copycloudfile)
- [triggerScreenshot](#triggerscreenshot)
- [hookScreenshots](#hookscreenshots)
- [writeScreenshot](#writescreenshot)
- [isBroadcasting](#isbroadcasting)
- [hookBroadcasting](#hookbroadcasting)
- [isIsSubscribedApp](#isissubscribedapp)
- [ssDlcInstalled](#ssdlcinstalled)
- [getDLCCount](#getdlccount)
- [getDLCData](#getdlcdata)

---

### initialized

プロパティ \ アクセス: `r`

**解説**

実績情報初期化済み

---

### achievementsCount

プロパティ \ アクセス: `r`

**解説**

実績個数

---

### steamID

プロパティ \ アクセス: `r`

**解説**

--------------------------------------------------------- ユーザ情報 --------------------------------------------------------- セーブデータの置き場所をユーザごとに分ける用途を想定している。 Steam 自身の userdata フォルダは 32bit のアカウント ID で分かれるので、 それに合わせるなら accountID を使う。 SteamID (64bit) の文字列。取れないときは空文字列

---

### accountID

プロパティ \ アクセス: `r`

**解説**

アカウント ID (32bit の整数)。Steam の userdata フォルダ名と同じ値。 取れないときは 0

---

### loggedOn

プロパティ \ アクセス: `r`

**解説**

Steam にログイン済みかどうか

---

### personaName

プロパティ \ アクセス: `r`

**解説**

表示名 (ペルソナ名)。取れないときは空文字列

---

### appID

プロパティ \ アクセス: `r`

**解説**

動作中の AppID。取れないときは 0

---

### cloudEnabled

プロパティ \ アクセス: `r/w`

**解説**

--------------------------------------------------------- クラウド --------------------------------------------------------- Steamクラウドの有効/無効設定

---

### coundFileCount

プロパティ \ アクセス: `r/w`

**解説**

Steamクラウドのファイル数

---

### requestInitialize

メソッド

**戻り値**

呼び出し成功

**解説**

実績情報再取得要求 ※起動時に呼び出されるので普通は呼ぶ必要なし

--------------------------------------------------------- 実績 ---------------------------------------------------------

---

### getAchievement

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### setAchievement

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### clearAchievment

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n` | `&nbsp;` | 番号または識別名 |

**解説**

実績を解除する

---

### getLanguage

メソッド

**戻り値**

現在の Steam の言語を取得

**解説**

static method

--------------------------------------------------------- その他情報 ---------------------------------------------------------

---

### RestartAppIfNecessary

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `appid` | `&nbsp;` | 自分の AppID |

**戻り値**

true なら Steam が起動し直すので、すぐアプリを終了すること

※このメソッドだけは Steam の初期化を起こさずに呼べる
(初期化は最初に他の Steam.* を参照した時点で行われる)

**解説**

Steam クライアント経由で起動し直す必要があるかを調べる

--------------------------------------------------------- 起動チェック ---------------------------------------------------------

---

### getCloudQuota

メソッド

**戻り値**

%[total:トータルサイズ, available:使用可能容量]

**解説**

Steamクラウドの容量情報の取得

---

### getCloudFileInfo

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `n` | `&nbsp;` | ファイル番号 |

**戻り値**

%[filename:名前, size:サイズ, time:タイムスタンプ]

**解説**

個別のSteamクラウドファイルの名前とサイズの情報を取得

---

### deleteCloudFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**戻り値**

成功したら true

**解説**

Steamクラウドのファイルを削除する

---

### copyCloudFile

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `src` | `&nbsp;` |  |
| `dest` | `&nbsp;` |  |

**戻り値**

成功したら true

**解説**

Steamクラウドのファイルを複製する

---

### triggerScreenshot

メソッド

**解説**

スクリーンショット処理をアプリ側から起動させる

--------------------------------------------------------- スクリーンショット ---------------------------------------------------------

---

### hookScreenshots

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | コールバック関数（voidの場合は登録解除）<br>※コールバック関数内からwriteScreenshotを呼びます |

---

### writeScreenshot

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 画像 |
| `location` | `&nbsp;` | "場所文字列" (空文字の場合は登録しない） |

**解説**

スクリーンショットの登録

---

### isBroadcasting

メソッド

**戻り値**

配信中なら真

**解説**

--------------------------------------------------------- 配信状態 ---------------------------------------------------------

---

### hookBroadcasting

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | コールバック(function (is_start) {}) |

**解説**

配信状態変更時のコールバック

---

### isIsSubscribedApp

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**解説**

--------------------------------------------------------- DLC --------------------------------------------------------- only use this member if you need to check ownership of another game related to yours, a demo for example

---

### ssDlcInstalled

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**解説**

Takes AppID of DLC and checks if the user owns the DLC & if the DLC is installed

---

### getDLCCount

メソッド

**戻り値**

DLCの個数を返す

---

### getDLCData

メソッド

**引数**

| 引数 | 既定値 | 説明 |
| --- | --- | --- |
| `no` | `&nbsp;` | DLCの番号 |

---
