from objects_common.jsonObject import JsonObject
from queuingLatency import QueuingLatency
from objects_common.arrayType import ArrayType

class TransferTimingPac(JsonObject):

    def __init__(self, json_struct=None):
        self.queuingLatency=ArrayType.factory(QueuingLatency)
        self.wanderCharacteristic=""
        self.fixedLatencyCharacteristic=""
        self.jitterCharacteristic=""
        super(TransferTimingPac, self).__init__(json_struct)

