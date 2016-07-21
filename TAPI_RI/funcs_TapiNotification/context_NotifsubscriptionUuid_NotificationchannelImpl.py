import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NotifsubscriptionUuid_NotificationchannelImpl:

    @classmethod
    def put(cls, uuid, notificationchannel):
        print str(notificationchannel)
        print 'handling put'
        be.Context._notifSubscription[uuid] = notificationchannel

    @classmethod
    def post(cls, uuid, notificationchannel):
        print str(notificationchannel)
        print 'handling post'
        be.Context._notifSubscription[uuid] = notificationchannel

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._notifSubscription:
            del be.Context._notifSubscription[uuid]._notificationChannel
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._notifSubscription:
            return be.Context._notifSubscription[uuid]._notificationChannel
        else:
            raise KeyError('uuid')
