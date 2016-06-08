import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotifsubscriptionUuid_NotificationTargetobjectnameValuenameImpl:

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in Context._notifSubscription:
            if valueName in Context._notifSubscription[uuid]._notification.targetObjectName:
                return Context._notifSubscription[uuid]._notification.targetObjectName[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
