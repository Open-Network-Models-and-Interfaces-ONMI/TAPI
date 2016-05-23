from objects_common.jsonObject import JsonObject
from virtualNetworkService import VirtualNetworkService
from objects_common.arrayType import ArrayType

class GetVirtualNetworkServiceListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.vnwService=ArrayType.factory(VirtualNetworkService)
        super(GetVirtualNetworkServiceListRPCOutputSchema, self).__init__(json_struct)

