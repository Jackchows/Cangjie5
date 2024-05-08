# -*- coding: utf8 -*-
import os
import re
import time

def chooseGithub():                                    # 輸入文件
	print("此工具可以將碼表轉換成所需的格式，你可以選擇列序、分隔符以及換行符。")
	print("Step 1 - 選擇需要轉換的文件")
	print("[1] Cangjie5.txt")
	print("[2] Cangjie5_TC.txt")
	print("[3] Cangjie5_HK.txt")
	print("[4] Cangjie5_SC.txt")
	print("[5] Cangjie5_special.txt")
	github_input=input("輸入數字並按Enter (默認為1):")
	global github
	if github_input=='1':
		github='Cangjie5.txt'
	elif github_input=='2':
		github='Cangjie5_TC.txt'
	elif github_input=='3':
		github='Cangjie5_HK.txt'
	elif github_input=='4':
		github='Cangjie5_SC.txt'
	elif github_input=='5':
		github='Cangjie5_special.txt'

def chooseOrder():                                      # 順序
	print("Step 2 - 選擇字和倉頡碼的順序")
	print("[1] 字在前，倉頡碼在後")
	print("[2] 倉頡碼在前，字在後")
	order_input=input("輸入數字並按Enter (默認為1):")
	global order
	if order_input=='1':
		order='1'
	elif order_input=='2':
		order='2'

def chooseDelimiter():                                  # 分隔符
	print("Step 3 - 選擇字與倉頡碼之間的分隔符")
	print("[1] Tab")
	print("[2] Space (一個)")
	print("[3] Spaces (多個，對齊每一列)")
	print("[4] (無)")
	delimiter_input=input("輸入數字並按Enter (默認為1):")
	global delimiter
	if delimiter_input=='1':
		delimiter='\t'
	elif delimiter_input=='2':
		delimiter=' '
	elif delimiter_input=='3':
		delimiter="spaces"
	elif delimiter_input=='4':
		delimiter=''

def chooseLineBreak():                                  # 換行符
	print("Step 4 - 選擇換行符")
	print("[1] \\r\\n")
	print("[2] \\n")
	print("[3] \\r")
	linebreak_input=input("輸入數字並按Enter (默認為1):")
	global linebreak
	if linebreak_input=='1':
		linebreak="\r\n"
	elif linebreak_input=='2':
		linebreak="\n"
	elif linebreak_input=='3':
		linebreak="\r"

def buildTxt(github,order,delimiter,linebreak):

	# 獲取
	current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
	parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄
	github_file = parent_directory+'\\'+github
	# print(str(github_file))
	if (os.path.exists(github_file)==False):                               # 若github不存在
			# print ("["+str(github)+"] does not exists.")
			print ("未找到 "+str(github_file)+"，請檢查文件是否存在")
			return
	#output_file = current_directory+'\\'+'converter_output_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.txt'
	output_file = current_directory+'\\'+github.replace('.txt','_formatted.txt')
	# 開啟
	with open(github_file,'r',encoding='utf8') as gib, \
		 open(output_file,'w',encoding='utf8',newline='') as txt:
					# 寫入
					for line in gib:
						value_line = re.match(r'^([^\t\n\r]+)\t([a-z]{1,5}).*$', line)    # 排除開頭的說明文字
						if value_line:
							value_char = value_line[1]
							value_code = value_line[2]
							if order=='1':                                              # 先字後碼
								new_line = str(value_char)+delimiter+str(value_code)+linebreak
							elif order=='2':                                            # 先碼後字
								if delimiter=="spaces":
									new_delimiter=' ' * (8 - len(value_code))                     # 以空格代替tab對齊
								else:
									new_delimiter=delimiter
								new_line = str(value_code)+new_delimiter+str(value_char)+linebreak
							txt.write(new_line)
	# 關閉
	print("完成。輸出文件 "+output_file)


if __name__ == "__main__":
	github= "Cangjie5.txt"    # 默認值
	order = '1'
	delimiter="\t"
	linebreak='\r\n'

	chooseGithub()
	chooseOrder()
	chooseDelimiter()
	chooseLineBreak()

	buildTxt(github,order,delimiter,linebreak)