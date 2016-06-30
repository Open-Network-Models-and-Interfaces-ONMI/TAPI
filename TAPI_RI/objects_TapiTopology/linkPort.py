from localClass import LocalClass
from objects_common.enumType import EnumType

class LinkPort(LocalClass):

    def __init__(self, json_struct=None):
        self._nodeEdgePoint=""
        self.direction=Direction(0)
        self.role=Role(0)
        super(LinkPort, self).__init__(json_struct)

class Direction(EnumType):
    possible_values = ['BIDIRECTIONAL', 'INPUT', 'OUTPUT', 'UNIDENTIFIED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Direction, self).__init__(initial_value)
class Role(EnumType):
    possible_values = ['SYMMETRIC', 'ROOT', 'LEAF', 'UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Role, self).__init__(initial_value)
