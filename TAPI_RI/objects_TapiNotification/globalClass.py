from objects_common.jsonObject import JsonObject
from extensionsSpec import ExtensionsSpec
from nameAndValue import NameAndValue
from objects_common.keyedArrayType import KeyedArrayType

class GlobalClass(JsonObject):

    def __init__(self, json_struct=None):
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        self.uuid=""
        super(GlobalClass, self).__init__(json_struct)

