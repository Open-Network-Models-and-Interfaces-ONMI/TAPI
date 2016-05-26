import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathUuid_RoutingconstraintCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, costAlgorithm):
        print 'handling get'
        if uuid in Context._path:
            if costAlgorithm in Context._path[uuid]._routingConstraint.costCharacteristic:
                return Context._path[uuid]._routingConstraint.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')
