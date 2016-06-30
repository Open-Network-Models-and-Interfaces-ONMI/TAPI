import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectionUuid_RouteLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._connection:
            if localId in be.Context._connection[uuid]._route:
                return be.Context._connection[uuid]._route[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
