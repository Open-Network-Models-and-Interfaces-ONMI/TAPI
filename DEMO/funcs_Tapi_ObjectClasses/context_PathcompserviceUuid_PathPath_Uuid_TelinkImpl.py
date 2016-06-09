import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_PathPath_Uuid_TelinkImpl:

    @classmethod
    def get(cls, uuid, path_uuid):
        print 'handling get'
        if uuid in Context._pathCompService:
            if path_uuid in Context._pathCompService[uuid]._path:
                return Context._pathCompService[uuid]._path[path_uuid]._telink
            else:
                raise KeyError('path_uuid')
        else:
            raise KeyError('uuid')
