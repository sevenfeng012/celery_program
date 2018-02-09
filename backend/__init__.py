#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-18
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

# assert __name__ == 'backend',\
#     'import the backend module as ajmdContent.backend, not as a top-level module.'

print 'seven'

import sys
import os

cur_path = os.getcwd()
print(cur_path)
dir_path = os.path.dirname(cur_path)
print(dir_path)

pythonpath = sys.path
print(pythonpath)

path = pythonpath.append(dir_path)

print(path)

