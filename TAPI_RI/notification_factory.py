from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

import time
import thread

from funcs_TapiNotification.notificationImpl import NotificationImpl
class BaseService:

    def __init__(self, proto):
        self.proto = proto

    def onOpen(self):
        pass


    def onClose(self, wasClean, code, reason):
        self.proto.sendClose(code=1000)

    def onMessage(self, payload, isBinary):
        pass


class NotificationService(BaseService):

    def onOpen(self):
        backend = NotificationImpl(self.proto)
        backend.start()
        thread.start_new_thread(self.onAsyncronousEvent,(backend, 5))

    def onMessage(self, payload, isBinary):
        pass


    def onAsyncronousEvent(self, backend, timer):
        time.sleep(timer)
        backend.set_event(False)


class ServiceServerProtocol(WebSocketServerProtocol):

    SERVICEMAP = { '/restconf/streams/NotificationService' : NotificationService }

    def __init__(self):
        super(ServiceServerProtocol, self).__init__()
        self.service = None

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))
        if request.path in self.SERVICEMAP:
            cls = self.SERVICEMAP[request.path]
            self.service = cls(self)
        else:
            err = "No service under %s" % request.path
            print(err)

    def onOpen(self):
        if self.service:
            self.service.onOpen()

    def onMessage(self, payload, isBinary):
        if self.service:
            self.service.onMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        if self.service:
            self.service.onClose(wasClean, code, reason)


class NotificationServerFactory():

    def __init__(self):
        print '\nRunning notification server in port 8182'
        factory = WebSocketServerFactory('ws://localhost:8182')
        factory.protocol = ServiceServerProtocol
        listenWS(factory)
        try:
            reactor.run(installSignalHandlers=0)
        except KeyboardInterrupt:
            reactor.stop()
