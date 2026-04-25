# 仮想マシン

## TJS2 VM

TJS2 は、スクリプトをいったん仮想マシン (TJS2 **VM**) 用のバイナリコードにコンパイルしてから実行します。

例外が発生したときやダンプを行ったときにこの TJS2 VM のコードの逆アセンブル結果が表示されるので、この仮想マシンについて簡単に説明します。

## 命令コード

TJS2 VM は関数やプロパティなどの実行単位ごとに独立していて、ある一つの関数が他の関数と命令コード空間、レジスタ空間、フラグ、定数領域を共有することはありません。

命令ポインタ (ip) は関数などの頭でかならず 0 から始まります。

命令コードを人間が読みやすい簡単な名前で表したものをニーモニックと呼びます。

## レジスタ

TJS2 VM のレジスタは、ニーモニック中では %(数字) で表されます。数字は負の数になることもあり得ます。レジスタ数に制限はありません。ローカル変数や計算中の一時的な値などはすべてレジスタに記録されます。主記憶 (メインメモリ) やスタックは存在しません。

レジスタが表す値は TJS2 のいわゆる変数と同じで、整数、実数、オブジェクト、文字列、オクテット列、void を表すことができます。

現バージョンでは、レジスタ %0 は常に void になります。レジスタ %-1 は this になります。レジスタ %-2 は **this proxy** と呼ばれる特殊なオブジェクトで、このオブジェクトに対してメンバ参照を行うと、まず this を見て、そこに無ければ global を見に行くという動作をします。this proxy は global レベルの実行単位には存在しません。関数などの引数は %-3 や %-4 などのレジスタにあらかじめ格納された状態で実行が開始されます。

このような、あらかじめ用途が決まっていたり、実行前に値があらかじめ入っているレジスタ以外の値は、実行開始の時点では不定です。

## フラグ

TJS2 VM にはフラグが１つだけあり、比較結果が格納されます。フラグは真か偽の値のみをとります。

## 定数領域

TJS2 VM の定数領域は定数を記憶する場所で、ニーモニック中では *(数字) で表されます。定数領域は読み出し専用で、レジスタへこの定数領域の値を移すには const 命令が用いられます。また、関数名やプロパティ名など、名前でオブジェクトのメンバをアクセスするための「名前」もこの定数領域に格納されます。

## VM ニーモニック一覧

オペランドに `%obj.*name` や `%obj.%name` の形式を持つものがありますが、これらはオブジェクトのメンバ参照を伴うものです。

オペランドに `%obj.*name` の形式を持つものは直接参照を行うもので、レジスタ `%obj` で表されたオブジェクトから `*name` で表された名前をもったメンバを参照します。

オペランドに `%obj.%name` の形式を持つものは間接参照を行うもので、レジスタ `%obj` で表されたオブジェクトから `%name` で表された名前をもったメンバを参照します。

このような命令のニーモニックは d または pd (direct / property direct) や i または pi (indirect / property indirect) のサフィックスをもちます。

サフィックスに p を持つ物は、対象レジスタのプロパティハンドラを動作させます (単項 '*' 演算子の動作をします)。

- ****nop**  
(no operation)**  
  何もしません。
- ****const**  
(copy constant value)**  
  書式: `const %dest, *src`
  
  
  *src で示された定数領域の値を %dest で示されたレジスタにコピーします。
- ****cp**  
(copy register)**  
  書式: `cp %dest, %src`
  
  
  %src で示されたレジスタの値を %dest で示されたレジスタにコピーします。
- ****cl**  
(clear register)**  
  書式: `cl %dest`
  
  
  %dest で示されたレジスタを void にします。
- ****ccl**  
(clear register)**  
  書式: `ccl %low-%high`
  
  
  %low で示されたレジスタ から %high で示されたレジスタの範囲をすべて void にします。
