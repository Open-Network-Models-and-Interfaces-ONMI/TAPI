from objects_common.jsonObject import JsonObject

class OperationalStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.operationalState=""
        self.lifecycleState=""
        super(OperationalStatePac, self).__init__(json_struct)

