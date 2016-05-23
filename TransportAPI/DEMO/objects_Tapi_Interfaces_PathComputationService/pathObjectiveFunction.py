from objects_common.jsonObject import JsonObject

class PathObjectiveFunction(JsonObject):

    def __init__(self, json_struct=None):
        self.linkUtilization=""
        self.costOptimization=""
        self.bandwidthOptimization=""
        self.concurrentPaths=""
        self.resourceSharing=""
        super(PathObjectiveFunction, self).__init__(json_struct)

