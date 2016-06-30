import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_ScheduleImpl:

    @classmethod
    def put(cls, uuid, timerange):
        print str(timerange)
        print 'handling put'
        be.Context._vnwService[uuid] = timerange

    @classmethod
    def post(cls, uuid, timerange):
        print str(timerange)
        print 'handling post'
        be.Context._vnwService[uuid] = timerange

    @classmethod
    def delete(cls, uuid):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            del be.Context._vnwService[uuid]._schedule
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._vnwService:
            return be.Context._vnwService[uuid]._schedule
        else:
            raise KeyError('uuid')
