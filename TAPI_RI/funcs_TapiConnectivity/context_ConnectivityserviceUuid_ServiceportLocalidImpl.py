import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ServiceportLocalidImpl:

    @classmethod
    def put(cls, uuid, localId, connectivityserviceport):
        print str(connectivityserviceport)
        print 'handling put'
        if uuid in Context._connectivityService:
            be.Context._connectivityService[uuid]._servicePort[localId] = connectivityserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, connectivityserviceport):
        print str(connectivityserviceport)
        print 'handling post'
        if uuid in Context._connectivityService:
            be.Context._connectivityService[uuid]._servicePort[localId] = connectivityserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId):
        print 'handling delete'
        if uuid in be.Context._connectivityService:
            if localId in be.Context._connectivityService[uuid]._servicePort:
                del be.Context._connectivityService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if localId in be.Context._connectivityService[uuid]._servicePort:
                return be.Context._connectivityService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
