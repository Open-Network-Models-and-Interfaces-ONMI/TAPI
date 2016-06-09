import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_PathcompserviceUuid_PathPath_UuidLabelValuenameImpl:

    @classmethod
    def get(cls, uuid, path_uuid, valueName):
        print 'handling get'
        if uuid in Context._pathCompService:
            if path_uuid in Context._pathCompService[uuid]._path:
                if valueName in Context._pathCompService[uuid]._path[path_uuid].label:
                    return Context._pathCompService[uuid]._path[path_uuid].label[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('path_uuid')
        else:
            raise KeyError('uuid')
