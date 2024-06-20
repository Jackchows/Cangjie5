# -*- coding: utf8 -*-
import os
import re
import datetime
# import argparse
# import platform
import zipfile
import buildToolCmd

def buildRimeRelease():
    # 創建build/rime/*目錄
    sub_directory_path = {}
    for id in schema_id:
        sub_directory_path[id] = os.path.join(build_directory,'rime',sub_directory_name[id])
        if not os.path.exists(sub_directory_path[id]):
            os.makedirs(sub_directory_path[id])
    # 創建*.schema.yaml
    rime_schema_file = {}
    rime_schema_file_context = {}
    for id in schema_id:
        rime_schema_file[id] = os.path.join(build_directory,'rime',sub_directory_name[id],id+'.schema.yaml')
        #region rime_schema_file_context[id]
        rime_schema_file_context[id] = \
'''# Rime schema settings
# encoding: utf-8

schema:
  schema_id: '''+id+'''
  name: '''+schema_name[id]+'''
  version: "'''+str(datetime.datetime.now().strftime('%Y.%m.%d'))+'''"
  author:
    - 發明人 朱邦復先生
  description: |
    倉頡五代補完計畫
    專案網址：https://github.com/Jackchows/Cangjie5
    由「倉頡之友·馬來西亞」發佈的「倉頡平台2012」軟件所含「五倉世紀」碼表修改而來。
    網址：www.chinesecj.com
  dependencies:
    - luna_quanpin

switches:
  - name: ascii_mode
    reset: 0
    states: [ 中文, 西文 ]
  - name: full_shape
    states: [ 半角, 全角 ]
  - name: simplification
    states: [ 漢字, 汉字 ]
  - name: extended_charset
    states: [ 常用, 增廣 ]
  - name: ascii_punct
    states: [ 。，, ．， ]

engine:
  processors:
    - ascii_composer
    - recognizer
    - key_binder
    - speller
    - punctuator
    - selector
    - navigator
    - express_editor
  segmentors:
    - ascii_segmentor
    - matcher
    - abc_segmentor
    - punct_segmentor
    - fallback_segmentor
  translators:
    - punct_translator
    - reverse_lookup_translator
    - table_translator
  filters:
    - simplifier
    - uniquifier
    - single_char_filter

speller:
  alphabet: zyxwvutsrqponmlkjihgfedcba
  delimiter: " ;"
  #max_code_length: 5  # 五碼頂字上屏
translator:
  dictionary: '''+id+'''
  enable_charset_filter: true
  encode_commit_history: true
  enable_encoder: true
  enable_sentence: true
  enable_user_dict: false
  max_phrase_length: 5
  preedit_format:
    - 'xform/(?<![^x])x/#/'
    - "xlit|abcdefghijklmnopqrstuvwxyz#|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重|"
  comment_format:
    - 'xform/(?<![^x])x/#/'
    - "xlit|abcdefghijklmnopqrstuvwxyz#~|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重～|"
  disable_user_dict_for_patterns:
    - "^[a-x]$"
    - "^z.*$"
    - "^yyy.*$"

abc_segmentor:
  extra_tags:
#    - reverse_lookup  # 與拼音（反查碼）混打

reverse_lookup:
  dictionary: luna_pinyin
  prism: luna_quanpin
  prefix: "`"
  suffix: "'"
  tips: 〔拼音〕
  preedit_format:
    - xform/([nl])v/$1ü/
    - xform/([nl])ue/$1üe/
    - xform/([jqxy])v/$1u/
  comment_format:
    - 'xform/(?<![^x])x/#/'
    - "xlit|abcdefghijklmnopqrstuvwxyz#~|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重～|"

simplifier:
  tips: all  # 簡化字模式下提示對應的傳統漢字

punctuator:
  import_preset: symbols

key_binder:
  import_preset: default

recognizer:
  import_preset: default
  patterns:
    punct: "^/([0-9]0?|[a-z]+)$"
    reverse_lookup: "`[a-z]*'?$|[a-z]*'$"
'''
        #endregion rime_schema_file_context[id]
        with open(rime_schema_file[id],'w',encoding='utf-8') as rsf:
            rsf.write(rime_schema_file_context[id])

    # 創建*.dict.yaml
    rime_dict_file = {}
    for id in schema_id:
        source = os.path.join(parent_directory, id.capitalize().replace('_tc','_TC').replace('_hk','_HK').replace('_sc','_SC')+'.txt')
        rime_dict_file[id] = os.path.join(build_directory,'rime',sub_directory_name[id],id+'.dict.yaml')
        output = rime_dict_file[id]
        template = 'rime'
        py = os.path.join(current_directory,'buildToolCmd.py')
        command = ''.join(['python ',py,' -s "',source,'" -t weasel -f "',output,'"'])
        # print(command)
        os.system(command)

    # 創建*.custom.yaml
    rime_custom_file_context = r'''# Rime schema settings
# encoding: utf-8

patch:
  translator/enable_user_dict: false  # 是否開啟用戶詞典
  # reverse_lookup/prefix: "`"         # 反查鍵
  # menu/page_size: 8                  # 每頁候選字數

  # 編碼顯示格式
  # 【格式一】小狼毫原版 : xhx （難竹難）
  # translator/preedit_format:  # 已輸入編碼
  #   - 'xform/^([a-z]*)$/$1\t（\U$1\E）/'
  #   - "xlit|ABCDEFGHIJKLMNOPQRSTUVWXYZ|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜符|"
  # translator/comment_format:  # 編碼提示
  #   - "xlit|abcdefghijklmnopqrstuvwxyz~|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜符～|"
  # reverse_lookup/comment_format:  # 反查提示
  #   - "xlit|abcdefghijklmnopqrstuvwxyz|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜符|"
  # 【格式二】衹顯示倉頡字母 : 重竹難
  # translator/preedit_format:
  #   - 'xform/(?<![^x])x/#/'
  #   - "xlit|abcdefghijklmnopqrstuvwxyz#|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重|"
  # translator/comment_format:
  #   - 'xform/(?<![^x])x/#/'
  #   - "xlit|abcdefghijklmnopqrstuvwxyz#~|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重～|"
  # reverse_lookup/comment_format:
  #   - "xlit|abcdefghijklmnopqrstuvwxyz#~|日月金木水火土竹戈十大中一弓人心手口尸廿山女田難卜片重～|"
  # 【格式三】衹顯示小寫英文字母 : xhx
  # translator/preedit_format:      # 清空
  # translator/comment_format:      # 清空
  # reverse_lookup/comment_format:  # 清空
  # 【格式四】衹顯示大寫英文字母 : XHX
  # translator/preedit_format:
  #   - 'xform/^([a-z]*)$/\U$1\E/'
  # translator/comment_format:
  #   - "xlit|abcdefghijklmnopqrstuvwxyz#~|ABCDEFGHIJKLMNOPQRSTUVWXYZ#~|"
  # reverse_lookup/comment_format:
  #   - 'xform/^([a-z]*)$/\U$1\E/'
'''
    rime_custom_file = {}
    for id in schema_id:
        rime_custom_file[id] = os.path.join(build_directory,'rime',sub_directory_name[id],id+'.custom.yaml')
        with open(rime_custom_file[id],'w',encoding='utf-8') as rcf:
            rcf.write(rime_custom_file_context)
    # 創建zip
    zip_folder = os.path.join(build_directory,'rime')
    zip_file = os.path.join(release_directory,'RimeData_Cangjie5_'+str(datetime.datetime.now().strftime('%Y%m%d'))+'.zip')
    zip_release(zip_folder,zip_file)

