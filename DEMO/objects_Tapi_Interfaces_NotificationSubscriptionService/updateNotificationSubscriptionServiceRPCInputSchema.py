from objects_common.jsonObject import JsonObject
from subscriptionFilter import SubscriptionFilter

class UpdateNotificationSubscriptionServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        self.subscriptionFilter=SubscriptionFilter() #import
        self.subscriptionState=""
        super(UpdateNotificationSubscriptionServiceRPCInputSchema, self).__init__(json_struct)

