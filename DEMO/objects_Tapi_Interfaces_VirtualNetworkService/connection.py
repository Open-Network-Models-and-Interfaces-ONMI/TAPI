from route import Route
from connectionPort import ConnectionPort
from operationalStatePac import OperationalStatePac
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class Connection(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self.layerProtocolName=""
        self._route=ArrayType.factory(Route)
        self._connectionPort=ArrayType.factory(ConnectionPort)
        self._state=OperationalStatePac() #import
        self._node=""
        super(Connection, self).__init__(json_struct)

