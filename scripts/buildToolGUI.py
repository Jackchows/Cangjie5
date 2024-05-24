import tkinter as tk
from tkinter import filedialog
import os
import platform
import webbrowser
from buildToolCmd import chooseLineBreak # type: ignore
from buildToolCmd import chooseDelimiter # type: ignore
from buildToolCmd import buildYaml # type: ignore
from buildToolCmd import buildFcitx # type: ignore
from buildToolCmd import buildYong # type: ignore
from buildToolCmd import buildTxt # type: ignore
from buildToolCmd import checkSourceFileFormat # type: ignore
from buildToolCmd import linebreakDecode # type: ignore

# 函數 - 選擇輸入文件
def select_input_file():
    # 變量 - 輸入文件
    input_file_path = filedialog.askopenfilename(title="選擇碼表文件", 
                                                 initialdir=parent_directory, 
                                                 filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if debug:
        print('[DEBUG][23]input_file_path='+input_file_path)
    if input_file_path:
        input_file_entry.delete(0, tk.END)           # 清空 [Entry 文本輸入框 - 輸入文件] 的值
        input_file_entry.insert(0, input_file_path)  # 設置 [Entry 文本輸入框 - 輸入文件] 的值
        if output_file_selected=='no':               # 如果已經手工選擇了 [Entry 文本輸入框 - 輸出文件], 就不要更改
            output_file_defaule_value = input_file_entry.get().replace('.txt','_formatted.txt').replace('\\', '/')
                                                                    # 設置 [Entry 文本輸入框 - 輸出文件] 的默認值
            output_file_entry.delete(0, tk.END)                     # 清空 [Entry 文本輸入框 - 輸出文件] 的内容
            output_file_entry.insert(0, output_file_defaule_value)  # 設置 [Entry 文本輸入框 - 輸出文件] 的值

    result_label.config(text="")    # 重新選擇之後清空結果

# 函數 - 選擇輸出文件
def select_output_file():
    # 變量 - 輸出文件
    output_file_path = filedialog.asksaveasfilename(title="保存到", 
                                                    initialdir=parent_directory,
                                                    defaultextension=".txt",
                                                    filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if output_file_path:
        output_file_entry.delete(0, tk.END)           # 清空 [Entry 文本輸入框 - 輸出文件] 的值
        output_file_entry.insert(0, output_file_path) # 設置 [Entry 文本輸入框 - 輸出文件] 的值
    global output_file_selected
    output_file_selected = 'yes'                      # 標記已手工選擇 [Entry 文本輸入框 - 輸出文件]
    result_label.config(text="")    # 重新選擇之後清空結果

# 函數 - 生成輸出文件
def go_build():
    global seleted_source                           # 輸入文件 - 從 [Entry 文本輸入框 - 文件選擇] 中獲取值
    seleted_source=input_file_entry.get()
    global selected_order                           # 順序     - 無需處理
    global selected_delimiter                       # 分隔符   - 用chooseDelimiter()處理獲得
    # print('sent delimiter=['+selected_delimiter+']') #'        ',' ','spaces',''
    delimiter=chooseDelimiter(selected_delimiter)
    if debug:
            print('[DEBUG][56]selected_delimiter='+selected_delimiter)
            print('[DEBUG][56]delimiter='+delimiter)
    global selected_linebreak                       # 換行符   - 用chooseLineBreak()處理獲得
    linebreak=chooseLineBreak(selected_linebreak)
    if debug:
            print('[DEBUG][61]selected_linebreak='+selected_linebreak)
            print('[DEBUG][61]linebreak='+linebreak)
    build_with_template='no'                        # 模版     - 默認不使用
    global seleted_output                           # 輸出文件 - 從 [Entry 文本輸入框 - 輸出文件] 中獲取值
    build_txt_result=''                             # 調用build函數返回的結果
    seleted_output=output_file_entry.get()
    if seleted_source=='':
        result_label.config(text="未選擇碼表文件", fg="red")
    elif seleted_output=='':
        result_label.config(text="未選擇輸出文件", fg="red")
    elif checkSourceFileFormat(seleted_source)[0] == 'no':
        build_txt_result = 'ERR_NOT_SUPPORT_FORMAT'
    elif selected_template=='rime' and linebreak=='crlf':
        build_txt_result=buildYaml(seleted_source,'crlf',seleted_output)
    elif selected_template=='rime' and linebreak=='lf':
        build_txt_result=buildYaml(seleted_source,'lf',seleted_output)
    elif selected_template=='rime' and linebreak=='cr':
        build_txt_result=buildYaml(seleted_source,'cr',seleted_output)
    elif selected_template=='fcitx':
        build_txt_result=buildFcitx(seleted_source,seleted_output)
    elif selected_template=='yong':
        build_txt_result=buildYong(seleted_source,seleted_output)
    else:
        build_txt_result=buildTxt(seleted_source,selected_order,delimiter,linebreakDecode(linebreak),build_with_template,seleted_output)
    if build_txt_result == 'SUCCESS':
        result_label.config(text="轉換完成", fg='green')
    elif build_txt_result == 'ERR_SOURCE_FILE_NOT_EXISTS':
        result_label.config(text="找不到所選擇的碼表文件", fg='red')
    elif build_txt_result == 'ERR_NOT_SUPPORT_FORMAT':
        result_label.config(text="不支持的源碼表格式", fg='red')
    # elif build_txt_result == 'ERR_NOT_CJ5_FILE':
    #     result_label.config(text="此功能目前僅支持倉頡五代補完計劃的碼表文件", fg='red')
    else:
        result_label.config(text="轉換失敗", fg='red')


if __name__ == "__main__":

    debug = False
    # 全局變量
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
    selected_linebreak = ''
    order = ''
    seleted_source = ''
    output_file_selected = 'no'                                       # 是否已經手工選擇輸出文件

    # 建立主窗口
    window = tk.Tk()
    window.title('補完計劃碼表轉換工具 v0.1 beta')
    # window.geometry('800x400')
    window.resizable(False, False)

    # 建立框架容器，用于放置文本框和按钮
    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    #--------------------輸入文件--------------------------------------------------------------------------------
    # Label 文本標籤 - 輸入文件
    tk.Label(frame, text="碼表文件:").grid(row=0, column=0, pady=10, sticky='e')
    # Entry 文本輸入框 - 輸入文件
    input_file_entry = tk.Entry(frame, width=65)
    input_file_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=10, sticky='w')
    input_file_defaule_value = os.path.join(parent_directory,'Cangjie5.txt').replace('\\', '/')
    if platform.system().lower() == 'windows':                                                          # 在Windows上將盤符顯示為大寫
        input_file_defaule_value = input_file_defaule_value[0].upper() + input_file_defaule_value[1:]
    input_file_entry.insert(0, input_file_defaule_value)
    # button 按鈕 - 輸入文件選擇
    input_file_button = tk.Button(frame, text='選擇', width=10, command=select_input_file)
    input_file_button.grid(row=0, column=4, padx=5, pady=10, sticky='w')

    #--------------------輸出文件--------------------------------------------------------------------------------
    # Label 文本標籤 - 輸出文件
    tk.Label(frame, text="輸出文件:").grid(row=1, column=0, pady=5, sticky='e')
    # Entry 文本輸入框 - 輸出文件
    output_file_entry = tk.Entry(frame, width=65)
    output_file_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=10, sticky='w')
    output_file_defaule_value = input_file_defaule_value.replace('.txt','_formatted.txt').replace('\\', '/')
    output_file_entry.insert(0, output_file_defaule_value)
    # button 按鈕 - 輸出文件選擇
    output_file_button = tk.Button(frame, text='選擇', width=10, command=select_output_file)
    output_file_button.grid(row=1, column=4, padx=5, pady=10, sticky='w')

    #--------------------模版------------------------------------------------------------------------------------
    # Label 文本標籤 - 模版
    tk.Label(frame, text="模板:").grid(row=2, column=0, pady=5, sticky='e')
    # StringVar [字符串變量 - 模板] 默認值
    template_value = tk.StringVar(value="text")
    # template_value.trace_add("write", update_language_options)
    # List 字典 - 模版選項
    template_list = [('text', '(無)'), ('rime', 'RIME'), ('fcitx', 'Fcitx 5'), ('yong', '小小輸入法')]
    template_buttons = []
    for i, (value, text) in enumerate(template_list):
        template_button = tk.Radiobutton(frame, text=text, variable=template_value, value=value)
        template_button.grid(row=2, column=i+1, padx=5, pady=5, sticky='w')
        template_buttons.append(template_button)
    # Radiobutton 單選框選項 - 模版 
    templace_button_text  = template_buttons[0]
    templace_button_rime  = template_buttons[1]
    templace_button_fcitx = template_buttons[2]
    templace_button_yong  = template_buttons[3]
    # 變量 - 已選擇的模版
    selected_template = template_value.get()
    # 函數 - 監控 [單選欄 - 模版選項]
    def update_template_value(*args):
        global selected_template
        selected_template = template_value.get()
        result_label.config(text="")                        # 重新選擇之後清空結果
        if selected_template == 'text':                     # 如果選擇了模版，則限制下面的選項
            order_button_char.config(state="normal")            # 順序
            order_button_code.config(state="normal")
            delimiter_button_tab.config(state="normal")         # 分隔符
            delimiter_button_space.config(state="normal")
            delimiter_button_multi.config(state="normal")
            delimiter_button_none.config(state="normal")
            linebreak_button_auto.config(state="normal")        # 換行符
            linebreak_button_crlf.config(state="normal")
            linebreak_button_lf.config(state="normal")
            linebreak_button_cr.config(state="normal")
        elif selected_template == 'rime':
            order_value.set("char")                             # 順序設為char
            order_button_char.config(state="disabled")
            order_button_code.config(state="disabled")
            delimiter_value.set("tab")                          # 分隔符設為tab
            delimiter_button_tab.config(state="disabled")
            delimiter_button_space.config(state="disabled")
            delimiter_button_multi.config(state="disabled")
            delimiter_button_none.config(state="disabled")
            # linebreak_value.set("auto")                           # 換行符設為auto
            linebreak_button_auto.config(state="normal")
            linebreak_button_crlf.config(state="normal")
            linebreak_button_lf.config(state="normal")
            linebreak_button_cr.config(state="normal")
        elif selected_template == 'fcitx':
            order_value.set("code")                             # 順序設為code
            order_button_char.config(state="disabled")
            order_button_code.config(state="disabled")
            delimiter_value.set("space")                        # 分隔符設為space
            delimiter_button_tab.config(state="disabled")
            delimiter_button_space.config(state="disabled")
            delimiter_button_multi.config(state="disabled")
            delimiter_button_none.config(state="disabled")
            linebreak_value.set("lf")                           # 換行符設為lf
            linebreak_button_auto.config(state="disabled")
            linebreak_button_crlf.config(state="disabled")
            linebreak_button_lf.config(state="disabled")
            linebreak_button_cr.config(state="disabled")
        elif selected_template == 'yong':
            order_value.set("code")                             # 順序設為code
            order_button_char.config(state="disabled")
            order_button_code.config(state="disabled")
            delimiter_value.set("multi")                        # 分隔符設為multi
            delimiter_button_tab.config(state="disabled")
            delimiter_button_space.config(state="disabled")
            delimiter_button_multi.config(state="disabled")
            delimiter_button_none.config(state="disabled")
            linebreak_value.set("crlf")                         # 換行符設為crlf
            linebreak_button_auto.config(state="disabled")
            linebreak_button_crlf.config(state="disabled")
            linebreak_button_lf.config(state="disabled")
            linebreak_button_cr.config(state="disabled")
    template_value.trace_add("write", update_template_value)    # 將 [函數 - 監控(單選欄 - 模版選項)] 與 [字符串變量 - 模版] 綁定

    #--------------------順序------------------------------------------------------------------------------------
    # Label 文本標籤 - 順序
    tk.Label(frame, text="順序:").grid(row=3, column=0, pady=5, sticky='e')
    # StringVar [字符串變量 - 順序] 默認值
    order_value = tk.StringVar(value="char")
    # List 列表 - 順序選項
    order_list = [('char','字在前'), ('code','倉頡碼在前')]
    order_buttons = []
    for i, (value, text) in enumerate(order_list):
        order_button = tk.Radiobutton(frame, text=text, variable=order_value, value=value)
        order_button.grid(row=3, column=i+1, padx=5, pady=5, sticky='w')
        order_buttons.append(order_button)
    # Radiobutton 單選框選項 - 順序 
    order_button_char = order_buttons[0]    # char
    order_button_code = order_buttons[1]    # code
    # 變量 - 已選擇的順序
    selected_order = order_value.get()
    # 函數 - 監控 [單選欄 - 順序選項]
    def update_order_value(*args):
        global selected_order
        selected_order = order_value.get()
        result_label.config(text="")    # 重新選擇之後清空結果
    order_value.trace_add("write", update_order_value)    # 將 [函數 - 監控(單選欄 - 順序選項)] 與 [字符串變量 - 順序] 綁定

    #--------------------分隔符--------------------------------------------------------------------------------
    # Label 文本標籤 - 分隔符
    tk.Label(frame, text="行內字-碼分隔:").grid(row=4, column=0, pady=5, sticky='e')
    # StringVar [字符串變量 - 分隔符] 默認值
    delimiter_value = tk.StringVar(value="tab")
    # List 列表 - 分隔符選項
    delimiter_list = [('tab','Tab (製表鍵)'), ('space','單個空格'), ('multi','以空格代替Tab對齊'), ('none','(無)'), ]
    delimiter_buttons = []
    for i, (value, text) in enumerate(delimiter_list):
        delimiter_button = tk.Radiobutton(frame, text=text, variable=delimiter_value, value=value)
        delimiter_button.grid(row=4, column=i+1, padx=5, pady=5, sticky='w')
        delimiter_buttons.append(delimiter_button)
    # Radiobutton 單選框選項 - 分隔符 
    delimiter_button_tab   = delimiter_buttons[0]    # tab
    delimiter_button_space = delimiter_buttons[1]    # space
    delimiter_button_multi = delimiter_buttons[2]    # multi
    delimiter_button_none  = delimiter_buttons[3]    # none
    # 變量 - 已選擇的分隔符
    selected_delimiter = delimiter_value.get()
    # 函數 - 監控 [單選欄 - 分隔符]
    def update_delimiter_value(*args):
        global selected_delimiter
        selected_delimiter = delimiter_value.get()
        result_label.config(text="")    # 重新選擇之後清空結果
    delimiter_value.trace_add("write", update_delimiter_value)    # 將 [函數 - 監控(單選欄 - 換行符選項)] 與 [字符串變量 - 換行符] 綁定 

    #--------------------換行符--------------------------------------------------------------------------------
    # Label 文本標籤 - 換行符
    tk.Label(frame, text="換行符:").grid(row=5, column=0, pady=5, sticky='e')
    # StringVar [字符串變量 - 換行符] 默認值
    linebreak_value = tk.StringVar(value="auto")
    # List 列表 - 換行符選項
    linebreak_list = [('auto','與系統一致'), ('crlf','CRLF (Windows)'), ('lf','LF (Linux / macOS)'), ('cr','CR (Mac OS, 舊版)'), ]
    linebreak_buttons = []
    for i, (value, text) in enumerate(linebreak_list):
        linebreak_button = tk.Radiobutton(frame, text=text, variable=linebreak_value, value=value)
        linebreak_button.grid(row=5, column=i+1, padx=5, pady=5, sticky='w')
        linebreak_buttons.append(linebreak_button)
    # Radiobutton 單選框選項 - 換行符 
    linebreak_button_auto = linebreak_buttons[0]    # auto
    linebreak_button_crlf = linebreak_buttons[1]    # crlf
    linebreak_button_lf   = linebreak_buttons[2]    # lf
    linebreak_button_cr   = linebreak_buttons[3]    # cr
    # 變量 - 已選擇的換行符
    selected_linebreak = linebreak_value.get()
    # 函數 - 監控 [單選欄 - 換行符選項]
    def update_linebreak_value(*args):
        global selected_linebreak
        selected_linebreak = linebreak_value.get()
        if debug:
            print('[DEBUG][293]selected_linebreak='+selected_linebreak)
        result_label.config(text="")    # 重新選擇之後清空結果
    linebreak_value.trace_add("write", update_linebreak_value)    # 將 [函數 - 監控(單選欄 - 換行符選項)] 與 [字符串變量 - 換行符] 綁定 

    #--------------------轉換按鈕--------------------------------------------------------------------------------
    # button 按鈕 - 轉換
    build_txt_button = tk.Button(frame, text='轉換', width=10, command=go_build)
    build_txt_button.grid(row=8, column=0, columnspan=2, pady=20)
    #----------------------結果----------------------------------------------------------------------------------
    # Label 文本標籤 - 結果
    result_label = tk.Label(frame, text="")
    result_label.grid(row=8, column=2, pady=20)
    #--------------------項目信息--------------------------------------------------------------------------------
    imformation_label = tk.Label(frame, text="倉頡五代補完計劃", fg="gray")
    imformation_label.grid(row=10, column=0, columnspan=1, pady=0)
    url_label = tk.Label(frame, text="https://github.com/Jackchows/Cangjie5", fg="gray", cursor="hand2")
    url_label.grid(row=10, column=1, columnspan=2, pady=0)
    def open_link(event):
        webbrowser.open("https://github.com/Jackchows/Cangjie5")
    url_label.bind("<Button-1>", open_link)


    window.mainloop()