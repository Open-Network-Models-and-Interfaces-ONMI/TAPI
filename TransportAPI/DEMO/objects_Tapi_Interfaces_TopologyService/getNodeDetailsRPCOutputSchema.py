from objects_common.jsonObject import JsonObject
from node import Node

class GetNodeDetailsRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.node=Node() #import
        super(GetNodeDetailsRPCOutputSchema, self).__init__(json_struct)

