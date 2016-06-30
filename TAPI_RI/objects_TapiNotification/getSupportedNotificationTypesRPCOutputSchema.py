from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class GetSupportedNotificationTypesRPCOutputSchema(JsonObject):

    def __init__(self, json_struct=None):
        self.supportedObjectTypes=ArrayType.factory(str)
        self.supportedNotificationTypes=ArrayType.factory(str)
        super(GetSupportedNotificationTypesRPCOutputSchema, self).__init__(json_struct)

