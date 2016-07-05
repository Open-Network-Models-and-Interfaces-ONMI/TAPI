import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_LinkLink_Uuid_LinkportLocalid_ExtensionsImpl:

    @classmethod
    def get(cls, uuid, link_uuid, localId):
        print 'handling get'
        if uuid in be.Context._topology:
            if link_uuid in be.Context._topology[uuid]._link:
                if localId in be.Context._topology[uuid]._link[link_uuid]._linkPort:
                    return be.Context._topology[uuid]._link[link_uuid]._linkPort[localId]._extensions
                else:
                    raise KeyError('localId')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
