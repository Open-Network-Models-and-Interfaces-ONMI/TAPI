from teLink import TeLink
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from queuingLatency import QueuingLatency
from riskCharacteristic import RiskCharacteristic
from localClass import LocalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class RoutingConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.pathLayer=ArrayType.factory(str)
        self._excludePath=KeyedArrayType(TeLink, 'localId')
        self._includePath=KeyedArrayType(TeLink, 'localId')
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costAlgorithm')
        self._avoidTopology=ArrayType.factory(str)
        self.latencyCharacteristic=KeyedArrayType(QueuingLatency, 'latencyValue')
        self.serviceLevel=""
        self._includeTopology=ArrayType.factory(str)
        self.riskCharacteristic=KeyedArrayType(RiskCharacteristic, 'riskCharacteristicName')
        super(RoutingConstraint, self).__init__(json_struct)

