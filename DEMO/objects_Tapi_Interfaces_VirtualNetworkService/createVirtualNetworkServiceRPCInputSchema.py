from objects_common.jsonObject import JsonObject
from virtualNetworkConstraint import VirtualNetworkConstraint
from timeRange import TimeRange
from virtualNetworkServicePort import VirtualNetworkServicePort
from objects_common.arrayType import ArrayType

class CreateVirtualNetworkServiceRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.vnwConstraint=VirtualNetworkConstraint() #import
        self.connSchedule=TimeRange() #import
        self.servicePort=ArrayType.factory(VirtualNetworkServicePort)
        super(CreateVirtualNetworkServiceRPCInputSchema, self).__init__(json_struct)

