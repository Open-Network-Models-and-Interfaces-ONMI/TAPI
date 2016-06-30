from localClass import LocalClass
from objects_common.enumType import EnumType

class PathObjectiveFunction(LocalClass):

    def __init__(self, json_struct=None):
        self.linkUtilization=Linkutilization(0)
        self.costOptimization=Costoptimization(0)
        self.bandwidthOptimization=Bandwidthoptimization(0)
        self.concurrentPaths=Concurrentpaths(0)
        self.resourceSharing=Resourcesharing(0)
        super(PathObjectiveFunction, self).__init__(json_struct)

class Linkutilization(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Linkutilization, self).__init__(initial_value)
class Costoptimization(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Costoptimization, self).__init__(initial_value)
class Bandwidthoptimization(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Bandwidthoptimization, self).__init__(initial_value)
class Concurrentpaths(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Concurrentpaths, self).__init__(initial_value)
class Resourcesharing(EnumType):
    possible_values = ['MINIMIZE', 'MAXIMIZE', 'ALLOW', 'DISALLOW', 'DONT_CARE']
    range_end = 5

    def __init__(self, initial_value):
        super(Resourcesharing, self).__init__(initial_value)
