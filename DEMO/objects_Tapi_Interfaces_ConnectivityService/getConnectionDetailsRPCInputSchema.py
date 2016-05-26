from objects_common.jsonObject import JsonObject

class GetConnectionDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceIdOrName=""
        self.connectionIdOrName=""
        super(GetConnectionDetailsRPCInputSchema, self).__init__(json_struct)

