from route import Route
from connectionPort import ConnectionPort
from operationalStatePac import OperationalStatePac
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class Connection(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self.layerProtocolName=""
        self._route=KeyedArrayType(Route, 'localId')
        self._connectionPort=KeyedArrayType(ConnectionPort, 'localId')
        self._state=OperationalStatePac() #import
        self._node=""
        super(Connection, self).__init__(json_struct)

