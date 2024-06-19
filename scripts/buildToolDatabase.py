# -*- coding: utf8 -*-
# FUNCTION_RELATION
# db_initialize()                 創建數據庫並導入數據
#     db_import_basic_data()          導入基礎數據
# db_truncate_cangjie_table()     清空 cangjie_table
# db_insert_into_cangjie_table()  插入 cangjie_table
# db_initialize_cangjie_table()   補全 cangjie_table 數據
# db_count_charset()              計算字符數量
# db_mark_selected_charset()       標記已選擇的字符集
# db_build_final_table()          生成最終碼表
# db_commit()                     COMMIT
# db_get_setting()                查詢 setting
# db_config_setting()             更新 setting
# db_get_template()               查詢 template

import sqlite3
import os
import hashlib
import time
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] - %(funcName)s() - %(message)s')

# db 讀取setting表
def db_get_setting(sqlite_cursor, item):
    logging.debug(locals())
    sqlite_cursor.execute("SELECT setting_value FROM settings WHERE setting_item = ? ;", (item,))
    rows = sqlite_cursor.fetchall()
    if rows:
        for row in rows:
            value = str(row[0])
    else:
        value = ''
    # print('db_get_setting value='+value)
    return value

# db 寫入setting表
def db_config_setting(sqlite_conn, sqlite_cursor, item, value):
    logging.debug(locals())
    sqlite_cursor.execute("SELECT setting_value FROM settings WHERE setting_item = ? ;", (item,))
    rows = sqlite_cursor.fetchall()
    if rows:
        sqlite_cursor.execute("UPDATE settings SET setting_value = ? where setting_item = ? ;", (value, item))
        sqlite_conn.commit()
    else:
        sqlite_cursor.execute("INSERT INTO settings (setting_value, setting_item) values (?, ?) ;", (value, item))
        sqlite_conn.commit()
    return 'INFO_SUCCESS'

# db 讀取template表
def db_get_template(sqlite_cursor, item):
    logging.debug(locals())
    sqlite_cursor.execute("SELECT value FROM templates WHERE key = ? ;", (item,))
    rows = sqlite_cursor.fetchall()
    if rows:
        for row in rows:
            value = str(row[0])
    else:
        value = ''
    return value

# db COMMIT
def db_commit(sqlite_conn):
    logging.debug(locals())
    sqlite_conn.commit

# db TRUNCATE
def db_truncate_cangjie_table(sqlite_conn, sqlite_cursor):
    logging.debug(locals())
    sqlite_cursor.execute(
        '''
        DELETE FROM cangjie_table;
        '''
    )
    sqlite_conn.commit()

# db 讀取final_table
def db_export_final_table(sqlite_conn, sqlite_cursor):
    logging.debug(locals())
    # print('db_export_final_table()')
    sqlite_cursor.execute("SELECT character_value,code_value FROM build_final ORDER BY id;")
    rows = sqlite_cursor.fetchall()
    # for line in rows:
    #     print(line)
    return rows
    # if rows:
    #     print('[DEBUG]something')
    #     for row in rows:
    #         character_value, code_value = row
    #         yield character_value, code_value
    # else:
    #     print('[DEBUG]nothing')

