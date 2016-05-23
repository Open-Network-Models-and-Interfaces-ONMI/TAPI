from objects_common.jsonObject import JsonObject

class GetConnectionEndPointDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        self.connEPIdOrName=""
        self.connectionIdOrName=""
        super(GetConnectionEndPointDetailsRPCInputSchema, self).__init__(json_struct)

