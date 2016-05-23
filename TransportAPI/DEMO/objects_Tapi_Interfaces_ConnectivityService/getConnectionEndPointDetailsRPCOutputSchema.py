from objects_common.jsonObject import JsonObject
from connectionEndPoint import ConnectionEndPoint

class GetConnectionEndPointDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.connEP=ConnectionEndPoint() #import
        super(GetConnectionEndPointDetailsRPCOutputSchema, self).__init__(json_struct)

