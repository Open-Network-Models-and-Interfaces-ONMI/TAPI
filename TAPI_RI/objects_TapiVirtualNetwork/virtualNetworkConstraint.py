from capacity import Capacity
from latencyCharacteristic import LatencyCharacteristic
from costCharacteristic import CostCharacteristic
from localClass import LocalClass
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class VirtualNetworkConstraint(LocalClass):

    def __init__(self, json_struct=None):
        self.requestedCapacity=Capacity() #import
        self.latencyCharacteristic=KeyedArrayType(LatencyCharacteristic, 'trafficPropertyName')
        self._srcServiceEndPoint=""
        self.serviceLevel=""
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costName')
        self.serviceLayer=ArrayType.factory(str)
        self._diversityExclusion=ArrayType.factory(str)
        self._sinkServiceEndPoint=""
        super(VirtualNetworkConstraint, self).__init__(json_struct)

