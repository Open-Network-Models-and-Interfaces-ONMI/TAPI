from objects_common.jsonObject import JsonObject

class CostCharacteristic(JsonObject):

    def __init__(self, json_struct=None):
        self.costName=""
        self.costAlgorithm=""
        self.costValue=""
        super(CostCharacteristic, self).__init__(json_struct)

