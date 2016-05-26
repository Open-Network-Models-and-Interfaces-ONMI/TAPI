from objects_common.jsonObject import JsonObject
from connectivityConstraint import ConnectivityConstraint
from scheduleInfo import ScheduleInfo

class UpdateConnectivityServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connConstraint=ConnectivityConstraint() #import
        self.connSchedule=ScheduleInfo() #import
        self.serviceIdOrName=""
        super(UpdateConnectivityServiceRPCInputSchema, self).__init__(json_struct)

