import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotifsubscriptionUuid_SubscriptionfilterImpl:

    @classmethod
    def put(cls, uuid, subscriptionfilter):
        print str(subscriptionfilter)
        print 'handling put'
        Context._notifSubscription[uuid] = subscriptionfilter

    @classmethod
    def post(cls, uuid, subscriptionfilter):
        print str(subscriptionfilter)
        print 'handling post'
        Context._notifSubscription[uuid] = subscriptionfilter

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in Context._notifSubscription:
            del Context._notifSubscription[uuid]._subscriptionFilter
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._notifSubscription:
            return Context._notifSubscription[uuid]._subscriptionFilter
        else:
            raise KeyError('uuid')
