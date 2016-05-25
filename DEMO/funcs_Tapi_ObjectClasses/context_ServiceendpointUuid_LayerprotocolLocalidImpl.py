import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_ServiceendpointUuid_LayerprotocolLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in Context._serviceEndPoint:
            if localId in Context._serviceEndPoint[uuid]._layerProtocol:
                return Context._serviceEndPoint[uuid]._layerProtocol[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
