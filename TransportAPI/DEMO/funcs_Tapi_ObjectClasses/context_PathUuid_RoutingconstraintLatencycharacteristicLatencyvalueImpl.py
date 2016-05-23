import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathUuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def get(cls, uuid, latencyValue):
        print 'handling get'
        if uuid in Context._path:
            if latencyValue in Context._path[uuid]._routingConstraint.latencyCharacteristic:
                return Context._path[uuid]._routingConstraint.latencyCharacteristic[latencyValue]
            else:
                raise KeyError('latencyValue')
        else:
            raise KeyError('uuid')
