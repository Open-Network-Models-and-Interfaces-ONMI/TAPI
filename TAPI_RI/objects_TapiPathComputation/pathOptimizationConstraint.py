from localClass import LocalClass
from objects_common.enumType import EnumType

class PathOptimizationConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.trafficInterruption=Trafficinterruption(0)
        super(PathOptimizationConstraint, self).__init__(json_struct)

class Trafficinterruption(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Trafficinterruption, self).__init__(initial_value)
