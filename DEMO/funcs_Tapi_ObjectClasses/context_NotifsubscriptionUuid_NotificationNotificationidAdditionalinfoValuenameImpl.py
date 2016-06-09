import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotifsubscriptionUuid_NotificationNotificationidAdditionalinfoValuenameImpl:

    @classmethod
    def get(cls, uuid, notificationId, valueName):
        print 'handling get'
        if uuid in Context._notifSubscription:
            if notificationId in Context._notifSubscription[uuid]._notification:
                if valueName in Context._notifSubscription[uuid]._notification[notificationId].additionalInfo:
                    return Context._notifSubscription[uuid]._notification[notificationId].additionalInfo[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('notificationId')
        else:
            raise KeyError('uuid')
