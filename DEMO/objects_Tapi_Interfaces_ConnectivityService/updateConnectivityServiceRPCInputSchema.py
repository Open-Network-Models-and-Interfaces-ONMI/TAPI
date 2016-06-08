from objects_common.jsonObject import JsonObject
from connectivityConstraint import ConnectivityConstraint
from timeRange import TimeRange

class UpdateConnectivityServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connConstraint=ConnectivityConstraint() #import
        self.connSchedule=TimeRange() #import
        self.serviceIdOrName=""
        super(UpdateConnectivityServiceRPCInputSchema, self).__init__(json_struct)

