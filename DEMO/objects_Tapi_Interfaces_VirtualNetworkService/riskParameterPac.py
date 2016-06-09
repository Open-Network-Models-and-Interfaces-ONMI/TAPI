from objects_common.jsonObject import JsonObject
from riskCharacteristic import RiskCharacteristic
from objects_common.keyedArrayType import KeyedArrayType

class RiskParameterPac(JsonObject):

    def __init__(self, json_struct=None):
        self.riskCharacteristic=KeyedArrayType(RiskCharacteristic, 'riskCharacteristicName')
        super(RiskParameterPac, self).__init__(json_struct)