def buildYongRelease():
    # 創建build/yong/*目錄
    sub_directory_path = {}
    for id in schema_id:
        sub_directory_path[id] = os.path.join(build_directory,'yong',sub_directory_name[id])
        if not os.path.exists(sub_directory_path[id]):
            os.makedirs(sub_directory_path[id])
    # 創建*.txt
    yong_dict_file = {}
    for id in schema_id:
        yong_dict_file[id] = os.path.join(build_directory,'yong',sub_directory_name[id],id+'.txt')
        source = os.path.join(parent_directory, id.capitalize().replace('_tc','_TC').replace('_hk','_HK').replace('_sc','_SC')+'.txt')
        output = yong_dict_file[id]
        # output = os.path.join(build_directory,'yong',sub_directory_name[id],'cj5-90000.txt')
        # buildYong(source,output)
        py = os.path.join(current_directory,'buildToolCmd.py')
        command = ''.join(['python ',py,' -s "',source,'" -t yong -f "',output,'"'])
        # print(command)
        os.system(command)
    # 創建zip
    zip_folder = os.path.join(build_directory,'yong')
    zip_file = os.path.join(release_directory,'YongData_Cangjie5_'+str(datetime.datetime.now().strftime('%Y%m%d'))+'.zip')
    zip_release(zip_folder,zip_file)

def buildFcitxRelease():
    # 創建build/fcitx/*目錄
    sub_directory_path = {}
    for id in schema_id:
        sub_directory_path[id] = os.path.join(build_directory,'fcitx',sub_directory_name[id])
        if not os.path.exists(sub_directory_path[id]):
            os.makedirs(sub_directory_path[id])
    # 創建*.conf.in
    fcitx_conf_file = {}
    fcitx_conf_file_context = {}
    for id in schema_id:
        fcitx_conf_file[id] = os.path.join(build_directory,'fcitx',sub_directory_name[id],id+'.conf.in')
        #region fcitx_conf_file_context[id]
        fcitx_conf_file_context[id] = \
