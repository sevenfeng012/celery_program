#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-19
# @Author  : seven
# @Emial   : fengzhijian012@163.com
# @Link    : www.wortyby.com
# @Version : Version_1.0.0
# @Company : 阿基米德

from sqlalchemy import Column, String, Integer, VARCHAR, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from db import engine, Base


class Article(Base):
    """orm sql"""

    __tablename__ = 'articles'
    user = Column(VARCHAR(20), primary_key=True)
    title = Column(VARCHAR(40))
    time = Column(VARCHAR(20))
    content = Column(VARCHAR(2000))

    def setup():
        pass

    def tearDown():
        pass

Base.metadata.create_all(engine)
