import os

def check_path_type(path):
    if os.path.isabs(path):
        print(f"{path} 是绝对路径")
    else:
        print(f"{path} 是相对路径")

# 测试路径
path1 = "/usr/bin/python"
path2 = "scripts/script.py"

check_path_type(path1)
check_path_type(path2)
