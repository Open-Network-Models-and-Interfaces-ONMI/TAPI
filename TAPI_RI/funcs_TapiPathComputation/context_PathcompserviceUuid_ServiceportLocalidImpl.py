import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_ServiceportLocalidImpl:

    @classmethod
    def put(cls, uuid, localId, pathcompserviceport):
        print str(pathcompserviceport)
        print 'handling put'
        if uuid in Context._pathCompService:
            be.Context._pathCompService[uuid]._servicePort[localId] = pathcompserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, pathcompserviceport):
        print str(pathcompserviceport)
        print 'handling post'
        if uuid in Context._pathCompService:
            be.Context._pathCompService[uuid]._servicePort[localId] = pathcompserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId):
        print 'handling delete'
        if uuid in be.Context._pathCompService:
            if localId in be.Context._pathCompService[uuid]._servicePort:
                del be.Context._pathCompService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if localId in be.Context._pathCompService[uuid]._servicePort:
                return be.Context._pathCompService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
