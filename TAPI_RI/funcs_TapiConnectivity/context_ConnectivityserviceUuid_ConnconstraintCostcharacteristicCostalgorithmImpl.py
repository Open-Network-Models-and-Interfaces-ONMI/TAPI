import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, costAlgorithm):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if costAlgorithm in be.Context._connectivityService[uuid]._connConstraint.costCharacteristic:
                return be.Context._connectivityService[uuid]._connConstraint.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')
