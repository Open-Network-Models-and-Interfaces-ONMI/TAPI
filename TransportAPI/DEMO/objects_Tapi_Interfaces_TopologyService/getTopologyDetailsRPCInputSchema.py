from objects_common.jsonObject import JsonObject

class GetTopologyDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.topologyIdOrName=""
        super(GetTopologyDetailsRPCInputSchema, self).__init__(json_struct)

