from layerProtocol import LayerProtocol
from adminStatePac import AdminStatePac
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class NodeEdgePoint(ResourceSpec):

    def __init__(self, json_struct=None):
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.direction=""
        self._state=AdminStatePac() #import
        self._clientNodeEdgePoint=ArrayType.factory(str)
        self._mappedServiceEndPoint=ArrayType.factory(str)
        super(NodeEdgePoint, self).__init__(json_struct)

