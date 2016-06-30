from objects_common.jsonObject import JsonObject
from extensionsSpec import ExtensionsSpec
from objects_common.keyedArrayType import KeyedArrayType

class LocalClass(JsonObject):

    def __init__(self, json_struct=None):
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.localId=""
        super(LocalClass, self).__init__(json_struct)

