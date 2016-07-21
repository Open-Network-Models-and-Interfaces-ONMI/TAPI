from objects_common.jsonObject import JsonObject
from layerProtocol import LayerProtocol
from lifecycleStatePac import LifecycleStatePac
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class ServiceEndPoint(JsonObject):

    def __init__(self, json_struct=None):
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.direction=Direction(0)
        self._state=LifecycleStatePac() #import
        super(ServiceEndPoint, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
