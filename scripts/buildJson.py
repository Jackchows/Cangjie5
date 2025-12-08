import re
import json
from pathlib import Path

def buildJson(github: str):
    # 獲取
    current_directory = Path.cwd()              # 獲取文件目錄
    parent_directory = current_directory.parent # 獲取上級目錄
    github_file = parent_directory / github
    if not github_file.exists():                # 若 github 不存在
        print (f'未找到 {github_file}，請檢查文件是否存在')
        return
    # output_file = current_directory+'/'+'converter_output_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.json'
    # json_file = current_directory+'/'+github.replace('.txt','.json')
    json_file = current_directory / github.replace('.txt','.json')

    # 開啟
    with open(github_file, 'r', encoding='utf8') as gib,\
         open(json_file, 'w', encoding='utf8') as jsn:
        # 寫入
        data = {}

        value_pattern = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})')
        for line in gib:
            # value_line = re.match(r'^([^\t\n\r]+)\t([a-z]{1,5})', line)    # 排除開頭的說明文字
            if out := value_pattern.match(line): # 排除開頭的說明文字
                char, code = out[1], out[2]      # 取得輸出結果的前兩個 group
                
                if code in data:
                    data[code].append(char)
                else:
                    data[code] = [char]

        jsn.write(json.dumps(data, ensure_ascii=False, indent=2, check_circular=False))
    
    # 結束
    print(f'輸出文件 {json_file}')

if __name__ == '__main__':
    PROCESS_FILES = ('Cangjie5.txt', 'Cangjie5_TC.txt', 'Cangjie5_HK.txt', 'Cangjie5_SC.txt', 'Cangjie5_special.txt')
    
    for file in PROCESS_FILES:
        buildJson(file)

    print('完成。')