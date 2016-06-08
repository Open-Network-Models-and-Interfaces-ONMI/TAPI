from objects_common.jsonObject import JsonObject
from subscriptionFilter import SubscriptionFilter

class CreateNotificationSubscriptionServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionFilter=SubscriptionFilter() #import
        self.subscriptionState=""
        super(CreateNotificationSubscriptionServiceRPCInputSchema, self).__init__(json_struct)

