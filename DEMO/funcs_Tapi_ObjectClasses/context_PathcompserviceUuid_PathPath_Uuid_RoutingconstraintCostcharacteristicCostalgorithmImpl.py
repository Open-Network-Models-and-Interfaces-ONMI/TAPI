import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, path_uuid, costAlgorithm):
        print 'handling get'
        if uuid in Context._pathCompService:
            if path_uuid in Context._pathCompService[uuid]._path:
                if costAlgorithm in Context._pathCompService[uuid]._path[path_uuid]._routingConstraint.costCharacteristic:
                    return Context._pathCompService[uuid]._path[path_uuid]._routingConstraint.costCharacteristic[costAlgorithm]
                else:
                    raise KeyError('costAlgorithm')
            else:
                raise KeyError('path_uuid')
        else:
            raise KeyError('uuid')
