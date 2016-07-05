from objects_common.jsonObject import JsonObject

class DeleteP2PPathRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.pathIdOrName=""
        super(DeleteP2PPathRPCInputSchema, self).__init__(json_struct)

