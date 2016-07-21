from objects_common.jsonObject import JsonObject
from validationMechanism import ValidationMechanism
from objects_common.keyedArrayType import KeyedArrayType

class ValidationPac(JsonObject):

    def __init__(self, json_struct=None):
        self.validationMechanism=KeyedArrayType(ValidationMechanism, 'validationMechanism')
        super(ValidationPac, self).__init__(json_struct)

