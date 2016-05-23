from localClass import LocalClass
from objects_common.arrayType import ArrayType

class TeLink(LocalClass):

    def __init__(self, json_struct=None):
        self._nodeEdgePoint=ArrayType.factory(str)
        self._node=ArrayType.factory(str)
        super(TeLink, self).__init__(json_struct)

