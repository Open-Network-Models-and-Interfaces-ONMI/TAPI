import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_VnwserviceUuid_VnwconstraintLocalidLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def put(cls, uuid, localId, latencyValue, queuinglatency):
        print str(queuinglatency)
        print 'handling put'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic[latencyValue] = queuinglatency
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('localId')

    @classmethod
    def post(cls, uuid, localId, latencyValue, queuinglatency):
        print str(queuinglatency)
        print 'handling post'
        if uuid in Context._vnwService:
            if localId in Context._vnwService[uuid]._vnwConstraint:
                be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic[latencyValue] = queuinglatency
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('localId')

    @classmethod
    def delete(cls, uuid, localId, latencyValue):
        print 'handling delete'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if latencyValue in be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic:
                    del be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic[latencyValue]
                else:
                    raise KeyError('latencyValue')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')

    @classmethod
    def get(cls, uuid, localId, latencyValue):
        print 'handling get'
        if uuid in be.Context._vnwService:
            if localId in be.Context._vnwService[uuid]._vnwConstraint:
                if latencyValue in be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic:
                    return be.Context._vnwService[uuid]._vnwConstraint[localId].latencyCharacteristic[latencyValue]
                else:
                    raise KeyError('latencyValue')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
