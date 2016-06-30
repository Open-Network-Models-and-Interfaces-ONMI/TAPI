import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ConnectionUuid_ConnectionportImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._connection:
            return be.Context._connection[uuid]._connectionPort
        else:
            raise KeyError('uuid')
