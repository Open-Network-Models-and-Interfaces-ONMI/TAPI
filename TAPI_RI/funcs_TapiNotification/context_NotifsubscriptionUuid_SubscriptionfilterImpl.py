import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_NotifsubscriptionUuid_SubscriptionfilterImpl:

    @classmethod
    def put(cls, uuid, subscriptionfilter):
        print str(subscriptionfilter)
        print 'handling put'
        be.Context._notifSubscription[uuid] = subscriptionfilter

    @classmethod
    def post(cls, uuid, subscriptionfilter):
        print str(subscriptionfilter)
        print 'handling post'
        be.Context._notifSubscription[uuid] = subscriptionfilter

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._notifSubscription:
            del be.Context._notifSubscription[uuid]._subscriptionFilter
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._notifSubscription:
            return be.Context._notifSubscription[uuid]._subscriptionFilter
        else:
            raise KeyError('uuid')
