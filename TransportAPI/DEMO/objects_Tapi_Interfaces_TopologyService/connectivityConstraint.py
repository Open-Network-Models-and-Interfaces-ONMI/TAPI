from objects_common.jsonObject import JsonObject
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from riskCharacteristic import RiskCharacteristic
from queuingLatency import QueuingLatency
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class ConnectivityConstraint(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceType=""
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costAlgorithm')
        self.serviceLayer=ArrayType.factory(str)
        self.riskCharacteristic=KeyedArrayType(RiskCharacteristic, 'riskCharacteristicName')
        self.serviceLevel=""
        self.latencyCharacteristic=KeyedArrayType(QueuingLatency, 'latencyValue')
        self.excludePath=ArrayType.factory(str)
        self.avoidTopology=ArrayType.factory(str)
        self.includePath=ArrayType.factory(str)
        self.includeTopology=ArrayType.factory(str)
        super(ConnectivityConstraint, self).__init__(json_struct)

