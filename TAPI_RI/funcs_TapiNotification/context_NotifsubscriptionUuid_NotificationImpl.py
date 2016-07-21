import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NotifsubscriptionUuid_NotificationImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._notifSubscription:
            return be.Context._notifSubscription[uuid]._notification
        else:
            raise KeyError('uuid')
