import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuid_ConnconstraintsCostcharacteristicCostalgorithmImpl:

    @classmethod
    def get(cls, uuid, costAlgorithm):
        print 'handling get'
        if uuid in Context._connectivityService:
            if costAlgorithm in Context._connectivityService[uuid]._connConstraints.costCharacteristic:
                return Context._connectivityService[uuid]._connConstraints.costCharacteristic[costAlgorithm]
            else:
                raise KeyError('costAlgorithm')
        else:
            raise KeyError('uuid')
