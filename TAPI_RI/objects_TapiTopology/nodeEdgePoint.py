from layerProtocol import LayerProtocol
from adminStatePac import AdminStatePac
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class NodeEdgePoint(ResourceSpec):

    def __init__(self, json_struct=None):
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.direction=Direction(0)
        self._state=AdminStatePac() #import
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._mappedServiceEndPoint=ArrayType.factory(str)
        super(NodeEdgePoint, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
