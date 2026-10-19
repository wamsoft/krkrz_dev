---
source_hash: 48591fbe159c
---

# Math.RandomGenerator Class

## Math.RandomGenerator class

Math.RandomGenerator generates random numbers using the [Mersenne Twister](http://www.math.keio.ac.jp/~matumoto/emt.html) algorithm.


The constructor syntax is as follows.

```
new Math.RandomGenerator([<乱数種>]);
```

If you pass a number (a seed) to the constructor, the generator is initialized with that number.

If you pass a dictionary array object holding a state saved with the serialize method, the generator is created in that state.

If the argument is omitted, the generator is initialized with a random value derived from the current time (in Kirikiri 2, it is initialized with a random number from a generator based on environmental noise instead of the current time).

## randomize

The randomize method initializes the generator. Its argument is the same as the constructor's.

## random

The random method returns a random real number from 0 up to, but not including, 1.0.

## random32

The random32 method returns a random integer from 0 to 4,294,967,295 (0xffffffff) inclusive.

## random63

The random63 method returns a random integer from 0 to 9,223,372,036,854,775,807 (0x7fffffffffffffff) inclusive.

## random64

The random64 method returns a random integer from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 inclusive.

## serialize

The serialize method returns a dictionary array object that records the current state. Passing this object to the constructor or to the randomize method restores that state.

## Copyright notice

The Mersenne Twister implementation is a modified version of



A C-program for MT19937, with initialization improved 2002/2/10.
Coded by Takuji Nishimura and Makoto Matsumoto.



Many thanks to the authors for publishing such useful source code.



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
