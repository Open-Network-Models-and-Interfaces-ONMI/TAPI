from objects_common.jsonObject import JsonObject
from connectivityConstraint import ConnectivityConstraint
from timeRange import TimeRange
from connectivityServicePort import ConnectivityServicePort
from objects_common.arrayType import ArrayType

class CreateConnectivityServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connConstraint=ConnectivityConstraint() #import
        self.connSchedule=TimeRange() #import
        self.servicePort=ArrayType.factory(ConnectivityServicePort)
        super(CreateConnectivityServiceRPCInputSchema, self).__init__(json_struct)

