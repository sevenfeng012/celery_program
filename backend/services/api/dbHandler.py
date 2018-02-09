#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

from tornado.httpclient import HTTPClient, AsyncHTTPClient

# from ajmdContent.backend.db.tables import Article
from tables import Article

import tornado.web
import tornado.gen
import urllib
import json

import logging

import random

logger = logging.getLogger("ajmd_content")


class dbHandler(tornado.web.RequestHandler):
    """
    """

    @property
    def db(self):
        return self.application.db

    def get(self):
        data = self.db.query(Article).all()
        result = ''

        # for item in data:
        #     result += "title:%s,user:%s,time:%s,content:%s </br>" % (
        #         item.title, item.user, item.time, item.content)

        for item in data:
            result += "content:%s </br>" % (
                item.content)

        self.set_status(200)

        if len(data):
            self.write("结果:</br> %s " % (result))
        else:
            self.write("列表获取为空")

    def options(self):
        data = self.db.query(Article).all()

        self.write(json.dumps({"status": 0,
                               "msg": "返回成功",
                               "article": Article.__json__(data)
                               }, ensure_ascii=False, indent=4))

    def post(self):
        """	user 
        """

        data = json.loads(self.request.body.decode("utf-8"))

        logger.info(data)
        sample = random.randint(0,1000)
        div = random.randint(0,1001)
        userStr = str(sample*div)
        timeStr = 'today'
        titleStr = 'result'
        contentStr = data['result']

        article = Article(user=userStr, title=titleStr,
                          time=timeStr, content=contentStr)
        self.db.add(article)
        self.db.commit()
