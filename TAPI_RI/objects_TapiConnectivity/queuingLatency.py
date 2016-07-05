from objects_common.jsonObject import JsonObject

class QueuingLatency(JsonObject):

    def __init__(self, json_struct=None):
        self.latencyValue=""
        self.trafficPropertyName=""
        super(QueuingLatency, self).__init__(json_struct)

