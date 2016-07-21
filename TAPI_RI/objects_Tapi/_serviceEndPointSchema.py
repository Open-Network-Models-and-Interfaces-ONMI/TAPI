from layerProtocol import LayerProtocol
from lifecycleStatePac import LifecycleStatePac
from nameAndValue import NameAndValue
from extensionsSpec import ExtensionsSpec
from resourceSpec import ResourceSpec
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class _serviceEndPointSchema(ResourceSpec):

    def __init__(self, json_struct=None):
        self.direction=Direction(0)
        self.uuid=""
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self._state=LifecycleStatePac() #import
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_serviceEndPointSchema, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
