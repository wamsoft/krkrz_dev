# Steam

Steam class (static)

## Members

### Properties

- [initialized](#initialized)
- [achievementsCount](#achievementscount)
- [steamID](#steamid)
- [accountID](#accountid)
- [loggedOn](#loggedon)
- [personaName](#personaname)
- [appID](#appid)
- [cloudEnabled](#cloudenabled)
- [cloudFileCount](#cloudfilecount)

### Methods

- [requestInitialize](#requestinitialize)
- [getAchievement](#getachievement)
- [setAchievement](#setachievement)
- [clearAchievement](#clearachievement)
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
- [isDlcInstalled](#isdlcinstalled)
- [getDLCCount](#getdlccount)
- [getDLCData](#getdlcdata)

---

### initialized

Property \ Access: `r`

**Description**

Whether the achievement information has been initialized

---

### achievementsCount

Property \ Access: `r`

**Description**

Number of achievements

---

### steamID

Property \ Access: `r`

**Description**

SteamID (64-bit) as a string. An empty string if unavailable

---

### accountID

Property \ Access: `r`

**Description**

Account ID (32-bit integer), the same value as the Steam userdata folder name. 0 if unavailable

---

### loggedOn

Property \ Access: `r`

**Description**

Whether the user is logged on to Steam

---

### personaName

Property \ Access: `r`

**Description**

Display name (persona name). An empty string if unavailable

---

### appID

Property \ Access: `r`

**Description**

AppID of the running app. 0 if unavailable

---

### cloudEnabled

Property \ Access: `r/w`

**Description**

Whether Steam Cloud is enabled

---

### cloudFileCount

Property \ Access: `r`

**Description**

Number of files in Steam Cloud

---

### requestInitialize

Method

**Return value**

Whether the call succeeded.

**Description**

Requests the achievement information again (called at startup, so normally not needed)

---

### getAchievement

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### setAchievement

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### clearAchievement

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n` | `&nbsp;` | Index or identifier |

**Description**

Clears an achievement

---

### getLanguage

Method

**Return value**

The current Steam language.

**Description**

static method

---

### RestartAppIfNecessary

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `appid` | `&nbsp;` | Your own AppID. |

**Return value**

If true, Steam relaunches the app, so exit immediately.

Note: this is the only method that can be called without initializing Steam
(initialization happens the first time any other Steam.* member is accessed).

**Description**

Checks whether the app needs to be relaunched through the Steam client

---

### getCloudQuota

Method

**Return value**

%[total: total size, available: available space]

**Description**

Gets the Steam Cloud quota

---

### getCloudFileInfo

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `n` | `&nbsp;` | File index. |

**Return value**

%[filename: name, size: size, time: timestamp]

**Description**

Gets the name and size of an individual Steam Cloud file

---

### deleteCloudFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**Return value**

true on success.

**Description**

Deletes a Steam Cloud file

---

### copyCloudFile

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `src` | `&nbsp;` |  |
| `dest` | `&nbsp;` |  |

**Return value**

true on success.

**Description**

Copies a Steam Cloud file

---

### triggerScreenshot

Method

**Description**

Triggers a screenshot from the app

---

### hookScreenshots

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | Callback function (void unregisters it).<br>Call writeScreenshot from inside the callback. |

---

### writeScreenshot

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `layer` | `&nbsp;` | Image. |
| `location` | `&nbsp;` | Location string (not registered if empty). |

**Description**

Registers a screenshot

---

### isBroadcasting

Method

**Return value**

true while broadcasting.

---

### hookBroadcasting

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `callback` | `&nbsp;` | Callback (function (is_start) {}). |

**Description**

Callback for broadcast state changes

---

### isIsSubscribedApp

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**Description**

only use this member if you need to check ownership of another game related to yours, a demo for example

---

### isDlcInstalled

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**Description**

Takes AppID of DLC and checks if the user owns the DLC & if the DLC is installed

---

### getDLCCount

Method

**Return value**

Number of DLCs.

---

### getDLCData

Method

**Arguments**

| Arguments | Default | Description |
| --- | --- | --- |
| `no` | `&nbsp;` | DLC index. |

---
