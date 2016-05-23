from objects_common.jsonObject import JsonObject

class DeleteConnectivityServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        super(DeleteConnectivityServiceRPCInputSchema, self).__init__(json_struct)

