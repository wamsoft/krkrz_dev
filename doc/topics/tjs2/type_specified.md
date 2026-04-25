# 型指定構文

吉里吉里Zでは型指定されたTJSが実行可能。
型を指定してもエラーにならないだけで、スクリプトの動作は型指定しない場合と全く同じになる。エディタのインテリセンスを利用するためなどに使われる。

構文は以下の例のようになる。

## 変数宣言
変数名にコロンをつけ、その後に型を指定できる。
```
var i:int;
var win:Window = new Window();
```

## 関数定義
引数名にコロンをつけ、その後に型を指定できる。
戻り値は引数リストの後に指定できる。
```
function add(param1:int, param2:int) : int {
    return param1 + param2;
}
```

## 式中関数
関数定義と同様に引数と戻り値の型を指定できる。
```
var f = function(param1:string) : void {};
```

## プロパティ定義
setterの引数とgetterの戻り値の型をそれぞれ指定できる。
```
property prop {
    setter(value:int) {}
    getter:int { return 0; }
}
```
