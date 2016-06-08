from layerProtocol import LayerProtocol
from operationalStatePac import OperationalStatePac
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class ConnectionEndPoint(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._layerProtocol=ArrayType.factory(LayerProtocol)
        self._state=OperationalStatePac() #import
        self._serverNodeEdgePoint=""
        self._peerConnectionEndPoint=""
        self._ltpSpecData=LtpSpec() #import
        super(ConnectionEndPoint, self).__init__(json_struct)

