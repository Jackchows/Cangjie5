# -*- coding: utf8 -*-
import os
import re
import datetime
import argparse
import platform

def chooseSource(source=None):                                    # 輸入文件
    if source is None:                                              # 如果沒有使用--source參數，則交互式提示
        print("此工具可以將碼表轉換成所需的格式，你可以選擇字和倉頡碼的順序、分隔符以及換行符。")
        print("\nStep 1 - 選擇需要轉換的文件")
        print("[1] Cangjie5.txt")
        print("[2] Cangjie5_TC.txt")
        print("[3] Cangjie5_HK.txt")
        print("[4] Cangjie5_SC.txt")
        print("[5] Cangjie5_special.txt")
        source_input=input("輸入數字並按Enter (默認為1):")
        if source_input=='':
            source='Cangjie5.txt'
        elif source_input=='1':
            source='Cangjie5.txt'
        elif source_input=='2':
            source='Cangjie5_TC.txt'
        elif source_input=='3':
            source='Cangjie5_HK.txt'
        elif source_input=='4':
            source='Cangjie5_SC.txt'
        elif source_input=='5':
            source='Cangjie5_special.txt'
        else:
            print("輸入有誤")
            exit()
    return source

def chooseOrder(order=None):                                      # 順序
    if order is None:                                               # 如果沒有使用--order參數，則交互式提示
        print("\nStep 2 - 選擇字和倉頡碼的順序")
        print("[1] 字在前，倉頡碼在後")
        print("[2] 倉頡碼在前，字在後")
        order_input=input("輸入數字並按Enter (默認為1):")
        if order_input=='':
            order='char'
        elif order_input=='1':
            order='char'
        elif order_input=='2':
            order='code'
        else:
            print("輸入有誤")
            exit()
    elif order.lower()=='char':                                             # 如果有使用--order參數，則進行判斷
        order='char'
    elif order.lower()=='code':
        order='code'
    else:
        print("--order 參數有誤 [char=字在前, code=倉頡碼在前]")
        exit()
    return order

def chooseDelimiter(delimiter=None):                              # 分隔符
    # print("--delimiter accessed ["+delimiter+']')
    if delimiter is None:                                           # 如果沒有使用--delimiter參數，則交互式提示
        print("\nStep 3 - 選擇字與倉頡碼之間的分隔符")
        print("[1] Tab")
        print("[2] Space (一個空格)")
        print("[3] Spaces (以空格代替Tab對齊)")
        print("[4] (無)")
        delimiter_input=input("輸入數字並按Enter (默認為1):")
        if delimiter_input=='':
            delimiter='\t'
        elif delimiter_input=='1':
            delimiter='\t'
        elif delimiter_input=='2':
            delimiter=' '
        elif delimiter_input=='3':
            delimiter="spaces"
        elif delimiter_input=='4':
            delimiter=''
        else:
            print("輸入有誤")
            exit()
    elif delimiter.lower()=='tab':                                          # 如果有使用--delimiter參數，則進行判斷
        delimiter='\t'
    elif delimiter.lower()=='space':
        delimiter=' '
    elif delimiter.lower()=='multi':
        delimiter="spaces"
    elif delimiter.lower()=='none':
        delimiter=''
    # elif delimiter.lower()=='':
    #     delimiter=''
    else:
        print("--delimiter after ["+delimiter+']')
        print("--delimiter 參數有誤 [tab=製表鍵, space=一個空格, multi=以空格代替Tab對齊, none=無]")
        exit()
    return delimiter

