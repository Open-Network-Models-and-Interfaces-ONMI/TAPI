import Queue
import json
import random
import threading
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory
import time
import signal


poolThreads = range(1,100)
web_sockets = dict()

class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Server connected: {0}".format(response.peer))

    def onOpen(self):
        print("WebSocket connection open.")

        def hello():
            self.sendMessage(u"Hello, world!".encode('utf8'))
            self.sendMessage(b"\x00\x01\x03\x04", isBinary=True)
            self.factory.reactor.callLater(1, hello)

        # start sending messages every second ..
        hello()

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(json.loads(payload.decode('utf8'))))
            print("From : "+self.factory.url)
            self.factory.notification_q.put(payload)

    def onClose(self, wasClean, code, reason):
        print code
        print("WebSocket connection closed: {0}".format(reason))


class WSClientFactory(threading.Thread, WebSocketClientFactory):
    def __init__(self, threadID, uri, notificationQ):
        self.threadID = threadID
        self.uri = uri
        self.notification_q = notificationQ
        self.running = True
        WebSocketClientFactory.__init__(self,'ws://'+str(self.uri[7:]), debug=True)
        threading.Thread.__init__(self)
        self.protocol = MyClientProtocol
        self.setProtocolOptions(openHandshakeTimeout=15)
        print self.uri
        address = self.uri[7:].split('/')[0]
        path =  self.uri[7:].split('/')[1:]

        ip = address.split(':')[0]
        port = address.split(':')[1]

        reactor.connectTCP(ip, int(port), self)

    def stop(self):
        self.running = False
