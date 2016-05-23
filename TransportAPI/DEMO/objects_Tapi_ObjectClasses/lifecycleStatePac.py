from objects_common.jsonObject import JsonObject
from objects_common.enumType import EnumType

class LifecycleStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.lifecycleState=Lifecyclestate(0)
        super(LifecycleStatePac, self).__init__(json_struct)

class Lifecyclestate(EnumType):
    possible_values = ['PLANNED', 'POTENTIAL', 'INSTALLED', 'PENDING_REMOVAL']
    range_end = 4

    def __init__(self, initial_value):
        super(Lifecyclestate, self).__init__(initial_value)
