from tornado import websocket, web, ioloop
import json

class eventList(list):
    def __init__(self):
        super().__init__()
        self.appendEventListeners = []

    def eAppend(self, item):
        self.append(item)
        self.execute(self.appendEventListeners, item)

    def addEventListener(self, callback):
        self.appendEventListeners.append(callback)

    def delEventListener(self, callback):
        for callbacks, index in self.appendEventListeners:
            if callbacks ==  callback:
                pass

    def execute(self, eventList, item):
        for callback in eventList:
            callback(item)

cl = []
cHistory = eventList()


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("html/index.html")

class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        cHistory.addEventListener(self.message)
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        cl.append(message)
        cHistory.eAppend(message) 

    def on_close(self):
        if self in cl:
            cl.remove(self)

    def message(self, message):
        self.write_message(message)


app = web.Application([
    (r'/', IndexHandler),
    (r'/chat', SocketHandler),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/html/(.*)', web.StaticFileHandler, {'path': 'html/'}),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()


