from objects_common.jsonObject import JsonObject

class DeleteNotificationSubscriptionServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        super(DeleteNotificationSubscriptionServiceRPCInputSchema, self).__init__(json_struct)