- ****tt**  
(test true)**  
  書式: `tt %reg`
  
  
  %reg で示されたレジスタが真を表していればフラグを真に、偽を表していればフラグを偽に設定します。
- ****tf**  
(test false)**  
  書式: `tf %reg`
  
  
  tt と逆で、%reg で示されたレジスタが真を表していればフラグを偽に、偽を表していればフラグを真に設定します。
- ****ceq**  
(compare equal)**  
  書式: `ceq %reg1, %reg2`
  
  
  %reg1 と %reg2 が通常比較 ( == 演算子の動作 ) で一致すればフラグを真、そうでなければ偽に設定します。
- ****cdeq**  
(compare distinct equal)**  
  書式: `cdeq %reg1, %reg2`
  
  
  %reg1 と %reg2 が識別比較 ( === 演算子の動作 ) で一致すればフラグを真、そうでなければ偽に設定します。
- ****clt**  
(compare littler than)**  
  書式: `clt %reg1, %reg2`
  
  
  %reg1 > %reg2 ならばフラグを真、そうでなければ偽に設定します。
- ****cgt**  
(compare greater than)**  
  書式: `cgt %reg1, %reg2`
  
  
  %reg1 < %reg2 ならばフラグを真、そうでなければ偽に設定します。
- ****setf**  
(set flag)**  
  書式: `setf %dest`
  
  
  フラグが真ならば %dest を真 (整数非0) に、偽ならば偽 (整数0) に設定します。
- ****setnf**  
(set not flag)**  
  書式: `setnf %dest`
  
  
  setf と逆で、フラグが偽ならば %dest を真 (整数非0) に、真ならば偽 (整数0) に設定します。
- ****lnot**  
(logical not)**  
  書式: `lnot %reg`
  
  
  %reg の真偽を逆にします。
- ****nf**  
(not flag)**  
  書式: `nf`
  
  
  フラグの真偽を逆にします。
- ****jf**  
(jump if flag)**  
  書式: `jf ip`
  
  
  フラグが真ならば ip にジャンプします。
- ****jnf**  
(jump if not flag)**  
  書式: `jnf ip`
  
  
  フラグが偽ならば ip にジャンプします。
- ****inc**, **incpd**, **incpi**, **incp**  
(increment)**  
  書式: `inc %reg`
  
  書式: `incpd %res, %obj.*name`
  
  書式: `incpi %res, %obj.%name`
  
  書式: `incp %res, %propobj`
  
  
  
  %reg または %obj.*name または %obj.%name または %propobj をインクリメントします。
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****dec**, **decpd**, **decpi**, **decp**  
(decrement)**  
  書式: `dec %reg`
  
  書式: `decpd %res, %obj.*name`
  
  書式: `decpi %res, %obj.%name`
  
  書式: `decp %res, %propobj`
  
  
  
  %reg または %obj.*name または %obj.%name または %propobj をデクリメントします。
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****lor**, **lorpd**, **lorpi**, **lorp**  
(logical or)**  
  書式: `lor %dest, %src`
  
  
  %dest と %src の論理和をとり、結果を %dest に格納します。
  
  
  書式: `lorpd %res, %obj.*name, %src`
  
  
  %obj.*name と %src の論理和をとり、結果を %obj.*name に格納します。
  
  
  書式: `lorpi %res, %obj.%name, %src`
  
  
  %obj.%name と %src の論理和をとり、結果を %obj.%name に格納します。
  
  
  書式: `lorp %res, %propobj, %src`
  
  
  %propobj と %src の論理和をとり、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****land**, **landpd**, **landpi**, **landp**  
(logical and)**  
  書式: `land %dest, %src`
  
  
  %dest と %src の論理積をとり、結果を %dest に格納します。
  
  
  書式: `landpd %res, %obj.*name, %src`
  
  
  %obj.*name と %src の論理積をとり、結果を %obj.*name に格納します。
  
  
  書式: `landpi %res, %obj.%name, %src`
  
  
  %obj.%name と %src の論理積をとり、結果を %obj.%name に格納します。
  
  
  書式: `landp %res, %propobj, %src`
  
  
  %propobj と %src の論理積をとり、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****bor**, **borpd**, **borpi**, **borp**  
