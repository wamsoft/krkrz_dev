# ライセンス情報の取得と表示

吉里吉里Z は、本体とプラグインが内蔵する第三者コンポーネント ( ライブラリ・
フォント等 ) のライセンス文を実行ファイルの中に保持しています。これらは
TJS から一覧・全文とも取り出せるので、ゲーム内のクレジット画面やライセンス
表示画面をスクリプト側で自由に組めます。

## 3 つの供給元

一覧は次の 3 系統を合流させたものです。スクリプトから見るときの違いは
`source` メンバの値だけで、取得方法は同じです。

| `source` | 中身 | 供給のしかた |
|---|---|---|
| `builtin` | 本体が内蔵するぶん ( エンジンが使うライブラリ・同梱フォント ) | 実行ファイルに圧縮して埋め込み済み |
| `plugin` | プラグインが登録したぶん | プラグイン DLL がロード時に登録する |
| `storage` | プロジェクトが持つぶん | プロジェクトの `licenses` フォルダに置いたテキスト |

同じ名前が複数の供給元にある場合は 1 件にまとめられます
( 優先順位は `plugin` > `builtin` > `storage` )。

## TJS から取得する

### 一覧を取る

[System.getLicenseList](../reference/System.md#getlicenselist) は辞書の配列を
返します。各要素は `name` ( 表示名 ) `group` ( 分類 ) `source` ( 供給元 ) を
持ちます。

```tjs
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	Debug.message(e.name + " / " + e.group + " / " + e.source);
}
```

`group` は分類用の文字列で、本体内蔵ぶんは次の値を使っています。プラグインや
案件が登録するぶんは任意の文字列になり得るので、**網羅を前提にした
`switch` を書かない**でください ( 未知の値はそのまま表示する等の扱いにします )。

| `group` | 内容 |
|---|---|
| `engine` | エンジン基盤 ( zlib / libpng / Oniguruma など ) |
| `font-engine` | フォントエンジン ( FreeType / HarfBuzz など ) |
| `audio` | オーディオ ( libogg / libvorbis / Opus など ) |
| `video` | 動画 ( libvpx / libyuv など ) |
| `ui` | UI 描画 ( Elements / ThorVG ) |
| `platform` | プラットフォーム ( SDL3 / ANGLE など ) |
| `font` | 同梱フォント |
| `data` | プロジェクトの `licenses` フォルダに置いたぶん |

### 全文を取る

[System.getLicenseText](../reference/System.md#getlicensetext) に `name` を
渡すと、ライセンス文全体が文字列で返ります。**見つからない場合は void** です。

```tjs
var text = System.getLicenseText("FreeType");
if (text !== void) {
	Debug.message(text);
}
```

!!! warning "`if (text)` で判定しない"
    TJS2 では数値に変換できない文字列を条件式に置くと **常に偽** になります。
    ライセンス文のような文字列は `text !== void` で判定してください。

### 一覧と全文をまとめて 1 つの文字列にする

クレジット表示をテキストで一気に出したい場合の例です。

```tjs
function buildLicenseText()
{
	var list = System.getLicenseList();
	var buf = [];
	for (var i = 0; i < list.count; i++) {
		var name = list[i].name;
		var text = System.getLicenseText(name);
		if (text === void) continue;
		buf.add("======== " + name + " ========");
		buf.add(text);
	}
	return buf.join("\n");
}
```

### 分類ごとにまとめる

```tjs
var byGroup = %[];
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	if (byGroup[e.group] === void) byGroup[e.group] = [];
	byGroup[e.group].add(e.name);
}
```

辞書に無いメンバを読んだ場合は void が返るので、上のように初期化できます。

### System.licenseText との使い分け

[System.licenseText](../reference/System.md#licensetext) は
「バージョン行 + 吉里吉里Z 本体の条項 + 同梱コンポーネントの一覧」を
1 つの文字列にしたもので、**そのまま表示するだけ**の用途向けです。
個々のコンポーネントの全文は含まれないので、全文が要るときは
`getLicenseText` を使ってください。

| やりたいこと | 使うもの |
|---|---|
| 本体の条項をそのまま出す | `System.licenseText` |
| 何が入っているか一覧したい | `System.getLicenseList()` |
| 特定コンポーネントの全文が要る | `System.getLicenseText(name)` |

## 内蔵のビューアを使う

ElementsDialog が使えるビルドでは、サンプル実装
`data/ui/license_dialog.tjs` をそのまま利用できます。左ペイン = 分類別の
項目リスト、右ペイン = ライセンス本文の 2 ペイン構成です。

```tjs
Scripts.execStorage("ui/license_dialog.tjs");
showLicenseDialog(win);          // モーダル。閉じるまでブロック
showLicenseDialog(win, false);   // 非モーダル ( 戻り値 = ElementsDialog )
```

プロジェクトへコピーして改変してかまいません。ElementsDialog が無いビルド
( `KRKRZ_USE_ELEMENTS=OFF` ) では何もせず void を返します。

## プロジェクトの資材を一覧に載せる

プロジェクトの `licenses` フォルダに **1 資材 = 1 テキスト** で置くと、
起動時に自動で一覧へ合流します ( `source` は `storage`、`group` は `data` )。
拡張子は `.txt` と `.md` が対象です。

```
licenses/kenney-input-prompts.txt
licenses/myfont-regular.txt
```

- **表示名 ( `name` ) はファイル名から拡張子を除いて小文字にしたもの**です。
  `MyFont-Regular.txt` は `myfont-regular` として並びます。表示上のタイトルを
  整えたい場合は、ファイル本文の 1 行目に資材名を書いておくと親切です。
- `System.getLicenseText(name)` も同じ名前で引けます
  ( `licenses/<name>.txt` → 無ければ `.md` の順に探します )。
- ファイルは UTF-8 で置いてください ( BOM は付いていても構いません )。

### 記述例

ゲームパッドのボタン表示によく使う
[Kenney Input Prompts](https://kenney.nl/assets/input-prompts) ( CC0 ) を
同梱するなら `licenses/kenney-input-prompts.txt` として:

```
Input Prompts (Kenney)

This product includes "Input Prompts" by Kenney (www.kenney.nl),
released under Creative Commons Zero (CC0 1.0 Universal).

  https://kenney.nl/assets/input-prompts
  https://creativecommons.org/publicdomain/zero/1.0/

Attribution is not required, but appreciated:
  "Input Prompts" by Kenney (www.kenney.nl)
```

pack 同梱の License.txt をそのまま置いてもかまいません。CC0 は表記義務が
ありませんが、一覧に載せておくと資材の出所管理とクレジット表示が楽になります。

## 起動オプションから確認する

スクリプトを書かずに中身を確認したいときは、起動オプション
[-license](CommandLine.md) が使えます。開発中の確認や、配布物に何が入って
いるかの点検に向いています。

```
krkrz64.exe -license            # 一覧
krkrz64.exe -license=FreeType   # 1 件の全文
krkrz64.exe -license=all        # 全件の全文
```

プロジェクトを指定して起動すれば、そのプロジェクトの `licenses` フォルダの
ぶんも一覧に載ります。`-about` の「バージョン・著作権・環境情報」ダイアログ
にも同じ一覧が表示されます。

## 配布物に入るファイル

`make install` で作られる配布物には、実行時の一覧とは別に、ライセンス原文が
ファイルとしても書き出されます。

| パス | 内容 |
|---|---|
| `license.txt` | 吉里吉里Z 本体の条項 |
| `licenses/<名前>.txt` | 本体が内蔵する第三者コンポーネントの原文 |
| `licenses/plugins/<名前>.txt` | 同梱したプラグインが内蔵するぶんの原文 |

どのコンポーネントがどのライセンスかの対応表は
[同梱ライセンス一覧](BundledLicenses.md) にまとまっています。

## プラグインから登録する

プラグイン側が内蔵するライセンス文は、`tp_stub` で公開されている登録関数から
一覧へ合流させます ( 登録すると `source` が `plugin` の項目として現れます )。

| 関数 | 用途 |
|---|---|
| `TVPRegisterLicense(name, group, deflated, deflatedSize, originalSize)` | 圧縮済みテキストを登録 ( データは参照保持 ) |
| `TVPRegisterLicenseText(name, group, text)` | 生テキストを登録 ( 短いもの向け ) |
| `TVPGetLicenseText(name, &text)` | 名前で全文を取得 |
| `TVPEnumLicenses(sink)` | 全件を列挙 |

登録用のソースは manifest から生成できます。仕組みと生成手順は
エンジン側の `src/core/doc/LicenseSystem.md` を参照してください。
