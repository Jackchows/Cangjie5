# -*- coding: utf8 -*-
import sqlite3
import re
import os
import hashlib
import time

# 標記已選擇的字符
def mark_seleted_charset(sqlite_conn,sqlite_cursor,selected_options):
    sqlite_cursor.execute("UPDATE cangjie_table SET seleted = null where 1=1;")
    for item in selected_options:
        print(item)
        if item == 'charset_u':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'U';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ua':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UA';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ub':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UB';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uc':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UC';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ud':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UD';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ue':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UE';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uf':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UF';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ug':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UG';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uh':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UH';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ui':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UI';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ci':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CI';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_cis':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CIS';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_kr':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'KR';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_s':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'S';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_sp':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'SP';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_cf':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CF';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_idc':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'IDC';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_crn':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CF';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_pua':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'PUA';")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_gb2312':
            last_time = time.time() #
            sqlite_cursor.execute("SELECT id,character_value FROM cangjie_table WHERE seleted is null;")
            rows = sqlite_cursor.fetchall()
            if rows:
                for row in rows:
                    id = str(row[0])
                    char_value = row[1]
                    try:
                        char_value.encode('gb2312')
                        sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where id = ? ;", (id,))
                        sqlite_conn.commit()
                    except:
                        pass
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_gbk':
            last_time = time.time() #
            sqlite_cursor.execute("SELECT id,character_value FROM cangjie_table WHERE seleted is null;")
            rows = sqlite_cursor.fetchall()
            if rows:
                for row in rows:
                    id = str(row[0])
                    char_value = row[1]
                    try:
                        char_value.encode('gbk')
                        sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where id = ? ;", (id,))
                        sqlite_conn.commit()
                    except:
                        pass
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_hkscs':
            last_time = time.time() #
            sqlite_cursor.execute("SELECT id,character_value FROM cangjie_table WHERE seleted is null;")
            rows = sqlite_cursor.fetchall()
            if rows:
                for row in rows:
                    id = str(row[0])
                    char_value = row[1]
                    try:
                        char_value.encode('big5hkscs')
                        sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where id = ? ;", (id,))
                        sqlite_conn.commit()
                    except:
                        pass
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_big5':
            last_time = time.time() #
            sqlite_cursor.execute("SELECT id,character_value FROM cangjie_table WHERE seleted is null;")
            rows = sqlite_cursor.fetchall()
            if rows:
                for row in rows:
                    id = str(row[0])
                    char_value = row[1]
                    try:
                        char_value.encode('big5')
                        sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where id = ? ;", (id,))
                        sqlite_conn.commit()
                    except:
                        pass
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #

        else:
            print('未實現功能:'+item)

        sqlite_conn.commit()
    sqlite_cursor.execute("SELECT count(distinct unicode_hex) FROM cangjie_table WHERE seleted = '1';")
    rows = sqlite_cursor.fetchall()
    for row in rows:
        character_count = str(row[0])

    return character_count
    
'''
        charset_tygfhzb
        charset_gb18030_2022_l1
        实现级别１支持本文件的单字节编码部分、双字节编码部分和四字节编码部分的ＣＪＫ 统一汉字
（即０ｘ８２３５８Ｆ３３～０ｘ８２３５９６３６）和ＣＪＫ 统一汉字扩充Ａ（即０ｘ８１３９ＥＥ３９～０ｘ８２３５８７３８）。
        charset_gb18030_2022_l2
        实现级别２包含实现级别１。此外，实现级别２还支持《通用规范汉字表》中的没有包含在实现级
别１之内的编码汉字。《通用规范汉字表》所收汉字在本文件中的代码位置和字形，见附录Ｅ。
        charset_gb18030_2022_l3
        实现级别３包含实现级别２。此外，实现级别３ 还支持本文件规定的全部汉字及表３ 中的康熙
部首。
        charset_gb18030_2022_other
        其他
        charset_yyy
        charset_zx
        charset_other
        
'''

# 開始處理
def start_database_process(path):
    # 連接
    sqlite_conn   = sqlite3.connect(path['sqlite_locate'])
    sqlite_cursor = sqlite_conn.cursor()

    # 導入基礎數據
    import_normal_data_table(sqlite_conn, sqlite_cursor, path['sql_settings'])
    import_normal_data_table(sqlite_conn, sqlite_cursor, path['sql_unicode_block'])

    # 將碼表導入數據庫
    import_cangjie_table_from_source(sqlite_conn, path['source_file'], sqlite_cursor, path['sql_cangjie_table'])

    print("完成導入")
    # 斷開
    if __name__ == '__main__':
        sqlite_conn.close()
    else:
        return sqlite_conn,sqlite_cursor

# 導入基礎數據表
def import_normal_data_table(sqlite_conn, sqlite_cursor, init_sql):
    # 讀取建表sql文件
    with open(init_sql, 'r', encoding='utf8') as file:
        sql_commands = file.read().split(';')
    # 執行建表
    for command in sql_commands:
        sqlite_cursor.execute(command)
    sqlite_conn.commit()

