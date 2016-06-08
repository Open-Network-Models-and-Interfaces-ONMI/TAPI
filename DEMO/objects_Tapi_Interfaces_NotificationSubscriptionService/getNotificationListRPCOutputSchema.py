from objects_common.jsonObject import JsonObject
from notification import Notification
from objects_common.arrayType import ArrayType

class GetNotificationListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.notification=ArrayType.factory(Notification)
        super(GetNotificationListRPCOutputSchema, self).__init__(json_struct)

