from objects_common.jsonObject import JsonObject

class GetServiceEndPointListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEndPoint=""
        super(GetServiceEndPointListRPCOutputSchema, self).__init__(json_struct)

