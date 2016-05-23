from objects_common.jsonObject import JsonObject
from nodeEdgePoint import NodeEdgePoint

class GetNodeEdgePointDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.nodeEdgePoint=NodeEdgePoint() #import
        super(GetNodeEdgePointDetailsRPCOutputSchema, self).__init__(json_struct)

