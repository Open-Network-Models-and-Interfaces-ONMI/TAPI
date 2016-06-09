import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_ServiceportLocalidImpl:

    @classmethod
    def put(cls, uuid, localId, pathcompserviceport):
        print str(pathcompserviceport)
        print 'handling put'
        if uuid in Context._pathCompService:
            Context._pathCompService[uuid]._servicePort[localId] = pathcompserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, pathcompserviceport):
        print str(pathcompserviceport)
        print 'handling post'
        if uuid in Context._pathCompService:
            Context._pathCompService[uuid]._servicePort[localId] = pathcompserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId):
        print 'handling delete'
        if uuid in Context._pathCompService:
            if localId in Context._pathCompService[uuid]._servicePort:
                del Context._pathCompService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in Context._pathCompService:
            if localId in Context._pathCompService[uuid]._servicePort:
                return Context._pathCompService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
