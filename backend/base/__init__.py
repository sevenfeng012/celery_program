#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-18
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

"""Add functionality to dump stack trace on SIGUSR1 for all python process."""

import signal
import traceback

signal.signal(signal.SIGUSR1, lambda sig, stack: traceback.print_stack(stack))
