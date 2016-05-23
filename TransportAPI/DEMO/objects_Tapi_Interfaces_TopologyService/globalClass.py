from objects_common.jsonObject import JsonObject
from nameAndValue import NameAndValue
from objects_common.keyedArrayType import KeyedArrayType

class GlobalClass(JsonObject):

    def __init__(self, json_struct=None):
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        self.uuid=""
        self.extension=KeyedArrayType(NameAndValue, 'valueName')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        super(GlobalClass, self).__init__(json_struct)