(bitwise or)**  
  書式: `bor %dest, %src`
  
  
  %dest と %src のビットごとの論理和をとり、結果を %dest に格納します。
  
  
  書式: `borpd %res, %obj.*name, %src`
  
  
  %obj.*name と %src のビットごとの論理和をとり、結果を %obj.*name に格納します。
  
  
  書式: `borpi %res, %obj.%name, %src`
  
  
  %obj.%name と %src のビットごとの論理和をとり、結果を %obj.%name に格納します。
  
  
  書式: `borp %res, %propobj, %src`
  
  
  %propobj と %src のビットごとの論理和をとり、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****bxor**, **bxorpd**, **bxorpi**, **bxorp**  
(bitwise xor)**  
  書式: `bxor %dest, %src`
  
  
  %dest と %src のビットごとの排他的論理和をとり、結果を %dest に格納します。
  
  
  書式: `bxorpd %res, %obj.*name, %src`
  
  
  %obj.*name と %src のビットごとの排他的論理和をとり、結果を %obj.*name に格納します。
  
  
  書式: `bxorpi %res, %obj.%name, %src`
  
  
  %obj.%name と %src のビットごとの排他的論理和をとり、結果を %obj.%name に格納します。
  
  
  書式: `bxorp %res, %propobj, %src`
  
  
  %propobj と %src のビットごとの排他的論理和をとり、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****band**, **bandpd**, **bandpi**, **bandp**  
(bitwise and)**  
  書式: `band %dest, %src`
  
  
  %dest と %src のビットごとの論理積をとり、結果を %dest に格納します。
  
  
  書式: `bandpd %res, %obj.*name, %src`
  
  
  %obj.*name と %src のビットごとの論理積をとり、結果を %obj.*name に格納します。
  
  
  書式: `bandpi %res, %obj.%name, %src`
  
  
  %obj.%name と %src のビットごとの論理積をとり、結果を %obj.%name に格納します。
  
  
  書式: `bandp %res, %propobj, %src`
  
  
  %propobj と %src のビットごとの論理積をとり、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****sar**, **sarpd**, **sarpi**, **sarp**  
(shift arithmetic right)**  
  書式: `sar %dest, %src`
  
  
  %dest を %src で表された回数分算術右シフトを行った結果を %dest に格納します。
  
  
  書式: `sarpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で表された回数分算術右シフトを行った結果を %obj.*name に格納します。
  
  
  書式: `sarpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で表された回数分算術右シフトを行った結果を %obj.%name に格納します。
  
  
  書式: `sarp %res, %propobj, %src`
  
  
  %propobj を %src で表された回数分算術右シフトを行った結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****sal**, **salpd**, **salpi**, **salp**  
(shift arithmetic left)**  
  書式: `sal %dest, %src`
  
  
  %dest を %src で表された回数分算術左シフトを行った結果を %dest に格納します。
  
  
  書式: `salpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で表された回数分算術左シフトを行った結果を %obj.*name に格納します。
  
  
  書式: `salpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で表された回数分算術左シフトを行った結果を %obj.%name に格納します。
  
  
  書式: `salp %res, %propobj, %src`
  
  
  %propobj を %src で表された回数分算術左シフトを行った結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****sr**, **srpd**, **srpi**, **srp**  
(shift bitwise right)**  
  書式: `sr %dest, %src`
  
  
  %dest を %src で表された回数分ビット右シフトを行った結果を %dest に格納します。
  
  
  書式: `srpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で表された回数分ビット右シフトを行った結果を %obj.*name に格納します。
  
  
  書式: `srpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で表された回数分ビット右シフトを行った結果を %obj.%name に格納します。
  
  
  書式: `srp %res, %propobj, %src`
  
  
  %propobj を %src で表された回数分ビット右シフトを行った結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****add**, **addpd**, **addpi**, **addp**  
