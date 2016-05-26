from objects_common.jsonObject import JsonObject

class ScheduleInfo(JsonObject):

    def __init__(self, json_struct=None):
        self.endTime=""
        self.startTime=""
        super(ScheduleInfo, self).__init__(json_struct)

