from adminStatePac import AdminStatePac
from ltpSpec import LtpSpec
from layerProtocol import LayerProtocol
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class NodeEdgePoint(GlobalClass):

    def __init__(self, json_struct=None):
        self._state=AdminStatePac() #import
        self._ltpSpecData=LtpSpec() #import
        self.direction=""
        self._layerProtocol=ArrayType.factory(LayerProtocol)
        self._clientNodeEdgePoint=ArrayType.factory(str)
        super(NodeEdgePoint, self).__init__(json_struct)

