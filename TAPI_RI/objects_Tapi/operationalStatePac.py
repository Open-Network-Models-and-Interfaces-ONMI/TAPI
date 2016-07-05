from objects_common.jsonObject import JsonObject
from objects_common.enumType import EnumType

class OperationalStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.operationalState=Operationalstate(0)
        self.lifecycleState=Lifecyclestate(0)
        super(OperationalStatePac, self).__init__(json_struct)

class Operationalstate(EnumType):
    possible_values = ['DISABLED', 'ENABLED']
    range_end = 2

    def __init__(self, initial_value):
        super(Operationalstate, self).__init__(initial_value)
class Lifecyclestate(EnumType):
    possible_values = ['PLANNED', 'POTENTIAL', 'INSTALLED', 'PENDING_REMOVAL']
    range_end = 4

    def __init__(self, initial_value):
        super(Lifecyclestate, self).__init__(initial_value)
