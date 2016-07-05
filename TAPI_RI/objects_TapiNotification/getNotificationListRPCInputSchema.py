from objects_common.jsonObject import JsonObject

class GetNotificationListRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        self.timePeriod=""
        super(GetNotificationListRPCInputSchema, self).__init__(json_struct)

