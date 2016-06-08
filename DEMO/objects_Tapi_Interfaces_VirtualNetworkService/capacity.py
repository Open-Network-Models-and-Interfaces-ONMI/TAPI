from objects_common.jsonObject import JsonObject

class Capacity(JsonObject):

    def __init__(self, json_struct=None):
        self.maximumUsageSize=""
        self.totalSize=""
        self.numberingRange=""
        self.maximumUsageInstances=""
        super(Capacity, self).__init__(json_struct)

