import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathUuid_TelinkLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in Context._path:
            if localId in Context._path[uuid]._telink:
                return Context._path[uuid]._telink[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