(add)**  
  書式: `add %dest, %src`
  
  
  %dest に %src を加算し、結果を %dest に格納します。
  
  
  書式: `addpd %res, %obj.*name, %src`
  
  
  %obj.*name に %src を加算し、結果を %obj.*name に格納します。
  
  
  書式: `addpi %res, %obj.%name, %src`
  
  
  %obj.%name に %src を加算し、結果を %obj.%name に格納します。
  
  
  書式: `addp %res, %propobj, %src`
  
  
  %propobj に %src を加算し、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****sub**, **subpd**, **subpi**, **subp**  
(subtract)**  
  書式: `sub %dest, %src`
  
  
  %dest から %src を減算し、結果を %dest に格納します。
  
  
  書式: `subpd %res, %obj.*name, %src`
  
  
  %obj.*name から %src を減算し、結果を %obj.*name に格納します。
  
  
  書式: `subpi %res, %obj.%name, %src`
  
  
  %obj.%name から %src を減算し、結果を %obj.%name に格納します。
  
  
  書式: `subp %res, %propobj, %src`
  
  
  %propobj から %src を減算し、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****mod**, **modpd**, **modpi**, **modp**  
(modulo)**  
  書式: `mod %dest, %src`
  
  
  %dest を %src で割ったあまりを %dest に格納します。
  
  
  書式: `modpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で割ったあまりを %obj.*name に格納します。
  
  
  書式: `modpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で割ったあまりを %obj.%name に格納します。
  
  
  書式: `modp %res, %propobj, %src`
  
  
  %propobj を %src で割ったあまりを %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****div**, **divpd**, **divpi**, **divp**  
(real divide)**  
  書式: `div %dest, %src`
  
  
  %dest を %src で実数除算し、結果を %dest に格納します。
  
  
  書式: `divpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で実数除算し、結果を %obj.*name に格納します。
  
  
  書式: `divpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で実数除算し、結果を %obj.%name に格納します。
  
  
  書式: `divp %res, %propobj, %src`
  
  
  %propobj を %src で実数除算し、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****idiv**, **idivpd**, **idivpi**, **idivp**  
(integer divide)**  
  書式: `idiv %dest, %src`
  
  
  %dest を %src で整数除算し、結果を %dest に格納します。
  
  
  書式: `idivpd %res, %obj.*name, %src`
  
  
  %obj.*name を %src で整数除算し、結果を %obj.*name に格納します。
  
  
  書式: `idivpi %res, %obj.%name, %src`
  
  
  %obj.%name を %src で整数除算し、結果を %obj.%name に格納します。
  
  
  書式: `divp %res, %propobj, %src`
  
  
  %propobj を %src で整数除算し、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****mul**, **mulpd**, **mulpi**, **mulp**  
(multiply)**  
  書式: `mul %dest, %src`
  
  
  %dest に %src を乗算し、結果を %dest に格納します。
  
  
  書式: `mulpd %res, %obj.*name, %src`
  
  
  %obj.*name に %src を乗算し、結果を %obj.*name に格納します。
  
  
  書式: `mulpi %res, %obj.%name, %src`
  
  
  %obj.%name に %src を乗算し、結果を %obj.%name に格納します。
  
  
  書式: `mulp %res, %propobj, %src`
  
  
  %propobj に %src を乗算し、結果を %propobj に格納します。
  
  
  上記の命令の中で、%res をパラメータに持つ物は、res が 0 で無ければ結果を %res にも格納します。
- ****bnot**  
(bitwise not)**  
  書式: `bnot %reg`
  
  
  %reg をビットごとの真偽を逆にし、%reg に再び格納します。
- ****asc**  
(make ascii string)**  
  書式: `asc %reg`
  
  
  %reg で表された数値に相当する１文字を作成し、それを再び %reg に格納します。
