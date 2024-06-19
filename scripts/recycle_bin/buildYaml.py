# -*- coding: utf8 -*-
import os
import re
import datetime

def buildYaml(github, yaml, description, schema_id):
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    # print(current_directory)
    github_file = os.path.join(parent_directory,github)
    yaml_file = os.path.join(current_directory,yaml)
    if (os.path.exists(github_file)==False):                               # 若github不存在
        # print ("["+str(github_file.split('\\')[-1])+"] does not exists.")
        print ("[buildYaml.py > buildYaml()]未找到 "+str(github_file)+"，請檢查文件是否存在")
        return

    with open(github_file,'r',encoding='utf8') as gib,\
         open(yaml_file,'w',encoding='utf8') as yal:

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
        value_pattern = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})')
        for line in gib:
            # value_line = re.match(r'^([^\t\n\r]+)\t([a-z]{1,5}).*$', line)    # 排除開頭的說明文字
            value_line = value_pattern.match(line)                            # 排除開頭的說明文字
            if value_line:
                value_char = value_line[1]
                value_code = value_line[2]
                new_line = str(value_char)+'\t'+str(value_code)+'\n'
                yal.write(new_line)

        # 寫入結尾
        # yaml_tail ='\n'
        # yal.write(yaml_tail)

        print("輸出文件 "+yaml_file)


if __name__ == "__main__":
    github = 'Cangjie5.txt'
    yaml = 'cangjie5.dict.yaml'
    description = '''# 一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。
'''
    schema_id = "cangjie5"
    buildYaml(github, yaml, description, schema_id)

    github = 'Cangjie5_TC.txt'
    yaml = 'cangjie5_tc.dict.yaml'
    description = '''# 傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。
'''
    schema_id = "cangjie5_tc"
    buildYaml(github, yaml, description, schema_id)

    github = 'Cangjie5_HK.txt'
    yaml = 'cangjie5_hk.dict.yaml'
    description = '''# 傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。
'''
    schema_id = "cangjie5_hk"
    buildYaml(github, yaml, description, schema_id)

    github = 'Cangjie5_SC.txt'
    yaml = 'cangjie5_sc.dict.yaml'
    description = '''# 簡化字優先，符合《通用規範漢字表》的字形將排在前面。
'''
    schema_id = "cangjie5_sc"
    buildYaml(github, yaml, description, schema_id)
    
    github = 'Cangjie5_special.txt'
    yaml = 'cangjie5_special.dict.yaml'
    description = '''# 收字較少的版本，收錄主流系統通常可以顯示的字符。
'''
    schema_id = "cangjie5_special"
    buildYaml(github, yaml, description, schema_id)

    print("完成。")