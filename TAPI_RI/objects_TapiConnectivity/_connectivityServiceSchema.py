from connectivityServicePort import ConnectivityServicePort
from nameAndValue import NameAndValue
from adminStatePac import AdminStatePac
from extensionsSpec import ExtensionsSpec
from connectivityConstraint import ConnectivityConstraint
from timeRange import TimeRange
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class _connectivityServiceSchema(ServiceSpec):

    def __init__(self, json_struct=None):
        self._connection=ArrayType.factory(str)
        self._servicePort=KeyedArrayType(ConnectivityServicePort, 'localId')
        self.direction=Direction(0)
        self.layerProtocolName=Layerprotocolname(0)
        self.uuid=""
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        self._state=AdminStatePac() #import
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self._connConstraint=ConnectivityConstraint() #import
        self._schedule=TimeRange() #import
        super(_connectivityServiceSchema, self).__init__(json_struct)

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
