# -*- coding: utf8 -*-
# FUNCTION_RELATION
# cmd_delimiter_decode()                delimiter轉義     
# cmd_linebreak_decode()                linebreak轉義
# cmd_read_source_to_database()         將源碼表讀入數據庫
#     cmd_detect_souece_file_format()       判斷源碼表的格式
#     db_initialize()                       創建數據庫並導入基礎數據
#     db_get_setting(...)                   對比hash
#     db_truncate_cangjie_table()           清空倉頡表
#     db_insert_into_cangjie_table()        插入倉頡表
#     db_config_setting(...)                更新hash
#     db_initialize_cangjie_table()         補全倉頡表數據
#     db_count_charset()                    計算字符數量
# cmd_mark_selected_charset()            標記已選擇的字符集
#     db_build_final_table()                標記已選擇的字符集
# db_build_final_table()                生成最終碼表
# db_export_final_table()               導出最終碼表
# cmd_write_output_template()           輸出文件模板
# cmd_write_output_file()               輸出文件正文

import os
import re
import datetime
import argparse
import textwrap
import hashlib
import platform
import logging
from buildToolDatabase import db_initialize # type: ignore
from buildToolDatabase import db_get_setting # type: ignore
from buildToolDatabase import db_insert_into_cangjie_table # type: ignore
from buildToolDatabase import db_commit # type: ignore
from buildToolDatabase import db_config_setting # type: ignore
from buildToolDatabase import db_truncate_cangjie_table # type: ignore
from buildToolDatabase import db_initialize_cangjie_table # type: ignore
from buildToolDatabase import db_mark_selected_charset # type: ignore
from buildToolDatabase import db_build_final_table # type: ignore
from buildToolDatabase import db_export_final_table # type: ignore
from buildToolDatabase import db_get_template # type: ignore
from buildToolDatabase import db_count_charset # type: ignore
from buildToolDatabase import db_create_database # type: ignore

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] - %(funcName)s() - %(message)s')

'''
parse.add_argument('-o', '--order', help='字和倉頡碼的順序[char=字在前, code=倉頡碼在前]')
parse.add_argument('-d', '--delimiter', help='分隔符[tab=製表鍵, space=單個空格, multi=以空格代替Tab對齊, none=(無)]')
parse.add_argument('-l', '--linebreak', help='換行符[crlf, cr, lf, auto=與系統一致]')
parse.add_argument('-t', '--template', help='使用模板[rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]')
parse.add_argument('-c', '--charset', help=textwrap.dedent(
'''


# 輸出文件模版
def cmd_write_output_template(sqlite_cursor, output_file, template, order, delimiter, linebreak, source_basename):
    logging.debug(locals())
    # print(sqlite_cursor, output_file, template, order, delimiter, linebreak, source_basename)
    # # [rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]
    # print('cmd_write_output_template()')
    # order, delimiter, linebreak
    # 順序
    if order is None:
        if template in ['rime','weasel','squirrel']:
            order = 'char'
        elif template in ['yong','fcitx']:
            order = 'code'
    # 分隔符
    if delimiter is None:
        if template in ['rime','weasel','squirrel']:
            delimiter = 'tab'
        elif template in ['fcitx']:
            delimiter = 'space'
        elif template in ['yong']:
            delimiter = 'multi'
    # 換行符
    if linebreak is None:
        if template in ['rime','squirrel','fcitx']:
            linebreak = 'lf'
        elif template in ['weasel','yong']:
            linebreak = 'crlf'
    elif linebreak == 'auto':
        system_version=platform.system().lower()        # 判斷當前系統
        if system_version=='windows':
            linebreak="crlf"
        elif system_version=='linux':
            linebreak="lf"
        elif system_version=='darwin':
            mac_version=float('.'.join(platform.mac_ver()[0].split('.')[:2]))   # macOS版本號
            if mac_version>=10.8:
                linebreak="lf"
            else:
                linebreak="cr"
        else:
            linebreak="lf"
    # 寫入模板內容
    with open(output_file,'w',encoding='utf8',newline=cmd_linebreak_decode(linebreak)) as txt: 
        schema_id = ''
        version = str(datetime.datetime.now().strftime('%Y.%m.%d'))
        if template in ['rime','weasel','squirrel']:
            if source_basename == 'Cangjie5.txt':                                   # 五代補完
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj5_norm')
            elif source_basename == 'Cangjie5_TC.txt':
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj5_tc')
            elif source_basename == 'Cangjie5_HK.txt':
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj5_hk')
            elif source_basename == 'Cangjie5_SC.txt':
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj5_sc')
            elif source_basename == 'Cangjie5_special.txt':
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj5_special')
            elif source_basename in ['cj3.txt','cj3-30000.txt','cj3-special.txt']:  # 三代補完
                output_head = db_get_template(sqlite_cursor, 'yaml_head_cj3')
            else:                                                                   # 其他
                output_head = db_get_template(sqlite_cursor, 'yaml_head_other')
                schema_id = os.path.splitext(os.path.basename(source_basename))[0].lower()
        elif template == 'yong':
            if source_basename == 'Cangjie5.txt':                                   # 五代補完
                output_head = db_get_template(sqlite_cursor, 'yong_head_cj5_norm')
            elif source_basename == 'Cangjie5_TC.txt':
                output_head = db_get_template(sqlite_cursor, 'yong_head_cj5_tc')
            elif source_basename == 'Cangjie5_HK.txt':
                output_head = db_get_template(sqlite_cursor, 'yong_head_cj5_hk')
            elif source_basename == 'Cangjie5_SC.txt':
                output_head = db_get_template(sqlite_cursor, 'yong_head_cj5_sc')
            elif source_basename == 'Cangjie5_special.txt':
                output_head = db_get_template(sqlite_cursor, 'yong_head_cj5_special')
            else:                                                                   # 其他
                output_head = db_get_template(sqlite_cursor, 'yong_head_other')
                schema_id = os.path.splitext(os.path.basename(source_basename))[0].lower()
        elif template == 'fcitx':
                output_head = db_get_template(sqlite_cursor, 'fcitx_head')
        elif template == 'text':
            output_head = ''
        else:
            output_head = ''
        output_head = output_head.format(NAME=schema_id, VERSION=version)
        txt.write(output_head)

    # print(sqlite_cursor, output_file, template, order, delimiter, linebreak, source_basename)
    return order, delimiter, linebreak

