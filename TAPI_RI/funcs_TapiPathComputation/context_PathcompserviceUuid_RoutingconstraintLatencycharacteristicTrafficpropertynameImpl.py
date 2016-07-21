import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_RoutingconstraintLatencycharacteristicTrafficpropertynameImpl:

    @classmethod
    def get(cls, uuid, trafficPropertyName):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if trafficPropertyName in be.Context._pathCompService[uuid]._routingConstraint.latencyCharacteristic:
                return be.Context._pathCompService[uuid]._routingConstraint.latencyCharacteristic[trafficPropertyName]
            else:
                raise KeyError('trafficPropertyName')
        else:
            raise KeyError('uuid')
