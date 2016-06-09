import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotifsubscriptionUuid_NotificationNotificationidChangedattributesImpl:

    @classmethod
    def get(cls, uuid, notificationId):
        print 'handling get'
        if uuid in Context._notifSubscription:
            if notificationId in Context._notifSubscription[uuid]._notification:
                return Context._notifSubscription[uuid]._notification[notificationId].changedAttributes
            else:
                raise KeyError('notificationId')
        else:
            raise KeyError('uuid')
