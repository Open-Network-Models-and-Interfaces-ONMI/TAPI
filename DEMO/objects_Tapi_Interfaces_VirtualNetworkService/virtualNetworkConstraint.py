from objects_common.jsonObject import JsonObject
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from queuingLatency import QueuingLatency
from riskCharacteristic import RiskCharacteristic
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class VirtualNetworkConstraint(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceType=""
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costAlgorithm')
        self.latencyCharacteristic=KeyedArrayType(QueuingLatency, 'latencyValue')
        self.serviceLevel=""
        self.serviceLayer=ArrayType.factory(str)
        self.riskCharacteristic=KeyedArrayType(RiskCharacteristic, 'riskCharacteristicName')
        super(VirtualNetworkConstraint, self).__init__(json_struct)

