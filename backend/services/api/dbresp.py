import json

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
import tornado.options
from tornado.log import enable_pretty_logging

# from ajmdContent.backend.service.api import authenticate
from authenticate import authenticate
from dbHandler import dbHandler
from sqlalchemy.orm import scoped_session, sessionmaker
from db import engine


import sys
reload(sys)
sys.setdefaultencoding('utf8')

tornado.options.define('blocking_log_threshold', default=None, type=float,
                       help='Log a warning (with stack trace) if the IOLoop is blocked for this many seconds')


class MainHandler(RequestHandler):
    """demo for get or post method !"""

    @authenticate()
    def get(self):
        self.__set_response_header()
        self.write("hello world!")

    @authenticate()
    def post(self):
        self.__set_response_header()
        data = json.loads(self.request.body.decode("utf-8"))
        print(data)

        self.write({
            "success": True
        })

    def options(self):
        self.__set_response_header()

    def __set_response_header(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods",
                        "POST,GET,OPTIONS,HEAD")


if __name__ == "__main__":

    handlers = [
        (r"/", MainHandler),
        (r"/db$", dbHandler),
    ]

    application = Application(handlers=handlers,
                              autoreload=True)

    application.listen(9883, xheaders=True)
    enable_pretty_logging()
    print "begin to service !"
    application.db = scoped_session(sessionmaker(
        bind=engine, autocommit=False, autoflush=True, expire_on_commit=False))

    IOLoop.current().start()
