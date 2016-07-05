from objects_common.jsonObject import JsonObject

class TimeRange(JsonObject):

    def __init__(self, json_struct=None):
        self.endTime=""
        self.startTime=""
        super(TimeRange, self).__init__(json_struct)