# 輸出文件正文
def cmd_write_output_txt(output_file, output_data, order, delimiter, linebreak):
    logging.debug('output_file ={}, output_data ={}, order ={}, delimiter ={}, linebreak ={}'.format(output_file, 'output_data', order, delimiter, linebreak))
    # cmd_write_output_txt(output, output_data, order, delimiter, linebreak)  # 寫入正文
    # print('cmd_write_output_txt()')
    # print('output_data='+str(output_data))
    # delimiter 轉義
    if delimiter == 'tab':
        delimiter_decoded = '\t'
    elif delimiter == 'space':
        delimiter_decoded = ' '
    elif delimiter == 'none':
        delimiter_decoded = ''
    # linebreak 轉義
    if linebreak == 'crlf':
        linebreak_decoded = '\r\n'
    elif linebreak == 'cr':
        linebreak_decoded = '\r'
    elif linebreak == 'lf':
        linebreak_decoded = '\n'
    # 讀取並寫入
    with open(output_file,'a',encoding='utf8',newline='') as txt:
        for line in output_data:
            # print(line)
            character_value = line[0]
            code_value = line[1]
            if order=='char':
                if delimiter=='multi':
                    delimiter_decoded=' ' * 6
                new_line = character_value + delimiter_decoded + code_value + linebreak_decoded
            elif order=='code':
                if delimiter=='multi':
                    delimiter_decoded=' ' * (8 - len(code_value)) 
                new_line = code_value + delimiter_decoded + character_value + linebreak_decoded
            txt.writelines(new_line)

# 標記已選擇的字符集
def cmd_mark_selected_charset(sqlite_conn, sqlite_cursor, charset):
    logging.debug(locals())
    if charset == ['all']:
        charset = ['charset_all']
    else:
        for i,item in enumerate(charset):
            if re.match( r'charset_', charset[i]):
                pass
            else: 
                charset[i] = 'charset_'+charset[i]
    character_count = db_mark_selected_charset(sqlite_conn, sqlite_cursor, charset)
    return character_count

