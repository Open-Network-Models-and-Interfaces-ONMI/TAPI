import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ConnconstraintCostcharacteristicCostnameImpl:

    @classmethod
    def get(cls, uuid, costName):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if costName in be.Context._connectivityService[uuid]._connConstraint.costCharacteristic:
                return be.Context._connectivityService[uuid]._connConstraint.costCharacteristic[costName]
            else:
                raise KeyError('costName')
        else:
            raise KeyError('uuid')