- ****chr**  
(cheracter code)**  
  書式: `chr %reg`
  
  
  %reg で表された文字列の最初の一文字の文字コードを %reg に格納します。
- ****num**  
(number)**  
  書式: `num %reg`
  
  
  %reg で表されたレジスタを数値に変換します。
- ****chs**  
(change sign)**  
  書式: `chs %reg`
  
  
  %reg で表されたレジスタの数値の正負を逆にします。
- ****inv**  
(invalidate)**  
  書式: `inv %reg`
  
  
  %reg で表されたオブジェクトを無効化します。
- ****chkinv**  
(invalidate)**  
  書式: `chkinv %reg`
  
  
  %reg で表されたオブジェクトが無効化されていなければ %reg を真に、そうでなければ偽に設定します。
- ****int**  
(convert to integer)**  
  書式: `int %reg`
  
  
  %reg で表されたレジスタを整数に変換します。
- ****real**  
(convert to real)**  
  書式: `real %reg`
  
  
  %reg で表されたレジスタを実数に変換します。
- ****string**  
(convert to string)**  
  書式: `string %reg`
  
  
  %reg で表されたレジスタを文字列に変換します。
- ****octet**  
(convert to octet)**  
  書式: `octet %reg`
  
  
  %reg で表されたレジスタをオクテット列に変換します。
- ****typeof**, **typeofd**, **typeofi**  
(check type)**  
  書式: `typeof %reg`
  
  書式: `typeofd %obj.*name`
  
  書式: `typeofi %obj.%name`
  
  
  
  %reg または %obj.*name または %obj.%name の型を調べ、その型を表す文字列を再び %reg または %obj.*name または %obj.%name に格納します。
- ****eval**  
(evaluate expression)**  
  書式: `eval %reg`
  
  
  %reg で表された文字列を式として実行し、その結果を再び %reg に格納します。
- ****eexp**  
(execute expression)**  
  書式: `eexp %reg`
  
  
  %reg で表された文字列を式として実行し、結果を捨てます。
- ****chkins**  
(check instance)**  
  書式: `chkins %reg, %classname`
  
  
  %reg で表されたオブジェクトが、%classname で表されたクラス名のクラスのインスタンスであれば %reg に真を、そうでなければ偽を格納します。
- ****call**, **calld**, **calli**  
(function call)**  
  書式: `call %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  書式: `calld %dest, %obj.*name(%arg1, %arg2, %arg3, ...)`
  
  書式: `calli %dest, %obj.%name(%arg1, %arg2, %arg3, ...)`
  
  
  
  %func または %obj.*name または %obj.%name で表された関数オブジェクトを、%arg1, %arg2, %arg3 ... の引数で呼び出し、結果を %dest に格納します。%dest が %0 の場合は結果は ( %0 には格納されずに ) 捨てられます。
- ****new**  
(create new)**  
  書式: `new %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  
  %func で表されたクラスオブジェクトを、%arg1, %arg2, %arg3 ... の引数で構築し、結果を %dest に格納します。
- ****gpd**, **gpds**  
(get property direct)**  
  書式: `gpd %dest, %obj.*name`
  
  書式: `gpds %dest, %obj.*name`
  
  
  
  %obj で表されたオブジェクトから *name で表されたメンバを参照し、その値を %dest にコピーします。
  
  gpd はプロパティハンドラの呼び出しを伴いますが、gpds はプロパティハンドラを呼び出さず、プロパティオブジェクト自体を取得します。
- ****gpi**, **gpis**  
(get property indirect)**  
  書式: `gpi %dest, %obj.%name`
  
  書式: `gpis %dest, %obj.%name`
  
  
  
  %obj で表されたオブジェクトから %name で表されたメンバを参照し、その値を %dest にコピーします。
  
  gpi はプロパティハンドラの呼び出しを伴いますが、gpis はプロパティハンドラを呼び出さず、プロパティオブジェクト自体を取得します。
