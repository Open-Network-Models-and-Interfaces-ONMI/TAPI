from objects_common.jsonObject import JsonObject
from timeRange import TimeRange

class GetNotificationListRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        self.timePeriod=TimeRange() #import
        super(GetNotificationListRPCInputSchema, self).__init__(json_struct)

