# -*- coding: utf8 -*-
# FUNCTION_RELATION
# gui_select_input_file()              選擇碼表文件
# gui_check_input_file_exists()        檢查輸入文件是否存在
# gui_select_output_file()             選擇輸出文件
# gui_update_template_value()          根據模板更新選項
# gui_enable_charset_filter()          字符集過濾開關
#    db_create_database()                  創建數據庫
#    cmd_read_source_to_database()         將源碼表讀入數據庫
#    gui_charset_filter_option()           顯示字符集過濾選項
#        db_config_setting()                   讀取上一次的配置
#    gui_count_charset_selected()          計算過濾後字符數量
#        db_mark_selected_charset()            標記已選擇的字符集
#    gui_select_charset_all()              字符集選項全選
#    gui_select_charset_none()             字符集選項清空
#    gui_save_charset_option()             保存字符集選項
#    gui_show_charset_help_message()       字符集幫助說明
# gui_go_build_with_db()               轉換
#    db_build_final_table()                生成碼表
#    db_export_final_table()               從數據庫取出碼表
#    cmd_write_output_template()           輸出文件模板
#    cmd_write_output_txt()                輸出文件正文
# db_get_setting()                     讀取配置
# db_config_setting()                  更新配置

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import platform
import webbrowser
import textwrap
import logging
from buildToolCmd import cmd_read_source_to_database # type: ignore
from buildToolCmd import cmd_write_output_template # type: ignore
from buildToolCmd import cmd_write_output_txt # type: ignore
from buildToolDatabase import db_mark_selected_charset # type: ignore
from buildToolDatabase import db_config_setting # type: ignore
from buildToolDatabase import db_get_setting # type: ignore
from buildToolDatabase import db_build_final_table # type: ignore
from buildToolDatabase import db_export_final_table # type: ignore
from buildToolDatabase import db_create_database # type: ignore

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(filename)s][%(lineno)d] - %(funcName)s() - %(message)s')

