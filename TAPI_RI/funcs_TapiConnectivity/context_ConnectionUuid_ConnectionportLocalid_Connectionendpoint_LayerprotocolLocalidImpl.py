import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_LayerprotocolLocalidImpl:

    @classmethod
    def get(cls, uuid, localId, localId2):
        print 'handling get'
        if uuid in be.Context._connection:
            if localId in be.Context._connection[uuid]._connectionPort:
                if localId in be.Context._connection[uuid]._connectionPort[localId]._connectionEndPoint._layerProtocol:
                    return be.Context._connection[uuid]._connectionPort[localId]._connectionEndPoint._layerProtocol[localId]
                else:
                    raise KeyError('localId')
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
