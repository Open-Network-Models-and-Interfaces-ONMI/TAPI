from objects_common.jsonObject import JsonObject
from path import Path
from objects_common.arrayType import ArrayType

class OptimizeP2PPathRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.path=ArrayType.factory(Path)
        super(OptimizeP2PPathRPCOutputSchema, self).__init__(json_struct)