# 將source_file讀入數據庫
def cmd_read_source_to_database(path, sqlite_conn, sqlite_cursor):
    logging.debug(locals())
    # 檢查源碼表文件是否存在
    detect_source_file_format_result = cmd_detect_souece_file_format(path['source_locate'])
    if detect_source_file_format_result[0] == 'ERR_SOURCE_FILE_NOT_FOUND':
        print('源碼表文件不存在')
        result = 'ERR_SOURCE_FILE_NOT_FOUND'
        return(result, '', '', '', '', '')
    elif detect_source_file_format_result[0] == 'ERR_SOURCE_FILE_FAIL_TO_READ':
        print('源碼表文件讀取失敗')
        result = 'ERR_SOURCE_FILE_FAIL_TO_READ'
        return(result, '', '', '', '', '')
    elif detect_source_file_format_result[0] == 'no':
        print('不支持的源碼表文件格式')
        result = 'ERR_SOURCE_FILE_FORMAT_NOT_SUPPORT'
        return(result, '', '', '', '', '')
    elif detect_source_file_format_result[0] == 'yes':
        value_pattern = detect_source_file_format_result[1]
        char_first_confirmed = detect_source_file_format_result[2]
        # 導入基礎數據
        # print('[199]',sqlite_conn, sqlite_cursor)
        path, sqlite_conn, sqlite_cursor = db_initialize(path, sqlite_conn, sqlite_cursor)
        # 導入碼表數據
        last_source_file_hash = db_get_setting(sqlite_cursor, 'last_source_file_hash')      # 如果文件沒有變化，則不用重新導入
        with open(path['source_locate'],'rb') as f:
            sha1obj = hashlib.sha1()
            sha1obj.update(f.read())
            this_source_file_hash = sha1obj.hexdigest()
        if last_source_file_hash == this_source_file_hash:
            # print('No changes: ', 'txt[source_file]',  'both['+this_source_file_hash+']')
            pass
        else:
            # print('Changes:', 'txt[source_file]', 'last['+last_source_file_hash+']', 'this['+this_source_file_hash+']')
            # 謮取源碼表並插入數據庫
            db_truncate_cangjie_table(sqlite_conn, sqlite_cursor)   # 清空表
            batch_size = 10000   # 分批10000條提交一次  1000=70s,5000=28s,10000=23s,50000=14s
            data_batch = []
            id = 0
            with open(path['source_locate'],'r',encoding='utf8') as gib:
                for line in gib:
                    value_line = value_pattern.match(line)
                    if value_line:
                        id = id + 1
                        if char_first_confirmed:                            # 源碼表先字後碼
                            value_char = value_line[1]
                            value_code = value_line[2]
                            value_mark = value_line[3]
                        else:
                            value_char = value_line[2]                      # 源碼表先碼後字
                            value_code = value_line[1]
                            value_mark = value_line[3]
                        data_value = (value_char, value_code, value_mark, id)
                        data_batch.append(data_value)
                        # yield value_char, value_code, value_mark, id
                        if len(data_batch) >= batch_size:
                            db_insert_into_cangjie_table(sqlite_conn, sqlite_cursor, data_batch)
                            db_commit(sqlite_conn)
                            data_batch = []
                if data_batch:
                    db_insert_into_cangjie_table(sqlite_conn, sqlite_cursor, data_batch)
                    db_commit(sqlite_conn)
            db_config_setting(sqlite_conn, sqlite_cursor, 'last_source_file_hash', this_source_file_hash) # 更新hash
            db_commit(sqlite_conn)

        # 補全cangjie_table數據
        # print('111')
        count_total = db_initialize_cangjie_table(sqlite_conn, sqlite_cursor)
        # print('222')
        count_charset_data = db_count_charset(sqlite_conn, sqlite_cursor)
        count_charset = {}
        # print(type(count_charset_data))
        # print(count_charset_data)
        for item in count_charset_data:
            key = item[0]
            count = item[1]
            count_charset['charset_'+key.lower()] = count
            # print(key, count)
        result = 'SUCCESS'
    # print(result)
    return result, path, sqlite_conn, sqlite_cursor, count_total, count_charset

# 判斷source_file的格式
def cmd_detect_souece_file_format(source):
    logging.debug(locals())
    value_pattern_type = ['value_pattern_1_char_tab_code', 'value_pattern_2_char_space_code',
                          'value_pattern_3_code_tab_char', 'value_pattern_4_code_space_char']   # 別名
    value_pattern_match_num = {}
    for type in value_pattern_type:
        value_pattern_match_num[type] = 0   # 匹配的數量
    value_pattern_rule = {}                 # 規則，re.compile對象
    value_pattern_rule['value_pattern_1_char_tab_code']   = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})\t{0,1}(.*?)$')    #字tab碼
    value_pattern_rule['value_pattern_2_char_space_code'] = re.compile(r'^([^\t\n\r]+) +([a-z]{1,5})\t{0,1}(.*?)$')    #字space碼
    value_pattern_rule['value_pattern_3_code_tab_char']   = re.compile(r'^([a-z]{1,5})\t([^\t\n\r]+)\t{0,1}(.*?)$')    #碼tab字
    value_pattern_rule['value_pattern_4_code_space_char'] = re.compile(r'^([a-z]{1,5}) +([^\t\n\r]+)\t{0,1}(.*?)$')    #碼space字
    # value_pattern_char_tab_code = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\u20000-\u2cebf\u30000-\u323af\u2f800-\u2fa1f]+\t([a-z]{1,5})')
    try:
        with open(source,'r',encoding='utf8') as gib:
            for i, line in enumerate(gib):
                for type in value_pattern_type:                         # 對四款正則表達式遍歷, 看哪種匹配最多
                    value_line = value_pattern_rule[type].match(line)
                    if value_line:
                        value_pattern_match_num[type] = value_pattern_match_num[type] + 1
                if i>1000:
                    break
    except FileNotFoundError:
        return('ERR_SOURCE_FILE_NOT_FOUND',)
    except:
        return('ERR_SOURCE_FILE_FAIL_TO_READ',)
    value_pattern_confirmed = False
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

