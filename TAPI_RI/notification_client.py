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
poolSubscriberIds = range(1,100)
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
        WebSocketClientFactory.__init__(self,'ws://'+str(self.uri[7:]))
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

class NotificationService(threading.Thread):
    def __init__(self, notification_q):
        super(NotificationService, self).__init__()
        self.notification_queue = notification_q
        self.running = True
        self.clients = {}
        #self.subscribers = {}
        #self.backend = backend

    def addClient(self, uri, notification_q):
        threadId = getValidId(poolThreads)
        self.clients[threadId] = WSClientFactory(threadId, uri, notification_q)
        self.clients[threadId].start()


    def run(self):
        while self.running:
            if not self.notification_queue.empty():
                notification =  self.notification_queue.get()
                ## Here the notifications received by all clients are printed.
                ## TODO: Link the notification service with the services which are subscribed to the notification service,
                ## TODO(CONTINUE): for instance the another nofication server responsible to propagate the notifications or
                ## TODO(CONTINUE): some other intermediate module which processes the information received.
                print notification


    def stop(self):
        for sock in self.clients:
            self.clients[sock].stop()

        self.running = False


def getValidId(pool):
    valid = False

    while not valid:
        id = random.randint(1,100)
        if id in pool:
            valid=True
            del pool[pool.index(id)]

    return id


class LoopCheck(threading.Thread):

    def __init__(self, event, notification_service):
        super(LoopCheck, self).__init__()
        self.event = event
        self.notification_service = notification_service

    def run(self):
        while not self.event.is_set():
            time.sleep(1)

        self.notification_service.stop()
        reactor.stop()


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    status.set()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler )

    notification_q = Queue.Queue()
    backend_service = NotificationService(notification_q)
    backend_service.start()

    status = threading.Event()
    server_status = LoopCheck(status, backend_service)
    server_status.daemon = True
    server_status.start()

    backend_service.addClient('http://localhost:8182/restconf/streams/NotificationService', notification_q)
    try:
        reactor.run()
    except KeyboardInterrupt:
        print "Keyboard interrupt"
        reactor.stop()
