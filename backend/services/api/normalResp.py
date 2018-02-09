import json

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
import tornado.options

from backend.services.api.authenticate import authenticate
from authenticate import authenticate

tornado.options.define('blocking_log_threshold', default=None, type=float,
                       help='Log a warning (with stack trace) if the IOLoop is blocked for this many seconds')


class MainHandler(RequestHandler):
    """demo for get or post method !"""

    @authenticate()
    def get(self):
        self.__set_response_header()
        self.write("hello service!")

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
    tornado.options.parse_command_line()

    handlers = [
        (r"/", MainHandler),
    ]

    application = Application(handlers=handlers,
                              autoreload=True)

    application.listen(9884, xheaders=True)
    print "begin to service !"
    IOLoop.current().start()
