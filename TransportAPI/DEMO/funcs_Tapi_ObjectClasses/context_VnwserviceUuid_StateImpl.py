import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_StateImpl:

    @classmethod
    def put(cls, uuid, adminstatepac):
        print str(adminstatepac)
        print 'handling put'
        Context._vnwService[uuid] = adminstatepac

    @classmethod
    def post(cls, uuid, adminstatepac):
        print str(adminstatepac)
        print 'handling post'
        Context._vnwService[uuid] = adminstatepac

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in Context._vnwService:
            del Context._vnwService[uuid]._state
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._vnwService:
            return Context._vnwService[uuid]._state
        else:
            raise KeyError('uuid')
