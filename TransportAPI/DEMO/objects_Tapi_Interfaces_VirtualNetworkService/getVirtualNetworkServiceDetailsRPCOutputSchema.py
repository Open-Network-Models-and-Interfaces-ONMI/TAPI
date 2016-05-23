from objects_common.jsonObject import JsonObject
from virtualNetworkService import VirtualNetworkService

class GetVirtualNetworkServiceDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.vnwService=VirtualNetworkService() #import
        super(GetVirtualNetworkServiceDetailsRPCOutputSchema, self).__init__(json_struct)

