from objects_common.jsonObject import JsonObject
from virtualNetworkServicePort import VirtualNetworkServicePort
from virtualNetworkConstraint import VirtualNetworkConstraint
from objects_common.arrayType import ArrayType

class CreateVirtualNetworkServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.servicePort=ArrayType.factory(VirtualNetworkServicePort)
        self.connSchedule=""
        self.vnwConstraint=VirtualNetworkConstraint() #import
        super(CreateVirtualNetworkServiceRPCInputSchema, self).__init__(json_struct)