def chooseLineBreak(linebreak=None):                              # 換行符
    system_version=platform.system().lower()                        # 判斷當前系統
    # mac_version=float('.'.join(platform.mac_ver().split('.')[:2]))  # macOS版本號
    mac_version = 100
    if linebreak is None:                                           # 命令行沒有使用--linebreak參數，則交互式提示
        print("\nStep 4 - 選擇輪出文件的換行符")
        print("[1] \\r\\n")
        print("[2] \\n")
        print("[3] \\r")
        if system_version=='windows':
            linebreak_input=input("輸入數字並按Enter (Windows默認為1):")
        elif system_version=='linux':
            linebreak_input=input("輸入數字並按Enter (Unix/Linux默認為2):")
        elif system_version=='darwin' and mac_version>=10.8:
            linebreak_input=input("輸入數字並按Enter (macOS(OS X)默認為2):")
        elif system_version=='darwin' and mac_version<10.8:
            linebreak_input=input("輸入數字並按Enter (Mac OS默認為3):")
        else:
            linebreak_input=input("輸入數字並按Enter (默認為1):")
        if linebreak_input=='' and system_version=='windows':
            linebreak="\r\n"
        elif linebreak_input=='' and system_version=='linux':
            linebreak="\n"
        elif linebreak_input=='' and system_version=='darwin':
            linebreak="\r"
        elif linebreak_input=='':
            linebreak="\r\n"
        elif linebreak_input=='1':
            linebreak="\r\n"
        elif linebreak_input=='2':
            linebreak="\n"
        elif linebreak_input=='3':
            linebreak="\r"
        else:
            print("輸入有誤")
            exit()
    elif linebreak=='auto':                                         # GUI選擇[與系統一致]，則執行判斷
        if system_version=='windows':
            linebreak="\r\n"
        elif system_version=='linux':
            linebreak="\n"
        elif system_version=='darwin':
            linebreak="\r"
        else:
            linebreak="\r\n"
    elif linebreak.lower()=='crlf':                                 # 命令行有使用--linebreak參數，則進行判斷
        linebreak="\r\n"
    elif linebreak.lower()=='cr':
        linebreak="\r"
    elif linebreak.lower()=='lf':
        linebreak="\n"
    else:
        #print('[DEBUG]linebreak='+linebreak)
        print("--linebreak 參數有誤 [crlf, cr, lf, auto]")
        exit()
    return linebreak

def buildTxt(source,order,delimiter,linebreak,build_with_template,output=None):                   # 默認不使用模板

    # 獲取
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    source_file = os.path.join(parent_directory,source)
    if (os.path.exists(source_file)==False):                               # 若source_file不存在
            print ("未找到 "+str(source_file)+"，請檢查文件是否存在")
            return('ERR_SOURCE_FILE_NOT_EXISTS')
    #output_file = current_directory+'\\'+'converter_output_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.txt'
    # if output is None:
    #     output_file = os.path.join(current_directory,source.replace('.txt','_formatted.txt'))    # 不使用模板
    # else:
    #     output_file = output                                                                     # 使用模板
    if output:
        if os.path.isabs(output):
            output_file = output  
        else:
            output_file = os.path.join(current_directory,output)
    else:
        output_file = os.path.join(current_directory,source.replace('.txt','_formatted.txt'))

    # 開啟
    with open(source_file,'r',encoding='utf8') as gib, \
         open(output_file,'a',encoding='utf8',newline='') as txt:
        if build_with_template == 'no':                                                     # 不使用模板
            txt.seek(0,0)
            txt.truncate()
        # value_pattern = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})')
        check_source_file_format_result = checkSourceFileFormat(source)     # 檢查源文件格式是否符合要求
        if(check_source_file_format_result=='no'):
            print('不支持的源文件格式')
            exit()
        else:
            value_pattern = check_source_file_format_result[1]
            char_first_confirmed = check_source_file_format_result[2]
        # 寫入
        for line in gib:
            #value_line = re.match(r'^([^\t\n\r]+)\t([a-z]{1,5}).*$', line)    # 排除開頭的說明文字
            value_line = value_pattern.match(line)                            # 排除開頭的說明文字
            if value_line:
                if char_first_confirmed:                            # 源碼表先字後碼
                    value_char = value_line[1]
                    value_code = value_line[2]
                else:
                    value_char = value_line[2]                      # 源碼表先碼後字
                    value_code = value_line[1]
                # print('ok   order='+order)
                if order=='char':                                              # 輸出碼表先字後碼
                    if delimiter=="spaces":
                        new_delimiter=' ' * 6                                    # 以空格代替tab對齊
                    else:
                        new_delimiter=delimiter
                    new_line = str(value_char)+new_delimiter+str(value_code)+linebreak
                elif order=='code':                                            # 輸出碼表先碼後字
                    if delimiter=="spaces":
                        new_delimiter=' ' * (8 - len(value_code))                # 以空格代替tab對齊
                    else:
                        new_delimiter=delimiter
                    new_line = str(value_code)+new_delimiter+str(value_char)+linebreak
                txt.write(new_line)
                
    # 關閉
    if __name__ == "__main__":                                      # 如果是被引用則不輸出提示
        print("完成。輸出文件 "+os.path.abspath(output_file))
    #input("按Enter退出")
    return('SUCCESS')

