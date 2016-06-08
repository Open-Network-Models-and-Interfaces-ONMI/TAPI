import random
import threading
import Queue
from twisted.internet import reactor
import time
import signal
from notificationClientFactory import WSClientFactory

__author__ = 'amll'

poolThreads = range(1,100)
poolSubscriberIds = range(1,100)


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

    backend_service.addClient('http://localhost:8788/restconf/streams/Notification', notification_q)

    try:
        reactor.run()
    except KeyboardInterrupt:
        print "Keyboard interrupt"
        reactor.stop()
        
