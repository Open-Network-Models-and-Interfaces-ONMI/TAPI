import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_VnwserviceUuid_VnwconstraintLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def put(cls, uuid, latencyValue, queuinglatency):
        print str(queuinglatency)
        print 'handling put'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic[latencyValue] = queuinglatency
        else:
            raise KeyError('latencyValue')

    @classmethod
    def post(cls, uuid, latencyValue, queuinglatency):
        print str(queuinglatency)
        print 'handling post'
        if uuid in Context._vnwService:
            Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic[latencyValue] = queuinglatency
        else:
            raise KeyError('latencyValue')

    @classmethod
    def delete(cls, uuid, latencyValue):
        print 'handling delete'
        if uuid in Context._vnwService:
            if latencyValue in Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic:
                del Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, latencyValue):
        print 'handling get'
        if uuid in Context._vnwService:
            if latencyValue in Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic:
                return Context._vnwService[uuid]._vnwConstraint.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')
