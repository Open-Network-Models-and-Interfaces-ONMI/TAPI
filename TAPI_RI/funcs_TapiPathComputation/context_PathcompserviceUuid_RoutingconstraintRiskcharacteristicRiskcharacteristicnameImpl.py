import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_RoutingconstraintRiskcharacteristicRiskcharacteristicnameImpl:

    @classmethod
    def get(cls, uuid, riskCharacteristicName):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if riskCharacteristicName in be.Context._pathCompService[uuid]._routingConstraint.riskCharacteristic:
                return be.Context._pathCompService[uuid]._routingConstraint.riskCharacteristic[riskCharacteristicName]
            else:
                raise KeyError('riskCharacteristicName')
        else:
            raise KeyError('uuid')
