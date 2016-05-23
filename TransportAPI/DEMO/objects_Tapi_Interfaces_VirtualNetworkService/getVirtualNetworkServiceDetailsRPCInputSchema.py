from objects_common.jsonObject import JsonObject

class GetVirtualNetworkServiceDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        super(GetVirtualNetworkServiceDetailsRPCInputSchema, self).__init__(json_struct)

