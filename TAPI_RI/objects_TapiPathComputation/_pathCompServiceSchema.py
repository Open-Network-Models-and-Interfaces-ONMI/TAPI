from pathCompServicePort import PathCompServicePort
from routingConstraint import RoutingConstraint
from pathOptimizationConstraint import PathOptimizationConstraint
from nameAndValue import NameAndValue
from extensionsSpec import ExtensionsSpec
from pathObjectiveFunction import PathObjectiveFunction
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class _pathCompServiceSchema(ServiceSpec):

    def __init__(self, json_struct=None):
        self._servicePort=KeyedArrayType(PathCompServicePort, 'localId')
        self.uuid=""
        self._routingConstraint=RoutingConstraint() #import
        self._optimizationConstraint=PathOptimizationConstraint() #import
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self._path=ArrayType.factory(str)
        self._objectiveFunction=PathObjectiveFunction() #import
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_pathCompServiceSchema, self).__init__(json_struct)

