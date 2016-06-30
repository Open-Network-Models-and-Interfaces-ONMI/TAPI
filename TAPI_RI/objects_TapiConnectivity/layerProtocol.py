from localClass import LocalClass
from objects_common.enumType import EnumType

class LayerProtocol(LocalClass):

    def __init__(self, json_struct=None):
        self.terminationState=""
        self.layerProtocolName=Layerprotocolname(0)
        self.terminationDirection=Terminationdirection(0)
        super(LayerProtocol, self).__init__(json_struct)

class Layerprotocolname(EnumType):
    possible_values = ['OCH', 'ODU', 'ETH', 'MPLS_TP']
    range_end = 4

    def __init__(self, initial_value):
        super(Layerprotocolname, self).__init__(initial_value)
class Terminationdirection(EnumType):
    possible_values = ['BIDIRECTIONAL', 'SINK', 'SOURCE', 'UNDEFINED_OR_UNKNOWN']
    range_end = 4

    def __init__(self, initial_value):
        super(Terminationdirection, self).__init__(initial_value)
