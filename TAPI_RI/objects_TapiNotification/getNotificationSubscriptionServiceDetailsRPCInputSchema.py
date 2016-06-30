from objects_common.jsonObject import JsonObject

class GetNotificationSubscriptionServiceDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        super(GetNotificationSubscriptionServiceDetailsRPCInputSchema, self).__init__(json_struct)

