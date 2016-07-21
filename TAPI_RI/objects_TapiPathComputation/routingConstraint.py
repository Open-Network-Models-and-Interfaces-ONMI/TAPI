from teLink import TeLink
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from latencyCharacteristic import LatencyCharacteristic
from localClass import LocalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class RoutingConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.pathLayer=ArrayType.factory(str)
        self._excludePath=KeyedArrayType(TeLink, 'localId')
        self._includePath=KeyedArrayType(TeLink, 'localId')
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costName')
        self._avoidTopology=ArrayType.factory(str)
        self.latencyCharacteristic=KeyedArrayType(LatencyCharacteristic, 'trafficPropertyName')
        self.serviceLevel=""
        self._includeTopology=ArrayType.factory(str)
        super(RoutingConstraint, self).__init__(json_struct)

