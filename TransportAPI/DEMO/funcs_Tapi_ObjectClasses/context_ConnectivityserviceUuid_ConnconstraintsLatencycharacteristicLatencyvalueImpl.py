import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ConnectivityserviceUuid_ConnconstraintsLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def get(cls, uuid, latencyValue):
        print 'handling get'
        if uuid in Context._connectivityService:
            if latencyValue in Context._connectivityService[uuid]._connConstraints.latencyCharacteristic:
                return Context._connectivityService[uuid]._connConstraints.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')
