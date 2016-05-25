import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuid_ConnectionConnection_UuidImpl:

    @classmethod
    def get(cls, uuid, connection_uuid):
        print 'handling get'
        if uuid in Context._connectivityService:
            if connection_uuid in Context._connectivityService[uuid]._connection:
                return Context._connectivityService[uuid]._connection[connection_uuid]
            else:
                raise KeyError('connection_uuid')
        else:
            raise KeyError('uuid')
