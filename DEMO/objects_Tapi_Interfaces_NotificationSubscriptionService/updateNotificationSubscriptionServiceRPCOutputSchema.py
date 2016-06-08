from objects_common.jsonObject import JsonObject
from notificationSubscriptionService import NotificationSubscriptionService

class UpdateNotificationSubscriptionServiceRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionService=NotificationSubscriptionService() #import
        super(UpdateNotificationSubscriptionServiceRPCOutputSchema, self).__init__(json_struct)

