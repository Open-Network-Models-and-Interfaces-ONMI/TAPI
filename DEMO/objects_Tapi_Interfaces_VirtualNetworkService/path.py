from connectivityConstraint import ConnectivityConstraint
from teLink import TeLink
from pathObjectiveFunction import PathObjectiveFunction
from pathOptimizationConstraint import PathOptimizationConstraint
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class Path(GlobalClass):

    def __init__(self, json_struct=None):
        self._routingConstraint=ConnectivityConstraint() #import
        self._telink=ArrayType.factory(TeLink)
        self._objectiveFunction=PathObjectiveFunction() #import
        self._optimizationConstraint=PathOptimizationConstraint() #import
        super(Path, self).__init__(json_struct)

