from objects_common.jsonObject import JsonObject
from costCharacteristic import CostCharacteristic
from objects_common.keyedArrayType import KeyedArrayType

class TransferCostPac(JsonObject):

    def __init__(self, json_struct=None):
        self.costCharacteristic=KeyedArrayType(CostCharacteristic, 'costName')
        super(TransferCostPac, self).__init__(json_struct)

