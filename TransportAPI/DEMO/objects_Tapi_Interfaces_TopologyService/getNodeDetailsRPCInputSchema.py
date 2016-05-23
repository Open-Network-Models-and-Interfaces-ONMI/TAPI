from objects_common.jsonObject import JsonObject

class GetNodeDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.topologyIdOrName=""
        self.nodeIdOrName=""
        super(GetNodeDetailsRPCInputSchema, self).__init__(json_struct)