# 導入cangjie_table表
def import_cangjie_table_from_source(sqlite_conn, source_file, sqlite_cursor, init_sql):

    last_source_file_hash = ''

    with open(source_file,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        this_source_file_hash = sha1obj.hexdigest()

    sqlite_cursor.execute("SELECT setting_value FROM settings WHERE setting_item = 'last_source_file_hash';")
    rows = sqlite_cursor.fetchall()
    if rows:
        for row in rows:
            setting_value = row
            last_source_file_hash = str(setting_value[0])
    else:
        # print(this_source_file_hash)
        sqlite_cursor.execute("INSERT INTO settings (setting_item, setting_value) VALUES ('last_source_file_hash','"+this_source_file_hash+"');")
        sqlite_conn.commit()

    last_source_file_hash = '123456'        # 每次都重新導入

    if last_source_file_hash == this_source_file_hash:                 # 如果碼表文件無變化，則毋需重新導入
        print('equal','['+this_source_file_hash+']')
        pass
    else:                                                              # 否則重新導入
        print('not equal,','last['+last_source_file_hash+']','this['+this_source_file_hash+']')
        try:
            # 讀取建表sql文件
            with open(init_sql, 'r', encoding='utf8') as file:
                sql_commands = file.read().split(';')
            # 執行建表
            for command in sql_commands:
                sqlite_cursor.execute(command)
            sqlite_conn.commit()
            # 謮取源碼表並插入數據庫
            batch_size = 10000   # 分批10000條提交一次  1000=70s,5000=28s,10000=23s,50000=14s
            data_batch = []
            for data in read_cangjie_table_source(source_file):
                data_batch.append(data)
                if len(data_batch) >= batch_size:
                    insert_cangjie_table(sqlite_cursor, data_batch)
                    sqlite_conn.commit()  # 批量提交
                    data_batch = []
            if data_batch:
                insert_cangjie_table(sqlite_cursor, data_batch)
                sqlite_conn.commit()
            # 整理數據表
            initialize_cangjie_table(sqlite_conn, sqlite_cursor)
            # 更新last_source_file_hash
            sqlite_cursor.execute("UPDATE settings SET setting_value='"+this_source_file_hash+"';")
            sqlite_conn.commit()
            # last_source_file_hash = this_source_file_hash
        except:
            print('[89]exception')

# 導入cangjie_table表: 讀取源文件
def read_cangjie_table_source(source_file):
    value_pattern = re.compile(r'^([^\t\n\r]+)\t([a-z]{1,5})\t{0,1}\[{0,1}(.*?)\]{0,1}$')
    id = 0
    with open(source_file, 'r', encoding='utf-8') as gib:
        for line in gib:
            value_line = value_pattern.match(line)
            if value_line:
                value_char = value_line[1]
                value_code = value_line[2]
                value_mark = value_line[3]
                id = id + 1
                yield value_char, value_code, value_mark, id
# 導入cangjie_table表: 插入數據表
def insert_cangjie_table(cursor, data_batch):
    cursor.executemany('INSERT INTO cangjie_table (character_value, code_value, marks, id) VALUES (?, ?, ?, ?)', data_batch)
def initialize_cangjie_table(sqlite_conn, sqlite_cursor):
    # 將marks由""改為null
    sqlite_cursor.execute("UPDATE cangjie_table SET marks = null where marks = '';")
    sqlite_conn.commit()
    # 補全unicode_dex和unicode_dec
    sqlite_cursor.execute("SELECT id,unicode_hex,unicode_dec,character_value FROM cangjie_table;")
    rows = sqlite_cursor.fetchall()
    i = 0
    for row in rows:
        id, unicode_hex, unicode_dec, character_value = row
        unicode_dec = ord(character_value)
        unicode_hex = hex(unicode_dec)
        sqlite_cursor.execute("UPDATE cangjie_table SET unicode_hex = ?, unicode_dec = ? WHERE id = ?", (unicode_hex, unicode_dec, id))
        i = i + 1
    if i > 1000:
        sqlite_conn.commit()
        i = 0
    sqlite_conn.commit()
    # 補全block和block_no
    sqlite_cursor.execute("SELECT c.id, \
                    (SELECT u.name_abbr FROM unicode_block u WHERE c.unicode_dec > u.start_dec AND c.unicode_dec < u.end_dec) AS block, \
                    (SELECT u.area_no FROM unicode_block u WHERE c.unicode_dec > u.start_dec AND c.unicode_dec < u.end_dec) AS block_no \
                    FROM cangjie_table c;")
    rows = sqlite_cursor.fetchall()
    i = 0
    for row in rows:
        id, block, block_no = row
        sqlite_cursor.execute("UPDATE cangjie_table SET block = ?, block_no = ? WHERE id = ?", (block, block_no, id))
        i = i + 1
    if i > 1000:
        sqlite_conn.commit()
        i = 0
    sqlite_conn.commit()
    # 補全is_letter 倉頡字母
    cangjie_letter = ['0x65e5','0x6708','0x91d1','0x6728','0x6c34','0x706b','0x571f',
                      '0x7af9','0x6208','0x5341','0x5927','0x4e2d','0x4e00','0x5f13',
                      '0x4eba','0x5fc3','0x624b','0x53e3','0x5c38','0x5eff','0x5c71',
                      '0x5973','0x7530','0x535c']
    for unicode in cangjie_letter:
        sqlite_cursor.execute("UPDATE cangjie_table SET is_letter = 1 WHERE unicode_hex = '"+unicode+"'")
    sqlite_conn.commit()

if __name__ == '__main__':
    # 文件路徑
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄

    path = {}
    path['source_file'] = os.path.join(parent_directory,'Cangjie5_TC.txt')
    path['sqlite_locate'] = os.path.join(current_directory,'sqlite','cangjie.db')
    path['sql_settings']  = os.path.join(current_directory,'sqlite','settings.sql')
    path['sql_cangjie_table'] = os.path.join(current_directory,'sqlite','cangjie_table.sql')
    path['sql_unicode_block'] = os.path.join(current_directory,'sqlite','unicode_block.sql')

    source_file_hash = ''
    # source_file = 'E:/程式/GitHub/Cangjie5-dev/Cangjie5.txt'
    # sqlite_locate = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/cangjie.db'
    # sql_cangjie_table = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/cangjie_table.sql'
    # sql_unicode_block = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/unicode_block.sql'


    # sqlite_conn   = ''
    # sqlite_cursor = ''

    start_database_process(path)