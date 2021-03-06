#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德


"""

# ready for mysql
# DB_HOST
# DB_USER
# DB_PWD
# DB_NAME

"""

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PWD = ''
DB_NAME = 'lession_for_sqlalchemy'


from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@staticmethod
def sqlalchemy_json(self):
    obj_dict = self.__dict__

    return dict((key, obj_dict[key]) for key in obj_dict if not key.startwith("_"))

Base.__json__ = sqlalchemy_json

# sqlite://<nohostname>/<path>
engine = create_engine('sqlite:///lession_for_sqlalchemy.db', echo=True)
metadata = MetaData(engine)

metadata.create_all()
