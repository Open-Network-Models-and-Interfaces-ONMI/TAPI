from objects_common.jsonObject import JsonObject
from objects_common.arrayType import ArrayType

class SubscriptionFilter(JsonObject):

    def __init__(self, json_struct=None):
        self.requestedObjectTypes=ArrayType.factory(str)
        self.requestedLayerProtocols=ArrayType.factory(str)
        self.requestedObjectIdentifier=ArrayType.factory(str)
        self.requestedNotificationTypes=ArrayType.factory(str)
        self.includeContent=False
        super(SubscriptionFilter, self).__init__(json_struct)

