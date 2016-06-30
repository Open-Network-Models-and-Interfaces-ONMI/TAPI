from objects_common.jsonObject import JsonObject
from notificationSubscriptionService import NotificationSubscriptionService
from objects_common.arrayType import ArrayType

class GetNotificationSubscriptionServiceListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionService=ArrayType.factory(NotificationSubscriptionService)
        super(GetNotificationSubscriptionServiceListRPCOutputSchema, self).__init__(json_struct)

