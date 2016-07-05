from lifecycleStatePac import LifecycleStatePac
from connectionEndPoint import ConnectionEndPoint
from layerProtocol import LayerProtocol
from nameAndValue import NameAndValue
from extensionsSpec import ExtensionsSpec
from resource import Resource
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class _serviceEndPointSchema(Resource):

    def __init__(self, json_struct=None):
        self.direction=Direction(0)
        self.uuid=""
        self.resourceSpecification=""
        self._state=LifecycleStatePac() #import
        self._connectionEndPoint=KeyedArrayType(ConnectionEndPoint, 'uuid')
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._mappedNodeEdgePoint=ArrayType.factory(str)
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_serviceEndPointSchema, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
