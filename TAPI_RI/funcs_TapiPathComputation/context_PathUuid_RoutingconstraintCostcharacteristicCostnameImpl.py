import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathUuid_RoutingconstraintCostcharacteristicCostnameImpl:

    @classmethod
    def get(cls, uuid, costName):
        print 'handling get'
        if uuid in be.Context._path:
            if costName in be.Context._path[uuid]._routingConstraint.costCharacteristic:
                return be.Context._path[uuid]._routingConstraint.costCharacteristic[costName]
            else:
                raise KeyError('costName')
        else:
            raise KeyError('uuid')
