from objects_common.jsonObject import JsonObject
from connectivityService import ConnectivityService

class CreateConnectivityServiceRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connService=ConnectivityService() #import
        super(CreateConnectivityServiceRPCOutputSchema, self).__init__(json_struct)

