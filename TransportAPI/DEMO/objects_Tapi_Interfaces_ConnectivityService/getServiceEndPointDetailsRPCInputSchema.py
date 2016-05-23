from objects_common.jsonObject import JsonObject

class GetServiceEndPointDetailsRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEPIdOrName=""
        super(GetServiceEndPointDetailsRPCInputSchema, self).__init__(json_struct)

