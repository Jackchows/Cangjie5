# -*- coding: utf8 -*-
import os
import re
import datetime
import argparse
import platform
from buildTxt import buildYaml

def buildRimeRelease():
    # 創建build目錄
    build_directory = os.path.join(parent_directory,'build')
    if not os.path.exists(build_directory):
      os.makedirs(build_directory)
    # 創建build/rime目錄
    build_directory_rime_normal = os.path.join(build_directory,'rime','一般排序')
    build_directory_rime_tc = os.path.join(build_directory,'rime','傳統漢字優先（偏好台灣用字習慣）')
    build_directory_rime_hk = os.path.join(build_directory,'rime','傳統漢字優先（偏好香港用字習慣）')
    build_directory_rime_sc = os.path.join(build_directory,'rime','簡化字優先')
    if not os.path.exists(build_directory_rime_normal):
      os.makedirs(build_directory_rime_normal)
    if not os.path.exists(build_directory_rime_tc):
      os.makedirs(build_directory_rime_tc)
    if not os.path.exists(build_directory_rime_hk):
      os.makedirs(build_directory_rime_hk)
    if not os.path.exists(build_directory_rime_sc):
      os.makedirs(build_directory_rime_sc)

if __name__ == "__main__":

    current_directory = os.path.dirname(os.path.abspath(__file__))    # 獲取文件目錄
    parent_directory = os.path.dirname(current_directory)             # 獲取上級目錄

    buildRimeRelease()
    #buildYaml()
    
