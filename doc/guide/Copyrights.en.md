---
source_hash: ccdbfe02f48e
---

# Copyrights

## Checking and Displaying Third-Party Licenses

The license texts of the third-party components ( libraries / fonts ) built into
the engine and plugins can be retrieved from TJS at runtime:

```tjs
var list = System.getLicenseList();   // [%[name, group, source], ...]
var text = System.getLicenseText("FreeType");
```

In addition to the entries built into the engine, entries registered by plugins
and **text files placed in the project's `licenses` folder** ( licenses for
additional fonts, etc. ) are merged into the same list. How to retrieve and
display them, and how to add assets, is covered in
**[Getting and Displaying License Information](Licenses.md)**.

- You can also check the list / full texts with the [-license](CommandLine.md)
  command-line option ( the list also appears in the `-about` dialog ).
- **Which component uses which license** is summarized in
  [Bundled Licenses](BundledLicenses.md)
  ( split into engine / plugins / fonts; generated automatically from the manifests ).

## Copyright / License

See license.txt included with the SDK.

The following are FAQs about copyright and licensing, or things many people are likely to wonder about.

The principles are as written in license.txt, so be sure to read license.txt.

If anything written here conflicts with license.txt, license.txt takes precedence.

- **Do I have to pay the author of Kirikiri...?**  
  No, you do not.
- **I want to use it commercially ( including shareware )...**  
  You can use it commercially.
  
  Even for commercial use, no license fees are required. You can use it free of charge.
