from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class LayerProtocolTransitionPac(JsonObject):

    def __init__(self, json_struct=None):
        self._nodeEdgePoint=ArrayType.factory(str)
        self.transitionedLayerProtocolName=ArrayType.factory(str)
        super(LayerProtocolTransitionPac, self).__init__(json_struct)

