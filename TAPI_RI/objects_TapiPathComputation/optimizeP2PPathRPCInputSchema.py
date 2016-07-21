from objects_common.jsonObject import JsonObject
from pathOptimizationConstraint import PathOptimizationConstraint
from routingConstraint import RoutingConstraint
from pathObjectiveFunction import PathObjectiveFunction

class OptimizeP2PPathRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.pathIdOrName=""
        self.optimizationConstraint=PathOptimizationConstraint() #import
        self.routingConstraint=RoutingConstraint() #import
        self.objectiveFunction=PathObjectiveFunction() #import
        super(OptimizeP2PPathRPCInputSchema, self).__init__(json_struct)

