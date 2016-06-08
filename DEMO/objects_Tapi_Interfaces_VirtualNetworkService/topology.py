from node import Node
from link import Link
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class Topology(GlobalClass):

    def __init__(self, json_struct=None):
        self._node=ArrayType.factory(Node)
        self.layerProtocolName=ArrayType.factory(str)
        self._link=ArrayType.factory(Link)
        super(Topology, self).__init__(json_struct)

