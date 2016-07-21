from objects_common.jsonObject import JsonObject

class NotificationChannel(JsonObject):

    def __init__(self, json_struct=None):
        self.streamAddress=""
        self.nextSequenceNo=""
        super(NotificationChannel, self).__init__(json_struct)

