from objects_common.jsonObject import JsonObject
from topology import Topology

class GetTopologyDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.topology=Topology() #import
        super(GetTopologyDetailsRPCOutputSchema, self).__init__(json_struct)

