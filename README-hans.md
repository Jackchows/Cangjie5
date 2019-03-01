# Cangjie5

[傳統漢字版說明](https://github.com/Jackchows/Cangjie5/blob/master/README.md)

相关项目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

原码表为[「仓颉平台 2012」](http://www.chinesecj.com/forum/viewthread.php?tid=2596)的「五仓世纪」码表。

## 目标

**本项目参考官方资料对码表进行修改，可能与其他常见仓颉输入法软件存在差异，使用前务必阅读[说明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
1. 所称「官方资料」，包括：
	1. 《第五代仓颉输入法手册》（文化传信，1999、博硕，2006）
	2. [「汉文库典」](http://hanculture.com/dic/index.php)网站（连接已失效）
	3. 朱邦复工作室《内码对照表》（含2003版五代、六代编码）
	4. 《仓颉第三代中文字母输入法》（全华，1984）、《仓颉第三代中文输入法》（全华，1994）
	5. 《标准仓颉第二代中文输入法》（全华，1983）
	6. 沈红莲女士之信函
2. 本项目：
	1. **(✓)意图**　修改字码以贴近官方资料
	2. **(✗)无意**　修改或解释官方码表中被认为不符合仓颉输入法规则的部分（明显的笔误除外）
	3. **(✓)意图**　完善字形兼容（参考官方码表为主，适当添加各地字形）
	4. **(✗)无意**　兼容全部旧字形、中国大陆、香港、台湾、日本、韩国、越南字形
	5. **(✓)意图**　根据个人主观理解制作一份码表，为大家提供一个选择
	6. **(✗)无意**　满足所有人的需求

## 内容

- **[Cangjie5.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5.txt)**<br />
码表。**一般排序**，综合考虑字频及繁简（**部分常用的简化字可能排列于传统汉字前**）。<br />
收录中日韩统一表意文字（基本区至扩展F区）字符、[中日韩兼容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)区中未见于统一汉字区的十二个字符，以及官方码表中收录的符号。<br />
同时收录以下 Unicode 区域的字符：中日韩兼容表意文字（除十二个不重复的字符）、中日韩兼容表意文字补充、康熙部首、中日韩部首补充、中日韩笔画、中日韩符号和标点（部分）、中日韩兼容标点（部分）及表意文字描述字符。**此部分字符，编码以「z」开头**（兼容汉字「zc」，部首「zr」，笔画「zs」，符号「zf」，表意文字描述字符「zi」）。<br />
- **[Cangjie5_TC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_TC.txt)**<br />
码表。**传统汉字优先**（限《常用国字标准字体表》、《次常用国字标准字体表》及《常用字字形表》范围）。<br />
收字范围与 Cangjie5.txt 相同。
- **[Cangjie5_SC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_SC.txt)**<br />
码表。**简化字优先**（限《通用规范汉字表》范围）。<br />
收字范围与 Cangjie5.txt 相同。
- **[Cangjie5_supplement.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_supplement.txt)**<br />
码表。收录以下 Unicode 区域的字符：中日韩兼容表意文字（除十二个不重复的字符）、中日韩兼容表意文字补充、康熙部首、中日韩部首补充、中日韩笔画、中日韩符号和标点（部分）、中日韩兼容标点（部分）及表意文字描述字符。此表按原始编码收录，编码不以「z」开头。<br />
- **[change_summary.md](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md)    ※请首先阅读此文档。**<br />
取码争议、字形兼容、重码字排序调整说明（仅记录 Cangjie5.txt 的排序调整）。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
码表的详细编辑记录。

## 反馈

若发现错误，可在此处[反馈](https://github.com/Jackchows/Cangjie5/issues/new)。
多谢！

## 连接
- [「仓颉之友·马来西亚」论坛](http://www.chinesecj.com/forum/forum.php)
- [「天苍人颉」论坛](http://ejsoon.win/phpbb/)
- [「仓颉输入法」Facebook 群组](https://www.facebook.com/groups/cjinput/)
- [「仓颉」百度贴吧](http://tieba.baidu.com/f?kw=%E4%BB%93%E9%A2%89)
- 「仓颉输入法」QQ 群组 [30476878](https://jq.qq.com/?_wv=1027&k=5W3qETZ)
- 「仓颉输入法」Freenode IRC 频道 [#CJDFH](https://webchat.freenode.net/?channels=%23CJDFH)
- 「仓颉输入法」Telegram 群组 [@changjei](https://t.me/changjei)