# db 處理數據並生成build_final
def db_build_final_table(sqlite_conn, sqlite_cursor, selected_options):
    logging.debug(locals())
    # 按重碼排序添加x編碼
    sqlite_cursor.execute("DELETE FROM build_temp WHERE 1=1;")
    sqlite_conn.commit()
    if selected_options == ['charset_all']:
        sqlite_cursor.execute(
            '''
            INSERT INTO build_temp (unicode_hex,character_value,code_value,marks,block,block_no,is_letter,repeat_order,unicode_dec)
                SELECT c.unicode_hex,c.character_value,c.code_value,c.marks,c.block,c.block_no,c.is_letter,
                        RANK() OVER (PARTITION BY c.code_value
                                        ORDER BY c.code_value,c.is_letter DESC,c.block_no,c.`id`,c.unicode_dec) AS repeat,
                        c.unicode_dec
                FROM cangjie_table c
              WHERE (c.code_value NOT LIKE 'x%' OR c.code_value = 'xxxxx')
            ORDER BY code_value,is_letter desc,`id`;
            ''')
    else:
        sqlite_cursor.execute(
            '''
            INSERT INTO build_temp (unicode_hex,character_value,code_value,marks,block,block_no,is_letter,repeat_order,unicode_dec)
                SELECT c.unicode_hex,c.character_value,c.code_value,c.marks,c.block,c.block_no,c.is_letter,
                        RANK() OVER (PARTITION BY c.code_value
                                        ORDER BY c.code_value,c.is_letter DESC,c.block_no,c.`id`,c.unicode_dec) AS repeat,
                        c.unicode_dec
                FROM cangjie_table c WHERE c.selected = '1'
                AND (c.code_value NOT LIKE 'x%' OR c.code_value = 'xxxxx')
            ORDER BY code_value,is_letter desc,`id`;
            ''')
    sqlite_cursor.execute(
        '''
        UPDATE build_temp 
           SET repeat_order = null 
         WHERE (block IS NULL OR block NOT LIKE 'U%');
        ''')
    sqlite_conn.commit()
    sqlite_cursor.execute("update build_temp set repeat_code = 'x'||substr(code_value,1,4) where repeat_order = 2;")
    sqlite_cursor.execute("update build_temp set repeat_code = 'xx'||substr(code_value,1,3) where repeat_order = 3;")
    sqlite_cursor.execute("update build_temp set repeat_code = 'xxx'||substr(code_value,1,2) where repeat_order = 4;")
    sqlite_conn.commit()

    for i in range(2,5):
        # 如果有重複，刪除常用字表未收錄的字
        sqlite_cursor.execute(
            '''
            UPDATE build_temp
            SET repeat_code = NULL
            WHERE repeat_code in 
                        (select c.repeat_code from build_temp c where c.repeat_order = ? group by c.repeat_code having count(1)>1)
            AND repeat_code in 
                        (select c.repeat_code from build_temp c where exists
                            (SELECT 1 
                            FROM charset_table s 
                            WHERE c.unicode_hex = s.unicode_hex 
                                AND (s.gui_fan IN ('LV_1','LV_2','LV_3','NOTE') OR 
                                    s.zi_jing = 'STANDARD' OR 
                                    s.guo_zi = '1')))
            AND EXISTS (SELECT 1 
                            FROM charset_table s 
                            WHERE build_temp.unicode_hex = s.unicode_hex
                            AND (s.gui_fan NOT IN ('LV_1','LV_2','LV_3','NOTE') OR s.gui_fan IS NULL)
                            AND (s.zi_jing <> 'STANDARD' OR s.zi_jing IS NULL)
                            AND (s.guo_zi <> '1' OR s.guo_zi IS NULL));
            ''',
            (i,)
        )
        sqlite_conn.commit()
        # 如果仍有重複，按Unicode順序刪除排在後面的字
        sqlite_cursor.execute(
            '''
            UPDATE build_temp
            SET repeat_code = NULL
            WHERE repeat_code in 
                    (select c.repeat_code from build_temp c where c.repeat_order = ? group by c.repeat_code having count(1)>1)
            AND block_no not in 
                    (select min(block_no) from build_temp c where build_temp.repeat_code = c.repeat_code group by repeat_code);
            ''',
            (i,)
        )
        sqlite_conn.commit()
        sqlite_cursor.execute(
            '''
            UPDATE build_temp
            SET repeat_code = NULL
            WHERE repeat_code in 
                    (select c.repeat_code from build_temp c where c.repeat_order = ? group by c.repeat_code having count(1)>1)
            AND unicode_dec not in 
                    (select min(unicode_dec) from build_temp c where build_temp.repeat_code = c.repeat_code group by repeat_code);
            ''',
            (i,)
        )
        sqlite_conn.commit()
        # 如果本來是一字多碼，加x之後重複，則删除排在後面的一個
        sqlite_cursor.execute(
            '''
            UPDATE build_temp
            SET repeat_code = NULL
            WHERE repeat_code in 
                    (select c.repeat_code from build_temp c where c.repeat_order = ? group by c.repeat_code having count(1)>1)
            AND id not in 
                    (select min(id) from build_temp c where build_temp.repeat_code = c.repeat_code group by repeat_code);
            ''',
            (i,)
        )
        sqlite_conn.commit()
        # 確保xabcd和xxabc是同一組，原始編碼都是abcde
        sqlite_cursor.execute(
            '''
            UPDATE build_temp
            SET repeat_code = null
            WHERE repeat_order = ? 
            AND code_value NOT IN
                    (SELECT s.code_value
                    FROM build_temp s
                    WHERE s.repeat_order = ? 
                        AND s.repeat_code IS NOT NULL);
            ''',
            (i+1,i) 
        )
        sqlite_conn.commit()

    sqlite_cursor.execute("DELETE from build_final WHERE 1=1;")
    sqlite_cursor.execute(
        '''
        INSERT INTO build_final (character_value, code_value, marks)
        SELECT character_value,code_value,marks 
        FROM 
            (SELECT c.character_value,c.code_value,marks,id
                FROM build_temp c
            UNION ALL 
            SELECT c.character_value,c.repeat_code,marks,id
                FROM build_temp c
                WHERE c.repeat_code IS NOT NULL)
        ORDER BY code_value, id
        '''
    )
    sqlite_conn.commit()

