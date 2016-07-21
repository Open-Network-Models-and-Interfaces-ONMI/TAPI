import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NotifsubscriptionUuid_NotificationNotification_UuidTargetobjectnameValuenameImpl:

    @classmethod
    def get(cls, uuid, notification_uuid, valueName):
        print 'handling get'
        if uuid in be.Context._notifSubscription:
            if notification_uuid in be.Context._notifSubscription[uuid]._notification:
                if valueName in be.Context._notifSubscription[uuid]._notification[notification_uuid].targetObjectName:
                    return be.Context._notifSubscription[uuid]._notification[notification_uuid].targetObjectName[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('notification_uuid')
        else:
            raise KeyError('uuid')
