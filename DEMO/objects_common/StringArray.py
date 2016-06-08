from objects_common.jsonObject import JsonObject

class StringArray(JsonObject):

    def __init__(self, json_struct=None):
        self.array=[]
        super(StringArray, self).__init__(json_struct)

