# -*- coding: utf8 -*-
import sqlite3
import re
import os
import hashlib
import time

# 標記已選擇的字符
def mark_seleted_charset(sqlite_conn,sqlite_cursor,selected_options):
    sqlite_cursor.execute("UPDATE cangjie_table SET seleted = null where 1=1;")
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
    for item in selected_options:
        print(item)
        if item == 'charset_u':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'U' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ua':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UA' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ub':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UB' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uc':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UC' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ud':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UD' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ue':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UE' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uf':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UF' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ug':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UG' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_uh':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UH' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ui':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'UI' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_ci':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CI' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_cis':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CIS' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_kr':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'KR' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_rs':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'RS' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_s':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'S' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_sp':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'SP' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_cf':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CF' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_idc':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'IDC' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_crn':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'CRN' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_pua':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block in ('PUA','PUAA','PUAB') and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_other':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = 1 \
                                    WHERE (block IS NULL OR \
                                           block NOT IN ('U','UA','UB','UC','UD','UE','UF','UG','UH','UI', \
                                                         'CI','CIS','KR','RS','S','SP','CF','IDC','CRN', \
                                                         'PUA','PUAA','PUAB')) \
                                      AND seleted IS NULL;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
            last_time = this_time #
        elif item == 'charset_gb2312':
            last_time = time.time() #
            # 如果charset_table有這個字符，但是未測試過gb2312，則進行測試
            sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.gb2312 IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.seleted is NULL);")
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
            # print('start update seleted')
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.gb2312 = '1' \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
        elif item == 'charset_gbk':
            last_time = time.time() #
            # 如果charset_table有這個字符，但是未測試過gbk，則進行測試
            sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.gbk IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.seleted is NULL);")
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
            # print('start update seleted')
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.hkscs = '1' \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
        elif item == 'charset_hkscs':
            last_time = time.time() #
            # 如果charset_table有這個字符，但是未測試過hkscs，則進行測試
            sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.hkscs IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.seleted is NULL);")
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
            # print('start update seleted')
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.hkscs = '1' \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
        elif item == 'charset_big5':
            last_time = time.time() #
            # 如果charset_table有這個字符，但是未測試過big5，則進行測試
            sqlite_cursor.execute("SELECT s.unicode_hex, s.character_value FROM charset_table s WHERE s.big5 IS NULL AND EXISTS (SELECT 1 FROM cangjie_table c WHERE s.unicode_hex = c.unicode_hex AND c.seleted is NULL);")
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
                        print(character_value, 'yes')
                    else:
                        sqlite_cursor.execute("UPDATE charset_table SET big5 = '0' where unicode_hex = ? ;", (unicode_hex,))
                        sqlite_conn.commit()
                        print(character_value, 'no')
            # 測試完之後更新標記
            # print('start update seleted')
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.big5 = '1' \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
        elif item == 'charset_tygfhzb':
            last_time = time.time() #
            # 如果charset_table有這個字符，但是未測試過big5，則進行測試
            sqlite_cursor.execute("UPDATE charset_table SET tygfhzb = '0' where tygfhzb is null ;")
            sqlite_conn.commit()
            # 測試完之後更新標記
            # print('start update seleted')
            sqlite_cursor.execute("UPDATE cangjie_table \
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.tygfhzb <> '0' \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
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
					                                 AND c.seleted IS NULL);")
            rows = sqlite_cursor.fetchall()
            if rows:
                for row in rows:
                    can_be_encoded = False
                    unicode_hex = row[0]
                    character_value = row[1]
                    print('[337]'+character_value)
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
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.gb18030 = '1' \
                                      AND s.gb18030_byte in ('1','2') \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # 四字節的基本區和擴展A區
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block in ('U','UA') and seleted is null;")
            sqlite_conn.commit()
            # print('finished update seleted')
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
					                                 AND c.seleted IS NULL);")
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
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.gb18030 = '1' \
                                      AND s.gb18030_byte in ('1','2') \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # 四字節的基本區和擴展A區
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block in ('U','UA') and seleted is null;")
            sqlite_conn.commit()
            # 通用規範漢字表
            sqlite_cursor.execute("UPDATE cangjie_table \
                            SET seleted = '1' \
                        WHERE unicode_hex IN ( \
                        SELECT c.unicode_hex \
                            FROM cangjie_table c, charset_table s \
                        WHERE c.unicode_hex = s.unicode_hex \
                            AND s.tygfhzb <> '0' \
                            AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # print('finished update seleted')
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
					                                 AND c.seleted IS NULL);")
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
                                      SET seleted = '1' \
                                    WHERE unicode_hex IN ( \
                                   SELECT c.unicode_hex \
                                     FROM cangjie_table c, charset_table s \
                                    WHERE c.unicode_hex = s.unicode_hex \
                                      AND s.gb18030 = '1' \
                                      AND s.gb18030_byte in ('1','2') \
                                      AND c.seleted IS NULL );")
            sqlite_conn.commit()
            # 全部漢字
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block like 'U%' and seleted is null;")
            sqlite_conn.commit()
            # 康熙部首
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where block = 'KR' and seleted is null;")
            sqlite_conn.commit()
            # print('finished update seleted')
        elif item == 'charset_yyy':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where code_value like 'yyy%' and block not like 'U%' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
        elif item == 'charset_zx':
            last_time = time.time() #
            sqlite_cursor.execute("UPDATE cangjie_table SET seleted = 1 where code_value like 'zx%' and block not like 'U%' and seleted is null;")
            sqlite_conn.commit()
            this_time = time.time() #
            print(item+'\ttime'+': '+str(this_time-last_time)) #
        else:
            print('未實現功能:'+item)

        sqlite_conn.commit()
    sqlite_cursor.execute("SELECT count(distinct unicode_hex) FROM cangjie_table WHERE seleted = '1';")
    rows = sqlite_cursor.fetchall()
    for row in rows:
        character_count = str(row[0])

    return character_count