'''
[InputMethod]
Name='''+id+'''
Icon=fcitx-cangjie
Label='''+schema_name[id]+'''
LangCode=zh_TW
Addon=table
Configurable=True

[Table]
File=table/cangjie5.main.dict
OrderPolicy=Freq
PinyinKey=`
AutoSelect=True
AutoSelectLength=-1
NoMatchAutoSelectLength=0
MatchingKey=*
ExactMatch=False
Hint=False
DisplayCustomHint=True
PageSize=9
CandidateLayoutHint=Vertical

[Table/PrevPage]
0=Up
1=minus

[Table/NextPage]
0=Down
1=equal
'''
        #endregion fcitx_conf_file_context[id]
        with open(fcitx_conf_file[id],'w',encoding='utf-8') as rsf:
            rsf.write(fcitx_conf_file_context[id])
    # 創建*.txt
    fcitx_dict_file = {}
    for id in schema_id:
        fcitx_dict_file[id] = os.path.join(build_directory,'fcitx',sub_directory_name[id],id+'.txt')
        source = os.path.join(parent_directory, id.capitalize().replace('_tc','_TC').replace('_hk','_HK').replace('_sc','_SC')+'.txt')
        output = fcitx_dict_file[id]
        # buildFcitx(source,output)
        py = os.path.join(current_directory,'buildToolCmd.py')
        command = ''.join(['python ',py,' -s "',source,'" -t fcitx -f "',output,'"'])
        # print(command)
        os.system(command)
    # 創建zip
    zip_folder = os.path.join(build_directory,'fcitx')
    zip_file = os.path.join(release_directory,'FcitxData_Cangjie5_'+str(datetime.datetime.now().strftime('%Y%m%d'))+'.zip')
    zip_release(zip_folder,zip_file)

def buildMscjRelease():
    # 創建build/mscj/*目錄
    sub_directory_path = {}
    for id in schema_id:
        sub_directory_path[id] = os.path.join(build_directory,'mscj',sub_directory_name[id])
        if not os.path.exists(sub_directory_path[id]):
            os.makedirs(sub_directory_path[id])
    # 創建*.txt
    mscj_dict_file = {}
    for id in schema_id:
        mscj_dict_file[id] = os.path.join(build_directory,'mscj',sub_directory_name[id],id+'.txt')
        source = os.path.join(parent_directory, id.capitalize().replace('_tc','_TC').replace('_hk','_HK').replace('_sc','_SC')+'.txt')
        order = 'code'
        delimiter = '\t'
        linebreak = '\r\n'
        build_with_template = 'no'
        output = mscj_dict_file[id]
        py = os.path.join(current_directory,'buildToolCmd.py')
        command = ''.join(['python ',py,' -s "',source,'" -o code -d tab -l crlf -f "',output,'"'])
        # print(command)
        os.system(command)

    # 創建zip
    # old_lex_num = 0
    new_lex_num = 0
    zip_folder = os.path.join(build_directory,'mscj')
    for root, dirs, files in os.walk(zip_folder):
        for file in files:
            file_path = os.path.join(root, file)
            #arcname = os.path.relpath(file_path, zip_folder)    # 相對路徑
            if file == 'ChtChangjieExt.lex':
                # old_lex_num = old_lex_num + 1
                os.rename(os.path.join(root, 'ChtChangjieExt.lex'),os.path.join(root, 'ChtCangjieExt.lex'))
                new_lex_num = new_lex_num + 1
            elif file == 'ChtCangjieExt.lex':
                new_lex_num = new_lex_num + 1

    if new_lex_num==4:
      zip_file = os.path.join(release_directory,'MSCJData_Cangjie5_'+str(datetime.datetime.now().strftime('%Y%m%d'))+'.zip')
      zip_release(zip_folder,zip_file)
    elif new_lex_num<4:
        print('未生成.lex文件 (已有 '+str(new_lex_num)+'/4)')

def zip_release(folder_path, zip_path):
    mscj_txt_pattern = re.compile(r'^.*mscj.*cangjie5.*txt$')
    mscj_symbol_txt_pattern = re.compile(r'^.*mscj.*symbol.txt$')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zif:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                if mscj_txt_pattern.match(file_path):
                    pass
                elif mscj_symbol_txt_pattern.match(file_path):
                    pass
                # if re.match(r'^.*mscj.*txt$', file_path):
                #     pass
                else:
                    zif.write(file_path, arcname)
    # basename = os.path.basename(folder_path)
    # print(basename)

if __name__ == "__main__":

    # 方案id
    schema_id = ['cangjie5','cangjie5_tc','cangjie5_hk','cangjie5_sc']
    schema_name = {}
    schema_name['cangjie5'] = '倉頡五代'
    schema_name['cangjie5_tc'] = '倉頡五代TC'
    schema_name['cangjie5_hk'] = '倉頡五代HK'
    schema_name['cangjie5_sc'] = '倉頡五代SC'
    sub_directory_name = {}
    sub_directory_name['cangjie5'] = '一般排序'
    sub_directory_name['cangjie5_tc'] = '傳統漢字優先（偏好台灣用字習慣）'
    sub_directory_name['cangjie5_hk'] = '傳統漢字優先（偏好香港用字習慣）'
    sub_directory_name['cangjie5_sc'] = '簡化字優先'

    # 当前目錄
    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄

    # 創建build目錄
    build_directory = os.path.join(parent_directory,'build')
    release_directory = os.path.join(parent_directory,'release')
    if not os.path.exists(build_directory):
        os.makedirs(build_directory)
    if not os.path.exists(release_directory):
        os.makedirs(release_directory)

    buildRimeRelease()
    buildYongRelease()
    buildFcitxRelease()
    buildMscjRelease()
