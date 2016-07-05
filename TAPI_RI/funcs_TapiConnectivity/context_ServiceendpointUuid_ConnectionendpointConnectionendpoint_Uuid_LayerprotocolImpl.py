import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ServiceendpointUuid_ConnectionendpointConnectionendpoint_Uuid_LayerprotocolImpl:

    @classmethod
    def get(cls, uuid, connectionEndPoint_uuid):
        print 'handling get'
        if uuid in be.Context._serviceEndPoint:
            if connectionEndPoint_uuid in be.Context._serviceEndPoint[uuid]._connectionEndPoint:
                return be.Context._serviceEndPoint[uuid]._connectionEndPoint[connectionEndPoint_uuid]._layerProtocol
            else:
                raise KeyError('connectionEndPoint_uuid')
        else:
            raise KeyError('uuid')
