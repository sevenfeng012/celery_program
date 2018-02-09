#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

from functools import wraps
import base64

import tornado.web

USERS = [
    ("admin", "admin")
]


"""身份认证的装饰者模式

装饰http request 的网络请求参数

"""


def authenticate():
    def decorate(api):
        @wraps(api)
        def wrapper(*args, **kwargs):
            instance = args[0]
            assert isinstance(instance, tornado.web.RequestHandler)

            if "Authorization" in instance.request.headers:
                signature = instance.request.headers[
                    "Authorization"].split(" ")[1]
                user, pwd = base64.b64decode(
                    signature.encode()).decode("utf-8").split(":")

                for item in USERS:
                    if user == item[0] and pwd == item[1]:
                        return api(*args, **kwargs)

            instance.clear()
            instance.set_status(401)
            instance.add_header("WWW-Authenticate",
                                "Basic realm=\"user and password ?\"")

        return wrapper
    return decorate
