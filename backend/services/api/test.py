#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 13:10:22
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

import os
import sys
import requests
import json


class test(object):
    """
    """

    @classmethod
    def run(self):
        print "test"
        sys.stdout.write("\r 任务进度:{0}%\n".format(10))

    @classmethod
    def testAddCelery(self):
        url = "http://127.0.0.1:9882/task"
        for x in xrange(1, 150):
            payload = {"x": x, "y": x + 2}
            r = requests.post(url, data=json.dumps(payload))
            sys.stdout.write("\r 任务进度:{0}\n".format(r.text))

    @classmethod
    def testGetCelery(self):
        url = "http://127.0.0.1:9882/task"
        for x in xrange(1, 2):
            r = requests.get(url)
        sys.stdout.write("\r 任务进度:{0}\n".format(r.text))


if __name__ == "__main__":
    # test = test()
    test.run()
    # test.testAddCelery()
    test.testGetCelery()
