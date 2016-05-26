from objects_common.jsonObject import JsonObject

class TransferIntegrityPac(JsonObject):

    def __init__(self, json_struct=None):
        self.errorCharacteristic=""
        self.repeatDeliveryCharacteristic=""
        self.lossCharacteristic=""
        self.unavailableTimeCharacteristic=""
        self.deliveryOrderCharacteristic=""
        self.serverIntegrityProcessCharacteristic=""
        super(TransferIntegrityPac, self).__init__(json_struct)

