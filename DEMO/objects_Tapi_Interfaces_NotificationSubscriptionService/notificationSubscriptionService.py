from subscriptionFilter import SubscriptionFilter
from objects_Tapi_ObjectClasses.notification import Notification
from globalClass import GlobalClass
from objects_common.arrayType import ArrayType

class NotificationSubscriptionService(GlobalClass):

    def __init__(self, json_struct=None):
        self._subscriptionFilter=SubscriptionFilter() #import
        self.supportedObjectTypes=ArrayType.factory(str)
        self._notification=ArrayType.factory(Notification)
        self.supportedNotificationTypes=ArrayType.factory(str)
        self.subscriptionState=""
        super(NotificationSubscriptionService, self).__init__(json_struct)

