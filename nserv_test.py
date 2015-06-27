from tornado import testing
from tornado import web, websocket

from nserv import (
    NotificationHandler,
    config,
    redis
)

TEST_STRING = 'TeStStRiNg'

# send test messages through other channel
config.set('redis', 'notifications_test')

class NotificationHandlerTest(testing.AsyncHTTPTestCase):
    def get_app(self):
        return web.Application([
            ('/notifications', NotificationHandler)
        ])

    def get_protocol(self):
        """ Make AsyncHTTPTestCase compatible with websockets """
        return 'ws'

    @testing.gen_test
    def test_message(self):
        client = yield websocket.websocket_connect(
            self.get_url('/notifications')
        )

        while True:
            yield redis.publish(config.get('redis', 'channel'), TEST_STRING)
            msg = yield client.read_message()
            self.assertEqual(msg, TEST_STRING)

            return
