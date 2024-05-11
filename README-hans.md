# Cangjie5

[傳統漢字版說明](https://github.com/Jackchows/Cangjie5/blob/master/README.md)

相关项目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

由[「仓颉平台 2012」](https://chinesecj.com/forum/forum.php?mod=viewthread&tid=2596)的「五仓世纪」码表修改而来。

## 下载
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.1/RimeData_20240201_Cangjie5.7z)下载适用于RIME的输入法方案文档。<br />
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.1/MSCJData_20240218_Cangjie5.7z)下载适用于替换微软仓颉码表的文档。（使用说明见[此处](http://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=194346)）

## 目标

**本项目参考官方资料对码表进行修改，可能与其他常见仓颉输入法软件存在差异，详阅[说明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
1. 本项目：
	1. **(✓)意图**　修改字码以贴近官方资料
	2. **(✗)无意**　修改或解释官方码表中被认为不符合仓颉输入法规则的部分，除非是明显的笔误
	3. **(✓)意图**　完善字形兼容。参考官方码表为主，适当添加各地字形
	4. **(✗)无意**　兼容全部旧字形、中国大陆、香港、台湾、日本、韩国、越南字形
	5. **(✓)意图**　根据个人主观理解制作一份码表，为大家提供一个选择
	6. **(✗)无意**　满足所有人的需求
2. 所称「官方资料」，包括：
	1. 《第五代仓颉输入法手册》（松岗，1993、文化传信，1999、博硕，2006）
	2. [「汉文库典」](http://chidic.eduhk.hk/)网站
	3. 朱邦复工作室《内码对照表》（含2003版五代、六代编码）
	4. 《零壹中文电脑丛书之八 仓颉第三代中文字母输入法》（全华，1984）、《零壹中文电脑丛书之九 增订版仓颉第三代中文输入法》（全华，1991）
	5. 《零壹中文电脑丛书之七 标准仓颉第二代中文输入法》（全华，1983）
	6. 沈红莲女士之信函

## 内容

- **[Cangjie5.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5.txt)**<br />
码表。**一般排序**，综合考虑字频及繁简，部分常用简化字可能排在传统汉字前面。<br />
- **[Cangjie5_TC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_TC.txt)**<br />
码表。**传统汉字优先，偏好台湾用字习惯**，符合《常用国字标准字体表》的字形将排在前面。<br />
- **[Cangjie5_HK.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_HK.txt)**<br />
码表。**传统汉字优先，偏好香港用字习惯**，符合《常用字字形表》的字形将排在前面。<br />
- **[Cangjie5_SC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_SC.txt)**<br />
码表。**简化字优先**，符合《通用规范汉字表》的字形将排在前面。<br />
**※以上四份码表收录字符相同**，包括：中日韩统一表意文字基本区至扩展I区、[兼容汉字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)区中视作统一汉字的十二个字符，以及官方码表中收录的符号。<br />
另外收录兼容汉字、部首、笔画以及其他一些形似汉字的符号。为避免与常规汉字混淆，**此部分字符编码以「z」开头**（兼容汉字「zc」，部首「zr」，笔画「zs」，表意文字描述字符「zi」，算筹符号「zn」，其他符号「zf」）。
- **[Cangjie5_supplement.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_supplement.txt)**<br />
码表。收录兼容汉字、部首、笔画以及其他一些形似汉字的符号。此表按原始编码收录，编码不以「z」开头。<br />
- **[change_summary.md](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md)**<br />
总体说明，包括取码争议、字形兼容、重码字排序调整说明。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
码表的详细编辑记录。
- **[Cangjie5_special.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_special.txt)**<br />
码表。**收字较少的版本**，收录主流系统通常可以显示的字符，包括：中日韩统一表意文字基本区（除去`U+9FF0`至`U+9FFF`）、扩展A区（除去`U+4DB6`至`U+4DBF`）、兼容汉字区中视作统一汉字的十二个字符、《通用规范汉字表》、《香港增补字符集—2016》（HKSCS）。<br />
此码表与前面几份码表更新可能不同步。

## FAQ

1. Q：此项目是「官方」码表吗？<br />
   A：不是。本项目为个人制作，非仓颉输入法官方。本项目修订过程中参考官方资料为主，遇到疑难问题有咨询沈红莲女士之意见，但并不与官方完全一致。
2. Q：有些官方编码不合理，为什么此项目不作出更正，是盲从吗？<br />
   A：仓颉输入法是自由的，朱邦复先生放弃专利，允许各界自由使用和修改。坊间对仓颉输入法有不同理解，亦衍生出许多有差异的码表。<br />
    讨论当然是好的，但最终未必能达成共识。本人没有能力，也认为没有必要追求统一。<br />
    仅就本项目而言，修订的方向是以官方资料为主，结合个人的理解。用户可以根据需要，选用任何适合自己的码表。<br />
3. Q：码表的重码字排序是如何确定的？<br />
   A：重码字排序参考了各地的常用字表以及字频数据。<br />
   「一般排序」版本假设用户繁简并用，以繁体为主，但是常用的简体字也可能排在不那么常用的繁体字之前。<br />
   「传统汉字优先」版本又分为「偏好台湾用字习惯」和「偏好香港用字习惯」两种，差异在于「群羣」等异体字的排序。<br />
   「简化字优先」版本除简体字排在前面外，符合《通用规范汉字表》的繁体字（俗称「陆标繁体」）也会排在相对前面的位置。<br />
   除此之外，粤语白话文的常用字获得了一定程度的权重加成。<br />
   显然，每个人有不同的用字习惯，重码字排序不可能同时满足所有人。用户可根据自己的需要自行调整。<br />
   以下为四个版本的排序**示例**：
   |字码|`Cangjie5.txt`|`Cangjie5_TC.txt`|`Cangjie5_HK.txt`|`Cangjie5_SC.txt`|
   |-|-|-|-|-|
   |ol|仲个|仲个|仲个|个仲|
   |srtq|群羣|群羣|羣群|群羣|
   |tknl|鄭郑鄚|鄭鄚郑|鄭鄚郑|郑鄚鄭|
   |tomg|荃荏|荏荃|荃荏|荃荏|
   |yrcru|說説|說説|説說|説說|
4. Q：为什么有些字有多个编码，字形兼容的意义何在？<br />
   A：不同地区有不同字形规范，例如「次」字的左边，香港写作「冫」，台湾写作「二」。有些码表只收录了「冫欠」的字形，即「戈一弓人」。习惯「二欠」的用户按这个字形取码「一一弓人」，就打不出字。<br />
   为了避免这种困扰，本项目兼容不同字形，使用户可以按自己习惯的字形取码。<br />
   不过，出于实用性的考量，有一些字形没有收录。例如，「今」字的「丶」也可写作「一」，后者取「人一弓」。「今」「气」「俞」都常作为汉字的右偏旁出现，三者作字身时均取码「人一弓」，产生「汽渝汵」「喻吟」等大量重码字。因此，本项目没有收录「今」的「人一弓」这一字形。
5. Q：为什么码表中很多字无法显示？<br />
   A：`Cangjie5.txt`、`Cangjie5_TC.txt`、`Cangjie5_HK.txt`、`Cangjie5_SC.txt`四份码表收录了 Unicode 中日韩统一表意文字基本区至扩展I区的所有汉字，数量为九万余。有一些扩展区的汉字，若电脑和手机系统字体不支持，就会显示为方框「□」、问号「�」或空白。<br />
   有些用户可能不会用到扩展区汉字，`Cangjie5_special.txt`只保留了主流手机、电脑系统通常可以显示的汉字，字数为三万余。<br />
   以下为不同版本的收字**示例**：
   |汉字举例|`Cangjie5_special.txt`|`Cangjie5.txt`/`Cangjie5_TC.txt`/`Cangjie5_HK.txt`/`Cangjie5_SC.txt`|备注|
   |-|-|-|-|
   |常用字|✓|✓||
   |[㗎](https://zi.tools/zi/%E3%97%8E)、[䶮](https://zi.tools/zi/%E4%B6%AE)|✓|✓|扩展A区字|
   |[𠝹](https://zi.tools/zi/%F0%A0%9D%B9)、[𡁻](https://zi.tools/zi/%F0%A1%81%BB)|✓|✓|HKSCS字|
   |[𫫇](https://zi.tools/zi/%F0%AB%AB%87)、[𩾌](https://zi.tools/zi/%F0%A9%BE%8C)|✓|✓|通用规范汉字表字|
   |[鿿](https://zi.tools/zi/%E9%BF%BF)、[𫬷](https://zi.tools/zi/%F0%AB%AC%B7)|✗|✓|新版本Unicode增收的基本区和扩展A区字，2016年之后HKSCS增收的字|
   |[𪠽](https://zi.tools/zi/%F0%AA%A0%BD)、[𰻞](https://zi.tools/zi/%F0%B0%BB%9E)|✗|✓|扩展B区至I区的其他字|

## 反馈

若发现错误，可在此处[反馈](https://github.com/Jackchows/Cangjie5/issues/new)。
多谢！
