# 台羅拼音、方音符號轉換器 Tailo-TPS-Converter
Python program to do conversion between Tailo Romanisation and Taiwan Phonetic Symbol.

Requirement
=====================
Python 2.7+

How to Use
=====================
```bash
python run.py [--safe] -i input.txt [-o] output.txt
```

Arguments
=====================
<pre>
Compulsory:
-i      Input file

Optional:
--safe  Enable unicode-safe TPS that render on most system/browser (known except iOS).
-o      Output file, output.txt by default
</pre>

### Example input.txt
<pre>
朝辭白帝彩雲間，千里江陵一日還
tiau1 su5 pek8 te7 pek8 te7 tshai2 un5 kan1,
tshian1 li2 kang1 leng5 it4 jit8 huan5
兩岸猿聲啼不住，輕舟已過萬重山
liong2 gan7 uan5 seng1 the5 put4 tsu3,
kheng1 tsiu1 i2 kue3 ban7 tiong5 san1
</pre>

### Output
<pre>
朝辭白帝彩雲間，千里江陵一日還
ㄉㄧㄠ ㄙㄨˊㄅㆤㆶ˙ㄉㆤ˫ㄅㆤㆶ˙ㄉㆤ˫ㄘㄞˋㄨㄣˊㄍㄢ ，
ㄑㄧㄢ ㄌㄧˋㄍㄤ ㄌㆤㄥˊㄧㆵㆢㄧㆵ˙ㄏㄨㄢˊ
兩岸猿聲啼不住，輕舟已過萬重山
ㄌㄧㆲˋㆣㄢ˫ㄨㄢˊㄙㆤㄥ ㄊㆤˊㄅㄨㆵㄗㄨ˪，
ㄎㆤㄥ ㄐㄧㄨ ㄧˋㄍㄨㆤ˪ㆠㄢ˫ㄉㄧㆲˊㄙㄢ 
</pre>


The MIT License (MIT)
=====================

Copyright © 2018 Lee Chun Hoe

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
