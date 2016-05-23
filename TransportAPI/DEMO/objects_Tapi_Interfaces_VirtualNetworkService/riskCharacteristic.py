from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class RiskCharacteristic(JsonObject):

    def __init__(self, json_struct=None):
        self.riskIdentifierList=ArrayType.factory(str)
        self.riskCharacteristicName=""
        super(RiskCharacteristic, self).__init__(json_struct)