def buildYaml(source,template,output):                                               # RIME 模板

    if output:
        if os.path.isabs(output):
            yaml_file = output
        else:
            yaml_file = os.path.join(current_directory,output)
    else:
        yaml_file = os.path.join(current_directory,source.replace('.txt','.dict.yaml').lower())
    if (os.path.exists(source)==False):                               # 若source_file不存在
        print ("未找到 "+str(source)+"，請檢查文件是否存在")
        return('ERR_SOURCE_FILE_NOT_EXISTS')
    if template == 'weasel':
        linebreak="\r\n"
    elif template == 'squirrel':
        linebreak="\r"
    elif template == 'rime':
        linebreak="\n"
    order = 'char'
    delimiter = '\t'
    build_with_template = 'yes'

    supported_file_name_cj5 = ['Cangjie5.txt','Cangjie5_TC.txt','Cangjie5_HK.txt','Cangjie5_SC.txt','Cangjie5_special.txt']
    supported_file_name_cj3 = ['cj3.txt','cj3-30000.txt','cj3-special.txt']
    description_dict = {}
    description_dict['Cangjie5.txt']='一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。'
    description_dict['Cangjie5_TC.txt']='傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。'
    description_dict['Cangjie5_HK.txt']='傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。'
    description_dict['Cangjie5_SC.txt']='簡化字優先，符合《通用規範漢字表》的字形將排在前面。'
    description_dict['Cangjie5_special.txt']='收字較少的版本，收錄主流系統通常可以顯示的字符。'
    
    schema_id = os.path.basename(source).replace('.txt','').lower()
    if os.path.basename(source) in supported_file_name_cj3:             # schema_id 如果是三代補完計劃
        schema_id = 'cangjie3'
    if os.path.basename(source) in supported_file_name_cj5:             # description 如果是五代補完計劃
        description = description_dict[os.path.basename(source)]
    else:                                                               # 如果是其他碼表
        description = ''
    # print('[DEBUG]source='+source)
    # print('[DEBUG]os.path.basename(source)='+os.path.basename(source))
    # 開頭
    #region yaml_head
    yaml_head_cj5 ='''# encoding: utf-8
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
# '''+str(description)+'''
---
'''
    yaml_head_cj3 ='''# encoding: utf-8
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
'''
    yaml_head_2 ='''name: "'''+str(schema_id)+'''"
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

    if os.path.basename(source) in supported_file_name_cj5:                 # yaml_head 如果是五代補完計劃
        yaml_head = yaml_head_cj5 + yaml_head_2
    elif os.path.basename(source) in supported_file_name_cj3:               # 如果是三代補完計劃
        yaml_head = yaml_head_cj3 + yaml_head_2
    else:                                                                   # 如果是其他碼表
        description = ''
        yaml_head = yaml_head_2
    #endregion
    # 寫入yaml
    with open(yaml_file,'w',encoding='utf8') as yal:
        yal.write(yaml_head)
    buildTxt(source,order,delimiter,linebreak,build_with_template,yaml_file)
    return('SUCCESS')
    
def buildYong(source,output):                                                        # 小小輸入法模板
    print('[332]source='+source)
    if (os.path.exists(source)==False):                               # 若source_file不存在
        print ("未找到 "+str(source)+"，請檢查文件是否存在")
        return('ERR_SOURCE_FILE_NOT_EXISTS')

    if output:
        if os.path.isabs(output):
            yong_file = output
        else:
            yong_file = os.path.join(current_directory,output)
    else:
        yong_file = os.path.join(current_directory,source.replace('.txt','_yong.txt'))

    linebreak="\r\n"
    order = 'code'
    delimiter = 'spaces'
    build_with_template = 'yes'

    supported_file_name_cj5 = ['Cangjie5.txt','Cangjie5_TC.txt','Cangjie5_HK.txt','Cangjie5_SC.txt','Cangjie5_special.txt']
    supported_file_name_cj3 = ['cj3.txt','cj3-30000.txt','cj3-special.txt']
    description_dict = {}
    description_dict['Cangjie5.txt']='一般排序，綜合考慮字頻及繁簡，部分常用簡化字可能排在傳統漢字前面。'
    description_dict['Cangjie5_TC.txt']='傳統漢字優先，偏好台灣用字習慣，符合《常用國字標準字體表》的字形將排在前面。'
    description_dict['Cangjie5_HK.txt']='傳統漢字優先，偏好香港用字習慣，符合《常用字字形表》的字形將排在前面。'
    description_dict['Cangjie5_SC.txt']='簡化字優先，符合《通用規範漢字表》的字形將排在前面。'
    description_dict['Cangjie5_special.txt']='收字較少的版本，收錄主流系統通常可以顯示的字符。'
    schema_id = os.path.basename(source).replace('.txt','').lower()

    if os.path.basename(source) in supported_file_name_cj5:                 # description 如果是五代補完計劃
        description = description_dict[os.path.basename(source)]
        name='倉頡五代'
    elif os.path.basename(source) in supported_file_name_cj3:                 # description 如果是三代補完計劃
        description = ''
        name='倉頡三代'
    else:                                                               # 如果是其他碼表
        description = ''
        name=schema_id

    # 開頭
    yong_head_cj5 ='''#-----------------------------------------------------------------
