from objects_common.jsonObject import JsonObject
from objects_common.enumType import EnumType

class AdminStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.administrativeState=Administrativestate(0)
        self.operationalState=Operationalstate(0)
        self.lifecycleState=Lifecyclestate(0)
        super(AdminStatePac, self).__init__(json_struct)

class Administrativestate(EnumType):
    possible_values = ['LOCKED', 'UNLOCKED']
    range_end = 2

    def __init__(self, initial_value):
        super(Administrativestate, self).__init__(initial_value)
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
