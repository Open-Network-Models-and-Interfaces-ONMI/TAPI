from connection import Connection
from connectivityServicePort import ConnectivityServicePort
from timeRange import TimeRange
from adminStatePac import AdminStatePac
from connectivityConstraint import ConnectivityConstraint
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class ConnectivityService(GlobalClass):

    def __init__(self, json_struct=None):
        self._connection=ArrayType.factory(Connection)
        self._servicePort=KeyedArrayType(ConnectivityServicePort, 'localId')
        self.direction=""
        self.layerProtocolName=""
        self._schedule=TimeRange() #import
        self._state=AdminStatePac() #import
        self._connConstraints=ConnectivityConstraint() #import
        super(ConnectivityService, self).__init__(json_struct)

