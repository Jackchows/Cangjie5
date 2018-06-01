# Cangjie5

[傳統漢字版說明](https://github.com/Jackchows/Cangjie5/blob/master/README.md)

相关项目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

原码表为[「仓颉平台 2012」](http://www.chinesecj.com/forum/viewthread.php?tid=2596)的「五仓世纪」码表。

**本项目参考官方资料对码表进行修改，但无意完善仓颉输入法理论，亦无意追求客观。使用前务必阅读[说明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
本项目以 1999 版仓颉五代为基础，采纳部份 2003 版仓颉五代的修改。<br />

- **[Cangjie5.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5.txt)**<br />
码表。**一般排序**，综合考虑字频及繁简。<br />
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
争议取码、字形兼容、重码字排序调整说明（仅记录 Cangjie5.txt 的排序调整）。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
码表的详细编辑记录。

## 编辑原则

本项目主要参考以下资料：<br />
1. 《第五代仓颉输入法手册》正文中对规则的描述（简称「手册」）<br />
本项目认为「手册」阐述了仓颉输入法的基本理念和规则，但描述并不详尽。<br />
《第五代仓颉输入法手册》有两个版本，分别由文化传信和博硕文化出版，两个版本仅在列举字例上有细微差异。<br />
「手册」属于 1999 版仓颉五代。<br />
2. 《第五代仓颉输入法手册》附录码表（简称「附表」）<br />
本项目认为，与编写《手册》相比，官方在实际编写码表时对规则的考虑更为周全，因此「附表」较「手册」有更高可信度。<br />
3. [「汉文库典」](http://hanculture.com/dic/index.php)网站（简称「汉文库典」）<br />
本项目认为「汉文库典」对于大字库的考虑比「手册」和「附表」周全，但「汉文库典」存在受仓颉六代影响而出现错误的情况。<br />
《汉文库典》属于 2003 版仓颉五代。<br />
4. 《第二代仓颉输入法手册》、《第三代仓颉输入法手册》、朱邦复工作室《内码对照表》的六代编码<br />
本项目认为这些资料虽不属于仓颉五代的范围，但可体现官方的设计理念。<br />

修改编码时，将遵循以下原则：<br />
1. 某字收录于「附表」，则依「附表」取码。<br />
2. 「附表」和「手册」发生矛盾，依「附表」取码，适当设兼容码。<br />
3. 采纳「汉文库典」针对「难字」取码的修改，采纳「汉文库典」针对大字库集的修改。<br />
4. 「附表」和「汉文库典」发生矛盾，适当设兼容码，属于原则③的情况除外。<br />
5. 「手册」和「汉文库典」发生矛盾，而该字未见于「附表」，适当设兼容码。<br />
6. 取码发生争议，将参考各方观点，凭个人理解确定编码，并在[说明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)中列明理由。<br />

## 反馈错误

若发现错误，可在此处[反馈](https://github.com/Jackchows/Cangjie5/issues/new)。
另外，也会收集在下方「友情连接」各处反馈的错误。
多谢！

## 友情连接
- [「仓颉之友·马来西亚」论坛](http://www.chinesecj.com/forum/forum.php)
- [「天苍人颉」论坛](http://ejsoon.win/phpbb/)
- [「仓颉输入法」Facebook 群组](https://www.facebook.com/groups/cjinput/)
- [「仓颉」百度贴吧](http://tieba.baidu.com/f?kw=%E4%BB%93%E9%A2%89)
- 「仓颉输入法」QQ 群组 [30476878](https://jq.qq.com/?_wv=1027&k=5W3qETZ)
- 「仓颉输入法」Freenode IRC 频道 [#CJDFH](https://webchat.freenode.net/?channels=%23CJDFH)
- 「仓颉输入法」Telegram 群组 [@changjei](https://t.me/changjei)