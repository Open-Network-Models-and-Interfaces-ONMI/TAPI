from objects_common.jsonObject import JsonObject
from latencyCharacteristic import LatencyCharacteristic
from objects_common.keyedArrayType import KeyedArrayType

class TransferTimingPac(JsonObject):

    def __init__(self, json_struct=None):
        self.latencyCharacteristic=KeyedArrayType(LatencyCharacteristic, 'trafficPropertyName')
        super(TransferTimingPac, self).__init__(json_struct)

