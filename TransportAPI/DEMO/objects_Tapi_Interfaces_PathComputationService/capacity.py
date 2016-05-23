from objects_common.jsonObject import JsonObject

class Capacity(JsonObject):

    def __init__(self, json_struct=None):
        self.totalSize=""
        self.maximumUsageInstances=""
        self.numberingRange=""
        self.maximumUsageSize=""
        super(Capacity, self).__init__(json_struct)

