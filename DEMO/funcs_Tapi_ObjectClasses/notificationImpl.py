import os.path, sys
import threading
import json
import time
import datetime
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__))))

from objects_Tapi_ObjectClasses.notification import Notification


class NotificationImpl (threading.Thread):
    def __init__(self, handler):
        threading.Thread.__init__(self)
        self.event = True
        self.handler = handler

    def set_event(self, event):
        print 'Event occur - sending notification'
        self.event = event

    def run(self):
        while self.event:
            time.sleep(1)
        timestamp=time.time()
        st = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
        payload = json.dumps(Notification({"notificationId":"notif1", "notificationType": "STATE_CHANGE", "targetObjectType":"TOPOLOGY", "targetObjectIdentifier":"top0", "eventTimeStamp": str(st) }).json_serializer()).encode('utf8')
        self.handler.sendMessage(payload, False)
