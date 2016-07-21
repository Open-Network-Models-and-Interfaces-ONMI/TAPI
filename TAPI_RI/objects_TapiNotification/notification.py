from nameAndValue import NameAndValue
from nameAndValueChange import NameAndValueChange
from resourceSpec import ResourceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class Notification(ResourceSpec):

    def __init__(self, json_struct=None):
        self.additionalInfo=KeyedArrayType(NameAndValue, 'valueName')
        self.layerProtocolName=Layerprotocolname(0)
        self.changedAttributes=ArrayType.factory(NameAndValueChange)
        self.sequenceNumber=""
        self.targetObjectIdentifier=""
        self.additionalText=""
        self.notificationType=Notificationtype(0)
        self.targetObjectType=Targetobjecttype(0)
        self.sourceIndicator=Sourceindicator(0)
        self.eventTimeStamp=""
        self.targetObjectName=KeyedArrayType(NameAndValue, 'valueName')
        super(Notification, self).__init__(json_struct)

class Layerprotocolname(EnumType):
    possible_values = ['OCH', 'ODU', 'ETH', 'MPLS_TP']
    range_end = 4

    def __init__(self, initial_value):
        super(Layerprotocolname, self).__init__(initial_value)
class Notificationtype(EnumType):
    possible_values = ['OBJECT_CREATION', 'OBJECT_DELETION', 'ATTRIBUTE_VALUE_CHANGE']
    range_end = 3

    def __init__(self, initial_value):
        super(Notificationtype, self).__init__(initial_value)
class Targetobjecttype(EnumType):
    possible_values = ['TOPOLOGY', 'NODE', 'LINK', 'CONNECTION', 'PATH', 'CONNECTIVITY_SERVICE', 'VIRTUAL_NETWORK_SERVICE', 'PATH_COMPUTATION_SERVICE', 'NODE_EDGE_POINT', 'SERVICE_END_POINT', 'CONNECTION_END_POINT']
    range_end = 11

    def __init__(self, initial_value):
        super(Targetobjecttype, self).__init__(initial_value)
class Sourceindicator(EnumType):
    possible_values = ['RESOURCE_OPERATION', 'MANAGEMENT_OPERATION', 'UNKNOWN']
    range_end = 3

    def __init__(self, initial_value):
        super(Sourceindicator, self).__init__(initial_value)
