import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalidImpl:

    @classmethod
    def get(cls, uuid, link_uuid, localId):
        print 'handling get'
        if uuid in Context._topology:
            if link_uuid in Context._topology[uuid]._link:
                if localId in Context._topology[uuid]._link[link_uuid]._linkPort:
                    return Context._topology[uuid]._link[link_uuid]._linkPort[localId]
                else:
                    raise KeyError('localId')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
