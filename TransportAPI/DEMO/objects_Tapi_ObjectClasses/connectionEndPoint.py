from operationalStatePac import OperationalStatePac
from layerProtocol import LayerProtocol
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class ConnectionEndPoint(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=Direction(0)
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._state=OperationalStatePac() #import
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self._serverNodeEdgePoint=""
        self._peerConnectionEndPoint=""
        self._ltpSpecData=LtpSpec() #import
        super(ConnectionEndPoint, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
