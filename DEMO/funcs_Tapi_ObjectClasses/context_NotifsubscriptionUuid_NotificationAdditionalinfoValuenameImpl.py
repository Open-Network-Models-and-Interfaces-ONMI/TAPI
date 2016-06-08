import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotifsubscriptionUuid_NotificationAdditionalinfoValuenameImpl:

    @classmethod
    def get(cls, uuid, valueName):
        print 'handling get'
        if uuid in Context._notifSubscription:
            if valueName in Context._notifSubscription[uuid]._notification.additionalInfo:
                return Context._notifSubscription[uuid]._notification.additionalInfo[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('uuid')
