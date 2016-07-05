import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_StateImpl:

    @classmethod
    def put(cls, uuid, adminstatepac):
        print str(adminstatepac)
        print 'handling put'
        be.Context._vnwService[uuid] = adminstatepac

    @classmethod
    def post(cls, uuid, adminstatepac):
        print str(adminstatepac)
        print 'handling post'
        be.Context._vnwService[uuid] = adminstatepac

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            del be.Context._vnwService[uuid]._state
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._vnwService:
            return be.Context._vnwService[uuid]._state
        else:
            raise KeyError('uuid')
