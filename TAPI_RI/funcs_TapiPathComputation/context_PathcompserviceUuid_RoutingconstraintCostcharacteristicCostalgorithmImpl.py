import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathcompserviceUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, costAlgorithm):
        print 'handling get'
        if uuid in be.Context._pathCompService:
            if costAlgorithm in be.Context._pathCompService[uuid]._routingConstraint.costCharacteristic:
                return be.Context._pathCompService[uuid]._routingConstraint.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')
