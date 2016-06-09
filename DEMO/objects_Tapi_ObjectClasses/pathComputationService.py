from connectivityConstraint import ConnectivityConstraint
from pathCompServicePort import PathCompServicePort
from pathObjectiveFunction import PathObjectiveFunction
from pathOptimizationConstraint import PathOptimizationConstraint
from path import Path
from globalClass import GlobalClass
from objects_common.keyedArrayType import KeyedArrayType

class PathComputationService(GlobalClass):

    def __init__(self, json_struct=None):
        self._routingConstraint=ConnectivityConstraint() #import
        self._servicePort=KeyedArrayType(PathCompServicePort, 'localId')
        self._objectiveFunction=PathObjectiveFunction() #import
        self._optimizationConstraint=PathOptimizationConstraint() #import
        self._path=KeyedArrayType(Path, 'uuid')
        super(PathComputationService, self).__init__(json_struct)

