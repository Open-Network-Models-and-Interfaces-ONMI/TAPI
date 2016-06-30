import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectivityserviceUuid_ConnconstraintLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def get(cls, uuid, latencyValue):
        print 'handling get'
        if uuid in be.Context._connectivityService:
            if latencyValue in be.Context._connectivityService[uuid]._connConstraint.latencyCharacteristic:
                return be.Context._connectivityService[uuid]._connConstraint.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')
