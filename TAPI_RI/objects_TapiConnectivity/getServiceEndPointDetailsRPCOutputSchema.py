from objects_common.jsonObject import JsonObject

class GetServiceEndPointDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEndPoint=""
        super(GetServiceEndPointDetailsRPCOutputSchema, self).__init__(json_struct)

