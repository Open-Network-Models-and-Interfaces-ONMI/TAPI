from objects_common.jsonObject import JsonObject
from pathObjectiveFunction import PathObjectiveFunction
from connectivityConstraint import ConnectivityConstraint
from connectivityServicePort import ConnectivityServicePort
from objects_common.arrayType import ArrayType

class ComputeP2PPathRPCInputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.objectiveFunction=PathObjectiveFunction() #import
        self.routingConstraint=ConnectivityConstraint() #import
        self.servicePort=ArrayType.factory(ConnectivityServicePort)
        super(ComputeP2PPathRPCInputSchema, self).__init__(json_struct)

