from objects_common.jsonObject import JsonObject
from queuingLatency import QueuingLatency
from objects_common.keyedArrayType import KeyedArrayType

class TransferTimingPac(JsonObject):

    def __init__(self, json_struct=None):
        self.queuingLatency=KeyedArrayType(QueuingLatency, 'latencyValue')
        self.wanderCharacteristic=""
        self.fixedLatencyCharacteristic=""
        self.jitterCharacteristic=""
        super(TransferTimingPac, self).__init__(json_struct)

