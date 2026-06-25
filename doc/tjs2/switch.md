# switch ステートメント

## switch ステートメント

switch ステートメントを使うと、if ～ else if を簡潔に書くことができます。以下の構文をとります。

```
switch(base_expression)
{
**case** condition_expression1 :

case condition_expression2 :

:
:

**default**:

:
:
}
```

base_expression には式を書き、最初にこの式が評価されます。switch の次のブロックの中の case の次の condition_expression? にも式を書きます。

condition_expression? はブロック内で次々に評価されます。評価された結果が base_expression と同じ場合、そこから実行が開始されます。condition_expression? に合致しない場合は、その間にかかれた文やステートメントは無視されます。また、合致した場合、それ以降、case や default は無視されます。

default: は省略できますが、default がかかれた場合は強制的に default 以降の文やステートメントが実行されます。

ブロックを抜けるには **break**; を書きます。break を書き忘れて、次の case の内容まで実行してしまうのはよくあることなので注意してください。

```
	switch(a)
	{
	case 0:
		inform("a は 0 です");
		break;
	case 1:
		inform("b は 1 です");
		break;
	case 2:
		inform("b は 2 です");
		break;
	default:
		inform("b は 0 でも 1 でも 2 でもありません");
	}


	switch(a)
	{
	case 0:
	case 1: // break がないので case 0 の場合はここを通過する
		inform("a は 0 か 1 です");
		break;
	case 2:
		inform("a は 2 です");
	} // default がないので 0 1 2 以外の場合はなにも実行されない


	switch(a)
	{
	case b+1: // case の後には式も指定できる
		inform("a==b+1");
		break;
	case c+b:
		inform("a==c+b");
	}

	switch(str)
	{
	case "あいうえお": // 文字列も指定できる
		type=1;
		break;
	case "かきくけこ":
		type=2;
		break;
	}
```