# 選擇輸入文件
def gui_select_input_file():
    logging.debug(locals())
    global path
    # print(type(path))
    # print(path)
    path = {}
    path['current_directory'] = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    path['parent_directory'] = os.path.dirname(path['current_directory'])     # 獲取上級目錄
    path['source_locate'] = filedialog.askopenfilename(title="選擇碼表文件", 
                                                 initialdir=path['parent_directory'], 
                                                 filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    # print('input_file_path='+input_file_path)
    if path['source_locate']:
        input_file_entry.delete(0, tk.END)           # 清空輸入文件的值
        input_file_entry.insert(0, path['source_locate'])  # 設置輸入文件的值
        if output_file_selected=='no':               # 如果已經手工選擇了輸出文件就不要更改
            output_file_defaule_value = input_file_entry.get().replace('.txt','_output.txt').replace('\\', '/')
            output_file_entry.delete(0, tk.END)
            output_file_entry.insert(0, output_file_defaule_value)      # 設置輸出文件的值
            path['output_locate'] = output_file_defaule_value
            # print("path['output_locate']="+path['output_locate'])
        gui_enable_charset_filter(path)     # 重新計算字符集
        selected_options = []
        last_charset_option =  db_get_setting(sqlite_cursor, 'last_charset_option').split()
        for value in last_charset_option:
            value = value.strip(",'][")
            selected_options.append(value)
        # print('selected_options='+str(selected_options))
        character_count_selected= db_mark_selected_charset(sqlite_conn,sqlite_cursor,selected_options)
        charset_filter_message.config(text='字符數: '+format(int(character_count_total), ',d')+' -> '+format(int(character_count_selected), ',d'))

    result_label.config(text="")    # 重新選擇之後清空結果

# 檢查輸入文件是否存在
def gui_check_input_file_exists(path):
    logging.debug(locals())
    # print("checked")
    if path=='':
        pass
    elif not os.path.isfile(path):
        input_file_message.config(text="文件不存在")

# 選擇輸出文件
def gui_select_output_file():
    logging.debug(locals())
    global path
    output_file_path = filedialog.asksaveasfilename(title="保存到", 
                                                    initialdir=path['parent_directory'],
                                                    defaultextension=".txt",
                                                    filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
    if output_file_path:
        output_file_entry.delete(0, tk.END)           # 清空輸出文件的值
        output_file_entry.insert(0, output_file_path) # 設置輸出文件的值
        # print('output_file_path='+output_file_path)
    global output_file_selected
    output_file_selected = 'yes'                      # 標記已手工選擇輸出文件
    path['output_locate'] = output_file_path
    result_label.config(text="")    # 重新選擇之後清空結果

# 根據模板更新選項
def gui_update_template_value(*args):
    logging.debug(locals())
    global template_value
    global order_option
    global order_button
    global order_value
    global delimiter_option
    global delimiter_button
    global delimiter_value
    global linebreak_option
    global linebreak_button
    global linebreak_value
    template_value = template_button_selected.get()
    # print("template_value="+template_value)
    result_label.config(text="")                        # 重新選擇之後清空結果
    if template_value == 'text':                     # 如果選擇了模版，則限制下面的選項
        for i, (value, text) in enumerate(order_option):        # 顺序
            order_button[value].config(state="normal")
        for i, (value, text) in enumerate(delimiter_option):    # 分隔符
            delimiter_button[value].config(state="normal")
        for i, (value, text) in enumerate(linebreak_option):    # 換行符
            linebreak_button[value].config(state="normal")
    elif template_value == 'rime':
        order_button_selected.set('char')                                 # 順序設置為char
        for i, (value, text) in enumerate(order_option):
            if value in ['char']:
                order_button[value].config(state="normal")
            else:
                order_button[value].config(state="disable")
        delimiter_button_selected.set('tab')                              # 分隔符設置為tab
        for i, (value, text) in enumerate(delimiter_option):
            if value in ['tab']:
                delimiter_button[value].config(state="normal")
            else:
                delimiter_button[value].config(state="disable")
        linebreak_button_selected.set('auto')                             # 換行符設置為auto
        for i, (value, text) in enumerate(linebreak_option):
                linebreak_button[value].config(state="normal")
    elif template_value == 'fcitx':
        order_button_selected.set('code')                                 # 順序設置為code
        for i, (value, text) in enumerate(order_option):
            if value in ['code']:
                order_button[value].config(state="normal")
            else:
                order_button[value].config(state="disable")
        delimiter_button_selected.set('space')                            # 分隔符設置為space
        for i, (value, text) in enumerate(delimiter_option):
            if value in ['space']:
                delimiter_button[value].config(state="normal")
            else:
                delimiter_button[value].config(state="disable")
        linebreak_button_selected.set('lf')                               # 換行符設置為lf
        for i, (value, text) in enumerate(linebreak_option):
            if value in ['lf']:
                linebreak_button[value].config(state="normal")
            else:
                linebreak_button[value].config(state="disable")
    elif template_value == 'yong':                              # 順序設置為code
        order_button_selected.set('code')
        for i, (value, text) in enumerate(order_option):
            if value in ['code']:
                order_button[value].config(state="normal")
            else:
                order_button[value].config(state="disable")
        delimiter_button_selected.set('multi')                            # 分隔符設置為multi
        for i, (value, text) in enumerate(delimiter_option):
            if value in ['multi']:
                delimiter_button[value].config(state="normal")
            else:
                delimiter_button[value].config(state="disable")
        linebreak_button_selected.set('crlf')                               # 換行符設置為lf
        for i, (value, text) in enumerate(linebreak_option):
            if value in ['crlf']:
                linebreak_button[value].config(state="normal")
            else:
                linebreak_button[value].config(state="disable")
    order_value = order_button_selected.get()
    delimiter_value = delimiter_button_selected.get()
    linebreak_value = linebreak_button_selected.get()
    # print('order_value='+order_value)
    # print('delimiter_value='+delimiter_value)
    # print('linebreak_value='+linebreak_value)

# 計算過濾後字符數量
def gui_count_charset_selected():
    logging.debug(locals())
    # print('RUN gui_count_charset_selected()')
    selected_options = []
    global charset_checkbutton_dict
    for value in charset_checkbutton_dict:
        if charset_checkbutton_dict[value].get():
            # print(value)
            selected_options.append(value)
    global sqlite_conn
    global sqlite_cursor
    global character_count_selected
    character_count_selected= db_mark_selected_charset(sqlite_conn,sqlite_cursor,selected_options)
    global charset_count_message
    charset_count_message.config(text='過濾後字符數: '+format(int(character_count_selected), ',d'))
    # print(character_count)
    # print(charset_checkbutton)
    # for value in charset_unicode_list:
    # for i, (value, text) in enumerate(charset_list):
    #     if charset_checkbutton[value].get():
    #         selected_options.append(f"{value}")
    # for i, (value, text) in enumerate(charset_unicode_list):
    #     if charset_checkbutton[value].get():
    #         selected_options.append(f"{value}")
    # for i, (value, text) in enumerate(charset_other_list):
    #     if charset_checkbutton[value].get():
    #         selected_options.append(f"{value}")
    # print('selected_option='+selected_options)

# 字符集選項全選
def gui_select_charset_all(event, charset_cjk_list,charset_unicode_list,charset_other_list):
    logging.debug(locals())
    for i, (value, text) in enumerate(charset_cjk_list):
        charset_checkbutton_dict[value].set(1)
    for i, (value, text) in enumerate(charset_unicode_list):
        charset_checkbutton_dict[value].set(1)
    for i, (value, text) in enumerate(charset_other_list):
        charset_checkbutton_dict[value].set(1)
    gui_count_charset_selected()
    
# 字符集選項清空
def gui_select_charset_none(event, charset_cjk_list,charset_unicode_list,charset_other_list):
    logging.debug(locals())
    for i, (value, text) in enumerate(charset_cjk_list):
        charset_checkbutton_dict[value].set(0)
    for i, (value, text) in enumerate(charset_unicode_list):
        charset_checkbutton_dict[value].set(0)
    for i, (value, text) in enumerate(charset_other_list):
        charset_checkbutton_dict[value].set(0)
    gui_count_charset_selected()

# 保存字符集選項
def gui_save_charset_option(charset_filter_window):
    logging.debug(locals())
    selected_options = []
    global charset_checkbutton_dict
    for value in charset_checkbutton_dict:
        if charset_checkbutton_dict[value].get():
            # print(value)
            selected_options.append(value)
    db_config_setting(sqlite_conn, sqlite_cursor, 'last_charset_option',str(selected_options))
    charset_filter_window.destroy()     # 關閉窗口
    # charset_filter_message.config(text='過濾後的字符數量: '+format(int(character_count_selected), ',d'))
    charset_filter_message.config(text='字符數: '+format(int(character_count_total), ',d')+' -> '+format(int(character_count_selected), ',d'))
    # global charset_filter_message_status
    # charset_filter_message_status = 'count_selected'

# 字符集過濾開關
def gui_enable_charset_filter(path):
    logging.debug(locals())
    global character_count_total            # 過濾前字符數
    global character_count_selected         # 過濾後字符數
    if charset_filter_enable_button_selected.get():
        charset_filter_option_button.config(state="normal")
        global sqlite_conn
        global sqlite_cursor
        global count_charset_result
        if sqlite_conn == '':
            sqlite_conn, sqlite_cursor = db_create_database(path)                 # 創建數據庫
        result, path, sqlite_conn, sqlite_cursor, character_count_total, count_charset_result = cmd_read_source_to_database(path, sqlite_conn, sqlite_cursor)
        # if result == 'ERR_SOURCE_FILE_NOT_FOUND':
        #     charset_filter_message.config(text='源碼表文件不存在', fg='red')
        # elif result == 'ERR_SOURCE_FILE_FAIL_TO_READ':
        #     charset_filter_message.config(text='源碼表文件讀取失敗', fg='red')
        # elif result == 'ERR_SOURCE_FILE_FORMAT_NOT_SUPPORT':
        #     charset_filter_message.config(text='不支持的源碼表文件格式', fg='red')

        charset_filter_message.config(text='正在讀取數據')
        # character_count_total = count_total
        # global count_charset_result 
        # count_charset_result = count_charset    # 每個字符集的字數
        # global charset_filter_message_status    # 顯示甚麼提示
    else:
        charset_filter_option_button.config(state="disable")

    try:
        result
        if result == 'SUCCESS':
            if character_count_selected == '':
                charset_filter_message.config(text='字符數: '+format(int(character_count_total), ',d')+' -> 0', fg='RoyalBlue')
            else:
                charset_filter_message.config(text='字符數: '+format(int(character_count_total), ',d')+' -> '+format(int(character_count_selected), ',d'), fg='RoyalBlue')
        elif result == 'ERR_SOURCE_FILE_NOT_FOUND':
            charset_filter_message.config(text='源碼表文件不存在', fg='red')
        elif result == 'ERR_SOURCE_FILE_FAIL_TO_READ':
            charset_filter_message.config(text='源碼表文件讀取失敗', fg='red')
        elif result == 'ERR_SOURCE_FILE_FORMAT_NOT_SUPPORT':
            charset_filter_message.config(text='不支持的源碼表文件格式', fg='red')
    except:
        pass



# 字符集幫助說明
def gui_show_charset_help_message(event):
    logging.debug(locals())
    # 創建提示窗口
    charset_message_window = tk.Toplevel(window)
    charset_message_window.title("字符集過濾說明")
    # 獲取主窗口位置和大小
    root_x = window.winfo_x()
    root_y = window.winfo_y()
    root_width = window.winfo_width()
    root_height = window.winfo_height()
    # 設置提示窗口的大小
    charset_message_window.geometry("560x380")
    # 設置提示窗口的位置在正中間
    charset_message_window.update_idletasks()  # 更新窗口信息
    new_window_width = charset_message_window.winfo_width()
    new_window_height = charset_message_window.winfo_height()
    new_x = root_x + (root_width - new_window_width) // 2
    new_y = root_y + (root_height - new_window_height) // 2
    charset_message_window.geometry(f"+{new_x}+{new_y}")
    # 文字
    message_label = tk.Label(charset_message_window, 
                            anchor='w', justify='left', wraplength=540,
                            text=textwrap.dedent('''\
                                過濾結果取已選項目的併集。\n
                                例如選取「CJK 基本區」及「HKSCS-2016」，過濾結果會包含 HKSCS 中的 Unicode 擴展區漢字。\n
                                【注意】在本程式的選項中：\n
                                「CJK 基本區」包含：
                                﨎(U+FA0E), 﨏(U+FA0F), 﨑(U+FA11), 﨓(U+FA13), 﨔(U+FA14), 﨟(U+FA1F),
                                﨡(U+FA21), 﨣(U+FA23), 﨤(U+FA24), 﨧(U+FA27), 﨨(U+FA28), 﨩(U+FA29).
                                而「兼容漢字」不包含上述字符。\n
                                「CJK 基本區」包含：〇(U+3007)
                                而「符號標點」不包含上述字符。\n
                                「表意文字描述字符」包含：〾(U+303E), ㇯(U+31EF)
                                而「符號標點」及「筆畫」不包含上述字符。\n
                                「通用規範漢字表」包含：〇(U+3007)
                                「〇(U+3007)」並未出現在該表的正文，而是出現在腳註。
                                ''')
                            )
    message_label.pack(padx=10, pady=10)
    # 關閉按鈕
    close_button = tk.Button(charset_message_window,  text="關閉", width=10, command=charset_message_window.destroy)
    close_button.pack(pady=0)
    # 設置焦點
    charset_message_window.focus_set()

# 字符集過濾選項
def gui_charset_filter_option():
    logging.debug(locals())
    charset_filter_window = tk.Toplevel(window)
    charset_filter_window.title("字符集過濾選項")
    # charset_filter_window.geometry("300x200")
    
    # 獲取主窗口位置和大小
    root_x = window.winfo_x()
    root_y = window.winfo_y()
    new_x = root_x + 15
    new_y = root_y + 15
    charset_filter_window.geometry(f"+{new_x}+{new_y}")
    # 框架
    charset_filter_frame = tk.Frame(charset_filter_window)
    charset_filter_frame.pack(padx=50, pady=20)
    # 統一漢字
    character_count_label = tk.Label(charset_filter_frame, text='▪  Unicode CJK 統一漢字')
    character_count_label.grid(row=0, column=0, columnspan=4, pady=4, sticky='w')
    charset_help_label = tk.Label(charset_filter_frame, text="* 說明", fg="blue", relief="flat")
    charset_help_label.grid(row=0, column=9, sticky='w')
    charset_help_label.bind("<Button-1>", gui_show_charset_help_message)
    charset_checkbutton = {}
    # global charset_checkbutton
    global charset_checkbutton_dict
    # charset_checkbutton_dict = {}
    global charset_count  # 計數
    # charset_count = {}  # 計數
    charset_cjk_list = [('charset_u', '基本區 *'), ('charset_ua', '擴展區 A'), 
                        ('charset_ub', '擴展區 B'), ('charset_uc', '擴展區 C'), 
                        ('charset_ud', '擴展區 D'), ('charset_ue', '擴展區 E'), 
                        ('charset_uf', '擴展區 F'), ('charset_ug', '擴展區 G'),
                        ('charset_uh', '擴展區 H'), ('charset_ui', '擴展區 I')]
    # for i in range(len(charset_unicode_list)):
    for i, (value, text) in enumerate(charset_cjk_list):
        charset_checkbutton_dict[value] = tk.IntVar()
        charset_checkbutton[value] = tk.Checkbutton(charset_filter_frame, text=text, variable=charset_checkbutton_dict[value], command=lambda: gui_count_charset_selected())
        charset_checkbutton[value].grid(row=1+i//5, column=(i%5)*2, padx=5, pady=4, sticky='w')
        # print(i%5)
        # print('EEE')
        # print(charset_count)
        # charset_count[value] = tk.Label(charset_filter_frame, text='0', fg='PaleGreen4')
        if value not in count_charset_result:
            count_charset_result[value] = 0
        charset_count[value] = tk.Label(charset_filter_frame, text=format(int(count_charset_result[value]), ',d'), fg='PaleGreen4')
        charset_count[value].grid(row=1+i//5, column=(i%5)*2+1, padx=0, pady=4, sticky='e')
        # checkbutton[value].config(state=tk.DISABLED)
    
    # 其他區塊
    character_count_label = tk.Label(charset_filter_frame, text='▪  Unicode 其他區塊')
    character_count_label.grid(row=4, column=0, columnspan=4, pady=4, sticky='w')
    charset_unicode_list = [('charset_ci', '兼容漢字'), ('charset_cis', '兼容漢字增補'), 
                            ('charset_kr', '康熙部首'), ('charset_rs', '部首增補'), 
                            ('charset_s', '筆畫 *'), ('charset_sp', '符號標點 *'), 
                            ('charset_cf', '兼容符號'), ('charset_idc', '表意文字描述字符 *'),
                            ('charset_crn', '算籌符號'), ('charset_pua', '私用區 (PUA+SPUA)'),
                            ('charset_other', '未列出的其他區塊')]
    for i, (value, text) in enumerate(charset_unicode_list):
        charset_checkbutton_dict[value] = tk.IntVar()
        charset_checkbutton[value] = tk.Checkbutton(charset_filter_frame, text=text, variable=charset_checkbutton_dict[value], command=lambda: gui_count_charset_selected())
        charset_checkbutton[value].grid(row=5+i//5, column=(i%5)*2, padx=5, pady=4, sticky='w')
        if value not in count_charset_result:
            count_charset_result[value] = 0
        charset_count[value] = tk.Label(charset_filter_frame, text=format(int(count_charset_result[value]), ',d'), fg='PaleGreen4')
        charset_count[value].grid(row=5+i//5, column=(i%5)*2+1, padx=5, pady=4, sticky='e')
        # checkbutton[value].config(state=tk.DISABLED)
    # 其他劃分
    character_count_label = tk.Label(charset_filter_frame, text='▪  其他劃分')
    character_count_label.grid(row=8, column=0, columnspan=4, pady=4, sticky='w')
    charset_other_list = [('charset_gb2312', 'GB/T 2312-1980'), 
                          ('charset_gbk', 'GBK'), 
                          ('charset_gb18030_2022_l1', 'GB 18030-2022 級別1'), 
                          ('charset_gb18030_2022_l2', 'GB 18030-2022 級別2'), 
                          ('charset_gb18030_2022_l3', 'GB 18030-2022 級別3'),
                          ('charset_big5','Big5'),
                          ('charset_hkscs', 'HKSCS-2016'),
                          ('charset_gui_fan', '通用規範漢字表 *'),
                          ('charset_yyy', 'YYY 開頭的標點符號'),
                          ('charset_zx', 'ZX 開頭的標點符號')]
    for i, (value, text) in enumerate(charset_other_list):
        charset_checkbutton_dict[value] = tk.IntVar()
        charset_checkbutton[value] = tk.Checkbutton(charset_filter_frame, text=text, variable=charset_checkbutton_dict[value], command=lambda: gui_count_charset_selected())
        charset_checkbutton[value].grid(row=9+i//5, column=(i%5)*2, padx=5, pady=4, sticky='w')
        if value not in count_charset_result:
            count_charset_result[value] = 0
        charset_count[value] = tk.Label(charset_filter_frame, text=format(int(count_charset_result[value]), ',d'), fg='PaleGreen4')
        charset_count[value].grid(row=9+i//5, column=(i%5)*2+1, padx=5, pady=4, sticky='e')
    # 關閉按鈕
    # close_button = tk.Button(charset_filter_frame, text="確定", width=10, command=charset_filter_window.destroy)
    close_button = tk.Button(charset_filter_frame, text="確定", width=10, command=lambda: gui_save_charset_option(charset_filter_window))
    close_button.grid(row=20, column=0, pady=10)
    # 全選&清空
    select_frame = tk.Frame(charset_filter_frame)
    select_frame.grid(row=20, column=2)
    select_all_label = tk.Label(select_frame, text="全選", fg="blue", relief="flat")
    select_all_label.grid(row=0, column=0, padx=5, sticky='w')
    select_all_label.bind("<Button-1>", lambda event: gui_select_charset_all(event, charset_cjk_list,charset_unicode_list,charset_other_list))
    select_all_label = tk.Label(select_frame, text="清空", fg="blue", relief="flat")
    select_all_label.grid(row=0, column=1, padx=5, sticky='w')
    select_all_label.bind("<Button-1>", lambda event: gui_select_charset_none(event, charset_cjk_list,charset_unicode_list,charset_other_list))
    # 提示文字
    global charset_count_message
    charset_count_message = tk.Label(charset_filter_frame, text="過濾後字符數: 0", fg='RoyalBlue')
    charset_count_message.grid(row=20, column=6, columnspan=2, padx=0, pady=0, sticky='w')
    # 讀取上一次的選擇
    if sqlite_cursor == '':
        last_charset_option = ''
    else:
        last_charset_option = db_get_setting(sqlite_cursor, 'last_charset_option').split()
        # print(last_charset_option)
    for value in last_charset_option:
        value = value.strip(",'][")
        charset_checkbutton_dict[value].set(1)
    gui_count_charset_selected()
    # 設置焦點
    charset_filter_window.focus_set()

# 轉換
def gui_go_build_with_db():
    logging.debug(locals())
    result_label.config(text="正在處理", fg='RoyalBlue')    # 重新選擇之後清空結果
    global sqlite_conn
    global sqlite_cursor
    global template_value
    global order_value
    global delimiter_value
    global linebreak_value
    global path
    source_basename = os.path.basename(path['source_locate'])
    if sqlite_cursor == '':
        sqlite_conn, sqlite_cursor = db_create_database(path)                 # 創建數據庫
    # print('[404]', sqlite_conn, sqlite_cursor)
    result, path, sqlite_conn, sqlite_cursor, character_count_total, count_charset_result = cmd_read_source_to_database(path, sqlite_conn, sqlite_cursor)  # 導入數據
    if result == 'SUCCESS':
        if charset_filter_enable_button_selected.get():
            db_build_final_table(sqlite_conn, sqlite_cursor, '')                    # 生成碼表
        else:
            selected_options = ['charset_all']
            # character_count_selected= db_mark_selected_charset(sqlite_conn,sqlite_cursor,selected_options)
            db_build_final_table(sqlite_conn, sqlite_cursor, selected_options)
        output_data = db_export_final_table(sqlite_conn, sqlite_cursor)   # 從數據庫導出碼表
        # order, delimiter, linebreak = cmd_write_output_template(sqlite_cursor, output, template, order, delimiter, linebreak, source_basename)  # 寫入模板
        output = path['output_locate']
        template = template_value
        order = order_value
        delimiter = delimiter_value
        linebreak = linebreak_value
        order, delimiter, linebreak = cmd_write_output_template(sqlite_cursor, output, template, order, delimiter, linebreak, source_basename)  # 寫入模板
        # print(sqlite_cursor, output, template, order, delimiter, linebreak, source_basename)
        cmd_write_output_txt(output, output_data, order, delimiter, linebreak)
        result_label.config(text='轉換成功', fg='green')
    elif result == 'ERR_SOURCE_FILE_NOT_FOUND':
        result_label.config(text='源碼表文件不存在', fg='red')
    elif result == 'ERR_SOURCE_FILE_FAIL_TO_READ':
        result_label.config(text='源碼表文件讀取失敗', fg='red')
    elif result == 'ERR_SOURCE_FILE_FORMAT_NOT_SUPPORT':
        result_label.config(text='不支持的源碼表文件格式', fg='red')
    

    # db_build_final_table(sqlite_conn, sqlite_cursor, charset)         # 生成碼表
    # output_data = db_export_final_table(sqlite_conn, sqlite_cursor)   # 從數據庫導出碼表
    # order, delimiter, linebreak = cmd_write_output_template(sqlite_cursor, output, template, order, delimiter, linebreak, source_basename)  # 寫入模板
    # cmd_write_output_txt(output, output_data, order, delimiter, linebreak)  # 寫入正文

    # result, path, sqlite_conn, sqlite_cursor, character_count_total, count_charset_result = cmd_read_source_to_database(path)   # 讀入數據庫
    # # db_build_final_table(sqlite_conn, sqlite_cursor)
    # if charset_filter_enable_button_selected.get():
    #     db_build_final_table(sqlite_conn, sqlite_cursor, '')
    # else:
    #     selected_options = ['charset_all']
    #     # character_count_selected= db_mark_selected_charset(sqlite_conn,sqlite_cursor,selected_options)
    #     db_build_final_table(sqlite_conn, sqlite_cursor, selected_options)
    # # gui_count_charset_selected()
    # output_data = db_export_final_table(sqlite_conn, sqlite_cursor)   # 從數據庫導出碼表
    # for item in output_data:
    #     print(item)
    # output = path['output_locate']
    # template = template_button_selected.get()
    # linebreak = linebreak_button_selected.get()
    # source_basename = os.path.basename(path['source_locate'])
    # order, delimiter, linebreak = cmd_write_output_template(sqlite_cursor, output, template, order_value, delimiter_value, linebreak, source_basename)    # 寫入模版
    # # print('len='+len(output_data))
    # cmd_write_output_txt(output, output_data, order, delimiter, linebreak)  # 寫入正文
    # print('OK')

if __name__ == "__main__":

    debug = True
    # 全局變量
    path = {}
    path['current_directory'] = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    path['parent_directory'] = os.path.dirname(path['current_directory'])     # 獲取上級目錄
    sqlite_conn = ''                # 數據庫連接
    sqlite_cursor = ''              # 數據庫指針
    output_file_selected = 'no'     # 是否已手工選擇輸出文件
    charset_count = {}              # 字符集字數tk.Label
    count_charset_result = {}       # 字符集字數dict
    charset_checkbutton_dict = {}   # 字符集多選框的值 charset_checkbutton_dict[value] = tk.IntVar()
    charset_count_message = ''      # 字符集過濾選項中的字數統計文字
    character_count_total = ''      # 過濾前的字符數
    character_count_selected = ''   # 過濾後的字符數
    # charset_filter_message_status = 'notice'
    template_value = 'text'         # 默認值
    order_value = 'char'
    delimiter_value = 'tab'
    linebreak_value = 'auto'

    # 建立主窗口
    window = tk.Tk()
    window.title('補完計劃碼表轉換工具 v0.2 beta')
    # window.geometry('800x400')
    window.resizable(False, False)

    # 建立框架容器，用于放置文本框和按钮
    frame = tk.Frame(window)
    frame.pack(padx=30, pady=10)

    # 輸入文件
    input_file_label = tk.Label(frame, text="碼表文件:")
    input_file_label.grid(row=0, column=0, pady=5, sticky='e')
    input_file_entry = tk.Entry(frame, width=75)
    input_file_entry.grid(row=0, column=1, columnspan=4, padx=5, pady=0, sticky='w')
    path['source_locate'] = os.path.join(path['parent_directory'],'Cangjie5.txt').replace('\\', '/')     # 輸入文件默認值
    if platform.system().lower() == 'windows':                                                              # 在Windows上將盤符顯示為大寫
        path['source_locate'] = path['source_locate'][0].upper() + path['source_locate'][1:]
    input_file_entry.insert(0, path['source_locate'])
    input_file_button = tk.Button(frame, text='選擇', width=10, command=gui_select_input_file)
    input_file_button.grid(row=0, column=5, padx=5, pady=0, sticky='w')
    input_file_message = tk.Label(frame, text="")   # 默認提示為空白
    input_file_message.grid(row=1, column=1, columnspan=4, padx=5, pady=0, sticky='w')
    # 輸出文件
    output_file_label = tk.Label(frame, text="輸出文件:")
    output_file_label.grid(row=2, column=0, pady=5, sticky='e')
    output_file_entry = tk.Entry(frame, width=75)
    output_file_entry.grid(row=2, column=1, columnspan=4, padx=5, pady=0, sticky='w')
    output_file_defaule_value = path['source_locate'].replace('.txt','_output.txt').replace('\\', '/')
    output_file_entry.insert(0, output_file_defaule_value)
    path['output_locate'] = output_file_defaule_value
    output_file_button = tk.Button(frame, text='選擇', width=10, command=gui_select_output_file)
    output_file_button.grid(row=2, column=5, padx=5, pady=0, sticky='w')
    output_file_message = tk.Label(frame, text="")  # 默認提示為空白
    output_file_message.grid(row=3, column=1, columnspan=4, padx=5, pady=0, sticky='w')
    # 模版
    template_label = tk.Label(frame, text="模板:")
    template_label.grid(row=4, column=0, pady=4, sticky='e')
    template_option = [('text', '(無)'), ('rime', 'RIME'), ('fcitx', 'Fcitx 5'), ('yong', '小小輸入法')]
    template_button_selected = tk.StringVar(value="text")     # 默認值
    template_button = {}
    for i, (value, text) in enumerate(template_option):
        this_button = tk.Radiobutton(frame, text=text, variable=template_button_selected, value=value)
        this_button.grid(row=4, column=i+1, padx=5, pady=4, sticky='w')
        template_button[value] = this_button
    template_button_selected.trace_add("write", gui_update_template_value)
    # 順序
    order_label = tk.Label(frame, text="行內順序:")
    order_label.grid(row=5, column=0, pady=4, sticky='e')
    order_option = [('char','字在前'), ('code','倉頡碼在前')]
    order_button_selected = tk.StringVar(value="char")        # 默認值
    order_button = {}
    for i, (value, text) in enumerate(order_option):
        this_button = tk.Radiobutton(frame, text=text, variable=order_button_selected, value=value)
        this_button.grid(row=5, column=i+1, padx=5, pady=4, sticky='w')
        order_button[value] = this_button
    def update_order_value(*args):
        global order_value
        order_value = order_button_selected.get()
        # print("order_value="+order_value)
    order_button_selected.trace_add("write", update_order_value)
    # 分隔符
    delimiter_label = tk.Label(frame, text="行內分隔符:")
    delimiter_label.grid(row=6, column=0, pady=4, sticky='e')
    delimiter_option = [('tab','Tab (製表鍵)'), ('space','單個空格'), ('multi','以空格代替Tab對齊'), ('none','(無)')]
    delimiter_button_selected = tk.StringVar(value="tab")        # 默認值
    delimiter_button = {}
    for i, (value, text) in enumerate(delimiter_option):
        this_button = tk.Radiobutton(frame, text=text, variable=delimiter_button_selected, value=value)
        this_button.grid(row=6, column=i+1, padx=5, pady=4, sticky='w')
        delimiter_button[value] = this_button
    def update_delimiter_value(*args):
        global delimiter_value
        delimiter_value = delimiter_button_selected.get()
        # print("delimiter_value="+delimiter_value)
    delimiter_button_selected.trace_add("write", update_delimiter_value)
    # 換行符
    linebreak_label = tk.Label(frame, text="換行符:")
    linebreak_label.grid(row=7, column=0, pady=4, sticky='e')
    linebreak_option = [('auto','與系統一致'), ('crlf','CRLF (Windows)'), ('lf','LF (Linux / macOS)'), ('cr','CR (Mac OS, 舊版)')]
    linebreak_button_selected = tk.StringVar(value="auto")        # 默認值
    linebreak_button = {}
    for i, (value, text) in enumerate(linebreak_option):
        this_button = tk.Radiobutton(frame, text=text, variable=linebreak_button_selected, value=value)
        this_button.grid(row=7, column=i+1, padx=5, pady=4, sticky='w')
        linebreak_button[value] = this_button
    def update_linebreak_value(*args):
        global linebreak_value
        linebreak_value = linebreak_button_selected.get()
        # print("linebreak_value="+linebreak_value)
    linebreak_button_selected.trace_add("write", update_linebreak_value)
    # 字符集過濾
    charset_filter_label = tk.Label(frame, text="字符集過濾:")
    charset_filter_label.grid(row=8, column=0, pady=4, sticky='e')
    charset_filter_frame = tk.Frame(frame)
    charset_filter_frame.grid(row=8, column=1, padx=0, pady=4)
    charset_filter_enable_button_selected = tk.IntVar()                  # 默認值
    charset_filter_enable_button = tk.Checkbutton(charset_filter_frame, text='啟用', variable=charset_filter_enable_button_selected, command=lambda: gui_enable_charset_filter(path))
    charset_filter_enable_button.grid(row=8, column=1, padx=0, sticky='w')
    charset_filter_option_button = tk.Button(frame, text='選項', width=10, command=gui_charset_filter_option)
    charset_filter_option_button.grid(row=8, column=2, padx=0, sticky='w')
    charset_filter_option_button.config(state="disable")
    charset_filter_message = tk.Label(frame, text="", fg='RoyalBlue')
    # if charset_filter_message_status == 'notice':                              # 默認提示信息
    #     charset_filter_message.config(text="過濾器讀取數據可能需要較長時間")
    charset_filter_message.config(text="過濾器讀取數據可能需要較長時間")            # 默認提示信息
    charset_filter_message.grid(row=8, column=3, columnspan=2, padx=0, pady=0, sticky='w')
    # 空白行
    # empty_label = tk.Label(frame, text=" ")
    # empty_label.grid(row=9, column=0, pady=4, sticky='e')
    # 轉換按鈕
    build_button = tk.Button(frame, text='轉換', width=10, command=gui_go_build_with_db)
    build_button.grid(row=19, column=0, columnspan=2, pady=20)
    result_label = tk.Label(frame, text="轉換結果")
    result_label.configure(text="")
    result_label.grid(row=19, column=2, pady=20, sticky='w')
    # 信息
    imformation_label = tk.Label(frame, text="倉頡五代補完計劃", fg="gray")
    imformation_label.grid(row=20, column=0, columnspan=1, pady=0)
    url_label = tk.Label(frame, text="https://github.com/Jackchows/Cangjie5", fg="gray", cursor="hand2")
    url_label.grid(row=20, column=1, columnspan=2, pady=0)
    def open_link(event):
        webbrowser.open("https://github.com/Jackchows/Cangjie5")
    url_label.bind("<Button-1>", open_link)

    # 開始循環
    window.mainloop()