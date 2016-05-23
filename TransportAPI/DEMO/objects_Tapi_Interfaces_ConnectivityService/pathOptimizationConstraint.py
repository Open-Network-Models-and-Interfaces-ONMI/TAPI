from objects_common.jsonObject import JsonObject

class PathOptimizationConstraint(JsonObject):

    def __init__(self, json_struct=None):
        self.trafficInterruption=""
        super(PathOptimizationConstraint, self).__init__(json_struct)

