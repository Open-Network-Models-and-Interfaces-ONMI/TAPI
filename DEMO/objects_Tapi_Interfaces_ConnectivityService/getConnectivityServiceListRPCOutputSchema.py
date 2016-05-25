from objects_common.jsonObject import JsonObject
from connectivityService import ConnectivityService
from objects_common.arrayType import ArrayType

class GetConnectivityServiceListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connService=ArrayType.factory(ConnectivityService)
        super(GetConnectivityServiceListRPCOutputSchema, self).__init__(json_struct)

