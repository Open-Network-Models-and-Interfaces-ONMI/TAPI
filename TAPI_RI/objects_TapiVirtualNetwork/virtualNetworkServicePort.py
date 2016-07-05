from localClass import LocalClass
from objects_common.enumType import EnumType

class VirtualNetworkServicePort(LocalClass):

    def __init__(self, json_struct=None):
        self.serviceLayer=Servicelayer(0)
        self.direction=Direction(0)
        self.role=Role(0)
        self._serviceEndPoint=""
        super(VirtualNetworkServicePort, self).__init__(json_struct)

class Servicelayer(EnumType):
    possible_values = ['OCH', 'ODU', 'ETH', 'MPLS_TP']
    range_end = 4

    def __init__(self, initial_value):
        super(Servicelayer, self).__init__(initial_value)
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
