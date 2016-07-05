import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def get(cls, uuid, latencyValue):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if latencyValue in be.Context._pathCompService[uuid]._routingConstraint.latencyCharacteristic:
                return be.Context._pathCompService[uuid]._routingConstraint.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')