# 開始處理
def start_database_process(path):
    # 連接
    # print('AAA'+path['sqlite_locate'])
    sqlite_conn   = sqlite3.connect(path['sqlite_locate'])
    sqlite_cursor = sqlite_conn.cursor()

    # 導入基礎數據
    import_normal_data_table(sqlite_conn, sqlite_cursor, path['sql_settings'])
    import_normal_data_table(sqlite_conn, sqlite_cursor, path['sql_unicode_block'])
    last_time = time.time() #
    # print('import '+path['sql_charset_table'])
    import_normal_data_table(sqlite_conn, sqlite_cursor, path['sql_charset_table'])
    this_time = time.time() #
    print('import charset_table'+'\ttime'+': '+str(this_time-last_time)) #
    
    # 將碼表導入數據庫
    import_cangjie_table_from_source(sqlite_conn, path['source_file'], sqlite_cursor, path['sql_cangjie_table'])

    # 斷開
    if __name__ == '__main__':
        sqlite_conn.close()
    else:
        return sqlite_conn,sqlite_cursor

# 導入基礎數據表
def import_normal_data_table(sqlite_conn, sqlite_cursor, init_sql):
    table_name = os.path.basename(init_sql).replace('.sql','')
    key = 'last_'+table_name+'_hash'
    # 創建設定表
    sqlite_cursor.execute('CREATE TABLE IF NOT EXISTS "settings" ( \
                                setting_item        TEXT, \
                                setting_value       TEXT);')
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
    if last_data_file_hash == this_data_table_hash:                 # 如果碼表文件無變化，則毋需重新導入
        print('No changes: ','['+table_name+'] both['+this_data_table_hash+']')
        pass
    else:                                                              # 否則重新導入
        print('Changes:','['+table_name+']','last['+last_data_file_hash+']','this['+this_data_table_hash+']')
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
            last_source_file_hash = str(row[0])
    else:
        # print(this_source_file_hash)
        sqlite_cursor.execute("INSERT INTO settings (setting_item, setting_value) VALUES ('last_source_file_hash','"+this_source_file_hash+"');")
        sqlite_conn.commit()

    # last_source_file_hash = '123456'        # 每次都重新導入

    if last_source_file_hash == this_source_file_hash:                 # 如果碼表文件無變化，則毋需重新導入
        print('No changes: ','[cangjie_table] both['+this_source_file_hash+']')
        pass
    else:                                                              # 否則重新導入
        print('Changes:','[cangjie_table]','last['+last_source_file_hash+']','this['+this_source_file_hash+']')
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
            # sqlite_cursor.execute("UPDATE settings SET setting_value='"+this_source_file_hash+"';")
            sqlite_cursor.execute("UPDATE settings SET setting_value= ? WHERE setting_item = 'last_source_file_hash' ;", (this_source_file_hash,))
            sqlite_conn.commit()
            # last_source_file_hash = this_source_file_hash
        except:
            print('[450]exception')

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
    path['sql_charset_table'] = os.path.join(current_directory,'sqlite','charset_table.sql')

    source_file_hash = ''
    # source_file = 'E:/程式/GitHub/Cangjie5-dev/Cangjie5.txt'
    # sqlite_locate = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/cangjie.db'
    # sql_cangjie_table = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/cangjie_table.sql'
    # sql_unicode_block = 'E:/程式/GitHub/Cangjie5-dev/scripts/sqlite/unicode_block.sql'


    # sqlite_conn   = ''
    # sqlite_cursor = ''

    # start_database_process(path)