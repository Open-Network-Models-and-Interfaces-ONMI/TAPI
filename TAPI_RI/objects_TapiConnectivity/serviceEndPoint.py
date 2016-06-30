from connectionEndPoint import ConnectionEndPoint
from lifecycleStatePac import LifecycleStatePac
from layerProtocol import LayerProtocol
from resource import Resource
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class ServiceEndPoint(Resource):

    def __init__(self, json_struct=None):
        self._mappedNodeEdgePoint=ArrayType.factory(str)
        self.direction=Direction(0)
        self._connectionEndPoint=KeyedArrayType(ConnectionEndPoint, 'uuid')
        self._state=LifecycleStatePac() #import
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        super(ServiceEndPoint, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
