from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class LtpSpec(JsonObject):

    def __init__(self, json_struct=None):
        self.ltpSpecReference=""
        self.lpSpecReference=ArrayType.factory(str)
        super(LtpSpec, self).__init__(json_struct)

