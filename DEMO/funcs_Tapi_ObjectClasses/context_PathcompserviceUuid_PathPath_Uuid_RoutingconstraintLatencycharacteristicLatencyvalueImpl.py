import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_PathPath_Uuid_RoutingconstraintLatencycharacteristicLatencyvalueImpl:

    @classmethod
    def get(cls, uuid, path_uuid, latencyValue):
        print 'handling get'
        if uuid in Context._pathCompService:
            if path_uuid in Context._pathCompService[uuid]._path:
                if latencyValue in Context._pathCompService[uuid]._path[path_uuid]._routingConstraint.latencyCharacteristic:
                    return Context._pathCompService[uuid]._path[path_uuid]._routingConstraint.latencyCharacteristic[latencyValue]
                else:
                    raise KeyError('latencyValue')
            else:
                raise KeyError('path_uuid')
        else:
            raise KeyError('uuid')
