from objects_common.jsonObject import JsonObject
from serviceEndPoint import ServiceEndPoint

class GetServiceEndPointDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEndPoint=ServiceEndPoint() #import
        super(GetServiceEndPointDetailsRPCOutputSchema, self).__init__(json_struct)

