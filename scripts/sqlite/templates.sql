DROP TABLE IF EXISTS templates;
CREATE TABLE "templates"(
    "key"    TEXT,
    "value"  BLOB
);
CREATE INDEX "idx_templates_key" ON "templates"("key");

-- #region yaml_head_cj5_norm
INSERT INTO templates VALUES ('yaml_head_cj5_norm',
'# encoding: utf-8
#
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
# 
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。
---
name: "cangjie5"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...

');
-- #endregion

-- #region yaml_head_cj5_tc
INSERT INTO templates VALUES ('yaml_head_cj5_tc',
'# encoding: utf-8
#
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
# 
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。
---
name: "cangjie5_tc"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...

');
-- #endregion

-- #region yaml_head_cj5_hk
INSERT INTO templates VALUES ('yaml_head_cj5_hk',
'# encoding: utf-8
#
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
# 
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。
---
name: "cangjie5_hk"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...

');
-- #endregion

-- #region yaml_head_cj5_sc
INSERT INTO templates VALUES ('yaml_head_cj5_sc',
'# encoding: utf-8
#
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
# 
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 簡化字優先，符合《通用規範漢字表》的字形將排在前面。
---
name: "cangjie5_sc"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...

');
-- #endregion

-- #region yaml_head_cj5_special
INSERT INTO templates VALUES ('yaml_head_cj5_special',
'# encoding: utf-8
#
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
# 
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 收字較少的版本，收錄主流系統通常可以顯示的字符。
---
name: "cangjie5_special"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...
');
-- #endregion

-- #region yaml_head_cj3
INSERT INTO templates VALUES ('yaml_head_cj3',
'# encoding: utf-8
#
# 倉頡三代補完計畫
#
#
# 說明：
# 倉頡三代補完計畫
# 專案網址：https://github.com/Arthurmcarthur/Cangjie3-Plus
# 相關項目：倉頡五代補完計畫
# 專案網址：https://github.com/Jackchows/Cangjie5
#

---
name: "cangjie3"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...
');
-- #endregion

-- #region yaml_head_other
INSERT INTO templates VALUES ('yaml_head_other',
'# encoding: utf-8
---
name: "{NAME}"
version: "{VERSION}"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - ''^x.*$''
    - ''^z.*$''
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "''"
...
');
-- #endregion

-- #region yong_head_cj5_norm
INSERT INTO templates VALUES ('yong_head_cj5_norm',
'#-----------------------------------------------------------------
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
#
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。
#-----------------------------------------------------------------
encode=UTF-8
name=倉頡五代
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
');
-- #endregion

-- #region yong_head_cj5_tc
INSERT INTO templates VALUES ('yong_head_cj5_tc',
'#-----------------------------------------------------------------
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
#
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。
#-----------------------------------------------------------------
encode=UTF-8
name=倉頡五代
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
');
-- #endregion

-- #region yong_head_cj5_hk
INSERT INTO templates VALUES ('yong_head_cj5_hk',
'#-----------------------------------------------------------------
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
#
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。
#-----------------------------------------------------------------
encode=UTF-8
name=倉頡五代
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
');
-- #endregion

-- #region yong_head_cj5_sc
INSERT INTO templates VALUES ('yong_head_cj5_sc',
'#-----------------------------------------------------------------
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
#
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# 簡化字優先，符合《通用規範漢字表》的字形將排在前面。
#-----------------------------------------------------------------
encode=UTF-8
name=倉頡五代
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
');
-- #endregion

-- #region yong_head_other
INSERT INTO templates VALUES ('yong_head_other',
'encode=UTF-8
name={NAME}
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
');
-- #endregion

-- #region fcitx_head
INSERT INTO templates VALUES ('fcitx_head',
'键码=abcdefghijklmnopqrstuvwxyz
提示=&
码长=6
[数据]
&a 日
&b 月
&c 金
&d 木
&e 水
&f 火
&g 土
&h 竹
&i 戈
&j 十
&k 大
&l 中
&m 一
&n 弓
&o 人
&p 心
&q 手
&r 口
&s 尸
&t 廿
&u 山
&v 女
&w 田
&x 難
&y 卜
&z 片
');
-- #endregion

COMMIT;