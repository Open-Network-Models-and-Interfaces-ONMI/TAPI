from route import Route
from connectionPort import ConnectionPort
from operationalStatePac import OperationalStatePac
from resourceSpec import ResourceSpec
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class Connection(ResourceSpec):

    def __init__(self, json_struct=None):
        self.direction=Direction(0)
        self.layerProtocolName=Layerprotocolname(0)
        self._route=KeyedArrayType(Route, 'localId')
        self._connectionPort=KeyedArrayType(ConnectionPort, 'localId')
        self._state=OperationalStatePac() #import
        self._node=""
        super(Connection, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'UNIDIRECTIONAL', 'UNDEFINED_OR_UNKNOWN']
    range_end = 3

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
class Layerprotocolname(EnumType):
    possible_values = ['OCH', 'ODU', 'ETH', 'MPLS_TP']
    range_end = 4

    def __init__(self, initial_value):
        super(Layerprotocolname, self).__init__(initial_value)
