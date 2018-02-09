#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven 
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德


# http://trytofix.github.io/2016/07/07/Celery-Tornado-Supervisor%E6%9E%84%E5%BB%BA%E5%92%8C%E8%B0%90%E7%9A%84%E5%88%86%E5%B8%83%E5%BC%8F%E6%A1%86%E6%9E%B6/
# http://docs.celeryproject.org/en/latest/internals/reference/celery.backends.rpc.html
# https://www.rapospectre.com/blog/42


# Requests 文档
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

# Celery 文档
# http://docs.celeryproject.org/en/latest/userguide/workers.html

# gevent 介绍
# https://segmentfault.com/a/1190000008022050

# 使用介绍
# http://www.dongwm.com/archives/how-to-use-celery/



# 步骤
# 1. redis-server  开启redis server
# 2. 进入对应的task 目录下执行 如下指令: celery -A tasks worker --loglevel=info
# 3. lsof -i:port 端口号，进行重新执行 端口服务 ,kill 当前占用端口pid
# 4. redis-cli 进入 redis 里面
# 5. flower 查看 celery tasks 运行状况  celery flower --broker=redis://localhost:6379/0