- **I would like to credit you in my work...**  
  You do not need to state in your documentation or elsewhere that you used Kirikiri.
  
  Of course, you are welcome to do so (^^;
  
  Unless you state it, you cannot remove the license notice shown by -about.
  
  If you include the license notice in your documentation or elsewhere in accordance with the modified BSD license, you may also remove the license notice shown by -about.
- **Do I have to notify the author of Kirikiri when my work is finished...?**  
  You are not obliged to notify anyone that you used Kirikiri, even for commercial use.
  
  That said, a quick word would certainly be appreciated.
- **I want to reuse Kirikiri's source...**  
  Kirikiri Z is under the modified BSD license. You can reuse the source in accordance with the modified BSD license.

## Acknowledgments

Kirikiri 2 and Kirikiri Z exist thanks to the cooperation of many people. We are grateful for everyone's kindness.

In particular, Second Lieutenant PIA gave us a great deal of advice on Kirikiri. Thank you.



Kirikiri Z was developed with the financial support of many people through crowdfunding.

Our supporters (in no particular order, honorifics omitted) are:　W.Dee, casper, 有限会社MCF, Biscrat, 青猫, nagai, ルー, 高際 雅之, 永劫,ゆんゆん探偵, りょうご（今は無きあの星）, AZ-UME, 京 秋人, Katsumasa Tsuneyoshi, 小池潤, miahmie, サークル獏, アザナシ, はっしぃ, 棚中製作所, わっふる/waffle, ワムソフト, TYPE-MOON, 有限会社エムツー.



Many plugins, including the Win32Ole plugin, were contributed by Go Watanabe. Thank you.



The Photoshop-compatible blend functions were contributed by Kenjo. Thank you.



The gamepad support code was contributed by Kiyobee. Thank you.



The documentation for the KAGParser class and the KAGParser extensions were contributed by Kouhei Yanagita. Thank you.



The Kirikiri icon is by MIK. Thank you.



Various movie playback features, such as movie playback on layers, incorporate the "Movie Extension" by Takenori Imoto. Thank you.

[http://www.kaede-software.com/](http://www.kaede-software.com/)



The blur implementation is based on code contributed by yun. Thank you.



mey contributed patches enhancing the Pad features and implementations such as String.reverse(). Thank you.



The following is a list of programming libraries and support software used by Kirikiri (in no particular order, honorifics omitted). We thank everyone who publishes such useful libraries.

- **IJG JPEG Library (Independent JPEG Group)**  
  [http://www.ijg.org/](http://www.ijg.org/)
  
  This software is based in part on the work of the Independent JPEG Group.
- **libpng (Guy Eric Schalnat, Andreas Dilger, Glenn Randers-Pehrson,  and others)**  
  [http://www.libpng.org/pub/png/libpng.html](http://www.libpng.org/pub/png/libpng.html)
- **zlib (Jean-loup Gailly, Mark Adler)**  
  [http://www.gzip.org/zlib/](http://www.gzip.org/zlib/)
- **ERINA-Library (L.Entis)**  
  [http://www.entis.jp/eri/](http://www.entis.jp/eri/)
  
  ERINA-Library Copyright (C) 2001 Leshade Entis, Entis-soft.
- **Regex++ (Dr John Maddock)**  
  [http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm](http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm)
  
  Regex++ Copyright (c) 1998-2000 Dr John Maddock
- **UPX (Markus F.X.J. Oberhumer & Laszlo Molnar)**  
  [http://upx.sourceforge.net/](http://upx.sourceforge.net/)
- **Shell Component Library (Takashi Ito)**  
  [http://www.bekkoame.ne.jp/~itotaka/](http://www.bekkoame.ne.jp/~itotaka/)
- **NASM, The Netwide Assembler (Simon Tatham, Julian Hall and others)**  
  [http://nasm.sourceforge.net/](http://nasm.sourceforge.net/)
- **alink (Anthony A.J. Williams)**  
  [http://alink.home.dhs.org/](http://alink.home.dhs.org/)
- **md5.c (L. Peter Deutsch)**  
  Copyright (C) 1999, 2000, 2002 Aladdin Enterprises.  All rights reserved.
- **libogg/libvorbis (Xiph.Org Foundation)**  
  [http://www.xiph.org/](http://www.xiph.org/)
  
  
  
  Copyright (c) 2002, Xiph.org Foundation
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  
  
  
  - Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
  
  
  
  - Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
  
  
  
  - Neither the name of the Xiph.org Foundation nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
  
  
  
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
  A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- **Ogg Vorbis Acceleration Project**  
  Kirikiri 2 uses, inside the Phase Vocoder, the SSE-enabled FFT code published by blacksword's Ogg Vorbis Acceleration Project.
  [http://homepage3.nifty.com/blacksword/](http://homepage3.nifty.com/blacksword/)
- **A C-program for MT19937 (Makoto Matsumoto and Takuji Nishimura)**  
  [http://www.math.keio.ac.jp/matumoto/emt.html](http://www.math.keio.ac.jp/matumoto/emt.html)
  
  
  
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
  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- **LibTomCrypt (Tom St Denis)**  
  [http://libtomcrypt.org/](http://libtomcrypt.org/)
- **AGG (Anti-Grain Geometry)**  
  [http://antigrain.com/](http://antigrain.com/)
  
  
  
  The Anti-Grain Geometry Project
  
  A high quality rendering engine for C++
  
  http://antigrain.com
  
  
  
  Anti-Grain Geometry - Version 2.3
  
  Copyright (C) 2002-2005 Maxim Shemanarev (McSeem)
  
  
  
  Permission to copy, use, modify, sell and distribute this software
  is granted provided this copyright notice appears in all copies.
  This software is provided "as is" without express or implied
  warranty, and with no claim as to its suitability for any purpose.
- **Expat**  
  [http://expat.sourceforge.net/](http://expat.sourceforge.net/)
  
  
  
  Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
  and Clark Cooper
  
  Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006 Expat maintainers.
  
  
  
  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:
  
  
  
  The above copyright notice and this permission notice shall be included
  in all copies or substantial portions of the Software.
  
  
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
- **Oniguruma**  
  [http://www.geocities.jp/kosako3/oniguruma/index_ja.html](http://www.geocities.jp/kosako3/oniguruma/index_ja.html)
  
  
  
  Copyright (c) 2002-2007  K.Kosako ( sndgk393 AT ybb DOT ne DOT jp )
  All rights reserved.
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  
  1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
  
  THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
  OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
  OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
  SUCH DAMAGE.
- **FreeType**  
  [http://www.freetype.org/](http://www.freetype.org/)
  
  Copyright 1996-2002, 2006 by David Turner, Robert Wilhelm, and Werner Lemberg
- **picojson**  
  [https://github.com/kazuho/picojson](https://github.com/kazuho/picojson)
  
  
  
  Copyright 2009 Cybozu Labs, Inc.
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:
  
  1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  
  THIS SOFTWARE IS PROVIDED BY CYBOZU LABS, INC. ``AS IS'' AND ANY EXPRESS OR
  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
  EVENT SHALL CYBOZU LABS, INC. OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  
  
  
  The views and conclusions contained in the software and documentation are
  those of the authors and should not be interpreted as representing official
  policies, either expressed or implied, of Cybozu Labs, Inc.