# linebreak轉義
def cmd_linebreak_decode(linebreak_code):        # lf -> \n
    logging.debug(locals())
    if linebreak_code == 'crlf':
        linebreak_value = "\r\n"
    elif linebreak_code == 'cr':
         linebreak_value = "\r"
    elif linebreak_code == 'lf':
         linebreak_value = "\n"
    else:
        # print('aaalinebreak_code='+str(linebreak_code))
        pass
    return linebreak_value

# delimiter轉義
def cmd_delimiter_decode(delimiter_code):        # tab -> \t
    logging.debug(locals())
    if delimiter_code == 'space':
        delimiter_value = " "
    elif delimiter_code == 'tab':
        delimiter_value = "\t"
    return delimiter_value

# cmd 參數定義
def parse_args():                           # parse_args
    parse = argparse.ArgumentParser(description='參數', formatter_class=argparse.RawTextHelpFormatter)
    parse.add_argument('-s', '--source', help='需要轉換的源文件(衹接受絕對路徑)')  # 創建參數
    parse.add_argument('-q', '--quick_source', help='以倉五補完計劃的文件作為源文件, 源文件必須位於上一級目錄[norm=Cangjie5.txt, tc=Cangjie5_TC.txt, hk=Cangjie5_HK.txt, sc=Cangjie5_SC.txt, sp=Cangjie5_special.txt]')  # 創建參數
    parse.add_argument('-f', '--filename', help='轉換輸出的文件名稱')
    parse.add_argument('-o', '--order', help='字和倉頡碼的順序[char=字在前, code=倉頡碼在前]')
    parse.add_argument('-d', '--delimiter', help='分隔符[tab=製表鍵, space=單個空格, multi=以空格代替Tab對齊, none=(無)]')
    parse.add_argument('-l', '--linebreak', help='換行符[crlf, cr, lf, auto=與系統一致]')
    parse.add_argument('-t', '--template', help='使用模板[rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]')
    parse.add_argument('-c', '--charset', help=textwrap.dedent('''\
                                        可多選，以","分隔
                                        u=  CJK 基本區,  ua= CJK 擴展A區, ub= CJK 擴展B區, uc= CJK 擴展C區, ud= CJK 擴展D區,
                                        ue= CJK 擴展E區, uf= CJK 擴展F區, ug= CJK 擴展G區, uh= CJK 擴展H區, ui= CJK 擴展I區,
                                        ci= 兼容漢字, cis= 兼容漢字增補, kr= 康熙部首, rs= 部首增補, s= 筆畫,
                                        sp= 符號標點, cf= 兼容符號, idc= 表意文字描述字符, crn= 算籌符號, pua= 私用區 (PUA+SPUA),
                                        other= Unicode 中的其他區塊,
                                        gb2312= GB/T 2312-1980, gbk= GBK, big5= Big5, hkscs= HKSCS-2016, gui_fan= 通用規範漢字表,
                                        gb18030_2022_l1= GB 18030-2022 級別1,
                                        gb18030_2022_l2= GB 18030-2022 級別2,
                                        gb18030_2022_l3= GB 18030-2022 級別3,
                                        yyy= YYY開頭的標點符號, zx= ZX開頭的標點符號
                                        '''))
    args = parse.parse_args()                   # 解析參數
    return args

