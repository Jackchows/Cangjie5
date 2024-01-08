# Cangjie5

[简化字版说明](https://github.com/Jackchows/Cangjie5/blob/master/README-hans.md)

相關項目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

原碼表為[「倉頡平台 2012」](https://chinesecj.com/forum/forum.php?mod=viewthread&tid=2596)的「五倉世紀」碼表。

## 下載
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.0/RimeData_20231117_Cangjie5.7z)下載適用於RIME的輸入法方案文檔。<br />
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.0/MSCJData_20231117_Cangjie5.7z)下載適用於替換微軟倉頡碼表的文檔。（使用說明見[此處](http://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=194346)）

## 目標

**本項目參考官方資料對碼表進行修改，可能與其他常見倉頡輸入法軟件存在差異，使用前務必閱讀[說明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
1. 所稱「官方資料」，包括：
	1. 《第五代倉頡輸入法手冊》（松崗，1993、文化傳信，1999、博碩，2006）
	2. [「漢文庫典」](http://chidic.eduhk.hk/)網站
	3. 朱邦復工作室《內碼對照表》（含2003版五代、六代編碼）
	4. 《零壹中文電腦叢書之八 倉頡第三代中文字母輸入法》（全華，1984）、《零壹中文電腦叢書之九 增訂版倉頡第三代中文輸入法》（全華，1991）
	5. 《零壹中文電腦叢書之七 標準倉頡第二代中文輸入法》（全華，1983）
	6. 沈紅蓮女士之信函
2. 本項目：
	1. **(✓)意圖**　修改字碼以貼近官方資料
	2. **(✗)無意**　修改或解釋官方碼表中被認為不符合倉頡輸入法規則的部分（明顯的筆誤除外）
	3. **(✓)意圖**　完善字形兼容（參考官方碼表為主，適當添加各地字形）
	4. **(✗)無意**　兼容全部舊字形、中國大陸、香港、台灣、日本、韓國、越南字形
	5. **(✓)意圖**　根據個人主觀理解製作一份碼表，為大家提供一個選擇
	6. **(✗)無意**　滿足所有人的需求

## 內容

- **[Cangjie5.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5.txt)**<br />
碼表。**一般排序**，綜合考慮字頻及繁簡（**部分常用簡化字可能排列於傳統漢字前**）。<br />
收錄中日韓統一表意文字（基本區至擴展I區）字符、[兼容漢字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%9B%B8%E5%AE%B9%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)區中視作統一漢字的十二個字符，以及官方碼表中收錄的符號。<br />
另外收錄兼容漢字、部首、筆畫以及其他一些形似漢字的符號。為避免與常規漢字混淆，**此部分字符編碼以「z」開頭**（兼容漢字「zc」，部首「zr」，筆畫「zs」，表意文字描述字符「zi」，算籌符號「zn」，其他符號「zf」）。
- **[Cangjie5_TC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_TC.txt)**<br />
碼表。**傳統漢字優先**（限《常用國字標準字體表》、《次常用國字標準字體表》及《常用字字形表》範圍）。<br />
收字範圍與 Cangjie5.txt 相同。
- **[Cangjie5_SC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_SC.txt)**<br />
碼表。**簡化字優先**（限《通用規範漢字表》範圍）。<br />
收字範圍與 Cangjie5.txt 相同。
- **[Cangjie5_supplement.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_supplement.txt)**<br />
碼表。收錄兼容漢字、部首、筆畫以及其他一些形似漢字的符號。此表按原始編碼收錄，編碼不以「z」開頭。<br />
- **[change_summary.md](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md)    ※請首先閱讀此文檔。**<br />
總體說明，包括取碼爭議、字形兼容、重碼字排序調整說明。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
碼表的詳細編輯記錄。
- **[Cangjie5_special.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_special.txt)**<br />
碼表。**特別版本**，收錄主流系統可以直接顯示的字符，包括：中日韓統一表意文字基本區（除去 U+9FD1 至 U+9FFF）、擴展A區（除去 U+4DB6 至 U+4DBF）、兼容漢字區中視作統一漢字的十二個字符、《通用規範漢字表》、《香港增補字符集—2016》（HKSCS）。<br />
另外，[Change_summary.md#字形問題](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E5%AD%97%E5%BD%A2%E5%95%8F%E9%A1%8C) 中列出的多種字形，此表會盡數收錄。<br />
此碼表與前面幾份碼表更新可能不同步。

## 反饋

若發現錯誤，可在此處[反饋](https://github.com/Jackchows/Cangjie5/issues/new)。
多謝！
