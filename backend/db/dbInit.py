#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven 
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

from tornado.httpclient import HTTPClient, AsyncHTTPClient

from tables import Article

import tornado.web
import tornado.gen
import urllib


class dbHandler(tornado.web.RequestHandler):
    """
    """

    @property
    def db(self):
        return self.application.db

    def get(self):
        data = self.db.query(Articles).all()

        for item in data:
            print item.content
        