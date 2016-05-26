import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathUuidImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in Context._path:
            return Context._path[uuid]
        else:
            raise KeyError('uuid')
