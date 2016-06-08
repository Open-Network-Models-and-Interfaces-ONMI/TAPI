from objects_common.jsonObject import JsonObject
from validationMechanism import ValidationMechanism
from objects_common.arrayType import ArrayType

class ValidationPac(JsonObject):

    def __init__(self, json_struct=None):
        self.validationMechanism=ArrayType.factory(ValidationMechanism)
        super(ValidationPac, self).__init__(json_struct)

