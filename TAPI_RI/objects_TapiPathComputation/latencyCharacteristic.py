from objects_common.jsonObject import JsonObject

class LatencyCharacteristic(JsonObject):

    def __init__(self, json_struct=None):
        self.trafficPropertyQueingLatency=""
        self.wanderCharacteristic=""
        self.fixedLatencyCharacteristic=""
        self.trafficPropertyName=""
        self.jitterCharacteristic=""
        super(LatencyCharacteristic, self).__init__(json_struct)

