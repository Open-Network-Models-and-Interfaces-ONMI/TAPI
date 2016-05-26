import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathUuid_RoutingconstraintImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._path:
            return Context._path[uuid]._routingConstraint
        else:
            raise KeyError('uuid')
