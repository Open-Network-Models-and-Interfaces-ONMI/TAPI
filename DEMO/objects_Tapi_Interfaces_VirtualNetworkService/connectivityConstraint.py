from objects_common.jsonObject import JsonObject
from capacity import Capacity
from costCharacteristic import CostCharacteristic
from queuingLatency import QueuingLatency
from riskCharacteristic import RiskCharacteristic
from objects_common.arrayType import ArrayType

class ConnectivityConstraint(JsonObject):

    def __init__(self, json_struct=None):
        self.serviceType=""
        self.requestedCapacity=Capacity() #import
        self.costCharacteristic=ArrayType.factory(CostCharacteristic)
        self.latencyCharacteristic=ArrayType.factory(QueuingLatency)
        self.includeTopology=ArrayType.factory(str)
        self.serviceLevel=""
        self.serviceLayer=ArrayType.factory(str)
        self.excludePath=ArrayType.factory(str)
        self.avoidTopology=ArrayType.factory(str)
        self.includePath=ArrayType.factory(str)
        self.riskCharacteristic=ArrayType.factory(RiskCharacteristic)
        super(ConnectivityConstraint, self).__init__(json_struct)

