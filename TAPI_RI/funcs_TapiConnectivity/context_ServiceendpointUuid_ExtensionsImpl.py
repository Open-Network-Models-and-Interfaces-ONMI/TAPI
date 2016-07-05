import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ServiceendpointUuid_ExtensionsImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._serviceEndPoint:
            return be.Context._serviceEndPoint[uuid]._extensions
        else:
            raise KeyError('uuid')
