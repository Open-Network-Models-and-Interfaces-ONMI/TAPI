from objects_common.jsonObject import JsonObject
from nameAndValue import NameAndValue
from objects_common.arrayType import ArrayType

class GlobalClass(JsonObject):

    def __init__(self, json_struct=None):
        self.uuid=""
        self.name=ArrayType.factory(NameAndValue)
        self.label=ArrayType.factory(NameAndValue)
        super(GlobalClass, self).__init__(json_struct)

