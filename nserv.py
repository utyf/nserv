import json
import os.path
from ConfigParser import ConfigParser

from gredis.client import AsyncRedis
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.web import (
    Application,
    StaticFileHandler,
    url
)

config = ConfigParser()
config.read('nserv.ini')

redis = AsyncRedis(
    config.get('redis', 'host'),
    config.get('redis', 'port'),
)


class NotificationHandler(WebSocketHandler):
    """
    Websocket handler for "pushing" notifications to the client
    """
    @gen.coroutine
    def open(self):
        pubsub = redis.pubsub()
        yield pubsub.subscribe(config.get('redis' , 'channel'))

        while True:
            message = yield pubsub.get_message(True)
            if message['type'] == 'message':
                try:
                    self.write_message(message['data'])
                except WebSocketClosedError:
                    return


    def check_origin(self, origin):
        """
        Always pass cross-origin check
        """
        return True


def notify(text, level):
    # publish notification synchroniously (blocking)
    redis.to_blocking_client().publish(
        config.get('redis', 'channel'),
        json.dumps(dict(
            text=text,
            level=level
        ))
    )


def main():
    # path for html + js
    static_path = os.path.join(
        os.path.dirname(__file__),
        'ui'
    )

    app = Application(
        [
            url(r'/notifications', NotificationHandler),
            url(r'/(.*)', StaticFileHandler, dict(path=static_path)),
        ],
    )

    app.listen(config.get('web', 'port'))
    IOLoop.current().start()


if __name__ == '__main__':
    main()
