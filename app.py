from typing import Any

import tornado.ioloop
import tornado.web
from loguru import logger
from tornado import httputil
from tornado.web import Application
from resources import header_server, body, top_ports
from tornado.log import enable_pretty_logging

enable_pretty_logging()


class MainHandler(tornado.web.RequestHandler):
    def __init__(self, application: "Application", request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.clear_header("server")
        self.add_header("server", header_server)

    def get(self):
        self.write(body + self.request.path.encode(errors="ignore"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/.*?", MainHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    listened_ports = []
    for i in top_ports:
        try:
            app.listen(i, address="0.0.0.0")
            listened_ports.append(i)
        except Exception as e:
            logger.warning("%s %s" % (e, i))
            pass
    logger.info("bind on %d port. start." % len(listened_ports))
    tornado.ioloop.IOLoop.current().start()
