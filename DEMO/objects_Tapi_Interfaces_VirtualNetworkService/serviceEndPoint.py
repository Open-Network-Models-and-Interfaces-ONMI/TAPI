from layerProtocol import LayerProtocol
from connectionEndPoint import ConnectionEndPoint
from lifecycleStatePac import LifecycleStatePac
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class ServiceEndPoint(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self._layerProtocol=ArrayType.factory(LayerProtocol)
        self._connectionEndPoint=ArrayType.factory(ConnectionEndPoint)
        self._state=LifecycleStatePac() #import
        self._mappedNodeEdgePoint=ArrayType.factory(str)
        self._ltpSpecData=LtpSpec() #import
        super(ServiceEndPoint, self).__init__(json_struct)

