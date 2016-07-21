import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NotifsubscriptionUuid_NotificationNotification_UuidAdditionalinfoImpl:

    @classmethod
    def get(cls, uuid, notification_uuid):
        print 'handling get'
        if uuid in be.Context._notifSubscription:
            if notification_uuid in be.Context._notifSubscription[uuid]._notification:
                return be.Context._notifSubscription[uuid]._notification[notification_uuid].additionalInfo
            else:
                raise KeyError('notification_uuid')
        else:
            raise KeyError('uuid')
