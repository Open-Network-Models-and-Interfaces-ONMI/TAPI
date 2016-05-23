from objects_common.jsonObject import JsonObject

class LifecycleStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.lifecycleState=""
        super(LifecycleStatePac, self).__init__(json_struct)

