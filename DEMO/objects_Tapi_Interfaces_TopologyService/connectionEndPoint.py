from operationalStatePac import OperationalStatePac
from layerProtocol import LayerProtocol
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class ConnectionEndPoint(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._state=OperationalStatePac() #import
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self._serverNodeEdgePoint=""
        self._peerConnectionEndPoint=""
        self._ltpSpecData=LtpSpec() #import
        super(ConnectionEndPoint, self).__init__(json_struct)

