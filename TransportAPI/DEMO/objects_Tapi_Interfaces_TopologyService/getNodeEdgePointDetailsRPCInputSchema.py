from objects_common.jsonObject import JsonObject

class GetNodeEdgePointDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.epIdOrName=""
        self.topologyIdOrName=""
        self.nodeIdOrName=""
        super(GetNodeEdgePointDetailsRPCInputSchema, self).__init__(json_struct)

