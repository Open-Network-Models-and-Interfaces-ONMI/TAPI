import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuid_ConnconstraintsImpl:

    @classmethod
    def put(cls, uuid, connectivityconstraint):
        print str(connectivityconstraint)
        print 'handling put'
        Context._connectivityService[uuid] = connectivityconstraint

    @classmethod
    def post(cls, uuid, connectivityconstraint):
        print str(connectivityconstraint)
        print 'handling post'
        Context._connectivityService[uuid] = connectivityconstraint

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in Context._connectivityService:
            del Context._connectivityService[uuid]._connConstraints
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._connectivityService:
            return Context._connectivityService[uuid]._connConstraints
        else:
            raise KeyError('uuid')
