import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_NodeNode_UuidNameValuenameImpl:

    @classmethod
    def get(cls, uuid, node_uuid, valueName):
        print 'handling get'
        if uuid in be.Context._topology:
            if node_uuid in be.Context._topology[uuid]._node:
                if valueName in be.Context._topology[uuid]._node[node_uuid].name:
                    return be.Context._topology[uuid]._node[node_uuid].name[valueName]
                else:
                    raise KeyError('valueName')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
