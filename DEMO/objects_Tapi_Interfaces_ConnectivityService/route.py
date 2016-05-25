from localClass import LocalClass
from objects_common.arrayType import ArrayType

class Route(LocalClass):

    def __init__(self, json_struct=None):
        self._lowerConnection=ArrayType.factory(str)
        super(Route, self).__init__(json_struct)