# 倉頡五代補完計劃：
# https://github.com/Jackchows/Cangjie5
# 使用前務必閱讀：
# https://github.com/Jackchows/Cangjie5/blob/master/README.md 及
# https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md
#
# 相關項目：倉頡三代補完計畫
# https://github.com/Arthurmcarthur/Cangjie3-Plus
#
# '''+description+'''
#-----------------------------------------------------------------
'''
    yong_head_2 ='''encode=UTF-8
name='''+name+'''
key=abcdefghijklmnopqrstuvwxyz
len=6
wildcard=*
commit=1 6 0
#dicts=mb/cj5-ftzk.txt
#dicts=mb/cj5-jtzk.txt
#assist=mb/assist/pinyin.txt

[DATA]
'''

    if os.path.basename(source) in supported_file_name_cj5:                 # yong_head 如果是五代補完計劃
        yong_head = yong_head_cj5 + yong_head_2
    else:                                                               # 如果是其他碼表
        description = ''
        yong_head = yong_head_2

    # 寫入yong
    with open(yong_file,'w',encoding='utf8') as yog:
        yog.write(yong_head)
    buildTxt(source,order,delimiter,linebreak,build_with_template,yong_file)
    return('SUCCESS')

def buildFcitx(source,output):                                                       # Fcitx 5 模板
    if (os.path.exists(source)==False):                               # 若source_file不存在
        print ("未找到 "+str(source)+"，請檢查文件是否存在")
        return('ERR_SOURCE_FILE_NOT_EXISTS')
    
    if output:
        if os.path.isabs(output):
            fcitx_file = output
        else:
            fcitx_file = os.path.join(current_directory,output)
    else:
        fcitx_file = os.path.join(current_directory,source.replace('.txt','_fcitx.txt'))
    linebreak="\n"
    order = 'code'
    delimiter = ' '
    build_with_template = 'yes'
    fcitx_head ='''键码=abcdefghijklmnopqrstuvwxyz
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
'''
    # 寫入fcitx
    with open(fcitx_file,'w',encoding='utf8',newline = '\n') as fcx:
        fcx.write(fcitx_head.replace('\r\n','\n'))
    buildTxt(source,order,delimiter,linebreak,build_with_template,fcitx_file)
    return('SUCCESS')

def buildWithTemplate(template,source,output):                                  # 判斷是否使用模板
    global build_with_template
    if template is None:
        build_with_template = 'no'
    elif template == 'rime':
        buildYaml(source,template,output)
        build_with_template = 'yes'
    elif template == 'weasel':
        buildYaml(source,template,output)
        build_with_template = 'yes'
    elif template == 'squirrel':
        buildYaml(source,template,output)
        build_with_template = 'yes'
    elif template == 'fcitx':
        buildFcitx(source,output)
        build_with_template = 'yes'
    elif template == 'yong':
        buildYong(source,output)
        build_with_template = 'yes'
    else:
        print("--template 參數有誤 [rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]")
        build_with_template = 'error'
    
def checkSourceFileFormat(source_file):
    # 判斷source_file格式
    value_pattern_type = ['value_pattern_1_char_tab_code', 'value_pattern_2_char_space_code',
                          'value_pattern_3_code_tab_char', 'value_pattern_4_code_space_char']   # 別名
    value_pattern_match_num = {}
    for type in value_pattern_type:
        value_pattern_match_num[type] = 0   # 匹配的數量
    value_pattern_rule = {}                 # 規則，re.compile對象
    value_pattern_rule['value_pattern_1_char_tab_code']   = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})')    #字tab碼
    value_pattern_rule['value_pattern_2_char_space_code'] = re.compile(r'^([^\t\n\r]+) +([a-z]{1,5})')    #字space碼
    value_pattern_rule['value_pattern_3_code_tab_char']   = re.compile(r'^([a-z]{1,5})\t([^\t\n\r]+)')    #碼tab字
    value_pattern_rule['value_pattern_4_code_space_char'] = re.compile(r'^([a-z]{1,5}) +([^\t\n\r]+)')    #碼space字
    # value_pattern_char_tab_code = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\u20000-\u2cebf\u30000-\u323af\u2f800-\u2fa1f]+\t([a-z]{1,5})')
    with open(source_file,'r',encoding='utf8') as gib:
        for i, line in enumerate(gib):
            for type in value_pattern_type:                         # 對四款正則表達式遍歷, 看哪種匹配最多
                value_line = value_pattern_rule[type].match(line)
                if value_line:
                    value_pattern_match_num[type] = value_pattern_match_num[type] + 1
            if i>1000:
                break
    value_pattern_confirmed = False
    # for type in value_pattern_type:
    #     print('type='+type+', num='+str(value_pattern_match_num[type]))
    for type in value_pattern_type:
        if value_pattern_match_num[type] > 800:                     # 超過800行匹配則確認是這種格式, 預留一些非字碼的行
            value_pattern = value_pattern_rule[type]
            if type in ['value_pattern_1_char_tab_code', 'value_pattern_2_char_space_code']:
                char_first_confirmed = True
            elif type in ['value_pattern_3_code_tab_char', 'value_pattern_4_code_space_char']:
                char_first_confirmed = False
            value_pattern_confirmed = True
    if value_pattern_confirmed:
        return(['yes',value_pattern,char_first_confirmed])
    else:
        return(['no'])


def parse_args():
    parse = argparse.ArgumentParser(description='參數')
    parse.add_argument('-s', '--source', help='需要轉換的源文件，如[Cangjie5.txt]')  # 創建參數
    parse.add_argument('-f', '--filename', help='轉換輸出的文件名稱')
    parse.add_argument('-o', '--order', help='字和倉頡碼的順序[char=字在前, code=倉頡碼在前]')
    parse.add_argument('-d', '--delimiter', help='分隔符[tab=製表鍵, space=一個空格, multi=以空格代替Tab對齊, none=無]')
    parse.add_argument('-l', '--linebreak', help='換行符[crlf, cr, lf, auto=與系統一致]')
    parse.add_argument('-t', '--template', help='使用模板[rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]')
    # parse.add_argument('--release', action='store_true', help='發佈')
    args = parse.parse_args()                   # 解析參數
    return args

if __name__ == "__main__":
    args = parse_args()                         # 處理參數
    source = args.source
    order = args.order
    delimiter = args.delimiter
    linebreak = args.linebreak
    template = args.template
    output = args.filename

    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    
    # if release:
    #     print("To release")
    #     buildRelease()
    #     exit()

    build_with_template = 'no'  # 是否使用了模板

    if template:
        if (order is not None) | (delimiter is not None) | (linebreak is not None):
            print('--template 參數衹可以與 --source, --filename 參數共用')
            exit()
        elif source is None:
            print('--template 參數需要與 --source 參數共用')
            exit()

    buildWithTemplate(template,source,output)   # 判斷是否使用模板

    if build_with_template == 'no':                     # 不使用模板
        source=chooseSource(source)
        order=chooseOrder(order)
        delimiter=chooseDelimiter(delimiter)
        linebreak=chooseLineBreak(linebreak)
        buildTxt(source,order,delimiter,linebreak,build_with_template,output)

    