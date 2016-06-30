from objects_common.jsonObject import JsonObject

class ValidationMechanism(JsonObject):

    def __init__(self, json_struct=None):
        self.layerProtocolAdjacencyValidated=""
        self.validationMechanism=""
        self.validationRobustness=""
        super(ValidationMechanism, self).__init__(json_struct)