if __name__ == "__main__":
    # 文件路徑常量
    path = {}
    path['current_directory'] = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    path['parent_directory'] = os.path.dirname(path['current_directory'])     # 獲取上級目錄
    
    # 解析cmd參數
    args = parse_args()                         # 解析參數
    source = args.source
    quick_source = args.quick_source
    order = args.order
    delimiter = args.delimiter
    linebreak = args.linebreak
    template = args.template
    output = args.filename
    charset = args.charset

    # print(template)

    # 校驗cmd參數組合
    if quick_source is not None:                    # 全部轉小寫
        quick_source = quick_source.lower()
    if order is not None:
        order = order.lower()
    if delimiter is not None:
        delimiter = delimiter.lower()
    if linebreak is not None:
        linebreak = linebreak.lower()
    if template is not None:
        template = template.lower()
    if charset is not None:
        charset = charset.lower()

    if source is None:
        if quick_source is None:
            print('--source 參數有誤 [需要轉換的源文件]')
            exit()
        else:                   # 將quick_source轉換為source
            quick_source_short = ['norm','tc','hk','sc','sp']
            quick_source_full = ['Cangjie5.txt','Cangjie5_TC.txt','Cangjie5_HK.txt','Cangjie5_SC.txt','Cangjie5_special.txt']
            quick_source_dict = {}
            for i in range(0, len(quick_source_short)):
                quick_source_dict[quick_source_short[i]] = quick_source_full[i]
            if quick_source in quick_source_short:
                path['source_locate'] = os.path.join(path['parent_directory'],quick_source_dict[quick_source])
            else:
                print('--quick_source 參數有誤, 以倉五補完計劃的文件作為源文件, 源文件必須位於上一級目錄[norm=Cangjie5.txt, tc=Cangjie5_TC.txt, hk=tc=Cangjie5_HK.txt, sc=Cangjie5_SC.txt, sp=Cangjie5_special.txt]')
    else:
        if os.path.isabs(source):               # 絕對路徑
            path['source_locate'] = source
        else:                                   # 相對路徑
            path['source_locate'] = os.path.join(path['current_directory'],source)

    if output is None:
        output = path['source_locate'].replace('.txt','_output.txt')

    if template is None:
        if order is None or order not in ['char','code']:
            print('--order 參數有誤 [char=字在前, code=倉頡碼在前]')
            exit()
        elif delimiter is None or delimiter not in ['tab','space','multi','none']:
            print('--delimiter 參數有誤 [tab=製表鍵, space=單個空格, multi=以空格代替Tab對齊, none=(無)]')
            exit()
        elif linebreak is None or linebreak not in ['crlf','cr','lf','auto']:
            print("--linebreak 參數有誤 [crlf, cr, lf, auto]")
            exit()
    else:
        if template not in ['rime','weasel','squirrel','fcitx','yong']:
            print("'--template 參數有誤 [rime=ibus-rime, weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]'")
            exit()
        else:
            if (order is not None) or (delimiter is not None):
                print('--template 參數不可以與 --order, --delimiter 參數共用')
                exit()

    if charset is None:
        charset = ['all']           # 默認全選
    else:
        charset = charset.split(',')
        charset_support_list = ['u','ua','ub','uc','ud','ue','uf','ug','uh','ui',
                                'ci','cis','kr','rs','s','sp','cf','idc','crn','pua','other',
                                'gb2312','gbk','big5','hkscs','gui_fan','yyy','zx',
                                'gb18030_2022_l1','gb18030_2022_l2','gb18030_2022_l3']
        for item in charset:
            if item not in charset_support_list:
                print('--charset 參數有誤, 不支持的選項: '+item)
                exit()

    # 開始處理
    source_basename = os.path.basename(path['source_locate'])
    # result, path, sqlite_conn, sqlite_cursor = cmd_read_source_to_database(path)            # 將源碼表讀入數據庫
    sqlite_conn, sqlite_cursor = db_create_database(path)                 # 創建數據庫
    # print('[342]', sqlite_conn, sqlite_cursor)
    result, path, sqlite_conn, sqlite_cursor, character_count_total, count_charset_result = cmd_read_source_to_database(path, sqlite_conn, sqlite_cursor)
    character_count = 0
    character_count = cmd_mark_selected_charset(sqlite_conn, sqlite_cursor, charset) # 字符集篩選並統計字數
    if charset == ['all']:
        print(f"字符數量: {character_count}")
    else:
        print(f"篩選後的字符數量: {character_count}")
    db_build_final_table(sqlite_conn, sqlite_cursor, charset)         # 生成碼表
    output_data = db_export_final_table(sqlite_conn, sqlite_cursor)   # 從數據庫導出碼表
    order, delimiter, linebreak = cmd_write_output_template(sqlite_cursor, output, template, order, delimiter, linebreak, source_basename)  # 寫入模板
    cmd_write_output_txt(output, output_data, order, delimiter, linebreak)  # 寫入正文
    # E:\程式\GitHub\Cangjie5-dev\scripts> python .\newCmd.py -q norm -t rime -f "Cangjie5_output.txt"
    
