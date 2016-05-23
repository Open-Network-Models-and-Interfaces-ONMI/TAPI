from objects_common.jsonObject import JsonObject

class GetLinkDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.linkIdOrName=""
        self.topologyIdOrName=""
        super(GetLinkDetailsRPCInputSchema, self).__init__(json_struct)

