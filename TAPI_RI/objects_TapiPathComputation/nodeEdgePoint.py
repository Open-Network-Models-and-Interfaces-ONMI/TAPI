from layerProtocol import LayerProtocol
from adminStatePac import AdminStatePac
from resource import Resource
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class NodeEdgePoint(Resource):

    def __init__(self, json_struct=None):
        self._layerProtocol=KeyedArrayType(LayerProtocol, 'localId')
        self.direction=""
        self._state=AdminStatePac() #import
        self._clientNodeEdgePoint=ArrayType.factory(str)
        super(NodeEdgePoint, self).__init__(json_struct)

