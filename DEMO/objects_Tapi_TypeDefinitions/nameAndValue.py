from objects_common.jsonObject import JsonObject

class NameAndValue(JsonObject):

    def __init__(self, json_struct=None):
        self.value=""
        self.valueName=""
        super(NameAndValue, self).__init__(json_struct)

