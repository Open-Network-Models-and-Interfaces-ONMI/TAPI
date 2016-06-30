from objects_common.jsonObject import JsonObject
from connectivityConstraint import ConnectivityConstraint
from connectivityServicePort import ConnectivityServicePort
from objects_common.arrayType import ArrayType

class CreateConnectivityServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connConstraint=ConnectivityConstraint() #import
        self.connSchedule=""
        self.servicePort=ArrayType.factory(ConnectivityServicePort)
        super(CreateConnectivityServiceRPCInputSchema, self).__init__(json_struct)

