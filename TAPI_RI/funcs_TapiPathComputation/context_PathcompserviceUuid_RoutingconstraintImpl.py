import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_RoutingconstraintImpl:

    @classmethod
    def put(cls, uuid, routingconstraint):
        print str(routingconstraint)
        print 'handling put'
        be.Context._pathCompService[uuid] = routingconstraint

    @classmethod
    def post(cls, uuid, routingconstraint):
        print str(routingconstraint)
        print 'handling post'
        be.Context._pathCompService[uuid] = routingconstraint

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._pathCompService:
            del be.Context._pathCompService[uuid]._routingConstraint
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            return be.Context._pathCompService[uuid]._routingConstraint
        else:
            raise KeyError('uuid')
