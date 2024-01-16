# Cangjie5

[简化字版说明](https://github.com/Jackchows/Cangjie5/blob/master/README-hans.md)

相關項目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

由[「倉頡平台 2012」](https://chinesecj.com/forum/forum.php?mod=viewthread&tid=2596)的「五倉世紀」碼表修改而來。

## 下載
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.0/RimeData_20231117_Cangjie5.7z)下載適用於RIME的輸入法方案文檔。<br />
[按此](https://github.com/Jackchows/Cangjie5/releases/download/v3.0/MSCJData_20231117_Cangjie5.7z)下載適用於替換微軟倉頡碼表的文檔。（使用說明見[此處](http://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=194346)）

## 目標

**本項目參考官方資料對碼表進行修改，可能與其他常見倉頡輸入法軟件存在差異，詳閱[說明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E4%B8%BB%E8%A6%81%E6%94%B9%E7%A2%BC%E8%AA%AA%E6%98%8E%E5%8F%8A%E7%88%AD%E8%AD%B0%E5%8F%96%E7%A2%BC)。**<br />
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
收字範圍與`Cangjie5.txt`相同。
- **[Cangjie5_SC.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_SC.txt)**<br />
碼表。**簡化字優先**（限《通用規範漢字表》範圍）。<br />
收字範圍與`Cangjie5.txt`相同。
- **[Cangjie5_supplement.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_supplement.txt)**<br />
碼表。收錄兼容漢字、部首、筆畫以及其他一些形似漢字的符號。此表按原始編碼收錄，編碼不以「z」開頭。<br />
- **[change_summary.md](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md)**<br />
總體說明，包括取碼爭議、字形兼容、重碼字排序調整說明。
- **[change_details.log](https://github.com/Jackchows/Cangjie5/blob/master/change_details.log)**<br />
碼表的詳細編輯記錄。
- **[Cangjie5_special.txt](https://github.com/Jackchows/Cangjie5/blob/master/Cangjie5_special.txt)**<br />
碼表。**特別版本**，收錄主流系統通常可以顯示的字符，包括：中日韓統一表意文字基本區（除去`U+9FD1`至`U+9FFF`）、擴展A區（除去`U+4DB6`至`U+4DBF`）、兼容漢字區中視作統一漢字的十二個字符、《通用規範漢字表》、《香港增補字符集—2016》（HKSCS）。<br />
另外，[Change_summary.md#字形問題](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#%E5%AD%97%E5%BD%A2%E5%95%8F%E9%A1%8C) 中列出的多種字形，此表會盡數收錄。<br />
此碼表與前面幾份碼表更新可能不同步。

## FAQ

1. Q：此項目是「官方」碼表嗎？<br />
   A：不是。本項目為個人製作，非倉頡輸入法官方。本項目修訂過程中參考官方資料為主，遇到疑難問題有諮詢沈紅蓮女士之意見，但並不與官方完全一致。
2. Q：有些官方編碼不合理，為甚麼此項目不作出更正，是盲從嗎？<br />
   A：倉頡輸入法是自由的，朱邦復先生放棄專利，允許各界自由使用和修改。坊間對倉頡輸入法有不同理解，亦衍生出許多有差異的碼表。<br />
    討論當然是好的，但最終未必能達成共識。本人沒有能力，也認為沒有必要追求統一。<br />
    僅就本項目而言，修訂的方向是以官方資料為主，結合個人的理解。用戶可以根據需要，選用任何適合自己的碼表。<br />
3. Q：碼表的重碼字排序是如何確定的？<br />
   A：重碼字排序參考了各地的常用字表以及字頻數據。<br />
   「一般排序」版本假設用戶繁簡並用，以繁體為主，但是常用的簡體字也可能排在不那麼常用的繁體字之前。<br />
   「傳統漢字優先」和「簡化字優先」版本分別針對使用繁體和簡體為主的用戶。<br />
   除此之外，粵語白話文的常用字獲得了一定程度的權重加成。<br />
   顯然，每個人有不同的用字習慣，重碼字排序不可能同時滿足所有人。用戶可根據自己的需要自行調整。<br />
   以下為三個版本的排序**示例**，供參考：
   |字碼|一般排序|傳統漢字優先|簡化字優先|
   |-|-|-|-|
   |ol|仲个|仲个|个仲|
   |tk|关艾|艾关|关艾|
   |tknl|鄭郑鄚|鄭鄚郑|郑鄚鄭|
4. Q：為甚麼有些字有多個編碼，字形兼容的意義何在？<br />
   A：不同地區有不同字形規範，例如「次」字的左邊，香港寫作「冫」，台灣寫作「二」。有些碼表只收錄了「冫欠」的字形，即「戈一弓人」。習慣「二欠」的用戶按這個字形取碼「一一弓人」，就打不出字。<br />
   為了避免這種困擾，本項目兼容不同字形，使用戶可以按自己習慣的字形取碼。<br />
   不過，出於實用性的考量，有一些字形沒有收錄。例如，「今」字的「丶」也可寫作「一」，後者取「人一弓」。「今」「气」「俞」都常作為漢字的右偏旁出現，三者作字身時均取碼「人一弓」，產生「汽渝汵」「喻吟」等大量重碼字。因此，本項目沒有收錄「今」的「人一弓」這一字形。
5. Q：為甚麼碼表中很多字無法顯示？<br />
   A：`Cangjie5.txt`、`Cangjie5_TC.txt`、`Cangjie5_SC.txt`三份碼表收錄了 Unicode 中日韓統一表意文字基本區至擴展I區的所有漢字，數量為九萬餘。有一些擴展區的漢字，若電腦和手機系統字體不支持，就會顯示為方框「□」、問號「�」或空白。<br />
   有些用戶可能不會用到擴展區漢字，`Cangjie5_special.txt`只保留了主流手機、電腦系統通常可以顯示的漢字，字數為三萬餘。<br />
   以下為兩個版本的收字**示例**，供參考：
   |漢字|`Cangjie5_special.txt`|`Cangjie5.txt`/`Cangjie5_TC.txt`/`Cangjie5_SC.txt`|備註|
   |-|-|-|-|
   |常用字|✓|✓||
   |[㗎](https://zi.tools/zi/%E3%97%8E)、[䶮](https://zi.tools/zi/%E4%B6%AE)|✓|✓|擴展A區字|
   |[𠝹](https://zi.tools/zi/%F0%A0%9D%B9)、[𡁻](https://zi.tools/zi/%F0%A1%81%BB)|✓|✓|HKSCS字|
   |[𫫇](https://zi.tools/zi/%F0%AB%AB%87)、[𩾌](https://zi.tools/zi/%F0%A9%BE%8C)|✓|✓|通用規範漢字表字|
   |[鿫](https://zi.tools/zi/%E9%BF%AB)、[鿬](https://zi.tools/zi/%E9%BF%AC)|✗|✓|新版本Unicode增收的基本區和擴展A區字|
   |[𪠽](https://zi.tools/zi/%F0%AA%A0%BD)、[𰻞](https://zi.tools/zi/%F0%B0%BB%9E)|✗|✓|擴展B區至I區的其他字|

## 反饋

若發現錯誤，可在此處[反饋](https://github.com/Jackchows/Cangjie5/issues/new)。
多謝！
