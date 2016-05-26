from objects_common.jsonObject import JsonObject

class AdminStatePac(JsonObject):

    def __init__(self, json_struct=None):
        self.administrativeState=""
        self.operationalState=""
        self.lifecycleState=""
        super(AdminStatePac, self).__init__(json_struct)

