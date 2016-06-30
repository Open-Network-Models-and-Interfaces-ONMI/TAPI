from localClass import LocalClass
from objects_common.enumType import EnumType

class LayerProtocol(LocalClass):

    def __init__(self, json_struct=None):
        self.terminationState=Terminationstate(0)
        self.layerProtocolName=Layerprotocolname(0)
        self.terminationDirection=Terminationdirection(0)
        super(LayerProtocol, self).__init__(json_struct)

class Terminationstate(EnumType):
    possible_values = ['LP_CAN_NEVER_TERMINATE', 'LT_NOT_TERMINATED', 'TERMINATED_SERVER_TO_CLIENT_FLOW', 'TERMINATED_CLIENT_TO_SERVER_FLOW', 'TERMINATED_BIDIRECTIONAL', 'LT_PERMENANTLY_TERMINATED', 'TERMINATION_STATE_UNKNOWN']
    range_end = 7

    def __init__(self, initial_value):
        super(Terminationstate, self).__init__(initial_value)
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
