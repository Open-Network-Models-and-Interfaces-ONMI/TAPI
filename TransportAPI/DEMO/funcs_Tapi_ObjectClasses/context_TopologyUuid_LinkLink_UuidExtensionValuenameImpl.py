import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_LinkLink_UuidExtensionValuenameImpl:

    @classmethod
    def get(cls, uuid, link_uuid, valueName):
        print 'handling get'
        if uuid in Context._topology:
            if link_uuid in Context._topology[uuid]._link:
                if valueName in Context._topology[uuid]._link[link_uuid].extension:
                    return Context._topology[uuid]._link[link_uuid].extension[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
