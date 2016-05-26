import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_ServiceportLocalidImpl:

    @classmethod
    def put(cls, uuid, localId, virtualnetworkserviceport):
        print str(virtualnetworkserviceport)
        print 'handling put'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._servicePort[localId] = virtualnetworkserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, virtualnetworkserviceport):
        print str(virtualnetworkserviceport)
        print 'handling post'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._servicePort[localId] = virtualnetworkserviceport
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId):
        print 'handling delete'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._servicePort:
                del Context._vnwService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._servicePort:
                return Context._vnwService[uuid]._servicePort[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
