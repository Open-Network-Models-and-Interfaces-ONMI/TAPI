from objects_common.jsonObject import JsonObject

class LocalClass(JsonObject):

    def __init__(self, json_struct=None):
        self.localId=""
        super(LocalClass, self).__init__(json_struct)

