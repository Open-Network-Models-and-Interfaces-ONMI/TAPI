from connection import Connection
from connectivityServicePort import ConnectivityServicePort
from scheduleInfo import ScheduleInfo
from adminStatePac import AdminStatePac
from connectivityConstraint import ConnectivityConstraint
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class ConnectivityService(GlobalClass):

    def __init__(self, json_struct=None):
        self._connection=KeyedArrayType(Connection, 'uuid')
        self._servicePort=KeyedArrayType(ConnectivityServicePort, 'localId')
        self.direction=""
        self.layerProtocolName=""
        self._schedule=ScheduleInfo() #import
        self._state=AdminStatePac() #import
        self._connConstraints=ConnectivityConstraint() #import
        super(ConnectivityService, self).__init__(json_struct)

