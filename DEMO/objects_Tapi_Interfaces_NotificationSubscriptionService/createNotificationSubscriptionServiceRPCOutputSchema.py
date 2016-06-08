from objects_common.jsonObject import JsonObject
from notificationSubscriptionService import NotificationSubscriptionService

class CreateNotificationSubscriptionServiceRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionService=NotificationSubscriptionService() #import
        super(CreateNotificationSubscriptionServiceRPCOutputSchema, self).__init__(json_struct)

