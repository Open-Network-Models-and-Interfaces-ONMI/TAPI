from capacity import Capacity
from costCharacteristic import CostCharacteristic
from queuingLatency import QueuingLatency
from riskCharacteristic import RiskCharacteristic
from localClass import LocalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class VirtualNetworkConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costAlgorithm')
        self._srcServiceEndPoint=""
        self._sinkServiceEndPoint=""
        self.serviceLevel=""
        self.serviceLayer=ArrayType.factory(str)
        self.latencyCharacteristic=KeyedArrayType(QueuingLatency, 'latencyValue')
        self.riskCharacteristic=KeyedArrayType(RiskCharacteristic, 'riskCharacteristicName')
        super(VirtualNetworkConstraint, self).__init__(json_struct)

