from objects_common.jsonObject import JsonObject

class GetConnectivityServiceDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        super(GetConnectivityServiceDetailsRPCInputSchema, self).__init__(json_struct)

