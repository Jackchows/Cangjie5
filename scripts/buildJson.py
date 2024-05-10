# -*- coding: utf8 -*-
import os
import re
import json

def buildJson(github):
    # 獲取
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    github_file = os.path.join(parent_directory,github)
    # print(str(github_file))
    if (os.path.exists(github_file)==False):                               # 若github不存在
        # print ("["+str(github)+"] does not exists.")
        print ("未找到 "+str(github_file)+"，請檢查文件是否存在")
        return
    #output_file = current_directory+'/'+'converter_output_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.json'
    #json_file = current_directory+'/'+github.replace('.txt','.json')
    json_file = os.path.join(current_directory,github.replace('.txt','.json'))

    # 開啟
    with open(github_file,'r',encoding='utf8') as gib,\
         open(json_file,'w',encoding='utf8') as jsn:
        # 寫入
        data = {}

        value_pattern = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})')
        for line in gib:
            # value_line = re.match(r'^([^\t\n\r]+)\t([a-z]{1,5})', line)    # 排除開頭的說明文字
            value_line = value_pattern.match(line)                         # 排除開頭的說明文字
            if value_line:
                value_char = value_line[1]
                value_code = value_line[2]
                if value_code in data:
                    data[value_code].append(value_char)
                else:
                    data[value_code] = [value_char]

        json_data = json.dumps(data, ensure_ascii=False, indent=2, check_circular=False)
        jsn.write(json_data)
    
    # 結束
    print("輸出文件 "+json_file)

if __name__ == "__main__":
    github = 'Cangjie5.txt'
    buildJson(github)
    github = 'Cangjie5_TC.txt'
    buildJson(github)
    github = 'Cangjie5_HK.txt'
    buildJson(github)
    github = 'Cangjie5_SC.txt'
    buildJson(github)
    github = 'Cangjie5_special.txt'
    buildJson(github)

    print("完成。")