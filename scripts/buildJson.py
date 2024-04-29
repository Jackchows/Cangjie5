# -*- coding: utf8 -*-
import os
import re
import json

def buildJson(github):
    # 獲取
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    github_file = parent_directory+'\\'+github
    # print(str(github_file))
    if (os.path.exists(github_file)==False):                               # 若github不存在
        print ("["+str(github)+"] does not exists.")
        return
    #output_file = current_directory+'\\'+'converter_output_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.json'
    json_file = current_directory+'\\'+github.replace('.txt','.json')

    # 開啟
    gib = open(github_file,'r',encoding='utf8')
    jsn = open(json_file,'w+',encoding='utf8')
    jsn.truncate()
  
    # 寫入
    data = {}
    for line in gib:
        if re.match(r'^.*\t[a-z]{1,5}\t*.*$',line):
            this_line = line.split()
            this_char = this_line[0]
            this_code = this_line[1]
            if this_code in data:
                data[this_code].append(this_char)
            else:
                data[this_code] = [this_char]

    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    jsn.write(json_data)

    # 關閉
    gib.close()
    jsn.close()
    
    print("輸出文件為 "+json_file)

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