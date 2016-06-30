from subscriptionFilter import SubscriptionFilter
from notification import Notification
from service import Service
from objects_common.arrayType import ArrayType
from objects_common.keyedArrayType import KeyedArrayType
from objects_common.enumType import EnumType

class NotificationSubscriptionService(Service):

    def __init__(self, json_struct=None):
        self._subscriptionFilter=SubscriptionFilter() #import
        self.supportedObjectTypes=ArrayType.factory(str)
        self.subscriptionState=Subscriptionstate(0)
        self.supportedNotificationTypes=ArrayType.factory(str)
        self._notification=KeyedArrayType(Notification, 'uuid')
        super(NotificationSubscriptionService, self).__init__(json_struct)

class Subscriptionstate(EnumType):
    possible_values = ['SUSPENDED', 'ACTIVE']
    range_end = 2

    def __init__(self, initial_value):
        super(Subscriptionstate, self).__init__(initial_value)