# db 更新字符集標記
def db_mark_selected_charset(sqlite_conn,sqlite_cursor,selected_options):
    logging.debug(locals())
    # print('LALALA'+str(selected_options))
    sqlite_cursor.execute("UPDATE cangjie_table SET selected = null where 1=1;")
    sqlite_conn.commit()
    # 如果charset_table沒有這個字符，則添加進去
    sqlite_cursor.execute("SELECT DISTINCT c.unicode_hex, c.character_value FROM cangjie_table c WHERE NOT EXISTS (SELECT 1 FROM charset_table s WHERE c.unicode_hex = s.unicode_hex);")
    rows = sqlite_cursor.fetchall()
    # print('rows = sqlite_cursor.fetchall():'+str(len(rows)))
    if rows:
        i = 0
        for row in rows:
            unicode_hex = row[0]
            character_value  = row[1]
            sqlite_cursor.execute("INSERT INTO charset_table (unicode_hex, character_value) VALUES ( ?, ? )", (unicode_hex, character_value))
            # print(unicode_hex)
            i = i + 1
            if i % 5000 == 0:
                sqlite_conn.commit()
        sqlite_conn.commit()
    # 逐個判斷字符集
    if 'charset_all' in selected_options:
        sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1;")
        sqlite_conn.commit()
    else:
        for item in selected_options:
            # print(item)
            if item == 'charset_u':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'U' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ua':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UA' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ub':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UB' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_uc':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UC' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ud':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UD' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ue':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UE' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_uf':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UF' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ug':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UG' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_uh':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UH' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ui':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'UI' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_ci':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'CI' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_cis':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'CIS' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_kr':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'KR' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_rs':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'RS' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_s':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'S' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_sp':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'SP' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_cf':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'CF' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_idc':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'IDC' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_crn':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'CRN' and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_pua':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block in ('PUA','PUAA','PUAB') and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_other':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = 1 \
                                        WHERE (block IS NULL OR \
                                            block NOT IN ('U','UA','UB','UC','UD','UE','UF','UG','UH','UI', \
                                                            'CI','CIS','KR','RS','S','SP','CF','IDC','CRN', \
                                                            'PUA','PUAA','PUAB')) \
                                        AND selected IS NULL;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
                last_time = this_time #
            elif item == 'charset_gb2312':
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過gb2312，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.gb2312 IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.selected is NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('gb2312')
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET gb2312 = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET gb2312 = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                # 測試完之後更新標記
                # print('start update selected')
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gb2312 = '1' \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_gbk':
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過gbk，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.gbk IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.selected is NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('gbk')
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET gbk = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET gbk = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                            # 測試完之後更新標記
                # print('start update selected')
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gbk = '1' \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_hkscs':
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過hkscs，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.hkscs IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.selected is NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('big5hkscs')
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET hkscs = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET hkscs = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                            # 測試完之後更新標記
                # print('start update selected')
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.hkscs = '1' \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_big5':
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過big5，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.big5 IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.selected is NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('big5')
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET big5 = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                            # print(character_value, 'yes')
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET big5 = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                            # print(character_value, 'no')
                # 測試完之後更新標記
                # print('start update selected')
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.big5 = '1' \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_gui_fan':
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過big5，則進行測試
                sqlite_cursor.execute("UPDATE charset_table SET gui_fan = '0' where gui_fan is null ;")
                sqlite_conn.commit()
                # 測試完之後更新標記
                # print('start update selected')
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gui_fan <> '0' \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_gb18030_2022_l1':
                '''
                实现级别１支持本文件的单字节编码部分、双字节编码部分和四字节编码部分的ＣＪＫ 统一汉字（即０ｘ８２３５８Ｆ３３～０ｘ８２３５９６３６）和
                ＣＪＫ 统一汉字扩充Ａ（即０ｘ８１３９ＥＥ３９～０ｘ８２３５８７３８）。
                '''
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過gb18030，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value \
                                        FROM charset_table s \
                                        WHERE (s.gb18030 IS NULL OR s.gb18030_byte IS NULL) \
                                        AND EXISTS (SELECT 1 \
                                                        FROM cangjie_table c \
                                                    WHERE s.unicode_hex = c.unicode_hex \
                                                        AND c.selected IS NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        # print('[337]'+character_value)
                        try:
                            character_value.encode('gb18030')
                            byte = len(character_value.encode('gb18030'))
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030_byte = ? where unicode_hex = ? ;", (byte, unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                # 測試完之後更新標記
                # 單字節和雙字節
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gb18030 = '1' \
                                        AND s.gb18030_byte in ('1','2') \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # 四字節的基本區和擴展A區
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block in ('U','UA') and selected is null;")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_gb18030_2022_l2':
                '''
                实现级别２包含实现级别１。此外，实现级别２还支持《通用规范汉字表》中的没有包含在实现级别１之内的编码汉字。
                《通用规范汉字表》所收汉字在本文件中的代码位置和字形，见附录Ｅ。
                '''
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過gb18030，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value \
                                        FROM charset_table s \
                                        WHERE (s.gb18030 IS NULL OR s.gb18030_byte IS NULL) \
                                        AND EXISTS (SELECT 1 \
                                                        FROM cangjie_table c \
                                                    WHERE s.unicode_hex = c.unicode_hex \
                                                        AND c.selected IS NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('gb18030')
                            byte = len(character_value.encode('gb18030'))
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030_byte = ? where unicode_hex = ? ;", (byte, unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                # 測試完之後更新標記
                # 單字節和雙字節
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gb18030 = '1' \
                                        AND s.gb18030_byte in ('1','2') \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # 四字節的基本區和擴展A區
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block in ('U','UA') and selected is null;")
                sqlite_conn.commit()
                # 通用規範漢字表
                sqlite_cursor.execute("UPDATE cangjie_table \
                                SET selected = '1' \
                            WHERE unicode_hex IN ( \
                            SELECT c.unicode_hex \
                                FROM cangjie_table c, charset_table s \
                            WHERE c.unicode_hex = s.unicode_hex \
                                AND s.gui_fan <> '0' \
                                AND c.selected IS NULL );")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_gb18030_2022_l3':
                '''
                实现级别３包含实现级别２。此外，实现级别３ 还支持本文件规定的全部汉字及表３ 中的康熙部首。
                '''
                last_time = time.time() #
                # 如果charset_table有這個字符，但是未測試過gb18030，則進行測試
                sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value \
                                        FROM charset_table s \
                                        WHERE (s.gb18030 IS NULL OR s.gb18030_byte IS NULL) \
                                        AND EXISTS (SELECT 1 \
                                                        FROM cangjie_table c \
                                                    WHERE s.unicode_hex = c.unicode_hex \
                                                        AND c.selected IS NULL);")
                rows = sqlite_cursor.fetchall()
                if rows:
                    for row in rows:
                        can_be_encoded = False
                        unicode_hex = row[0]
                        character_value = row[1]
                        try:
                            character_value.encode('gb18030')
                            byte = len(character_value.encode('gb18030'))
                            can_be_encoded = True
                        except:
                            pass
                        if can_be_encoded:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '1' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030_byte = ? where unicode_hex = ? ;", (byte, unicode_hex,))
                            sqlite_conn.commit()
                        else:
                            sqlite_cursor.execute("UPDATE charset_table SET gb18030 = '0' where unicode_hex = ? ;", (unicode_hex,))
                            sqlite_conn.commit()
                # 測試完之後更新標記
                # 單字節和雙字節
                sqlite_cursor.execute("UPDATE cangjie_table \
                                        SET selected = '1' \
                                        WHERE unicode_hex IN ( \
                                    SELECT c.unicode_hex \
                                        FROM cangjie_table c, charset_table s \
                                        WHERE c.unicode_hex = s.unicode_hex \
                                        AND s.gb18030 = '1' \
                                        AND s.gb18030_byte in ('1','2') \
                                        AND c.selected IS NULL );")
                sqlite_conn.commit()
                # 全部漢字
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block like 'U%' and selected is null;")
                sqlite_conn.commit()
                # 康熙部首
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where block = 'KR' and selected is null;")
                sqlite_conn.commit()
                # print('finished update selected')
            elif item == 'charset_yyy':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where code_value like 'yyy%' and (block not like 'U%' or block is null) and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
            elif item == 'charset_zx':
                last_time = time.time() #
                sqlite_cursor.execute("UPDATE cangjie_table SET selected = 1 where code_value like 'zx%' and (block not like 'U%' or block is null) and selected is null;")
                sqlite_conn.commit()
                this_time = time.time() #
                # print(item+'\ttime'+': '+str(this_time-last_time)) #
            else:
                print('未實現功能:'+item)

            sqlite_conn.commit()
    sqlite_cursor.execute("SELECT count(distinct unicode_hex) FROM cangjie_table WHERE selected = '1';")
    rows = sqlite_cursor.fetchall()
    for row in rows:
        character_count = str(row[0])

    return character_count

# db 計算字符數量
def db_count_charset(sqlite_conn, sqlite_cursor):
    logging.debug(locals())
    sqlite_cursor.execute("DELETE FROM charset_count;")
    sqlite_cursor.execute(
        '''
        INSERT INTO charset_count
            SELECT block,COUNT(1) 
              FROM (SELECT distinct unicode_hex,block FROM cangjie_table)
             WHERE block IS NOT null
             GROUP BY block  
            UNION ALL
            SELECT 'OTHER',COUNT(1) 
              FROM (SELECT distinct unicode_hex,block FROM cangjie_table)
             WHERE (block IS null OR
                    block NOT IN ('U','UA','UB','UC','UD','UE','UF','UG','UH','UI',
                                  'CI','CIS','KR','RS','S','SP','CF','IDC','CRN',
                                  'PUA','PUAA','PUAB'))
            UNION ALL
            SELECT 'GB2312',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gb2312 = '1'
            UNION ALL
            SELECT 'GBK',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gbk = '1'
            UNION ALL
            SELECT 'HKSCS',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.hkscs = '1'
            UNION ALL
            SELECT 'BIG5',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.big5 = '1'
            UNION ALL
            SELECT 'GUI_FAN',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gui_fan IN ('LV_1','LV_2','LV_3','NOTE')
            UNION ALL
            SELECT 'GB18030_2022_L1',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gb18030 = '1'
               AND (t.gb18030_byte in ('1','2') OR
                    c.block IN ('U','UA'))
            UNION ALL
            SELECT 'GB18030_2022_L2',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gb18030 = '1'
               AND (t.gb18030_byte in ('1','2') OR
                    c.block IN ('U','UA') OR
					t.gui_fan IN ('LV_1','LV_2','LV_3','NOTE'))
            UNION ALL
            SELECT 'GB18030_2022_L3',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c, charset_table t
             WHERE c.unicode_hex = t.unicode_hex
               AND t.gb18030 = '1'
               AND (t.gb18030_byte in ('1','2') OR
                    c.block IN ('U','UA','UB','UC','UD','UE','UF','UG','UH','UI','KR'))
            UNION ALL
            SELECT 'YYY',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c
             WHERE c.code_value like 'yyy%'
               AND (c.block not like 'U%' or c.block is null)
            UNION ALL
            SELECT 'ZX',COUNT(DISTINCT c.unicode_hex) FROM cangjie_table c
             WHERE c.code_value like 'zx%'
               AND (c.block not like 'U%' or c.block is null);
        ''')
    sqlite_conn.commit()
    sqlite_cursor.execute("SELECT block,count FROM charset_count;")
    rows = sqlite_cursor.fetchall()
    return rows


# db 補全cangjie_table數據
def db_initialize_cangjie_table(sqlite_conn, sqlite_cursor):
    logging.debug(locals())
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
                    (SELECT u.name_abbr FROM unicode_block u WHERE c.unicode_dec >= u.start_dec AND c.unicode_dec <= u.end_dec) AS block, \
                    (SELECT u.area_no FROM unicode_block u WHERE c.unicode_dec >= u.start_dec AND c.unicode_dec <= u.end_dec) AS block_no \
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
    # 補全unicode_point (這些字符所在block與其script屬性不一致，為方便處理而按此表更新)
    sqlite_cursor.execute(
        '''
        SELECT c.id,
               (SELECT p.point FROM unicode_point p WHERE c.unicode_hex = p.unicode_hex) AS block,
               (SELECT b.area_no FROM unicode_point p,unicode_block b WHERE c.unicode_hex = p.unicode_hex AND p.point = b.name_abbr) AS block_no
          FROM cangjie_table c
         WHERE EXISTS (SELECT 1 FROM unicode_point p WHERE c.unicode_hex = p.unicode_hex);
        ''')
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
    sqlite_cursor.execute("SELECT count(distinct unicode_hex) from cangjie_table")
    rows = sqlite_cursor.fetchall()
    if rows:
        for row in rows:
            count_total = row[0]
    return count_total

# db 導入碼表數據
def db_insert_into_cangjie_table(sqlite_conn, sqlite_cursor, data_batch):
    # logging.debug(sqlite_cursor, data_batch)    # debug???
    sqlite_cursor.executemany('INSERT INTO cangjie_table (character_value, code_value, marks, id) VALUES (?, ?, ?, ?)', data_batch)

# db 導入基礎數據
def db_import_basic_data(sqlite_conn, sqlite_cursor, init_sql):
    logging.debug(locals())
    # print('db_import_basic_data()')
    # print(sqlite_conn, sqlite_cursor, init_sql)
    table_name = os.path.basename(init_sql).replace('.sql','')
    # print(table_name)
    key = 'last_'+table_name+'_hash'
    # 創建設定表
    sqlite_cursor.execute('CREATE TABLE IF NOT EXISTS "settings" ( \
                                setting_item        TEXT, \
                                setting_value       TEXT);')
    sqlite_conn.commit()
    # 計算這一次的sql文件hash
    with open(init_sql,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        this_data_table_hash = sha1obj.hexdigest()
    # 獲取上一次導入的sql文件hash
    sqlite_cursor.execute("SELECT setting_value FROM settings WHERE setting_item = ? ;", (key,))
    rows = sqlite_cursor.fetchall()
    if rows:
        for row in rows:
            last_data_file_hash = str(row[0])
    else:
        last_data_file_hash = ''
        sqlite_cursor.execute("INSERT INTO settings (setting_item, setting_value) VALUES (?, ?);", (key, this_data_table_hash))
        sqlite_conn.commit()
    # 判斷sql文件是否有變化
    if last_data_file_hash == this_data_table_hash:                 # 如果SQL文件無變化，則毋需重新導入
        # print('No changes: ','sql['+table_name+'] both['+this_data_table_hash+']')
        pass
    else:                                                              # 否則重新導入
        # print('Changes:','['+table_name+']','last['+last_data_file_hash+']','this['+this_data_table_hash+']')
        try:
            # 讀取建表sql文件
            with open(init_sql, 'r', encoding='utf8') as file:
                sql_commands = file.read().split(';')
            # 執行建表
            for command in sql_commands:
                sqlite_cursor.execute(command)
            sqlite_conn.commit()
            # 更新hash
            sqlite_cursor.execute("UPDATE settings SET setting_value= ? WHERE setting_item = ? ;", (this_data_table_hash, key))
            sqlite_conn.commit()
        except:
            print('[394]exception')

# db 創建數據庫並導入數據
def db_initialize(path, sqlite_conn, sqlite_cursor):
    logging.debug(locals())
    # print ('sqlite_conn[931]'+str(sqlite_conn))
    path['sql_settings']  = os.path.join(path['current_directory'],'sqlite','settings.sql')
    path['sql_build_temp'] = os.path.join(path['current_directory'],'sqlite','build_temp.sql')
    path['sql_build_final'] = os.path.join(path['current_directory'],'sqlite','build_final.sql')
    path['sql_cangjie_table'] = os.path.join(path['current_directory'],'sqlite','cangjie_table.sql')
    path['sql_unicode_block'] = os.path.join(path['current_directory'],'sqlite','unicode_block.sql')
    path['sql_charset_table'] = os.path.join(path['current_directory'],'sqlite','charset_table.sql')
    path['sql_charset_count'] = os.path.join(path['current_directory'],'sqlite','charset_count.sql')
    path['sql_unicode_point'] = os.path.join(path['current_directory'],'sqlite','unicode_point.sql')
    path['sql_templates'] = os.path.join(path['current_directory'],'sqlite','templates.sql')
    # 連接數據庫
    # if sqlite_conn == '':   # 若還沒有數據庫連接則創建，若有則沿用
    #     print('sqlite_conn為空')
    #     sqlite_conn = sqlite3.connect(path['sqlite_locate'])
    # else:
    #     print('sqlite_conn不為空')
    # sqlite_cursor = sqlite_conn.cursor()
    # print ('sqlite_conn[952]'+str(sqlite_conn))
    # 導入基礎數據
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_settings'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_unicode_block'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_unicode_point'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_charset_table'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_charset_count'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_build_temp'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_build_final'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_cangjie_table'])
    db_import_basic_data(sqlite_conn, sqlite_cursor, path['sql_templates'])
    return path, sqlite_conn, sqlite_cursor

def db_create_database(path):
    logging.debug(locals())
    # 數據庫文件路徑
    # path['sqlite_locate'] = os.path.join(path['current_directory'],'sqlite','cangjie.db')
    path['sqlite_locate'] = ':memory:'
    # path['sqlite_locate'] = 'G:/TEMP/cangjie.db'
    sqlite_conn = sqlite3.connect(path['sqlite_locate'])
    sqlite_cursor = sqlite_conn.cursor()

    return sqlite_conn, sqlite_cursor