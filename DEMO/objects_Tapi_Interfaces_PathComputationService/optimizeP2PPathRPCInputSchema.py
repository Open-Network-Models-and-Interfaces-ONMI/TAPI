from objects_common.jsonObject import JsonObject
from pathOptimizationConstraint import PathOptimizationConstraint
from connectivityConstraint import ConnectivityConstraint
from pathObjectiveFunction import PathObjectiveFunction

class OptimizeP2PPathRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.pathIdOrName=""
        self.optimizationConstraint=PathOptimizationConstraint() #import
        self.routingConstraint=ConnectivityConstraint() #import
        self.objectiveFunction=PathObjectiveFunction() #import
        super(OptimizeP2PPathRPCInputSchema, self).__init__(json_struct)