- ****spd**, **spde**, **spdeh**, **spds**  
(set property direct)**  
  書式: `spd %obj.*name`
  
  書式: `spde %obj.*name`
  
  書式: `spdeh %obj.*name`
  
  書式: `spds %obj.*name`
  
  
  
  %obj で表されたオブジェクトの *name で表されたメンバに、%src の値を代入します。
  
  spd は通常のアクセスを行いますが、メンバが存在しない場合は例外が発生します。
  
  spde はメンバが存在しなければメンバを新規に作成します。
  
  spdeh はメンバを隠しメンバとして設定します。現バージョンでは意味を持ちません。
  
  spds はプロパティハンドラを呼び出さず、プロパティオブジェクト自体を置き換えます。
- ****spi**, **spie**, **spis**  
(set property indirect)**  
  書式: `spi %obj.%name`
  
  書式: `spie %obj.%name`
  
  書式: `spis %obj.%name`
  
  
  
  %obj で表されたオブジェクトの %name で表されたメンバに、%src の値を代入します。
  
  spi は通常のアクセスを行いますが、メンバが存在しない場合は例外が発生します。
  
  spie はメンバが存在しなければメンバを新規に作成します。
  
  spis はプロパティハンドラを呼び出さず、プロパティオブジェクト自体を置き換えます。
- ****getp****  
  書式: `getp %reg, %propobj`
  
  
  
  %propobj で表されたプロパティオブジェクトの getter を動作させ、プロパティの値を得て、%reg に代入します。単項 '*' 演算子の動作を行います。
- ****setp****  
  書式: `setp %propobj, %reg`
  
  
  
  %propobj で表されたプロパティオブジェクトの setter を動作させ、%reg の値を設定します。単項 '*' 演算子の動作を行います。
- ****deld**, **deli**  
(delete member)**  
  書式: `deld %reg, %obj.*name`
  
  書式: `deli %reg, %obj.%name`
  
  
  
  %obj で表されたオブジェクトの *name または %name で表されたメンバを削除します。
  
  削除が成功したかどうかの真偽を %reg に格納しますが、%reg が %0 の場合は結果を捨てます。
- ****srv**  
(set result value)**  
  書式: `srv %reg`
  
  
  %reg の値を関数の戻り値とします ( 関数の戻り値は %reg で表された値になります )。
- ****ret**  
(return)**  
  書式: `ret`
  
  
  呼び出し元に戻ります。
- ****entry**  
(enter try block)**  
  書式: `entry ip, %reg`
  
  
  例外保護されたブロックに入ります。例外が発生した場合、ip にジャンプし、例外オブジェクトを %reg に設定します。
- ****extry**  
(exit from try block)**  
  書式: `extry`
  
  
  例外保護されたブロックから出ます。
- ****throw**  
(throw exception object)**  
  書式: `throw %reg`
  
  
  %reg で表されたオブジェクトを例外オブジェクトとして投げます。
- ****chgthis**  
(change this)**  
  書式: `chgthis %dest, %src`
  
  
  %dest で表されたオブジェクトのクロージャ部分を、%src で示されたオブジェクトに変更します。
- ****global**  
(get global object)**  
  書式: `global %dest`
  
  
  グローバルオブジェクトを %dest に格納します。
- ****addci**  
(add class instance information)**  
  書式: `addci %dest, %info`
  
  
  %dest で表されるオブジェクトのクラスインスタンス情報に %info を追加します。
- ****regmember**  
(register members)**  
  書式: `regmember`
  
  
  クラスのメンバを "this" オブジェクトに登録します。内部的に用いられます。
- ****debugger**  
(call debugger)**  
  書式: `debugger`
  
  
  実行を中断し、デバッガを呼び出します。現バージョンの実装では、TJS2デバッガではなく、ネイティブなデバッガを呼び出します。
