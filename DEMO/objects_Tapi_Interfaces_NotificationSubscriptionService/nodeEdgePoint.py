from adminStatePac import AdminStatePac
from layerProtocol import LayerProtocol
from ltpSpec import LtpSpec
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class NodeEdgePoint(GlobalClass):

    def __init__(self, json_struct=None):
        self._state=AdminStatePac() #import
        self.direction=""
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._ltpSpecData=LtpSpec() #import
        super(NodeEdgePoint, self).__init__(json_struct)

