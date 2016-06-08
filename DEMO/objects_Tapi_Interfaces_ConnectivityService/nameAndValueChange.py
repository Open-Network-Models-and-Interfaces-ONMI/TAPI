from objects_common.jsonObject import JsonObject

class NameAndValueChange(JsonObject):

    def __init__(self, json_struct=None):
        self.newValue=""
        self.oldValue=""
        self.valueName=""
        super(NameAndValueChange, self).__init__(json_struct)

