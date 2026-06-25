# RegExp クラス

## RegExp クラス

RegExp クラスは**正規表現パターン**を扱うクラスです。

正規表現パターンには perl 互換のパターンを指定することができます。

JavaScript の RegExp クラスににていますが、互換性は低いです。



コンストラクタの構文は以下の通りです。

```
new RegExp(<パターン文字列>, <フラグ文字列=''>);
```

パターン文字列は正規表現パターンです。パターン中に指定する \ は、文字列即値中で書くときは \\ と書くことに注意してください。

フラグ文字列は g i l の文字の組み合わせです。

g はグローバルサーチフラグです。このフラグをつけると、match、exec、replace の各メソッドで、パターンにマッチした文字列の部分すべてに対して処理が行われます。

i フラグは英字の大文字/小文字の区別を行いません。

l フラグはローカライズされたコレーションを行うようにするフラグです。

```
	var re = new RegExp("[a-z]+[0-9]*", "gi");
	var re = new RegExp("\\.\\.\\."); // /\.\.\./ ( ... にマッチさせたい )
```

## 正規表現パターン

/ と / で囲まれた部分に正規表現パターンを指定することができます。

を参照してください。

## compile

compile メソッドは、正規表現オブジェクトに新しい正規表現パターンを設定します。

引数は RegExp クラスのコンストラクタに指定するものと同一です。

## test

test メソッドは、引数に指定した文字列がパターンにマッチするかどうかを返します。

```
構文 : test(<文字列>)
```

パターンにマッチすれば真、マッチしなければ偽が返ります。

このメソッドはこのオブジェクトの各プロパティの値を更新します。

## exec

exec メソッドは、引数に指定した文字列に正規表現パターンマッチングを行い、マッチした結果を含む配列を返します。

```
構文 : exec(<文字列>)
```

パターンにマッチしない場合、配列の要素数は 0 になります。

マッチした場合、要素 0 (最初の要素) はマッチした部分全体、それ以降の要素は各マッチ部分 ( 正規表現パターン中の (  ) で指定した部分 ) が入っています。

このメソッドはこのオブジェクトの各プロパティの値を更新します。

## match

match メソッドは、このオブジェクトのプロパティの値を更新しない以外は、exec メソッドと同一です。

```
構文 : match(<文字列>)
```

## replace

replace メソッドは、文字列の置き換えを行い、置き換えが行われた後の文字列を返します。

```
構文 : replace(<対象文字列>, <置き換え文字列>)
```

対象文字列に対してマッチングを行い、マッチした部分を置き換え文字列で置き換え、置き換えが行われた後の文字列を返します。

置き換え文字列として、文字列ではなく関数を渡すと、置き換え動作のためにその関数が呼ばれるようになります。関数は引数をひとつとり、対象文字列の中のマッチした部分をあらわす配列オブジェクトが渡されます ( この配列については exec メソッドを参照してください )。対象文字列中のマッチした部分は、関数の戻した文字列に置き換わります。

このメソッドは start プロパティを無視します。

## split

split メソッドは、文字列を分割します。

```
構文 : split(<対象文字列>, <(予約)>, <空の要素を無視するか=false>)
```

文字列を分割した結果が格納された配列オブジェクトを返します。

の split メソッドも参照してください。

## matches

matches プロパティは、マッチした各部分を含む配列を表す読み出し専用のプロパティです。

パターンにマッチしない場合、配列の要素数は 0 になります。

マッチした場合、要素 0 (最初の要素) はマッチした部分全体、それ以降の要素は各マッチ部分 ( 正規表現パターン中の (  ) で指定した部分 ) が入っています。

## start

文字列の検索開始位置を表すプロパティです。値を設定することもできます。

## index

マッチした部分の先頭文字の位置を表す、読み出し専用のプロパティです。0 が先頭を表すので、それがマッチング対象文字列の先頭の文字ならば 0 になります。

## lastIndex

マッチした部分の最終文字の次の文字の位置を表す、読み出し専用のプロパティです。0 が先頭を表します。

## input

マッチング対象の文字列をあらわす、読み出し専用のプロパティです。

## leftContext

マッチング対象文字列のうち、マッチした部分よりも左側の文字列をあらわす、読み出し専用のプロパティです。

## rightContext

マッチング対象文字列のうち、マッチした部分よりも右側の文字列をあらわす、読み出し専用のプロパティです。

## lastMatch

マッチング対象文字列を表します。matches[0] と同じです。

## lastParen

マッチした各部分のうち、最後の部分を返します。matches[matches.count-1] と同じです。

## RegExp.last

最後に test あるいは exec メソッドが実行された RegExp クラスのインスタンスです。

```
例 : if(/pat(\d+)/.test(target)) { return RegExp.last.matches[1]; }
```

## Copyright notice

正規表現機能の実装には John Maddock 氏の [Regex++](http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm) を用いています。有用なライブラリを公開なさっている氏に感謝します。



Copyright (c) 1998-2001



Dr John Maddock



Permission to use, copy, modify, distribute and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. Dr John Maddock makes no representations about the suitability of this software for any purpose. It is provided "as is" without express or implied warranty.
