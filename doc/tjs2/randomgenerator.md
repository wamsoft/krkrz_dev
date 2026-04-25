# Math.RandomGenerator クラス

## Math.RandomGenerator クラス

Math.RandomGenerator は、[Mersenne Twister 法](http://www.math.keio.ac.jp/~matumoto/emt.html) による乱数を発生するためのクラスです。


コンストラクタの構文は以下の通りです。

```
new Math.RandomGenerator([<乱数種>]);
```

コンストラクタに数値を指定すると、その数値で乱数発生器が初期化されます。

コンストラクタに serialize メソッドで状態を保存した辞書配列オブジェクトを指定すると、その状態で乱数発生器を作成できます。

コンストラクタを省略すると、現在時刻を元にした乱数値で乱数発生器が初期化されます (吉里吉里2の場合は現在時刻ではなく、環境ノイズを元にした乱数発生器からの乱数で初期化されます)。

## randomize

randomize メソッドは、乱数発生器を初期化します。引数はコンストラクタに指定する物と同じです。

## random

random メソッドは、0以上1.0未満の実数の乱数値を返します。

## random32

random32 メソッドは、0以上4,294,967,295以下 (0xffffffff 以下) の整数の乱数値を返します。

## random63

random63 メソッドは、0以上9,223,372,036,854,775,807以下(0x7fffffffffffffff 以下) の整数の乱数値を返します。

## random64

random64 メソッドは、-9,223,372,036,854,775,808以上9,223,372,036,854,775,807以下の整数の乱数値を返します。

## serialize

serialize メソッドは、現在の状態を記録した辞書配列オブジェクトを返します。この辞書配列オブジェクトは、コンストラクタや randomize メソッドに渡すことで、再び現在の状態を再現できる物です。

## Copyright notice

Mersenne Twister法の実装には



A C-program for MT19937, with initialization improved 2002/2/10.
Coded by Takuji Nishimura and Makoto Matsumoto.



を改変した物を用いています。有用なプログラムソースを公開なさっている両氏に感謝します。



Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,

All rights reserved.



Redistribution and use in source and binary forms, with or without

modification, are permitted provided that the following conditions

are met:



1. Redistributions of source code must retain the above copyright

notice, this list of conditions and the following disclaimer.



2. Redistributions in binary form must reproduce the above copyright

notice, this list of conditions and the following disclaimer in the

documentation and/or other materials provided with the distribution.



3. The names of its contributors may not be used to endorse or promote

products derived from this software without specific prior written

permission.



THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS

"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT

LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR

A PARTICULAR PURPOSE ARE DISCLAIMED.	 IN NO EVENT SHALL THE COPYRIGHT OWNER OR

CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,

EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,

PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR

PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF

LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING

NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS

SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
