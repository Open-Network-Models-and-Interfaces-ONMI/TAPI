import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ConnconstraintImpl:

    @classmethod
    def put(cls, uuid, connectivityconstraint):
        print str(connectivityconstraint)
        print 'handling put'
        be.Context._connectivityService[uuid] = connectivityconstraint

    @classmethod
    def post(cls, uuid, connectivityconstraint):
        print str(connectivityconstraint)
        print 'handling post'
        be.Context._connectivityService[uuid] = connectivityconstraint

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._connectivityService:
            del be.Context._connectivityService[uuid]._connConstraint
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            return be.Context._connectivityService[uuid]._connConstraint
        else:
            raise KeyError('uuid')
