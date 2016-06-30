from objects_common.jsonObject import JsonObject
from subscriptionFilter import SubscriptionFilter
from objects_common.enumType import EnumType

class UpdateNotificationSubscriptionServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.subscriptionIdOrName=""
        self.subscriptionFilter=SubscriptionFilter() #import
        self.subscriptionState=Subscriptionstate(0)
        super(UpdateNotificationSubscriptionServiceRPCInputSchema, self).__init__(json_struct)

class Subscriptionstate(EnumType):
    possible_values = ['SUSPENDED', 'ACTIVE']
    range_end = 2

    def __init__(self, initial_value):
        super(Subscriptionstate, self).__init__(initial_value)
