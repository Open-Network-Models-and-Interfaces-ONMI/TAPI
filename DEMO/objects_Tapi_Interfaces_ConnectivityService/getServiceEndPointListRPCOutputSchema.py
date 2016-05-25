from objects_common.jsonObject import JsonObject
from serviceEndPoint import ServiceEndPoint
from objects_common.arrayType import ArrayType

class GetServiceEndPointListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceEndPoint=ArrayType.factory(ServiceEndPoint)
        super(GetServiceEndPointListRPCOutputSchema, self).__init__(json_struct)

