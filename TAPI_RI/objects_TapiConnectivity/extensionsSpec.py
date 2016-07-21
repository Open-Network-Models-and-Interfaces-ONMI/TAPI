from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class ExtensionsSpec(JsonObject):

    def __init__(self, json_struct=None):
        self.extensionsSpecTarget=ArrayType.factory(str)
        self.extensionsSpecification=""
        super(ExtensionsSpec, self).__init__(json_struct)

