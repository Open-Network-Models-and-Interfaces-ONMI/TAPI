import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectionUuid_ConnectionportLocalid_Connectionendpoint_ExtensionsImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._connection:
            if localId in be.Context._connection[uuid]._connectionPort:
                return be.Context._connection[uuid]._connectionPort[localId]._connectionEndPoint._extensions
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
