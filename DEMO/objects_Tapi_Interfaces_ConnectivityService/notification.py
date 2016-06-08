from objects_common.jsonObject import JsonObject
from nameAndValueChange import NameAndValueChange
from nameAndValue import NameAndValue
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType

class Notification(JsonObject):

    def __init__(self, json_struct=None):
        self.targetObjectIdentifier=""
        self.layerProtocolName=""
        self.changedAttributes=ArrayType.factory(NameAndValueChange)
        self.additionalInfo=KeyedArrayType(NameAndValue, 'valueName')
        self.additionalText=""
        self.notificationType=""
        self.targetObjectType=""
        self.sourceIndicator=""
        self.eventTimeStamp=""
        self.targetObjectName=KeyedArrayType(NameAndValue, 'valueName')
        self.notificationId=""
        super(Notification, self).__init__(json_struct)

