from lifecycleStatePac import LifecycleStatePac
from connectionEndPoint import ConnectionEndPoint
from layerProtocol import LayerProtocol
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class ServiceEndPoint(GlobalClass):

    def __init__(self, json_struct=None):
        self.direction=""
        self._state=LifecycleStatePac() #import
        self._connectionEndPoint=KeyedArrayType(ConnectionEndPoint, 'uuid')
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self._mappedNodeEdgePoint=ArrayType.factory(str)
        self._ltpSpecData=LtpSpec() #import
        super(ServiceEndPoint, self).__init__(json_struct)

