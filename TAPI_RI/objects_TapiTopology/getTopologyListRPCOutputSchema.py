from objects_common.jsonObject import JsonObject
from topology import Topology
from objects_common.arrayType import ArrayType

class GetTopologyListRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.topology=ArrayType.factory(Topology)
        super(GetTopologyListRPCOutputSchema, self).__init__(json_struct)

