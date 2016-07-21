from notification import Notification
from subscriptionFilter import SubscriptionFilter
from extensionsSpec import ExtensionsSpec
from nameAndValue import NameAndValue
from serviceSpec import ServiceSpec
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class _notifSubscriptionSchema(ServiceSpec):

    def __init__(self, json_struct=None):
        self.uuid=""
        self._notification=KeyedArrayType(Notification, 'uuid')
        self._subscriptionFilter=SubscriptionFilter() #import
        self.subscriptionState=Subscriptionstate(0)
        self._extensions=KeyedArrayType(ExtensionsSpec, 'extensionsSpecification')
        self.label=KeyedArrayType(NameAndValue, 'valueName')
        self.supportedNotificationTypes=ArrayType.factory(str)
        self.supportedObjectTypes=ArrayType.factory(str)
        self.name=KeyedArrayType(NameAndValue, 'valueName')
        super(_notifSubscriptionSchema, self).__init__(json_struct)

class Subscriptionstate(EnumType):
    possible_values = ['SUSPENDED', 'ACTIVE']
    range_end = 2

    def __init__(self, initial_value):
        super(Subscriptionstate, self).__init__(initial_value)
