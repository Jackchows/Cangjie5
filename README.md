# Cangjie5

**[2018-09-25] 有朋友正計劃去信官方提問規則和編碼問題，有興趣的朋友可在[此處](https://zh.wikibooks.org/wiki/Talk:%E5%80%89%E9%A0%A1%E8%BC%B8%E5%85%A5%E6%B3%95/%E4%BF%A1%E5%87%BD)參與討論。（[邀请函](https://github.com/Jackchows/Cangjie5/issues/128)）**

##
[简化字版说明](https://github.com/Jackchows/Cangjie5/blob/master/README-hans.md)

相關項目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

原碼表為[「倉頡平台 2012」](http://www.chinesecj.com/forum/viewthread.php?tid=2596)的「五倉世紀」碼表。

**本項目參考官方資料對碼表進行修改，但無意完善倉頡輸入法理論，亦無意追求客觀。使用前務必閱讀[說明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
本項目以 1999 版倉頡五代為基礎，採納部份 2003 版倉頡五代的修改。<br />

**※注意，本項目的目標不包括以下各項：**
1. 修改官方碼表中被認為不符合倉頡輸入法規則的部份（明顯的筆誤除外）。
2. 添加官方碼表未支持的字形兼容（但並非不能添加）。

- **[Cangjie5.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5.txt)**<br />
碼表。**一般排序**，綜合考慮字頻及繁簡。<br />
收錄中日韓統一表意文字（基本區至擴展F區）字符、[中日韓兼容表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)區中未見於統一漢字區的十二個字符，以及官方碼表中收錄的符號。<br />
同時收錄以下 Unicode 區域的字符：中日韓兼容表意文字（除十二個不重複的字符）、中日韓兼容表意文字補充、康熙部首、中日韓部首補充、中日韓筆畫、中日韓符號和標點（部分）、中日韓兼容標點（部分）及表意文字描述字符。**此部分字符，編碼以「z」開頭**（兼容漢字「zc」，部首「zr」，筆畫「zs」，符號「zf」，表意文字描述字符「zi」）。<br />
- **[Cangjie5_TC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_TC.txt)**<br />
碼表。**傳統漢字優先**（限《常用國字標準字體表》、《次常用國字標準字體表》及《常用字字形表》範圍）。<br />
收字範圍與 Cangjie5.txt 相同。
- **[Cangjie5_SC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_SC.txt)**<br />
碼表。**簡化字優先**（限《通用規範漢字表》範圍）。<br />
收字範圍與 Cangjie5.txt 相同。
- **[Cangjie5_supplement.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_supplement.txt)**<br />
碼表。收錄以下 Unicode 區域的字符：中日韓兼容表意文字（除十二個不重複的字符）、中日韓兼容表意文字補充、康熙部首、中日韓部首補充、中日韓筆畫、中日韓符號和標點（部分）、中日韓兼容標點（部分）及表意文字描述字符。此表按原始編碼收錄，編碼不以「z」開頭。<br />
- **[change_summary.md](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md)    ※請首先閱讀此文檔。**<br />
爭議取碼、字形兼容、重碼字排序調整說明（僅記錄 Cangjie5.txt 的排序調整）。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
碼表的詳細編輯記錄。

## 編輯原則

本項目主要參考以下資料：<br />
1. 《第五代倉頡輸入法手冊》正文中對規則的描述（簡稱「手冊」）<br />
本項目認為「手冊」闡述了倉頡輸入法的基本理念和規則，但描述並不詳盡。<br />
《第五代倉頡輸入法手冊》有兩個版本，分別由文化傳信和博碩文化出版，兩個版本僅在列舉字例上有細微差異。<br />
「手冊」屬於 1999 版倉頡五代。<br />
2. 《第五代倉頡輸入法手冊》附錄碼表（簡稱「附表」）<br />
本項目認為，與編寫《手冊》相比，官方在實際編寫碼表時對規則的考慮更為周全，因此「附表」較「手冊」有更高可信度。<br />
3. [「漢文庫典」](http://hanculture.com/dic/index.php)網站（簡稱「漢文庫典」）<br />
本項目認為「漢文庫典」對於大字庫的考慮比「手冊」和「附表」周全，但「漢文庫典」存在受倉頡六代影響而出現錯誤的情況。<br />
《漢文庫典》屬於 2003 版倉頡五代。<br />
4. 《第二代倉頡輸入法手冊》、《第三代倉頡輸入法手冊》、朱邦復工作室《內碼對照表》的六代編碼<br />
本項目認為這些資料雖不屬於倉頡五代的範圍，但可體現官方的設計理念。<br />

修改編碼時，將遵循以下原則：<br />
1. 某字收錄於「附表」，則依「附表」取碼。<br />
2. 「附表」和「手冊」發生矛盾，依「附表」取碼，適當設兼容碼。<br />
3. 採納「漢文庫典」針對「難字」取碼的修改，採納「漢文庫典」針對大字庫集的修改。<br />
4. 「附表」和「漢文庫典」發生矛盾，適當設兼容碼，屬於原則③的情況除外。<br />
5. 「手冊」和「漢文庫典」發生矛盾，而該字未見於「附表」，適當設兼容碼。<br />
6. 取碼發生爭議，將參考各方觀點，憑個人理解確定編碼，並在[說明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)中列明理由。<br />

## 反饋錯誤

若發現錯誤，可在此處[反饋](https://github.com/Jackchows/Cangjie5/issues/new)。
另外，也會收集在下方「友情連接」各處反饋的錯誤。
多謝！

## 友情連接
- [「倉頡之友·馬來西亞」論壇](http://www.chinesecj.com/forum/forum.php)
- [「天蒼人頡」論壇](http://ejsoon.win/phpbb/)
- [「倉頡輸入法」Facebook 群組](https://www.facebook.com/groups/cjinput/)
- [「倉頡」百度貼吧](http://tieba.baidu.com/f?kw=%E4%BB%93%E9%A2%89)
- 「倉頡輸入法」QQ 群組 [30476878](https://jq.qq.com/?_wv=1027&k=5W3qETZ)
- 「倉頡輸入法」Freenode IRC 頻道 [#CJDFH](https://webchat.freenode.net/?channels=%23CJDFH)
- 「倉頡輸入法」Telegram 群組 [@changjei](https://t.me/changjei)