import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuidImpl:

    @classmethod
    def put(cls, uuid, connectivityservice):
        print str(connectivityservice)
        print 'handling put'
        Context._connectivityService[uuid] = connectivityservice

    @classmethod
    def post(cls, uuid, connectivityservice):
        print str(connectivityservice)
        print 'handling post'
        Context._connectivityService[uuid] = connectivityservice

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in Context._connectivityService:
            del Context._connectivityService[uuid]
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._connectivityService:
            return Context._connectivityService[uuid]
        else:
            raise KeyError('uuid')
