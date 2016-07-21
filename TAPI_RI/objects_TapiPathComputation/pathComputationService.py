from routingConstraint import RoutingConstraint
from pathCompServicePort import PathCompServicePort
from pathObjectiveFunction import PathObjectiveFunction
from pathOptimizationConstraint import PathOptimizationConstraint
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class PathComputationService(ServiceSpec):

    def __init__(self, json_struct=None):
        self._routingConstraint=RoutingConstraint() #import
        self._servicePort=KeyedArrayType(PathCompServicePort, 'localId')
        self._objectiveFunction=PathObjectiveFunction() #import
        self._optimizationConstraint=PathOptimizationConstraint() #import
        self._path=ArrayType.factory(str)
        super(PathComputationService, self).__init__(json_struct)

