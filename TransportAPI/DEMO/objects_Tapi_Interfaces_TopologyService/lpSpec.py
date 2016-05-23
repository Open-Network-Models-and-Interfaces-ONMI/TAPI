from objects_common.jsonObject import JsonObject

class LpSpec(JsonObject):

    def __init__(self, json_struct=None):
        self.lpSpecReference=""
        super(LpSpec, self).__init__(json_struct)

