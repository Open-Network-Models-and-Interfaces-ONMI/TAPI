import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuid_ConnectionConnection_Uuid_ConnectionportLocalidImpl:

    @classmethod
    def get(cls, uuid, connection_uuid, localId):
        print 'handling get'
        if uuid in Context._connectivityService:
            if connection_uuid in Context._connectivityService[uuid]._connection:
                if localId in Context._connectivityService[uuid]._connection[connection_uuid]._connectionPort:
                    return Context._connectivityService[uuid]._connection[connection_uuid]._connectionPort[localId]
                else:
                    raise KeyError('localId')
            else:
                raise KeyError('connection_uuid')
        else:
            raise KeyError('uuid')
