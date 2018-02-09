#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

from tornado import web
from tornado import gen
import tcelery
import tasks_media
import json

tcelery.setup_nonblocking_producer()


class taskHandler(web.RequestHandler):
    """
    """

    def add(self, x, y):
        # tasks.add.apply_async(args=[x, y])

        # result = tasks.add.delay(x,y)

        # while not result.ready():
        #     print "not ready"

        # return result.get()

        result = tasks_media.calstoreresult(x, y)
        return 2

    @web.asynchronous
    @gen.coroutine
    def get(self):
        print "CALLING get()"
        ret = self.add(1, 5)
        # tasks.add.apply_async(args=[1,5], queue="audio",
        #                        routing_key="ajmd.audio",callback=self.on_result)
        # tasks.add.apply_async(args=[1,6],callback=self.on_result)
        self.write(str(ret))
        self.finish()

        # tasks.demo.apply_async(
        #     args=['demo'],
        #     queue='demo',
        #     routing_key='task.demo',
        #     callback=self.on_success)

    @web.asynchronous
    @gen.coroutine
    def post(self):
        data = json.loads(self.request.body)

        xAix = int(data["x"])
        yAix = int(data["y"])

        ret = self.add(xAix, yAix)

        self.write(str(ret))
        self.finish()

    @staticmethod
    def on_result(self, response):
        self.write("success")
        self.write(str(response.result))
        self.finish()
