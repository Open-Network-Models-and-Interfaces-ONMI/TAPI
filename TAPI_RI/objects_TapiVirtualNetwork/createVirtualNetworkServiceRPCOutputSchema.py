from objects_common.jsonObject import JsonObject
from virtualNetworkService import VirtualNetworkService

class CreateVirtualNetworkServiceRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.vnwService=VirtualNetworkService() #import
        super(CreateVirtualNetworkServiceRPCOutputSchema, self).__init__(json_struct)

