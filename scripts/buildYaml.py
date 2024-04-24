# -*- coding: utf8 -*-
import os
import re
import datetime

def buildYaml(github, yaml, description, schema_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    # print(current_directory)
    github = current_directory+'\\'+github
    yaml = current_directory+'\\'+yaml
    if (os.path.exists(github)==False):                               # 若github不存在
        print ("["+str(github.split('\\')[-1])+"] does not exists.")
        return
    else:                                                             # 若github存在
        if (os.path.exists(yaml)==False):                                 # 若yaml不存在
            print("["+str(yaml.split("\\")[-1])+"] creating.")

    gib = open(github,'r',encoding='utf8')
    yal = open(yaml,'w+',encoding='utf8')


    yal.truncate()

    # 寫入文件頭
    yaml_head ='''# encoding: utf-8
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
'''+str(description)+'''---
name: "'''+str(schema_id)+'''"
version: "'''+str(datetime.datetime.now().strftime('%Y.%m.%d'))+'''"
sort: original
use_preset_vocabulary: true
max_phrase_length: 1
columns:
  - text
  - code
  - stem
encoder:
  exclude_patterns:
    - '^x.*$'
    - '^z.*$'
  rules:
    - length_equal: 2
      formula: "AaAzBaBbBz"
    - length_equal: 3
      formula: "AaAzBaBzCz"
    - length_in_range: [4, 10]
      formula: "AaBzCaYzZz"
  tail_anchor: "'"
...

''' 
    yal.write(yaml_head)
    #print(yaml_head)

    # 寫入中間
    for line in gib:
        if re.match(r'^.*\t[a-z]{1,5}\t*.*$',line):
            this_line = line.split()
            this_char = this_line[0]
            this_code = this_line[1]
            new_line = str(this_char)+'\t'+str(this_code)+'\n'
            # new_line = str(this_char)+'\t'+str(this_code)
            yal.write(new_line)

    # 寫入結尾
#     yaml_tail ='''
# '''
#     yal.write(yaml_tail)

    # 關閉文件
    gib.close()
    yal.close()

if __name__ == "__main__":
  github = '..\Cangjie5.txt'
  yaml = 'cangjie5.dict.yaml'
  description = '''# 一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。
  '''
  schema_id = "cangjie5"
  buildYaml(github, yaml, description, schema_id)

  github = '..\Cangjie5_TC.txt'
  yaml = 'cangjie5_tc.dict.yaml'
  description = '''# 傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。
  '''
  schema_id = "cangjie5_tc"
  buildYaml(github, yaml, description, schema_id)

  github = '..\Cangjie5_HK.txt'
  yaml = 'cangjie5_hk.dict.yaml'
  description = '''# 傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。
  '''
  schema_id = "cangjie5_hk"
  buildYaml(github, yaml, description, schema_id)

  github = '..\Cangjie5_SC.txt'
  yaml = 'cangjie5_sc.dict.yaml'
  description = '''# 簡化字優先，符合《通用規範漢字表》的字形將排在前面。
  '''
  schema_id = "cangjie5_sc"
  buildYaml(github, yaml, description, schema_id)

  print("Done.")