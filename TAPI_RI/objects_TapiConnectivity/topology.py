from node import Node
from link import Link
from resource import Resource
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class Topology(Resource):

    def __init__(self, json_struct=None):
        self._node=KeyedArrayType(Node, 'uuid')
        self.layerProtocolName=ArrayType.factory(str)
        self._link=KeyedArrayType(Link, 'uuid')
        super(Topology, self).__init__(json_struct)

