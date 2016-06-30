from objects_common.jsonObject import JsonObject

class DeleteVirtualNetworkServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        super(DeleteVirtualNetworkServiceRPCInputSchema, self).__init__(json_struct)

