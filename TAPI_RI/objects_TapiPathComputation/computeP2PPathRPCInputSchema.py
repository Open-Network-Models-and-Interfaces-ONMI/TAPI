from objects_common.jsonObject import JsonObject
from pathObjectiveFunction import PathObjectiveFunction
from routingConstraint import RoutingConstraint
from pathCompServicePort import PathCompServicePort
from objects_common.arrayType import ArrayType

class ComputeP2PPathRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.objectiveFunction=PathObjectiveFunction() #import
        self.routingConstraint=RoutingConstraint() #import
        self.servicePort=ArrayType.factory(PathCompServicePort)
        super(ComputeP2PPathRPCInputSchema, self).__init__(json_struct)

