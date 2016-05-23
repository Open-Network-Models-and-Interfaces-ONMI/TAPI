from connection import Connection
from connectivityServicePort import ConnectivityServicePort
from scheduleInfo import ScheduleInfo
from adminStatePac import AdminStatePac
from connectivityConstraint import ConnectivityConstraint
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class ConnectivityService(GlobalClass):

    def __init__(self, json_struct=None):
        self._connection=KeyedArrayType(Connection, 'uuid')
        self._servicePort=KeyedArrayType(ConnectivityServicePort, 'localId')
        self.direction=Direction(0)
        self.layerProtocolName=Layerprotocolname(0)
        self._schedule=ScheduleInfo() #import
        self._state=AdminStatePac() #import
        self._connConstraints=ConnectivityConstraint() #import
        super(ConnectivityService, self).__init__(json_struct)

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
