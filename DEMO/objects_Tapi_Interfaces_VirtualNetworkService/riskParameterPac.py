from objects_common.jsonObject import JsonObject
from riskCharacteristic import RiskCharacteristic
from objects_common.arrayType import ArrayType

class RiskParameterPac(JsonObject):

    def __init__(self, json_struct=None):
        self.riskCharacteristic=ArrayType.factory(RiskCharacteristic)
        super(RiskParameterPac, self).__init__(json_struct)

